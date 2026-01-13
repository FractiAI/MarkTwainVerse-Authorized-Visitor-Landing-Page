"use client";

import { motion } from 'framer-motion';
import { communities, lifePackages, calculatePrice, formatSYNTH } from '@/data/content';
import { useState } from 'react';

interface CommunitiesSectionProps {
  userType?: 'visitor' | 'extendedStay' | 'resident' | 'citizen';
}

export default function CommunitiesSection({ userType = 'visitor' }: CommunitiesSectionProps) {
  const [selectedCommunity, setSelectedCommunity] = useState<string | null>(null);
  const [selectedPackage, setSelectedPackage] = useState<string | null>(null);

  const selected = communities.find(c => c.id === selectedCommunity);

  return (
    <div className="space-y-8">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h2 className="heading-xl mb-4">Seven Living Communities</h2>
        <p className="body-text max-w-3xl mx-auto">
          Each community is a living organism with its own atmosphere, residents, and premium multiplier.
          Choose where you want to call home on the frontier.
        </p>
      </motion.div>

      {/* Communities Grid */}
      <div className="community-grid">
        {communities.map((community, index) => (
          <motion.div
            key={community.id}
            className={`frontier-card living-card cursor-pointer ${
              selectedCommunity === community.id ? 'border-frontier-gold border-2' : ''
            }`}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.03, y: -5 }}
            onClick={() => setSelectedCommunity(community.id)}
          >
            <div className="breathing">
              <div className="flex justify-between items-start mb-4">
                <h3 className="heading-md">{community.name}</h3>
                <div className="synth-glow font-bold text-lg">
                  {community.premiumMultiplier}x
                </div>
              </div>
              
              <p className="body-text text-sm mb-4">{community.description}</p>
              
              <div className="space-y-2 mb-4">
                <div className="text-sm font-bold text-frontier-tan">Features:</div>
                {community.features.map((feature, i) => (
                  <div key={i} className="text-sm flex items-start gap-2">
                    <span className="text-frontier-gold">•</span>
                    <span>{feature}</span>
                  </div>
                ))}
              </div>
              
              <div className="text-sm italic text-frontier-tan border-t border-frontier-tan/30 pt-3">
                Atmosphere: {community.atmosphere}
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Selected Community Details */}
      {selected && (
        <motion.div
          className="hero-host-card breathing-glow"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
        >
          <h3 className="heading-lg mb-4 flex items-center gap-3">
            <span>🏘️</span>
            {selected.name} - Life Packages
          </h3>
          <p className="body-text mb-6">
            Base prices shown below are multiplied by <span className="synth-glow font-bold">{selected.premiumMultiplier}x</span> for {selected.name}.
            {userType === 'resident' && ' As a resident, you receive 15% off.'}
            {userType === 'citizen' && ' As a citizen, you receive 33% off.'}
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {lifePackages.map((pkg, index) => {
              const finalPrice = calculatePrice(pkg.basePrice, selected, userType);
              
              return (
                <motion.div
                  key={pkg.name}
                  className={`frontier-card cursor-pointer ${
                    selectedPackage === pkg.name ? 'border-synth-primary border-2' : ''
                  }`}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.05 }}
                  whileHover={{ scale: 1.05 }}
                  onClick={() => setSelectedPackage(pkg.name)}
                >
                  <h4 className="font-bold text-frontier-gold mb-2">{pkg.name}</h4>
                  <div className="text-2xl font-bold synth-glow mb-2">
                    {formatSYNTH(finalPrice)}
                  </div>
                  <div className="text-sm text-frontier-tan mb-3">{pkg.duration}</div>
                  
                  <div className="space-y-1">
                    {pkg.benefits.map((benefit, i) => (
                      <div key={i} className="text-xs flex items-start gap-2">
                        <span className="text-frontier-gold">✓</span>
                        <span>{benefit}</span>
                      </div>
                    ))}
                  </div>

                  {pkg.basePrice !== finalPrice && (
                    <div className="mt-3 pt-3 border-t border-frontier-tan/30 text-xs">
                      <span className="line-through text-frontier-tan/50">
                        Base: {formatSYNTH(pkg.basePrice)}
                      </span>
                      <span className="text-frontier-gold ml-2">
                        → {formatSYNTH(finalPrice)}
                      </span>
                    </div>
                  )}
                </motion.div>
              );
            })}
          </div>

          {selectedPackage && (
            <motion.div
              className="mt-6 text-center"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
            >
              <button className="synth-button text-lg">
                Add {selectedPackage} to Cart
              </button>
            </motion.div>
          )}
        </motion.div>
      )}

      {/* Mark Twain's Community Guidance */}
      <motion.div
        className="hero-host-card breathing"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
      >
        <div className="flex items-start gap-4">
          <div className="text-5xl">🤠</div>
          <div className="flex-1">
            <h4 className="font-bold text-frontier-gold mb-2">Mark Twain's Guidance</h4>
            <p className="twain-quote text-sm">
              "Now, choosing a community is like picking a neighborhood—each one's got its own character. 
              The Frontier Colony folks like their independence, the Wilderness types want pure nature, 
              and the Mega-Metro crowd? Well, they like their conveniences. Pick what suits your spirit, 
              friend. You can always visit the others—that's the beauty of this frontier."
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}


