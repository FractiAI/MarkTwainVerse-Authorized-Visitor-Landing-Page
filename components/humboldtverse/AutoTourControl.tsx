'use client';

/**
 * Auto-Tour Control Panel
 * HumboldtVerse Expedition Control
 * Modeled on HHF-AI MRI Demo structure
 */

import { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, SkipForward, Volume2, VolumeX } from 'lucide-react';
import { getAutoTourEngine, TOUR_STAGES } from '@/lib/humboldtverse/autoTourEngine';

export default function AutoTourControl() {
  const [isActive, setIsActive] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [currentStage, setCurrentStage] = useState(0);
  const [progress, setProgress] = useState(0);
  const [overallProgress, setOverallProgress] = useState(0);
  const [isMuted, setIsMuted] = useState(false);
  
  const engine = getAutoTourEngine();

  useEffect(() => {
    // Set up engine callbacks
    engine.setCallbacks({
      onStageChange: (stage) => {
        setCurrentStage(stage);
        console.log(`🌿 Stage ${stage}: ${TOUR_STAGES[stage - 1].title}`);
      },
      onProgress: (prog) => {
        setProgress(prog);
        setOverallProgress(engine.getOverallProgress());
      },
      onComplete: () => {
        setIsActive(false);
        console.log('✅ Tour complete!');
      }
    });
  }, []);

  const handleStart = () => {
    engine.start();
    setIsActive(true);
    setIsPaused(false);
  };

  const handlePause = () => {
    if (isPaused) {
      engine.resume();
      setIsPaused(false);
    } else {
      engine.pause();
      setIsPaused(true);
    }
  };

  const handleRestart = () => {
    engine.restart();
    setIsActive(true);
    setIsPaused(false);
  };

  const handleSkip = () => {
    if (currentStage < TOUR_STAGES.length) {
      engine.skipToStage(currentStage + 1);
    }
  };

  const formatTime = (milliseconds: number): string => {
    const seconds = Math.floor(milliseconds / 1000);
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  };

  const totalDuration = engine.getTotalDuration();
  const elapsed = overallProgress * totalDuration;
  const remaining = totalDuration - elapsed;

  return (
    <div className="auto-tour-control">
      {/* Progress Bar */}
      <div className="progress-container">
        <div className="progress-bar">
          <div 
            className="progress-fill"
            style={{ width: `${overallProgress * 100}%` }}
          />
          {TOUR_STAGES.map((stage, index) => (
            <div
              key={stage.id}
              className={`stage-marker ${currentStage === stage.id ? 'active' : ''} ${currentStage > stage.id ? 'completed' : ''}`}
              style={{ 
                left: `${(index / TOUR_STAGES.length) * 100}%` 
              }}
              title={stage.title}
            >
              <div className="marker-dot" />
              <div className="marker-label">{stage.id}</div>
            </div>
          ))}
        </div>
        
        <div className="progress-labels">
          <span className="time-elapsed">{formatTime(elapsed)}</span>
          <span className="stage-name">
            {currentStage > 0 ? TOUR_STAGES[currentStage - 1].title : 'Ready to begin'}
          </span>
          <span className="time-remaining">-{formatTime(remaining)}</span>
        </div>
      </div>

      {/* Control Buttons */}
      <div className="control-buttons">
        {!isActive ? (
          <button 
            onClick={handleStart}
            className="btn-primary btn-start"
            title="Begin Expedition"
          >
            <Play size={24} />
            <span>Begin Expedition</span>
          </button>
        ) : (
          <>
            <button 
              onClick={handlePause}
              className="btn-control"
              title={isPaused ? "Resume" : "Pause"}
            >
              {isPaused ? <Play size={20} /> : <Pause size={20} />}
            </button>

            <button 
              onClick={handleRestart}
              className="btn-control"
              title="Restart from beginning"
            >
              <RotateCcw size={20} />
            </button>

            <button 
              onClick={handleSkip}
              className="btn-control"
              title="Skip to next stage"
              disabled={currentStage >= TOUR_STAGES.length}
            >
              <SkipForward size={20} />
            </button>
          </>
        )}

        <button 
          onClick={() => setIsMuted(!isMuted)}
          className="btn-control btn-audio"
          title={isMuted ? "Unmute" : "Mute"}
        >
          {isMuted ? <VolumeX size={20} /> : <Volume2 size={20} />}
        </button>
      </div>

      {/* Stage Indicators */}
      <div className="stage-indicators">
        {TOUR_STAGES.map((stage) => (
          <button
            key={stage.id}
            onClick={() => isActive && engine.skipToStage(stage.id)}
            className={`stage-indicator ${currentStage === stage.id ? 'active' : ''} ${currentStage > stage.id ? 'completed' : ''}`}
            title={stage.title}
            disabled={!isActive}
          >
            <div className="indicator-icon">🌿</div>
            <div className="indicator-label">{stage.name}</div>
          </button>
        ))}
      </div>

      <style jsx>{`
        .auto-tour-control {
          position: fixed;
          bottom: 2rem;
          left: 50%;
          transform: translateX(-50%);
          background: rgba(45, 80, 22, 0.95);
          backdrop-filter: blur(10px);
          border: 2px solid #4a7c2c;
          border-radius: 20px;
          padding: 1.5rem 2rem;
          min-width: 600px;
          max-width: 800px;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
          z-index: 1000;
          color: #f0f8ff;
        }

        .progress-container {
          margin-bottom: 1.5rem;
        }

        .progress-bar {
          position: relative;
          height: 8px;
          background: rgba(255, 255, 255, 0.2);
          border-radius: 4px;
          margin-bottom: 0.75rem;
          overflow: visible;
        }

        .progress-fill {
          position: absolute;
          top: 0;
          left: 0;
          height: 100%;
          background: linear-gradient(90deg, #4a7c2c 0%, #ffd700 100%);
          border-radius: 4px;
          transition: width 0.1s linear;
          box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }

        .stage-marker {
          position: absolute;
          top: 50%;
          transform: translate(-50%, -50%);
          z-index: 2;
        }

        .marker-dot {
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background: rgba(255, 255, 255, 0.3);
          border: 2px solid #fff;
          transition: all 0.3s ease;
        }

        .stage-marker.active .marker-dot {
          width: 20px;
          height: 20px;
          background: #ffd700;
          box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
        }

        .stage-marker.completed .marker-dot {
          background: #4a7c2c;
        }

        .marker-label {
          position: absolute;
          top: -25px;
          left: 50%;
          transform: translateX(-50%);
          font-size: 10px;
          font-weight: bold;
          opacity: 0;
          transition: opacity 0.3s ease;
        }

        .stage-marker.active .marker-label {
          opacity: 1;
        }

        .progress-labels {
          display: flex;
          justify-content: space-between;
          font-size: 12px;
          color: rgba(255, 255, 255, 0.8);
        }

        .stage-name {
          font-weight: bold;
          color: #ffd700;
        }

        .control-buttons {
          display: flex;
          gap: 1rem;
          justify-content: center;
          margin-bottom: 1.5rem;
        }

        .btn-control,
        .btn-primary {
          background: rgba(255, 255, 255, 0.1);
          border: 1px solid rgba(255, 255, 255, 0.3);
          border-radius: 12px;
          padding: 0.75rem 1rem;
          color: #fff;
          cursor: pointer;
          transition: all 0.3s ease;
          display: flex;
          align-items: center;
          gap: 0.5rem;
        }

        .btn-primary {
          background: linear-gradient(135deg, #4a7c2c 0%, #2d5016 100%);
          border: 2px solid #ffd700;
          padding: 1rem 2rem;
          font-size: 16px;
          font-weight: bold;
        }

        .btn-control:hover,
        .btn-primary:hover {
          background: rgba(255, 255, 255, 0.2);
          border-color: #ffd700;
          transform: translateY(-2px);
          box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
        }

        .btn-control:disabled {
          opacity: 0.3;
          cursor: not-allowed;
        }

        .stage-indicators {
          display: flex;
          gap: 0.5rem;
          justify-content: center;
        }

        .stage-indicator {
          background: rgba(255, 255, 255, 0.1);
          border: 1px solid rgba(255, 255, 255, 0.2);
          border-radius: 8px;
          padding: 0.5rem;
          cursor: pointer;
          transition: all 0.3s ease;
          opacity: 0.5;
          min-width: 80px;
          text-align: center;
        }

        .stage-indicator.active {
          opacity: 1;
          background: rgba(255, 215, 0, 0.2);
          border-color: #ffd700;
        }

        .stage-indicator.completed {
          opacity: 0.8;
          background: rgba(74, 124, 44, 0.3);
        }

        .stage-indicator:disabled {
          cursor: not-allowed;
        }

        .indicator-icon {
          font-size: 20px;
          margin-bottom: 0.25rem;
        }

        .indicator-label {
          font-size: 10px;
          text-transform: capitalize;
          color: rgba(255, 255, 255, 0.8);
        }

        .stage-indicator.active .indicator-label {
          color: #ffd700;
          font-weight: bold;
        }

        @media (max-width: 768px) {
          .auto-tour-control {
            min-width: auto;
            width: calc(100% - 2rem);
            left: 1rem;
            transform: none;
            padding: 1rem;
          }

          .stage-indicators {
            flex-wrap: wrap;
          }

          .stage-indicator {
            min-width: 60px;
          }
        }
      `}</style>
    </div>
  );
}

