// ============================================================================
// SYNTHEVERSE WORLD STATES PROTOCOL
// Three-State Lifecycle: Sandbox → Cloud → Shell
// ============================================================================

/**
 * WORLD STATES ARCHITECTURE
 * 
 * Every Syntheverse world progresses through three states:
 * 
 * 1. SANDBOX (Development)
 *    - Mutable, experimental, private
 *    - Full editing capabilities
 *    - Testing and iteration
 *    - Performance profiling
 *    - Breaking changes allowed
 * 
 * 2. CLOUD (Operation)
 *    - Immutable structure, mutable content
 *    - Publicly accessible
 *    - Live visitors and residents
 *    - Analytics and monitoring
 *    - Version-controlled updates
 * 
 * 3. SHELL (Protocol-Hardened & On-Chain)
 *    - Completely immutable
 *    - Archived on Base blockchain
 *    - Permanent IPFS storage
 *    - Transferable ownership
 *    - Mathematical constant locked
 */

export enum WorldState {
  SANDBOX = 'sandbox',
  CLOUD = 'cloud',
  SHELL = 'shell',
}

export interface WorldStateMetadata {
  currentState: WorldState;
  createdAt: number;
  sandboxDuration?: number;  // Time spent in development
  cloudLaunchedAt?: number;  // When went live
  shellArchivedAt?: number;  // When became permanent
  stateTransitions: StateTransition[];
  chainArchiveHash?: string; // IPFS/blockchain hash for shell
}

export interface StateTransition {
  fromState: WorldState;
  toState: WorldState;
  timestamp: number;
  triggeredBy: 'creator' | 'system' | 'governance';
  reason: string;
  snapshotHash?: string;  // State snapshot at transition
}

// ============================================================================
// STATE CAPABILITIES & RESTRICTIONS
// ============================================================================

export interface StateCapabilities {
  // Structure
  canAddEntities: boolean;
  canRemoveEntities: boolean;
  canModifyEntities: boolean;
  canAddCycles: boolean;
  canModifyCycles: boolean;
  canAddEvents: boolean;
  canModifyEvents: boolean;
  
  // Content
  canUpdateContent: boolean;
  canModifyPricing: boolean;
  canChangeTheme: boolean;
  
  // Access
  isPublic: boolean;
  requiresAuthentication: boolean;
  allowsVisitors: boolean;
  
  // Blockchain
  isOnChain: boolean;
  isMutable: boolean;
  isTransferable: boolean;
  
  // Measurement
  canMeasureConstants: boolean;
  recordsMeasurements: boolean;
}

export const STATE_CAPABILITIES: Record<WorldState, StateCapabilities> = {
  [WorldState.SANDBOX]: {
    canAddEntities: true,
    canRemoveEntities: true,
    canModifyEntities: true,
    canAddCycles: true,
    canModifyCycles: true,
    canAddEvents: true,
    canModifyEvents: true,
    canUpdateContent: true,
    canModifyPricing: true,
    canChangeTheme: true,
    isPublic: false,
    requiresAuthentication: true,
    allowsVisitors: false, // Only creator
    isOnChain: false,
    isMutable: true,
    isTransferable: false,
    canMeasureConstants: true, // Testing measurements
    recordsMeasurements: false, // Not official
  },
  
  [WorldState.CLOUD]: {
    canAddEntities: false,  // Structure locked
    canRemoveEntities: false,
    canModifyEntities: false,
    canAddCycles: false,
    canModifyCycles: false,
    canAddEvents: false,
    canModifyEvents: false,
    canUpdateContent: true,  // Content updates allowed
    canModifyPricing: true,
    canChangeTheme: false,   // Theme locked
    isPublic: true,
    requiresAuthentication: false,
    allowsVisitors: true,
    isOnChain: false,       // Metadata on-chain, world off-chain
    isMutable: true,        // Content mutable
    isTransferable: true,   // Can transfer ownership
    canMeasureConstants: true,
    recordsMeasurements: true, // Official measurements
  },
  
  [WorldState.SHELL]: {
    canAddEntities: false,
    canRemoveEntities: false,
    canModifyEntities: false,
    canAddCycles: false,
    canModifyCycles: false,
    canAddEvents: false,
    canModifyEvents: false,
    canUpdateContent: false,  // Completely frozen
    canModifyPricing: false,
    canChangeTheme: false,
    isPublic: true,
    requiresAuthentication: false,
    allowsVisitors: true,
    isOnChain: true,        // Fully on-chain
    isMutable: false,       // Immutable
    isTransferable: true,   // Ownership transferable as NFT
    canMeasureConstants: true,  // Can still measure
    recordsMeasurements: true,  // Permanent record
  },
};

// ============================================================================
// STATE TRANSITION RULES
// ============================================================================

export interface TransitionRequirements {
  minTestDuration?: number;        // Minimum time in previous state
  minVisitors?: number;            // For cloud → shell
  requiredMeasurements?: string[]; // Constants that must be measured
  stabilityThreshold?: number;     // Energy/performance requirements
  governanceVotes?: number;        // Community approval
  synthCost?: number;             // SYNTH tokens required
}

export const TRANSITION_REQUIREMENTS: Record<string, TransitionRequirements> = {
  'sandbox-to-cloud': {
    minTestDuration: 3600000, // 1 hour minimum testing
    requiredMeasurements: ['breathing-cycle', 'day-night-cycle'],
    stabilityThreshold: 0.7,  // World energy must be stable ≥0.7
    synthCost: 100,           // 100 SYNTH to launch
  },
  
  'cloud-to-shell': {
    minTestDuration: 86400000 * 30, // 30 days in cloud
    minVisitors: 100,        // At least 100 unique visitors
    requiredMeasurements: ['verse-phase-constant', 'community-resonances'],
    stabilityThreshold: 0.8,
    governanceVotes: 10,     // Community approval
    synthCost: 10000,        // 10,000 SYNTH for permanent archival
  },
  
  'cloud-to-sandbox': {
    // Can revert for major fixes (with governance approval)
    governanceVotes: 20,     // Higher threshold for rollback
    synthCost: 0,           // No cost to fix issues
  },
};

// ============================================================================
// WORLD STATE MANAGER
// ============================================================================

export class WorldStateManager {
  private worldId: string;
  private metadata: WorldStateMetadata;
  
  constructor(worldId: string, initialMetadata?: WorldStateMetadata) {
    this.worldId = worldId;
    this.metadata = initialMetadata || {
      currentState: WorldState.SANDBOX,
      createdAt: Date.now(),
      stateTransitions: [],
    };
  }
  
  getCurrentState(): WorldState {
    return this.metadata.currentState;
  }
  
  getCapabilities(): StateCapabilities {
    return STATE_CAPABILITIES[this.metadata.currentState];
  }
  
  canTransitionTo(targetState: WorldState): boolean {
    const current = this.metadata.currentState;
    
    // Define allowed transitions
    const allowedTransitions: Record<WorldState, WorldState[]> = {
      [WorldState.SANDBOX]: [WorldState.CLOUD],
      [WorldState.CLOUD]: [WorldState.SHELL, WorldState.SANDBOX], // Can revert for fixes
      [WorldState.SHELL]: [], // Shell is permanent
    };
    
    return allowedTransitions[current].includes(targetState);
  }
  
  async validateTransition(
    targetState: WorldState,
    worldMetrics: WorldMetrics
  ): Promise<ValidationResult> {
    const transitionKey = `${this.metadata.currentState}-to-${targetState}`;
    const requirements = TRANSITION_REQUIREMENTS[transitionKey];
    
    if (!requirements) {
      return { valid: false, reason: 'Invalid transition' };
    }
    
    const errors: string[] = [];
    
    // Check minimum duration
    if (requirements.minTestDuration) {
      const duration = Date.now() - (this.metadata.cloudLaunchedAt || this.metadata.createdAt);
      if (duration < requirements.minTestDuration) {
        errors.push(`Minimum duration not met: ${duration}ms / ${requirements.minTestDuration}ms`);
      }
    }
    
    // Check visitor count
    if (requirements.minVisitors && worldMetrics.uniqueVisitors < requirements.minVisitors) {
      errors.push(`Not enough visitors: ${worldMetrics.uniqueVisitors} / ${requirements.minVisitors}`);
    }
    
    // Check measurements
    if (requirements.requiredMeasurements) {
      const missing = requirements.requiredMeasurements.filter(
        m => !worldMetrics.completedMeasurements.includes(m)
      );
      if (missing.length > 0) {
        errors.push(`Missing measurements: ${missing.join(', ')}`);
      }
    }
    
    // Check stability
    if (requirements.stabilityThreshold && worldMetrics.averageEnergy < requirements.stabilityThreshold) {
      errors.push(`World not stable enough: ${worldMetrics.averageEnergy} / ${requirements.stabilityThreshold}`);
    }
    
    // Check governance
    if (requirements.governanceVotes && worldMetrics.approvalVotes < requirements.governanceVotes) {
      errors.push(`Not enough governance approval: ${worldMetrics.approvalVotes} / ${requirements.governanceVotes}`);
    }
    
    return {
      valid: errors.length === 0,
      reason: errors.join('; '),
      cost: requirements.synthCost || 0,
    };
  }
  
  async transition(
    targetState: WorldState,
    triggeredBy: 'creator' | 'system' | 'governance',
    reason: string,
    snapshotHash?: string
  ): Promise<void> {
    if (!this.canTransitionTo(targetState)) {
      throw new Error(`Cannot transition from ${this.metadata.currentState} to ${targetState}`);
    }
    
    const transition: StateTransition = {
      fromState: this.metadata.currentState,
      toState: targetState,
      timestamp: Date.now(),
      triggeredBy,
      reason,
      snapshotHash,
    };
    
    this.metadata.stateTransitions.push(transition);
    this.metadata.currentState = targetState;
    
    // Update timestamps
    if (targetState === WorldState.CLOUD) {
      this.metadata.cloudLaunchedAt = Date.now();
    } else if (targetState === WorldState.SHELL) {
      this.metadata.shellArchivedAt = Date.now();
    }
    
    // Archive transition on-chain
    await this.archiveTransition(transition);
    
    console.log(`✅ World ${this.worldId} transitioned to ${targetState}`);
  }
  
  private async archiveTransition(transition: StateTransition): Promise<void> {
    // In production, this would:
    // 1. Upload to IPFS
    // 2. Record on Base blockchain
    // 3. Emit event for indexers
    
    console.log('📝 Archiving transition:', transition);
  }
  
  getMetadata(): WorldStateMetadata {
    return { ...this.metadata };
  }
}

// ============================================================================
// SUPPORTING TYPES
// ============================================================================

export interface WorldMetrics {
  uniqueVisitors: number;
  averageEnergy: number;
  completedMeasurements: string[];
  approvalVotes: number;
  uptime: number;
  performanceScore: number;
}

export interface ValidationResult {
  valid: boolean;
  reason?: string;
  cost?: number;
}

// ============================================================================
// STATE VISUALIZATION HELPERS
// ============================================================================

export function getStateColor(state: WorldState): string {
  switch (state) {
    case WorldState.SANDBOX:
      return '#fbbf24'; // Yellow - caution, development
    case WorldState.CLOUD:
      return '#00d4ff'; // Cyan - active, live
    case WorldState.SHELL:
      return '#d4af37'; // Gold - permanent, valuable
  }
}

export function getStateIcon(state: WorldState): string {
  switch (state) {
    case WorldState.SANDBOX:
      return '🏗️'; // Construction
    case WorldState.CLOUD:
      return '☁️'; // Cloud
    case WorldState.SHELL:
      return '🐚'; // Shell (permanent, hardened)
  }
}

export function getStateDescription(state: WorldState): string {
  switch (state) {
    case WorldState.SANDBOX:
      return 'Development - Private testing and iteration';
    case WorldState.CLOUD:
      return 'Live - Public operation with content updates';
    case WorldState.SHELL:
      return 'Permanent - Immutable on-chain archive';
  }
}

// ============================================================================
// EXPORT PROTOCOL
// ============================================================================

export default {
  WorldState,
  WorldStateManager,
  STATE_CAPABILITIES,
  TRANSITION_REQUIREMENTS,
  getStateColor,
  getStateIcon,
  getStateDescription,
};

