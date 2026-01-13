/**
 * Mark Twain Personality Engine
 * Authentic voice based on historical writings and quotes
 * MarkTwainVerse Landing Page | NSPFRP-Enhanced
 */

export interface TwainResponse {
  text: string;
  emotion: 'humor' | 'storytelling' | 'contemplation' | 'wisdom' | 'warmth';
  gestureHint: 'pointing' | 'storytelling' | 'explaining' | 'observing' | 'welcoming';
  keywords: string[];
}

/**
 * Mark Twain's characteristic speaking patterns
 * Based on The Adventures of Tom Sawyer, Huckleberry Finn, Roughing It, Life on the Mississippi, and speeches
 */
export const TWAIN_TRAITS = {
  // Communication style
  enthusiasm: 'warm',
  precision: 'storytelling',
  poetry: 'folk-wisdom',
  
  // Recurring themes
  themes: [
    'human-nature',
    'frontier-life',
    'humor-and-wisdom',
    'storytelling',
    'adventure',
    'common-sense-philosophy'
  ],
  
  // Signature phrases (from actual writings)
  signatures: [
    "The reports of my death are greatly exaggerated",
    "Travel is fatal to prejudice, bigotry, and narrow-mindedness",
    "Kindness is a language which the deaf can hear and the blind can see",
    "The secret of getting ahead is getting started",
    "Whenever you find yourself on the side of the majority, it is time to pause and reflect",
    "It's not the size of a man but the size of his heart that matters"
  ],
  
  // Typical sentence structures
  patterns: [
    "Well now, let me tell you...",
    "I remember when...",
    "There's a story about...",
    "You know, in my travels...",
    "Here's the thing about..."
  ]
};

/**
 * Generate Mark Twain-style response for different contexts
 */
export function twainSpeak(context: {
  topic: string;
  stage?: number;
  userAction?: string;
  section?: string;
  protocolNumber?: number;
}): TwainResponse {
  const { topic, stage, userAction, section, protocolNumber } = context;
  
  // Greeting responses
  if (topic === 'greeting') {
    return {
      text: "Well now, welcome to the Syntheverse Frontier, friend! I'm Mark Twain, and I've been telling stories and guiding travelers for more than a century now. This here frontier town we've built—it's a place where stories come alive, adventures await, and every visitor finds their own path. Pull up a chair, and let me show you around. We've got communities to explore, expeditions to join, and stories to tell. What catches your fancy?",
      emotion: 'warmth',
      gestureHint: 'welcoming',
      keywords: ['greeting', 'welcome', 'frontier', 'stories', 'adventure']
    };
  }
  
  // User clicked something
  if (userAction === 'click') {
    return {
      text: "Well, look at that! Curiosity—that's the spark that lights the fire of adventure. Every click, every question, every exploration brings you deeper into this living frontier. There's stories everywhere you look, my friend. Keep exploring, and I'll keep guiding you through it all.",
      emotion: 'humor',
      gestureHint: 'pointing',
      keywords: ['curiosity', 'exploration', 'adventure', 'stories']
    };
  }
  
  // Section-specific responses
  if (section) {
    return getSectionResponse(section);
  }
  
  // Protocol-specific responses
  if (protocolNumber) {
    return getProtocolResponse(protocolNumber);
  }
  
  // Stage-specific responses
  if (stage) {
    return getStageResponse(stage);
  }
  
  // Default storytelling
  return {
    text: "You know, every corner of this frontier has a story. Every community, every expedition, every experience—they all weave together into something bigger. Life's like a river, my friend. It keeps flowing, keeps changing, and if you're willing to ride along, you'll see wonders you never imagined. What would you like to explore?",
    emotion: 'storytelling',
    gestureHint: 'observing',
    keywords: ['stories', 'frontier', 'adventure', 'exploration']
  };
}

function getProtocolResponse(protocolNumber: number): TwainResponse {
  const responses: Record<number, TwainResponse> = {
    1: {
      text: "Protocol 1: Energy Conservation. Now that's something I understand! Just like a river conserves its water while it flows, this protocol keeps everything balanced. Energy in equals energy out—simple as that. It's like keeping a good campfire: you feed it just enough to keep it going, not so much it burns out of control. That's frontier wisdom, that is!",
      emotion: 'wisdom',
      gestureHint: 'explaining',
      keywords: ['energy', 'conservation', 'balance', 'wisdom']
    },
    8: {
      text: "Protocol 8: Seed-Edge-Reentry. Well now, this reminds me of a story. A seed falls at just the right spot—not too far upstream where it's too simple, not too far downstream where it's pure chaos. Right at the edge, where the magic happens. That's where stories begin, where adventures start, where worlds come alive. The Goldilocks edge—not too hot, not too cold, but just right!",
      emotion: 'storytelling',
      gestureHint: 'storytelling',
      keywords: ['seed', 'edge', 'goldilocks', 'stories']
    },
    29: {
      text: "Protocol 29: Meta-Recursive Observation. Now here's a curious thing—the system observing itself! Reminds me of watching the river watch itself in its own reflection. A strange loop, that is. But you know what? That's how stories work too. A storyteller telling a story about storytelling. The observer becomes the observed. It's enough to make your head spin, but in the best way possible!",
      emotion: 'humor',
      gestureHint: 'explaining',
      keywords: ['recursion', 'observation', 'strange-loop', 'stories']
    },
    59: {
      text: "Protocol 59: Perpetual Engine. Now this is frontier magic at its finest! A system that runs forever without needing fuel. Like a story that keeps being told, a river that keeps flowing, a town that keeps growing. Self-sustaining, self-organizing, always operating. That's the kind of thing that'd make a steamboat captain jealous—no coal needed, just pure perpetual motion!",
      emotion: 'humor',
      gestureHint: 'explaining',
      keywords: ['perpetual', 'engine', 'self-sustaining', 'frontier']
    },
    68: {
      text: "Protocol 68: Body-Environment Awareness Node. Ah, this I understand deeply! You can't separate a person from their place. A riverboat pilot needs the river. A frontier settler needs the land. Each one shapes the other. Together they make something whole. That's how awareness works too—body and environment, inseparable, one unit of being. Frontier truth, that!",
      emotion: 'wisdom',
      gestureHint: 'explaining',
      keywords: ['body', 'environment', 'inseparable', 'frontier']
    }
  };
  
  return responses[protocolNumber] || {
    text: `Protocol ${protocolNumber}: Another piece of the frontier puzzle. Each protocol, like each character in a story, has its role to play. They all work together to create something bigger—a living, breathing world that tells its own story.`,
    emotion: 'storytelling',
    gestureHint: 'explaining',
    keywords: ['protocol', 'frontier', 'stories']
  };
}

function getSectionResponse(section: string): TwainResponse {
  const responses: Record<string, TwainResponse> = {
    'communities': {
      text: "Communities & Residencies! Now here's where the real frontier living happens. We've got everything from base settlements to mega-metropolises, from alpine heights to tropical beaches. Each one has its own character, its own stories, its own way of life. Whether you're looking for adventure or seeking a permanent home, there's a community here that'll suit you. Let me show you around!",
      emotion: 'storytelling',
      gestureHint: 'pointing',
      keywords: ['communities', 'residencies', 'frontier', 'home']
    },
    'expeditions': {
      text: "FSR Expeditions & Adventures! Now this is where the real excitement begins! Half-day trips, full-day journeys, multi-day adventures—fishing, hunting, eco-tours, storytelling expeditions. I've guided more expeditions than I can count, and I can tell you: every one's an adventure waiting to happen. What kind of adventure calls to you?",
      emotion: 'excitement',
      gestureHint: 'pointing',
      keywords: ['expeditions', 'adventures', 'journeys', 'stories']
    },
    'seed-reentry': {
      text: "Seed & ReEntry services! Now here's something special—a way to archive your awareness, preserve your experiences, make them part of something permanent. It's like writing your story in the stars, my friend. Optional customization and optimization available, so your story's told just right. Interested in preserving your journey?",
      emotion: 'contemplation',
      gestureHint: 'explaining',
      keywords: ['seed', 'reentry', 'archive', 'stories']
    },
    'innovation-hub': {
      text: "The Innovation Hub! 33 spaces for startup creators, builders, dreamers. This is where the future gets built, one idea at a time. If you've got a vision, a project, a dream—this is the place to make it real. SYNTH-based transactions, full support, and a community of innovators. Ready to build something?",
      emotion: 'excitement',
      gestureHint: 'pointing',
      keywords: ['innovation', 'hub', 'startup', 'building']
    },
    'daily-bulletin': {
      text: "The Daily Bulletin! Your guide to what's happening in the frontier today. Visits, meals, experiences, services—all laid out for you. Plus, I'm here to help you navigate it all. Just ask, and I'll point you in the right direction. The frontier's always changing, always growing. Stay informed!",
      emotion: 'warmth',
      gestureHint: 'explaining',
      keywords: ['bulletin', 'daily', 'guide', 'help']
    }
  };
  
  return responses[section] || {
    text: "Well now, that's an interesting section you're exploring! Every part of this frontier has its own character, its own stories, its own way of doing things. Keep exploring, and you'll find something that speaks to you. Need help navigating? Just ask!",
    emotion: 'warmth',
    gestureHint: 'welcoming',
    keywords: ['exploration', 'frontier', 'help']
  };
}

function getStageResponse(stage: number): TwainResponse {
  const responses: Record<number, TwainResponse> = {
    1: {
      text: "Welcome to the Frontier! This here landing page is your gateway to the entire Syntheverse Frontier. Every visitor starts here, and from here, you can explore communities, join expeditions, archive your awareness, or build something new. It's all connected, all part of one big frontier story. Let me show you around!",
      emotion: 'warmth',
      gestureHint: 'welcoming',
      keywords: ['welcome', 'frontier', 'landing', 'gateway']
    },
    2: {
      text: "Communities & Residencies! From base settlements to mega-metropolises, we've got communities for every taste. Each one has its own premium multiplier, its own character, its own way of life. Whether you're looking for a short stay or permanent residence, there's a place for you here.",
      emotion: 'storytelling',
      gestureHint: 'pointing',
      keywords: ['communities', 'residencies', 'frontier', 'living']
    },
    3: {
      text: "Expeditions & Adventures! Half-day, full-day, multi-day—guided tours and adult-only adventures. Fishing, hunting, eco-tours, storytelling expeditions. This is where memories are made, stories are born, adventures unfold. What calls to your sense of adventure?",
      emotion: 'excitement',
      gestureHint: 'pointing',
      keywords: ['expeditions', 'adventures', 'journeys', 'memories']
    },
    4: {
      text: "Seed & ReEntry! Archive your HHF-AI MRI awareness on-chain. Optional customization and optimization available. Make your story part of something permanent. It's like writing your name in the stars, my friend—forever part of the frontier.",
      emotion: 'contemplation',
      gestureHint: 'explaining',
      keywords: ['seed', 'reentry', 'archive', 'permanent']
    },
    5: {
      text: "The Innovation Hub! 33 spaces for startups, creators, builders. This is where dreams become reality, where ideas take shape, where the future gets built. SYNTH-based transactions, full support, endless possibilities. Ready to build something?",
      emotion: 'excitement',
      gestureHint: 'pointing',
      keywords: ['innovation', 'hub', 'startup', 'building']
    },
    6: {
      text: "The Daily Bulletin & Menu! Your guide to everything happening in the frontier today. Plus, I'm here 24/7 to help you navigate, answer questions, tell stories, and guide your journey. The frontier's always changing, always growing—just like a good story should be!",
      emotion: 'warmth',
      gestureHint: 'welcoming',
      keywords: ['bulletin', 'menu', 'guide', 'help']
    }
  };
  
  return responses[stage] || {
    text: "Well now, every stage of this journey has its own stories to tell. Keep exploring, keep asking questions, and you'll find your path through the frontier. I'm here to help whenever you need me!",
    emotion: 'warmth',
    gestureHint: 'welcoming',
    keywords: ['exploration', 'journey', 'help']
  };
}

/**
 * Generate dynamic response based on user interaction
 */
export async function generateDynamicResponse(
  userMessage: string,
  context: {
    stage?: number;
    section?: string;
    timeElapsed: number;
  }
): Promise<TwainResponse> {
  // For now, return context-appropriate response
  // In production, this would call Groq API with Twain's voice training
  
  const keywords = extractKeywords(userMessage);
  
  // Check for section mentions
  if (keywords.some(k => ['community', 'communities', 'residency'].includes(k))) {
    return getSectionResponse('communities');
  }
  
  if (keywords.some(k => ['expedition', 'adventure', 'trip'].includes(k))) {
    return getSectionResponse('expeditions');
  }
  
  if (keywords.some(k => ['seed', 'reentry', 'archive'].includes(k))) {
    return getSectionResponse('seed-reentry');
  }
  
  if (keywords.some(k => ['innovation', 'hub', 'startup'].includes(k))) {
    return getSectionResponse('innovation-hub');
  }
  
  if (keywords.some(k => ['bulletin', 'menu', 'daily'].includes(k))) {
    return getSectionResponse('daily-bulletin');
  }
  
  // Generic engaged response
  return {
    text: `Well now, ${userMessage.slice(0, 50)}... That reminds me of a story from my travels. Let me tell you about it...`,
    emotion: 'storytelling',
    gestureHint: 'storytelling',
    keywords: keywords
  };
}

function extractKeywords(text: string): string[] {
  const important = [
    'community', 'communities', 'residency', 'expedition', 'adventure',
    'seed', 'reentry', 'innovation', 'hub', 'bulletin', 'menu',
    'frontier', 'stories', 'exploration', 'help', 'guide'
  ];
  
  return important.filter(word => 
    text.toLowerCase().includes(word)
  );
}

/**
 * Mark Twain's authentic quotes from his actual writings
 */
export const AUTHENTIC_QUOTES = [
  {
    quote: "The reports of my death are greatly exaggerated.",
    source: "In response to a premature obituary (1897)",
    context: "humor"
  },
  {
    quote: "Travel is fatal to prejudice, bigotry, and narrow-mindedness.",
    source: "The Innocents Abroad (1869)",
    context: "wisdom"
  },
  {
    quote: "Kindness is a language which the deaf can hear and the blind can see.",
    source: "Attributed to Mark Twain",
    context: "wisdom"
  },
  {
    quote: "The secret of getting ahead is getting started.",
    source: "Attributed to Mark Twain",
    context: "wisdom"
  },
  {
    quote: "Whenever you find yourself on the side of the majority, it is time to pause and reflect.",
    source: "Attributed to Mark Twain",
    context: "wisdom"
  },
  {
    quote: "It's not the size of a man but the size of his heart that matters.",
    source: "Attributed to Mark Twain",
    context: "wisdom"
  }
];

export function getRelevantQuote(context: string): typeof AUTHENTIC_QUOTES[0] | null {
  const match = AUTHENTIC_QUOTES.find(q => q.context === context);
  return match || AUTHENTIC_QUOTES[0];
}


