"use client";

import { motion } from 'framer-motion';
import { expeditions } from '@/data/content';
import { useState } from 'react';

export default function ExpeditionsSection() {
  const [selectedType, setSelectedType] = useState<string>('all');
  const [selectedExpedition, setSelectedExpedition] = useState<string | null>(null);

  const types = ['all', 'fishing', 'hunting', 'eco-adventure', 'storytelling', 'exploration'];
  
  const filteredExpeditions = selectedType === 'all'
    ? expeditions
    : expeditions.filter(exp => exp.type === selectedType);

  const selected = expeditions.find(exp => exp.id === selectedExpedition);

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'fishing': return '🎣';
      case 'hunting': return '🏹';
      case 'eco-adventure': return '🌿';
      case 'storytelling': return '📖';
      case 'exploration': return '🗺️';
      default: return '⭐';
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h2 className="heading-xl mb-4">FSR Expeditions & Adventures</h2>
        <p className="body-text max-w-3xl mx-auto">
          From half-day morning catches to week-long wilderness immersions. 
          Every expedition is guided by experts—and many feature storytelling sessions with Mark Twain himself.
        </p>
      </motion.div>

      {/* Type Filter */}
      <motion.div
        className="flex flex-wrap justify-center gap-3"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        {types.map((type) => (
          <button
            key={type}
            className={`px-6 py-2 rounded-lg font-bold transition-all ${
              selectedType === type
                ? 'bg-synth-primary text-white shadow-lg'
                : 'bg-frontier-brown text-frontier-tan hover:bg-frontier-tan hover:text-frontier-dark'
            }`}
            onClick={() => setSelectedType(type)}
          >
            {getTypeIcon(type)} {type === 'all' ? 'All Types' : type.replace('-', ' ')}
          </button>
        ))}
      </motion.div>

      {/* Expeditions Grid */}
      <div className="expedition-grid">
        {filteredExpeditions.map((expedition, index) => (
          <motion.div
            key={expedition.id}
            className={`frontier-card living-card cursor-pointer ${
              selectedExpedition === expedition.id ? 'border-frontier-gold border-2' : ''
            }`}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.05 }}
            whileHover={{ scale: 1.05, y: -5 }}
            onClick={() => setSelectedExpedition(expedition.id)}
          >
            <div className="breathing">
              <div className="flex justify-between items-start mb-3">
                <div className="text-3xl">{getTypeIcon(expedition.type)}</div>
                <div className="text-right">
                  <div className="synth-glow font-bold text-xl">
                    {expedition.price} SYNTH
                  </div>
                  <div className="text-xs text-frontier-tan">{expedition.duration}</div>
                </div>
              </div>

              <h3 className="heading-md text-lg mb-2">{expedition.name}</h3>
              
              <div className="flex gap-2 mb-3 flex-wrap">
                {expedition.guided && (
                  <span className="text-xs px-2 py-1 bg-frontier-gold/20 rounded text-frontier-gold">
                    Guided
                  </span>
                )}
                {expedition.adultsOnly ? (
                  <span className="text-xs px-2 py-1 bg-synth-accent/20 rounded text-synth-accent">
                    Adults Only
                  </span>
                ) : (
                  <span className="text-xs px-2 py-1 bg-green-500/20 rounded text-green-400">
                    Family Friendly
                  </span>
                )}
              </div>

              <p className="body-text text-sm">{expedition.description}</p>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Selected Expedition Details */}
      {selected && (
        <motion.div
          className="hero-host-card breathing-glow"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
        >
          <div className="flex flex-col md:flex-row gap-6">
            <div className="md:w-1/3">
              <div className="text-8xl mb-4 text-center">{getTypeIcon(selected.type)}</div>
              <div className="text-center">
                <h3 className="heading-lg mb-2">{selected.name}</h3>
                <div className="synth-glow text-3xl font-bold mb-2">
                  {selected.price} SYNTH
                </div>
                <div className="text-frontier-tan mb-4">{selected.duration}</div>
                <button className="synth-button w-full">
                  Book This Expedition
                </button>
              </div>
            </div>

            <div className="md:w-2/3 space-y-4">
              <div>
                <h4 className="font-bold text-frontier-gold mb-2">Description</h4>
                <p className="body-text">{selected.description}</p>
              </div>

              <div>
                <h4 className="font-bold text-frontier-gold mb-2">What's Included</h4>
                <div className="space-y-2">
                  {selected.included.map((item, i) => (
                    <div key={i} className="flex items-start gap-2">
                      <span className="text-frontier-gold">✓</span>
                      <span className="body-text text-sm">{item}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="flex gap-3 flex-wrap">
                {selected.guided && (
                  <div className="flex items-center gap-2 text-sm">
                    <span className="text-2xl">👥</span>
                    <span>Expert Guide Included</span>
                  </div>
                )}
                {!selected.adultsOnly && (
                  <div className="flex items-center gap-2 text-sm">
                    <span className="text-2xl">👨‍👩‍👧‍👦</span>
                    <span>Family Friendly</span>
                  </div>
                )}
                <div className="flex items-center gap-2 text-sm">
                  <span className="text-2xl">⏱️</span>
                  <span>{selected.duration}</span>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      )}

      {/* Mark Twain's Expedition Stories */}
      <motion.div
        className="hero-host-card breathing"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
      >
        <div className="flex items-start gap-4">
          <div className="text-5xl">🤠</div>
          <div className="flex-1">
            <h4 className="font-bold text-frontier-gold mb-2">Mark Twain on Expeditions</h4>
            <p className="twain-quote text-sm">
              "Ah, expeditions! This is where the Syntheverse really shows its colors. I've been on every one of these adventures myself, 
              and I can tell you—they're genuine experiences. The fishing? Peaceful and profound. The hunting? Teaches you respect for 
              nature and yourself. The eco-adventures? You'll see things that'll change how you think about life itself. And the storytelling 
              sessions? Well, those are my personal favorites. Nothing beats a good story under the stars, friend."
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}



