/**
 * ============================================================================
 * UX WALKTHROUGH & PRESENTATION VIDEO GENERATOR
 * ============================================================================
 * Lead UX Engineer & Playwright Specialist Implementation
 *
 * Produces a fluid, high-definition (1280x720) user experience showcase video
 * demonstrating layout architecture, micro-interactions, smooth scrolling,
 * and realistic humanized interaction cadence.
 * ============================================================================
 */

import { chromium, type Browser, type BrowserContext, type Page, type Locator } from 'playwright';
import * as fs from 'fs';
import * as path from 'path';

// --- PRESENTATION CONFIGURATION ---
const CONFIG = {
  // Support both 5173 (standard Vite) and custom APP_URL/port 3000
  baseUrl: process.env.APP_URL || 'http://localhost:5173',
  outputDir: path.resolve(__dirname, '../ux-walkthrough-videos'),
  viewport: { width: 1280, height: 720 }, // 16:9 HD Standard
  delays: {
    micro: 350,         // Micro-interactions, hover snaps, toggle triggers
    glance: 750,        // Human visual scan on newly revealed UI components
    comprehend: 1300,   // Cognitive pause for reading dashboards & results
    scrollPause: 850,   // Settling pause after smooth scrolling
  },
  typingSpeed: { min: 45, max: 90 }, // Realistic human per-keystroke speed in ms
};

// ============================================================================
// UX INTERACTION PRIMITIVES (HUMANIZING AGENT)
// ============================================================================

/**
 * Injects a natural human cognitive pause so video viewers can visually
 * digest layout transitions, data visualizations, and state changes.
 */
async function humanPause(page: Page, durationMs: number = CONFIG.delays.glance): Promise<void> {
  await page.waitForTimeout(durationMs);
}

/**
 * Demonstrates hover states, tooltips, and micro-interactions by moving the
 * cursor over an element and dwelling before committing the click action.
 */
async function glanceAndClick(locator: Locator, hoverDurationMs: number = 650): Promise<void> {
  await locator.scrollIntoViewIfNeeded();
  await locator.hover();
  await locator.page().waitForTimeout(hoverDurationMs);
  await locator.click();
}

/**
 * Types sequentially with realistic variable cadence instead of instant string pasting.
 */
async function humanType(locator: Locator, text: string): Promise<void> {
  await locator.scrollIntoViewIfNeeded();
  await locator.click();
  await locator.page().waitForTimeout(CONFIG.delays.micro);

  for (const char of text) {
    const delay = Math.floor(
      Math.random() * (CONFIG.typingSpeed.max - CONFIG.typingSpeed.min) + CONFIG.typingSpeed.min
    );
    await locator.pressSequentially(char, { delay });
  }
}

/**
 * Emulates human-paced continuous smooth scrolling so viewers can perceive
 * content flow and page structure without disorienting layout snaps.
 */
async function smoothScroll(page: Page, distancePx: number, durationSteps: number = 3): Promise<void> {
  const stepDistance = distancePx / durationSteps;
  for (let i = 0; i < durationSteps; i++) {
    await page.evaluate((step) => {
      window.scrollBy({ top: step, behavior: 'smooth' });
    }, stepDistance);
    await page.waitForTimeout(300);
  }
  await page.waitForTimeout(CONFIG.delays.scrollPause);
}

// ============================================================================
// MAIN USER EXPERIENCE JOURNEY
// ============================================================================

async function runUXWalkthrough(): Promise<void> {
  if (!fs.existsSync(CONFIG.outputDir)) {
    fs.mkdirSync(CONFIG.outputDir, { recursive: true });
  }

  console.log('🎥 Launching visual recording engine at', CONFIG.baseUrl, '...');

  const browser: Browser = await chromium.launch({
    headless: true, // Clean headless recording environment
  });

  // 1. VISUAL RECORDING & CONTEXT LOCK
  // Setting viewport matching recordVideo.size avoids letterboxing or fuzzy scaling
  const context: BrowserContext = await browser.newContext({
    viewport: CONFIG.viewport,
    recordVideo: {
      dir: CONFIG.outputDir,
      size: CONFIG.viewport,
    },
    deviceScaleFactor: 1.5, // Retina-quality crisp font and SVG rendering
  });

  const page: Page = await context.newPage();

  try {
    // ------------------------------------------------------------------------
    // PHASE 1: LANDING & BRAND DISCOVERY
    // ------------------------------------------------------------------------
    console.log('👉 Phase 1: Landing Experience & Visual Scan');
    await page.goto(CONFIG.baseUrl, { waitUntil: 'domcontentloaded' });
    await humanPause(page, CONFIG.delays.comprehend);

    // Visual scan of Brand and Hero headline
    const heroHeadline = page.locator('h1').first();
    if (await heroHeadline.isVisible()) {
      await heroHeadline.hover();
      await humanPause(page, CONFIG.delays.micro);
    }

    // Smooth scroll down to highlight value-proposition feature cards
    await smoothScroll(page, 450);
    const featureCards = page.locator('.card');
    const cardsCount = await featureCards.count();
    for (let i = 0; i < Math.min(cardsCount, 3); i++) {
      await featureCards.nth(i).hover();
      await humanPause(page, CONFIG.delays.micro);
    }

    // Smooth scroll back up to hero CTA
    await smoothScroll(page, -450);
    const startCta = page.getByRole('link', { name: /start your analysis|enter app/i }).first();
    if (await startCta.isVisible()) {
      await glanceAndClick(startCta, 700);
      await humanPause(page, CONFIG.delays.comprehend);
    }

    // ------------------------------------------------------------------------
    // PHASE 2: AUTHENTICATION FLOW
    // ------------------------------------------------------------------------
    console.log('👉 Phase 2: Form Interaction & Natural Keystrokes');
    // If redirected to /auth or landing on login
    if (page.url().includes('/auth')) {
      const emailField = page.getByPlaceholder(/email/i).or(page.locator('input[type="email"]')).first();
      if (await emailField.isVisible()) {
        await humanType(emailField, 'guest@example.com');
        await humanPause(page, CONFIG.delays.micro);

        const passwordField = page.getByPlaceholder(/password/i).or(page.locator('input[type="password"]')).first();
        await humanType(passwordField, 'password123');
        await humanPause(page, CONFIG.delays.micro);

        const loginBtn = page.getByRole('button', { name: /sign in|login|continue/i }).first();
        await glanceAndClick(loginBtn, 700);
        await humanPause(page, CONFIG.delays.comprehend);
      }
    }

    // ------------------------------------------------------------------------
    // PHASE 3: DASHBOARD METRICS & READINESS OVERVIEW
    // ------------------------------------------------------------------------
    console.log('👉 Phase 3: Dashboard Exploration & Chart Interaction');
    await page.waitForURL('**/dashboard', { timeout: 8000 }).catch(() => {});
    await humanPause(page, CONFIG.delays.comprehend);

    // Scan KPI metric cards & header
    const dashboardHeader = page.locator('h1').first();
    if (await dashboardHeader.isVisible()) {
      await dashboardHeader.hover();
      await humanPause(page, CONFIG.delays.micro);
    }

    // Hover over any metric cards / readiness displays
    const statCards = page.locator('.card');
    const statCount = await statCards.count();
    for (let i = 0; i < Math.min(statCount, 3); i++) {
      await statCards.nth(i).hover();
      await humanPause(page, CONFIG.delays.micro);
    }

    await smoothScroll(page, 400);
    await humanPause(page, CONFIG.delays.comprehend);
    await smoothScroll(page, -400);

    // ------------------------------------------------------------------------
    // PHASE 4: SKILLS INVENTORY & DYNAMIC ENTRY
    // ------------------------------------------------------------------------
    console.log('👉 Phase 4: My Skills Management');
    const skillsNav = page.getByRole('link', { name: /my skills|skills/i }).first();
    if (await skillsNav.isVisible()) {
      await glanceAndClick(skillsNav, 600);
      await humanPause(page, CONFIG.delays.comprehend);

      // Add a modern technical skill via natural typing
      const skillNameInput = page.getByPlaceholder(/skill name|e\.g\./i).or(page.locator('input[name="name"]')).first();
      if (await skillNameInput.isVisible()) {
        await humanType(skillNameInput, 'TypeScript');
        await humanPause(page, CONFIG.delays.micro);

        // Select proficiency if available
        const proficiencySelect = page.locator('select').nth(1);
        if (await proficiencySelect.isVisible()) {
          await proficiencySelect.selectOption({ label: 'Advanced' }).catch(() => {});
          await humanPause(page, CONFIG.delays.micro);
        }

        // Click Add Skill button
        const addSkillBtn = page.getByRole('button', { name: /add skill/i }).first();
        if (await addSkillBtn.isVisible()) {
          await glanceAndClick(addSkillBtn, 600);
          await humanPause(page, CONFIG.delays.comprehend);
        }
      }

      // Hover over existing skill tags/cards
      const skillPills = page.locator('.badge, .skill-pill, .card .flex');
      const pillCount = await skillPills.count();
      for (let i = 0; i < Math.min(pillCount, 4); i++) {
        await skillPills.nth(i).hover();
        await humanPause(page, CONFIG.delays.micro);
      }

      await smoothScroll(page, 300);
      await smoothScroll(page, -300);
    }

    // ------------------------------------------------------------------------
    // PHASE 5: AI SKILL GAP ANALYSIS & TAILORED ROADMAP
    // ------------------------------------------------------------------------
    console.log('👉 Phase 5: AI Skill Gap Analysis & Roadmap');
    const analysisNav = page.getByRole('link', { name: /skill gap|analysis/i }).first();
    if (await analysisNav.isVisible()) {
      await glanceAndClick(analysisNav, 600);
      await humanPause(page, CONFIG.delays.comprehend);

      // Inspect target role selector
      const roleSelect = page.locator('select').first();
      if (await roleSelect.isVisible()) {
        await roleSelect.hover();
        await humanPause(page, CONFIG.delays.micro);
      }

      // Trigger ML Analysis
      const analyzeBtn = page.getByRole('button', { name: /run analysis|analyze/i }).first();
      if (await analyzeBtn.isVisible()) {
        await glanceAndClick(analyzeBtn, 800);
        // Allow time for calculation and smooth render
        await humanPause(page, 2000);
      }

      // Smooth scroll through the generated readiness breakdown and roadmap
      await smoothScroll(page, 500);
      await humanPause(page, CONFIG.delays.comprehend);

      const roadmapSteps = page.locator('.markdown, .roadmap-step, .card');
      if (await roadmapSteps.first().isVisible()) {
        await roadmapSteps.first().hover();
        await humanPause(page, CONFIG.delays.glance);
      }

      await smoothScroll(page, 500);
      await humanPause(page, CONFIG.delays.comprehend);
      await smoothScroll(page, -1000);
    }

    // ------------------------------------------------------------------------
    // PHASE 6: INTELLIGENT JOB RECOMMENDATIONS
    // ------------------------------------------------------------------------
    console.log('👉 Phase 6: Job Recommendations Showcase');
    const jobsNav = page.getByRole('link', { name: /jobs/i }).first();
    if (await jobsNav.isVisible()) {
      await glanceAndClick(jobsNav, 600);
      await humanPause(page, CONFIG.delays.comprehend);

      // Explore Tab toggles (e.g. "For You" vs "Trending Jobs")
      const trendingTab = page.getByRole('button', { name: /trending/i }).first();
      if (await trendingTab.isVisible()) {
        await glanceAndClick(trendingTab, 600);
        await humanPause(page, CONFIG.delays.comprehend);
      }

      const forYouTab = page.getByRole('button', { name: /for you/i }).first();
      if (await forYouTab.isVisible()) {
        await glanceAndClick(forYouTab, 600);
        await humanPause(page, CONFIG.delays.glance);
      }

      // Hover over job cards to showcase match scores and salary tags
      const jobCards = page.locator('.card');
      const jobCount = await jobCards.count();
      for (let i = 0; i < Math.min(jobCount, 3); i++) {
        await jobCards.nth(i).hover();
        await humanPause(page, CONFIG.delays.micro);
      }

      await smoothScroll(page, 500);
      await humanPause(page, CONFIG.delays.comprehend);
      await smoothScroll(page, -500);
    }

    // ------------------------------------------------------------------------
    // PHASE 7: PROFILE & FINALIZING GLANCE
    // ------------------------------------------------------------------------
    console.log('👉 Phase 7: Profile Management & Aesthetic Wrap-up');
    const profileNav = page.getByRole('link', { name: /profile/i }).first();
    if (await profileNav.isVisible()) {
      await glanceAndClick(profileNav, 600);
      await humanPause(page, CONFIG.delays.comprehend);

      await smoothScroll(page, 350);
      await humanPause(page, CONFIG.delays.glance);
      await smoothScroll(page, -350);
    }

    // Return to Dashboard for a clean visual anchor conclusion
    if (await dashboardHeader.isVisible() || await page.getByRole('link', { name: /dashboard/i }).isVisible()) {
      const returnDashboard = page.getByRole('link', { name: /dashboard/i }).first();
      await glanceAndClick(returnDashboard, 600);
      await humanPause(page, CONFIG.delays.comprehend);
    }

  } catch (error) {
    console.warn('⚠️ Note during visual walk:', error);
  } finally {
    // ------------------------------------------------------------------------
    // PHASE 8: TEARDOWN & HIGH-DEFINITION VIDEO FLUSH
    // ------------------------------------------------------------------------
    console.log('💾 Finalizing video stream and flushing to disk...');
    
    // Explicit context and page close guarantees container finalization
    const videoRef = page.video();
    await context.close();
    await browser.close();

    if (videoRef) {
      const rawPath = await videoRef.path();
      const finalVideoPath = path.join(CONFIG.outputDir, 'SkillGap_UX_Walkthrough_HD.webm');
      
      // Rename to semantic presentation artifact
      if (fs.existsSync(rawPath)) {
        fs.copyFileSync(rawPath, finalVideoPath);
      }

      console.log(`\n🎉 High-Definition UX Walkthrough Video generated successfully!`);
      console.log(`📁 Saved to: ${finalVideoPath}`);
    }
  }
}

// Execute the walkthrough
runUXWalkthrough().catch((err) => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
