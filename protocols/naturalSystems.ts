// ============================================================================
// MARKTWAINVERSE NATURAL SYSTEMS PROTOCOL (NSP)
// A Living, Breathing, Self-Operating Worldbuilding Framework
// ============================================================================
// Inspired by: Natural ecosystems, frontier towns, living organisms
// Architecture: Autonomous, adaptive, animated, organic
// Philosophy: The world operates itself; visitors join its rhythm
// ============================================================================

export interface NaturalCycle {
  name: string;
  duration: number; // milliseconds
  phase: number; // 0-1
  effects: CycleEffect[];
}

export interface CycleEffect {
  target: string;
  property: string;
  modulation: (phase: number) => number;
}

export interface LivingEntity {
  id: string;
  type: 'building' | 'landscape' | 'character' | 'system';
  state: EntityState;
  behaviors: Behavior[];
  connections: string[];
  energy: number; // 0-1
}

export interface EntityState {
  position: [number, number, number];
  scale: number;
  animation: string;
  mood: 'dormant' | 'awakening' | 'active' | 'thriving' | 'resting';
  age: number; // milliseconds since creation
}

export interface Behavior {
  name: string;
  trigger: 'cycle' | 'proximity' | 'interaction' | 'random' | 'energy';
  action: (entity: LivingEntity, context: WorldContext) => void;
  probability: number; // 0-1
}

export interface WorldContext {
  time: number;
  dayPhase: number; // 0 = midnight, 0.5 = noon, 1 = midnight
  seasonPhase: number; // 0-1 through year
  visitorCount: number;
  totalEnergy: number; // Sum of all entity energies
  dominantMood: string;
}

// ============================================================================
// NATURAL CYCLES - The World's Heartbeat
// ============================================================================

export const naturalCycles: Record<string, NaturalCycle> = {
  // Fast heartbeat - ambient animation (6 seconds)
  breathing: {
    name: "Breathing Cycle",
    duration: 6000,
    phase: 0,
    effects: [
      {
        target: "living-architecture",
        property: "luminosity",
        modulation: (phase) => 0.8 + Math.sin(phase * Math.PI * 2) * 0.2,
      },
      {
        target: "landscapes",
        property: "scale",
        modulation: (phase) => 1.0 + Math.sin(phase * Math.PI * 2) * 0.02,
      },
    ],
  },
  
  // Day-night cycle (2 minutes for demo, 24 hours for production)
  dayNight: {
    name: "Day-Night Cycle",
    duration: 120000, // 2 minutes for demo
    phase: 0,
    effects: [
      {
        target: "lighting",
        property: "intensity",
        modulation: (phase) => {
          // Dawn: 0-0.25, Day: 0.25-0.75, Dusk: 0.75-1, Night: 0-0.25
          if (phase < 0.25) return phase * 4; // Dawning
          if (phase < 0.75) return 1.0; // Daytime
          if (phase < 1.0) return 1.0 - ((phase - 0.75) * 4); // Dusking
          return 0.1; // Night
        },
      },
      {
        target: "sky",
        property: "hue",
        modulation: (phase) => phase * 360, // Full color rotation
      },
      {
        target: "activity-level",
        property: "multiplier",
        modulation: (phase) => {
          // More activity during day
          if (phase < 0.25) return 0.3 + phase * 2.8; // Morning awakening
          if (phase < 0.75) return 1.0; // Full day activity
          if (phase < 1.0) return 1.0 - ((phase - 0.75) * 2); // Evening slowing
          return 0.3; // Night activity
        },
      },
    ],
  },
  
  // Weekly expedition cycle (7 minutes for demo)
  expeditionCycle: {
    name: "Expedition Rhythm",
    duration: 420000, // 7 minutes
    phase: 0,
    effects: [
      {
        target: "expeditions",
        property: "featured",
        modulation: (phase) => Math.floor(phase * 7), // 0-6, different expedition each "day"
      },
    ],
  },
  
  // Seasonal cycle (28 minutes for demo, 1 year for production)
  seasons: {
    name: "Seasonal Progression",
    duration: 1680000, // 28 minutes
    phase: 0,
    effects: [
      {
        target: "communities",
        property: "aesthetic",
        modulation: (phase) => phase, // 0=spring, 0.25=summer, 0.5=fall, 0.75=winter
      },
      {
        target: "expeditions",
        property: "availability",
        modulation: (phase) => phase, // Different expeditions available by season
      },
    ],
  },
};

// ============================================================================
// LIVING ENTITIES - Buildings, Landscapes, Characters That Breathe
// ============================================================================

export const livingEntities: Record<string, LivingEntity> = {
  // Mark Twain himself - always present, always animated
  markTwain: {
    id: "hero-host-mark-twain",
    type: "character",
    state: {
      position: [0, 0, 0],
      scale: 1.0,
      animation: "idle-storytelling",
      mood: "thriving",
      age: 0,
    },
    behaviors: [
      {
        name: "spontaneous-story",
        trigger: "random",
        probability: 0.05, // 5% chance per cycle check
        action: (entity, context) => {
          // Randomly tell a story when energy is high
          if (context.totalEnergy > 0.7) {
            entity.state.animation = "telling-story";
            // Story gets dispatched to UI
          }
        },
      },
      {
        name: "greet-newcomers",
        trigger: "proximity",
        probability: 1.0,
        action: (entity) => {
          entity.state.animation = "wave-greeting";
          entity.state.mood = "thriving";
        },
      },
      {
        name: "rest-at-night",
        trigger: "cycle",
        probability: 1.0,
        action: (entity, context) => {
          if (context.dayPhase < 0.25 || context.dayPhase > 0.75) {
            entity.state.animation = "resting";
            entity.state.mood = "resting";
          } else {
            entity.state.animation = "idle-storytelling";
            entity.state.mood = "active";
          }
        },
      },
    ],
    connections: ["daily-bulletin", "all-communities", "all-expeditions"],
    energy: 0.9,
  },
  
  // Frontier Town Center - The beating heart
  townCenter: {
    id: "frontier-town-center",
    type: "building",
    state: {
      position: [0, 0, 0],
      scale: 1.0,
      animation: "breathing",
      mood: "active",
      age: 0,
    },
    behaviors: [
      {
        name: "pulse-with-activity",
        trigger: "energy",
        probability: 1.0,
        action: (entity, context) => {
          entity.scale = 1.0 + (context.totalEnergy * 0.1);
          entity.energy = context.totalEnergy;
        },
      },
      {
        name: "emit-light",
        trigger: "cycle",
        probability: 1.0,
        action: (entity, context) => {
          // Brighter during day, warm glow at night
          const nightGlow = context.dayPhase < 0.25 || context.dayPhase > 0.75;
          entity.state.animation = nightGlow ? "warm-glow" : "daytime-shimmer";
        },
      },
    ],
    connections: ["all-communities"],
    energy: 0.8,
  },
  
  // Each community as a living organism
  frontierColony: {
    id: "frontier-colony-district",
    type: "building",
    state: {
      position: [-100, 0, 50],
      scale: 1.0,
      animation: "breathing",
      mood: "active",
      age: 0,
    },
    behaviors: [
      {
        name: "expand-with-residents",
        trigger: "interaction",
        probability: 1.0,
        action: (entity, context) => {
          // Grows when visitors select it
          entity.state.scale += 0.01;
          entity.state.mood = "thriving";
        },
      },
      {
        name: "frontier-sounds",
        trigger: "random",
        probability: 0.1,
        action: (entity) => {
          // Emit frontier ambiance: hammering, voices, horses
          entity.state.animation = "activity-burst";
        },
      },
    ],
    connections: ["town-center", "expeditions"],
    energy: 0.75,
  },
  
  // Wilderness - most organic, least human-controlled
  wildernessPreserve: {
    id: "wilderness-preserve-zone",
    type: "landscape",
    state: {
      position: [200, 0, -150],
      scale: 1.0,
      animation: "wind-sway",
      mood: "thriving",
      age: 0,
    },
    behaviors: [
      {
        name: "natural-growth",
        trigger: "cycle",
        probability: 1.0,
        action: (entity, context) => {
          // Grows and shifts with seasons
          const seasonalGrowth = Math.sin(context.seasonPhase * Math.PI * 2) * 0.1;
          entity.state.scale = 1.0 + seasonalGrowth;
        },
      },
      {
        name: "wildlife-sounds",
        trigger: "random",
        probability: 0.15,
        action: (entity, context) => {
          // Bird calls during day, crickets at night
          if (context.dayPhase > 0.25 && context.dayPhase < 0.75) {
            entity.state.animation = "bird-activity";
          } else {
            entity.state.animation = "night-sounds";
          }
        },
      },
    ],
    connections: ["eco-expeditions"],
    energy: 1.0, // Wilderness has highest natural energy
  },
};

// ============================================================================
// AUTONOMOUS BEHAVIORS - Self-Operating Events
// ============================================================================

export interface AutonomousEvent {
  id: string;
  name: string;
  trigger: 'time' | 'condition' | 'visitor-count' | 'random';
  condition?: (context: WorldContext) => boolean;
  action: (context: WorldContext) => EventResult;
  cooldown: number; // milliseconds before can trigger again
  lastTriggered: number;
}

export interface EventResult {
  type: 'story' | 'announcement' | 'special-offer' | 'community-event' | 'expedition-departure';
  content: any;
  duration: number;
}

export const autonomousEvents: AutonomousEvent[] = [
  {
    id: "morning-greeting",
    name: "Mark Twain's Morning Greeting",
    trigger: "time",
    condition: (context) => context.dayPhase > 0.24 && context.dayPhase < 0.26,
    action: (context) => ({
      type: "story",
      content: {
        title: "Good morning, frontier friends!",
        message: "Well now, looks like the sun's come up on another fine day in the Syntheverse. Let me tell you what's happening today...",
        from: "Mark Twain",
      },
      duration: 5000,
    }),
    cooldown: 120000, // Once per day-cycle
    lastTriggered: 0,
  },
  
  {
    id: "expedition-departure",
    name: "Expedition Group Departing",
    trigger: "time",
    condition: (context) => context.dayPhase > 0.3 && context.dayPhase < 0.32,
    action: (context) => ({
      type: "expedition-departure",
      content: {
        expedition: "Morning Catch Adventure",
        participants: Math.floor(context.visitorCount * 0.3),
        destination: "Crystal Lake",
      },
      duration: 3000,
    }),
    cooldown: 120000,
    lastTriggered: 0,
  },
  
  {
    id: "innovation-hub-demo",
    name: "Innovation Hub Demo Day",
    trigger: "condition",
    condition: (context) => context.dayPhase > 0.5 && context.dayPhase < 0.55 && context.visitorCount > 5,
    action: () => ({
      type: "community-event",
      content: {
        title: "Innovation Hub Demo Day Starting!",
        location: "Innovation Hub - Space 12",
        description: "Come see what our builders are creating!",
      },
      duration: 10000,
    }),
    cooldown: 300000,
    lastTriggered: 0,
  },
  
  {
    id: "evening-fireside",
    name: "Fireside Tales with Mark Twain",
    trigger: "time",
    condition: (context) => context.dayPhase > 0.78 && context.dayPhase < 0.82,
    action: () => ({
      type: "story",
      content: {
        title: "Fireside Tales - Evening Gathering",
        message: "The fire's crackling, the stars are coming out, and I've got stories to tell. Gather 'round, friends!",
        from: "Mark Twain",
      },
      duration: 8000,
    }),
    cooldown: 120000,
    lastTriggered: 0,
  },
  
  {
    id: "spontaneous-discount",
    name: "Random Frontier Special",
    trigger: "random",
    condition: (context) => Math.random() < 0.01 && context.visitorCount > 3,
    action: () => ({
      type: "special-offer",
      content: {
        title: "Frontier Flash Sale!",
        discount: 15,
        items: ["Weekly Residency", "Fishing Expeditions"],
        duration: 300000, // 5 minutes
      },
      duration: 300000,
    }),
    cooldown: 600000, // 10 minutes minimum between specials
    lastTriggered: 0,
  },
  
  {
    id: "weather-change",
    name: "Weather Pattern Shift",
    trigger: "random",
    condition: () => Math.random() < 0.05,
    action: () => ({
      type: "announcement",
      content: {
        title: "Weather Shifting",
        message: "A frontier storm's rolling in from the west. Beautiful sight from the Alpine Heights!",
        effect: "rain-animation",
      },
      duration: 30000,
    }),
    cooldown: 180000,
    lastTriggered: 0,
  },
];

// ============================================================================
// NATURAL SYSTEMS PROTOCOL ENGINE
// ============================================================================

export class NaturalSystemsEngine {
  private cycles: Map<string, NaturalCycle>;
  private entities: Map<string, LivingEntity>;
  private events: AutonomousEvent[];
  private context: WorldContext;
  private startTime: number;
  private animationFrameId: number | null = null;
  private subscribers: Map<string, Function[]>;

  constructor() {
    this.cycles = new Map(Object.entries(naturalCycles));
    this.entities = new Map(Object.entries(livingEntities));
    this.events = [...autonomousEvents];
    this.startTime = Date.now();
    this.subscribers = new Map();
    
    this.context = {
      time: 0,
      dayPhase: 0.3, // Start at morning
      seasonPhase: 0.25, // Start in spring
      visitorCount: 0,
      totalEnergy: 0.8,
      dominantMood: "awakening",
    };
  }

  // Start the natural systems protocol
  start() {
    console.log("🌱 Natural Systems Protocol: INITIATING");
    console.log("🏔️  MarkTwainVerse: AWAKENING");
    this.animate();
  }

  // Stop the protocol
  stop() {
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
      this.animationFrameId = null;
    }
    console.log("🌙 Natural Systems Protocol: RESTING");
  }

  // Main animation loop - the world's heartbeat
  private animate = () => {
    const now = Date.now();
    const elapsed = now - this.startTime;
    this.context.time = elapsed;

    // Update all natural cycles
    this.updateCycles(elapsed);

    // Update all living entities
    this.updateEntities();

    // Check for autonomous events
    this.checkEvents();

    // Emit state updates to subscribers
    this.emit("world-update", this.context);

    // Continue animation loop
    this.animationFrameId = requestAnimationFrame(this.animate);
  };

  private updateCycles(elapsed: number) {
    this.cycles.forEach((cycle, name) => {
      cycle.phase = (elapsed % cycle.duration) / cycle.duration;
      
      // Update context with key cycle phases
      if (name === "dayNight") {
        this.context.dayPhase = cycle.phase;
      }
      if (name === "seasons") {
        this.context.seasonPhase = cycle.phase;
      }

      // Apply cycle effects
      cycle.effects.forEach(effect => {
        const value = effect.modulation(cycle.phase);
        this.emit(`cycle-effect:${effect.target}:${effect.property}`, value);
      });
    });
  }

  private updateEntities() {
    let totalEnergy = 0;
    const moods: Record<string, number> = {};

    this.entities.forEach(entity => {
      // Age the entity
      entity.state.age += 16; // ~60fps

      // Run behaviors
      entity.behaviors.forEach(behavior => {
        if (this.shouldTriggerBehavior(behavior)) {
          behavior.action(entity, this.context);
        }
      });

      // Accumulate energy and mood
      totalEnergy += entity.energy;
      moods[entity.state.mood] = (moods[entity.state.mood] || 0) + 1;

      // Emit entity updates
      this.emit(`entity-update:${entity.id}`, entity);
    });

    this.context.totalEnergy = totalEnergy / this.entities.size;
    
    // Determine dominant mood
    const dominantMood = Object.entries(moods).sort((a, b) => b[1] - a[1])[0];
    if (dominantMood) {
      this.context.dominantMood = dominantMood[0];
    }
  }

  private shouldTriggerBehavior(behavior: Behavior): boolean {
    if (Math.random() > behavior.probability) return false;

    switch (behavior.trigger) {
      case "cycle":
        return true; // Always check cycle-based behaviors
      case "random":
        return Math.random() < 0.01; // 1% chance per frame
      case "energy":
        return this.context.totalEnergy > 0.7;
      case "proximity":
        return this.context.visitorCount > 0;
      default:
        return false;
    }
  }

  private checkEvents() {
    const now = Date.now();
    
    this.events.forEach(event => {
      // Check cooldown
      if (now - event.lastTriggered < event.cooldown) return;

      let shouldTrigger = false;

      switch (event.trigger) {
        case "time":
        case "condition":
          shouldTrigger = event.condition ? event.condition(this.context) : false;
          break;
        case "random":
          shouldTrigger = event.condition ? event.condition(this.context) : false;
          break;
        case "visitor-count":
          shouldTrigger = this.context.visitorCount > 0;
          break;
      }

      if (shouldTrigger) {
        const result = event.action(this.context);
        event.lastTriggered = now;
        this.emit(`autonomous-event:${event.type}`, result);
        console.log(`🎭 Autonomous Event: ${event.name}`);
      }
    });
  }

  // Event subscription system
  subscribe(eventName: string, callback: Function) {
    if (!this.subscribers.has(eventName)) {
      this.subscribers.set(eventName, []);
    }
    this.subscribers.get(eventName)!.push(callback);
  }

  private emit(eventName: string, data: any) {
    const callbacks = this.subscribers.get(eventName);
    if (callbacks) {
      callbacks.forEach(callback => callback(data));
    }
  }

  // Public methods for external interaction
  addVisitor() {
    this.context.visitorCount++;
    this.emit("visitor-joined", this.context.visitorCount);
  }

  removeVisitor() {
    this.context.visitorCount = Math.max(0, this.context.visitorCount - 1);
    this.emit("visitor-left", this.context.visitorCount);
  }

  getEntity(id: string): LivingEntity | undefined {
    return this.entities.get(id);
  }

  getContext(): WorldContext {
    return { ...this.context };
  }

  getCyclePhase(cycleName: string): number {
    return this.cycles.get(cycleName)?.phase || 0;
  }

  // Interact with entity (boosts its energy)
  interactWithEntity(entityId: string) {
    const entity = this.entities.get(entityId);
    if (entity) {
      entity.energy = Math.min(1.0, entity.energy + 0.1);
      entity.state.mood = "thriving";
      this.emit(`entity-interaction:${entityId}`, entity);
    }
  }
}

// ============================================================================
// SINGLETON INSTANCE - One Living World
// ============================================================================

let engineInstance: NaturalSystemsEngine | null = null;

export function initializeNaturalSystems(): NaturalSystemsEngine {
  if (!engineInstance) {
    engineInstance = new NaturalSystemsEngine();
    engineInstance.start();
    console.log("🌍 MarkTwainVerse Natural Systems Protocol: ACTIVE");
  }
  return engineInstance;
}

export function getNaturalSystemsEngine(): NaturalSystemsEngine | null {
  return engineInstance;
}

export function shutdownNaturalSystems() {
  if (engineInstance) {
    engineInstance.stop();
    engineInstance = null;
    console.log("🌙 MarkTwainVerse: SLEEPING");
  }
}

// ============================================================================
// EXPORT PROTOCOL
// ============================================================================

export default {
  NaturalSystemsEngine,
  initializeNaturalSystems,
  getNaturalSystemsEngine,
  shutdownNaturalSystems,
  naturalCycles,
  livingEntities,
  autonomousEvents,
};

