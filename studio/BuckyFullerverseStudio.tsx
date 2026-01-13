"use client";

import { motion, AnimatePresence } from 'framer-motion';
import { useState, useEffect } from 'react';
import { NaturalSystemsEngine, LivingEntity, NaturalCycle, AutonomousEvent } from '@/protocols/naturalSystems';
import { AIAssistant } from './AIAssistant';
import { WorldPreview } from './WorldPreview';
import { EntityDesigner } from './EntityDesigner';
import { CycleConfigurator } from './CycleConfigurator';
import { EventCreator } from './EventCreator';

// ============================================================================
// BUCKY FULLERVERSE CREATOR STUDIO
// "Do more with less" - Buckminster Fuller
// 
// Philosophy: The most elegant system is one that generates infinite 
// possibilities from simple, reusable components. Like geodesic domes,
// complex worlds emerge from fundamental patterns.
// ============================================================================

interface WorldConfig {
  name: string;
  description: string;
  theme: 'frontier' | 'cyberpunk' | 'fantasy' | 'scifi' | 'nature' | 'custom';
  entities: LivingEntity[];
  cycles: NaturalCycle[];
  events: AutonomousEvent[];
  heroHost?: {
    name: string;
    personality: string;
    avatar: string;
  };
}

type StudioTab = 'overview' | 'entities' | 'cycles' | 'events' | 'preview' | 'export';

export default function BuckyFullerverseStudio() {
  const [activeTab, setActiveTab] = useState<StudioTab>('overview');
  const [worldConfig, setWorldConfig] = useState<WorldConfig>({
    name: 'My Living World',
    description: 'A self-operating world built on the Natural Systems Protocol',
    theme: 'frontier',
    entities: [],
    cycles: [],
    events: [],
  });
  const [showAI, setShowAI] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [previewEngine, setPreviewEngine] = useState<NaturalSystemsEngine | null>(null);

  // Initialize preview engine when world config changes
  useEffect(() => {
    if (worldConfig.entities.length > 0 || worldConfig.cycles.length > 0) {
      // In production, this would instantiate a live NSP engine
      // For now, we'll create a mock
      console.log('Preview engine would update here with:', worldConfig);
    }
  }, [worldConfig]);

  const tabs = [
    { id: 'overview', name: 'World Overview', icon: '🌍', description: 'Basic settings and theme' },
    { id: 'entities', name: 'Living Entities', icon: '🏛️', description: 'Buildings, characters, landscapes' },
    { id: 'cycles', name: 'Natural Cycles', icon: '🌬️', description: 'Breathing, day/night, seasons' },
    { id: 'events', name: 'Autonomous Events', icon: '🎭', description: 'Stories and happenings' },
    { id: 'preview', name: 'Live Preview', icon: '👁️', description: 'See your world in action' },
    { id: 'export', name: 'Export & Deploy', icon: '🚀', description: 'Generate code and launch' },
  ];

  const themes = [
    { id: 'frontier', name: 'Frontier Outpost', example: 'Like MarkTwainVerse', colors: ['#3d2817', '#d4af37', '#f5e6d3'] },
    { id: 'cyberpunk', name: 'Cyberpunk City', example: 'Neon-lit megacity', colors: ['#0a0e27', '#00d4ff', '#ff006e'] },
    { id: 'fantasy', name: 'Fantasy Realm', example: 'Magical kingdoms', colors: ['#2d1b3d', '#8b5cf6', '#fbbf24'] },
    { id: 'scifi', name: 'Sci-Fi Station', example: 'Space habitats', colors: ['#0f172a', '#06b6d4', '#f0f9ff'] },
    { id: 'nature', name: 'Natural Paradise', example: 'Pristine ecosystems', colors: ['#064e3b', '#10b981', '#d1fae5'] },
    { id: 'custom', name: 'Custom Theme', example: 'Build from scratch', colors: ['#000000', '#ffffff', '#808080'] },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
      {/* Header */}
      <motion.header
        className="border-b border-white/20 backdrop-blur-lg bg-black/30"
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ type: 'spring', damping: 20 }}
      >
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <motion.div
                className="text-5xl"
                animate={{ rotate: [0, 360] }}
                transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
              >
                ⚙️
              </motion.div>
              <div>
                <h1 className="text-3xl font-bold bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text text-transparent">
                  Bucky Fullerverse Creator Studio
                </h1>
                <p className="text-sm text-white/60">
                  "Do more with less" - Build living worlds with Natural Systems Protocol
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button
                className="px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg font-bold transition-colors flex items-center gap-2"
                onClick={() => setShowAI(!showAI)}
              >
                <span>🤖</span>
                <span>AI Assistant</span>
              </button>
              <button className="px-4 py-2 bg-cyan-600 hover:bg-cyan-700 rounded-lg font-bold transition-colors">
                Save Project
              </button>
            </div>
          </div>
        </div>
      </motion.header>

      <div className="flex h-[calc(100vh-80px)]">
        {/* Sidebar - Tab Navigation */}
        <motion.aside
          className="w-72 border-r border-white/20 backdrop-blur-lg bg-black/30 p-4"
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          <div className="space-y-2">
            {tabs.map((tab, index) => (
              <motion.button
                key={tab.id}
                className={`w-full text-left p-4 rounded-lg transition-all ${
                  activeTab === tab.id
                    ? 'bg-gradient-to-r from-cyan-600 to-purple-600 shadow-lg'
                    : 'bg-white/5 hover:bg-white/10'
                }`}
                onClick={() => setActiveTab(tab.id as StudioTab)}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.3 + index * 0.05 }}
              >
                <div className="flex items-center gap-3 mb-1">
                  <span className="text-2xl">{tab.icon}</span>
                  <span className="font-bold">{tab.name}</span>
                </div>
                <p className="text-xs text-white/60 ml-9">{tab.description}</p>
              </motion.button>
            ))}
          </div>

          {/* Quick Stats */}
          <motion.div
            className="mt-6 p-4 bg-white/5 rounded-lg border border-white/10"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.8 }}
          >
            <h3 className="font-bold mb-3 text-sm text-white/80">World Stats</h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-white/60">Entities:</span>
                <span className="font-bold">{worldConfig.entities.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-white/60">Cycles:</span>
                <span className="font-bold">{worldConfig.cycles.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-white/60">Events:</span>
                <span className="font-bold">{worldConfig.events.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-white/60">Theme:</span>
                <span className="font-bold capitalize">{worldConfig.theme}</span>
              </div>
            </div>
          </motion.div>

          {/* Geodesic Inspiration */}
          <motion.div
            className="mt-6 p-4 bg-gradient-to-br from-purple-600/20 to-cyan-600/20 rounded-lg border border-white/20"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.0 }}
          >
            <div className="text-4xl text-center mb-2">🌐</div>
            <p className="text-xs text-center text-white/80 italic">
              "I just invent, then wait until man comes around to needing what I've invented."
            </p>
            <p className="text-xs text-center text-white/60 mt-1">— Buckminster Fuller</p>
          </motion.div>
        </motion.aside>

        {/* Main Content Area */}
        <main className="flex-1 overflow-y-auto p-8">
          <AnimatePresence mode="wait">
            {activeTab === 'overview' && (
              <OverviewTab
                worldConfig={worldConfig}
                setWorldConfig={setWorldConfig}
                themes={themes}
                onAIAssist={() => setShowAI(true)}
              />
            )}
            {activeTab === 'entities' && (
              <EntitiesTab
                worldConfig={worldConfig}
                setWorldConfig={setWorldConfig}
                onAIAssist={() => setShowAI(true)}
              />
            )}
            {activeTab === 'cycles' && (
              <CyclesTab
                worldConfig={worldConfig}
                setWorldConfig={setWorldConfig}
                onAIAssist={() => setShowAI(true)}
              />
            )}
            {activeTab === 'events' && (
              <EventsTab
                worldConfig={worldConfig}
                setWorldConfig={setWorldConfig}
                onAIAssist={() => setShowAI(true)}
              />
            )}
            {activeTab === 'preview' && (
              <PreviewTab worldConfig={worldConfig} />
            )}
            {activeTab === 'export' && (
              <ExportTab worldConfig={worldConfig} />
            )}
          </AnimatePresence>
        </main>
      </div>

      {/* AI Assistant Sidebar */}
      <AIAssistant
        isOpen={showAI}
        onClose={() => setShowAI(false)}
        worldConfig={worldConfig}
        onSuggestion={(suggestion) => {
          // Apply AI suggestion to world config
          setWorldConfig({ ...worldConfig, ...suggestion });
        }}
      />
    </div>
  );
}

// ============================================================================
// OVERVIEW TAB - World basics and theme
// ============================================================================

interface OverviewTabProps {
  worldConfig: WorldConfig;
  setWorldConfig: (config: WorldConfig) => void;
  themes: any[];
  onAIAssist: () => void;
}

function OverviewTab({ worldConfig, setWorldConfig, themes, onAIAssist }: OverviewTabProps) {
  return (
    <motion.div
      key="overview"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div>
        <h2 className="text-3xl font-bold mb-2">World Overview</h2>
        <p className="text-white/60">Define the basics of your living world</p>
      </div>

      {/* World Name & Description */}
      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-bold mb-2">World Name</label>
            <input
              type="text"
              value={worldConfig.name}
              onChange={(e) => setWorldConfig({ ...worldConfig, name: e.target.value })}
              className="w-full px-4 py-3 bg-black/30 border border-white/20 rounded-lg text-white placeholder-white/40 focus:outline-none focus:border-cyan-400"
              placeholder="e.g., MarkTwainVerse, CyberCity 2099"
            />
          </div>

          <div>
            <label className="block text-sm font-bold mb-2">Description</label>
            <textarea
              value={worldConfig.description}
              onChange={(e) => setWorldConfig({ ...worldConfig, description: e.target.value })}
              className="w-full px-4 py-3 bg-black/30 border border-white/20 rounded-lg text-white placeholder-white/40 focus:outline-none focus:border-cyan-400 h-24 resize-none"
              placeholder="Describe your world's purpose and atmosphere..."
            />
          </div>

          <button
            onClick={onAIAssist}
            className="px-4 py-2 bg-purple-600/30 hover:bg-purple-600/50 border border-purple-400/50 rounded-lg text-sm font-bold transition-colors"
          >
            ✨ AI: Enhance Description
          </button>
        </div>
      </div>

      {/* Theme Selection */}
      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-xl font-bold">Choose Theme</h3>
          <button
            onClick={onAIAssist}
            className="px-3 py-1 bg-purple-600/30 border border-purple-400/50 rounded-lg text-xs font-bold"
          >
            🤖 Suggest Theme
          </button>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {themes.map((theme) => (
            <motion.button
              key={theme.id}
              className={`p-4 rounded-lg border-2 transition-all ${
                worldConfig.theme === theme.id
                  ? 'border-cyan-400 bg-cyan-600/20'
                  : 'border-white/20 bg-white/5 hover:border-white/40'
              }`}
              onClick={() => setWorldConfig({ ...worldConfig, theme: theme.id })}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <div className="flex gap-2 mb-2">
                {theme.colors.map((color: string, i: number) => (
                  <div
                    key={i}
                    className="w-6 h-6 rounded-full border border-white/30"
                    style={{ backgroundColor: color }}
                  />
                ))}
              </div>
              <div className="font-bold text-left mb-1">{theme.name}</div>
              <div className="text-xs text-white/60 text-left">{theme.example}</div>
            </motion.button>
          ))}
        </div>
      </div>

      {/* Hero Host Configuration */}
      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
        <div className="flex justify-between items-center mb-4">
          <div>
            <h3 className="text-xl font-bold">Hero Host (Optional)</h3>
            <p className="text-sm text-white/60">Add an AI guide like Mark Twain</p>
          </div>
          <button
            onClick={onAIAssist}
            className="px-3 py-1 bg-purple-600/30 border border-purple-400/50 rounded-lg text-xs font-bold"
          >
            🤖 Generate Host
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-bold mb-2">Host Name</label>
            <input
              type="text"
              value={worldConfig.heroHost?.name || ''}
              onChange={(e) =>
                setWorldConfig({
                  ...worldConfig,
                  heroHost: { ...worldConfig.heroHost!, name: e.target.value },
                })
              }
              className="w-full px-4 py-2 bg-black/30 border border-white/20 rounded-lg"
              placeholder="e.g., Mark Twain, Ada Lovelace, Carl Sagan"
            />
          </div>

          <div>
            <label className="block text-sm font-bold mb-2">Personality Traits</label>
            <input
              type="text"
              value={worldConfig.heroHost?.personality || ''}
              onChange={(e) =>
                setWorldConfig({
                  ...worldConfig,
                  heroHost: { ...worldConfig.heroHost!, personality: e.target.value },
                })
              }
              className="w-full px-4 py-2 bg-black/30 border border-white/20 rounded-lg"
              placeholder="e.g., Witty, wise, storyteller, adventurous"
            />
          </div>
        </div>
      </div>

      {/* Quick Start Templates */}
      <div className="bg-gradient-to-br from-purple-600/20 to-cyan-600/20 rounded-lg p-6 border border-white/20">
        <h3 className="text-xl font-bold mb-4">🚀 Quick Start Templates</h3>
        <div className="grid md:grid-cols-2 gap-3">
          <button className="p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
            <div className="font-bold mb-1">📖 MarkTwainVerse Clone</div>
            <div className="text-xs text-white/60">Start with the full frontier experience</div>
          </button>
          <button className="p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
            <div className="font-bold mb-1">🌱 Minimal Garden</div>
            <div className="text-xs text-white/60">Simple peaceful world, easy to customize</div>
          </button>
          <button className="p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
            <div className="font-bold mb-1">🏙️ Cyberpunk Megacity</div>
            <div className="text-xs text-white/60">Neon-lit urban sprawl template</div>
          </button>
          <button className="p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
            <div className="font-bold mb-1">⚡ Blank Canvas</div>
            <div className="text-xs text-white/60">Start from absolute scratch</div>
          </button>
        </div>
      </div>
    </motion.div>
  );
}

// ============================================================================
// ENTITIES TAB - Living entities designer
// ============================================================================

interface EntitiesTabProps {
  worldConfig: WorldConfig;
  setWorldConfig: (config: WorldConfig) => void;
  onAIAssist: () => void;
}

function EntitiesTab({ worldConfig, setWorldConfig, onAIAssist }: EntitiesTabProps) {
  const [showEntityForm, setShowEntityForm] = useState(false);

  return (
    <motion.div
      key="entities"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-3xl font-bold mb-2">Living Entities</h2>
          <p className="text-white/60">Buildings, characters, and landscapes that breathe</p>
        </div>
        <div className="flex gap-3">
          <button
            onClick={onAIAssist}
            className="px-4 py-2 bg-purple-600/30 border border-purple-400/50 rounded-lg font-bold"
          >
            🤖 AI: Generate Entities
          </button>
          <button
            onClick={() => setShowEntityForm(true)}
            className="px-4 py-2 bg-cyan-600 hover:bg-cyan-700 rounded-lg font-bold"
          >
            + Add Entity
          </button>
        </div>
      </div>

      {/* Entity Gallery */}
      {worldConfig.entities.length === 0 ? (
        <div className="bg-white/5 backdrop-blur-lg rounded-lg p-12 border border-white/10 text-center">
          <div className="text-6xl mb-4">🏛️</div>
          <h3 className="text-xl font-bold mb-2">No Entities Yet</h3>
          <p className="text-white/60 mb-6">Entities are the living parts of your world - buildings, characters, landscapes.</p>
          <div className="flex gap-3 justify-center">
            <button
              onClick={() => setShowEntityForm(true)}
              className="px-6 py-3 bg-cyan-600 hover:bg-cyan-700 rounded-lg font-bold"
            >
              Create First Entity
            </button>
            <button
              onClick={onAIAssist}
              className="px-6 py-3 bg-purple-600/30 border border-purple-400/50 rounded-lg font-bold"
            >
              🤖 AI Generate
            </button>
          </div>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {worldConfig.entities.map((entity, index) => (
            <motion.div
              key={entity.id}
              className="bg-white/5 backdrop-blur-lg rounded-lg p-4 border border-white/10 hover:border-cyan-400/50 transition-colors"
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: index * 0.05 }}
              whileHover={{ scale: 1.02 }}
            >
              <div className="flex justify-between items-start mb-3">
                <div className="text-3xl">
                  {entity.type === 'character' ? '🤠' :
                   entity.type === 'building' ? '🏛️' :
                   entity.type === 'landscape' ? '🌄' : '⚙️'}
                </div>
                <div className="text-xs px-2 py-1 bg-cyan-600/30 rounded capitalize">
                  {entity.type}
                </div>
              </div>
              <h4 className="font-bold mb-2">{entity.id}</h4>
              <div className="text-xs space-y-1 text-white/60">
                <div>Energy: {(entity.energy * 100).toFixed(0)}%</div>
                <div>Mood: {entity.state.mood}</div>
                <div>Behaviors: {entity.behaviors.length}</div>
              </div>
              <div className="mt-3 flex gap-2">
                <button className="flex-1 px-3 py-1 bg-white/10 hover:bg-white/20 rounded text-xs">
                  Edit
                </button>
                <button className="px-3 py-1 bg-red-600/30 hover:bg-red-600/50 rounded text-xs">
                  Delete
                </button>
              </div>
            </motion.div>
          ))}
        </div>
      )}

      {/* Entity Templates */}
      <div className="bg-gradient-to-br from-purple-600/20 to-cyan-600/20 rounded-lg p-6 border border-white/20">
        <h3 className="text-xl font-bold mb-4">🎨 Entity Templates</h3>
        <div className="grid md:grid-cols-4 gap-3">
          {[
            { icon: '🤠', name: 'Character', type: 'character' },
            { icon: '🏛️', name: 'Building', type: 'building' },
            { icon: '🌄', name: 'Landscape', type: 'landscape' },
            { icon: '⚙️', name: 'System', type: 'system' },
          ].map((template) => (
            <button
              key={template.type}
              className="p-4 bg-white/10 rounded-lg hover:bg-white/20 transition-colors"
              onClick={() => setShowEntityForm(true)}
            >
              <div className="text-3xl mb-2">{template.icon}</div>
              <div className="font-bold text-sm">{template.name}</div>
            </button>
          ))}
        </div>
      </div>
    </motion.div>
  );
}

// ============================================================================
// CYCLES TAB - Natural cycles configurator
// ============================================================================

interface CyclesTabProps {
  worldConfig: WorldConfig;
  setWorldConfig: (config: WorldConfig) => void;
  onAIAssist: () => void;
}

function CyclesTab({ worldConfig, setWorldConfig, onAIAssist }: CyclesTabProps) {
  return (
    <motion.div
      key="cycles"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-3xl font-bold mb-2">Natural Cycles</h2>
          <p className="text-white/60">The rhythms that make your world breathe</p>
        </div>
        <button
          onClick={onAIAssist}
          className="px-4 py-2 bg-purple-600/30 border border-purple-400/50 rounded-lg font-bold"
        >
          🤖 AI: Optimize Cycles
        </button>
      </div>

      {/* Essential Cycles - Pre-configured */}
      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
        <h3 className="text-xl font-bold mb-4">Essential Cycles (Recommended)</h3>
        <div className="space-y-3">
          {[
            { id: 'breathing', name: 'Breathing Cycle', duration: '6 seconds', icon: '🌬️', description: 'Subtle animation, the world pulses' },
            { id: 'dayNight', name: 'Day/Night Cycle', duration: '2 minutes (demo) / 24 hours (production)', icon: '🌅', description: 'Lighting and activity changes' },
            { id: 'seasons', name: 'Seasonal Cycle', duration: '28 minutes (demo) / 365 days (production)', icon: '🍂', description: 'Long-term aesthetic shifts' },
          ].map((cycle) => (
            <div
              key={cycle.id}
              className="flex items-center gap-4 p-4 bg-white/5 rounded-lg border border-white/10"
            >
              <div className="text-3xl">{cycle.icon}</div>
              <div className="flex-1">
                <div className="font-bold">{cycle.name}</div>
                <div className="text-sm text-white/60">{cycle.description}</div>
                <div className="text-xs text-cyan-400 mt-1">Duration: {cycle.duration}</div>
              </div>
              <label className="flex items-center gap-2">
                <input type="checkbox" defaultChecked className="w-5 h-5" />
                <span className="text-sm">Enabled</span>
              </label>
            </div>
          ))}
        </div>
      </div>

      {/* Custom Cycles */}
      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-xl font-bold">Custom Cycles</h3>
          <button className="px-4 py-2 bg-cyan-600 rounded-lg font-bold text-sm">
            + Add Custom Cycle
          </button>
        </div>
        <p className="text-sm text-white/60">
          Create your own cycles - tides, weather patterns, economic fluctuations, anything that should change over time.
        </p>
      </div>
    </motion.div>
  );
}

// ============================================================================
// EVENTS TAB - Autonomous events creator
// ============================================================================

interface EventsTabProps {
  worldConfig: WorldConfig;
  setWorldConfig: (config: WorldConfig) => void;
  onAIAssist: () => void;
}

function EventsTab({ worldConfig, setWorldConfig, onAIAssist }: EventsTabProps) {
  return (
    <motion.div
      key="events"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-3xl font-bold mb-2">Autonomous Events</h2>
          <p className="text-white/60">Things that happen without user input</p>
        </div>
        <button
          onClick={onAIAssist}
          className="px-4 py-2 bg-purple-600/30 border border-purple-400/50 rounded-lg font-bold"
        >
          🤖 AI: Generate Events
        </button>
      </div>

      <div className="bg-white/5 backdrop-blur-lg rounded-lg p-12 border border-white/10 text-center">
        <div className="text-6xl mb-4">🎭</div>
        <h3 className="text-xl font-bold mb-2">Event System</h3>
        <p className="text-white/60 mb-6">
          Events are the stories your world tells itself. They can be time-based, conditional, or random.
        </p>
        <button
          onClick={onAIAssist}
          className="px-6 py-3 bg-purple-600 hover:bg-purple-700 rounded-lg font-bold"
        >
          🤖 AI: Create Event Schedule
        </button>
      </div>
    </motion.div>
  );
}

// ============================================================================
// PREVIEW TAB - Live world preview
// ============================================================================

interface PreviewTabProps {
  worldConfig: WorldConfig;
}

function PreviewTab({ worldConfig }: PreviewTabProps) {
  return (
    <motion.div
      key="preview"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div>
        <h2 className="text-3xl font-bold mb-2">Live Preview</h2>
        <p className="text-white/60">See your world operating in real-time</p>
      </div>

      <div className="bg-black/50 backdrop-blur-lg rounded-lg p-8 border border-white/10 min-h-[600px] flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4 animate-pulse">🌍</div>
          <h3 className="text-xl font-bold mb-2">Preview Engine</h3>
          <p className="text-white/60 mb-4">
            Your world "{worldConfig.name}" will render here
          </p>
          <button className="px-6 py-3 bg-cyan-600 hover:bg-cyan-700 rounded-lg font-bold">
            ▶️ Start Preview
          </button>
        </div>
      </div>
    </motion.div>
  );
}

// ============================================================================
// EXPORT TAB - Generate code and deploy
// ============================================================================

interface ExportTabProps {
  worldConfig: WorldConfig;
}

function ExportTab({ worldConfig }: ExportTabProps) {
  return (
    <motion.div
      key="export"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="space-y-6"
    >
      <div>
        <h2 className="text-3xl font-bold mb-2">Export & Deploy</h2>
        <p className="text-white/60">Generate production-ready code</p>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
          <h3 className="text-xl font-bold mb-4">📦 Export Options</h3>
          <div className="space-y-3">
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">Next.js Project</div>
              <div className="text-xs text-white/60">Full Next.js app with NSP integrated</div>
            </button>
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">React Component</div>
              <div className="text-xs text-white/60">Standalone React component</div>
            </button>
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">NSP JSON Config</div>
              <div className="text-xs text-white/60">Pure data, import anywhere</div>
            </button>
          </div>
        </div>

        <div className="bg-white/5 backdrop-blur-lg rounded-lg p-6 border border-white/10">
          <h3 className="text-xl font-bold mb-4">🚀 Deploy Options</h3>
          <div className="space-y-3">
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">Vercel</div>
              <div className="text-xs text-white/60">One-click deploy to Vercel</div>
            </button>
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">Syntheverse Cloud</div>
              <div className="text-xs text-white/60">Deploy to Syntheverse hosting</div>
            </button>
            <button className="w-full p-4 bg-white/10 rounded-lg text-left hover:bg-white/20 transition-colors">
              <div className="font-bold mb-1">Download ZIP</div>
              <div className="text-xs text-white/60">Self-host anywhere</div>
            </button>
          </div>
        </div>
      </div>

      <div className="bg-gradient-to-br from-purple-600/20 to-cyan-600/20 rounded-lg p-6 border border-white/20">
        <h3 className="text-xl font-bold mb-4">✨ Ready to Launch!</h3>
        <p className="text-white/80 mb-6">
          Your world "{worldConfig.name}" is configured with {worldConfig.entities.length} entities, 
          {worldConfig.cycles.length} cycles, and {worldConfig.events.length} events.
        </p>
        <button className="w-full py-4 bg-gradient-to-r from-cyan-600 to-purple-600 hover:from-cyan-700 hover:to-purple-700 rounded-lg font-bold text-lg">
          🚀 Generate & Export World
        </button>
      </div>
    </motion.div>
  );
}


