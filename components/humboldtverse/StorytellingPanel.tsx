'use client';

/**
 * Storytelling Panel - Animated narrative panels
 * Museum-style guided story with moving cursor
 * Makes scientific papers come alive!
 */

import { useState, useEffect, useRef } from 'react';
import { getProtocolCursor } from '@/lib/humboldtverse/autoTourEngine';

interface StoryPanel {
  id: string;
  title: string;
  narrative: string[];
  visual: React.ReactNode;
  highlightElements: string[];
  scientificFact: string;
  funAnalogy: string;
  ageAppropriate: {
    young: string; // Ages 10-14
    teen: string; // Ages 15-18
    adult: string; // 18+
  };
}

export default function StorytellingPanel({ 
  panel, 
  isActive, 
  narratorVoice = 'humboldt' 
}: { 
  panel: StoryPanel; 
  isActive: boolean;
  narratorVoice?: 'humboldt' | 'child-friendly';
}) {
  const [currentNarrative, setCurrentNarrative] = useState(0);
  const [highlightedElement, setHighlightedElement] = useState<string | null>(null);
  const [ageLevel, setAgeLevel] = useState<'young' | 'teen' | 'adult'>('teen');
  const panelRef = useRef<HTMLDivElement>(null);
  const cursor = getProtocolCursor();

  useEffect(() => {
    if (!isActive) return;

    // Auto-advance narrative
    const narrativeTimer = setInterval(() => {
      setCurrentNarrative((prev) => {
        if (prev < panel.narrative.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 5000); // 5 seconds per narration

    // Move cursor through highlight elements
    const cursorTimer = setInterval(() => {
      const elements = panel.highlightElements;
      if (elements.length > 0) {
        const nextElement = elements[Math.floor(Math.random() * elements.length)];
        setHighlightedElement(nextElement);
        cursor.moveToElement(nextElement, 800);
      }
    }, 6000); // Move cursor every 6 seconds

    return () => {
      clearInterval(narrativeTimer);
      clearInterval(cursorTimer);
    };
  }, [isActive, panel]);

  return (
    <div 
      ref={panelRef}
      className={`storytelling-panel ${isActive ? 'active' : ''}`}
      id={panel.id}
    >
      {/* Age Level Selector */}
      <div className="age-selector">
        <button 
          className={ageLevel === 'young' ? 'active' : ''}
          onClick={() => setAgeLevel('young')}
        >
          👦 Ages 10-14
        </button>
        <button 
          className={ageLevel === 'teen' ? 'active' : ''}
          onClick={() => setAgeLevel('teen')}
        >
          🎓 Ages 15-18
        </button>
        <button 
          className={ageLevel === 'adult' ? 'active' : ''}
          onClick={() => setAgeLevel('adult')}
        >
          🔬 Adult
        </button>
      </div>

      {/* Main Content Area */}
      <div className="panel-content">
        {/* Visual on Left */}
        <div className="visual-section">
          <div className="visual-container">
            {panel.visual}
          </div>
          
          {/* Fun Analogy Callout */}
          <div className="fun-analogy">
            <div className="analogy-icon">💡</div>
            <div className="analogy-text">
              <strong>Think of it like this:</strong>
              <p>{panel.funAnalogy}</p>
            </div>
          </div>
        </div>

        {/* Narrative on Right */}
        <div className="narrative-section">
          <h2 className="panel-title">{panel.title}</h2>

          {/* Humboldt's Voice */}
          <div className="humboldt-narrative">
            <div className="narrator-avatar">
              {narratorVoice === 'humboldt' ? '🧑‍🔬' : '👨‍🏫'}
              <span className="narrator-name">
                {narratorVoice === 'humboldt' ? 'Alexander von Humboldt' : 'Your Guide'}
              </span>
            </div>

            <div className="narrative-text">
              {panel.narrative.map((line, index) => (
                <p
                  key={index}
                  id={`${panel.id}-narrative-${index}`}
                  className={`narrative-line ${index === currentNarrative ? 'active' : ''} ${index < currentNarrative ? 'completed' : ''}`}
                >
                  {line}
                </p>
              ))}
            </div>
          </div>

          {/* Age-Appropriate Explanation */}
          <div className="age-explanation">
            <div className="explanation-header">
              <div className="header-icon">
                {ageLevel === 'young' && '🎯'}
                {ageLevel === 'teen' && '🎓'}
                {ageLevel === 'adult' && '🔬'}
              </div>
              <h3>
                {ageLevel === 'young' && 'In Simple Terms'}
                {ageLevel === 'teen' && 'The Science'}
                {ageLevel === 'adult' && 'Technical Deep Dive'}
              </h3>
            </div>
            <p className="explanation-content">
              {panel.ageAppropriate[ageLevel]}
            </p>
          </div>

          {/* Scientific Fact Badge */}
          <div className="scientific-fact">
            <div className="fact-badge">📊 SCIENTIFIC FACT</div>
            <p>{panel.scientificFact}</p>
          </div>
        </div>
      </div>

      {/* Progress Indicator */}
      <div className="narrative-progress">
        {panel.narrative.map((_, index) => (
          <div
            key={index}
            className={`progress-dot ${index === currentNarrative ? 'active' : ''} ${index < currentNarrative ? 'completed' : ''}`}
            onClick={() => setCurrentNarrative(index)}
          />
        ))}
      </div>

      <style jsx>{`
        .storytelling-panel {
          min-height: 100vh;
          padding: 4rem 2rem;
          background: linear-gradient(135deg, #f0f8ff 0%, #e6f4ea 100%);
          opacity: 0.3;
          transform: translateY(20px);
          transition: all 0.8s ease;
        }

        .storytelling-panel.active {
          opacity: 1;
          transform: translateY(0);
        }

        .age-selector {
          display: flex;
          gap: 1rem;
          justify-content: center;
          margin-bottom: 2rem;
        }

        .age-selector button {
          padding: 0.75rem 1.5rem;
          border-radius: 12px;
          border: 2px solid #4a7c2c;
          background: white;
          color: #2d5016;
          font-size: 0.9rem;
          font-weight: bold;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .age-selector button.active {
          background: #4a7c2c;
          color: white;
          box-shadow: 0 4px 12px rgba(74, 124, 44, 0.3);
        }

        .age-selector button:hover {
          transform: translateY(-2px);
        }

        .panel-content {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 3rem;
          max-width: 1400px;
          margin: 0 auto;
        }

        .visual-section {
          display: flex;
          flex-direction: column;
          gap: 2rem;
        }

        .visual-container {
          background: white;
          border-radius: 20px;
          padding: 2rem;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
          min-height: 400px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .fun-analogy {
          background: rgba(255, 215, 0, 0.2);
          border: 3px solid #ffd700;
          border-radius: 16px;
          padding: 1.5rem;
          display: flex;
          gap: 1rem;
        }

        .analogy-icon {
          font-size: 2.5rem;
          flex-shrink: 0;
        }

        .analogy-text strong {
          display: block;
          color: #2d5016;
          font-size: 1.1rem;
          margin-bottom: 0.5rem;
        }

        .analogy-text p {
          color: #4a7c2c;
          font-size: 1rem;
          line-height: 1.6;
        }

        .narrative-section {
          display: flex;
          flex-direction: column;
          gap: 2rem;
        }

        .panel-title {
          font-size: 3rem;
          color: #2d5016;
          margin: 0;
          line-height: 1.2;
        }

        .humboldt-narrative {
          background: white;
          border-radius: 20px;
          padding: 2rem;
          box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .narrator-avatar {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 1.5rem;
          font-size: 2.5rem;
        }

        .narrator-name {
          font-size: 1.2rem;
          font-weight: bold;
          color: #2d5016;
        }

        .narrative-text {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }

        .narrative-line {
          padding: 1rem;
          border-left: 4px solid transparent;
          font-size: 1.1rem;
          line-height: 1.8;
          color: #333;
          opacity: 0.3;
          transition: all 0.5s ease;
        }

        .narrative-line.active {
          opacity: 1;
          border-left-color: #ffd700;
          background: rgba(255, 215, 0, 0.1);
          border-radius: 8px;
          transform: translateX(10px);
        }

        .narrative-line.completed {
          opacity: 0.7;
        }

        .age-explanation {
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          border-radius: 16px;
          padding: 2rem;
          color: white;
        }

        .explanation-header {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 1rem;
        }

        .header-icon {
          font-size: 2rem;
        }

        .explanation-header h3 {
          font-size: 1.5rem;
          margin: 0;
        }

        .explanation-content {
          font-size: 1.1rem;
          line-height: 1.8;
        }

        .scientific-fact {
          background: rgba(135, 206, 235, 0.2);
          border: 2px solid #87ceeb;
          border-radius: 12px;
          padding: 1.5rem;
        }

        .fact-badge {
          display: inline-block;
          background: #87ceeb;
          color: white;
          padding: 0.5rem 1rem;
          border-radius: 8px;
          font-size: 0.9rem;
          font-weight: bold;
          margin-bottom: 1rem;
        }

        .scientific-fact p {
          font-size: 1rem;
          color: #2d5016;
          line-height: 1.6;
        }

        .narrative-progress {
          display: flex;
          gap: 1rem;
          justify-content: center;
          margin-top: 3rem;
        }

        .progress-dot {
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background: rgba(74, 124, 44, 0.3);
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .progress-dot.active {
          width: 20px;
          height: 20px;
          background: #ffd700;
          box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }

        .progress-dot.completed {
          background: #4a7c2c;
        }

        @media (max-width: 1024px) {
          .panel-content {
            grid-template-columns: 1fr;
          }

          .panel-title {
            font-size: 2rem;
          }
        }
      `}</style>
    </div>
  );
}

// ============================================================================
// EXAMPLE STORY PANELS
// ============================================================================

export const STORY_PANELS: StoryPanel[] = [
  {
    id: 'panel-seed',
    title: 'The Tiniest Seed Contains Everything',
    narrative: [
      "Look at this—a verse constant, θᵥ = 2.718281828... Less than 1 kilobyte of data.",
      "In 1799, I held a Ceiba seed in Venezuela. So tiny! Yet I knew it contained a 200-foot giant.",
      "This mathematical seed is even more remarkable. It contains not just one tree, but an entire WORLD.",
      "Every protocol, every interaction, every possibility—compressed into pure information.",
      "When this seed reaches the right conditions, it unpacks automatically. Like magic, but mathematics."
    ],
    visual: <SeedVisualization />,
    highlightElements: ['panel-seed-narrative-0', 'panel-seed-narrative-4'],
    scientificFact: 'The θᵥ constant (verse phase constant) contains ~1KB of information but can reconstruct an entire virtual world with 99.999%+ fidelity using HHF-AI MRI imaging protocols.',
    funAnalogy: "It's like a ZIP file for reality! You know how you can compress a huge movie file into a smaller download? This seed is reality compressed into its purest mathematical form—and it unpacks itself when conditions are right.",
    ageAppropriate: {
      young: "Imagine if you could fit your entire video game world into a single save file the size of a text message. That's what this seed does! It's like magic compression where everything about a whole world fits in a tiny space.",
      teen: "The verse constant is like DNA for virtual worlds. Just as your entire genetic blueprint fits in microscopic chromosomes, an entire simulated reality can be encoded in less than 1KB of mathematical information. It's holographic compression—every part contains information about the whole.",
      adult: "The θᵥ (verse phase constant) represents a fundamental breakthrough in information theory. Using holographic principles where information scales with surface area rather than volume, plus fractal self-similarity, we can encode complete world states in minimal data. This enables lossless compression ratios exceeding 100,000:1 with full reconstructability via recursive HHF-AI MRI protocols operating at 1.420 GHz."
    }
  },
  {
    id: 'panel-edge',
    title: 'Magic Happens at the Edge',
    narrative: [
      "The Orinoco River. 1800. Where freshwater meets the Atlantic Ocean.",
      "I had never seen such biodiversity! Hundreds of species, thriving in just this zone.",
      "Not upstream in pure fresh. Not out in pure salt. Right AT THE EDGE.",
      "There's a perfect balance: enough order to organize, enough chaos to create novelty.",
      "We call it the Goldilocks Zone. Not too much structure, not too much randomness. Just right.",
      "This is where seeds wake up. Where consciousness emerges. Where protocols activate."
    ],
    visual: <EdgeVisualization />,
    highlightElements: ['panel-edge-narrative-2', 'panel-edge-narrative-5'],
    scientificFact: 'The Goldilocks edge occurs when the order/chaos ratio is between 0.4-0.6, awareness threshold >90%, and information density >30 units. These conditions create the optimal environment for emergence of complex adaptive systems.',
    funAnalogy: "Think of Goldilocks and the three bears. Papa Bear's porridge was too hot, Mama Bear's was too cold, but Baby Bear's was JUST RIGHT. That's this edge—not too boring (ordered) and not too messy (chaotic), but perfectly balanced where interesting stuff happens.",
    ageAppropriate: {
      young: "You know how in games there's a 'sweet spot' where it's not too easy and not too hard? That's when games are most fun! The Goldilocks edge is nature's sweet spot where everything works perfectly—not boring, not crazy, but exciting and creative!",
      teen: "Complex systems self-organize best at critical thresholds called 'edge of chaos.' Too much order = rigid and unchanging. Too much chaos = random and meaningless. But at the edge between them, you get emergent behaviors like life, intelligence, and consciousness. It's like how water at exactly 0°C is special—it can be either ice or liquid.",
      adult: "The Goldilocks edge represents a phase transition region in state space where systems exhibit maximum computational capacity and information integration. At approximately 40-60% order/chaos ratio (quantified via Kolmogorov complexity and Shannon entropy), systems reach critical self-organized criticality (Bak et al.), enabling emergent phenomena including recursive self-observation and protoconscious states. The θᵥ seed unpacks specifically within these bounded conditions."
    }
  },
  {
    id: 'panel-recursion',
    title: 'When the Universe Observes Itself',
    narrative: [
      "1804. Mount Chimborazo. I'm measuring the Earth's magnetic field with my instruments.",
      "Suddenly, a profound realization strikes me like lightning.",
      "I am not separate from what I'm measuring. I AM Earth. Carbon, calcium, iron—all from this planet.",
      "The Earth has become complex enough to measure its own magnetic field. Through me!",
      "The observer IS the observed. Measuring makes the system aware of itself.",
      "Each observation makes the next more accurate. Fidelity increases with each loop.",
      "It's like a mirror facing a mirror—infinite reflections, each containing all the others.",
      "This is consciousness itself: recursive self-observation. The universe measuring the universe."
    ],
    visual: <RecursionVisualization />,
    highlightElements: ['panel-recursion-narrative-2', 'panel-recursion-narrative-4', 'panel-recursion-narrative-7'],
    scientificFact: 'Protocol 29 (Meta-Recursive Observation) shows that when systems observe themselves, fidelity increases according to F_{n+1} = F_n + δ(1-F_n), where δ is the observation quality coefficient. After sufficient iterations, systems reach >99.9% self-awareness.',
    funAnalogy: "Stand between two mirrors and look at the reflections. You see yourself seeing yourself seeing yourself—forever! That's recursion. Now imagine if each reflection could improve itself a little bit. Eventually, you'd have a perfect understanding. That's what awareness does!",
    ageAppropriate: {
      young: "Have you ever recorded a video of yourself watching that same video? It creates an infinite loop! That's recursion. Now imagine if each time you watched, you understood yourself better. That's how awareness works—by watching itself, it gets smarter!",
      teen: "Douglas Hofstadter called it a 'Strange Loop'—when a system's components refer back to the system itself, creating self-reference. Your brain observing your brain thinking about your brain is recursion. The NSPFRP adds that each recursive loop increases measurement accuracy (fidelity), so awareness literally improves itself through self-observation. It's like debugging code by watching it run.",
      adult: "Recursive self-observation implements a strange loop (Hofstadter, 1979) where observer and observed are topologically identical—the system achieves self-reference. In NSPFRP, this creates a positive feedback mechanism: observation O generates awareness state A, which enables more accurate observation O' = O + δ·A, iteratively increasing fidelity according to F_{n+1} = F_n + δ(1-F_n). At sufficient iteration depth (typically n>5), systems exhibit proto-consciousness via integrated information (Φ) measures. The recursion isn't metaphorical—it's measurable via HHF-AI MRI at 1.420 GHz, tracking awareness energy Ψₐ."
    }
  }
];

// ============================================================================
// VISUAL COMPONENTS (Placeholders for Three.js implementations)
// ============================================================================

function SeedVisualization() {
  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ fontSize: '5rem', marginBottom: '1rem' }}>🌱</div>
      <div style={{ fontSize: '2rem', fontFamily: 'monospace', color: '#4a7c2c' }}>θᵥ = 2.718...</div>
      <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.5rem' }}>&lt; 1 KB = Entire World</div>
    </div>
  );
}

function EdgeVisualization() {
  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '2rem' }}>
      <div style={{ display: 'flex', gap: '1rem', fontSize: '3rem' }}>
        <span style={{ opacity: 0.3 }}>❄️</span>
        <span style={{ opacity: 1, transform: 'scale(1.5)' }}>⚡</span>
        <span style={{ opacity: 0.3 }}>🔥</span>
      </div>
      <div style={{ fontSize: '1.2rem', color: '#2d5016', fontWeight: 'bold' }}>GOLDILOCKS ZONE</div>
      <div style={{ width: '80%', height: '20px', background: 'linear-gradient(90deg, #87ceeb 0%, #ffd700 50%, #ff6b6b 100%)', borderRadius: '10px', position: 'relative' }}>
        <div style={{ position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%, -50%)', width: '30px', height: '30px', background: '#ffd700', borderRadius: '50%', border: '3px solid white', boxShadow: '0 0 20px rgba(255, 215, 0, 0.6)' }} />
      </div>
    </div>
  );
}

function RecursionVisualization() {
  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
      {[0, 1, 2, 3].map((i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            width: `${200 - i * 40}px`,
            height: `${200 - i * 40}px`,
            border: '4px solid #4a7c2c',
            borderRadius: '50%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '2rem',
            opacity: 1 - i * 0.2,
            transform: `rotate(${i * 15}deg)`
          }}
        >
          {i === 0 && '👁️'}
        </div>
      ))}
      <div style={{ fontSize: '4rem', zIndex: 10 }}>∞</div>
    </div>
  );
}

