// ============================================================================
// NATURAL SYSTEMS PROVIDER
// React Context Provider for MarkTwainVerse Living World
// ============================================================================

"use client";

import React, { createContext, useContext, useEffect, useState, useCallback } from 'react';
import {
  NaturalSystemsEngine,
  initializeNaturalSystems,
  getNaturalSystemsEngine,
  WorldContext,
  LivingEntity,
  EventResult,
} from '@/protocols/naturalSystems';

interface NaturalSystemsContextType {
  engine: NaturalSystemsEngine | null;
  worldContext: WorldContext | null;
  entities: Map<string, LivingEntity>;
  recentEvents: EventResult[];
  isAwake: boolean;
  interactWithEntity: (entityId: string) => void;
  addVisitor: () => void;
  removeVisitor: () => void;
}

const NaturalSystemsContext = createContext<NaturalSystemsContextType>({
  engine: null,
  worldContext: null,
  entities: new Map(),
  recentEvents: [],
  isAwake: false,
  interactWithEntity: () => {},
  addVisitor: () => {},
  removeVisitor: () => {},
});

export function useNaturalSystems() {
  const context = useContext(NaturalSystemsContext);
  if (!context) {
    throw new Error('useNaturalSystems must be used within NaturalSystemsProvider');
  }
  return context;
}

interface NaturalSystemsProviderProps {
  children: React.ReactNode;
}

export function NaturalSystemsProvider({ children }: NaturalSystemsProviderProps) {
  const [engine, setEngine] = useState<NaturalSystemsEngine | null>(null);
  const [worldContext, setWorldContext] = useState<WorldContext | null>(null);
  const [entities, setEntities] = useState<Map<string, LivingEntity>>(new Map());
  const [recentEvents, setRecentEvents] = useState<EventResult[]>([]);
  const [isAwake, setIsAwake] = useState(false);

  // Initialize the Natural Systems Engine
  useEffect(() => {
    console.log("🌱 Initializing MarkTwainVerse Natural Systems...");
    const engineInstance = initializeNaturalSystems();
    setEngine(engineInstance);
    setIsAwake(true);

    // Subscribe to world updates
    engineInstance.subscribe('world-update', (context: WorldContext) => {
      setWorldContext(context);
    });

    // Subscribe to entity updates
    engineInstance.subscribe('entity-update:hero-host-mark-twain', (entity: LivingEntity) => {
      setEntities(prev => new Map(prev).set(entity.id, entity));
    });

    // Subscribe to autonomous events
    const eventTypes = ['story', 'announcement', 'special-offer', 'community-event', 'expedition-departure'];
    eventTypes.forEach(type => {
      engineInstance.subscribe(`autonomous-event:${type}`, (event: EventResult) => {
        setRecentEvents(prev => [...prev.slice(-9), event]); // Keep last 10 events
        console.log(`🎭 Autonomous Event (${type}):`, event.content);
      });
    });

    // Add this visitor
    engineInstance.addVisitor();

    // Cleanup
    return () => {
      engineInstance.removeVisitor();
    };
  }, []);

  const interactWithEntity = useCallback((entityId: string) => {
    if (engine) {
      engine.interactWithEntity(entityId);
    }
  }, [engine]);

  const addVisitor = useCallback(() => {
    if (engine) {
      engine.addVisitor();
    }
  }, [engine]);

  const removeVisitor = useCallback(() => {
    if (engine) {
      engine.removeVisitor();
    }
  }, [engine]);

  const value: NaturalSystemsContextType = {
    engine,
    worldContext,
    entities,
    recentEvents,
    isAwake,
    interactWithEntity,
    addVisitor,
    removeVisitor,
  };

  return (
    <NaturalSystemsContext.Provider value={value}>
      {children}
    </NaturalSystemsContext.Provider>
  );
}

// ============================================================================
// NATURAL SYSTEMS HOOKS - For Component Access
// ============================================================================

export function useDayNightCycle(): number {
  const { engine } = useNaturalSystems();
  const [phase, setPhase] = useState(0);

  useEffect(() => {
    if (!engine) return;

    const interval = setInterval(() => {
      setPhase(engine.getCyclePhase('dayNight'));
    }, 100);

    return () => clearInterval(interval);
  }, [engine]);

  return phase;
}

export function useSeasonalCycle(): number {
  const { engine } = useNaturalSystems();
  const [phase, setPhase] = useState(0);

  useEffect(() => {
    if (!engine) return;

    const interval = setInterval(() => {
      setPhase(engine.getCyclePhase('seasons'));
    }, 1000);

    return () => clearInterval(interval);
  }, [engine]);

  return phase;
}

export function useMarkTwainState(): LivingEntity | null {
  const { entities } = useNaturalSystems();
  return entities.get('hero-host-mark-twain') || null;
}

export function useWorldEnergy(): number {
  const { worldContext } = useNaturalSystems();
  return worldContext?.totalEnergy || 0;
}

export function useAutonomousEvents(maxCount: number = 5): EventResult[] {
  const { recentEvents } = useNaturalSystems();
  return recentEvents.slice(-maxCount);
}

