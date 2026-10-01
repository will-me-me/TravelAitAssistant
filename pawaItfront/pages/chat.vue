<!-- ================================ CHAT PAGE ================================ -->
<template>
  <div class="chat-page">
    <!-- Background layers -->
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>

    <div class="chat-shell">
      <v-row no-gutters class="fill-height">
        <!-- ==================== SIDEBAR ==================== -->
        <v-col cols="12" md="4" lg="3" class="sidebar-col">
          <aside class="sidebar">
            <!-- Sidebar header -->
            <div class="sidebar-header">
              <div class="d-flex align-center">
                <div class="sidebar-icon">
                  <v-icon size="18" color="white">mdi-history</v-icon>
                </div>
                <div class="ml-3">
                  <div class="sidebar-title">Chat History</div>
                  <div class="sidebar-count">
                    {{ travelStore.queries.length }}
                    {{ travelStore.queries.length === 1 ? "chat" : "chats" }}
                  </div>
                </div>
              </div>
              <v-btn
                icon
                size="small"
                variant="text"
                class="new-chat-btn"
                @click="startNewChat"
              >
                <v-icon size="18">mdi-plus</v-icon>
              </v-btn>
            </div>

            <!-- Sidebar list -->
            <div class="sidebar-scroll">
              <div
                v-if="travelStore.queries.length === 0"
                class="empty-sidebar"
              >
                <div class="empty-icon">
                  <v-icon size="26" color="rgba(168,85,247,0.7)"
                    >mdi-chat-outline</v-icon
                  >
                </div>
                <p class="empty-title">No conversations yet</p>
                <p class="empty-hint">Start a new chat to see it here</p>
              </div>

              <v-list v-else class="sidebar-list" bg-color="transparent">
                <v-list-item
                  v-for="q in travelStore.queries"
                  :key="q.id"
                  @click="travelStore.selectQuery(q)"
                  :class="[
                    'sidebar-item',
                    {
                      'sidebar-item--active':
                        travelStore.currentQuery?.id === q.id,
                    },
                  ]"
                  lines="two"
                  rounded="lg"
                >
                  <template #prepend>
                    <div
                      class="item-avatar"
                      :class="{
                        'item-avatar--active':
                          travelStore.currentQuery?.id === q.id,
                      }"
                    >
                      <v-icon size="16" color="white">mdi-chat</v-icon>
                    </div>
                  </template>

                  <v-list-item-title class="item-title">
                    {{ truncateText(q.query, 42) }}
                  </v-list-item-title>

                  <v-list-item-subtitle class="item-subtitle">
                    <v-icon size="11" class="mr-1">mdi-clock-outline</v-icon>
                    {{ formatDate(q.created_at) }}
                  </v-list-item-subtitle>

                  <template #append>
                    <v-menu location="bottom end">
                      <template #activator="{ props }">
                        <v-btn
                          icon
                          size="x-small"
                          variant="text"
                          class="item-menu-btn"
                          v-bind="props"
                          @click.stop
                        >
                          <v-icon size="16">mdi-dots-vertical</v-icon>
                        </v-btn>
                      </template>

                      <v-list class="dropdown-menu" density="compact">
                        <v-list-item
                          @click.stop="handleDelete(q.id)"
                          class="dropdown-item dropdown-item--danger"
                        >
                          <template #prepend>
                            <v-icon size="16" color="#f87171"
                              >mdi-delete-outline</v-icon
                            >
                          </template>
                          <v-list-item-title class="dropdown-text">
                            Delete
                          </v-list-item-title>
                        </v-list-item>
                      </v-list>
                    </v-menu>
                  </template>
                </v-list-item>
              </v-list>
            </div>
          </aside>
        </v-col>

        <!-- ==================== CHAT MAIN ==================== -->
        <v-col cols="12" md="8" lg="9" class="chat-col">
          <main class="chat-main">
            <!-- Chat header -->
            <header class="chat-header">
              <div class="d-flex align-center">
                <div class="bot-avatar">
                  <v-icon size="20" color="white">mdi-robot-happy</v-icon>
                  <span class="bot-status" aria-hidden="true"></span>
                </div>
                <div class="ml-3">
                  <div class="chat-header-title">Travel Assistant</div>
                  <div class="chat-header-subtitle">
                    <span class="status-dot"></span>
                    Online · Powered by Claude AI
                  </div>
                </div>
              </div>

              <div class="header-actions">
                <v-btn
                  size="small"
                  variant="text"
                  class="header-btn"
                  @click="startNewChat"
                >
                  <v-icon left size="16">mdi-plus</v-icon>
                  New Chat
                </v-btn>
              </div>
            </header>

            <!-- Messages -->
            <div ref="chatContainer" class="chat-messages">
              <!-- Welcome state -->
              <div v-if="!travelStore.currentQuery" class="welcome-wrap">
                <div class="welcome-inner">
                  <div class="welcome-avatar">
                    <div class="welcome-avatar-glow" aria-hidden="true"></div>
                    <v-icon size="42" color="white">mdi-airplane</v-icon>
                  </div>
                  <h2 class="welcome-title">
                    Welcome to
                    <span class="welcome-gradient">Travel Assistant</span>
                  </h2>
                  <p class="welcome-subtitle">
                    Ask me about visa requirements, travel documentation, and
                    more. I'll help you plan with confidence.
                  </p>

                  <div class="examples-label">
                    <v-icon size="14" class="mr-2"
                      >mdi-lightbulb-on-outline</v-icon
                    >
                    TRY ASKING
                  </div>
                  <div class="examples-grid">
                    <button
                      v-for="example in exampleQueries"
                      :key="example"
                      class="example-chip"
                      @click="query = example"
                    >
                      <v-icon size="14" class="mr-2"
                        >mdi-arrow-top-right</v-icon
                      >
                      {{ example }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- Conversation -->
              <div v-else class="messages-inner">
                <!-- User -->
                <div class="msg-row msg-row--user">
                  <div class="msg-bubble msg-bubble--user">
                    {{ travelStore.currentQuery.query }}
                  </div>
                </div>

                <!-- AI -->
                <div class="msg-row msg-row--ai">
                  <div class="msg-avatar">
                    <v-icon size="14" color="white">mdi-robot</v-icon>
                  </div>
                  <div class="msg-bubble msg-bubble--ai">
                    <div class="msg-author">Travel Assistant</div>
                    <div
                      class="response-content"
                      v-html="formatResponse(travelStore.currentQuery.response)"
                    />
                  </div>
                </div>
              </div>

              <!-- Loading -->
              <div v-if="travelStore.loading" class="msg-row msg-row--ai">
                <div class="msg-avatar">
                  <v-icon size="14" color="white">mdi-robot</v-icon>
                </div>
                <div class="msg-bubble msg-bubble--ai msg-bubble--loading">
                  <div class="typing">
                    <span></span><span></span><span></span>
                  </div>
                  <div class="msg-author ml-2">Thinking…</div>
                </div>
              </div>
            </div>

            <!-- Input -->
            <footer class="chat-input-wrap">
              <form @submit.prevent="handleSubmit" class="chat-form">
                <div class="input-shell">
                  <v-textarea
                    v-model="query"
                    placeholder="Ask about travel requirements…"
                    variant="plain"
                    rows="1"
                    auto-grow
                    max-rows="5"
                    hide-details
                    class="input-field"
                    @keydown.enter.prevent="handleSubmit"
                  />
                  <button
                    type="submit"
                    class="send-btn"
                    :disabled="!query.trim() || travelStore.loading"
                  >
                    <v-icon size="20" color="white">mdi-send</v-icon>
                  </button>
                </div>
                <div class="input-hint">
                  Press <kbd>Enter</kbd> to send · <kbd>Shift</kbd> +
                  <kbd>Enter</kbd> for new line
                </div>
              </form>
            </footer>
          </main>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: "auth",
});

const travelStore = useTravelStore();
const query = ref("");
const chatContainer = ref(null);

const exampleQueries = [
  "Kenya to Ireland visa requirements",
  "US to Japan travel documents",
  "COVID-19 travel restrictions",
  "Passport renewal process",
];

const handleDelete = async (queryId) => {
  try {
    await travelStore.deleteQuery(queryId);
  } catch (error) {
    console.error("Error deleting query:", error);
  }
};

const handleSubmit = async () => {
  if (!query.value.trim()) return;

  try {
    await travelStore.submitQuery(query.value);
    query.value = "";
    nextTick(() => {
      scrollToBottom();
    });
  } catch (error) {
    console.error("Error submitting query:", error);
  }
};

const startNewChat = () => {
  travelStore.currentQuery = null;
  query.value = "";
};

const truncateText = (text, maxLength) => {
  return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
};

const formatDate = (dateString) => {
  if (!dateString) return "";
  return new Date(dateString).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const formatResponse = (text) => {
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n\n/g, "</p><p>")
    .replace(/\n/g, "<br>")
    .replace(/^/, "<p>")
    .replace(/$/, "</p>");
};

const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

onMounted(() => {
  travelStore.fetchHistory();
});
</script>

<style scoped>
/* ===================== FONT & GLOBAL ===================== */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap");

.chat-page {
  position: relative;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  font-family: "Plus Jakarta Sans", sans-serif !important;
  background: #05060f;
  color: #e2e8f0;
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
      rgba(148, 163, 184, 0.05) 1px,
      transparent 1px
    ),
    linear-gradient(90deg, rgba(148, 163, 184, 0.05) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: radial-gradient(
    ellipse 80% 70% at 50% 40%,
    #000 20%,
    transparent 100%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 80% 70% at 50% 40%,
    #000 20%,
    transparent 100%
  );
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.4;
  pointer-events: none;
  z-index: 0;
  animation: float 20s ease-in-out infinite;
}
.orb-1 {
  width: 500px;
  height: 500px;
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

/* Shell */
.chat-shell {
  position: relative;
  z-index: 2;
  height: 100vh;
}

/* ===================== SIDEBAR ===================== */
.sidebar-col {
  height: 100vh;
}

.sidebar {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: rgba(15, 23, 42, 0.6);
  border-right: 1px solid rgba(148, 163, 184, 0.1);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 20px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.sidebar-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  box-shadow: 0 8px 20px -6px rgba(139, 92, 246, 0.6);
}

.sidebar-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: -0.01em;
}

.sidebar-count {
  font-size: 0.72rem;
  color: rgba(148, 163, 184, 0.7);
  font-weight: 500;
  margin-top: 2px;
}

.new-chat-btn {
  color: rgba(203, 213, 225, 0.8) !important;
  border: 1px solid rgba(148, 163, 184, 0.15) !important;
  border-radius: 10px !important;
  transition: all 0.25s ease !important;
}

.new-chat-btn:hover {
  background: rgba(139, 92, 246, 0.15) !important;
  border-color: rgba(139, 92, 246, 0.5) !important;
  color: #c4b5fd !important;
}

.sidebar-scroll {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
}

.sidebar-scroll::-webkit-scrollbar {
  width: 6px;
}
.sidebar-scroll::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.15);
  border-radius: 3px;
}

/* Empty state */
.empty-sidebar {
  text-align: center;
  padding: 40px 20px;
}

.empty-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto 16px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.empty-title {
  font-size: 0.85rem;
  font-weight: 600;
  color: rgba(203, 213, 225, 0.9);
  margin: 0 0 4px;
}

.empty-hint {
  font-size: 0.75rem;
  color: rgba(148, 163, 184, 0.6);
  margin: 0;
}

/* Sidebar items */
.sidebar-list {
  padding: 0 !important;
}

.sidebar-item {
  margin-bottom: 6px !important;
  padding: 12px 10px !important;
  border-radius: 12px !important;
  border: 1px solid transparent !important;
  cursor: pointer;
  transition: all 0.25s ease;
  min-height: auto !important;
}

.sidebar-item:hover {
  background: rgba(139, 92, 246, 0.08) !important;
  border-color: rgba(139, 92, 246, 0.15) !important;
}

.sidebar-item--active {
  background: linear-gradient(
    135deg,
    rgba(99, 102, 241, 0.18),
    rgba(168, 85, 247, 0.14)
  ) !important;
  border-color: rgba(139, 92, 246, 0.35) !important;
  box-shadow: 0 6px 20px -10px rgba(139, 92, 246, 0.5);
}

.item-avatar {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(148, 163, 184, 0.15);
  transition: all 0.25s ease;
}

.item-avatar--active {
  background: linear-gradient(135deg, #6366f1, #a855f7);
  box-shadow: 0 4px 12px -4px rgba(139, 92, 246, 0.7);
}

.item-title {
  font-size: 0.83rem !important;
  font-weight: 600 !important;
  color: rgba(226, 232, 240, 0.92) !important;
  white-space: normal !important;
  line-height: 1.35 !important;
  margin-bottom: 3px !important;
  opacity: 1 !important;
}

.item-subtitle {
  font-size: 0.7rem !important;
  color: rgba(148, 163, 184, 0.65) !important;
  opacity: 1 !important;
  display: flex;
  align-items: center;
  font-weight: 500 !important;
}

.item-menu-btn {
  color: rgba(148, 163, 184, 0.5) !important;
  transition: all 0.2s ease !important;
}

.item-menu-btn:hover {
  color: #f87171 !important;
  background: rgba(248, 113, 113, 0.1) !important;
}

.dropdown-menu {
  background: rgba(15, 23, 42, 0.95) !important;
  backdrop-filter: blur(20px);
  border: 1px solid rgba(148, 163, 184, 0.15);
  border-radius: 10px !important;
}

.dropdown-item--danger:hover {
  background: rgba(248, 113, 113, 0.1) !important;
}

.dropdown-text {
  font-size: 0.8rem !important;
  font-weight: 600 !important;
  color: #f87171 !important;
}

/* ===================== CHAT MAIN ===================== */
.chat-col {
  height: 100vh;
}

.chat-main {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: rgba(5, 6, 15, 0.4);
  backdrop-filter: blur(10px);
}

/* Header */
.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 28px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(20px);
}

.bot-avatar {
  position: relative;
  width: 42px;
  height: 42px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  box-shadow: 0 8px 24px -8px rgba(139, 92, 246, 0.7);
}

.bot-status {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #22c55e;
  border: 2px solid #0f172a;
  box-shadow: 0 0 8px rgba(34, 197, 94, 0.8);
}

.chat-header-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: -0.01em;
}

.chat-header-subtitle {
  font-size: 0.72rem;
  color: rgba(148, 163, 184, 0.75);
  display: flex;
  align-items: center;
  margin-top: 2px;
  font-weight: 500;
}

.status-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  margin-right: 6px;
  box-shadow: 0 0 6px rgba(34, 197, 94, 0.8);
}

.header-btn {
  color: rgba(203, 213, 225, 0.85) !important;
  border: 1px solid rgba(148, 163, 184, 0.15) !important;
  border-radius: 10px !important;
  text-transform: none !important;
  font-weight: 600 !important;
  letter-spacing: 0 !important;
  transition: all 0.25s ease !important;
}

.header-btn:hover {
  background: rgba(139, 92, 246, 0.15) !important;
  border-color: rgba(139, 92, 246, 0.5) !important;
  color: #c4b5fd !important;
}

/* Messages scroll area */
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 28px;
  scroll-behavior: smooth;
}

.chat-messages::-webkit-scrollbar {
  width: 8px;
}
.chat-messages::-webkit-scrollbar-track {
  background: transparent;
}
.chat-messages::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.15);
  border-radius: 4px;
}
.chat-messages::-webkit-scrollbar-thumb:hover {
  background: rgba(148, 163, 184, 0.3);
}

/* Welcome */
.welcome-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  padding: 20px;
}

.welcome-inner {
  text-align: center;
  max-width: 640px;
}

.welcome-avatar {
  position: relative;
  display: inline-flex;
  width: 88px;
  height: 88px;
  border-radius: 26px;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  box-shadow: 0 20px 46px -14px rgba(139, 92, 246, 0.8);
  margin-bottom: 28px;
  transform: rotate(-4deg);
}

.welcome-avatar-glow {
  position: absolute;
  inset: -14px;
  border-radius: 32px;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.5) 0%,
    transparent 70%
  );
  filter: blur(24px);
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

.welcome-title {
  font-size: clamp(1.6rem, 3.5vw, 2.25rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #f8fafc;
  margin-bottom: 14px;
}

.welcome-gradient {
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
  padding-right: 0.06em;
}

.welcome-subtitle {
  font-size: 1rem;
  line-height: 1.65;
  color: rgba(148, 163, 184, 0.85);
  max-width: 480px;
  margin: 0 auto 32px;
}

.examples-label {
  display: inline-flex;
  align-items: center;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: rgba(168, 85, 247, 0.85);
  margin-bottom: 14px;
}

.examples-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

.example-chip {
  display: inline-flex;
  align-items: center;
  padding: 11px 18px;
  border-radius: 999px;
  font-size: 0.83rem;
  font-weight: 600;
  color: #cbd5e1;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(148, 163, 184, 0.16);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  font-family: inherit;
  backdrop-filter: blur(10px);
}

.example-chip:hover {
  color: #ffffff;
  background: linear-gradient(
    120deg,
    rgba(99, 102, 241, 0.25),
    rgba(168, 85, 247, 0.25)
  );
  border-color: rgba(168, 85, 247, 0.6);
  transform: translateY(-2px);
  box-shadow: 0 10px 24px -8px rgba(139, 92, 246, 0.6);
}

/* Conversation */
.messages-inner {
  max-width: 860px;
  margin: 0 auto;
}

.msg-row {
  display: flex;
  margin-bottom: 22px;
  animation: msgIn 0.4s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

@keyframes msgIn {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.msg-row--user {
  justify-content: flex-end;
}

.msg-row--ai {
  justify-content: flex-start;
  gap: 10px;
}

.msg-bubble {
  max-width: 78%;
  padding: 14px 18px;
  border-radius: 18px;
  font-size: 0.93rem;
  line-height: 1.65;
  word-wrap: break-word;
}

.msg-bubble--user {
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  color: #ffffff;
  border-bottom-right-radius: 6px;
  box-shadow: 0 10px 28px -10px rgba(139, 92, 246, 0.7);
  font-weight: 500;
}

.msg-bubble--ai {
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(148, 163, 184, 0.14);
  color: #e2e8f0;
  border-bottom-left-radius: 6px;
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px -14px rgba(0, 0, 0, 0.6);
}

.msg-avatar {
  flex-shrink: 0;
  width: 30px;
  height: 30px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  box-shadow: 0 6px 16px -6px rgba(139, 92, 246, 0.7);
  margin-top: 2px;
}

.msg-author {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #c4b5fd;
  margin-bottom: 8px;
}

.msg-bubble--loading {
  display: flex;
  align-items: center;
  padding: 16px 20px;
}

.typing {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.typing span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #c4b5fd;
  animation: typingBounce 1.4s ease-in-out infinite;
}

.typing span:nth-child(2) {
  animation-delay: 0.2s;
}
.typing span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typingBounce {
  0%,
  60%,
  100% {
    transform: translateY(0);
    opacity: 0.5;
  }
  30% {
    transform: translateY(-5px);
    opacity: 1;
  }
}

/* Response content */
.response-content :deep(p) {
  margin-bottom: 0.75rem;
}
.response-content :deep(p:last-child) {
  margin-bottom: 0;
}
.response-content :deep(strong) {
  font-weight: 700;
  color: #c4b5fd;
}

/* Input */
.chat-input-wrap {
  padding: 18px 28px 22px;
  border-top: 1px solid rgba(148, 163, 184, 0.1);
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(20px);
}

.chat-form {
  max-width: 860px;
  margin: 0 auto;
}

.input-shell {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  padding: 8px 8px 8px 18px;
  border-radius: 20px;
  background: rgba(2, 6, 23, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.16);
  transition: all 0.3s ease;
}

.input-shell:focus-within {
  border-color: rgba(168, 85, 247, 0.6);
  background: rgba(2, 6, 23, 0.85);
  box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.12),
    0 12px 30px -12px rgba(139, 92, 246, 0.5);
}

.input-field {
  flex: 1;
}

.input-field :deep(.v-field) {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

.input-field :deep(.v-field__input) {
  color: #f1f5f9 !important;
  font-size: 0.95rem !important;
  font-weight: 500 !important;
  font-family: inherit !important;
  padding: 10px 0 !important;
  min-height: auto !important;
}

.input-field :deep(.v-field__input::placeholder) {
  color: rgba(148, 163, 184, 0.5) !important;
  font-weight: 400 !important;
}

.input-field :deep(textarea) {
  resize: none !important;
  padding: 0 !important;
}

.send-btn {
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  border-radius: 14px;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  box-shadow: 0 8px 24px -8px rgba(139, 92, 246, 0.8),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.send-btn:hover:not(:disabled) {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 14px 32px -8px rgba(139, 92, 246, 0.95),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.send-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  filter: grayscale(0.4);
}

.input-hint {
  font-size: 0.7rem;
  color: rgba(148, 163, 184, 0.5);
  text-align: center;
  margin-top: 10px;
  font-weight: 500;
}

.input-hint kbd {
  display: inline-block;
  padding: 1px 6px;
  border-radius: 5px;
  background: rgba(148, 163, 184, 0.12);
  border: 1px solid rgba(148, 163, 184, 0.2);
  font-family: inherit;
  font-size: 0.68rem;
  color: rgba(203, 213, 225, 0.85);
  margin: 0 2px;
}

/* ===================== RESPONSIVE ===================== */
@media (max-width: 960px) {
  .sidebar-col {
    display: none;
  }
  .chat-messages {
    padding: 20px 16px;
  }
  .chat-input-wrap {
    padding: 14px 16px 18px;
  }
  .chat-header {
    padding: 14px 18px;
  }
  .msg-bubble {
    max-width: 88%;
  }
}
</style>
