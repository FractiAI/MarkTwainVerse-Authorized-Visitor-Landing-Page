"use client";

import { motion, AnimatePresence } from 'framer-motion';
import { useState, useRef, useEffect } from 'react';
import { WorldConfig } from './BuckyFullerverseStudio';

// ============================================================================
// AI ASSISTANT - Groq-Powered World Building Helper
// "The most efficient way to build worlds: conversation with AI"
// ============================================================================

interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: number;
  suggestions?: any;
}

interface AIAssistantProps {
  isOpen: boolean;
  onClose: () => void;
  worldConfig: any;
  onSuggestion: (suggestion: any) => void;
}

export function AIAssistant({ isOpen, onClose, worldConfig, onSuggestion }: AIAssistantProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: `Howdy, world builder! I'm your AI assistant, powered by Groq for lightning-fast help. 

I can help you:
• Generate entities, cycles, and events
• Suggest themes and aesthetics  
• Optimize your world's performance
• Write character personalities
• Create storylines and narratives
• Debug Natural Systems Protocol issues

What would you like to build today?`,
      timestamp: Date.now(),
    },
  ]);
  const [input, setInput] = useState('');
  const [isThinking, setIsThinking] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const quickPrompts = [
    "Generate 5 frontier entities for me",
    "Create a day/night cycle optimized for 2-minute demos",
    "Suggest autonomous events for a cyberpunk world",
    "Write a personality for a wise robot character",
    "Help me theme this world like a coral reef ecosystem",
    "What entities would work well together?",
  ];

  const sendMessage = async (message: string) => {
    if (!message.trim()) return;

    // Add user message
    const userMessage: Message = {
      role: 'user',
      content: message,
      timestamp: Date.now(),
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsThinking(true);

    try {
      // Call Groq API
      const response = await fetch('/api/ai-assist', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message,
          worldConfig,
          conversationHistory: messages.slice(-10), // Last 10 messages for context
        }),
      });

      const data = await response.json();

      // Add assistant response
      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response,
        timestamp: Date.now(),
        suggestions: data.suggestions, // Structured data to apply
      };
      setMessages((prev) => [...prev, assistantMessage]);

    } catch (error) {
      console.error('AI Assistant error:', error);
      const errorMessage: Message = {
        role: 'assistant',
        content: "I'm having trouble connecting right now. But let me give you a manual suggestion based on common patterns...",
        timestamp: Date.now(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsThinking(false);
    }
  };

  const applySuggestion = (suggestion: any) => {
    onSuggestion(suggestion);
    const confirmMessage: Message = {
      role: 'assistant',
      content: "✓ Applied! Your world has been updated. Anything else you'd like to add?",
      timestamp: Date.now(),
    };
    setMessages((prev) => [...prev, confirmMessage]);
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            className="fixed inset-0 bg-black/70 z-40 backdrop-blur-sm"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
          />

          {/* Assistant Panel */}
          <motion.div
            className="fixed right-0 top-0 bottom-0 w-full md:w-[500px] bg-gradient-to-br from-purple-900/95 to-slate-900/95 backdrop-blur-xl border-l-4 border-purple-400 z-50 flex flex-col"
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25 }}
          >
            {/* Header */}
            <div className="p-6 border-b border-white/20">
              <div className="flex justify-between items-center">
                <div>
                  <h2 className="text-2xl font-bold flex items-center gap-3">
                    <motion.span
                      animate={{ rotate: [0, 10, -10, 0] }}
                      transition={{ duration: 2, repeat: Infinity }}
                    >
                      🤖
                    </motion.span>
                    AI Assistant
                  </h2>
                  <p className="text-sm text-white/60">Powered by Groq ⚡</p>
                </div>
                <button
                  className="text-3xl hover:text-purple-400 transition-colors"
                  onClick={onClose}
                >
                  ×
                </button>
              </div>
            </div>

            {/* World Context Chip */}
            <div className="px-6 py-3 bg-black/30 border-b border-white/10">
              <div className="text-xs text-white/60 mb-1">Current World:</div>
              <div className="font-bold text-sm">
                {worldConfig.name || 'Untitled World'} · {worldConfig.theme} theme
              </div>
              <div className="text-xs text-white/60 mt-1">
                {worldConfig.entities?.length || 0} entities · {worldConfig.cycles?.length || 0} cycles · {worldConfig.events?.length || 0} events
              </div>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto p-6 space-y-4">
              {messages.map((message, index) => (
                <motion.div
                  key={index}
                  className={`flex gap-3 ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                >
                  {message.role === 'assistant' && (
                    <div className="text-2xl">🤖</div>
                  )}
                  <div
                    className={`max-w-[80%] rounded-lg p-4 ${
                      message.role === 'user'
                        ? 'bg-cyan-600 text-white'
                        : 'bg-white/10 text-white'
                    }`}
                  >
                    <div className="whitespace-pre-wrap text-sm">{message.content}</div>
                    
                    {message.suggestions && (
                      <div className="mt-3 pt-3 border-t border-white/20">
                        <button
                          className="px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg text-sm font-bold transition-colors"
                          onClick={() => applySuggestion(message.suggestions)}
                        >
                          ✨ Apply Suggestion
                        </button>
                      </div>
                    )}
                    
                    <div className="text-[10px] text-white/40 mt-2">
                      {new Date(message.timestamp).toLocaleTimeString()}
                    </div>
                  </div>
                  {message.role === 'user' && (
                    <div className="text-2xl">👤</div>
                  )}
                </motion.div>
              ))}

              {isThinking && (
                <motion.div
                  className="flex gap-3 justify-start"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                >
                  <div className="text-2xl">🤖</div>
                  <div className="bg-white/10 rounded-lg p-4">
                    <motion.div
                      className="flex gap-2"
                      animate={{ opacity: [0.5, 1, 0.5] }}
                      transition={{ duration: 1.5, repeat: Infinity }}
                    >
                      <div className="w-2 h-2 bg-purple-400 rounded-full"></div>
                      <div className="w-2 h-2 bg-cyan-400 rounded-full"></div>
                      <div className="w-2 h-2 bg-purple-400 rounded-full"></div>
                    </motion.div>
                  </div>
                </motion.div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Quick Prompts */}
            <div className="px-6 py-3 border-t border-white/10 overflow-x-auto">
              <div className="text-xs text-white/60 mb-2">Quick Prompts:</div>
              <div className="flex gap-2 pb-2">
                {quickPrompts.map((prompt, index) => (
                  <button
                    key={index}
                    className="px-3 py-1 bg-white/10 hover:bg-white/20 rounded-full text-xs whitespace-nowrap transition-colors"
                    onClick={() => sendMessage(prompt)}
                  >
                    {prompt}
                  </button>
                ))}
              </div>
            </div>

            {/* Input */}
            <div className="p-6 border-t border-white/20 bg-black/30">
              <div className="flex gap-3">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && sendMessage(input)}
                  placeholder="Ask me anything about your world..."
                  className="flex-1 px-4 py-3 bg-white/10 border border-white/20 rounded-lg text-white placeholder-white/40 focus:outline-none focus:border-purple-400"
                  disabled={isThinking}
                />
                <button
                  className="px-6 py-3 bg-purple-600 hover:bg-purple-700 rounded-lg font-bold transition-colors disabled:opacity-50"
                  onClick={() => sendMessage(input)}
                  disabled={isThinking || !input.trim()}
                >
                  Send
                </button>
              </div>
              <div className="text-xs text-white/40 mt-2 text-center">
                Powered by Groq · Ultra-fast AI inference
              </div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}

// ============================================================================
// MOCK AI RESPONSES (for when API not available)
// ============================================================================

export function generateMockResponse(message: string, worldConfig: any): any {
  const lowerMessage = message.toLowerCase();

  if (lowerMessage.includes('entities') || lowerMessage.includes('generate')) {
    return {
      response: `Great! Based on your ${worldConfig.theme} theme, here are 5 entities I'd suggest:

1. **Frontier Town Hall** (Building)
   - Central gathering point
   - Energy: 0.9, Mood: Active
   - Behaviors: Pulse with visitor activity, glow at night

2. **Wandering Storyteller** (Character)
   - Roams between locations
   - Energy: 0.8, Mood: Thriving
   - Behaviors: Tell random stories, greet newcomers

3. **Living Forest** (Landscape)
   - Breathing, growing ecosystem
   - Energy: 1.0, Mood: Thriving
   - Behaviors: Seasonal changes, wildlife sounds

4. **Market Square** (System)
   - Economic activity hub
   - Energy: 0.75, Mood: Active
   - Behaviors: Busy during day, quiet at night

5. **Ancient Monument** (Building)
   - Historical landmark
   - Energy: 0.6, Mood: Resting
   - Behaviors: Subtle glow, wisdom aura

Would you like me to add these to your world?`,
      suggestions: {
        entities: [
          {
            id: 'frontier-town-hall',
            type: 'building',
            energy: 0.9,
            // ... full entity config
          },
          // ... other entities
        ],
      },
    };
  }

  if (lowerMessage.includes('cycle') || lowerMessage.includes('day') || lowerMessage.includes('night')) {
    return {
      response: `For a 2-minute demo cycle, I recommend:

**Optimized Day/Night Cycle:**
- Duration: 120,000ms (2 minutes)
- Dawn: 0-0.25 (30 seconds) - Gradual brightening
- Day: 0.25-0.75 (60 seconds) - Full activity
- Dusk: 0.75-0.9 (18 seconds) - Beautiful sunset
- Night: 0.9-1.0 (12 seconds) - Starry sky

This gives visitors enough time to experience both day and night without waiting too long. The longer day period ensures most visitors see your world in full light.

Shall I apply this cycle configuration?`,
      suggestions: {
        cycles: [
          {
            name: 'demo-day-night',
            duration: 120000,
            // ... full cycle config
          },
        ],
      },
    };
  }

  // Default response
  return {
    response: `I'm here to help! I can assist with:

• **Entities**: Create buildings, characters, landscapes
• **Cycles**: Set up breathing, day/night, seasons
• **Events**: Design autonomous happenings
• **Themes**: Choose aesthetics and colors
• **Optimization**: Make your world run smoothly

What specific aspect would you like help with?`,
  };
}

