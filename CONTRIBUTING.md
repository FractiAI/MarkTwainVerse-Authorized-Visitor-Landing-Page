# Contributing to MarkTwainVerse & Natural Systems Protocol

Thank you for your interest in contributing! MarkTwainVerse and the Natural Systems Protocol are open-source projects that welcome contributions from the community.

---

## 🌟 Ways to Contribute

### 1. Code Contributions
- **Protocol Enhancements** - Improve NSP core engine
- **New Features** - Add sections, expeditions, or communities
- **Bug Fixes** - Resolve issues and improve stability
- **Performance** - Optimize animations and rendering
- **Accessibility** - Improve keyboard navigation and screen readers

### 2. Content Contributions
- **Mark Twain Stories** - Write new frontier tales
- **Expedition Designs** - Create new adventure types
- **Community Concepts** - Design new frontier communities
- **Daily Bulletins** - Draft engaging daily content

### 3. Documentation
- **Improve Guides** - Enhance existing documentation
- **Write Tutorials** - Create integration examples
- **Translate** - Help internationalize the project
- **API Documentation** - Document NSP interfaces

### 4. Testing & Quality Assurance
- **Bug Reports** - Report issues with detailed reproduction steps
- **Cross-Browser Testing** - Test on different browsers and devices
- **Performance Testing** - Profile and identify bottlenecks
- **Accessibility Auditing** - Test with assistive technologies

### 5. Design
- **UI/UX Improvements** - Enhance user interface design
- **Animation Design** - Create new living animations
- **Asset Creation** - Design icons, images, textures
- **Branding** - Improve frontier aesthetic

---

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/MarkTwainVerse-Authorized-Visitor-Landing-Page.git
cd MarkTwainVerse-Authorized-Visitor-Landing-Page

# Add upstream remote
git remote add upstream https://github.com/FractiAI/MarkTwainVerse-Authorized-Visitor-Landing-Page.git
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Create a Branch

```bash
# Use descriptive branch names
git checkout -b feature/new-expedition-type
git checkout -b fix/animation-stutter
git checkout -b docs/integration-guide
```

### 4. Make Your Changes

Follow our coding standards (see below).

### 5. Test Your Changes

```bash
# Run type checking
npm run type-check

# Run development server
npm run dev

# Build for production
npm run build
```

### 6. Commit with Conventional Commits

```bash
git add .
git commit -m "feat(expeditions): add deep-sea fishing adventure"
```

**Commit Prefixes:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style/formatting (no logic changes)
- `refactor:` - Code restructuring
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 7. Push & Create Pull Request

```bash
git push origin feature/new-expedition-type
```

Then open a Pull Request on GitHub with:
- Clear description of changes
- Link to related issues
- Screenshots/videos if UI changes
- Test results

---

## 📋 Coding Standards

### TypeScript

```typescript
// ✅ Good
interface Expedition {
  id: string;
  name: string;
  type: 'fishing' | 'hunting' | 'eco-adventure';
  price: number;
}

function calculatePrice(basePrice: number, multiplier: number): number {
  return Math.round(basePrice * multiplier);
}

// ❌ Bad
function calc(a, b) {  // No types
  return a * b;
}
```

### Naming Conventions

- **Variables/Functions:** `camelCase`
- **Components:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Files:** Match component name or descriptive `camelCase`

### File Organization

```
components/
  ├── CommunitiesSection.tsx      # One component per file
  ├── ExpeditionsSection.tsx
  └── shared/
      └── Card.tsx                # Reusable components in shared/
```

### Component Structure

```typescript
// 1. Imports
import { motion } from 'framer-motion';
import { useState } from 'react';

// 2. Types/Interfaces
interface Props {
  title: string;
  onSelect: (id: string) => void;
}

// 3. Component
export default function MyComponent({ title, onSelect }: Props) {
  // 4. State
  const [selected, setSelected] = useState<string | null>(null);
  
  // 5. Effects
  useEffect(() => {
    // ...
  }, []);
  
  // 6. Handlers
  const handleClick = () => {
    // ...
  };
  
  // 7. Render
  return (
    <div>
      {/* JSX */}
    </div>
  );
}
```

### CSS/Styling

- Use Tailwind utility classes when possible
- Custom animations in `globals.css`
- Follow frontier aesthetic (browns, golds, SYNTH accents)
- Ensure responsive design (`md:`, `lg:` breakpoints)

### Natural Systems Protocol

When extending NSP:

```typescript
// Document your additions
interface CustomEntity extends LivingEntity {
  customProperty: string;  // Describe what this does
}

// Follow existing patterns
const myEntity: LivingEntity = {
  id: 'my-entity',
  type: 'building',
  state: { /* ... */ },
  behaviors: [
    {
      name: 'descriptive-behavior-name',
      trigger: 'cycle',
      probability: 1.0,
      action: (entity, context) => {
        // Clear, documented logic
      },
    },
  ],
  connections: [],
  energy: 0.8,
};
```

---

## 🧪 Testing Requirements

### Before Submitting PR

- [ ] Code type-checks (`npm run type-check`)
- [ ] No linting errors (`npm run lint`)
- [ ] Builds successfully (`npm run build`)
- [ ] Tested in development mode
- [ ] Cross-browser tested (Chrome, Firefox, Safari)
- [ ] Mobile responsiveness checked
- [ ] No console errors or warnings
- [ ] Animations run at 60fps
- [ ] NSP metrics remain stable

### NSP-Specific Testing

If modifying the Natural Systems Protocol:

```typescript
// Test cycle progression
const engine = initializeNaturalSystems();
engine.start();

setTimeout(() => {
  const phase = engine.getCyclePhase('dayNight');
  console.assert(phase > 0, 'Day/night cycle should progress');
}, 1000);

// Test entity behaviors
engine.interactWithEntity('hero-host-mark-twain');
const entity = engine.getEntity('hero-host-mark-twain');
console.assert(entity.energy > 0.8, 'Interaction should increase energy');
```

---

## 📝 Pull Request Guidelines

### PR Title Format

```
feat(expeditions): add underwater cave exploration
fix(nsp): resolve memory leak in cycle updates
docs(readme): improve installation instructions
```

### PR Description Template

```markdown
## Description
Brief summary of changes

## Related Issues
Fixes #123

## Changes Made
- Added X feature
- Modified Y component
- Improved Z performance

## Testing
- [ ] Tested locally
- [ ] Cross-browser verified
- [ ] Mobile responsive
- [ ] NSP stable

## Screenshots/Videos
(if applicable)

## Breaking Changes
(if any)
```

### Review Process

1. **Automated Checks** - GitHub Actions run type-check and lint
2. **Code Review** - Maintainers review code quality
3. **Testing** - Changes tested in staging environment
4. **Approval** - At least one maintainer approval required
5. **Merge** - Squash and merge to main

---

## 🎯 Priority Areas

We especially welcome contributions in:

### High Priority
- 🔥 Performance optimization for 100+ concurrent visitors
- 🔥 Mobile UX improvements
- 🔥 Accessibility enhancements (WCAG 2.1 AA)
- 🔥 Cross-world NSP synchronization

### Medium Priority
- 📊 Analytics and monitoring dashboard
- 🎨 Additional community types
- 🧪 Automated testing suite
- 🌐 Internationalization (i18n)

### Low Priority (but still valuable!)
- ✨ Easter eggs and hidden features
- 📖 Additional Mark Twain stories
- 🎭 New autonomous event types
- 🖼️ Asset improvements

---

## 🤝 Community Guidelines

### Code of Conduct

- **Be Respectful** - Treat everyone with kindness and professionalism
- **Be Constructive** - Provide helpful, actionable feedback
- **Be Inclusive** - Welcome newcomers and diverse perspectives
- **Be Patient** - Remember that maintainers are volunteers
- **Be Collaborative** - Work together toward shared goals

### Communication

- **GitHub Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions
- **Discord** - Real-time discussion and support
- **Email** - Security issues (security@fractiai.com)

### Attribution

Contributors will be:
- Listed in `CONTRIBUTORS.md`
- Credited in release notes
- Eligible for special recognition in the Syntheverse

---

## 🏆 Recognition

Significant contributors may receive:
- **Frontier Pioneer Badge** - Your name in the Hall of Fame
- **Early Access** - Preview upcoming features
- **SYNTH Tokens** - Community rewards for major contributions
- **Citizenship** - Special status in the Syntheverse

---

## 📚 Resources

- **NSP Specification:** `NATURAL_SYSTEMS_PROTOCOL_SPEC.md`
- **Deployment Guide:** `DEPLOYMENT.md`
- **Integration Guide:** `INTEGRATION.md`
- **Project README:** `README.md`

---

## ❓ Questions?

- **General Questions:** Open a GitHub Discussion
- **Bug Reports:** Create an Issue with template
- **Security Concerns:** Email security@fractiai.com
- **Feature Ideas:** Start a Discussion first, then create Issue

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make MarkTwainVerse and the Natural Systems Protocol better for everyone. We're building the future of living digital worlds together.

**Welcome to the frontier, friend!** 🤠

— The FractiAI Team

