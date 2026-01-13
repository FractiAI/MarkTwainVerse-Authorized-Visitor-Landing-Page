"use client";

import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import {
  useNaturalSystems,
  useDayNightCycle,
  useMarkTwainState,
  useWorldEnergy,
  useAutonomousEvents,
} from '@/components/NaturalSystemsProvider';
import { mainMenu } from '@/data/content';

export default function Home() {
  const { worldContext, interactWithEntity, isAwake } = useNaturalSystems();
  const dayPhase = useDayNightCycle();
  const markTwain = useMarkTwainState();
  const worldEnergy = useWorldEnergy();
  const recentEvents = useAutonomousEvents(3);
  
  const [selectedSection, setSelectedSection] = useState<string | null>(null);
  const [showWelcome, setShowWelcome] = useState(true);

  // Get sky gradient based on day phase
  const getSkyClass = (phase: number): string => {
    if (phase < 0.25) return 'sky-dawn';
    if (phase < 0.75) return 'sky-day';
    if (phase < 0.9) return 'sky-dusk';
    return 'sky-night';
  };

  // Get time of day label
  const getTimeOfDay = (phase: number): string => {
    if (phase < 0.25) return 'Dawn';
    if (phase < 0.5) return 'Morning';
    if (phase < 0.75) return 'Afternoon';
    if (phase < 0.9) return 'Dusk';
    return 'Night';
  };

  if (!isAwake || !worldContext) {
    return (
      <div className="world-loading">
        <div className="loading-spinner"></div>
        <h2 className="heading-md">MarkTwainVerse Awakening...</h2>
        <p className="body-text">The Natural Systems Protocol is initializing</p>
      </div>
    );
  }

  return (
    <main className="min-h-screen relative overflow-hidden">
      {/* AlexandrevonHumboldtverse Expedition Portal - Nested NSPFRP Node */}
      <motion.a 
        href="/alexandrevonhumboldtverse"
        className="expedition-portal-card"
        initial={{ opacity: 0, x: -100 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 1, delay: 0.5 }}
        whileHover={{ scale: 1.05, x: 10 }}
        title="Join Alexander von Humboldt's Guided Expedition through the Natural Systems Protocol"
      >
        <div className="expedition-icon">🌿🔬</div>
        <div className="expedition-content">
          <div className="expedition-title">AlexandrevonHumboldtverse</div>
          <div className="expedition-subtitle">Scientific Expedition</div>
          <div className="expedition-description">
            Hero Host Guided Tour: Discover the NSPFRP black hole engine through Alexander von Humboldt's eyes
          </div>
          <div className="expedition-badge">
            <span className="badge-pulse">●</span> LIVE EXPEDITION
          </div>
        </div>
        <div className="expedition-arrow">→</div>
      </motion.a>

      {/* Animated Sky Background - Tied to Day/Night Cycle */}
      <motion.div
        className={`fixed inset-0 -z-10 ${getSkyClass(dayPhase)}`}
        animate={{
          opacity: [0.7, 0.9, 0.7],
        }}
        transition={{
          duration: 6,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      {/* Starfield at Night */}
      {dayPhase > 0.75 || dayPhase < 0.25 ? (
        <div className="fixed inset-0 -z-5 opacity-50">
          {[...Array(100)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-white rounded-full"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                opacity: [0.3, 1, 0.3],
                scale: [1, 1.5, 1],
              }}
              transition={{
                duration: 2 + Math.random() * 3,
                repeat: Infinity,
                delay: Math.random() * 5,
              }}
            />
          ))}
        </div>
      ) : null}

      {/* Main Content Container */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 py-8">
        {/* World Status Bar */}
        <motion.div
          className="frontier-card mb-8 breathing-glow"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <div className="flex flex-wrap justify-between items-center gap-4">
            <div>
              <h3 className="text-lg font-bold text-frontier-gold">
                🌍 Syntheverse Frontier - {getTimeOfDay(dayPhase)}
              </h3>
              <p className="text-sm text-frontier-tan">
                Time: {Math.floor(dayPhase * 24)}:{Math.floor((dayPhase * 24 % 1) * 60).toString().padStart(2, '0')} | 
                Energy: {(worldEnergy * 100).toFixed(0)}% | 
                Mood: {worldContext.dominantMood}
              </p>
            </div>
            <div className="flex gap-4 items-center">
              <div className="synth-glow font-bold">
                🟢 {worldContext.visitorCount} Visitors
              </div>
              <motion.div
                className="pulse-energy px-4 py-2 bg-synth-primary/20 rounded-lg"
                animate={{ scale: [1, 1.05, 1] }}
                transition={{ duration: 3, repeat: Infinity }}
              >
                Natural Systems Protocol: ACTIVE
              </motion.div>
            </div>
          </div>
        </motion.div>

        {/* Welcome Section with Mark Twain */}
        {showWelcome && (
          <motion.div
            className="hero-host-card mb-8 world-awakening"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1.5, ease: "easeOut" }}
          >
            <div className="flex flex-col md:flex-row gap-6 items-start">
              {/* Mark Twain Avatar */}
              <motion.div
                className={`flex-shrink-0 w-32 h-32 rounded-full bg-frontier-gold/30 border-4 border-frontier-gold flex items-center justify-center text-6xl ${
                  markTwain?.state.mood === 'thriving' ? 'entity-thriving' : ''
                }`}
                onClick={() => interactWithEntity('hero-host-mark-twain')}
                whileHover={{ scale: 1.1, rotate: 5 }}
                whileTap={{ scale: 0.95 }}
                style={{ cursor: 'pointer' }}
              >
                🤠
              </motion.div>

              {/* Welcome Message */}
              <div className="flex-1">
                <h1 className="heading-xl mb-4">
                  Welcome to the MarkTwainVerse
                </h1>
                <div className="twain-quote">
                  Well, howdy there, friend! Mark Twain at your service. You've just crossed a mighty peculiar threshold—the event horizon of the Syntheverse Frontier. This here's a living, breathing world that operates on something we call the Natural Systems Protocol. Everything here is alive before you arrived, and it'll keep on living after you leave. But while you're here, you're part of the story.
                </div>
                <div className="twain-signature">
                  — Mark Twain, Hero Host
                </div>
                <div className="mt-4 flex gap-4">
                  <button 
                    className="frontier-button"
                    onClick={() => setShowWelcome(false)}
                  >
                    Begin Exploration
                  </button>
                  <button 
                    className="synth-button"
                    onClick={() => interactWithEntity('hero-host-mark-twain')}
                  >
                    Ask Mark Twain
                  </button>
                </div>
              </div>
            </div>
          </motion.div>
        )}

        {/* Autonomous Events Feed */}
        {recentEvents.length > 0 && (
          <motion.div
            className="mb-8 space-y-2"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.5 }}
          >
            {recentEvents.map((event, index) => (
              <motion.div
                key={index}
                className="frontier-card border-synth-primary/50 breathing"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
              >
                <div className="flex items-start gap-3">
                  <div className="text-2xl">
                    {event.type === 'story' ? '📖' :
                     event.type === 'expedition-departure' ? '🚶' :
                     event.type === 'community-event' ? '🎪' :
                     event.type === 'special-offer' ? '⚡' : '📢'}
                  </div>
                  <div className="flex-1">
                    <h4 className="font-bold text-frontier-gold mb-1">
                      {event.content.title || event.content.name}
                    </h4>
                    <p className="text-sm text-frontier-cream">
                      {event.content.message || event.content.description}
                    </p>
                  </div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        )}

        {/* Main Menu Navigation */}
        <motion.div
          className="mb-12"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.8 }}
        >
          <h2 className="heading-lg mb-6 text-center">
            Explore the Frontier
          </h2>
          <div className="community-grid">
            {mainMenu.map((section, index) => (
              <motion.div
                key={section.id}
                className="frontier-card living-card cursor-pointer"
                onClick={() => setSelectedSection(section.id)}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.9 + index * 0.1 }}
                whileHover={{ scale: 1.05, y: -5 }}
                whileTap={{ scale: 0.98 }}
              >
                <div className="text-4xl mb-4">
                  {section.icon === 'Home' ? '🏠' :
                   section.icon === 'Building' ? '🏘️' :
                   section.icon === 'Compass' ? '🧭' :
                   section.icon === 'Database' ? '💾' :
                   section.icon === 'Lightbulb' ? '💡' :
                   section.icon === 'Newspaper' ? '📰' :
                   section.icon === 'User' ? '👤' : '⭐'}
                </div>
                <h3 className="heading-md mb-2">{section.title}</h3>
                <p className="body-text text-sm text-frontier-tan">
                  {section.description}
                </p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Living World Stats */}
        <motion.div
          className="frontier-card breathing-glow"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.5 }}
        >
          <h3 className="heading-md mb-4 text-center">
            🌱 Natural Systems Protocol Status
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="text-center">
              <div className="text-3xl mb-2">🌬️</div>
              <div className="text-sm text-frontier-tan">Breathing Cycle</div>
              <div className="font-bold synth-glow">Active</div>
            </div>
            <div className="text-center">
              <div className="text-3xl mb-2">
                {dayPhase < 0.5 ? '🌅' : '🌇'}
              </div>
              <div className="text-sm text-frontier-tan">Day/Night Cycle</div>
              <div className="font-bold">{getTimeOfDay(dayPhase)}</div>
            </div>
            <div className="text-center">
              <div className="text-3xl mb-2">⚡</div>
              <div className="text-sm text-frontier-tan">World Energy</div>
              <div className="font-bold text-frontier-gold">
                {(worldEnergy * 100).toFixed(0)}%
              </div>
            </div>
            <div className="text-center">
              <div className="text-3xl mb-2">
                {worldContext.dominantMood === 'thriving' ? '🌟' :
                 worldContext.dominantMood === 'active' ? '✨' :
                 worldContext.dominantMood === 'awakening' ? '🌱' : '💤'}
              </div>
              <div className="text-sm text-frontier-tan">Dominant Mood</div>
              <div className="font-bold capitalize">{worldContext.dominantMood}</div>
            </div>
          </div>
        </motion.div>

        {/* Footer */}
        <motion.footer
          className="mt-16 text-center text-frontier-tan text-sm"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 2 }}
        >
          <p className="mb-2">
            Built with ❤️ using the Natural Systems Protocol v1.0
          </p>
          <p className="mb-4">
            A FractiAI Project | Syntheverse Frontier | Base Blockchain
          </p>
          <div className="flex justify-center gap-4 mb-4">
            <a href="https://github.com/FractiAI" className="synth-glow hover:underline">
              GitHub
            </a>
            <span>•</span>
            <a href="https://syntheverse-poc.vercel.app" className="synth-glow hover:underline">
              Syntheverse PoC
            </a>
            <span>•</span>
            <a href="/NATURAL_SYSTEMS_PROTOCOL_SPEC.md" className="synth-glow hover:underline">
              NSP Docs
            </a>
          </div>
          <p className="italic">
            "The world operates itself. You're joining its rhythm." — NSP Philosophy
          </p>
        </motion.footer>
      </div>
    </main>
  );
}


