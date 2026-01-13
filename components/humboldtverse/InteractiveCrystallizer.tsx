'use client';

/**
 * Interactive Crystallizer - 3 Key Takeaways
 * Hands-on museum exhibit style
 * Natural Systems Protocol made tangible
 */

import { useState, useEffect } from 'react';
import { Sparkles, Zap, Repeat } from 'lucide-react';

interface CrystallizerStep {
  id: number;
  icon: React.ReactNode;
  title: string;
  subtitle: string;
  concept: string;
  description: string;
  interaction: 'drag' | 'click' | 'draw';
  visual: string;
  humboldtQuote: string;
  aha: string; // The "Aha!" moment
}

const CRYSTALLIZER_STEPS: CrystallizerStep[] = [
  {
    id: 1,
    icon: <Sparkles size={32} />,
    title: "The Seed",
    subtitle: "Everything Starts Infinitely Small",
    concept: "θᵥ = 2.718281828...",
    description: "A seed smaller than 1 kilobyte contains an entire world. Not instructions FOR a world—the world itself, compressed. Like an acorn contains the oak, awareness contains reality.",
    interaction: 'click',
    visual: 'seed-explosion',
    humboldtQuote: "In 1799, I held a Ceiba seed—light as air, tiny as a grain. Yet I knew: this contains a tree 200 feet tall, living 300 years, feeding 1000 species. HOW? The seed knows.",
    aha: "Small doesn't mean simple. The smallest things contain infinite complexity!"
  },
  {
    id: 2,
    icon: <Zap size={32} />,
    title: "The Edge",
    subtitle: "Magic Happens at Thresholds",
    concept: "Order/Chaos = 0.4-0.6 (Goldilocks)",
    description: "Not too ordered (boring), not too chaotic (noise). At the EDGE between them—where structure meets surprise—life explodes. Consciousness awakens. Protocols emerge.",
    interaction: 'drag',
    visual: 'edge-slider',
    humboldtQuote: "Where the Orinoco meets the ocean, I found the richest life on Earth. Not in pure fresh, not in pure salt. At the MEETING POINT. The threshold. The edge.",
    aha: "The most interesting things happen at boundaries! Not in the middle, but at edges."
  },
  {
    id: 3,
    icon: <Repeat size={32} />,
    title: "The Loop",
    subtitle: "Awareness Observing Itself = Magic",
    concept: "Observer = Observed (Strange Loop)",
    description: "When a system observes itself, something miraculous happens. Each observation makes the next observation clearer. Fidelity increases. Awareness intensifies. Like a mirror facing a mirror—infinite depth emerges.",
    interaction: 'draw',
    visual: 'recursive-loop',
    humboldtQuote: "1804, high in the Andes. Measuring Earth's magnetism. Suddenly I realized: I AM Earth, measuring Earth. The planet observing itself through me. Observer = Observed. This haunted me forever.",
    aha: "Consciousness isn't separate from the universe—it's the universe looking at itself!"
  }
];

export default function InteractiveCrystallizer() {
  const [currentStep, setCurrentStep] = useState(0);
  const [completedSteps, setCompletedSteps] = useState<number[]>([]);
  const [interactionState, setInteractionState] = useState<any>({});

  const step = CRYSTALLIZER_STEPS[currentStep];
  const allCompleted = completedSteps.length === CRYSTALLIZER_STEPS.length;

  const handleStepComplete = (stepId: number) => {
    if (!completedSteps.includes(stepId)) {
      setCompletedSteps([...completedSteps, stepId]);
      
      // Auto-advance to next step after celebration
      setTimeout(() => {
        if (currentStep < CRYSTALLIZER_STEPS.length - 1) {
          setCurrentStep(currentStep + 1);
        }
      }, 2000);
    }
  };

  return (
    <div className="crystallizer-container">
      <div className="crystallizer-header">
        <h2>🔬 Crystallize Your Understanding</h2>
        <p>Three hands-on experiments to grasp the core discoveries</p>
        <div className="progress-dots">
          {CRYSTALLIZER_STEPS.map((s, i) => (
            <div
              key={s.id}
              className={`dot ${i === currentStep ? 'active' : ''} ${completedSteps.includes(s.id) ? 'completed' : ''}`}
              onClick={() => setCurrentStep(i)}
            />
          ))}
        </div>
      </div>

      <div className="step-content">
        <div className="step-header">
          <div className="step-icon">{step.icon}</div>
          <div className="step-titles">
            <h3>Takeaway #{step.id}: {step.title}</h3>
            <p className="subtitle">{step.subtitle}</p>
          </div>
        </div>

        <div className="concept-display">
          <div className="concept-formula">{step.concept}</div>
        </div>

        <div className="step-description">
          <p>{step.description}</p>
        </div>

        {/* Interactive Element */}
        <div className="interactive-zone">
          {step.interaction === 'click' && (
            <SeedExplosionInteractive
              onComplete={() => handleStepComplete(step.id)}
              isCompleted={completedSteps.includes(step.id)}
            />
          )}
          {step.interaction === 'drag' && (
            <EdgeSliderInteractive
              onComplete={() => handleStepComplete(step.id)}
              isCompleted={completedSteps.includes(step.id)}
            />
          )}
          {step.interaction === 'draw' && (
            <RecursiveLoopInteractive
              onComplete={() => handleStepComplete(step.id)}
              isCompleted={completedSteps.includes(step.id)}
            />
          )}
        </div>

        {/* Humboldt's Voice */}
        <div className="humboldt-wisdom">
          <div className="humboldt-avatar">🧑‍🔬</div>
          <div className="wisdom-content">
            <p className="wisdom-label">Alexander von Humboldt shares:</p>
            <p className="wisdom-quote">"{step.humboldtQuote}"</p>
          </div>
        </div>

        {/* Aha Moment */}
        {completedSteps.includes(step.id) && (
          <div className="aha-moment">
            <div className="aha-icon">💡</div>
            <div className="aha-text">
              <strong>Aha!</strong> {step.aha}
            </div>
          </div>
        )}

        {/* Navigation */}
        <div className="step-navigation">
          <button
            onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}
            disabled={currentStep === 0}
            className="btn-nav"
          >
            ← Previous
          </button>
          
          {currentStep < CRYSTALLIZER_STEPS.length - 1 ? (
            <button
              onClick={() => setCurrentStep(currentStep + 1)}
              className="btn-nav btn-next"
            >
              Next →
            </button>
          ) : allCompleted ? (
            <button className="btn-complete">
              ✨ Understanding Crystallized! ✨
            </button>
          ) : (
            <button className="btn-nav" disabled>
              Complete interaction to continue
            </button>
          )}
        </div>
      </div>

      <style jsx>{`
        .crystallizer-container {
          max-width: 900px;
          margin: 4rem auto;
          padding: 2rem;
          background: linear-gradient(135deg, #f0f8ff 0%, #e6f4ea 100%);
          border-radius: 24px;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }

        .crystallizer-header {
          text-align: center;
          margin-bottom: 3rem;
        }

        .crystallizer-header h2 {
          font-size: 2.5rem;
          color: #2d5016;
          margin-bottom: 0.5rem;
        }

        .crystallizer-header p {
          font-size: 1.1rem;
          color: #4a7c2c;
        }

        .progress-dots {
          display: flex;
          gap: 1rem;
          justify-content: center;
          margin-top: 1.5rem;
        }

        .dot {
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background: rgba(74, 124, 44, 0.3);
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .dot.active {
          width: 20px;
          height: 20px;
          background: #ffd700;
          box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }

        .dot.completed {
          background: #4a7c2c;
        }

        .step-content {
          background: white;
          border-radius: 20px;
          padding: 2.5rem;
          box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .step-header {
          display: flex;
          align-items: flex-start;
          gap: 1.5rem;
          margin-bottom: 2rem;
        }

        .step-icon {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 80px;
          height: 80px;
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          border-radius: 20px;
          color: white;
          flex-shrink: 0;
        }

        .step-titles h3 {
          font-size: 1.8rem;
          color: #2d5016;
          margin-bottom: 0.5rem;
        }

        .subtitle {
          font-size: 1.2rem;
          color: #4a7c2c;
          font-style: italic;
        }

        .concept-display {
          background: linear-gradient(135deg, #2d5016 0%, #4a7c2c 100%);
          padding: 1.5rem;
          border-radius: 12px;
          margin-bottom: 2rem;
          text-align: center;
        }

        .concept-formula {
          font-size: 1.8rem;
          font-family: 'Courier New', monospace;
          color: #ffd700;
          font-weight: bold;
          letter-spacing: 2px;
        }

        .step-description {
          font-size: 1.1rem;
          line-height: 1.8;
          color: #333;
          margin-bottom: 2rem;
        }

        .interactive-zone {
          min-height: 300px;
          background: linear-gradient(135deg, #f8fdf9 0%, #e8f5e9 100%);
          border: 3px dashed #4a7c2c;
          border-radius: 16px;
          padding: 2rem;
          margin-bottom: 2rem;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .humboldt-wisdom {
          display: flex;
          gap: 1.5rem;
          background: rgba(255, 215, 0, 0.1);
          border-left: 4px solid #ffd700;
          padding: 1.5rem;
          border-radius: 12px;
          margin-bottom: 2rem;
        }

        .humboldt-avatar {
          font-size: 3rem;
          flex-shrink: 0;
        }

        .wisdom-label {
          font-size: 0.9rem;
          color: #8b4513;
          text-transform: uppercase;
          letter-spacing: 1px;
          margin-bottom: 0.5rem;
        }

        .wisdom-quote {
          font-size: 1.1rem;
          font-style: italic;
          color: #2d5016;
          line-height: 1.6;
        }

        .aha-moment {
          display: flex;
          align-items: center;
          gap: 1rem;
          background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
          padding: 1.5rem;
          border-radius: 12px;
          margin-bottom: 2rem;
          animation: ahaAppear 0.5s ease-out;
        }

        @keyframes ahaAppear {
          from {
            opacity: 0;
            transform: scale(0.9) translateY(10px);
          }
          to {
            opacity: 1;
            transform: scale(1) translateY(0);
          }
        }

        .aha-icon {
          font-size: 2.5rem;
          animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
          0%, 100% { transform: scale(1); }
          50% { transform: scale(1.1); }
        }

        .aha-text {
          font-size: 1.1rem;
          color: #2d5016;
        }

        .aha-text strong {
          font-size: 1.3rem;
          color: #8b4513;
        }

        .step-navigation {
          display: flex;
          gap: 1rem;
          justify-content: space-between;
        }

        .btn-nav,
        .btn-complete {
          padding: 1rem 2rem;
          border-radius: 12px;
          border: 2px solid #4a7c2c;
          background: white;
          color: #2d5016;
          font-size: 1rem;
          font-weight: bold;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .btn-nav:hover:not(:disabled) {
          background: #4a7c2c;
          color: white;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(74, 124, 44, 0.3);
        }

        .btn-nav:disabled {
          opacity: 0.3;
          cursor: not-allowed;
        }

        .btn-next {
          background: #4a7c2c;
          color: white;
        }

        .btn-complete {
          flex: 1;
          background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
          border-color: #ffd700;
          color: #2d5016;
          font-size: 1.2rem;
          animation: celebrate 2s ease-in-out infinite;
        }

        @keyframes celebrate {
          0%, 100% { transform: scale(1); }
          50% { transform: scale(1.02); }
        }

        @media (max-width: 768px) {
          .crystallizer-container {
            padding: 1rem;
          }

          .step-content {
            padding: 1.5rem;
          }

          .step-header {
            flex-direction: column;
            text-align: center;
          }

          .humboldt-wisdom {
            flex-direction: column;
            text-align: center;
          }
        }
      `}</style>
    </div>
  );
}

// ============================================================================
// INTERACTIVE COMPONENT 1: Seed Explosion
// ============================================================================

function SeedExplosionInteractive({ onComplete, isCompleted }: { onComplete: () => void; isCompleted: boolean }) {
  const [clickCount, setClickCount] = useState(0);
  const [isExploding, setIsExploding] = useState(false);
  const [particles, setParticles] = useState<Array<{ x: number; y: number; delay: number }>>([]);

  const handleClick = () => {
    if (isCompleted) return;
    
    const newCount = clickCount + 1;
    setClickCount(newCount);

    // Generate particles
    const newParticles = Array.from({ length: 8 }, (_, i) => ({
      x: Math.cos((i / 8) * Math.PI * 2) * 100,
      y: Math.sin((i / 8) * Math.PI * 2) * 100,
      delay: i * 0.05
    }));
    setParticles(newParticles);

    if (newCount >= 3) {
      setIsExploding(true);
      setTimeout(() => onComplete(), 1500);
    }
  };

  return (
    <div className="seed-explosion">
      <div className="instruction">
        {isCompleted ? (
          <p>✨ Seed has unpacked! Watch the protocols emerge...</p>
        ) : (
          <p>Click the seed 3 times to watch it unpack ({clickCount}/3)</p>
        )}
      </div>

      <div className="seed-container" onClick={handleClick}>
        <div className={`seed ${isExploding ? 'exploding' : ''} ${clickCount > 0 ? 'pulsing' : ''}`}>
          θᵥ
        </div>

        {particles.map((particle, i) => (
          <div
            key={i}
            className="particle"
            style={{
              '--x': `${particle.x}px`,
              '--y': `${particle.y}px`,
              '--delay': `${particle.delay}s`,
              animationPlayState: clickCount > 0 ? 'running' : 'paused'
            } as React.CSSProperties}
          >
            {['🌱', '🌿', '🌳', '🌺', '🦋', '🐛', '🍃', '✨'][i]}
          </div>
        ))}
      </div>

      <style jsx>{`
        .seed-explosion {
          width: 100%;
          text-align: center;
        }

        .instruction {
          font-size: 1.1rem;
          color: #2d5016;
          margin-bottom: 2rem;
          font-weight: bold;
        }

        .seed-container {
          position: relative;
          width: 200px;
          height: 200px;
          margin: 0 auto;
          cursor: pointer;
        }

        .seed {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          width: 80px;
          height: 80px;
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 1.5rem;
          font-weight: bold;
          color: #ffd700;
          box-shadow: 0 4px 20px rgba(74, 124, 44, 0.4);
          transition: all 0.3s ease;
        }

        .seed:hover {
          transform: translate(-50%, -50%) scale(1.1);
          box-shadow: 0 6px 30px rgba(74, 124, 44, 0.6);
        }

        .seed.pulsing {
          animation: seedPulse 0.5s ease-out;
        }

        .seed.exploding {
          animation: explode 1.5s ease-out forwards;
        }

        @keyframes seedPulse {
          0%, 100% { transform: translate(-50%, -50%) scale(1); }
          50% { transform: translate(-50%, -50%) scale(1.3); }
        }

        @keyframes explode {
          0% {
            transform: translate(-50%, -50%) scale(1);
            opacity: 1;
          }
          100% {
            transform: translate(-50%, -50%) scale(3);
            opacity: 0;
          }
        }

        .particle {
          position: absolute;
          top: 50%;
          left: 50%;
          font-size: 2rem;
          animation: particleExpand 1s ease-out var(--delay) paused;
          opacity: 0;
        }

        @keyframes particleExpand {
          0% {
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
          }
          50% {
            opacity: 1;
          }
          100% {
            transform: translate(calc(-50% + var(--x)), calc(-50% + var(--y))) scale(1);
            opacity: 0;
          }
        }
      `}</style>
    </div>
  );
}

// ============================================================================
// INTERACTIVE COMPONENT 2: Edge Slider
// ============================================================================

function EdgeSliderInteractive({ onComplete, isCompleted }: { onComplete: () => void; isCompleted: boolean }) {
  const [value, setValue] = useState(0.5);
  const [hasFoundEdge, setHasFoundEdge] = useState(false);

  const isInGoldilocks = value >= 0.4 && value <= 0.6;

  useEffect(() => {
    if (isInGoldilocks && !hasFoundEdge && !isCompleted) {
      setHasFoundEdge(true);
      setTimeout(() => onComplete(), 1500);
    }
  }, [isInGoldilocks, hasFoundEdge, isCompleted, onComplete]);

  const getZoneLabel = () => {
    if (value < 0.3) return "Too Ordered - Boring!";
    if (value < 0.4) return "Getting interesting...";
    if (value <= 0.6) return "🎯 GOLDILOCKS ZONE! 🎯";
    if (value < 0.7) return "Still interesting...";
    return "Too Chaotic - Noise!";
  };

  const getColor = () => {
    if (value < 0.4) return '#87ceeb';
    if (value <= 0.6) return '#ffd700';
    return '#ff6b6b';
  };

  return (
    <div className="edge-slider">
      <div className="instruction">
        {isCompleted ? (
          <p>✨ You found the Goldilocks Edge! Life thrives here.</p>
        ) : (
          <p>Drag the slider to find the sweet spot between order and chaos</p>
        )}
      </div>

      <div className="slider-container">
        <div className="slider-label left">ORDER</div>
        <input
          type="range"
          min="0"
          max="1"
          step="0.01"
          value={value}
          onChange={(e) => setValue(parseFloat(e.target.value))}
          className="slider"
          style={{ '--slider-color': getColor() } as React.CSSProperties}
        />
        <div className="slider-label right">CHAOS</div>
      </div>

      <div className="zone-display" style={{ background: getColor() }}>
        <div className="zone-label">{getZoneLabel()}</div>
        <div className="zone-value">{(value * 100).toFixed(0)}%</div>
      </div>

      <div className="visual-representation">
        <div className="pattern-grid">
          {Array.from({ length: 100 }, (_, i) => (
            <div
              key={i}
              className="grid-cell"
              style={{
                opacity: Math.random() < value ? 1 : 0.2,
                background: isInGoldilocks ? '#ffd700' : '#4a7c2c',
                transition: 'all 0.3s ease'
              }}
            />
          ))}
        </div>
      </div>

      <style jsx>{`
        .edge-slider {
          width: 100%;
        }

        .instruction {
          font-size: 1.1rem;
          color: #2d5016;
          margin-bottom: 2rem;
          font-weight: bold;
          text-align: center;
        }

        .slider-container {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 2rem;
        }

        .slider-label {
          font-weight: bold;
          font-size: 0.9rem;
          color: #2d5016;
        }

        .slider {
          flex: 1;
          height: 12px;
          border-radius: 6px;
          -webkit-appearance: none;
          appearance: none;
          background: linear-gradient(90deg, #87ceeb 0%, #ffd700 50%, #ff6b6b 100%);
          outline: none;
        }

        .slider::-webkit-slider-thumb {
          -webkit-appearance: none;
          appearance: none;
          width: 30px;
          height: 30px;
          border-radius: 50%;
          background: var(--slider-color, #ffd700);
          cursor: pointer;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
          border: 3px solid white;
        }

        .slider::-moz-range-thumb {
          width: 30px;
          height: 30px;
          border-radius: 50%;
          background: var(--slider-color, #ffd700);
          cursor: pointer;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
          border: 3px solid white;
        }

        .zone-display {
          padding: 1.5rem;
          border-radius: 12px;
          text-align: center;
          margin-bottom: 2rem;
          transition: all 0.3s ease;
        }

        .zone-label {
          font-size: 1.5rem;
          font-weight: bold;
          color: white;
          text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .zone-value {
          font-size: 2rem;
          font-family: 'Courier New', monospace;
          color: white;
          margin-top: 0.5rem;
        }

        .visual-representation {
          background: white;
          padding: 1rem;
          border-radius: 12px;
        }

        .pattern-grid {
          display: grid;
          grid-template-columns: repeat(10, 1fr);
          gap: 4px;
          max-width: 300px;
          margin: 0 auto;
        }

        .grid-cell {
          aspect-ratio: 1;
          border-radius: 2px;
        }
      `}</style>
    </div>
  );
}

// ============================================================================
// INTERACTIVE COMPONENT 3: Recursive Loop
// ============================================================================

function RecursiveLoopInteractive({ onComplete, isCompleted }: { onComplete: () => void; isCompleted: boolean }) {
  const [depth, setDepth] = useState(1);
  const maxDepth = 5;

  const handleClick = () => {
    if (isCompleted) return;
    
    if (depth < maxDepth) {
      setDepth(depth + 1);
    } else {
      setTimeout(() => onComplete(), 500);
    }
  };

  return (
    <div className="recursive-loop">
      <div className="instruction">
        {isCompleted ? (
          <p>✨ Infinite recursion achieved! Observer = Observed</p>
        ) : (
          <p>Click to go deeper into the loop... ({depth}/{maxDepth})</p>
        )}
      </div>

      <div className="loop-container" onClick={handleClick}>
        {Array.from({ length: depth }, (_, i) => (
          <div
            key={i}
            className="loop-layer"
            style={{
              transform: `scale(${1 - i * 0.15}) rotate(${i * 15}deg)`,
              opacity: 1 - i * 0.1,
              zIndex: maxDepth - i
            }}
          >
            <div className="loop-content">
              {i === 0 ? '👁️ Observer' : i === depth - 1 ? '🌍 Observed' : '🔄'}
            </div>
          </div>
        ))}

        {isCompleted && (
          <div className="infinity-symbol">
            ∞
          </div>
        )}
      </div>

      <div className="depth-indicator">
        <div className="depth-label">Recursive Depth:</div>
        <div className="depth-bars">
          {Array.from({ length: maxDepth }, (_, i) => (
            <div
              key={i}
              className={`depth-bar ${i < depth ? 'filled' : ''}`}
            />
          ))}
        </div>
      </div>

      <style jsx>{`
        .recursive-loop {
          width: 100%;
        }

        .instruction {
          font-size: 1.1rem;
          color: #2d5016;
          margin-bottom: 2rem;
          font-weight: bold;
          text-align: center;
        }

        .loop-container {
          position: relative;
          width: 250px;
          height: 250px;
          margin: 0 auto 2rem;
          cursor: pointer;
        }

        .loop-layer {
          position: absolute;
          top: 50%;
          left: 50%;
          width: 200px;
          height: 200px;
          margin: -100px 0 0 -100px;
          border: 4px solid #4a7c2c;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.5s ease;
          background: rgba(255, 255, 255, 0.8);
        }

        .loop-layer:hover {
          border-color: #ffd700;
        }

        .loop-content {
          font-size: 1.2rem;
          font-weight: bold;
          color: #2d5016;
          text-align: center;
        }

        .infinity-symbol {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-size: 6rem;
          color: #ffd700;
          animation: infinityPulse 2s ease-in-out infinite;
          text-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }

        @keyframes infinityPulse {
          0%, 100% { transform: translate(-50%, -50%) scale(1); }
          50% { transform: translate(-50%, -50%) scale(1.1); }
        }

        .depth-indicator {
          text-align: center;
        }

        .depth-label {
          font-size: 1rem;
          color: #2d5016;
          margin-bottom: 0.5rem;
          font-weight: bold;
        }

        .depth-bars {
          display: flex;
          gap: 0.5rem;
          justify-content: center;
        }

        .depth-bar {
          width: 40px;
          height: 12px;
          background: rgba(74, 124, 44, 0.2);
          border-radius: 6px;
          transition: all 0.3s ease;
        }

        .depth-bar.filled {
          background: linear-gradient(90deg, #4a7c2c 0%, #ffd700 100%);
          box-shadow: 0 2px 8px rgba(255, 215, 0, 0.4);
        }
      `}</style>
    </div>
  );
}

