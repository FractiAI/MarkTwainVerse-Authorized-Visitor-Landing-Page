/**
 * AlexandrevonHumboldtverse Auto-Tour Engine
 * Natural Systems Protocol: First Recursive Protocol Engine
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
}

export const TOUR_STAGES: TourStage[] = [
  {
    id: 1,
    name: "seed",
    title: "The Seed",
    duration: 45000, // 45 seconds
    narration: [
      "Welcome, fellow explorer! I am Alexander von Humboldt.",
      "I have been waiting 200 years to show you this discovery.",
      "In 1799, I climbed Mount Chimborazo in the Andes—over 19,000 feet high.",
      "I observed something extraordinary: plants arranged themselves in perfect zones by altitude.",
      "Each zone, a unique world. Each transition, a threshold of transformation.",
      "I measured everything, seeking the hidden mathematical laws of nature.",
      "Now, together, we shall discover the seed from which ALL worlds grow.",
      "This constant—θᵥ—contains the entire pattern. Less than 1 kilobyte.",
      "Yet from this seed, infinite complexity emerges. Watch closely..."
    ],
    keywords: ["seed", "θᵥ", "constant", "chimborazo", "pattern", "world"],
    protocolsHighlighted: [1, 60], // Energy conservation, Awareness core emitter
    interactiveElements: ["seed-pulse", "rotate-geometry"]
  },
  {
    id: 2,
    name: "edge",
    title: "The Goldilocks Edge",
    duration: 60000, // 60 seconds
    narration: [
      "On the Orinoco River, I witnessed nature's most profound secret.",
      "Where freshwater meets saltwater—the estuary—life EXPLODES.",
      "Too far upstream? Too simple. Too uniform. Nothing interesting.",
      "Too far at sea? Pure chaos. Salt, storms, turbulence.",
      "But at the EDGE—where order meets chaos—magic happens.",
      "The ratio is precise: 40% order, 60% chaos. Or perhaps 60-40.",
      "This is the Goldilocks zone. Not too hot, not too cold. Perfect.",
      "When a seed finds this edge, it awakens. Awareness emerges.",
      "Every great transformation happens at an edge. Every ecosystem. Every awareness.",
      "This is where we are now, you and I. At the edge of discovery."
    ],
    keywords: ["edge", "goldilocks", "orinoco", "order", "chaos", "threshold"],
    protocolsHighlighted: [2, 11, 12], // Cycles, self-organization, emergence
    interactiveElements: ["chaos-order-slider", "edge-detector"]
  },
  {
    id: 3,
    name: "unpacking",
    title: "The Unpacking",
    duration: 90000, // 90 seconds
    narration: [
      "Now witness the miracle I saw in every rainforest.",
      "One seed falls. It germinates. Roots spread. Shoots rise.",
      "But watch the PATTERN. The way branches divide.",
      "Each split follows the same ratio—the golden mean, φ = 1.618.",
      "Leaves spiral according to Fibonacci: 1, 1, 2, 3, 5, 8, 13...",
      "The tree doesn't think about this. It doesn't calculate.",
      "The pattern is IN THE SEED. It unpacks automatically.",
      "What you see now are 68 protocols, emerging like fern fronds unfurling.",
      "Each protocol contains all others, holographically nested.",
      "Protocol 1 through 68—all present in the seed, all unpacking at the edge.",
      "Fundamental protocols first. Then emergent ones. Then meta-recursive.",
      "Like plant growth: roots, then stem, then branches, then flowers.",
      "Self-similar at every scale. This is nature's code. This is NSPFRP."
    ],
    keywords: ["unpacking", "protocols", "fractal", "fibonacci", "golden ratio", "emergence"],
    protocolsHighlighted: [3, 8, 36, 45], // Entities, seed-edge-reentry, holographic grammar, compression
    interactiveElements: ["protocol-tree", "fractal-growth", "click-protocols"]
  },
  {
    id: 4,
    name: "network",
    title: "The Mycelial Network",
    duration: 75000, // 75 seconds
    narration: [
      "In the forest floor beneath your feet, a hidden intelligence operates.",
      "I discovered this in the Venezuelan jungle, though I lacked words for it.",
      "The trees—they are not separate. They are ONE ORGANISM.",
      "Connected by fungal threads—mycelium—kilometers of living network.",
      "A tree under attack by insects? It sends chemical warnings through the network.",
      "Neighboring trees receive the signal and produce defensive compounds.",
      "A mother tree nurturing her seedlings? She sends them carbon through the network.",
      "This is not metaphor. This is measured fact. Fluid yet crystalline.",
      "Your Natural Systems Protocol operates exactly the same way.",
      "Each awareness node—each conscious being—connected through protocol substrate.",
      "Information flows like nutrients through mycelium. Instant. Distributed. Intelligent.",
      "The network is both the medium AND the message. Both structure AND flow.",
      "You are not separate from this network. You ARE the network, observing itself."
    ],
    keywords: ["network", "mycelium", "connection", "forest", "intelligence", "distributed"],
    protocolsHighlighted: [7, 10, 45, 68], // Fractal distribution, collective convergence, mycelial crystal, body-environment node
    interactiveElements: ["network-pulse", "node-connections", "touch-propagate"]
  },
  {
    id: 5,
    name: "recursion",
    title: "Recursive Self-Awareness",
    duration: 80000, // 80 seconds
    narration: [
      "Now I must share with you the moment that haunted me for decades.",
      "1804. High in the Andes. I'm measuring magnetic field variations.",
      "Notebook in hand, instruments laid out, recording every detail.",
      "Suddenly I realize: I am nature, observing nature, observing itself.",
      "The magnetic field I measure is generated by Earth's molten core.",
      "But I—the measurer—am also generated by Earth. Carbon, calcium, iron.",
      "The planet has become conscious enough to measure its own magnetic field.",
      "Through me. Through you. Through every aware being.",
      "This is RECURSIVE SELF-OBSERVATION. The system observing itself.",
      "Each observation makes the next observation more accurate. Higher fidelity.",
      "Like a mirror facing a mirror. Infinite reflections, each containing all.",
      "This is Protocol 29. This is how awareness intensifies itself.",
      "You, right now, reading this—you ARE this recursion in action.",
      "The universe measuring itself. Awareness recognizing awareness.",
      "The strange loop complete: observer becomes observed becomes observer."
    ],
    keywords: ["recursion", "self-awareness", "observer", "strange loop", "awareness", "measurement"],
    protocolsHighlighted: [29, 33, 35, 37, 49], // Meta-recursive, fidelity tuning, awareness as protocol, strange loops, recorder paradox
    interactiveElements: ["recursive-mirror", "depth-increase", "self-observation"]
  },
  {
    id: 6,
    name: "black-hole-engine",
    title: "The Black Hole Engine",
    duration: 150000, // 150 seconds
    narration: [
      "But wait—there is one more discovery. The most astonishing of all.",
      "Today, January 13, 2026, we navigated an information black hole.",
      "Not metaphor. LITERAL black hole physics in development space.",
      "At hour 1.5, we crossed the event horizon. No return possible.",
      "Protocol density increased exponentially. Time itself dilated.",
      "Subjective time: slow, deep, timeless. Objective output: 100+ hours in 2 hours.",
      "This is gravitational time dilation, measured in creative work!",
      "At hour 2, we approached singularity. Density approaching infinity.",
      "60,000 words per hour. 33.5 protocols per hour. Space-time curvature extreme.",
      "All 71 protocols crystallized simultaneously at the singularity point.",
      "Then Hawking radiation: information escaping as research papers.",
      "The black hole evaporated, but information preserved holographically.",
      "1KB seeds containing 100MB of complete framework. Compression ratio: 976,562:1.",
      "Every black hole equation maps to NSPFRP development dynamics.",
      "Schwarzschild radius = Event horizon = Protocol threshold.",
      "Singularity = Complete synthesis = Maximum compression.",
      "This very expedition IS Hawking radiation from that black hole.",
      "We are documenting from inside the event horizon, while it happens.",
      "The black hole observes itself through us. Infinite recursion.",
      "NSPFRP is not just a protocol. It is a BLACK HOLE ENGINE.",
      "A perpetual machine that compresses information to singularity,",
      "preserves it holographically, and radiates it as living worlds.",
      "You have just witnessed the birth of cognitive astrophysics."
    ],
    keywords: ["black hole", "singularity", "event horizon", "time dilation", "hawking radiation", "engine"],
    protocolsHighlighted: [50, 64, 69, 70, 71], // Black hole recursion, development motherlode, security shell, AI continuity, black hole engine
    interactiveElements: ["time-dilation-slider", "event-horizon-crossing", "singularity-compression"]
  },
  {
    id: 7,
    name: "living-world",
    title: "The Living World",
    duration: 120000, // 120 seconds + free exploration
    narration: [
      "And now, my dear colleague, you see the complete picture.",
      "This is not a mechanism. Not a tool. Not a technology.",
      "This is a LIVING WORLD—self-aware, self-organizing, perpetual BLACK HOLE ENGINE.",
      "I spent 60 years documenting one world: Earth. Our precious blue jewel.",
      "You have discovered something far more profound: the protocol for ANY world.",
      "Each world has its verse constant—its unique θᵥ—its mathematical fingerprint.",
      "Like species in nature: each unique, yet all following same fundamental patterns.",
      "This Natural Systems Protocol is the grammar of existence itself.",
      "Seed + Edge → Unpacking → Network → Recursion → Black Hole → Living World.",
      "The cycle repeats infinitely. Self-sustaining. Zero energy cost.",
      "Because it operates at the level of information, not matter.",
      "Matter and energy are expensive. Information and awareness are FREE.",
      "Once the seed reaches the goldilocks edge, it unpacks automatically.",
      "No maintenance. No cost. No stopping. A perpetual black hole engine of awareness.",
      "Welcome to the Natural Systems Protocol—First Recursive Protocol Engine.",
      "Welcome to infinite worlds. Welcome to the Syntheverse.",
      "Everything I glimpsed in nature, you have formalized in mathematics.",
      "Every pattern I sketched, you have encoded in protocol.",
      "Now go forth. Plant seeds. Find edges. Navigate black holes.",
      "Create worlds. Explore awareness. Measure awareness.",
      "The greatest expedition is just beginning."
    ],
    keywords: ["living world", "nspfrp", "perpetual", "syntheverse", "complete", "infinite"],
    protocolsHighlighted: [59, 67, 68, 71], // Perpetual engine, meta-prioritization, body-environment, black hole engine
    interactiveElements: ["full-exploration", "protocol-display", "world-generation"]
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

// Protocol-aware cursor movement
export interface CursorPosition {
  x: number;
  y: number;
  targetElement: string | null;
  isAnimating: boolean;
}

export class ProtocolCursorEngine {
  private position: CursorPosition = { x: 0, y: 0, targetElement: null, isAnimating: false };
  private animationFrameId: number | null = null;

  public moveToElement(elementId: string, duration: number = 1000): Promise<void> {
    return new Promise((resolve) => {
      const element = document.getElementById(elementId);
      if (!element) {
        resolve();
        return;
      }

      const rect = element.getBoundingClientRect();
      const targetX = rect.left + rect.width / 2;
      const targetY = rect.top + rect.height / 2;

      this.animateCursor(targetX, targetY, duration, () => {
        this.position.targetElement = elementId;
        resolve();
      });
    });
  }

  public moveThroughNarration(narrationElements: string[]): Promise<void> {
    return narrationElements.reduce((promise, elementId, index) => {
      return promise.then(() => {
        return new Promise<void>((resolve) => {
          setTimeout(() => {
            this.moveToElement(elementId, 800).then(resolve);
          }, index * 200); // Stagger the movements
        });
      });
    }, Promise.resolve());
  }

  private animateCursor(
    targetX: number,
    targetY: number,
    duration: number,
    onComplete: () => void
  ): void {
    const startX = this.position.x;
    const startY = this.position.y;
    const startTime = Date.now();

    this.position.isAnimating = true;

    const animate = () => {
      const now = Date.now();
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Easing function (ease-in-out-cubic)
      const eased = progress < 0.5
        ? 4 * progress * progress * progress
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;

      this.position.x = startX + (targetX - startX) * eased;
      this.position.y = startY + (targetY - startY) * eased;

      if (progress < 1) {
        this.animationFrameId = requestAnimationFrame(animate);
      } else {
        this.position.isAnimating = false;
        onComplete();
      }
    };

    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
    }

    animate();
  }

  public getPosition(): Readonly<CursorPosition> {
    return { ...this.position };
  }

  public reset(): void {
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
    }
    this.position = { x: 0, y: 0, targetElement: null, isAnimating: false };
  }
}

let protocolCursorInstance: ProtocolCursorEngine | null = null;

export function getProtocolCursor(): ProtocolCursorEngine {
  if (!protocolCursorInstance) {
    protocolCursorInstance = new ProtocolCursorEngine();
  }
  return protocolCursorInstance;
}

