'use client';

/**
 * AlexandrevonHumboldtverse - Natural Systems Protocol Expedition
 * Interactive Museum-Style Science Communication
 * Bringing scientific papers to life for all ages
 */

import { useState, useEffect } from 'react';
import { Compass, Book, Sparkles, ArrowLeft } from 'lucide-react';
import Link from 'next/link';
import AutoTourControl from '@/components/alexandrevonhumboldtverse/AutoTourControl';
import StorytellingPanel, { STORY_PANELS } from '@/components/alexandrevonhumboldtverse/StorytellingPanel';
import InteractiveCrystallizer from '@/components/alexandrevonhumboldtverse/InteractiveCrystallizer';
import { humboldtSpeak } from '@/lib/alexandrevonhumboldtverse/humboldtPersonality';

export default function AlexandrevonHumboldtversePage() {
  const [hasStarted, setHasStarted] = useState(false);
  const [currentPanel, setCurrentPanel] = useState(0);
  const [showCrystallizer, setShowCrystallizer] = useState(false);

  const greeting = humboldtSpeak({ topic: 'greeting' });

  return (
    <div className="alexandrevonhumboldtverse-page">
      {/* Navigation Header */}
      <header className="humboldt-header">
        <Link href="/" className="back-button">
          <ArrowLeft size={20} />
          <span>Back to MarkTwainVerse</span>
        </Link>
        
        <div className="header-title">
          <Compass className="compass-icon" />
          <h1>AlexandrevonHumboldtverse Expedition</h1>
        </div>

        <button 
          onClick={() => setShowCrystallizer(!showCrystallizer)}
          className="crystallizer-toggle"
        >
          <Sparkles size={20} />
          <span>Key Takeaways</span>
        </button>
      </header>

      {!hasStarted ? (
        // ============================================================================
        // LANDING / INVITATION SCREEN
        // ============================================================================
        <div className="landing-screen">
          <div className="landing-content">
            <div className="humboldt-portrait">
              <div className="portrait-frame">
                🧑‍🔬
              </div>
              <div className="portrait-glow" />
            </div>

            <h1 className="expedition-title">
              Natural Systems Protocol
              <span className="subtitle">First Recursive Protocol Engine</span>
            </h1>

            <div className="invitation">
              <div className="greeting-bubble">
                <p>"{greeting.text}"</p>
                <div className="narrator-tag">— Alexander von Humboldt</div>
              </div>

              <div className="expedition-details">
                <div className="detail-item">
                  <Book size={24} />
                  <div>
                    <strong>6 Interactive Stages</strong>
                    <p>From seed to living world</p>
                  </div>
                </div>
                <div className="detail-item">
                  <Sparkles size={24} />
                  <div>
                    <strong>3 Key Takeaways</strong>
                    <p>Hands-on crystallization</p>
                  </div>
                </div>
                <div className="detail-item">
                  <Compass size={24} />
                  <div>
                    <strong>~7.5 Minutes</strong>
                    <p>Guided auto-tour</p>
                  </div>
                </div>
              </div>

              <div className="age-badges">
                <div className="badge">Ages 10+ Welcome</div>
                <div className="badge">Museum Quality</div>
                <div className="badge">Scientifically Accurate</div>
              </div>

              <button 
                onClick={() => setHasStarted(true)}
                className="begin-button"
              >
                <Compass size={32} />
                <span>Begin Expedition</span>
                <div className="button-shine" />
              </button>

              <p className="footnote">
                🌿 Making scientific papers accessible and exciting for everyone
              </p>
            </div>
          </div>

          <div className="landing-background">
            <div className="floating-element" style={{ '--delay': '0s' } as React.CSSProperties}>🌱</div>
            <div className="floating-element" style={{ '--delay': '2s' } as React.CSSProperties}>🦋</div>
            <div className="floating-element" style={{ '--delay': '4s' } as React.CSSProperties}>🌿</div>
            <div className="floating-element" style={{ '--delay': '1s' } as React.CSSProperties}>🌺</div>
            <div className="floating-element" style={{ '--delay': '3s' } as React.CSSProperties}>🍃</div>
          </div>
        </div>
      ) : (
        // ============================================================================
        // EXPEDITION EXPERIENCE
        // ============================================================================
        <div className="expedition-experience">
          {/* Auto-Tour Control Panel */}
          <AutoTourControl />

          {/* Interactive Crystallizer (Key Takeaways) */}
          {showCrystallizer && (
            <div className="crystallizer-overlay">
              <div className="overlay-content">
                <button 
                  onClick={() => setShowCrystallizer(false)}
                  className="close-crystallizer"
                >
                  ✕
                </button>
                <InteractiveCrystallizer />
              </div>
            </div>
          )}

          {/* Storytelling Panels */}
          <div className="panels-container">
            {STORY_PANELS.map((panel, index) => (
              <StorytellingPanel
                key={panel.id}
                panel={panel}
                isActive={currentPanel === index}
                narratorVoice="humboldt"
              />
            ))}
          </div>

          {/* Panel Navigation */}
          <div className="panel-navigation">
            <button
              onClick={() => setCurrentPanel(Math.max(0, currentPanel - 1))}
              disabled={currentPanel === 0}
              className="nav-button"
            >
              ← Previous Panel
            </button>

            <div className="panel-indicator">
              Panel {currentPanel + 1} of {STORY_PANELS.length}
            </div>

            <button
              onClick={() => setCurrentPanel(Math.min(STORY_PANELS.length - 1, currentPanel + 1))}
              disabled={currentPanel === STORY_PANELS.length - 1}
              className="nav-button"
            >
              Next Panel →
            </button>
          </div>

          {/* Completion Screen */}
          {currentPanel === STORY_PANELS.length - 1 && (
            <div className="completion-screen">
              <h2>🎉 Expedition Complete!</h2>
              <p>You've discovered the Natural Systems Protocol - First Recursive Protocol Engine</p>
              
              <div className="completion-actions">
                <button 
                  onClick={() => setShowCrystallizer(true)}
                  className="action-button primary"
                >
                  <Sparkles size={20} />
                  Review Key Takeaways
                </button>

                <button 
                  onClick={() => { setCurrentPanel(0); window.scrollTo(0, 0); }}
                  className="action-button"
                >
                  <Compass size={20} />
                  Restart Expedition
                </button>

                <Link href="/" className="action-button">
                  <ArrowLeft size={20} />
                  Return to MarkTwainVerse
                </Link>
              </div>

              <div className="share-encouragement">
                <p>✨ Share this expedition with young explorers!</p>
                <p className="small">Making science accessible, one protocol at a time</p>
              </div>
            </div>
          )}
        </div>
      )}

      <style jsx>{`
        .alexandrevonhumboldtverse-page {
          min-height: 100vh;
          background: linear-gradient(135deg, #f0f8ff 0%, #e6f4ea 100%);
        }

        .humboldt-header {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          background: rgba(45, 80, 22, 0.95);
          backdrop-filter: blur(10px);
          padding: 1rem 2rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          z-index: 900;
          border-bottom: 2px solid #4a7c2c;
        }

        .back-button,
        .crystallizer-toggle {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.75rem 1.5rem;
          border-radius: 12px;
          border: 2px solid rgba(255, 255, 255, 0.3);
          background: rgba(255, 255, 255, 0.1);
          color: white;
          text-decoration: none;
          font-weight: bold;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .back-button:hover,
        .crystallizer-toggle:hover {
          background: rgba(255, 255, 255, 0.2);
          border-color: #ffd700;
          transform: translateY(-2px);
        }

        .header-title {
          display: flex;
          align-items: center;
          gap: 1rem;
          color: white;
        }

        .header-title h1 {
          margin: 0;
          font-size: 1.5rem;
        }

        .compass-icon {
          animation: spin 20s linear infinite;
        }

        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }

        .landing-screen {
          position: relative;
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 6rem 2rem 2rem;
          overflow: hidden;
        }

        .landing-content {
          max-width: 900px;
          text-align: center;
          position: relative;
          z-index: 2;
        }

        .humboldt-portrait {
          position: relative;
          width: 200px;
          height: 200px;
          margin: 0 auto 3rem;
        }

        .portrait-frame {
          position: relative;
          width: 100%;
          height: 100%;
          font-size: 10rem;
          z-index: 2;
        }

        .portrait-glow {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          width: 150%;
          height: 150%;
          background: radial-gradient(circle, rgba(255, 215, 0, 0.3) 0%, transparent 70%);
          animation: glow 3s ease-in-out infinite;
        }

        @keyframes glow {
          0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
          50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
        }

        .expedition-title {
          font-size: 3.5rem;
          color: #2d5016;
          margin-bottom: 1rem;
          line-height: 1.2;
        }

        .subtitle {
          display: block;
          font-size: 1.5rem;
          color: #4a7c2c;
          font-style: italic;
          margin-top: 0.5rem;
        }

        .invitation {
          background: white;
          border-radius: 24px;
          padding: 3rem;
          box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
          margin-top: 3rem;
        }

        .greeting-bubble {
          background: rgba(255, 215, 0, 0.1);
          border-left: 4px solid #ffd700;
          padding: 2rem;
          border-radius: 16px;
          margin-bottom: 2rem;
          text-align: left;
        }

        .greeting-bubble p {
          font-size: 1.2rem;
          font-style: italic;
          color: #2d5016;
          line-height: 1.8;
          margin: 0;
        }

        .narrator-tag {
          text-align: right;
          color: #8b4513;
          font-weight: bold;
          margin-top: 1rem;
        }

        .expedition-details {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 2rem;
          margin: 2rem 0;
          padding: 2rem 0;
          border-top: 2px solid #e6f4ea;
          border-bottom: 2px solid #e6f4ea;
        }

        .detail-item {
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
          gap: 1rem;
          color: #4a7c2c;
        }

        .detail-item strong {
          font-size: 1.1rem;
          color: #2d5016;
        }

        .detail-item p {
          font-size: 0.9rem;
          margin: 0;
        }

        .age-badges {
          display: flex;
          gap: 1rem;
          justify-content: center;
          margin: 2rem 0;
        }

        .badge {
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          color: white;
          padding: 0.5rem 1.5rem;
          border-radius: 20px;
          font-size: 0.9rem;
          font-weight: bold;
        }

        .begin-button {
          position: relative;
          display: flex;
          align-items: center;
          gap: 1rem;
          padding: 1.5rem 3rem;
          font-size: 1.5rem;
          font-weight: bold;
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          color: white;
          border: 3px solid #ffd700;
          border-radius: 20px;
          cursor: pointer;
          transition: all 0.3s ease;
          margin: 2rem auto;
          overflow: hidden;
        }

        .begin-button:hover {
          transform: translateY(-4px) scale(1.05);
          box-shadow: 0 10px 40px rgba(255, 215, 0, 0.4);
        }

        .button-shine {
          position: absolute;
          top: 0;
          left: -100%;
          width: 100%;
          height: 100%;
          background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
          animation: shine 3s infinite;
        }

        @keyframes shine {
          0% { left: -100%; }
          100% { left: 200%; }
        }

        .footnote {
          font-size: 0.9rem;
          color: #4a7c2c;
          margin-top: 1rem;
        }

        .landing-background {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          pointer-events: none;
          overflow: hidden;
        }

        .floating-element {
          position: absolute;
          font-size: 3rem;
          animation: float 10s ease-in-out infinite;
          animation-delay: var(--delay);
          opacity: 0.3;
        }

        .floating-element:nth-child(1) { top: 10%; left: 10%; }
        .floating-element:nth-child(2) { top: 20%; right: 15%; }
        .floating-element:nth-child(3) { bottom: 15%; left: 20%; }
        .floating-element:nth-child(4) { top: 60%; right: 10%; }
        .floating-element:nth-child(5) { bottom: 30%; right: 30%; }

        @keyframes float {
          0%, 100% { transform: translateY(0) rotate(0deg); }
          50% { transform: translateY(-30px) rotate(10deg); }
        }

        .expedition-experience {
          padding-top: 5rem;
          min-height: 100vh;
        }

        .crystallizer-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.8);
          backdrop-filter: blur(10px);
          z-index: 950;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 2rem;
          overflow-y: auto;
        }

        .overlay-content {
          position: relative;
          width: 100%;
          max-width: 1000px;
        }

        .close-crystallizer {
          position: absolute;
          top: -3rem;
          right: 0;
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background: white;
          border: none;
          font-size: 1.5rem;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .close-crystallizer:hover {
          transform: rotate(90deg) scale(1.1);
          background: #ff6b6b;
          color: white;
        }

        .panels-container {
          margin-bottom: 8rem;
        }

        .panel-navigation {
          position: fixed;
          top: 50%;
          left: 0;
          right: 0;
          transform: translateY(-50%);
          display: flex;
          justify-content: space-between;
          padding: 0 2rem;
          pointer-events: none;
          z-index: 850;
        }

        .nav-button {
          pointer-events: all;
          padding: 1rem 2rem;
          background: rgba(74, 124, 44, 0.9);
          backdrop-filter: blur(10px);
          border: 2px solid #ffd700;
          border-radius: 12px;
          color: white;
          font-weight: bold;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .nav-button:hover:not(:disabled) {
          background: rgba(74, 124, 44, 1);
          transform: translateX(${props => props.children?.toString().includes('Previous') ? '-5px' : '5px'});
        }

        .nav-button:disabled {
          opacity: 0.3;
          cursor: not-allowed;
        }

        .panel-indicator {
          pointer-events: all;
          padding: 1rem 2rem;
          background: rgba(45, 80, 22, 0.9);
          backdrop-filter: blur(10px);
          border: 2px solid rgba(255, 255, 255, 0.3);
          border-radius: 12px;
          color: white;
          font-weight: bold;
        }

        .completion-screen {
          background: white;
          border-radius: 24px;
          padding: 4rem;
          max-width: 800px;
          margin: 4rem auto;
          text-align: center;
          box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        }

        .completion-screen h2 {
          font-size: 3rem;
          color: #2d5016;
          margin-bottom: 1rem;
        }

        .completion-screen > p {
          font-size: 1.2rem;
          color: #4a7c2c;
          margin-bottom: 3rem;
        }

        .completion-actions {
          display: flex;
          gap: 1rem;
          justify-content: center;
          flex-wrap: wrap;
          margin-bottom: 3rem;
        }

        .action-button {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          padding: 1rem 2rem;
          border-radius: 12px;
          border: 2px solid #4a7c2c;
          background: white;
          color: #2d5016;
          font-weight: bold;
          cursor: pointer;
          text-decoration: none;
          transition: all 0.3s ease;
        }

        .action-button.primary {
          background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
          border-color: #ffd700;
        }

        .action-button:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(74, 124, 44, 0.3);
        }

        .share-encouragement {
          padding: 2rem;
          background: rgba(255, 215, 0, 0.1);
          border-radius: 16px;
        }

        .share-encouragement p {
          margin: 0.5rem 0;
          color: #2d5016;
        }

        .share-encouragement .small {
          font-size: 0.9rem;
          color: #4a7c2c;
        }

        @media (max-width: 768px) {
          .expedition-title {
            font-size: 2rem;
          }

          .subtitle {
            font-size: 1.2rem;
          }

          .expedition-details {
            grid-template-columns: 1fr;
            gap: 1.5rem;
          }

          .age-badges {
            flex-direction: column;
            align-items: center;
          }

          .panel-navigation {
            flex-direction: column;
            gap: 1rem;
            top: auto;
            bottom: 1rem;
            transform: none;
          }
        }
      `}</style>
    </div>
  );
}

