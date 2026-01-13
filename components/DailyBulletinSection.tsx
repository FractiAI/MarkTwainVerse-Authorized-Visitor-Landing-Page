"use client";

import { motion } from 'framer-motion';
import { dailyBulletin } from '@/data/content';
import { useDayNightCycle } from '@/components/NaturalSystemsProvider';
import { useState } from 'react';

export default function DailyBulletinSection() {
  const dayPhase = useDayNightCycle();
  const [expandedStory, setExpandedStory] = useState(false);

  const getGreeting = (phase: number) => {
    if (phase < 0.25) return '🌅 Good morning';
    if (phase < 0.5) return '☀️ Good day';
    if (phase < 0.75) return '🌤️ Good afternoon';
    if (phase < 0.9) return '🌇 Good evening';
    return '🌙 Good night';
  };

  return (
    <div className="space-y-8">
      {/* Header with Dynamic Greeting */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <motion.h2
          className="heading-xl mb-4"
          animate={{ scale: [1, 1.05, 1] }}
          transition={{ duration: 4, repeat: Infinity }}
        >
          {getGreeting(dayPhase)}, Frontier Friends!
        </motion.h2>
        <h3 className="heading-lg mb-4">📰 Daily Menu & Bulletin</h3>
        <p className="body-text">
          {dailyBulletin.welcomeMessage}
        </p>
        <p className="text-sm text-frontier-tan mt-2">
          {dailyBulletin.date}
        </p>
      </motion.div>

      {/* Featured Story */}
      <motion.div
        className="hero-host-card breathing-glow"
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.2 }}
      >
        <div className="flex items-start gap-4">
          <div className="text-5xl">🤠</div>
          <div className="flex-1">
            <h3 className="heading-md mb-2 flex items-center gap-2">
              <span>📖</span>
              Featured Story: {dailyBulletin.featuredStory.title}
            </h3>
            <p className="body-text text-sm italic mb-4">
              {dailyBulletin.featuredStory.preview}
            </p>
            
            {expandedStory ? (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                className="twain-quote text-sm whitespace-pre-line mb-4"
              >
                {dailyBulletin.featuredStory.fullStory}
              </motion.div>
            ) : null}
            
            <button
              className="frontier-button text-sm"
              onClick={() => setExpandedStory(!expandedStory)}
            >
              {expandedStory ? 'Close Story' : 'Read Full Story'}
            </button>
          </div>
        </div>
      </motion.div>

      {/* Today's Specials */}
      <div className="space-y-4">
        <h3 className="heading-lg text-center">🌟 Today's Happenings</h3>
        
        {dailyBulletin.todaysSpecials.map((category, categoryIndex) => (
          <motion.div
            key={category.category}
            className="frontier-card living-card"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3 + categoryIndex * 0.1 }}
          >
            <h4 className="heading-md text-lg mb-4 flex items-center gap-2">
              <span>
                {category.category === 'Expeditions' ? '🧭' :
                 category.category === 'Dining' ? '🍽️' :
                 category.category === 'Community Events' ? '🎪' :
                 '💡'}
              </span>
              {category.category}
            </h4>
            
            <div className="space-y-3">
              {category.items.map((item, itemIndex) => (
                <motion.div
                  key={itemIndex}
                  className="flex items-start gap-3 p-3 bg-frontier-dark/30 rounded-lg breathing"
                  whileHover={{ x: 5, backgroundColor: 'rgba(212, 175, 55, 0.1)' }}
                >
                  <span className="text-frontier-gold">•</span>
                  <span className="body-text text-sm flex-1">{item}</span>
                  <button className="text-xs px-3 py-1 bg-synth-primary/20 rounded hover:bg-synth-primary hover:text-white transition-colors">
                    Details
                  </button>
                </motion.div>
              ))}
            </div>
          </motion.div>
        ))}
      </div>

      {/* Hero Host Prompts */}
      <motion.div
        className="hero-host-card breathing"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6 }}
      >
        <h3 className="heading-md mb-4 text-center">💬 Ask Your Hero Host</h3>
        <p className="text-center text-sm text-frontier-tan mb-4">
          Mark Twain is here to help. Here are some suggestions:
        </p>
        
        <div className="grid md:grid-cols-2 gap-3">
          {dailyBulletin.heroHostPrompts.map((prompt, index) => (
            <motion.button
              key={index}
              className="frontier-card text-left p-3 cursor-pointer border border-frontier-tan hover:border-frontier-gold transition-colors"
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.7 + index * 0.05 }}
            >
              <div className="flex items-start gap-2">
                <span className="text-xl">💭</span>
                <span className="text-sm">{prompt}</span>
              </div>
            </motion.button>
          ))}
        </div>
      </motion.div>

      {/* Announcements */}
      <motion.div
        className="frontier-card"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8 }}
      >
        <h3 className="heading-md mb-4 text-center">📢 Announcements</h3>
        <div className="space-y-3">
          {dailyBulletin.announcements.map((announcement, index) => (
            <motion.div
              key={index}
              className="flex items-start gap-3 p-3 bg-synth-primary/10 rounded-lg border border-synth-primary/30"
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.9 + index * 0.05 }}
            >
              <span className="text-synth-primary text-xl">
                {announcement.startsWith('New:') ? '✨' :
                 announcement.startsWith('Reminder:') ? '⏰' :
                 '📌'}
              </span>
              <span className="body-text text-sm flex-1">{announcement}</span>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Subscribe Section */}
      <motion.div
        className="hero-host-card text-center breathing-glow"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.0 }}
      >
        <h3 className="heading-md mb-3">📬 Never Miss a Bulletin</h3>
        <p className="body-text text-sm mb-4">
          Get the Daily Menu & Bulletin delivered to your Syntheverse inbox every morning at dawn.
        </p>
        <div className="flex gap-3 max-w-md mx-auto">
          <input
            type="email"
            placeholder="your@email.com"
            className="flex-1 px-4 py-2 rounded-lg bg-frontier-dark border border-frontier-tan text-frontier-cream focus:outline-none focus:border-synth-primary"
          />
          <button className="synth-button">
            Subscribe
          </button>
        </div>
        <p className="text-xs text-frontier-tan mt-2">
          Delivered via Syntheverse notifications and email
        </p>
      </motion.div>

      {/* Previous Bulletins */}
      <motion.div
        className="frontier-card"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.1 }}
      >
        <h3 className="heading-md mb-4 text-center">📚 Bulletin Archive</h3>
        <p className="text-center text-sm text-frontier-tan mb-4">
          Browse previous editions and Mark Twain's stories from past days on the frontier.
        </p>
        <div className="text-center">
          <button className="frontier-button">
            View Archive
          </button>
        </div>
      </motion.div>
    </div>
  );
}

