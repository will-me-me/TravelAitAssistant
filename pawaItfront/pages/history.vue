<!-- ============================ QUERY HISTORY PAGE ============================ -->
<template>
  <div class="history-page">
    <!-- Background layers -->
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>

    <div class="history-shell">
      <v-container class="pa-6 pa-md-10">
        <!-- Page header -->
        <header class="page-header">
          <div class="header-left">
            <div class="header-icon">
              <v-icon size="22" color="white">mdi-history</v-icon>
            </div>
            <div class="ml-4">
              <h1 class="page-title">
                Query <span class="page-title-gradient">History</span>
              </h1>
              <p class="page-subtitle">
                Browse your past travel documentation queries and answers
              </p>
            </div>
          </div>

          <div class="header-actions">
            <div class="count-badge">
              <span class="count-value">{{ travelStore.queries.length }}</span>
              <span class="count-label">
                {{ travelStore.queries.length === 1 ? "query" : "queries" }}
              </span>
            </div>
            <v-btn
              rounded="pill"
              class="new-query-btn"
              @click="navigateTo('/chat')"
            >
              <v-icon left size="18">mdi-plus</v-icon>
              New Query
            </v-btn>
          </div>
        </header>

        <!-- Grid -->
        <v-row v-if="travelStore.queries.length > 0" class="history-grid">
          <v-col
            v-for="(q, index) in travelStore.queries"
            :key="q.id"
            cols="12"
            md="6"
            lg="4"
            class="d-flex"
          >
            <article
              class="history-card"
              :style="{ animationDelay: `${index * 0.05}s` }"
              @click="viewQuery(q)"
            >
              <!-- Card top glow -->
              <div class="card-topline" aria-hidden="true"></div>

              <!-- Card header -->
              <div class="card-head">
                <div class="card-icon">
                  <v-icon size="16" color="white">mdi-chat</v-icon>
                </div>
                <div class="card-head-text">
                  <div class="card-label">QUERY</div>
                  <h3 class="card-title">
                    {{ truncateText(q.query, 60) }}
                  </h3>
                </div>
              </div>

              <!-- Card body -->
              <div class="card-body">
                <p class="card-excerpt">
                  {{ truncateText(q.response, 150) }}
                </p>
              </div>

              <!-- Card footer -->
              <div class="card-foot">
                <div class="card-date">
                  <v-icon size="13" class="mr-1">mdi-clock-outline</v-icon>
                  {{ formatDate(q.created_at) }}
                </div>
                <div class="card-cta">
                  View
                  <v-icon size="14" class="ml-1">mdi-arrow-right</v-icon>
                </div>
              </div>

              <!-- Card corner glow -->
              <div class="card-corner" aria-hidden="true"></div>
            </article>
          </v-col>
        </v-row>

        <!-- Empty state -->
        <div v-else class="empty-state">
          <div class="empty-avatar">
            <div class="empty-avatar-glow" aria-hidden="true"></div>
            <v-icon size="42" color="white">mdi-history</v-icon>
          </div>
          <h2 class="empty-title">No History Yet</h2>
          <p class="empty-subtitle">
            Start a conversation with the AI assistant to see your query history
            here.
          </p>
          <v-btn
            rounded="pill"
            size="large"
            class="empty-cta"
            @click="navigateTo('/chat')"
          >
            <v-icon left size="20">mdi-chat-plus-outline</v-icon>
            Start Chatting
          </v-btn>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: "auth",
});

const travelStore = useTravelStore();

const viewQuery = (query) => {
  travelStore.selectQuery(query);
  navigateTo("/chat");
};

const truncateText = (text, maxLength) => {
  return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
};

const formatDate = (dateString) => {
  if (!dateString) return "";
  return new Date(dateString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

onMounted(() => {
  travelStore.fetchHistory();
});
</script>

<style scoped>
/* ===================== FONT & GLOBAL ===================== */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap");

.history-page {
  position: relative;
  min-height: 100vh;
  font-family: "Plus Jakarta Sans", sans-serif !important;
  background: #05060f;
  color: #e2e8f0;
  overflow-x: hidden;
}

:deep(.v-application) {
  font-family: "Plus Jakarta Sans", sans-serif !important;
}

/* Background */
.bg-grid {
  position: absolute;
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
    ellipse 80% 60% at 50% 0%,
    #000 20%,
    transparent 100%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 80% 60% at 50% 0%,
    #000 20%,
    transparent 100%
  );
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.5;
  pointer-events: none;
  z-index: 0;
  animation: float 20s ease-in-out infinite;
}
.orb-1 {
  width: 520px;
  height: 520px;
  background: radial-gradient(circle, #6366f1 0%, transparent 70%);
  top: -180px;
  left: -180px;
}
.orb-2 {
  width: 460px;
  height: 460px;
  background: radial-gradient(circle, #a855f7 0%, transparent 70%);
  bottom: -180px;
  right: -180px;
  animation-delay: -10s;
}

@keyframes float {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  50% {
    transform: translate(30px, -30px) scale(1.08);
  }
}

.history-shell {
  position: relative;
  z-index: 2;
}

/* ===================== PAGE HEADER ===================== */
.page-header {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 40px;
  padding-bottom: 28px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
}

.header-icon {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  box-shadow: 0 14px 30px -10px rgba(139, 92, 246, 0.75),
    inset 0 1px 0 rgba(255, 255, 255, 0.25);
}

.page-title {
  font-size: clamp(1.6rem, 3vw, 2.25rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #f8fafc;
  line-height: 1.15;
  margin: 0;
}

.page-title-gradient {
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
  padding-right: 0.06em;
}

.page-subtitle {
  font-size: 0.9rem;
  color: rgba(148, 163, 184, 0.85);
  margin: 6px 0 0;
  font-weight: 400;
  line-height: 1.5;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.count-badge {
  display: inline-flex;
  align-items: baseline;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 999px;
  background: rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.25);
  backdrop-filter: blur(10px);
}

.count-value {
  font-size: 1.1rem;
  font-weight: 800;
  color: #c4b5fd;
  letter-spacing: -0.02em;
}

.count-label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(196, 181, 253, 0.7);
}

.new-query-btn {
  background: linear-gradient(
    120deg,
    #6366f1 0%,
    #8b5cf6 50%,
    #a855f7 100%
  ) !important;
  background-size: 200% auto !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em !important;
  text-transform: none !important;
  padding: 0 24px !important;
  height: 44px !important;
  box-shadow: 0 10px 26px -8px rgba(139, 92, 246, 0.7),
    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}

.new-query-btn:hover {
  background-position: right center !important;
  transform: translateY(-2px);
  box-shadow: 0 16px 38px -8px rgba(139, 92, 246, 0.9),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}

/* ===================== GRID ===================== */
.history-grid {
  margin-top: -8px;
}

.history-card {
  position: relative;
  width: 100%;
  padding: 26px 24px 22px;
  border-radius: 22px;
  background: rgba(15, 23, 42, 0.55);
  border: 1px solid rgba(148, 163, 184, 0.12);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  cursor: pointer;
  overflow: hidden;
  opacity: 0;
  animation: cardRise 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94),
    border-color 0.4s ease, box-shadow 0.4s ease;
}

@keyframes cardRise {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.history-card:hover {
  transform: translateY(-6px);
  border-color: rgba(168, 85, 247, 0.3);
  box-shadow: 0 26px 50px -20px rgba(139, 92, 246, 0.45),
    0 0 0 1px rgba(168, 85, 247, 0.15);
}

.card-topline {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(168, 85, 247, 0.7),
    rgba(99, 102, 241, 0.7),
    transparent
  );
  opacity: 0;
  transition: opacity 0.4s ease;
}

.history-card:hover .card-topline {
  opacity: 1;
}

/* Card header */
.card-head {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 18px;
}

.card-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  box-shadow: 0 8px 18px -6px rgba(139, 92, 246, 0.7);
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.history-card:hover .card-icon {
  transform: rotate(-6deg) scale(1.08);
}

.card-head-text {
  flex: 1;
  min-width: 0;
}

.card-label {
  font-size: 0.64rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: rgba(168, 85, 247, 0.85);
  margin-bottom: 6px;
}

.card-title {
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.4;
  letter-spacing: -0.015em;
  color: #f1f5f9;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Card body */
.card-body {
  margin-bottom: 20px;
}

.card-excerpt {
  font-size: 0.85rem;
  line-height: 1.7;
  color: rgba(148, 163, 184, 0.85);
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Card footer */
.card-foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
}

.card-date {
  display: inline-flex;
  align-items: center;
  font-size: 0.72rem;
  font-weight: 500;
  color: rgba(148, 163, 184, 0.7);
}

.card-cta {
  display: inline-flex;
  align-items: center;
  font-size: 0.78rem;
  font-weight: 700;
  color: #c4b5fd;
  transition: color 0.3s ease, transform 0.3s ease;
}

.history-card:hover .card-cta {
  color: #f0abfc;
  transform: translateX(3px);
}

.card-corner {
  position: absolute;
  bottom: -40px;
  right: -40px;
  width: 140px;
  height: 140px;
  background: radial-gradient(
    circle,
    rgba(168, 85, 247, 0.18) 0%,
    transparent 70%
  );
  opacity: 0;
  transition: opacity 0.5s ease;
  pointer-events: none;
}

.history-card:hover .card-corner {
  opacity: 1;
}

/* ===================== EMPTY STATE ===================== */
.empty-state {
  text-align: center;
  padding: 100px 20px;
  max-width: 500px;
  margin: 0 auto;
}

.empty-avatar {
  position: relative;
  display: inline-flex;
  width: 96px;
  height: 96px;
  border-radius: 28px;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  box-shadow: 0 22px 48px -16px rgba(139, 92, 246, 0.8);
  margin-bottom: 28px;
  transform: rotate(-4deg);
}

.empty-avatar-glow {
  position: absolute;
  inset: -16px;
  border-radius: 36px;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.5) 0%,
    transparent 70%
  );
  filter: blur(28px);
  z-index: -1;
  animation: pulseGlow 3.5s ease-in-out infinite;
}

@keyframes pulseGlow {
  0%,
  100% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
}

.empty-title {
  font-size: 1.65rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #f8fafc;
  margin-bottom: 12px;
}

.empty-subtitle {
  font-size: 0.95rem;
  line-height: 1.65;
  color: rgba(148, 163, 184, 0.85);
  margin: 0 auto 32px;
  max-width: 400px;
}

.empty-cta {
  background: linear-gradient(
    120deg,
    #6366f1 0%,
    #8b5cf6 50%,
    #a855f7 100%
  ) !important;
  background-size: 200% auto !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em !important;
  text-transform: none !important;
  padding: 0 30px !important;
  height: 50px !important;
  box-shadow: 0 14px 34px -10px rgba(139, 92, 246, 0.75),
    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}

.empty-cta:hover {
  background-position: right center !important;
  transform: translateY(-3px);
  box-shadow: 0 22px 46px -10px rgba(139, 92, 246, 0.95),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}

/* ===================== RESPONSIVE ===================== */
@media (max-width: 600px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  .header-actions {
    width: 100%;
  }
  .count-badge {
    flex: 1;
    justify-content: center;
  }
  .new-query-btn {
    flex: 1;
  }
  .history-card {
    padding: 22px 20px 18px;
  }
  .orb {
    filter: blur(70px);
    opacity: 0.35;
  }
  .orb-1,
  .orb-2 {
    width: 320px;
    height: 320px;
  }
  .empty-state {
    padding: 60px 16px;
  }
}
</style>
