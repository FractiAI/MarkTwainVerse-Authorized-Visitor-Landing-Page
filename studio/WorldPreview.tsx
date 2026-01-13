"use client";

import { motion } from 'framer-motion';
import { useEffect, useRef } from 'react';

// ============================================================================
// WORLD PREVIEW - Live NSP visualization
// ============================================================================

interface WorldPreviewProps {
  worldConfig: any;
}

export function WorldPreview({ worldConfig }: WorldPreviewProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (!canvasRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Simple visualization of the world
    let frame = 0;

    const animate = () => {
      frame++;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw background based on day phase
      const dayPhase = (frame % 360) / 360;
      const skyColor = getSkyColor(dayPhase);
      ctx.fillStyle = skyColor;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Draw entities
      worldConfig.entities?.forEach((entity: any, index: number) => {
        const x = 100 + index * 150;
        const y = canvas.height / 2;
        const breathing = Math.sin(frame * 0.1) * 5;

        // Entity representation
        ctx.fillStyle = getEntityColor(entity.type);
        ctx.beginPath();
        ctx.arc(x, y + breathing, 30 * entity.energy, 0, Math.PI * 2);
        ctx.fill();

        // Entity label
        ctx.fillStyle = 'white';
        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(entity.id.substring(0, 15), x, y + 60);
      });

      requestAnimationFrame(animate);
    };

    animate();
  }, [worldConfig]);

  return (
    <canvas
      ref={canvasRef}
      width={800}
      height={600}
      className="w-full h-full rounded-lg"
    />
  );
}

function getSkyColor(phase: number): string {
  if (phase < 0.25) return '#ff6b6b'; // Dawn
  if (phase < 0.75) return '#89f7fe'; // Day
  if (phase < 0.9) return '#fa709a'; // Dusk
  return '#0f2027'; // Night
}

function getEntityColor(type: string): string {
  switch (type) {
    case 'character': return '#d4af37';
    case 'building': return '#c9a66b';
    case 'landscape': return '#10b981';
    case 'system': return '#00d4ff';
    default: return '#ffffff';
  }
}

export function EntityDesigner() {
  return <div>Entity Designer Component</div>;
}

export function CycleConfigurator() {
  return <div>Cycle Configurator Component</div>;
}

export function EventCreator() {
  return <div>Event Creator Component</div>;
}


