# MarkTwainVerse Production Deployment Guide

## 🚀 Deployment Options

### 1. Vercel (Recommended for Next.js)

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod
```

**Environment Variables in Vercel:**
1. Go to Project Settings → Environment Variables
2. Add the following:
   - `NEXT_PUBLIC_GROQ_API_KEY` (optional, for enhanced AI)
   - `NEXT_PUBLIC_BASE_RPC_URL` (for blockchain interaction)

###  2. Netlify

```bash
# Build the project
npm run build

# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=.next
```

### 3. Self-Hosted (Node.js)

```bash
# Build for production
npm run build

# Start production server
npm start

# Or use PM2 for process management
npm install -g pm2
pm2 start npm --name "marktwainverse" -- start
```

### 4. Docker Deployment

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

```bash
# Build Docker image
docker build -t marktwainverse .

# Run container
docker run -p 3000:3000 -d marktwainverse
```

---

## 🔧 Environment Configuration

Create a `.env.local` file for local development:

```env
# Optional: AI Enhancement
NEXT_PUBLIC_GROQ_API_KEY=your_groq_api_key_here

# Base Blockchain Configuration
NEXT_PUBLIC_BASE_RPC_URL=https://mainnet.base.org
NEXT_PUBLIC_SYNTH_TOKEN_ADDRESS=0x...

# Natural Systems Protocol Configuration
NSP_TIME_SCALE=60
NSP_START_DAY_PHASE=0.3
NSP_START_SEASON_PHASE=0.25

# Analytics (optional)
NEXT_PUBLIC_GA_TRACKING_ID=G-XXXXXXXXXX
```

For production, set these in your hosting platform's environment variables.

---

## ⚙️ Build Configuration

### Next.js Configuration

The `next.config.js` is already configured for:
- Static image optimization
- React strict mode
- Production optimizations

### Performance Optimizations

1. **Enable Caching:**
```javascript
// next.config.js
module.exports = {
  // ... existing config
  headers: async () => [
    {
      source: '/:path*',
      headers: [
        {
          key: 'Cache-Control',
          value: 'public, max-age=3600, must-revalidate',
        },
      ],
    },
  ],
};
```

2. **Enable Compression:**
```bash
npm install compression
```

3. **Optimize Images:**
- Store static images in `/public/images/`
- Use Next.js `<Image />` component
- Serve WebP format when possible

---

## 🌐 Domain Configuration

### Custom Domain Setup

1. **Vercel:**
   - Project Settings → Domains → Add Domain
   - Update DNS records as instructed

2. **Netlify:**
   - Site Settings → Domain Management → Add Custom Domain
   - Configure DNS with provided nameservers

3. **Cloudflare (Recommended for Additional Features):**
   - Add site to Cloudflare
   - Point DNS to your hosting provider
   - Enable CDN and security features

---

## 🔒 Security Checklist

- [ ] Environment variables stored securely (not in code)
- [ ] HTTPS enabled (automatic on Vercel/Netlify)
- [ ] CSP headers configured for XSS protection
- [ ] Rate limiting implemented for API endpoints
- [ ] CORS configured appropriately
- [ ] Dependencies regularly updated (`npm audit`)

---

## 📊 Monitoring & Analytics

### 1. Vercel Analytics (Built-in)
Automatically enabled for Vercel deployments.

### 2. Google Analytics
```typescript
// Add to app/layout.tsx
<Script
  src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA_TRACKING_ID}`}
  strategy="afterInteractive"
/>
```

### 3. Natural Systems Protocol Monitoring
```typescript
// Custom monitoring hook
const { worldContext } = useNaturalSystems();

useEffect(() => {
  // Log world metrics
  console.log('World Energy:', worldContext?.totalEnergy);
  console.log('Visitor Count:', worldContext?.visitorCount);
  console.log('Dominant Mood:', worldContext?.dominantMood);
}, [worldContext]);
```

---

## 🧪 Pre-Deployment Testing

### 1. Run All Checks
```bash
# Type checking
npm run type-check

# Linting
npm run lint

# Build test
npm run build

# Run production build locally
npm start
```

### 2. Test Natural Systems Protocol
- [ ] Breathing animations working at 60fps
- [ ] Day/night cycle progressing smoothly
- [ ] Mark Twain entity responding to interactions
- [ ] Autonomous events triggering appropriately
- [ ] Energy levels updating correctly

### 3. Test User Flows
- [ ] Landing page loads and animates
- [ ] All sections accessible from main menu
- [ ] Communities section shows pricing correctly
- [ ] Expeditions filterable and selectable
- [ ] Seed & ReEntry options display properly
- [ ] Innovation Hub space grid renders
- [ ] Daily Bulletin loads with dynamic content
- [ ] Cart opens/closes smoothly

### 4. Cross-Browser Testing
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers (iOS Safari, Chrome Mobile)

### 5. Performance Testing
- [ ] Lighthouse score > 90
- [ ] First Contentful Paint < 2s
- [ ] Time to Interactive < 3s
- [ ] No console errors
- [ ] Memory usage stable over time

---

## 📱 Mobile Optimization

Already implemented in the CSS:
- Responsive grid layouts
- Touch-friendly button sizes
- Optimized font scaling with `clamp()`
- Mobile-first media queries

Test on actual devices:
- iOS (iPhone 12+, iPad)
- Android (various screen sizes)

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Type check
        run: npm run type-check
        
      - name: Lint
        run: npm run lint
        
      - name: Build
        run: npm run build
        
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
          vercel-args: '--prod'
```

---

## 🌍 Multi-Region Deployment

For global reach, deploy to multiple regions:

### Vercel Edge Network
Automatically handles global CDN distribution.

### Cloudflare Workers (Advanced)
For edge computing and ultra-low latency:
```bash
# Install Wrangler
npm install -g wrangler

# Deploy edge function
wrangler publish
```

---

## 💾 Database & State Management

### Current: Client-Side State
- Natural Systems Protocol engine runs in browser
- World state maintained in memory
- Cart/user preferences in localStorage

### Future: Persistent State
Consider adding:
- **Supabase** - PostgreSQL for user accounts
- **Redis** - Real-time world state synchronization
- **IPFS** - Decentralized archival storage
- **Base Blockchain** - On-chain state for critical data

---

## 📈 Scaling Considerations

### Current Capacity
- Handles 100-1000 concurrent visitors per instance
- Natural Systems Protocol optimized for client-side
- Stateless architecture scales horizontally

### Scaling Strategies

1. **Horizontal Scaling:**
   - Deploy multiple instances behind load balancer
   - Use CDN for static assets

2. **Optimize NSP Engine:**
   ```typescript
   // Reduce cycle check frequency for large visitor counts
   if (visitorCount > 100) {
     cycleCheckInterval = 200; // 5fps instead of 60fps
   }
   ```

3. **Progressive Enhancement:**
   - Reduce animation complexity on mobile
   - Lazy load sections below fold
   - Implement virtual scrolling for large lists

---

## 🔧 Troubleshooting

### Common Issues

1. **"World not awakening"**
   - Check browser console for errors
   - Verify Natural Systems Protocol initialized
   - Check for blocking scripts (ad blockers)

2. **Slow performance**
   - Monitor frame rate in DevTools
   - Reduce entity count if < 30fps
   - Check for memory leaks in long sessions

3. **Animations stuttering**
   - Disable `prefers-reduced-motion` check temporarily
   - Verify GPU acceleration enabled
   - Check for CPU throttling

4. **Environment variables not loading**
   - Ensure variables prefixed with `NEXT_PUBLIC_`
   - Restart dev server after changes
   - Check deployment platform configuration

---

## 📞 Support & Maintenance

### Regular Maintenance Tasks
- [ ] Update dependencies monthly (`npm update`)
- [ ] Security audit quarterly (`npm audit`)
- [ ] Performance testing after major updates
- [ ] Content updates (Daily Bulletin, Expeditions)
- [ ] Monitor error rates and user feedback

### Contact
- **Issues:** GitHub Issues
- **Security:** security@fractiai.com
- **General:** info@fractiai.com

---

## 🎉 Post-Deployment Checklist

- [ ] Production URL live and accessible
- [ ] Custom domain configured and SSL active
- [ ] Environment variables set correctly
- [ ] Analytics tracking functional
- [ ] All sections rendering properly
- [ ] Natural Systems Protocol operational
- [ ] Mobile responsiveness verified
- [ ] Cross-browser compatibility confirmed
- [ ] Performance metrics acceptable
- [ ] Error monitoring in place
- [ ] Backup/rollback strategy documented
- [ ] Team notified of deployment
- [ ] Documentation updated

---

## 🌟 Success Metrics

Track these KPIs post-launch:
- **Visitor Engagement:** Time on site, pages per session
- **NSP Performance:** Average frame rate, energy levels
- **Conversion:** Cart additions, checkout completions
- **Technical:** Page load time, error rates
- **Content:** Daily Bulletin opens, expedition bookings

---

**MarkTwainVerse is ready for the frontier!** 🤠

Deploy with confidence knowing you're launching a living, breathing world built on the Natural Systems Protocol.

