"use client";

import { motion } from 'framer-motion';
import { useState } from 'react';
import { 
  WorldState, 
  WorldStateManager,
  getStateColor,
  getStateIcon,
  getStateDescription,
  STATE_CAPABILITIES,
  TRANSITION_REQUIREMENTS
} from '@/protocols/worldStates';

// ============================================================================
// WORLD STATE PANEL - Manage Sandbox → Cloud → Shell Pipeline
// ============================================================================

interface WorldStatePanelProps {
  worldId: string;
  stateManager: WorldStateManager;
  onStateChange: (newState: WorldState) => void;
}

export function WorldStatePanel({ worldId, stateManager, onStateChange }: WorldStatePanelProps) {
  const [showTransitionModal, setShowTransitionModal] = useState(false);
  const [targetState, setTargetState] = useState<WorldState | null>(null);
  
  const currentState = stateManager.getCurrentState();
  const capabilities = stateManager.getCapabilities();
  const metadata = stateManager.getMetadata();

  return (
    <div className="bg-gradient-to-br from-slate-900 to-purple-900 rounded-lg p-6 border border-white/20">
      {/* Current State Display */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h3 className="text-xl font-bold mb-2">World State</h3>
          <p className="text-sm text-white/60">
            {getStateDescription(currentState)}
          </p>
        </div>
        <div className="text-center">
          <div className="text-6xl mb-2">{getStateIcon(currentState)}</div>
          <div 
            className="px-4 py-2 rounded-lg font-bold uppercase text-sm"
            style={{ backgroundColor: getStateColor(currentState) + '40', borderColor: getStateColor(currentState), borderWidth: '2px' }}
          >
            {currentState}
          </div>
        </div>
      </div>

      {/* State Timeline */}
      <div className="mb-6">
        <h4 className="text-sm font-bold mb-3 text-white/80">State Timeline</h4>
        <div className="relative">
          {/* Timeline bar */}
          <div className="absolute top-1/2 left-0 right-0 h-1 bg-white/10"></div>
          
          {/* State nodes */}
          <div className="relative flex justify-between">
            {[WorldState.SANDBOX, WorldState.CLOUD, WorldState.SHELL].map((state, index) => {
              const isPast = metadata.stateTransitions.some(t => t.toState === state);
              const isCurrent = state === currentState;
              const isFuture = !isPast && !isCurrent;
              
              return (
                <motion.div
                  key={state}
                  className="flex flex-col items-center"
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <div
                    className={`w-12 h-12 rounded-full flex items-center justify-center border-2 mb-2 ${
                      isCurrent ? 'scale-125 shadow-lg' : ''
                    }`}
                    style={{
                      backgroundColor: isPast || isCurrent ? getStateColor(state) : '#ffffff20',
                      borderColor: getStateColor(state),
                    }}
                  >
                    <span className="text-2xl">{getStateIcon(state)}</span>
                  </div>
                  <div className="text-xs font-bold uppercase">{state}</div>
                  {isPast && !isCurrent && (
                    <div className="text-[10px] text-white/40 mt-1">
                      {new Date(
                        metadata.stateTransitions.find(t => t.toState === state)?.timestamp || 0
                      ).toLocaleDateString()}
                    </div>
                  )}
                </motion.div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Current Capabilities */}
      <div className="mb-6">
        <h4 className="text-sm font-bold mb-3 text-white/80">Current Capabilities</h4>
        <div className="grid grid-cols-2 gap-2 text-xs">
          {Object.entries(capabilities).map(([key, value]) => (
            <div key={key} className="flex items-center gap-2">
              <span>{value ? '✅' : '❌'}</span>
              <span className="text-white/60">
                {key.replace(/([A-Z])/g, ' $1').trim()}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Transition Actions */}
      {currentState !== WorldState.SHELL && (
        <div>
          <h4 className="text-sm font-bold mb-3 text-white/80">Available Transitions</h4>
          <div className="space-y-2">
            {currentState === WorldState.SANDBOX && (
              <TransitionButton
                fromState={currentState}
                toState={WorldState.CLOUD}
                stateManager={stateManager}
                onClick={() => {
                  setTargetState(WorldState.CLOUD);
                  setShowTransitionModal(true);
                }}
              />
            )}
            
            {currentState === WorldState.CLOUD && (
              <>
                <TransitionButton
                  fromState={currentState}
                  toState={WorldState.SHELL}
                  stateManager={stateManager}
                  onClick={() => {
                    setTargetState(WorldState.SHELL);
                    setShowTransitionModal(true);
                  }}
                />
                <TransitionButton
                  fromState={currentState}
                  toState={WorldState.SANDBOX}
                  stateManager={stateManager}
                  onClick={() => {
                    setTargetState(WorldState.SANDBOX);
                    setShowTransitionModal(true);
                  }}
                  variant="warning"
                  label="Revert to Sandbox (for fixes)"
                />
              </>
            )}
          </div>
        </div>
      )}

      {/* Permanent State Notice */}
      {currentState === WorldState.SHELL && (
        <motion.div
          className="bg-gradient-to-r from-yellow-600/20 to-purple-600/20 border-2 border-yellow-400 rounded-lg p-4"
          initial={{ scale: 0.95 }}
          animate={{ scale: 1 }}
          transition={{ repeat: Infinity, duration: 2, repeatType: 'reverse' }}
        >
          <div className="flex items-start gap-3">
            <div className="text-3xl">🐚</div>
            <div>
              <h4 className="font-bold text-yellow-400 mb-1">Permanent Shell State</h4>
              <p className="text-xs text-white/80">
                This world is now permanently archived on-chain. It is immutable and will exist forever.
                The verse phase constant θ_{worldId} = {metadata.chainArchiveHash?.substring(0, 20)}...
              </p>
            </div>
          </div>
        </motion.div>
      )}

      {/* Transition Modal */}
      {showTransitionModal && targetState && (
        <TransitionModal
          stateManager={stateManager}
          targetState={targetState}
          onConfirm={async () => {
            await stateManager.transition(
              targetState,
              'creator',
              'Manual transition initiated from studio'
            );
            onStateChange(targetState);
            setShowTransitionModal(false);
          }}
          onCancel={() => setShowTransitionModal(false)}
        />
      )}
    </div>
  );
}

// ============================================================================
// TRANSITION BUTTON
// ============================================================================

interface TransitionButtonProps {
  fromState: WorldState;
  toState: WorldState;
  stateManager: WorldStateManager;
  onClick: () => void;
  variant?: 'primary' | 'warning';
  label?: string;
}

function TransitionButton({ 
  fromState, 
  toState, 
  stateManager, 
  onClick,
  variant = 'primary',
  label
}: TransitionButtonProps) {
  const canTransition = stateManager.canTransitionTo(toState);
  const transitionKey = `${fromState}-to-${toState}`;
  const requirements = TRANSITION_REQUIREMENTS[transitionKey];

  return (
    <motion.button
      className={`w-full p-4 rounded-lg border-2 text-left transition-all ${
        canTransition 
          ? variant === 'warning'
            ? 'bg-yellow-600/20 border-yellow-400 hover:bg-yellow-600/30'
            : 'bg-cyan-600/20 border-cyan-400 hover:bg-cyan-600/30'
          : 'bg-white/5 border-white/20 opacity-50 cursor-not-allowed'
      }`}
      onClick={canTransition ? onClick : undefined}
      disabled={!canTransition}
      whileHover={canTransition ? { scale: 1.02 } : {}}
      whileTap={canTransition ? { scale: 0.98 } : {}}
    >
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          <span className="text-2xl">{getStateIcon(toState)}</span>
          <span className="font-bold">
            {label || `Transition to ${toState.toUpperCase()}`}
          </span>
        </div>
        {requirements?.synthCost && (
          <div className="text-sm font-bold text-cyan-400">
            {requirements.synthCost} SYNTH
          </div>
        )}
      </div>
      <div className="text-xs text-white/60">
        {getStateDescription(toState)}
      </div>
      
      {requirements && (
        <div className="mt-3 pt-3 border-t border-white/10 text-xs space-y-1">
          <div className="font-bold text-white/80">Requirements:</div>
          {requirements.minTestDuration && (
            <div>⏱️ Min duration: {Math.floor(requirements.minTestDuration / 60000)} minutes</div>
          )}
          {requirements.minVisitors && (
            <div>👥 Min visitors: {requirements.minVisitors}</div>
          )}
          {requirements.requiredMeasurements && (
            <div>📊 Measurements: {requirements.requiredMeasurements.length} required</div>
          )}
          {requirements.stabilityThreshold && (
            <div>⚡ Energy stability: {requirements.stabilityThreshold * 100}%+</div>
          )}
          {requirements.governanceVotes && (
            <div>🗳️ Governance votes: {requirements.governanceVotes}</div>
          )}
        </div>
      )}
    </motion.button>
  );
}

// ============================================================================
// TRANSITION MODAL
// ============================================================================

interface TransitionModalProps {
  stateManager: WorldStateManager;
  targetState: WorldState;
  onConfirm: () => void;
  onCancel: () => void;
}

function TransitionModal({ stateManager, targetState, onConfirm, onCancel }: TransitionModalProps) {
  const currentState = stateManager.getCurrentState();
  const transitionKey = `${currentState}-to-${targetState}`;
  const requirements = TRANSITION_REQUIREMENTS[transitionKey];

  return (
    <motion.div
      className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <motion.div
        className="bg-slate-900 rounded-lg p-6 max-w-md w-full border-2"
        style={{ borderColor: getStateColor(targetState) }}
        initial={{ scale: 0.9, y: 20 }}
        animate={{ scale: 1, y: 0 }}
      >
        <div className="text-center mb-6">
          <div className="text-6xl mb-3">{getStateIcon(targetState)}</div>
          <h3 className="text-2xl font-bold mb-2">
            Transition to {targetState.toUpperCase()}
          </h3>
          <p className="text-sm text-white/60">
            {getStateDescription(targetState)}
          </p>
        </div>

        {targetState === WorldState.SHELL && (
          <div className="bg-yellow-600/20 border-2 border-yellow-400 rounded-lg p-4 mb-6">
            <div className="flex items-start gap-2">
              <span className="text-xl">⚠️</span>
              <div className="text-xs">
                <div className="font-bold mb-1">This action is irreversible!</div>
                <div className="text-white/80">
                  Shell state is permanent and immutable. Your world will be archived on-chain forever. 
                  No further changes will be possible.
                </div>
              </div>
            </div>
          </div>
        )}

        {requirements && (
          <div className="bg-white/5 rounded-lg p-4 mb-6">
            <div className="text-sm font-bold mb-3">Requirements:</div>
            <div className="space-y-2 text-sm">
              {requirements.synthCost && (
                <div className="flex justify-between">
                  <span className="text-white/60">Cost:</span>
                  <span className="font-bold text-cyan-400">{requirements.synthCost} SYNTH</span>
                </div>
              )}
              {requirements.minTestDuration && (
                <div className="flex justify-between">
                  <span className="text-white/60">Min Duration:</span>
                  <span>{Math.floor(requirements.minTestDuration / 60000)} minutes</span>
                </div>
              )}
              {requirements.minVisitors && (
                <div className="flex justify-between">
                  <span className="text-white/60">Min Visitors:</span>
                  <span>{requirements.minVisitors}</span>
                </div>
              )}
              {requirements.governanceVotes && (
                <div className="flex justify-between">
                  <span className="text-white/60">Governance Votes:</span>
                  <span>{requirements.governanceVotes}</span>
                </div>
              )}
            </div>
          </div>
        )}

        <div className="flex gap-3">
          <button
            className="flex-1 px-4 py-3 bg-white/10 hover:bg-white/20 rounded-lg font-bold transition-colors"
            onClick={onCancel}
          >
            Cancel
          </button>
          <button
            className="flex-1 px-4 py-3 rounded-lg font-bold transition-colors"
            style={{ 
              backgroundColor: getStateColor(targetState) + '40',
              borderColor: getStateColor(targetState),
              borderWidth: '2px'
            }}
            onClick={onConfirm}
          >
            Confirm Transition
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
}

export default WorldStatePanel;

