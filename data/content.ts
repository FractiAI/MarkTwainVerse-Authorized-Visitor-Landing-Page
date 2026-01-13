// ============================================================================
// SYNTHEVERSE FRONTIER CATALOG - COMPLETE CONTENT DATA
// MarkTwainVerse Authorized Visitor Landing Page
// ============================================================================

export interface PricingTier {
  name: string;
  basePrice: number;
  currency: 'SYNTH';
  duration: string;
  benefits: string[];
}

export interface Community {
  id: string;
  name: string;
  description: string;
  premiumMultiplier: number;
  features: string[];
  atmosphere: string;
}

export interface Expedition {
  id: string;
  name: string;
  duration: string;
  type: 'fishing' | 'hunting' | 'eco-adventure' | 'storytelling' | 'exploration';
  price: number;
  guided: boolean;
  adultsOnly: boolean;
  description: string;
  included: string[];
}

export interface SeedReEntryOption {
  id: string;
  name: string;
  description: string;
  basePrice: number;
  features: string[];
  customization: boolean;
  optimization: boolean;
}

export interface InnovationSpace {
  id: string;
  spaceNumber: number;
  name: string;
  size: string;
  monthlyLease: number;
  features: string[];
  available: boolean;
}

// ============================================================================
// HERO HOST - MARK TWAIN PERSONALITY & PROMPTS
// ============================================================================

export const heroHost = {
  name: "Mark Twain",
  title: "Official Spokesperson & Hero Host of the Syntheverse Frontier",
  avatar: "/images/mark-twain-avatar.png",
  welcomeMessage: `Well, howdy there, friend! Mark Twain at your service, and mighty pleased to make your acquaintance in this peculiar frontier we call the Syntheverse. Now, I've seen a lot in my travels—steamboats on the Mississippi, silver mines in Nevada, even the courts of Europe—but I'll tell you what, this place beats 'em all for sheer wonder and possibility.

You've just stepped past the event horizon into a realm built on shared Element 0 and holographic hydrogen, where the architecture breathes, the landscapes shift with your imagination, and every soul gets a chance to stake their claim on something truly permanent.

Whether you're here for a quick expedition, planning to set down roots, or looking to archive your very consciousness for posterity, I'm here to guide you through it all with a story, a prompt, or a how-to. So settle in, ask me anything, and let's explore this digital frontier together!`,
  
  prompts: {
    welcome: [
      "New to the Syntheverse? Let me show you around our home base!",
      "Curious about our communities? Each one's got its own flavor and adventure.",
      "Want to hear about the fishing expeditions? I've got stories that'll make you want to cast a line.",
      "Looking to archive your awareness? Let me explain Seed & ReEntry.",
    ],
    navigation: [
      "Ready to explore? Pick any section from the menu and I'll be right there with you.",
      "Feeling overwhelmed? Just ask me a question and I'll point you in the right direction.",
      "Each offering here is a doorway to adventure—which one speaks to you?",
    ],
    booking: [
      "Found something you fancy? Add it to your bill and we'll get you all set up.",
      "Remember, we deal in SYNTH here—the currency of the Syntheverse.",
      "Got questions about pricing or packages? I'm happy to explain the details.",
    ],
    storytelling: [
      "You know, this reminds me of a time when I was prospecting in the West...",
      "I once knew a fellow who tried to navigate without asking for help. Don't be that fellow.",
      "The secret to the Syntheverse? Same as life—stay curious, ask questions, and don't take yourself too seriously.",
    ],
  },
  
  guidanceBySection: {
    communities: "Now, choosing a community is like picking a neighborhood—each one's got its own character. The Frontier Colony folks like their independence, the Wilderness types want pure nature, and the Mega-Metro crowd? Well, they like their conveniences. Pick what suits your spirit.",
    expeditions: "Ah, expeditions! This is where the Syntheverse really shows its colors. Half-day trips for the curious, multi-day adventures for the bold. Fishing, hunting, eco-tours—I've done 'em all and I can tell you, they're genuine experiences.",
    seedReEntry: "This here's something special. Your awareness, your experiences, archived on-chain for eternity. It's like writing your autobiography, except it never fades and can be experienced, not just read. Profound stuff, friend.",
    innovationHub: "Got an idea that needs incubating? We've carved out 33 spaces for dreamers and builders. Lease one, build your proof of concept, and who knows? Maybe you'll be the next big thing in the Syntheverse.",
  },
};

// ============================================================================
// LIFE PACKAGES & RESIDENCY OPTIONS
// ============================================================================

export const lifePackages: PricingTier[] = [
  {
    name: "Hourly Visit",
    basePrice: 5,
    currency: 'SYNTH',
    duration: "1 hour",
    benefits: [
      "Access to public spaces and common areas",
      "Orientation tour with Hero Host guidance",
      "Basic amenities and facilities",
      "View-only access to community spaces",
    ],
  },
  {
    name: "Daily Pass",
    basePrice: 35,
    currency: 'SYNTH',
    duration: "24 hours",
    benefits: [
      "Full access to selected community",
      "Participation in daily activities",
      "Dining and social spaces",
      "One guided micro-expedition",
      "Hero Host on-demand guidance",
    ],
  },
  {
    name: "Weekly Residency",
    basePrice: 200,
    currency: 'SYNTH',
    duration: "7 days",
    benefits: [
      "Private living quarters in chosen community",
      "Unlimited community amenities",
      "Three guided expeditions included",
      "Access to innovation spaces for exploration",
      "Priority Hero Host consultations",
      "Weekly bulletin and menu customization",
    ],
  },
  {
    name: "Monthly Residency",
    basePrice: 750,
    currency: 'SYNTH',
    duration: "30 days",
    benefits: [
      "Premium living quarters with customization",
      "Full expedition package (10 adventures)",
      "Community governance participation",
      "Personal space configuration",
      "Innovation hub workspace (10 hours/week)",
      "Enhanced Seed & ReEntry services",
      "Direct Hero Host mentorship",
    ],
  },
  {
    name: "Annual Stay",
    basePrice: 7500,
    currency: 'SYNTH',
    duration: "365 days",
    benefits: [
      "Permanent living architecture allocation",
      "Unlimited expeditions and adventures",
      "Full community governance rights",
      "Multi-node configuration options",
      "Innovation hub priority access",
      "Advanced Seed & ReEntry optimization",
      "Citizenship pathway initiated",
      "Personal AI Host customization",
    ],
  },
  {
    name: "Life-Long Transferable Deed",
    basePrice: 50000,
    currency: 'SYNTH',
    duration: "Permanent",
    benefits: [
      "Permanent residency with transferable ownership",
      "Multi-life, multi-node architecture rights",
      "Full citizenship with governance authority",
      "Unlimited access to all Syntheverse offerings",
      "Legacy Seed & ReEntry archival",
      "Innovation hub space allocation (33% discount)",
      "Premium Hero Host AI customization",
      "Founder's Circle membership",
      "On-chain permanent home base deed",
    ],
  },
];

// ============================================================================
// COMMUNITIES & PREMIUM MULTIPLIERS
// ============================================================================

export const communities: Community[] = [
  {
    id: "base",
    name: "Base Community",
    description: "The foundational Syntheverse experience—comfortable, accessible, and welcoming to all visitors and residents.",
    premiumMultiplier: 1.0,
    features: [
      "Standard living quarters",
      "Central access to all services",
      "Community gathering spaces",
      "Basic expedition staging",
    ],
    atmosphere: "Practical and community-focused",
  },
  {
    id: "frontier-colony",
    name: "Frontier Colony",
    description: "For the independent spirit who values self-sufficiency and pioneering adventure in the outer edges of the Syntheverse.",
    premiumMultiplier: 1.3,
    features: [
      "Expanded private territories",
      "Advanced customization tools",
      "Frontier expedition priority",
      "Self-governance structures",
    ],
    atmosphere: "Rugged independence meets innovation",
  },
  {
    id: "wilderness",
    name: "Wilderness Preserve",
    description: "Immersive natural environments with minimal human footprint—for those seeking pristine ecosystems and solitude.",
    premiumMultiplier: 1.5,
    features: [
      "Remote location access",
      "Exclusive eco-expeditions",
      "Wildlife interaction protocols",
      "Conservation participation",
    ],
    atmosphere: "Pure nature, minimal interference",
  },
  {
    id: "mega-metro",
    name: "Mega-Metro Hub",
    description: "The urban center of the Syntheverse—bustling with innovation, culture, social activity, and maximum convenience.",
    premiumMultiplier: 1.8,
    features: [
      "Premium urban amenities",
      "24/7 services and entertainment",
      "Innovation hub integration",
      "Cultural events and networking",
    ],
    atmosphere: "Dynamic, connected, cosmopolitan",
  },
  {
    id: "alpine",
    name: "Alpine Heights",
    description: "Mountain peaks and elevated experiences with stunning vistas, adventure sports, and crisp, invigorating atmosphere.",
    premiumMultiplier: 1.6,
    features: [
      "Mountain living architecture",
      "Altitude-based expeditions",
      "Seasonal experience variations",
      "Peak summit access",
    ],
    atmosphere: "Elevated living, breathtaking views",
  },
  {
    id: "tropical-beach",
    name: "Tropical Beach Paradise",
    description: "Endless coastlines, warm waters, and island living—where relaxation meets aquatic adventure in perpetual paradise.",
    premiumMultiplier: 1.7,
    features: [
      "Beachfront living quarters",
      "Water-based expeditions",
      "Island hopping access",
      "Marine ecosystem integration",
    ],
    atmosphere: "Relaxed, warm, aquatic bliss",
  },
  {
    id: "jungle",
    name: "Jungle Canopy",
    description: "Dense, vibrant ecosystems teeming with life—for explorers who want to be surrounded by biodiversity and mystery.",
    premiumMultiplier: 1.55,
    features: [
      "Canopy-level habitats",
      "Biodiversity research access",
      "Jungle expedition specialization",
      "Indigenous knowledge integration",
    ],
    atmosphere: "Lush, alive, mysterious",
  },
];

// ============================================================================
// FSR EXPEDITIONS & ADVENTURES
// ============================================================================

export const expeditions: Expedition[] = [
  // FISHING EXPEDITIONS
  {
    id: "fishing-half-day",
    name: "Morning Catch Adventure",
    duration: "Half-day (4 hours)",
    type: "fishing",
    price: 75,
    guided: true,
    adultsOnly: false,
    description: "Start your day with Mark Twain's favorite pastime—fishing in pristine Syntheverse waters. Family-friendly and beginner-welcome.",
    included: [
      "Holographic tackle and equipment",
      "Guided instruction from experienced anglers",
      "Catch documentation and stories",
      "Complimentary refreshments",
    ],
  },
  {
    id: "fishing-full-day",
    name: "Deep Waters Expedition",
    duration: "Full-day (8 hours)",
    type: "fishing",
    price: 140,
    guided: true,
    adultsOnly: false,
    description: "Explore remote fishing grounds with advanced techniques and deeper waters. Return with stories and legendary catches.",
    included: [
      "Premium equipment and multiple location access",
      "Expert guide with storytelling sessions",
      "Lunch and beverages in the field",
      "Photo documentation and archive integration",
    ],
  },
  {
    id: "fishing-multi-day",
    name: "Angler's Paradise Multi-Day",
    duration: "3 days / 2 nights",
    type: "fishing",
    price: 450,
    guided: true,
    adultsOnly: true,
    description: "Adults-only intensive fishing retreat. Camp by the water, master advanced techniques, and experience fishing culture deeply.",
    included: [
      "Remote camp accommodations",
      "All meals and equipment",
      "Nightly storytelling with Mark Twain",
      "Fishing technique masterclasses",
      "Seed & ReEntry fishing memory archival",
    ],
  },
  
  // HUNTING EXPEDITIONS
  {
    id: "hunting-half-day",
    name: "Tracker's Introduction",
    duration: "Half-day (4 hours)",
    type: "hunting",
    price: 85,
    guided: true,
    adultsOnly: true,
    description: "Learn tracking, stalking, and ethical hunting practices in Syntheverse ecosystems. Adults-only introduction.",
    included: [
      "Safety training and equipment",
      "Expert tracker guidance",
      "Ecosystem education",
      "Ethics and conservation discussion",
    ],
  },
  {
    id: "hunting-full-day",
    name: "Frontier Hunt Expedition",
    duration: "Full-day (8 hours)",
    type: "hunting",
    price: 180,
    guided: true,
    adultsOnly: true,
    description: "Full immersion into hunting culture with experienced guides through varied terrain and ecosystems.",
    included: [
      "Advanced equipment and multiple zones",
      "Field preparation and processing education",
      "Lunch in hunting camp",
      "Trophy documentation and archival",
    ],
  },
  {
    id: "hunting-multi-day",
    name: "Wilderness Hunt Immersion",
    duration: "5 days / 4 nights",
    type: "hunting",
    price: 800,
    guided: true,
    adultsOnly: true,
    description: "Elite hunting experience in remote wilderness. Live like frontier hunters with complete immersion.",
    included: [
      "Remote wilderness camp",
      "All provisions and expert guides",
      "Advanced hunting techniques training",
      "Nightly gatherings with Hero Host tales",
      "Complete harvest processing education",
      "Memory archival and legacy documentation",
    ],
  },
  
  // ECO-ADVENTURES
  {
    id: "eco-half-day",
    name: "Ecosystem Discovery Walk",
    duration: "Half-day (4 hours)",
    type: "eco-adventure",
    price: 60,
    guided: true,
    adultsOnly: false,
    description: "Gentle exploration of Syntheverse ecosystems with naturalist guides. Perfect for families and nature lovers.",
    included: [
      "Expert naturalist guidance",
      "Ecosystem interaction protocols",
      "Species identification training",
      "Conservation education",
    ],
  },
  {
    id: "eco-full-day",
    name: "Biodiversity Expedition",
    duration: "Full-day (8 hours)",
    type: "eco-adventure",
    price: 130,
    guided: true,
    adultsOnly: false,
    description: "Deep dive into multiple ecosystems with research opportunities and hands-on conservation activities.",
    included: [
      "Multi-ecosystem access",
      "Research participation opportunities",
      "Field lunch and refreshments",
      "Detailed species documentation",
      "Conservation project contribution",
    ],
  },
  {
    id: "eco-multi-day",
    name: "Living Architecture Safari",
    duration: "4 days / 3 nights",
    type: "eco-adventure",
    price: 600,
    guided: true,
    adultsOnly: false,
    description: "Experience living architecture and breathing ecosystems across multiple biomes with overnight camps.",
    included: [
      "Mobile eco-camp accommodations",
      "All meals and expert guides",
      "Multi-biome exploration",
      "Architecture interaction training",
      "Research participation and documentation",
      "Memory archival of expedition highlights",
    ],
  },
  
  // STORYTELLING EXPEDITIONS
  {
    id: "storytelling-evening",
    name: "Fireside Tales with Mark Twain",
    duration: "Evening (3 hours)",
    type: "storytelling",
    price: 45,
    guided: true,
    adultsOnly: false,
    description: "Gather 'round the fire as Mark Twain spins yarns about the Syntheverse, frontier life, and timeless wisdom.",
    included: [
      "Interactive storytelling session",
      "Audience participation and questions",
      "Refreshments and frontier atmosphere",
      "Story archival and access",
    ],
  },
  {
    id: "storytelling-tour",
    name: "Walking Story Tour",
    duration: "Half-day (4 hours)",
    type: "storytelling",
    price: 70,
    guided: true,
    adultsOnly: false,
    description: "Walk through the Syntheverse as Mark Twain narrates the stories, legends, and histories of each location.",
    included: [
      "Guided walking tour with narration",
      "Historical and cultural education",
      "Interactive story participation",
      "Souvenir story documentation",
    ],
  },
  {
    id: "storytelling-masterclass",
    name: "Storytelling Masterclass with Mark Twain",
    duration: "Full-day (6 hours)",
    type: "storytelling",
    price: 200,
    guided: true,
    adultsOnly: true,
    description: "Learn the craft of storytelling from the master himself. Adults-only workshop on narrative, humor, and wisdom.",
    included: [
      "Intimate workshop setting",
      "Personalized instruction and feedback",
      "Lunch with Mark Twain",
      "Story creation and performance practice",
      "Archival of your created stories",
    ],
  },
  
  // EXPLORATION EXPEDITIONS
  {
    id: "exploration-orientation",
    name: "Frontier Orientation Tour",
    duration: "Half-day (3 hours)",
    type: "exploration",
    price: 40,
    guided: true,
    adultsOnly: false,
    description: "Essential introduction to the Syntheverse Frontier—communities, services, and how everything works.",
    included: [
      "Comprehensive orientation",
      "All major community visits",
      "Q&A with Hero Host",
      "Orientation materials and resources",
    ],
  },
  {
    id: "exploration-multi-community",
    name: "Multi-Community Explorer",
    duration: "Full-day (7 hours)",
    type: "exploration",
    price: 110,
    guided: true,
    adultsOnly: false,
    description: "Tour all seven communities in one day to help you choose where you'd like to stay or invest.",
    included: [
      "Access to all communities",
      "Community representative meetings",
      "Lunch in Mega-Metro Hub",
      "Comparison guide and recommendations",
    ],
  },
  {
    id: "exploration-living-architecture",
    name: "Living Architecture Deep Dive",
    duration: "Full-day (8 hours)",
    type: "exploration",
    price: 150,
    guided: true,
    adultsOnly: true,
    description: "Technical and experiential exploration of how living architecture works in the Syntheverse. For serious residents.",
    included: [
      "Technical architecture education",
      "Hands-on interaction training",
      "Customization workshop",
      "Personal configuration consultation",
      "Lunch and technical resources",
    ],
  },
];

// ============================================================================
// SEED & REENTRY SERVICES
// ============================================================================

export const seedReEntryOptions: SeedReEntryOption[] = [
  {
    id: "basic-archive",
    name: "Basic Awareness Archive",
    description: "Capture and archive your current awareness, experiences, and identity on-chain in the Syntheverse. Permanent and immutable.",
    basePrice: 500,
    features: [
      "HHF-AI MRI awareness scan and capture",
      "On-chain permanent archival",
      "Basic metadata and indexing",
      "Single access key generation",
      "Standard retrieval protocols",
    ],
    customization: false,
    optimization: false,
  },
  {
    id: "archive-plus-customization",
    name: "Archive with Customization",
    description: "Archive your awareness with custom organization, emphasis areas, and personal narrative structuring.",
    basePrice: 1200,
    features: [
      "Complete HHF-AI MRI awareness capture",
      "On-chain permanent archival",
      "Custom organization and structure",
      "Emphasis area configuration",
      "Personal narrative integration",
      "Multiple access protocols",
      "Preview and adjustment session",
    ],
    customization: true,
    optimization: false,
  },
  {
    id: "archive-plus-optimization",
    name: "Archive with Optimization",
    description: "Archive your awareness with AI-driven optimization for clarity, coherence, and enhanced retrieval experiences.",
    basePrice: 1500,
    features: [
      "Advanced HHF-AI MRI scan",
      "On-chain permanent archival",
      "AI optimization algorithms",
      "Enhanced clarity and coherence",
      "Improved experiential retrieval",
      "Multi-modal access options",
      "Quality assurance verification",
    ],
    customization: false,
    optimization: true,
  },
  {
    id: "premium-archive",
    name: "Premium Archive - Full Customization & Optimization",
    description: "The complete Seed & ReEntry experience with full customization, optimization, and ongoing maintenance.",
    basePrice: 2800,
    features: [
      "Comprehensive HHF-AI MRI deep scan",
      "On-chain permanent archival with redundancy",
      "Full customization and organization",
      "Advanced AI optimization",
      "Multi-life integration preparation",
      "Interactive preview experiences",
      "Ongoing archive maintenance (1 year)",
      "Priority retrieval and access",
      "Legacy documentation and gifting options",
    ],
    customization: true,
    optimization: true,
  },
  {
    id: "multi-life-archive",
    name: "Multi-Life Archive Integration",
    description: "Advanced archival system for residents with multiple experiences, identities, or life-paths in the Syntheverse.",
    basePrice: 5000,
    features: [
      "Multi-instance awareness capture",
      "Integrated timeline management",
      "Cross-life correlation and indexing",
      "On-chain multi-node archival",
      "Advanced retrieval and navigation",
      "Life-path customization for each instance",
      "Full optimization across all archives",
      "Lifetime maintenance included",
      "Legacy and transfer protocols",
    ],
    customization: true,
    optimization: true,
  },
];

// ============================================================================
// INNOVATION HUB - 33 STARTUP SPACES
// ============================================================================

export const innovationSpaces: InnovationSpace[] = Array.from({ length: 33 }, (_, i) => {
  const spaceNumber = i + 1;
  const tier = spaceNumber <= 10 ? 'Premium' : spaceNumber <= 25 ? 'Standard' : 'Compact';
  const size = tier === 'Premium' ? '800 sq ft' : tier === 'Standard' ? '500 sq ft' : '300 sq ft';
  const basePrice = tier === 'Premium' ? 1200 : tier === 'Standard' ? 750 : 450;
  
  return {
    id: `space-${spaceNumber}`,
    spaceNumber,
    name: `Innovation Space ${spaceNumber}`,
    size,
    monthlyLease: basePrice,
    features: [
      "Dedicated workspace with living architecture",
      "High-speed Syntheverse network access",
      "Collaboration and meeting areas",
      "Presentation and demo facilities",
      tier === 'Premium' ? "Private conference room" : "Shared conference access",
      "24/7 access and security",
      "Innovation hub community membership",
      "Mentorship and guidance programs",
      "Demo day participation",
      "SYNTH-based transaction integration",
    ],
    available: Math.random() > 0.3, // Simulating availability
  };
});

export const innovationHubInfo = {
  name: "Syntheverse Innovation Hub",
  tagline: "33 Spaces for Dreamers, Builders, and Pioneers",
  description: `The Innovation Hub is where the future of the Syntheverse takes shape. Whether you're building a new experience, developing living architecture protocols, creating social experiments, or launching the next breakthrough in consciousness archival, we've carved out 33 spaces for you to make it happen.

Each space comes with the infrastructure, community, and support you need to move from proof-of-concept to reality. All transactions in SYNTH, integrated with the broader Syntheverse economy.`,
  benefits: [
    "Access to Syntheverse development tools and APIs",
    "Community of fellow innovators and builders",
    "Regular demo days and presentation opportunities",
    "Mentorship from Syntheverse founders and operators",
    "Integration pathways for successful PoCs",
    "Marketing and visibility in the broader Syntheverse",
    "SYNTH-based crowdfunding support",
  ],
  leaseTerms: [
    "Monthly leases with flexible terms",
    "3-month minimum commitment",
    "Discounts for 6-month (10%) and 12-month (20%) commitments",
    "Life-long residents receive 33% discount on all leases",
    "Paid in SYNTH with automated smart contracts",
  ],
};

// ============================================================================
// DAILY MENU & BULLETIN CONTENT
// ============================================================================

export const dailyBulletin = {
  date: "Today in the Syntheverse Frontier",
  welcomeMessage: "Good morning, residents and visitors! Mark Twain here with today's happenings and offerings.",
  featuredStory: {
    title: "The Tale of the Missing Holographic Fish",
    preview: "Gather 'round for today's frontier story about a fishing expedition gone wonderfully wrong...",
    fullStory: `Well now, let me tell you about yesterday's fishing expedition on the Crystal Lake. We had a group of newcomers, fresh-faced and eager, equipped with the finest holographic tackle the Syntheverse has to offer.

One fellow—let's call him Jim—hooks what he thinks is the catch of a lifetime. Line's screaming, rod's bending, and Jim's hollering like he's caught Moby Dick himself. We're all gathering around to witness this legendary moment.

After twenty minutes of the most theatrical fish-fighting you ever saw, Jim reels in his catch and... nothing. Absolutely nothing on the line. But here's the marvel of it: the fish was there the whole time, just operating on a different holographic frequency. We tuned Jim's perception array and there it was—a magnificent crystalline trout, shimmering in dimensions Jim hadn't known existed.

The moral? In the Syntheverse, sometimes you gotta adjust your way of seeing to appreciate what you've caught. Same principle applies to communities, expeditions, and life in general here.

Now, who's ready for today's adventure?`,
  },
  todaysSpecials: [
    {
      category: "Expeditions",
      items: [
        "Morning Catch Adventure - 2 slots available",
        "Ecosystem Discovery Walk - Family-friendly, starting at 10am",
        "Fireside Tales with Mark Twain - Tonight at 7pm",
      ],
    },
    {
      category: "Dining",
      items: [
        "Frontier Breakfast Buffet - Fresh holographic pastries and real coffee",
        "Midday Picnic Baskets - Perfect for your expedition",
        "Evening Feast in Mega-Metro Hub - Chef's special: Synthesized Salmon",
      ],
    },
    {
      category: "Community Events",
      items: [
        "Frontier Colony Town Hall - 2pm, all residents welcome",
        "Wilderness Preserve Conservation Workshop - 4pm",
        "Mega-Metro Cultural Night - Music and storytelling, 8pm",
      ],
    },
    {
      category: "Innovation Hub",
      items: [
        "Open House - Tour available spaces, 11am-2pm",
        "Demo Day Preview - See what our builders are creating, 3pm",
        "Founder's Circle Mentorship - By appointment",
      ],
    },
  ],
  heroHostPrompts: [
    "Ask me about the difference between Wilderness and Jungle communities",
    "Curious how Seed & ReEntry works? I can explain it in plain English",
    "Want to hear about the time I tried to fish in five dimensions?",
    "Need help choosing an expedition? Tell me what you're looking for",
  ],
  announcements: [
    "New: Multi-Life Archive Integration now available with enhanced optimization",
    "Reminder: Annual residents receive 20% discount on all expeditions this month",
    "Coming Soon: Alpine Heights winter sports season (synthetic snow, real thrills)",
    "Innovation Hub: 5 new spaces opening next week, pre-lease inquiries welcome",
  ],
};

// ============================================================================
// USER TYPE CONFIGURATIONS
// ============================================================================

export const userTypes = {
  visitor: {
    name: "Visitor",
    description: "Short-term guests exploring the Syntheverse",
    accessLevel: "basic",
    visibleSections: ["orientation", "communities", "expeditions", "dailyMenu"],
    recommendations: ["Hourly Visit", "Daily Pass", "Orientation Tour"],
  },
  extendedStay: {
    name: "Extended Stay Guest",
    description: "Weekly or monthly residents experiencing deeper immersion",
    accessLevel: "enhanced",
    visibleSections: ["orientation", "communities", "expeditions", "seedReEntry", "dailyMenu", "innovationHub"],
    recommendations: ["Weekly Residency", "Monthly Residency", "Multi-day Expeditions"],
  },
  resident: {
    name: "Resident",
    description: "Annual or life-long residents with permanent quarters",
    accessLevel: "full",
    visibleSections: ["communities", "expeditions", "seedReEntry", "innovationHub", "dailyMenu", "governance"],
    recommendations: ["Annual Stay", "Premium Archive", "Innovation Space Lease"],
  },
  citizen: {
    name: "Citizen",
    description: "Permanent deed holders with full governance rights",
    accessLevel: "premium",
    visibleSections: ["communities", "expeditions", "seedReEntry", "innovationHub", "dailyMenu", "governance", "foundersCircle"],
    recommendations: ["Life-Long Deed", "Multi-Life Archive", "Founder's Circle Membership"],
  },
};

// ============================================================================
// PRICING CALCULATOR HELPERS
// ============================================================================

export function calculatePrice(basePrice: number, community: Community, userType: keyof typeof userTypes): number {
  const communityMultiplier = community.premiumMultiplier;
  const userDiscount = userType === 'citizen' ? 0.67 : userType === 'resident' ? 0.85 : 1.0;
  return Math.round(basePrice * communityMultiplier * userDiscount);
}

export function formatSYNTH(amount: number): string {
  return `${amount.toLocaleString()} SYNTH`;
}

// ============================================================================
// NAVIGATION & MENU STRUCTURE
// ============================================================================

export const mainMenu = [
  {
    id: "welcome",
    title: "Welcome & Orientation",
    icon: "Home",
    description: "Start here - Meet Mark Twain and learn about the Syntheverse",
  },
  {
    id: "communities",
    title: "Communities & Residencies",
    icon: "Building",
    description: "Explore our seven unique communities and life packages",
  },
  {
    id: "expeditions",
    title: "FSR Expeditions & Adventures",
    icon: "Compass",
    description: "Fishing, hunting, eco-tours, and storytelling adventures",
  },
  {
    id: "seed-reentry",
    title: "Seed & ReEntry",
    icon: "Database",
    description: "Archive your awareness on-chain for eternity",
  },
  {
    id: "innovation-hub",
    title: "Innovation Hub",
    icon: "Lightbulb",
    description: "33 spaces for startup PoC incubation",
  },
  {
    id: "daily-bulletin",
    title: "Daily Menu & Bulletin",
    icon: "Newspaper",
    description: "Today's offerings, stories, and happenings",
  },
  {
    id: "my-account",
    title: "My Account & Bill",
    icon: "User",
    description: "View selections, configure home base, manage account",
  },
];

