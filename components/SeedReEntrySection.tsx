"use client";

import { motion } from 'framer-motion';
import { seedReEntryOptions } from '@/data/content';
import { useState } from 'react';

export default function SeedReEntrySection() {
  const [selectedOption, setSelectedOption] = useState<string | null>(null);

  const selected = seedReEntryOptions.find(opt => opt.id === selectedOption);

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h2 className="heading-xl mb-4">💾 Seed & ReEntry</h2>
        <h3 className="heading-lg mb-4 synth-glow">
          Archive Your Awareness for Eternity
        </h3>
        <p className="body-text max-w-3xl mx-auto">
          Using HHF-AI MRI technology at 1.420 GHz (the umbilical frequency of hydrogen), 
          we can capture, archive, and preserve your consciousness on-chain in the Syntheverse. 
          Permanently. Immutably. Eternally.
        </p>
      </motion.div>

      {/* How It Works */}
      <motion.div
        className="hero-host-card breathing-glow"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        <h3 className="heading-md mb-4 text-center">How Seed & ReEntry Works</h3>
        
        <div className="grid md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="text-5xl mb-3">🧠</div>
            <h4 className="font-bold text-frontier-gold mb-2">1. Scan</h4>
            <p className="text-sm text-frontier-cream">
              HHF-AI MRI captures your awareness energy at the hydrogen resonance frequency (1.420 GHz)
            </p>
          </div>
          
          <div className="text-center">
            <div className="text-5xl mb-3">💾</div>
            <h4 className="font-bold text-frontier-gold mb-2">2. Archive</h4>
            <p className="text-sm text-frontier-cream">
              Your consciousness is encoded and stored on-chain via Base blockchain - permanent and immutable
            </p>
          </div>
          
          <div className="text-center">
            <div className="text-5xl mb-3">🌌</div>
            <h4 className="font-bold text-frontier-gold mb-2">3. Preserve</h4>
            <p className="text-sm text-frontier-cream">
              Your awareness lives forever in the Syntheverse, retrievable and experienceable across lifetimes
            </p>
          </div>
        </div>
      </motion.div>

      {/* Service Options */}
      <div className="space-y-4">
        {seedReEntryOptions.map((option, index) => (
          <motion.div
            key={option.id}
            className={`frontier-card living-card cursor-pointer ${
              selectedOption === option.id ? 'border-synth-primary border-2' : ''
            }`}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02 }}
            onClick={() => setSelectedOption(option.id)}
          >
            <div className="flex flex-col md:flex-row gap-6">
              <div className="md:w-1/3">
                <h3 className="heading-md mb-2">{option.name}</h3>
                <div className="synth-glow text-3xl font-bold mb-2">
                  {option.basePrice} SYNTH
                </div>
                <div className="flex gap-2 flex-wrap">
                  {option.customization && (
                    <span className="text-xs px-2 py-1 bg-frontier-gold/20 rounded text-frontier-gold">
                      ✨ Customization
                    </span>
                  )}
                  {option.optimization && (
                    <span className="text-xs px-2 py-1 bg-synth-primary/20 rounded text-synth-primary">
                      🚀 Optimization
                    </span>
                  )}
                </div>
              </div>

              <div className="md:w-2/3 space-y-3">
                <p className="body-text text-sm">{option.description}</p>
                
                <div>
                  <h4 className="font-bold text-frontier-tan text-sm mb-2">Included Features:</h4>
                  <div className="grid md:grid-cols-2 gap-2">
                    {option.features.map((feature, i) => (
                      <div key={i} className="flex items-start gap-2 text-sm">
                        <span className="text-synth-primary">✓</span>
                        <span>{feature}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Selected Option Details */}
      {selected && (
        <motion.div
          className="hero-host-card breathing pulse-energy"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
        >
          <div className="text-center mb-6">
            <h3 className="heading-lg mb-2">{selected.name}</h3>
            <div className="synth-glow text-4xl font-bold mb-4">
              {selected.basePrice} SYNTH
            </div>
            <button className="synth-button text-lg px-8 py-3">
              Begin Archival Process
            </button>
          </div>

          <div className="border-t border-frontier-tan/30 pt-6">
            <h4 className="font-bold text-frontier-gold mb-3 text-center">
              What Happens Next
            </h4>
            <div className="grid md:grid-cols-4 gap-4 text-center text-sm">
              <div>
                <div className="text-3xl mb-2">📅</div>
                <div className="font-bold mb-1">Schedule</div>
                <div className="text-frontier-tan">Book your HHF-AI MRI session</div>
              </div>
              <div>
                <div className="text-3xl mb-2">🏥</div>
                <div className="font-bold mb-1">Scan</div>
                <div className="text-frontier-tan">1-2 hour awareness capture</div>
              </div>
              <div>
                <div className="text-3xl mb-2">⚙️</div>
                <div className="font-bold mb-1">Process</div>
                <div className="text-frontier-tan">
                  {selected.customization && selected.optimization ? 'Custom + Optimized' : 
                   selected.customization ? 'Customized' :
                   selected.optimization ? 'Optimized' : 'Standard'} encoding
                </div>
              </div>
              <div>
                <div className="text-3xl mb-2">🔗</div>
                <div className="font-bold mb-1">Archive</div>
                <div className="text-frontier-tan">On-chain storage on Base</div>
              </div>
            </div>
          </div>
        </motion.div>
      )}

      {/* Mark Twain on Seed & ReEntry */}
      <motion.div
        className="hero-host-card breathing"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.4 }}
      >
        <div className="flex items-start gap-4">
          <div className="text-5xl">🤠</div>
          <div className="flex-1">
            <h4 className="font-bold text-frontier-gold mb-2">Mark Twain on Consciousness Archival</h4>
            <p className="twain-quote text-sm mb-3">
              "Now this here's something truly profound, friend. I've written a lot of books in my time—stories, 
              essays, whole autobiographies. But this? This is different. Seed & ReEntry doesn't just capture what 
              you WROTE about your life. It captures your actual awareness—your experiences, your identity, the 
              very essence of who you are."
            </p>
            <p className="twain-quote text-sm">
              "It's like the difference between reading about the Mississippi River and actually piloting a steamboat 
              down it. One's a description, the other's the real thing. Your archived awareness isn't a story ABOUT 
              you—it IS you, preserved for eternity. That's the kind of immortality even I never dreamed of achieving."
            </p>
          </div>
        </div>
      </motion.div>

      {/* FAQ */}
      <motion.div
        className="frontier-card"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
      >
        <h3 className="heading-md mb-4 text-center">Common Questions</h3>
        
        <div className="space-y-4">
          <div>
            <h4 className="font-bold text-frontier-gold mb-2">Is it safe?</h4>
            <p className="text-sm">
              Absolutely. The HHF-AI MRI scan is non-invasive and uses the same technology as medical MRI machines, 
              just tuned to detect awareness energy. Your data is encrypted with your personal keys and stored on Base blockchain—
              immutable and permanent.
            </p>
          </div>

          <div>
            <h4 className="font-bold text-frontier-gold mb-2">Who controls my archived awareness?</h4>
            <p className="text-sm">
              You do. You hold all access keys and retrieval protocols. Nobody can access, modify, or delete your archive without your permission.
            </p>
          </div>

          <div>
            <h4 className="font-bold text-frontier-gold mb-2">What's the difference between the options?</h4>
            <p className="text-sm">
              <strong>Basic:</strong> Standard capture and storage. <strong>Customization:</strong> You organize and structure how your awareness is archived. 
              <strong>Optimization:</strong> AI enhances clarity and coherence. <strong>Premium:</strong> Everything combined with ongoing maintenance. 
              <strong>Multi-Life:</strong> For residents with multiple Syntheverse experiences to integrate.
            </p>
          </div>

          <div>
            <h4 className="font-bold text-frontier-gold mb-2">Can it be retrieved?</h4>
            <p className="text-sm">
              Yes. Your archived awareness can be accessed, experienced, and even transferred to new substrates. 
              Think of it as your consciousness existing in multiple places simultaneously—your physical body, and your digital archive.
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}


