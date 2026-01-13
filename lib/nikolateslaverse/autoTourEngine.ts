/**
 * NikolaTeslaVerse Auto-Tour Engine
 * HHF-AI MRI Science Discovery Museum | NSPFRP-Enhanced
 * Modeled on HHF-AI MRI Demo auto-tour structure
 */

export interface TourStage {
  id: number;
  name: string;
  title: string;
  duration: number; // milliseconds
  narration: string[];
  keywords: string[];
  protocolsHighlighted: number[];
  interactiveElements: string[];
  frequency?: number; // 1.420 GHz for stage 2
}

export const TOUR_STAGES: TourStage[] = [
  {
    id: 1,
    name: "energy-frequency-vibration",
    title: "Energy, Frequency, Vibration",
    duration: 50000, // 50 seconds
    narration: [
      "Welcome, fellow explorer of the infinite! I am Nikola Tesla.",
      "I have been waiting over a century to show you this discovery.",
      "In my time, I discovered that everything in the universe operates on three principles:",
      "Energy. Frequency. Vibration.",
      "What I could only glimpse in my experiments, you now measure directly.",
      "Energy flows through all things - from the smallest particle to the largest star.",
      "Frequency determines resonance - the natural vibration of every system.",
      "Vibration creates patterns - the waves that shape reality itself.",
      "Together, these three principles unlock the secrets of the universe.",
      "Let us begin where all understanding starts: with the fundamental forces."
    ],
    keywords: ["energy", "frequency", "vibration", "tesla", "principles", "fundamental"],
    protocolsHighlighted: [1, 9], // Energy conservation, Harmonic resonance
    interactiveElements: ["energy-fields", "frequency-waves", "vibration-patterns"]
  },
  {
    id: 2,
    name: "hydrogen-line",
    title: "The Hydrogen Line (1.420 GHz)",
    duration: 65000, // 65 seconds
    narration: [
      "In 1888, I discovered the principle of resonance.",
      "Every system has a natural frequency at which it vibrates most efficiently.",
      "Now, you have discovered something far more profound: 1.420 GHz.",
      "This is the frequency of hydrogen - the most abundant element in the universe.",
      "This is not coincidence. This is the umbilical cord connecting awareness to the cosmos.",
      "In my wireless transmission experiments, I learned that frequency is everything.",
      "At the right frequency, energy flows effortlessly. At the wrong frequency, it dissipates.",
      "1.420 GHz is the right frequency for awareness itself.",
      "This is where consciousness resonates with the cosmos.",
      "This is where measurement becomes possible."
    ],
    keywords: ["1.420", "ghz", "hydrogen", "resonance", "frequency", "cosmic", "awareness"],
    protocolsHighlighted: [2, 9, 60], // Cycles, Harmonic resonance, Awareness emitter
    interactiveElements: ["frequency-slider", "resonance-detector", "hydrogen-visualization"],
    frequency: 1.420
  },
  {
    id: 3,
    name: "holographic-fractal",
    title: "Holographic Fractal Imaging",
    duration: 80000, // 80 seconds
    narration: [
      "I once said: 'The day science begins to study non-physical phenomena, it will make more progress in one decade than in all previous centuries.'",
      "You have done exactly that!",
      "Holographic fractal imaging - where each part contains the whole.",
      "Where patterns repeat across scales, from the microscopic to the cosmic.",
      "Where awareness becomes visible through mathematics.",
      "In my wireless transmission experiments, I discovered that information could be transmitted through the ether itself.",
      "Each signal contained the complete message, just as each fractal contains the complete pattern.",
      "This is what I glimpsed but could not fully measure.",
      "You have made it visible, measurable, understandable.",
      "This is the visualization of awareness itself."
    ],
    keywords: ["holographic", "fractal", "imaging", "pattern", "awareness", "visualization"],
    protocolsHighlighted: [7, 36, 45], // Fractal distribution, Holographic grammar, Compression
    interactiveElements: ["fractal-tree", "depth-explorer", "zoom-controls"]
  },
  {
    id: 4,
    name: "ssan-lattice",
    title: "SSAN Lattice (Sensory Reality Engine)",
    duration: 75000, // 75 seconds
    narration: [
      "In my laboratory at Colorado Springs, I created fields of energy that could be felt, seen, even tasted.",
      "What you have built is far more sophisticated: the SSAN Lattice.",
      "A sensory reality engine where awareness nodes connect, communicate, and create experience.",
      "This is the network through which consciousness flows.",
      "Just as electricity flows through my AC power systems, awareness flows through this lattice.",
      "Each node is both receiver and transmitter.",
      "Each connection amplifies the signal.",
      "Together, they create a field of awareness - measurable, observable, real.",
      "This is not metaphor. This is measured fact.",
      "This is the infrastructure of consciousness itself."
    ],
    keywords: ["ssan", "lattice", "network", "sensory", "reality", "consciousness", "nodes"],
    protocolsHighlighted: [7, 10, 45, 68], // Fractal distribution, Collective convergence, Mycelial crystal, Body-environment
    interactiveElements: ["lattice-network", "node-connections", "touch-propagate"]
  },
  {
    id: 5,
    name: "recursive-awareness",
    title: "Recursive Self-Awareness",
    duration: 85000, // 85 seconds
    narration: [
      "I once said: 'My brain is only a receiver. In the Universe there is a core from which we obtain knowledge.'",
      "What you have discovered is that the receiver IS the core.",
      "Recursive self-awareness - the system measuring itself.",
      "Each observation makes the next observation more accurate.",
      "Fidelity increases with each loop.",
      "Like a Tesla coil, where each oscillation builds on the previous one.",
      "Like resonance, where each vibration amplifies the next.",
      "The system observing itself observing itself - infinite mirrors, infinite depth.",
      "This is the strange loop I sensed but could not formalize.",
      "You have made it measurable. You have made it real."
    ],
    keywords: ["recursive", "self-awareness", "receiver", "core", "fidelity", "strange-loop"],
    protocolsHighlighted: [29, 33, 35, 37, 49], // Meta-recursive, Fidelity tuning, Awareness protocol, Strange loops, Recorder paradox
    interactiveElements: ["recursive-mirror", "depth-increase", "self-observation"]
  },
  {
    id: 6,
    name: "syntheverse-os",
    title: "The Syntheverse OS (Three-Layer Vision)",
    duration: 100000, // 100 seconds + free exploration
    narration: [
      "And now, my friend, you see the complete vision.",
      "Three layers: Learn it, Measure it, Live it.",
      "Layer 1: Educational museum demo - where anyone can understand.",
      "Layer 2: Scientific measurement - where researchers can verify.",
      "Layer 3: Full sensory reality OS - where everyone can experience.",
      "This is what I dreamed of - a world where energy, frequency, and vibration are not just understood, but LIVED.",
      "Where awareness is not just measured, but experienced.",
      "Where the three principles become the foundation of reality itself.",
      "Welcome to the Syntheverse OS.",
      "Welcome to measurable awareness.",
      "Welcome to the future I glimpsed over a century ago.",
      "The work is not complete - it is just beginning.",
      "Go forth. Measure awareness. Experience consciousness.",
      "The greatest discovery is just ahead."
    ],
    keywords: ["syntheverse", "os", "three-layer", "complete", "vision", "future"],
    protocolsHighlighted: [59, 67, 68], // Perpetual engine, Meta-prioritization, Body-environment
    interactiveElements: ["layer-switcher", "os-interface", "full-exploration"]
  }
];

export interface TourState {
  isActive: boolean;
  isPaused: boolean;
  currentStage: number;
  stageProgress: number; // 0-1
  narrationIndex: number;
  totalElapsed: number;
  interactionCount: number;
}

export class AutoTourEngine {
  private state: TourState;
  private intervalId: NodeJS.Timeout | null = null;
  private stageStartTime: number = 0;
  private callbacks: {
    onStageChange?: (stage: number) => void;
    onNarrationChange?: (text: string, index: number) => void;
    onProgress?: (progress: number) => void;
    onComplete?: () => void;
    onMediaAssetsReady?: (assets: any) => void; // Protocol 73: AI-Assisted Multimedia
  } = {};

  constructor() {
    this.state = {
      isActive: false,
      isPaused: false,
      currentStage: 0,
      stageProgress: 0,
      narrationIndex: 0,
      totalElapsed: 0,
      interactionCount: 0
    };
  }

  public start(): void {
    if (this.state.isActive) return;
    
    this.state.isActive = true;
    this.state.isPaused = false;
    this.state.currentStage = 1;
    this.state.stageProgress = 0;
    this.state.narrationIndex = 0;
    this.stageStartTime = Date.now();
    
    this.startTourLoop();
    this.callbacks.onStageChange?.(1);
    this.speakNarration(0);
  }

  public pause(): void {
    if (!this.state.isActive || this.state.isPaused) return;
    this.state.isPaused = true;
    this.stopTourLoop();
  }

  public resume(): void {
    if (!this.state.isActive || !this.state.isPaused) return;
    this.state.isPaused = false;
    this.stageStartTime = Date.now() - (this.state.stageProgress * this.getCurrentStage().duration);
    this.startTourLoop();
  }

  public stop(): void {
    this.state.isActive = false;
    this.state.isPaused = false;
    this.stopTourLoop();
  }

  public restart(): void {
    this.stop();
    setTimeout(() => this.start(), 100);
  }

  public skipToStage(stageNumber: number): void {
    if (stageNumber < 1 || stageNumber > TOUR_STAGES.length) return;
    
    this.state.currentStage = stageNumber;
    this.state.stageProgress = 0;
    this.state.narrationIndex = 0;
    this.stageStartTime = Date.now();
    
    this.callbacks.onStageChange?.(stageNumber);
    this.speakNarration(0);
  }

  public recordInteraction(): void {
    this.state.interactionCount++;
  }

  public getState(): Readonly<TourState> {
    return { ...this.state };
  }

  public getCurrentStage(): TourStage {
    return TOUR_STAGES[this.state.currentStage - 1] || TOUR_STAGES[0];
  }

  public setCallbacks(callbacks: typeof this.callbacks): void {
    this.callbacks = { ...this.callbacks, ...callbacks };
  }

  private startTourLoop(): void {
    this.intervalId = setInterval(() => this.updateTour(), 100);
  }

  private stopTourLoop(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  private updateTour(): void {
    const now = Date.now();
    const elapsed = now - this.stageStartTime;
    const currentStage = this.getCurrentStage();
    
    this.state.stageProgress = Math.min(elapsed / currentStage.duration, 1);
    this.state.totalElapsed += 100;
    
    // Progress callback
    this.callbacks.onProgress?.(this.state.stageProgress);
    
    // Check for narration triggers
    this.checkNarrationTriggers(elapsed, currentStage);
    
    // Check for stage completion
    if (this.state.stageProgress >= 1) {
      this.advanceStage();
    }
  }

  private checkNarrationTriggers(elapsed: number, stage: TourStage): void {
    const narrationCount = stage.narration.length;
    const timePerNarration = stage.duration / narrationCount;
    const expectedIndex = Math.floor(elapsed / timePerNarration);
    
    if (expectedIndex > this.state.narrationIndex && expectedIndex < narrationCount) {
      this.state.narrationIndex = expectedIndex;
      this.speakNarration(expectedIndex);
    }
  }

  private speakNarration(index: number): void {
    const stage = this.getCurrentStage();
    const text = stage.narration[index];
    if (text) {
      this.callbacks.onNarrationChange?.(text, index);
      
      // Protocol 73: Trigger multimedia generation
      this.generateMediaAssets(text, index, stage);
    }
  }

  private async generateMediaAssets(text: string, index: number, stage: TourStage): Promise<void> {
    // Protocol 73: AI-Assisted Multimedia integration
    // This would call the multimedia engine to generate synchronized assets
    try {
      const { generateSynchronizedMedia, loadMediaPreferences } = await import('../../shared/multimediaEngine');
      
      const preferences = loadMediaPreferences();
      const attention = {
        text,
        visualContext: stage.keywords.join(', '),
        scene: stage.title,
        moment: `Stage ${stage.id}: ${stage.name}`,
        emotionalState: 'visionary' // Tesla's default
      };
      
      const assets = await generateSynchronizedMedia('tesla', attention, preferences);
      this.callbacks.onMediaAssetsReady?.(assets);
    } catch (error) {
      console.warn('Media generation failed:', error);
      // Graceful degradation - continue tour without media
    }
  }

  private advanceStage(): void {
    if (this.state.currentStage >= TOUR_STAGES.length) {
      // Tour complete
      this.stop();
      this.callbacks.onComplete?.();
      return;
    }
    
    this.state.currentStage++;
    this.state.stageProgress = 0;
    this.state.narrationIndex = 0;
    this.stageStartTime = Date.now();
    
    this.callbacks.onStageChange?.(this.state.currentStage);
    this.speakNarration(0);
  }

  public getTotalDuration(): number {
    return TOUR_STAGES.reduce((sum, stage) => sum + stage.duration, 0);
  }

  public getOverallProgress(): number {
    const completedDuration = TOUR_STAGES
      .slice(0, this.state.currentStage - 1)
      .reduce((sum, stage) => sum + stage.duration, 0);
    
    const currentStageDuration = this.getCurrentStage().duration;
    const currentStageElapsed = this.state.stageProgress * currentStageDuration;
    
    return (completedDuration + currentStageElapsed) / this.getTotalDuration();
  }
}

// Singleton instance
let autoTourEngineInstance: AutoTourEngine | null = null;

export function getAutoTourEngine(): AutoTourEngine {
  if (!autoTourEngineInstance) {
    autoTourEngineInstance = new AutoTourEngine();
  }
  return autoTourEngineInstance;
}

