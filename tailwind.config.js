/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        frontier: {
          dark: '#1a1410',
          brown: '#3d2817',
          tan: '#c9a66b',
          gold: '#d4af37',
          cream: '#f5e6d3',
        },
        synth: {
          primary: '#00d4ff',
          secondary: '#7b2cbf',
          accent: '#ff6b35',
        },
      },
      fontFamily: {
        serif: ['Georgia', 'serif'],
        western: ['Courier New', 'monospace'],
      },
      backgroundImage: {
        'frontier-texture': "url('/textures/wood-grain.png')",
        'starfield': "url('/textures/stars.png')",
      },
    },
  },
  plugins: [],
}



