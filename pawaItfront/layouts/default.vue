<template>
  <v-app class="app-root">
    <!-- ==================== SIDEBAR ==================== -->
    <v-navigation-drawer
      v-if="authStore.isAuthenticated"
      v-model="drawer"
      app
      clipped
      :width="280"
      class="app-drawer"
    >
      <!-- Decorative gradient overlay -->
      <div class="drawer-aurora" aria-hidden="true"></div>

      <div class="drawer-inner">
        <!-- Brand mark -->
        <div class="drawer-brand">
          <div class="brand-mark">
            <v-icon size="20" color="white">mdi-airplane</v-icon>
          </div>
          <div class="brand-text">
            <div class="brand-name">Travel Assistant</div>
            <div class="brand-sub">Powered by Claude AI</div>
          </div>
        </div>

        <!-- User card -->
        <div class="user-card">
          <div class="user-avatar-wrap">
            <img :src="userAvatar" alt="avatar" class="user-avatar" />
            <span class="user-status" aria-hidden="true"></span>
          </div>
          <div class="user-info">
            <div class="user-name">
              {{ authStore.user?.name || "Traveler" }}
            </div>
            <div class="user-email">
              {{ authStore.user?.email || "—" }}
            </div>
          </div>
        </div>

        <!-- Section label -->
        <div class="section-label">
          <span>NAVIGATION</span>
          <span class="section-line"></span>
        </div>

        <!-- Nav items -->
        <nav class="drawer-nav">
          <button
            class="nav-item"
            :class="{ 'nav-item--active': isActive('/chat') }"
            @click="navigateTo('/chat')"
          >
            <span class="nav-icon">
              <v-icon size="18" color="white"
                >mdi-chat-processing-outline</v-icon
              >
            </span>
            <span class="nav-text">
              <span class="nav-title">Chat</span>
              <span class="nav-desc">Ask the AI assistant</span>
            </span>
            <v-icon size="16" class="nav-chevron">mdi-chevron-right</v-icon>
          </button>

          <button
            class="nav-item"
            :class="{ 'nav-item--active': isActive('/history') }"
            @click="navigateTo('/history')"
          >
            <span class="nav-icon nav-icon--alt">
              <v-icon size="18" color="white">mdi-history</v-icon>
            </span>
            <span class="nav-text">
              <span class="nav-title">History</span>
              <span class="nav-desc">Past queries</span>
            </span>
            <v-icon size="16" class="nav-chevron">mdi-chevron-right</v-icon>
          </button>
        </nav>

        <!-- Spacer -->
        <div class="drawer-spacer"></div>

        <!-- Footer card -->
        <div class="drawer-footer">
          <div class="footer-icon">
            <v-icon size="16" color="white">mdi-shield-check</v-icon>
          </div>
          <div class="footer-text">
            <div class="footer-title">Secure & private</div>
            <div class="footer-desc">Your data stays with you</div>
          </div>
        </div>
      </div>
    </v-navigation-drawer>

    <!-- ==================== APP BAR ==================== -->
    <v-app-bar
      v-if="authStore.isAuthenticated"
      app
      clipped-left
      flat
      class="app-bar"
    >
      <div class="app-bar-inner">
        <!-- Left -->
        <div class="app-bar-left">
          <button class="menu-btn" @click="drawer = !drawer">
            <v-icon size="20" color="white">mdi-menu</v-icon>
          </button>

          <div class="app-bar-title">
            <div class="title-main">
              Travel Documentation
              <span class="title-gradient">Assistant</span>
            </div>
            <div class="title-sub">
              <span class="status-dot"></span>
              All systems online
            </div>
          </div>
        </div>

        <!-- Right -->
        <div class="app-bar-right">
          <button class="icon-btn" title="Notifications">
            <v-icon size="18" color="white">mdi-bell-outline</v-icon>
            <span class="notif-dot" aria-hidden="true"></span>
          </button>

          <div class="app-bar-divider" aria-hidden="true"></div>

          <button class="user-chip" @click="authStore.logout()">
            <img :src="userAvatar" alt="avatar" class="chip-avatar" />
            <div class="chip-text">
              <div class="chip-name">
                {{ authStore.user?.name || "Traveler" }}
              </div>
              <div class="chip-action">Sign out</div>
            </div>
            <v-icon size="16" class="chip-icon">mdi-logout</v-icon>
          </button>
        </div>
      </div>
    </v-app-bar>

    <!-- ==================== MAIN ==================== -->
    <v-main class="app-main">
      <slot />
    </v-main>

    <!-- ==================== SNACKBAR ==================== -->
    <v-snackbar
      v-model="snackbar"
      :color="snackbarColor"
      timeout="4000"
      location="bottom right"
      rounded="pill"
      class="app-snackbar"
    >
      <div class="snack-inner">
        <v-icon size="18" class="mr-2">mdi-information-outline</v-icon>
        {{ snackbarText }}
      </div>
      <template #actions>
        <v-btn variant="text" size="small" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup>
import { useRoute } from "vue-router";

const authStore = useAuthStore();
const drawer = ref(false);
const snackbar = ref(false);
const snackbarText = ref("");
const snackbarColor = ref("success");
const route = useRoute();

const userAvatar =
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSgsRIV6Utl2UgUgLGQOCdQVBvA0trMZNisibqApn1HwFxHuw70gl92t35-2Qi8bcXzoE&usqp=CAU";

const isActive = (path) => route.path === path;

onMounted(() => {
  authStore.initAuth();
});
</script>

<style scoped>
/* ===================== FONT & GLOBAL ===================== */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap");

.app-root {
  font-family: "Plus Jakarta Sans", sans-serif !important;
  background: #05060f !important;
  color: #e2e8f0;
}

:deep(.v-application__wrap) {
  background: #05060f;
}

:deep(*) {
  font-family: "Plus Jakarta Sans", sans-serif;
}

/* ===================== SIDEBAR ===================== */
.app-drawer {
  background: rgba(10, 13, 26, 0.95) !important;
  border-right: 1px solid rgba(148, 163, 184, 0.1) !important;
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
}

.app-drawer :deep(.v-navigation-drawer__content) {
  overflow: hidden;
}

.drawer-aurora {
  position: absolute;
  top: -120px;
  right: -120px;
  width: 320px;
  height: 320px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.35) 0%,
    transparent 70%
  );
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
}

.drawer-inner {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 22px 16px 18px;
}

/* Brand */
.drawer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 8px 22px;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
  margin-bottom: 20px;
}

.brand-mark {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
  box-shadow: 0 10px 24px -8px rgba(139, 92, 246, 0.75),
    inset 0 1px 0 rgba(255, 255, 255, 0.25);
  transform: rotate(-4deg);
}

.brand-name {
  font-size: 0.9rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f8fafc;
  line-height: 1.2;
}

.brand-sub {
  font-size: 0.68rem;
  color: rgba(148, 163, 184, 0.65);
  font-weight: 500;
  margin-top: 3px;
  letter-spacing: 0.02em;
}

/* User card */
.user-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 16px;
  background: linear-gradient(
    135deg,
    rgba(99, 102, 241, 0.12),
    rgba(168, 85, 247, 0.1)
  );
  border: 1px solid rgba(139, 92, 246, 0.2);
  margin-bottom: 26px;
  transition: all 0.3s ease;
}

.user-card:hover {
  border-color: rgba(139, 92, 246, 0.4);
  box-shadow: 0 12px 30px -14px rgba(139, 92, 246, 0.6);
}

.user-avatar-wrap {
  position: relative;
  flex-shrink: 0;
}

.user-avatar {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  object-fit: cover;
  border: 2px solid rgba(139, 92, 246, 0.4);
  box-shadow: 0 6px 16px -6px rgba(139, 92, 246, 0.7);
  display: block;
}

.user-status {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #22c55e;
  border: 2px solid #0a0d1a;
  box-shadow: 0 0 8px rgba(34, 197, 94, 0.8);
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-size: 0.85rem;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.user-email {
  font-size: 0.7rem;
  color: rgba(148, 163, 184, 0.7);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 2px;
  font-weight: 500;
}

/* Section label */
.section-label {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 10px;
  margin-bottom: 12px;
}

.section-label span:first-child {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: rgba(148, 163, 184, 0.55);
}

.section-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, rgba(148, 163, 184, 0.18), transparent);
}

/* Nav */
.drawer-nav {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 14px;
  width: 100%;
  padding: 12px 14px;
  border-radius: 14px;
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  text-align: left;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  font-family: inherit;
  color: inherit;
}

.nav-item:hover {
  background: rgba(139, 92, 246, 0.08);
  border-color: rgba(139, 92, 246, 0.18);
  transform: translateX(3px);
}

.nav-item--active {
  background: linear-gradient(
    135deg,
    rgba(99, 102, 241, 0.2),
    rgba(168, 85, 247, 0.15)
  );
  border-color: rgba(139, 92, 246, 0.4);
  box-shadow: 0 10px 26px -14px rgba(139, 92, 246, 0.6);
}

.nav-icon {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 11px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  box-shadow: 0 8px 18px -6px rgba(99, 102, 241, 0.65);
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.nav-icon--alt {
  background: linear-gradient(135deg, #a855f7, #ec4899);
  box-shadow: 0 8px 18px -6px rgba(168, 85, 247, 0.65);
}

.nav-item:hover .nav-icon {
  transform: rotate(-6deg) scale(1.08);
}

.nav-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.nav-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.nav-desc {
  font-size: 0.7rem;
  color: rgba(148, 163, 184, 0.7);
  margin-top: 2px;
  font-weight: 500;
}

.nav-chevron {
  color: rgba(148, 163, 184, 0.4) !important;
  transition: transform 0.3s ease, color 0.3s ease;
}

.nav-item:hover .nav-chevron {
  color: #c4b5fd !important;
  transform: translateX(3px);
}

/* Spacer */
.drawer-spacer {
  flex: 1;
}

/* Footer */
.drawer-footer {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.55);
  border: 1px solid rgba(148, 163, 184, 0.12);
  backdrop-filter: blur(10px);
}

.footer-icon {
  flex-shrink: 0;
  width: 30px;
  height: 30px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #22c55e, #16a34a);
  box-shadow: 0 6px 14px -4px rgba(34, 197, 94, 0.7);
}

.footer-title {
  font-size: 0.75rem;
  font-weight: 700;
  color: #e2e8f0;
  line-height: 1.2;
}

.footer-desc {
  font-size: 0.68rem;
  color: rgba(148, 163, 184, 0.7);
  margin-top: 2px;
  font-weight: 500;
}

/* ===================== APP BAR ===================== */
.app-bar {
  background: rgba(10, 13, 26, 0.75) !important;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1) !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  height: 68px !important;
}

.app-bar :deep(.v-toolbar__content) {
  padding: 0 22px !important;
  height: 68px !important;
}

.app-bar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 16px;
}

.app-bar-left {
  display: flex;
  align-items: center;
  gap: 16px;
  min-width: 0;
}

.menu-btn {
  flex-shrink: 0;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(139, 92, 246, 0.12);
  border: 1px solid rgba(139, 92, 246, 0.22);
  cursor: pointer;
  transition: all 0.25s ease;
}

.menu-btn:hover {
  background: rgba(139, 92, 246, 0.25);
  border-color: rgba(139, 92, 246, 0.5);
  transform: scale(1.05);
}

.app-bar-title {
  min-width: 0;
}

.title-main {
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f8fafc;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title-gradient {
  background: linear-gradient(120deg, #a5b4fc, #d8b4fe);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-family: "Instrument Serif", serif !important;
  font-style: italic;
  font-weight: 400;
  padding-right: 0.06em;
}

.title-sub {
  display: flex;
  align-items: center;
  font-size: 0.7rem;
  color: rgba(148, 163, 184, 0.7);
  margin-top: 2px;
  font-weight: 500;
  letter-spacing: 0.02em;
}

.status-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  margin-right: 6px;
  box-shadow: 0 0 6px rgba(34, 197, 94, 0.9);
}

.app-bar-right {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.icon-btn {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(148, 163, 184, 0.08);
  border: 1px solid rgba(148, 163, 184, 0.14);
  cursor: pointer;
  transition: all 0.25s ease;
}

.icon-btn:hover {
  background: rgba(139, 92, 246, 0.18);
  border-color: rgba(139, 92, 246, 0.4);
}

.notif-dot {
  position: absolute;
  top: 9px;
  right: 10px;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ec4899;
  box-shadow: 0 0 8px rgba(236, 72, 153, 0.9);
}

.app-bar-divider {
  width: 1px;
  height: 26px;
  background: rgba(148, 163, 184, 0.15);
}

/* User chip */
.user-chip {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 5px 12px 5px 5px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(148, 163, 184, 0.15);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  font-family: inherit;
  color: inherit;
}

.user-chip:hover {
  background: rgba(139, 92, 246, 0.15);
  border-color: rgba(139, 92, 246, 0.45);
  transform: translateY(-1px);
  box-shadow: 0 10px 24px -10px rgba(139, 92, 246, 0.6);
}

.chip-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(139, 92, 246, 0.4);
  display: block;
}

.chip-text {
  display: flex;
  flex-direction: column;
  text-align: left;
  min-width: 0;
}

.chip-name {
  font-size: 0.78rem;
  font-weight: 700;
  color: #f1f5f9;
  line-height: 1.15;
  max-width: 120px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.chip-action {
  font-size: 0.65rem;
  color: rgba(148, 163, 184, 0.7);
  font-weight: 500;
  letter-spacing: 0.02em;
  margin-top: 1px;
}

.chip-icon {
  color: rgba(148, 163, 184, 0.6) !important;
  transition: transform 0.3s ease, color 0.3s ease;
}

.user-chip:hover .chip-icon {
  color: #f0abfc !important;
  transform: translateX(2px);
}

/* ===================== MAIN ===================== */
.app-main {
  background: #05060f !important;
  min-height: 100vh;
}

/* ===================== SNACKBAR ===================== */
.app-snackbar :deep(.v-snackbar__wrapper) {
  border-radius: 999px !important;
  box-shadow: 0 14px 40px -10px rgba(0, 0, 0, 0.6) !important;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.snack-inner {
  display: flex;
  align-items: center;
  font-weight: 600;
  font-size: 0.85rem;
}

/* ===================== RESPONSIVE ===================== */
@media (max-width: 960px) {
  .app-bar :deep(.v-toolbar__content) {
    padding: 0 14px !important;
  }
  .title-main {
    font-size: 0.9rem;
  }
  .chip-text {
    display: none;
  }
  .user-chip {
    padding: 5px;
  }
  .app-bar-divider {
    display: none;
  }
}

@media (max-width: 600px) {
  .icon-btn {
    display: none;
  }
  .title-sub {
    display: none;
  }
}
</style>
