import type { Metadata } from 'next';
import './globals.css';
import { NaturalSystemsProvider } from '@/components/NaturalSystemsProvider';

export const metadata: Metadata = {
  title: 'MarkTwainVerse | Syntheverse Frontier Landing Page',
  description: 'A living, breathing digital frontier built on the Natural Systems Protocol. Explore communities, expeditions, consciousness archival, and innovation spaces with Mark Twain as your guide.',
  keywords: [
    'Syntheverse',
    'MarkTwainVerse',
    'Natural Systems Protocol',
    'Living World',
    'Digital Frontier',
    'Consciousness Archival',
    'SYNTH Token',
    'Web3',
    'Base Blockchain',
  ],
  authors: [{ name: 'FractiAI', url: 'https://github.com/FractiAI' }],
  openGraph: {
    title: 'MarkTwainVerse | Living Digital Frontier',
    description: 'A self-operating world where visitors explore communities, expeditions, and permanent citizenship. Built on the Natural Systems Protocol.',
    type: 'website',
    url: 'https://marktwainverse.vercel.app',
    siteName: 'MarkTwainVerse',
    images: [
      {
        url: '/og-image.png',
        width: 1200,
        height: 630,
        alt: 'MarkTwainVerse - Living Digital Frontier',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'MarkTwainVerse | Living Digital Frontier',
    description: 'A self-operating world built on the Natural Systems Protocol',
    images: ['/og-image.png'],
  },
  viewport: {
    width: 'device-width',
    initialScale: 1,
    maximumScale: 5,
  },
  themeColor: '#d4af37',
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
        <meta name="theme-color" content="#d4af37" />
      </head>
      <body>
        <NaturalSystemsProvider>
          {children}
        </NaturalSystemsProvider>
      </body>
    </html>
  );
}


