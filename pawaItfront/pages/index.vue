<template>
  <div class="landing-page">
    <!-- Animated background grid overlay (fixed) -->
    <div class="bg-grid" aria-hidden="true"></div>

    <!-- Decorative floating orbs (fixed) -->
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>
    <div class="orb orb-3" aria-hidden="true"></div>

    <!-- ============================= HERO ============================= -->
    <section class="hero">
      <div class="hero-bg" aria-hidden="true"></div>

      <v-container class="hero-inner">
        <v-row justify="center" align="center" class="text-center">
          <v-col cols="12" md="10" lg="8">
            <v-fade-transition appear>
              <div>
                <!-- Eyebrow badge -->
                <div class="eyebrow mb-6">
                  <v-icon size="16" class="mr-2">mdi-star-four-points</v-icon>
                  <span>AI-POWERED TRAVEL INTELLIGENCE</span>
                </div>

                <h1 class="hero-title mb-6">
                  <span class="hero-title-line">Travel Documentation</span>
                  <span class="hero-title-line hero-title-gradient">
                    Assistant
                  </span>
                </h1>

                <p class="hero-subtitle mb-10">
                  Get AI-powered insights on visa requirements and travel
                  documentation for any destination — accurate, fast, and always
                  up to date.
                </p>

                <div
                  class="d-flex flex-column flex-sm-row justify-center ga-4 hero-actions"
                >
                  <v-btn
                    size="x-large"
                    rounded="pill"
                    class="btn-primary-hero"
                    @click="navigateTo('/register')"
                  >
                    <v-icon left size="20">mdi-account-plus</v-icon>
                    Get Started Free
                  </v-btn>
                  <v-btn
                    size="x-large"
                    rounded="pill"
                    variant="outlined"
                    class="btn-ghost-hero"
                    @click="navigateTo('/login')"
                  >
                    <v-icon left size="20">mdi-login</v-icon>
                    Sign In
                  </v-btn>
                </div>

                <!-- Trust indicators -->
                <div class="trust-row mt-12">
                  <div class="trust-item">
                    <v-icon size="18" color="#a5b4fc"
                      >mdi-check-decagram</v-icon
                    >
                    <span>No credit card</span>
                  </div>
                  <div class="trust-divider"></div>
                  <div class="trust-item">
                    <v-icon size="18" color="#a5b4fc"
                      >mdi-lightning-bolt</v-icon
                    >
                    <span>Instant results</span>
                  </div>
                  <div class="trust-divider"></div>
                  <div class="trust-item">
                    <v-icon size="18" color="#a5b4fc">mdi-earth</v-icon>
                    <span>195+ countries</span>
                  </div>
                </div>
              </div>
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-container>

      <!-- Scroll indicator -->
      <div class="scroll-indicator" aria-hidden="true">
        <v-icon size="22">mdi-chevron-down</v-icon>
      </div>
    </section>

    <!-- ============================= FEATURES ============================= -->
    <section class="features">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="9" lg="7" class="text-center mb-14">
            <div class="pill-badge mb-5">
              <v-icon size="14" class="mr-2">mdi-lightning-bolt</v-icon>
              WHY CHOOSE US
            </div>
            <h2 class="section-title mb-4">
              Everything you need to
              <span class="gradient-text">travel with confidence</span>
            </h2>
            <p class="section-subtitle">
              Powered by advanced AI and built for modern travelers who demand
              accuracy and speed.
            </p>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col
            cols="12"
            md="4"
            v-for="(feature, index) in features"
            :key="feature.title"
            class="d-flex"
          >
            <div
              class="feature-card"
              :style="{ animationDelay: `${index * 0.12}s` }"
            >
              <div class="feature-icon-wrap" :class="`icon-${feature.tone}`">
                <div class="feature-icon-glow"></div>
                <v-icon size="30" color="white">{{ feature.icon }}</v-icon>
              </div>
              <h3 class="feature-title">{{ feature.title }}</h3>
              <p class="feature-description">{{ feature.description }}</p>
              <div class="feature-corner" aria-hidden="true"></div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- ============================= STATS STRIP ============================= -->
    <section class="stats-strip">
      <v-container>
        <v-row justify="center" class="text-center">
          <v-col cols="6" sm="3" v-for="stat in stats" :key="stat.label">
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- ============================= CTA ============================= -->
    <section class="cta">
      <div class="cta-glow" aria-hidden="true"></div>
      <v-container class="cta-inner">
        <v-row justify="center">
          <v-col cols="12" md="9" lg="7" class="text-center">
            <div class="cta-badge mb-6">
              <v-icon size="14" class="mr-2">mdi-rocket-launch</v-icon>
              GET STARTED TODAY
            </div>
            <h2 class="cta-title mb-5">
              Ready to plan your
              <span class="cta-highlight">next trip?</span>
            </h2>
            <p class="cta-subtitle mb-10">
              Join thousands of travelers who trust our AI assistant for
              stress-free documentation and visa guidance.
            </p>
            <v-btn
              size="x-large"
              rounded="pill"
              class="btn-cta"
              @click="navigateTo('/register')"
            >
              Start Planning Now
              <v-icon right size="20">mdi-arrow-right</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false,
});

const features = [
  {
    icon: "mdi-robot-happy",
    title: "AI-Powered",
    description:
      "Advanced Claude AI provides accurate and up-to-date travel documentation requirements.",
    tone: "indigo",
  },
  {
    icon: "mdi-clock-fast",
    title: "Real-time Updates",
    description:
      "Get the latest visa requirements, travel advisories, and documentation changes.",
    tone: "violet",
  },
  {
    icon: "mdi-shield-star",
    title: "Reliable Information",
    description:
      "Comprehensive travel guidance with official source recommendations you can trust.",
    tone: "fuchsia",
  },
];

const stats = [
  { value: "195+", label: "Countries Covered" },
  { value: "50K+", label: "Happy Travelers" },
  { value: "99.9%", label: "Uptime" },
  { value: "<2s", label: "Avg. Response" },
];
</script>

<style scoped>
/* ===================== FONT & GLOBAL ===================== */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap");

.landing-page {
  position: relative;
  min-height: 100vh;
  font-family: "Plus Jakarta Sans", sans-serif !important;
  background: #05060f;
  color: #e2e8f0;
  overflow-x: hidden;
}

/* Apply font to all Vuetify components */
:deep(.v-application) {
  font-family: "Plus Jakarta Sans", sans-serif !important;
}

/* ===================== FIXED BACKGROUND LAYERS ===================== */
.bg-grid {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image: linear-gradient(
      rgba(148, 163, 184, 0.06) 1px,
      transparent 1px
    ),
    linear-gradient(90deg, rgba(148, 163, 184, 0.06) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: radial-gradient(
    ellipse 80% 60% at 50% 30%,
    #000 30%,
    transparent 100%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 80% 60% at 50% 30%,
    #000 30%,
    transparent 100%
  );
}

/* Floating gradient orbs */
.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(90px);
  opacity: 0.55;
  pointer-events: none;
  z-index: 0;
  animation: float 18s ease-in-out infinite;
}
.orb-1 {
  width: 520px;
  height: 520px;
  background: radial-gradient(circle, #6366f1 0%, transparent 70%);
  top: -120px;
  left: -120px;
  animation-delay: 0s;
}
.orb-2 {
  width: 460px;
  height: 460px;
  background: radial-gradient(circle, #a855f7 0%, transparent 70%);
  top: 35%;
  right: -140px;
  animation-delay: -6s;
}
.orb-3 {
  width: 420px;
  height: 420px;
  background: radial-gradient(circle, #ec4899 0%, transparent 70%);
  bottom: -140px;
  left: 30%;
  opacity: 0.35;
  animation-delay: -12s;
}

@keyframes float {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(40px, -30px) scale(1.08);
  }
  66% {
    transform: translate(-30px, 30px) scale(0.95);
  }
}

/* ===================== HERO ===================== */
.hero {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 120px 0 100px;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(
      ellipse 60% 50% at 50% 0%,
      rgba(99, 102, 241, 0.18) 0%,
      transparent 70%
    ),
    radial-gradient(
      ellipse 50% 40% at 80% 60%,
      rgba(168, 85, 247, 0.12) 0%,
      transparent 70%
    );
  pointer-events: none;
}

.hero-inner {
  position: relative;
  z-index: 3;
}

/* Eyebrow badge */
.eyebrow {
  display: inline-flex;
  align-items: center;
  padding: 8px 18px;
  border-radius: 999px;
  background: rgba(99, 102, 241, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.3);
  color: #c7d2fe;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  backdrop-filter: blur(12px);
  animation: pulseBorder 3s ease-in-out infinite;
}

@keyframes pulseBorder {
  0%,
  100% {
    border-color: rgba(139, 92, 246, 0.3);
    box-shadow: 0 0 0 0 rgba(139, 92, 246, 0.2);
  }
  50% {
    border-color: rgba(139, 92, 246, 0.6);
    box-shadow: 0 0 24px 0 rgba(139, 92, 246, 0.25);
  }
}

/* Hero title */
.hero-title {
  font-size: clamp(2.75rem, 7vw, 5.5rem);
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -0.035em;
}

.hero-title-line {
  display: block;
  color: #f8fafc;
}

.hero-title-gradient {
  background: linear-gradient(
    120deg,
    #a5b4fc 0%,
    #c4b5fd 30%,
    #f0abfc 60%,
    #fbcfe8 100%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  background-size: 200% auto;
  animation: shimmer 6s linear infinite;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
  padding-right: 0.1em;
}

@keyframes shimmer {
  0% {
    background-position: 0% center;
  }
  100% {
    background-position: 200% center;
  }
}

.hero-subtitle {
  font-size: clamp(1.05rem, 1.6vw, 1.3rem);
  line-height: 1.65;
  color: rgba(203, 213, 225, 0.75);
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
  font-weight: 400;
}

/* Hero buttons */
.hero-actions {
  margin-bottom: 8px;
}

.btn-primary-hero {
  background: linear-gradient(
    120deg,
    #6366f1 0%,
    #8b5cf6 50%,
    #a855f7 100%
  ) !important;
  background-size: 200% auto !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em;
  padding: 0 32px !important;
  text-transform: none !important;
  box-shadow: 0 10px 32px -8px rgba(139, 92, 246, 0.65),
    inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}

.btn-primary-hero:hover {
  background-position: right center !important;
  transform: translateY(-3px);
  box-shadow: 0 18px 44px -8px rgba(139, 92, 246, 0.85),
    inset 0 1px 0 rgba(255, 255, 255, 0.25) !important;
}

.btn-ghost-hero {
  border: 1px solid rgba(203, 213, 225, 0.25) !important;
  color: #e2e8f0 !important;
  font-weight: 600 !important;
  letter-spacing: 0.01em;
  padding: 0 32px !important;
  text-transform: none !important;
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.03) !important;
  transition: all 0.3s ease !important;
}

.btn-ghost-hero:hover {
  background: rgba(255, 255, 255, 0.08) !important;
  border-color: rgba(196, 181, 253, 0.6) !important;
  transform: translateY(-3px);
}

/* Trust indicators */
.trust-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.trust-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: rgba(203, 213, 225, 0.7);
  font-weight: 500;
}

.trust-divider {
  width: 1px;
  height: 18px;
  background: rgba(203, 213, 225, 0.2);
}

@media (max-width: 600px) {
  .trust-divider {
    display: none;
  }
  .trust-row {
    gap: 14px;
  }
}

/* Scroll indicator */
.scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  color: rgba(203, 213, 225, 0.5);
  animation: bounceDown 2s ease-in-out infinite;
  z-index: 4;
}

@keyframes bounceDown {
  0%,
  100% {
    transform: translateX(-50%) translateY(0);
    opacity: 0.5;
  }
  50% {
    transform: translateX(-50%) translateY(8px);
    opacity: 1;
  }
}

/* ===================== FEATURES ===================== */
.features {
  position: relative;
  z-index: 2;
  padding: 100px 0 80px;
}

.pill-badge {
  display: inline-flex;
  align-items: center;
  padding: 7px 16px;
  border-radius: 999px;
  background: rgba(168, 85, 247, 0.08);
  border: 1px solid rgba(168, 85, 247, 0.25);
  color: #d8b4fe;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.18em;
}

.section-title {
  font-size: clamp(2rem, 4.5vw, 3.25rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #f1f5f9;
}

.gradient-text {
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
  padding-right: 0.08em;
}

.section-subtitle {
  font-size: 1.05rem;
  color: rgba(148, 163, 184, 0.85);
  line-height: 1.7;
  font-weight: 400;
  max-width: 560px;
  margin: 0 auto;
}

/* Feature card */
.feature-card {
  position: relative;
  width: 100%;
  padding: 40px 32px 36px;
  border-radius: 24px;
  background: rgba(15, 23, 42, 0.55);
  border: 1px solid rgba(148, 163, 184, 0.12);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  overflow: hidden;
  opacity: 0;
  animation: cardRise 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  transition: transform 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94),
    border-color 0.45s ease, box-shadow 0.45s ease;
}

@keyframes cardRise {
  from {
    opacity: 0;
    transform: translateY(40px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.feature-card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(
    145deg,
    rgba(168, 85, 247, 0.5),
    transparent 40%,
    transparent 60%,
    rgba(99, 102, 241, 0.4)
  );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.45s ease;
  pointer-events: none;
}

.feature-card:hover {
  transform: translateY(-10px);
  border-color: rgba(168, 85, 247, 0.3);
  box-shadow: 0 30px 60px -20px rgba(139, 92, 246, 0.4),
    0 0 0 1px rgba(168, 85, 247, 0.15);
}

.feature-card:hover::before {
  opacity: 1;
}

/* Feature icon */
.feature-icon-wrap {
  position: relative;
  width: 68px;
  height: 68px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 26px;
  transition: transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.icon-indigo {
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  box-shadow: 0 12px 30px -8px rgba(99, 102, 241, 0.7);
}
.icon-violet {
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  box-shadow: 0 12px 30px -8px rgba(139, 92, 246, 0.7);
}
.icon-fuchsia {
  background: linear-gradient(135deg, #a855f7, #d946ef);
  box-shadow: 0 12px 30px -8px rgba(217, 70, 239, 0.6);
}

.feature-icon-glow {
  position: absolute;
  inset: -10px;
  border-radius: 22px;
  background: inherit;
  filter: blur(18px);
  opacity: 0;
  transition: opacity 0.45s ease;
  z-index: -1;
}

.feature-card:hover .feature-icon-wrap {
  transform: scale(1.1) rotate(-6deg);
}

.feature-card:hover .feature-icon-glow {
  opacity: 0.55;
}

.feature-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #f1f5f9;
  margin-bottom: 12px;
  letter-spacing: -0.015em;
}

.feature-description {
  font-size: 0.95rem;
  line-height: 1.7;
  color: rgba(148, 163, 184, 0.9);
  margin: 0;
}

/* Decorative corner accent */
.feature-corner {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 80px;
  height: 80px;
  background: radial-gradient(
    circle at 100% 100%,
    rgba(168, 85, 247, 0.15),
    transparent 70%
  );
  opacity: 0;
  transition: opacity 0.45s ease;
  pointer-events: none;
}

.feature-card:hover .feature-corner {
  opacity: 1;
}

/* ===================== STATS STRIP ===================== */
.stats-strip {
  position: relative;
  z-index: 2;
  padding: 60px 0;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  background: rgba(15, 23, 42, 0.35);
  backdrop-filter: blur(10px);
}

.stat-value {
  font-size: clamp(1.75rem, 3.5vw, 2.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 6px;
}

.stat-label {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(148, 163, 184, 0.7);
}

/* ===================== CTA ===================== */
.cta {
  position: relative;
  z-index: 2;
  padding: 110px 0 120px;
  overflow: hidden;
}

.cta-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.18) 0%,
    transparent 60%
  );
  pointer-events: none;
}

.cta-inner {
  position: relative;
  z-index: 2;
}

.cta-badge {
  display: inline-flex;
  align-items: center;
  padding: 7px 16px;
  border-radius: 999px;
  background: rgba(99, 102, 241, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.3);
  color: #c7d2fe;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.18em;
}

.cta-title {
  font-size: clamp(2.25rem, 5vw, 3.75rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: #f8fafc;
}

.cta-highlight {
  display: block;
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
}

.cta-subtitle {
  font-size: 1.1rem;
  line-height: 1.7;
  color: rgba(148, 163, 184, 0.85);
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
}

.btn-cta {
  background: linear-gradient(
    120deg,
    #6366f1 0%,
    #8b5cf6 50%,
    #a855f7 100%
  ) !important;
  background-size: 200% auto !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em;
  padding: 0 40px !important;
  text-transform: none !important;
  box-shadow: 0 14px 40px -10px rgba(139, 92, 246, 0.7),
    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}

.btn-cta:hover {
  background-position: right center !important;
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 22px 55px -10px rgba(139, 92, 246, 0.9),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}

/* ===================== RESPONSIVE ===================== */
@media (max-width: 960px) {
  .hero {
    min-height: auto;
    padding: 100px 0 80px;
  }
  .features {
    padding: 70px 0 60px;
  }
  .cta {
    padding: 80px 0 90px;
  }
}

@media (max-width: 600px) {
  .orb {
    filter: blur(70px);
    opacity: 0.4;
  }
  .orb-1,
  .orb-2,
  .orb-3 {
    width: 320px;
    height: 320px;
  }
  .btn-primary-hero,
  .btn-ghost-hero,
  .btn-cta {
    width: 100%;
  }
  .feature-card {
    padding: 32px 24px 28px;
  }
  .scroll-indicator {
    display: none;
  }
}
</style>
