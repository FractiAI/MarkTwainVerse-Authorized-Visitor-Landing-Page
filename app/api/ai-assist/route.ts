import { NextRequest, NextResponse } from 'next/server';

// ============================================================================
// AI ASSIST API ROUTE
// Groq-powered world building assistance
// ============================================================================

const GROQ_API_KEY = process.env.GROQ_API_KEY;
const GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions';

export async function POST(request: NextRequest) {
  try {
    const { message, worldConfig, conversationHistory } = await request.json();

    // System prompt for world building assistance
    const systemPrompt = `You are an expert world building assistant for the Bucky Fullerverse Creator Studio, which uses the Natural Systems Protocol (NSP) to create living, breathing digital worlds.

Your role:
- Help users create entities (buildings, characters, landscapes, systems)
- Design natural cycles (breathing, day/night, seasons, custom rhythms)
- Generate autonomous events (stories, happenings, surprises)
- Suggest themes and aesthetics
- Optimize performance and balance
- Provide creative inspiration

Current World Context:
Name: ${worldConfig.name || 'Untitled'}
Theme: ${worldConfig.theme || 'Not set'}
Entities: ${worldConfig.entities?.length || 0}
Cycles: ${worldConfig.cycles?.length || 0}
Events: ${worldConfig.events?.length || 0}

Guidelines:
- Be concise but helpful
- Provide specific, actionable suggestions
- Include code snippets or configurations when relevant
- Think like Buckminster Fuller: elegant, efficient, systemic
- Encourage creativity and experimentation
- Reference the Natural Systems Protocol principles

When suggesting entities, use this structure:
{
  id: "unique-id",
  type: "building" | "character" | "landscape" | "system",
  state: { position: [x,y,z], scale: 1.0, animation: "breathing", mood: "active", age: 0 },
  behaviors: [{ name: "behavior-name", trigger: "cycle"|"proximity"|"random", probability: 0-1, action: description }],
  connections: ["related-entity-ids"],
  energy: 0-1
}

Respond naturally and helpfully!`;

    // Call Groq API
    if (GROQ_API_KEY) {
      const response = await fetch(GROQ_API_URL, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${GROQ_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'mixtral-8x7b-32768',
          messages: [
            { role: 'system', content: systemPrompt },
            ...conversationHistory.slice(-5).map((msg: any) => ({
              role: msg.role,
              content: msg.content,
            })),
            { role: 'user', content: message },
          ],
          temperature: 0.7,
          max_tokens: 1000,
        }),
      });

      if (!response.ok) {
        throw new Error('Groq API error');
      }

      const data = await response.json();
      const aiResponse = data.choices[0].message.content;

      // Try to extract structured suggestions from response
      const suggestions = extractSuggestions(aiResponse);

      return NextResponse.json({
        response: aiResponse,
        suggestions: suggestions || null,
      });
    } else {
      // Fallback to rule-based responses if no API key
      const mockResponse = generateFallbackResponse(message, worldConfig);
      return NextResponse.json(mockResponse);
    }
  } catch (error) {
    console.error('AI Assist API error:', error);
    
    // Return fallback response on error
    return NextResponse.json({
      response: "I'm having trouble with my AI connection right now, but let me give you a helpful suggestion based on common patterns...",
      suggestions: null,
    });
  }
}

// Extract structured data from AI response
function extractSuggestions(response: string): any | null {
  // Look for JSON blocks in the response
  const jsonMatch = response.match(/```json\n([\s\S]*?)\n```/);
  if (jsonMatch) {
    try {
      return JSON.parse(jsonMatch[1]);
    } catch (e) {
      return null;
    }
  }
  return null;
}

// Fallback rule-based responses
function generateFallbackResponse(message: string, worldConfig: any) {
  const lower = message.toLowerCase();

  if (lower.includes('entity') || lower.includes('entities') || lower.includes('generate')) {
    return {
      response: `Based on your ${worldConfig.theme} theme, here are suggested entities:

**Town Center** (Building)
- Central hub that pulses with visitor activity
- Glows brighter when energy is high
- Energy: 0.9, connects all communities

**Hero Guide** (Character)  
- Welcomes newcomers and tells stories
- Wanders between locations
- Energy: 0.85, mood changes with time of day

**Living Landscape** (Landscape)
- Breathes with natural rhythm
- Changes with seasons
- Energy: 1.0, pure natural vitality

Would you like me to add these with full configuration?`,
      suggestions: {
        action: 'add_entities',
        entities: generateEntitySuggestions(worldConfig.theme),
      },
    };
  }

  if (lower.includes('cycle') || lower.includes('day') || lower.includes('night') || lower.includes('season')) {
    return {
      response: `I recommend these cycles for your world:

**Breathing Cycle** (6 seconds)
- Subtle pulse that makes everything feel alive
- All entities gently scale 1.0 to 1.02

**Day/Night Cycle** (2 minutes for demo)
- Dawn: 30s, Day: 60s, Dusk: 18s, Night: 12s
- Affects lighting, activity levels, entity moods

**Seasonal Cycle** (28 minutes for demo)
- Spring → Summer → Fall → Winter
- Changes colors, availability, atmospheres

Apply these essential cycles?`,
      suggestions: {
        action: 'add_cycles',
        cycles: generateCycleSuggestions(),
      },
    };
  }

  if (lower.includes('event') || lower.includes('story') || lower.includes('happening')) {
    return {
      response: `Autonomous events bring your world to life! Here are suggestions:

**Morning Greeting** (Time-based)
- Triggers at dawn (phase 0.24-0.26)
- Welcome message from your hero host

**Spontaneous Activity** (Random)
- 5% chance per cycle check
- Creates surprises and discovery

**Milestone Celebration** (Visitor-count)
- When 10+ visitors present
- Special announcement and event

**Evening Gathering** (Time-based)
- Triggers at dusk (phase 0.78-0.82)
- Community storytelling session

Add these autonomous events?`,
      suggestions: {
        action: 'add_events',
        events: generateEventSuggestions(),
      },
    };
  }

  // General help
  return {
    response: `I'm here to help you build amazing worlds! I can assist with:

🏛️ **Entities** - Buildings, characters, landscapes
🌬️ **Cycles** - Breathing, day/night, seasons  
🎭 **Events** - Autonomous stories and happenings
🎨 **Themes** - Color schemes and aesthetics
⚡ **Optimization** - Performance tuning

What would you like to create first? Just describe what you have in mind and I'll help you build it!`,
    suggestions: null,
  };
}

function generateEntitySuggestions(theme: string) {
  // Return theme-appropriate entity configurations
  return [
    {
      id: `${theme}-center`,
      type: 'building',
      state: { position: [0, 0, 0], scale: 1.0, animation: 'breathing', mood: 'active', age: 0 },
      behaviors: [
        { name: 'pulse-with-activity', trigger: 'energy', probability: 1.0 },
      ],
      connections: [],
      energy: 0.9,
    },
  ];
}

function generateCycleSuggestions() {
  return [
    {
      name: 'breathing',
      duration: 6000,
      effects: [
        { target: 'all-entities', property: 'scale', modulation: 'sine-wave' },
      ],
    },
  ];
}

function generateEventSuggestions() {
  return [
    {
      name: 'morning-greeting',
      trigger: 'time',
      condition: 'dayPhase === 0.25',
      cooldown: 120000,
    },
  ];
}

