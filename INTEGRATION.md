# Natural Systems Protocol Integration Guide

## 🔗 Integrating NSP with Other Frameworks

This guide shows how to integrate the Natural Systems Protocol with various frameworks and platforms beyond Next.js/React.

---

## 🎨 Framework Integrations

### React (Standalone)

```bash
npm install react react-dom framer-motion
```

```typescript
// App.tsx
import { NaturalSystemsProvider } from './components/NaturalSystemsProvider';

function App() {
  return (
    <NaturalSystemsProvider>
      <YourApp />
    </NaturalSystemsProvider>
  );
}
```

### Vue.js

```typescript
// plugins/naturalSystems.ts
import { initializeNaturalSystems } from '@/protocols/naturalSystems';

export default {
  install(app: App) {
    const engine = initializeNaturalSystems();
    engine.start();
    
    app.config.globalProperties.$nsp = engine;
    app.provide('nsp', engine);
  },
};

// Component usage
<script setup>
import { inject, ref, onMounted } from 'vue';

const nsp = inject('nsp');
const worldContext = ref(null);

onMounted(() => {
  nsp.subscribe('world-update', (context) => {
    worldContext.value = context;
  });
});
</script>
```

### Svelte

```typescript
// stores/naturalSystems.ts
import { writable } from 'svelte/store';
import { initializeNaturalSystems } from '../protocols/naturalSystems';

const engine = initializeNaturalSystems();
engine.start();

export const worldContext = writable(null);

engine.subscribe('world-update', (context) => {
  worldContext.set(context);
});

export { engine };

// Component usage
<script>
  import { worldContext } from './stores/naturalSystems';
</script>

<div>
  World Energy: {$worldContext?.totalEnergy}
</div>
```

### Angular

```typescript
// services/natural-systems.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { initializeNaturalSystems, WorldContext } from '../protocols/naturalSystems';

@Injectable({ providedIn: 'root' })
export class NaturalSystemsService {
  private engine = initializeNaturalSystems();
  public worldContext$ = new BehaviorSubject<WorldContext | null>(null);

  constructor() {
    this.engine.start();
    this.engine.subscribe('world-update', (context: WorldContext) => {
      this.worldContext$.next(context);
    });
  }
}

// Component usage
export class AppComponent {
  constructor(public nsp: NaturalSystemsService) {}
}
```

---

## 🎮 Game Engine Integrations

### Three.js (3D Visualization)

```typescript
import * as THREE from 'three';
import { getNaturalSystemsEngine } from './protocols/naturalSystems';

const engine = getNaturalSystemsEngine();
const scene = new THREE.Scene();

// Create 3D representation of entities
const entities = new Map<string, THREE.Mesh>();

engine.subscribe('entity-update:hero-host-mark-twain', (entity) => {
  const mesh = entities.get(entity.id);
  if (mesh) {
    mesh.position.set(...entity.state.position);
    mesh.scale.setScalar(entity.state.scale);
    
    // Mood affects material
    if (entity.state.mood === 'thriving') {
      mesh.material.emissive.setHex(0xffd700);
    }
  }
});

// Sync day/night with scene lighting
engine.subscribe('cycle-effect:lighting:intensity', (intensity) => {
  directionalLight.intensity = intensity;
});
```

### Babylon.js

```typescript
import * as BABYLON from 'babylonjs';
import { getNaturalSystemsEngine } from './protocols/naturalSystems';

const engine = getNaturalSystemsEngine();
const scene = new BABYLON.Scene(babylonEngine);

engine.subscribe('world-update', (context) => {
  // Update sky color based on day phase
  const skyMaterial = scene.getMaterialByName('skyMaterial') as BABYLON.StandardMaterial;
  if (skyMaterial) {
    const hue = context.dayPhase * 360;
    skyMaterial.diffuseColor = BABYLON.Color3.FromHSV(hue, 0.7, 0.9);
  }
});
```

### Unity (via WebGL/JavaScript Bridge)

```csharp
// Unity C# Script
using UnityEngine;
using System.Runtime.InteropServices;

public class NaturalSystemsBridge : MonoBehaviour {
    [DllImport("__Internal")]
    private static extern string GetWorldContext();
    
    void Update() {
        string contextJson = GetWorldContext();
        WorldContext context = JsonUtility.FromJson<WorldContext>(contextJson);
        
        // Use context in Unity
        RenderSettings.ambientIntensity = context.totalEnergy;
    }
}
```

```javascript
// JavaScript bridge
mergeInto(LibraryManager.library, {
  GetWorldContext: function() {
    const engine = window.nspEngine;
    if (engine) {
      const context = engine.getContext();
      return allocateUTF8(JSON.stringify(context));
    }
    return null;
  }
});
```

---

## 🌐 Web Platform Integrations

### WebGL/Canvas

```typescript
const canvas = document.getElementById('world-canvas') as HTMLCanvasElement;
const ctx = canvas.getContext('2d');
const engine = getNaturalSystemsEngine();

function render() {
  const context = engine.getContext();
  
  // Draw sky based on day phase
  const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
  if (context.dayPhase < 0.5) {
    gradient.addColorStop(0, '#89f7fe');
    gradient.addColorStop(1, '#66a6ff');
  } else {
    gradient.addColorStop(0, '#fa709a');
    gradient.addColorStop(1, '#fee140');
  }
  
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  requestAnimationFrame(render);
}

render();
```

### Web Components

```typescript
class NaturalWorldElement extends HTMLElement {
  private engine: NaturalSystemsEngine;
  
  connectedCallback() {
    this.engine = initializeNaturalSystems();
    this.engine.start();
    
    this.engine.subscribe('world-update', (context) => {
      this.updateDisplay(context);
    });
  }
  
  disconnectedCallback() {
    this.engine.stop();
  }
  
  updateDisplay(context: WorldContext) {
    this.innerHTML = `
      <div class="world-stats">
        <div>Energy: ${context.totalEnergy.toFixed(2)}</div>
        <div>Visitors: ${context.visitorCount}</div>
        <div>Mood: ${context.dominantMood}</div>
      </div>
    `;
  }
}

customElements.define('natural-world', NaturalWorldElement);
```

---

## 📡 Backend Integrations

### Node.js Express API

```typescript
import express from 'express';
import { initializeNaturalSystems } from './protocols/naturalSystems';

const app = express();
const engine = initializeNaturalSystems();
engine.start();

// World state endpoint
app.get('/api/world/status', (req, res) => {
  const context = engine.getContext();
  res.json(context);
});

// Trigger event endpoint
app.post('/api/world/interact/:entityId', (req, res) => {
  engine.interactWithEntity(req.params.entityId);
  res.json({ success: true });
});

// WebSocket for real-time updates
import { Server } from 'socket.io';
const io = new Server(server);

engine.subscribe('world-update', (context) => {
  io.emit('world-update', context);
});
```

### GraphQL API

```typescript
import { gql, ApolloServer } from 'apollo-server';
import { getNaturalSystemsEngine } from './protocols/naturalSystems';

const typeDefs = gql`
  type WorldContext {
    time: Float!
    dayPhase: Float!
    seasonPhase: Float!
    visitorCount: Int!
    totalEnergy: Float!
    dominantMood: String!
  }
  
  type Entity {
    id: String!
    type: String!
    mood: String!
    energy: Float!
  }
  
  type Query {
    worldContext: WorldContext!
    entity(id: String!): Entity
  }
  
  type Mutation {
    interactWithEntity(id: String!): Entity!
  }
`;

const resolvers = {
  Query: {
    worldContext: () => getNaturalSystemsEngine()?.getContext(),
    entity: (_, { id }) => getNaturalSystemsEngine()?.getEntity(id),
  },
  Mutation: {
    interactWithEntity: (_, { id }) => {
      const engine = getNaturalSystemsEngine();
      engine?.interactWithEntity(id);
      return engine?.getEntity(id);
    },
  },
};
```

---

## ⛓️ Blockchain Integrations

### Base (Ethereum L2)

```typescript
import { ethers } from 'ethers';
import { getNaturalSystemsEngine } from './protocols/naturalSystems';

const provider = new ethers.JsonRpcProvider(process.env.NEXT_PUBLIC_BASE_RPC_URL);
const engine = getNaturalSystemsEngine();

// Archive world state on-chain
async function archiveWorldState(wallet: ethers.Wallet) {
  const context = engine.getContext();
  
  const contract = new ethers.Contract(
    process.env.SYNTH_ARCHIVE_CONTRACT,
    archiveABI,
    wallet
  );
  
  const tx = await contract.archiveState(
    JSON.stringify(context),
    { value: ethers.parseEther('0.01') }
  );
  
  await tx.wait();
  console.log('World state archived on-chain:', tx.hash);
}

// Listen for on-chain events and trigger world events
contract.on('CitizenshipGranted', (address, deedId) => {
  engine.emit('autonomous-event:announcement', {
    type: 'announcement',
    content: {
      title: 'New Citizen!',
      message: `Welcome our newest permanent resident!`,
    },
    duration: 10000,
  });
});
```

### IPFS (Decentralized Storage)

```typescript
import { create } from 'ipfs-http-client';

const ipfs = create({ url: 'https://ipfs.infura.io:5001' });

async function archiveEntityToIPFS(entityId: string) {
  const engine = getNaturalSystemsEngine();
  const entity = engine.getEntity(entityId);
  
  const { cid } = await ipfs.add(JSON.stringify(entity));
  console.log('Entity archived to IPFS:', cid.toString());
  
  return cid.toString();
}
```

---

## 🎯 CMS Integrations

### Sanity.io

```typescript
import { createClient } from '@sanity/client';

const sanity = createClient({
  projectId: 'your-project-id',
  dataset: 'production',
  apiVersion: '2023-01-01',
});

// Fetch dynamic content for Daily Bulletin
async function updateDailyBulletin() {
  const bulletin = await sanity.fetch(`
    *[_type == "dailyBulletin" && date == $today][0] {
      welcomeMessage,
      featuredStory,
      todaysSpecials
    }
  `, { today: new Date().toISOString().split('T')[0] });
  
  return bulletin;
}
```

---

## 📊 Analytics Integrations

### Custom Analytics

```typescript
import { getNaturalSystemsEngine } from './protocols/naturalSystems';

class NSPAnalytics {
  private metrics: Map<string, number[]> = new Map();
  
  constructor() {
    const engine = getNaturalSystemsEngine();
    
    engine.subscribe('world-update', (context) => {
      this.recordMetric('energy', context.totalEnergy);
      this.recordMetric('visitors', context.visitorCount);
    });
  }
  
  recordMetric(name: string, value: number) {
    if (!this.metrics.has(name)) {
      this.metrics.set(name, []);
    }
    this.metrics.get(name)!.push(value);
  }
  
  getAverageEnergy(): number {
    const energyData = this.metrics.get('energy') || [];
    return energyData.reduce((a, b) => a + b, 0) / energyData.length;
  }
}
```

---

## 🔌 Plugin System

### Creating NSP Plugins

```typescript
// Plugin interface
interface NSPPlugin {
  name: string;
  version: string;
  onLoad: (engine: NaturalSystemsEngine) => void;
  onUnload?: () => void;
}

// Example plugin: Weather System
const weatherPlugin: NSPPlugin = {
  name: 'weather-system',
  version: '1.0.0',
  
  onLoad: (engine) => {
    // Add new cycle
    engine.addCycle({
      name: 'weather',
      duration: 300000, // 5 minutes
      effects: [
        {
          target: 'atmosphere',
          property: 'condition',
          modulation: (phase) => {
            if (phase < 0.3) return 'sunny';
            if (phase < 0.6) return 'cloudy';
            if (phase < 0.8) return 'rainy';
            return 'clear';
          },
        },
      ],
    });
    
    // Add weather events
    engine.addEvent({
      name: 'storm-approaching',
      trigger: 'random',
      condition: () => Math.random() < 0.05,
      action: () => ({
        type: 'announcement',
        content: {
          title: 'Storm Warning',
          message: 'A frontier storm is approaching from the west!',
        },
        duration: 15000,
      }),
      cooldown: 600000,
      lastTriggered: 0,
    });
  },
};

// Use plugin
engine.registerPlugin(weatherPlugin);
```

---

## 🌟 Advanced Integration Patterns

### Multi-World Synchronization

```typescript
// Sync multiple NSP instances across network
import { io } from 'socket.io-client';

const localEngine = initializeNaturalSystems();
const socket = io('wss://syntheverse-sync.com');

// Broadcast local events
localEngine.subscribe('entity-interaction:*', (data) => {
  socket.emit('world-event', {
    worldId: 'marktwainverse',
    event: data,
  });
});

// Receive events from other worlds
socket.on('world-event', (data) => {
  if (data.worldId !== 'marktwainverse') {
    // Visualize cross-world activity
    showCrossWorldNotification(data);
  }
});
```

### Recursive World Nesting

```typescript
// Parent world contains child worlds
const syntherverse = initializeNaturalSystems();
const markTwainVerse = initializeNaturalSystems();
const otherWorld = initializeNaturalSystems();

// Child worlds influence parent
markTwainVerse.subscribe('world-update', (context) => {
  // Aggregate energy to parent
  syntherverse.addExternalEnergy('marktwainverse', context.totalEnergy);
});

// Parent events cascade to children
syntherverse.subscribe('autonomous-event:*', (event) => {
  if (event.type === 'metaverse-announcement') {
    markTwainVerse.triggerEvent(event);
    otherWorld.triggerEvent(event);
  }
});
```

---

## 📚 Resources

- **NSP Specification:** `NATURAL_SYSTEMS_PROTOCOL_SPEC.md`
- **Example Implementations:** `/examples/` directory
- **Community Plugins:** https://github.com/FractiAI/nsp-plugins
- **Support:** https://discord.gg/syntheverse

---

**Happy Integrating!** 🚀

The Natural Systems Protocol is designed to work anywhere digital worlds need to breathe.

