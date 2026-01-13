"use client";

import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';
import { formatSYNTH } from '@/data/content';

interface CartItem {
  id: string;
  type: 'package' | 'expedition' | 'seed-reentry' | 'innovation-space';
  name: string;
  price: number;
  details?: string;
  duration?: string;
}

interface BookingCartProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function BookingCart({ isOpen, onClose }: BookingCartProps) {
  // Example cart state (in real app, this would come from global state)
  const [cartItems, setCartItems] = useState<CartItem[]>([
    {
      id: '1',
      type: 'package',
      name: 'Weekly Residency - Frontier Colony',
      price: 260,
      details: '7 days in Frontier Colony (1.3x multiplier)',
      duration: '7 days',
    },
    {
      id: '2',
      type: 'expedition',
      name: 'Morning Catch Adventure',
      price: 75,
      details: 'Half-day fishing expedition',
      duration: '4 hours',
    },
  ]);

  const subtotal = cartItems.reduce((sum, item) => sum + item.price, 0);
  const discount = 0; // Could be based on user type
  const total = subtotal - discount;

  const removeItem = (id: string) => {
    setCartItems(cartItems.filter(item => item.id !== id));
  };

  const getItemIcon = (type: string) => {
    switch (type) {
      case 'package': return '🏠';
      case 'expedition': return '🧭';
      case 'seed-reentry': return '💾';
      case 'innovation-space': return '💡';
      default: return '⭐';
    }
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

          {/* Cart Panel */}
          <motion.div
            className="fixed right-0 top-0 bottom-0 w-full md:w-[500px] bg-frontier-dark border-l-4 border-frontier-gold z-50 overflow-y-auto"
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25 }}
          >
            <div className="p-6 space-y-6">
              {/* Header */}
              <div className="flex justify-between items-center border-b border-frontier-tan/30 pb-4">
                <h2 className="heading-lg">🛒 Your Cart</h2>
                <button
                  className="text-3xl hover:text-frontier-gold transition-colors"
                  onClick={onClose}
                >
                  ×
                </button>
              </div>

              {/* Cart Items */}
              {cartItems.length === 0 ? (
                <div className="text-center py-12">
                  <div className="text-6xl mb-4">🤠</div>
                  <h3 className="heading-md mb-2">Your cart is empty, friend</h3>
                  <p className="body-text text-sm text-frontier-tan">
                    Start exploring the frontier and add some experiences to your cart!
                  </p>
                </div>
              ) : (
                <div className="space-y-4">
                  {cartItems.map((item, index) => (
                    <motion.div
                      key={item.id}
                      className="frontier-card breathing"
                      initial={{ opacity: 0, x: 20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.05 }}
                    >
                      <div className="flex gap-4">
                        <div className="text-4xl">{getItemIcon(item.type)}</div>
                        <div className="flex-1">
                          <h4 className="font-bold text-frontier-gold mb-1">{item.name}</h4>
                          {item.details && (
                            <p className="text-xs text-frontier-tan mb-2">{item.details}</p>
                          )}
                          {item.duration && (
                            <p className="text-xs text-frontier-cream">Duration: {item.duration}</p>
                          )}
                        </div>
                        <div className="text-right">
                          <div className="synth-glow font-bold text-lg mb-2">
                            {formatSYNTH(item.price)}
                          </div>
                          <button
                            className="text-xs text-synth-accent hover:underline"
                            onClick={() => removeItem(item.id)}
                          >
                            Remove
                          </button>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              )}

              {/* Totals */}
              {cartItems.length > 0 && (
                <motion.div
                  className="hero-host-card space-y-3"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: 0.3 }}
                >
                  <div className="flex justify-between text-sm">
                    <span>Subtotal:</span>
                    <span className="font-bold">{formatSYNTH(subtotal)}</span>
                  </div>
                  
                  {discount > 0 && (
                    <div className="flex justify-between text-sm text-frontier-gold">
                      <span>Resident Discount (15%):</span>
                      <span className="font-bold">-{formatSYNTH(discount)}</span>
                    </div>
                  )}

                  <div className="border-t border-frontier-tan/30 pt-3 flex justify-between">
                    <span className="heading-md">Total:</span>
                    <span className="heading-md synth-glow">{formatSYNTH(total)}</span>
                  </div>

                  <p className="text-xs text-frontier-tan text-center">
                    Paid in SYNTH tokens on Base blockchain
                  </p>
                </motion.div>
              )}

              {/* Actions */}
              {cartItems.length > 0 && (
                <div className="space-y-3">
                  <button className="synth-button w-full text-lg py-3">
                    Proceed to Checkout
                  </button>
                  <button className="frontier-button w-full">
                    Save Cart for Later
                  </button>
                  <p className="text-xs text-center text-frontier-tan">
                    🔒 Secure payment via Web3 wallet
                  </p>
                </div>
              )}

              {/* Mark Twain's Cart Message */}
              <motion.div
                className="frontier-card border-frontier-gold/50"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
              >
                <div className="flex items-start gap-3">
                  <div className="text-3xl">🤠</div>
                  <div>
                    <h4 className="font-bold text-frontier-gold mb-1 text-sm">
                      Mark Twain says:
                    </h4>
                    <p className="text-xs text-frontier-cream">
                      {cartItems.length === 0
                        ? "Don't be shy, friend. The frontier's got plenty to offer. Pick something that speaks to your spirit!"
                        : "Fine choices! Remember, you can always add more adventures later. The frontier ain't going anywhere."}
                    </p>
                  </div>
                </div>
              </motion.div>

              {/* Payment Methods */}
              {cartItems.length > 0 && (
                <motion.div
                  className="frontier-card"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: 0.6 }}
                >
                  <h4 className="font-bold text-frontier-tan mb-3 text-sm">Payment Methods</h4>
                  <div className="grid grid-cols-3 gap-2">
                    <div className="text-center p-2 bg-frontier-brown rounded">
                      <div className="text-2xl mb-1">💰</div>
                      <div className="text-xs">SYNTH</div>
                    </div>
                    <div className="text-center p-2 bg-frontier-brown rounded opacity-50">
                      <div className="text-2xl mb-1">💳</div>
                      <div className="text-xs">Card</div>
                      <div className="text-[10px] text-frontier-tan">(Soon)</div>
                    </div>
                    <div className="text-center p-2 bg-frontier-brown rounded opacity-50">
                      <div className="text-2xl mb-1">🔗</div>
                      <div className="text-xs">Crypto</div>
                      <div className="text-[10px] text-frontier-tan">(Soon)</div>
                    </div>
                  </div>
                </motion.div>
              )}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}



