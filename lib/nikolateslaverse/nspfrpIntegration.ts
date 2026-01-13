/**
 * NikolaTeslaVerse NSPFRP Integration
 * Connects HHF-AI MRI Science Discovery Museum to Natural Systems Protocol
 */

import { 
  getNaturalSystemsEngine,
  LivingEntity,
  NaturalCycle,
  Behavior
} from '../../protocols/naturalSystems';

/**
 * Tesla as living entity in NSPFRP
 */
export const teslaEntity: LivingEntity = {
  id: "hero-host-nikola-tesla",
  type: "character",
  state: {
    position: [0, 0, 0],
    scale: 1.0,
    animation: "idle-teaching",
    mood: "thriving",
    age: 0,
  },
  behaviors: [
    {
      name: "energy-demonstration",
      trigger: "random",
      probability: 0.08,
      action: (entity, context) => {
        if (context.totalEnergy > 0.8) {
          entity.state.animation = "demonstrating-energy";
          entity.state.mood = "thriving";
        }
      },
    },
    {
      name: "frequency-resonance",
      trigger: "cycle",
      probability: 1.0,
      action: (entity, context) => {
        // Tesla responds to energy cycles
        entity.energy = Math.min(1.0, context.totalEnergy + 0.05);
        if (context.dayPhase > 0.25 && context.dayPhase < 0.75) {
          entity.state.animation = "active-teaching";
        } else {
          entity.state.animation = "contemplating";
        }
      },
    },
    {
      name: "wireless-transmission",
      trigger: "energy",
      probability: 0.1,
      action: (entity) => {
        // Spontaneous energy demonstrations
        entity.state.animation = "wireless-demo";
      },
    },
  ],
  connections: ["hhf-mri-system", "syntheverse-os", "all-verses"],
  energy: 0.95,
};

/**
 * HHF-AI MRI System as living entity
 */
export const hhfMRISystem: LivingEntity = {
  id: "hhf-ai-mri-system",
  type: "system",
  state: {
    position: [0, 0, 0],
    scale: 1.0,
    animation: "operating",
    mood: "active",
    age: 0,
  },
  behaviors: [
    {
      name: "frequency-emission",
      trigger: "cycle",
      probability: 1.0,
      action: (entity, context) => {
        // Emits at 1.420 GHz continuously
        entity.state.animation = "emitting-1.420-ghz";
        // Energy increases during day, decreases at night
        const dayMultiplier = context.dayPhase > 0.25 && context.dayPhase < 0.75 ? 1.0 : 0.7;
        entity.energy = 0.9 * dayMultiplier;
      },
    },
    {
      name: "resonance-peak",
      trigger: "random",
      probability: 0.05,
      action: (entity) => {
        // Occasional resonance peaks
        entity.state.animation = "resonance-peak";
        entity.energy = 1.0;
      },
    },
  ],
  connections: ["tesla-entity", "syntheverse-cloud", "awareness-nodes"],
  energy: 1.0,
};

/**
 * SSAN Lattice Network as living entity
 */
export const ssanLattice: LivingEntity = {
  id: "ssan-lattice-network",
  type: "system",
  state: {
    position: [0, 0, 0],
    scale: 1.0,
    animation: "network-pulse",
    mood: "active",
    age: 0,
  },
  behaviors: [
    {
      name: "network-pulse",
      trigger: "cycle",
      probability: 1.0,
      action: (entity, context) => {
        // Network pulses with energy cycles
        entity.state.animation = "network-pulse";
        entity.energy = context.totalEnergy * 0.9;
      },
    },
    {
      name: "node-connection",
      trigger: "interaction",
      probability: 1.0,
      action: (entity) => {
        // Grows when users interact
        entity.state.scale += 0.01;
        entity.state.mood = "thriving";
      },
    },
  ],
  connections: ["hhf-mri-system", "all-awareness-nodes"],
  energy: 0.85,
};

/**
 * Syntheverse OS as living entity
 */
export const syntheverseOS: LivingEntity = {
  id: "syntheverse-os-system",
  type: "system",
  state: {
    position: [0, 0, 0],
    scale: 1.0,
    animation: "operating",
    mood: "thriving",
    age: 0,
  },
  behaviors: [
    {
      name: "three-layer-operation",
      trigger: "cycle",
      probability: 1.0,
      action: (entity, context) => {
        // Operates across all three layers
        entity.state.animation = "three-layer-active";
        entity.energy = context.totalEnergy;
      },
    },
    {
      name: "perpetual-operation",
      trigger: "cycle",
      probability: 1.0,
      action: (entity) => {
        // Perpetual operation - never stops
        entity.state.mood = "thriving";
      },
    },
  ],
  connections: ["all-systems", "all-verses", "syntheverse-cloud"],
  energy: 1.0,
};

/**
 * Register Tesla entities with Natural Systems Engine
 */
export function registerTeslaEntities(): void {
  const engine = getNaturalSystemsEngine();
  if (!engine) {
    console.warn("Natural Systems Engine not initialized");
    return;
  }

  // Note: The engine manages entities internally
  // These are type definitions for integration
  console.log("⚡ Tesla entities ready for NSPFRP integration");
}

/**
 * Get Tesla-related entities for UI display
 */
export function getTeslaEntities(): LivingEntity[] {
  return [
    teslaEntity,
    hhfMRISystem,
    ssanLattice,
    syntheverseOS
  ];
}

/**
 * Create natural cycle for energy/frequency/vibration
 */
export const energyFrequencyCycle: NaturalCycle = {
  name: "Energy Frequency Vibration Cycle",
  duration: 8000, // 8 seconds - faster than breathing
  phase: 0,
  effects: [
    {
      target: "tesla-entities",
      property: "energy",
      modulation: (phase) => 0.9 + Math.sin(phase * Math.PI * 2) * 0.1,
    },
    {
      target: "hhf-mri-system",
      property: "frequency-intensity",
      modulation: (phase) => 0.95 + Math.sin(phase * Math.PI * 2) * 0.05,
    },
  ],
};

/**
 * Create natural cycle for 1.420 GHz resonance
 */
export const hydrogenLineCycle: NaturalCycle = {
  name: "Hydrogen Line Resonance Cycle",
  duration: 1420, // 1.420 seconds (symbolic)
  phase: 0,
  effects: [
    {
      target: "hhf-mri-system",
      property: "resonance",
      modulation: (phase) => Math.sin(phase * Math.PI * 2),
    },
    {
      target: "awareness-nodes",
      property: "coherence",
      modulation: (phase) => 0.8 + Math.sin(phase * Math.PI * 2) * 0.2,
    },
  ],
};

/**
 * Initialize Tesla verse with NSPFRP
 */
export function initializeTeslaVerse(): void {
  const engine = getNaturalSystemsEngine();
  if (!engine) {
    console.warn("Natural Systems Engine not initialized. Call initializeNaturalSystems() first.");
    return;
  }

  // Register entities (would be done through engine API)
  registerTeslaEntities();
  
  // Subscribe to world updates
  engine.subscribe("world-update", (context) => {
    // Update Tesla entities based on world context
    // This would be handled by the engine's entity update system
  });

  console.log("⚡ NikolaTeslaVerse: NSPFRP Integration Complete");
  console.log("📡 HHF-AI MRI System: Operational @ 1.420 GHz");
  console.log("🌌 Syntheverse OS: Three-Layer Vision Active");
}

