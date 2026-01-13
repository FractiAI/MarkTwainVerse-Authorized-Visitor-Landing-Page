"use client";

import { motion } from 'framer-motion';
import { innovationSpaces, innovationHubInfo } from '@/data/content';
import { useState } from 'react';

export default function InnovationHubSection() {
  const [selectedSpace, setSelectedSpace] = useState<number | null>(null);
  const [filterAvailable, setFilterAvailable] = useState(false);

  const spaces = filterAvailable
    ? innovationSpaces.filter(s => s.available)
    : innovationSpaces;

  const selected = selectedSpace !== null
    ? innovationSpaces.find(s => s.spaceNumber === selectedSpace)
    : null;

  const getTierColor = (spaceNum: number) => {
    if (spaceNum <= 10) return 'border-frontier-gold';
    if (spaceNum <= 25) return 'border-synth-primary';
    return 'border-frontier-tan';
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h2 className="heading-xl mb-4">💡 Innovation Hub</h2>
        <h3 className="heading-lg mb-4">33 Spaces for Dreamers & Builders</h3>
        <p className="body-text max-w-3xl mx-auto">
          {innovationHubInfo.description}
        </p>
      </motion.div>

      {/* Benefits */}
      <motion.div
        className="hero-host-card breathing-glow"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        <h3 className="heading-md mb-4 text-center">What You Get</h3>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {innovationHubInfo.benefits.map((benefit, index) => (
            <motion.div
              key={index}
              className="flex items-start gap-3"
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 + index * 0.05 }}
            >
              <span className="text-synth-primary text-xl">✓</span>
              <span className="text-sm">{benefit}</span>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Filter */}
      <div className="flex justify-between items-center">
        <h3 className="heading-md">Available Spaces</h3>
        <button
          className={`px-4 py-2 rounded-lg font-bold transition-all ${
            filterAvailable
              ? 'bg-synth-primary text-white'
              : 'bg-frontier-brown text-frontier-tan'
          }`}
          onClick={() => setFilterAvailable(!filterAvailable)}
        >
          {filterAvailable ? '🟢 Available Only' : '📋 Show All'}
        </button>
      </div>

      {/* Spaces Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
        {spaces.map((space, index) => {
          const tier = space.spaceNumber <= 10 ? 'Premium' : space.spaceNumber <= 25 ? 'Standard' : 'Compact';
          
          return (
            <motion.div
              key={space.id}
              className={`frontier-card p-3 text-center cursor-pointer ${getTierColor(space.spaceNumber)} ${
                selectedSpace === space.spaceNumber ? 'border-2' : 'border'
              } ${space.available ? 'breathing' : 'opacity-50'}`}
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: index * 0.01 }}
              whileHover={{ scale: space.available ? 1.1 : 1.0 }}
              onClick={() => space.available && setSelectedSpace(space.spaceNumber)}
            >
              <div className="text-2xl mb-1">
                {space.available ? '🟢' : '🔴'}
              </div>
              <div className="font-bold text-sm mb-1">#{space.spaceNumber}</div>
              <div className="text-xs text-frontier-tan">{tier}</div>
              <div className="text-xs font-bold synth-glow mt-1">
                {space.monthlyLease}
              </div>
            </motion.div>
          );
        })}
      </div>

      {/* Selected Space Details */}
      {selected && (
        <motion.div
          className="hero-host-card breathing pulse-energy"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
        >
          <div className="flex flex-col md:flex-row gap-6">
            <div className="md:w-1/3 text-center">
              <div className="text-6xl mb-4">💡</div>
              <h3 className="heading-lg mb-2">Space #{selected.spaceNumber}</h3>
              <div className="text-frontier-tan mb-2">{selected.size}</div>
              <div className="synth-glow text-3xl font-bold mb-4">
                {selected.monthlyLease} SYNTH<span className="text-sm">/month</span>
              </div>
              <button className="synth-button w-full">
                Lease This Space
              </button>
            </div>

            <div className="md:w-2/3 space-y-4">
              <div>
                <h4 className="font-bold text-frontier-gold mb-2">Included Features</h4>
                <div className="space-y-2">
                  {selected.features.map((feature, i) => (
                    <div key={i} className="flex items-start gap-2 text-sm">
                      <span className="text-synth-primary">✓</span>
                      <span>{feature}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="border-t border-frontier-tan/30 pt-4">
                <h4 className="font-bold text-frontier-gold mb-2">Lease Terms</h4>
                <div className="space-y-1 text-sm">
                  {innovationHubInfo.leaseTerms.map((term, i) => (
                    <div key={i} className="flex items-start gap-2">
                      <span className="text-frontier-tan">•</span>
                      <span>{term}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      )}

      {/* Tier Comparison */}
      <motion.div
        className="frontier-card"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
      >
        <h3 className="heading-md mb-4 text-center">Space Tiers</h3>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="text-center p-4 border border-frontier-gold rounded-lg">
            <div className="text-3xl mb-2">⭐</div>
            <h4 className="font-bold text-frontier-gold mb-2">Premium</h4>
            <div className="text-sm text-frontier-tan mb-2">Spaces 1-10</div>
            <div className="text-2xl font-bold synth-glow mb-2">1,200 SYNTH</div>
            <div className="text-xs">800 sq ft • Private conference room</div>
          </div>

          <div className="text-center p-4 border border-synth-primary rounded-lg">
            <div className="text-3xl mb-2">💼</div>
            <h4 className="font-bold text-synth-primary mb-2">Standard</h4>
            <div className="text-sm text-frontier-tan mb-2">Spaces 11-25</div>
            <div className="text-2xl font-bold synth-glow mb-2">750 SYNTH</div>
            <div className="text-xs">500 sq ft • Shared conference</div>
          </div>

          <div className="text-center p-4 border border-frontier-tan rounded-lg">
            <div className="text-3xl mb-2">🚀</div>
            <h4 className="font-bold text-frontier-tan mb-2">Compact</h4>
            <div className="text-sm text-frontier-tan mb-2">Spaces 26-33</div>
            <div className="text-2xl font-bold synth-glow mb-2">450 SYNTH</div>
            <div className="text-xs">300 sq ft • Cozy & capable</div>
          </div>
        </div>
      </motion.div>

      {/* Mark Twain on Innovation */}
      <motion.div
        className="hero-host-card breathing"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
      >
        <div className="flex items-start gap-4">
          <div className="text-5xl">🤠</div>
          <div className="flex-1">
            <h4 className="font-bold text-frontier-gold mb-2">Mark Twain on Innovation</h4>
            <p className="twain-quote text-sm">
              "Got an idea rattling around in that head of yours? Well, the Innovation Hub is where you bring it to life. 
              I've seen some remarkable things come out of these 33 spaces—new expedition types, architectural innovations, 
              consciousness research, social experiments. The frontier rewards those who dare to build, friend. And remember: 
              every great invention started as someone's wild idea in a small room. Who knows? Maybe your proof-of-concept 
              will become the next big thing in the Syntheverse."
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}


