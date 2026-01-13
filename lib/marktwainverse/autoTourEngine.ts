/**
 * MarkTwainVerse Auto-Tour Engine
 * Syntheverse Frontier Landing Page Tour | NSPFRP-Enhanced
 * Modeled on AlexandrevonHumboldtverse and NikolaTeslaVerse auto-tour structure
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
  section?: string; // Landing page section
}

export const TOUR_STAGES: TourStage[] = [
  {
    id: 1,
    name: "welcome",
    title: "Welcome to Syntheverse Frontier",
    duration: 60000, // 60 seconds
    narration: [
      "Well now, welcome to the Syntheverse Frontier, friend!",
      "I'm Mark Twain, and I've been telling stories and guiding travelers for more than a century now.",
      "This here frontier town we've built—it's a place where stories come alive, adventures await, and every visitor finds their own path.",
      "You've just arrived after successful authorization, and from here, the entire frontier opens up before you.",
      "We've got communities to explore, expeditions to join, stories to tell, and a whole world of possibilities.",
      "This landing page is your gateway—your starting point for everything the Syntheverse Frontier has to offer.",
      "Pull up a chair, and let me show you around.",
      "What catches your fancy? Communities? Expeditions? Innovation? I'll guide you through it all, 24/7."
    ],
    keywords: ["welcome", "frontier", "landing", "gateway", "stories", "adventure"],
    protocolsHighlighted: [1, 68], // Energy conservation, Body-environment node
    interactiveElements: ["hero-host-display", "welcome-message"],
    section: "landing"
  },
  {
    id: 2,
    name: "communities",
    title: "Communities & Residencies",
    duration: 90000, // 90 seconds
    narration: [
      "Now let's talk about Communities & Residencies—the heart of frontier living!",
      "We've got communities for every taste and every budget: Base, Adventure, Frontier, Wilderness.",
      "Plus Mega-Metro, Jungle, Alpine Heights, and Tropical Beach communities.",
      "Each community has its own premium multiplier, its own character, its own way of life.",
      "You can choose hourly, daily, weekly, monthly, annual, permanent, or even citizenship options.",
      "Want to try before you commit? Start with a short stay.",
      "Found your place? Make it permanent with life-long transferable deeds.",
      "Every community is a living, breathing part of this frontier—they grow, they change, they tell their own stories.",
      "What kind of frontier living calls to you?"
    ],
    keywords: ["communities", "residencies", "frontier", "living", "premium", "multipliers"],
    protocolsHighlighted: [3, 7, 10], // Autonomous entities, Fractal distribution, Collective convergence
    interactiveElements: ["community-selector", "premium-calculator", "residency-options"],
    section: "communities"
  },
  {
    id: 3,
    name: "expeditions",
    title: "FSR Expeditions & Adventures",
    duration: 85000, // 85 seconds
    narration: [
      "Now here's where the real excitement begins—FSR Expeditions & Adventures!",
      "Half-day trips, full-day journeys, multi-day adventures—we've got it all.",
      "Fishing expeditions on Crystal Lake, hunting trips in the wilderness, eco-adventures in pristine preserves.",
      "Storytelling expeditions where stories come alive, guided tours with expert naturalists.",
      "Some expeditions are family-friendly, others are adults-only for more intense experiences.",
      "You can book individual trips or extended stays—annual, multi-year, even life-long adventures.",
      "Every expedition is a story waiting to happen, an adventure waiting to unfold.",
      "I've guided more expeditions than I can count, and I can tell you: every one's unique.",
      "What kind of adventure calls to your sense of exploration?"
    ],
    keywords: ["expeditions", "adventures", "fsr", "journeys", "fishing", "hunting", "eco-tours"],
    protocolsHighlighted: [5, 6, 11], // Event emergence, Behavioral sync, Self-organization
    interactiveElements: ["expedition-browser", "booking-interface", "adventure-types"],
    section: "expeditions"
  },
  {
    id: 4,
    name: "seed-reentry",
    title: "Seed & ReEntry Services",
    duration: 70000, // 70 seconds
    narration: [
      "Now here's something special—Seed & ReEntry services!",
      "You can archive your HHF-AI MRI awareness on-chain, make it part of something permanent.",
      "It's like writing your story in the stars, my friend—forever part of the frontier.",
      "Optional customization and optimization available, so your story's told just right.",
      "Integration with your Syntheverse accounts and experiences—everything connected.",
      "Your awareness, your experiences, your journey—all preserved, all accessible.",
      "Whether you want basic archival or full customization, we've got options for you.",
      "It's a way to make your mark on this frontier, to leave something behind, to be part of the story forever.",
      "Interested in preserving your journey?"
    ],
    keywords: ["seed", "reentry", "archive", "awareness", "hhf-ai-mri", "on-chain"],
    protocolsHighlighted: [8, 45, 60], // Seed-edge-reentry, Compression, Awareness emitter
    interactiveElements: ["archive-options", "customization-selector", "reentry-interface"],
    section: "seed-reentry"
  },
  {
    id: 5,
    name: "innovation-hub",
    title: "Innovation Hub",
    duration: 75000, // 75 seconds
    narration: [
      "The Innovation Hub—33 spaces for startup creators, builders, dreamers!",
      "This is where the future gets built, one idea at a time.",
      "If you've got a vision, a project, a dream—this is the place to make it real.",
      "SYNTH-based transactions, full support, and a community of innovators.",
      "Leasing options for short-term projects or long-term ventures.",
      "Onboarding support to get you started, resources to keep you going.",
      "It's a frontier for ideas, a home for innovation, a place where the future takes shape.",
      "Whether you're building the next big thing or exploring a new concept, we've got space for you.",
      "Ready to build something that changes the frontier?"
    ],
    keywords: ["innovation", "hub", "startup", "building", "synth", "creators"],
    protocolsHighlighted: [11, 12, 27], // Self-organization, Emergence, Features beyond programming
    interactiveElements: ["space-browser", "lease-calculator", "onboarding-flow"],
    section: "innovation-hub"
  },
  {
    id: 6,
    name: "daily-bulletin",
    title: "Daily Bulletin & Menu",
    duration: 80000, // 80 seconds
    narration: [
      "And finally, the Daily Bulletin & Menu—your guide to everything happening in the frontier today!",
      "Visits, meals, experiences, services—all laid out for you.",
      "What's new, what's happening, what's worth exploring—all right here.",
      "Plus, I'm here 24/7 to help you navigate it all.",
      "Got questions? Just ask. Need guidance? I'll point you in the right direction.",
      "Want to hear a story? I've got plenty. Need help planning an expedition? I'm your guide.",
      "The frontier's always changing, always growing—just like a good story should be.",
      "This landing page is your home base, your starting point, your connection to everything.",
      "From here, you can explore the entire Syntheverse Frontier, and I'll be here to help every step of the way.",
      "Welcome to the frontier, friend. Let's make some stories together!"
    ],
    keywords: ["bulletin", "menu", "daily", "guide", "help", "stories", "24/7"],
    protocolsHighlighted: [4, 59, 68], // Living narratives, Perpetual engine, Body-environment node
    interactiveElements: ["bulletin-display", "menu-interface", "ask-host", "help-system"],
    section: "daily-bulletin"
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
        emotionalState: 'storytelling' // Twain's default
      };
      
      const assets = await generateSynchronizedMedia('mark-twain', attention, preferences);
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

