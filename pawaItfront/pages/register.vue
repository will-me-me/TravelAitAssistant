<template>
  <div class="register-page">
    <!-- Animated background layers -->
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>
    <div class="orb orb-3" aria-hidden="true"></div>

    <v-container fluid class="fill-height register-inner">
      <v-row justify="center" align="center" class="fill-height">
        <v-col cols="12" sm="9" md="7" lg="5" xl="4">
          <v-fade-transition appear>
            <div class="register-card">
              <!-- Decorative gradient border glow -->
              <div class="card-glow" aria-hidden="true"></div>

              <!-- Header -->
              <div class="register-header">
                <div class="avatar-wrap">
                  <div class="avatar-glow" aria-hidden="true"></div>
                  <div class="avatar">
                    <v-icon size="32" color="white">mdi-account-plus</v-icon>
                  </div>
                </div>
                <h1 class="register-title">Create Account</h1>
                <p class="register-subtitle">
                  Join our travel community and start exploring
                </p>
              </div>

              <!-- Form -->
              <div class="register-body">
                <v-form @submit.prevent="handleRegister" ref="form">
                  <div class="field-wrap">
                    <label class="field-label">Full Name</label>
                    <v-text-field
                      v-model="name"
                      placeholder="John Doe"
                      prepend-inner-icon="mdi-account-outline"
                      variant="outlined"
                      :rules="nameRules"
                      required
                      density="comfortable"
                      hide-details="auto"
                      class="custom-field"
                    />
                  </div>

                  <div class="field-wrap">
                    <label class="field-label">Email Address</label>
                    <v-text-field
                      v-model="email"
                      placeholder="you@example.com"
                      type="email"
                      prepend-inner-icon="mdi-email-outline"
                      variant="outlined"
                      :rules="emailRules"
                      required
                      density="comfortable"
                      hide-details="auto"
                      class="custom-field"
                    />
                  </div>

                  <div class="field-wrap">
                    <label class="field-label">Password</label>
                    <v-text-field
                      v-model="password"
                      placeholder="Create a strong password"
                      :type="showPassword ? 'text' : 'password'"
                      prepend-inner-icon="mdi-lock-outline"
                      :append-inner-icon="
                        showPassword ? 'mdi-eye' : 'mdi-eye-off'
                      "
                      @click:append-inner="showPassword = !showPassword"
                      variant="outlined"
                      :rules="passwordRules"
                      required
                      density="comfortable"
                      hide-details="auto"
                      class="custom-field"
                    />
                  </div>

                  <div class="field-wrap">
                    <label class="field-label">Confirm Password</label>
                    <v-text-field
                      v-model="confirmPassword"
                      placeholder="Re-enter your password"
                      :type="showConfirmPassword ? 'text' : 'password'"
                      prepend-inner-icon="mdi-lock-check-outline"
                      :append-inner-icon="
                        showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'
                      "
                      @click:append-inner="
                        showConfirmPassword = !showConfirmPassword
                      "
                      variant="outlined"
                      :rules="confirmPasswordRules"
                      required
                      density="comfortable"
                      hide-details="auto"
                      class="custom-field"
                    />
                  </div>

                  <div class="terms-row mb-6">
                    <span class="terms-text">
                      By creating an account, you agree to our
                      <a href="#" class="terms-link">Terms</a> &
                      <a href="#" class="terms-link">Privacy Policy</a>
                    </span>
                  </div>

                  <v-btn
                    type="submit"
                    size="large"
                    rounded="pill"
                    block
                    :loading="loading"
                    class="btn-submit"
                  >
                    <span v-if="!loading">Create Account</span>
                    <v-icon v-if="!loading" right size="20" class="ml-2"
                      >mdi-arrow-right</v-icon
                    >
                  </v-btn>
                </v-form>

                <!-- Divider -->
                <div class="divider">
                  <span class="divider-line"></span>
                  <span class="divider-text">OR</span>
                  <span class="divider-line"></span>
                </div>

                <!-- Sign in prompt -->
                <div class="signin-prompt">
                  <p>
                    Already have an account?
                    <nuxt-link to="/login" class="signin-link">
                      Sign in
                      <v-icon size="14" class="ml-1">mdi-arrow-right</v-icon>
                    </nuxt-link>
                  </p>
                </div>
              </div>
            </div>
          </v-fade-transition>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false,
});

const authStore = useAuthStore();
const form = ref(null);
const name = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const showPassword = ref(false);
const showConfirmPassword = ref(false);
const loading = ref(false);

const nameRules = [
  (v) => !!v || "Name is required",
  (v) => v.length >= 2 || "Name must be at least 2 characters",
];

const emailRules = [
  (v) => !!v || "Email is required",
  (v) => /.+@.+\..+/.test(v) || "Email must be valid",
];

const passwordRules = [
  (v) => !!v || "Password is required",
  (v) => v.length >= 8 || "Password must be at least 8 characters",
  (v) =>
    /[A-Z]/.test(v) || "Password must contain at least one uppercase letter",
  (v) =>
    /[a-z]/.test(v) || "Password must contain at least one lowercase letter",
  (v) => /[0-9]/.test(v) || "Password must contain at least one number",
  (v) =>
    /[!@#$%^&*(),.?":{}|<>]/.test(v) ||
    "Password must contain at least one special character",
];

const confirmPasswordRules = [
  (v) => !!v || "Please confirm your password",
  (v) => v === password.value || "Passwords do not match",
];

const handleRegister = async () => {
  const { valid } = await form.value.validate();
  if (!valid) return;

  loading.value = true;
  try {
    let user = {
      name: name.value,
      email: email.value,
      password: password.value,
      confirm_password: confirmPassword.value,
    };
    console.log("Registering user:", user);
    await authStore.register(user);
    await navigateTo("/chat");
  } catch (error) {
    console.error("Registration failed:", error);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* ===================== FONT & GLOBAL ===================== */
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap");

.register-page {
  position: relative;
  min-height: 100vh;
  font-family: "Plus Jakarta Sans", sans-serif !important;
  background: #05060f;
  color: #e2e8f0;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
}

:deep(.v-application) {
  font-family: "Plus Jakarta Sans", sans-serif !important;
}

/* ===================== BACKGROUND LAYERS ===================== */
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
    ellipse 70% 60% at 50% 50%,
    #000 20%,
    transparent 100%
  );
  -webkit-mask-image: radial-gradient(
    ellipse 70% 60% at 50% 50%,
    #000 20%,
    transparent 100%
  );
}

.orb {
  position: absolute;
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
  top: -160px;
  left: -160px;
  animation-delay: 0s;
}
.orb-2 {
  width: 480px;
  height: 480px;
  background: radial-gradient(circle, #a855f7 0%, transparent 70%);
  bottom: -180px;
  right: -160px;
  animation-delay: -6s;
}
.orb-3 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, #ec4899 0%, transparent 70%);
  top: 30%;
  right: 5%;
  opacity: 0.28;
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

/* ===================== LAYOUT ===================== */
.register-inner {
  position: relative;
  z-index: 2;
  padding: 40px 20px;
}

/* ===================== CARD ===================== */
.register-card {
  position: relative;
  border-radius: 28px;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.14);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  overflow: hidden;
  box-shadow: 0 30px 80px -30px rgba(0, 0, 0, 0.8),
    0 0 0 1px rgba(255, 255, 255, 0.02) inset;
  animation: cardIn 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

@keyframes cardIn {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* Top gradient glow line */
.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(168, 85, 247, 0.8),
    rgba(99, 102, 241, 0.8),
    transparent
  );
  z-index: 1;
}

/* ===================== HEADER ===================== */
.register-header {
  position: relative;
  padding: 40px 40px 20px;
  text-align: center;
}

.avatar-wrap {
  position: relative;
  display: inline-flex;
  margin-bottom: 20px;
}

.avatar-glow {
  position: absolute;
  inset: -12px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.55) 0%,
    transparent 70%
  );
  filter: blur(20px);
  animation: pulseGlow 3.5s ease-in-out infinite;
}

@keyframes pulseGlow {
  0%,
  100% {
    opacity: 0.6;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.08);
  }
}

.avatar {
  position: relative;
  width: 72px;
  height: 72px;
  border-radius: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
  box-shadow: 0 14px 34px -10px rgba(139, 92, 246, 0.75),
    inset 0 1px 0 rgba(255, 255, 255, 0.25);
  transform: rotate(-4deg);
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.register-card:hover .avatar {
  transform: rotate(4deg) scale(1.05);
}

.register-title {
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #f8fafc;
  margin-bottom: 8px;
  line-height: 1.2;
}

.register-subtitle {
  font-size: 0.92rem;
  color: rgba(148, 163, 184, 0.85);
  font-weight: 400;
  line-height: 1.5;
  margin: 0;
}

/* ===================== BODY ===================== */
.register-body {
  padding: 8px 40px 40px;
}

.field-wrap {
  margin-bottom: 18px;
}

.field-label {
  display: block;
  font-size: 0.76rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(203, 213, 225, 0.65);
  margin-bottom: 8px;
}

/* Custom Vuetify text field styling */
.custom-field :deep(.v-field) {
  background: rgba(2, 6, 23, 0.55) !important;
  border-radius: 14px !important;
  border: 1px solid rgba(148, 163, 184, 0.16) !important;
  transition: all 0.3s ease !important;
}

.custom-field :deep(.v-field:hover) {
  border-color: rgba(168, 85, 247, 0.4) !important;
  background: rgba(2, 6, 23, 0.7) !important;
}

.custom-field :deep(.v-field--focused) {
  border-color: rgba(168, 85, 247, 0.7) !important;
  background: rgba(2, 6, 23, 0.8) !important;
  box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.12),
    0 8px 24px -8px rgba(139, 92, 246, 0.35) !important;
}

.custom-field :deep(.v-field__input) {
  color: #f1f5f9 !important;
  font-size: 0.95rem !important;
  font-weight: 500 !important;
  padding-top: 12px !important;
  padding-bottom: 12px !important;
}

.custom-field :deep(.v-field__input::placeholder) {
  color: rgba(148, 163, 184, 0.5) !important;
  font-weight: 400 !important;
}

.custom-field :deep(.v-field__prepend-inner .v-icon),
.custom-field :deep(.v-field__append-inner .v-icon) {
  color: rgba(168, 85, 247, 0.75) !important;
  opacity: 1 !important;
  transition: color 0.3s ease !important;
}

.custom-field :deep(.v-field--focused .v-field__prepend-inner .v-icon) {
  color: #c4b5fd !important;
}

.custom-field :deep(.v-messages__message) {
  color: #f87171 !important;
  font-size: 0.74rem !important;
  margin-top: 6px !important;
  font-weight: 500 !important;
  line-height: 1.4 !important;
}

.custom-field :deep(.v-field--error) {
  border-color: rgba(248, 113, 113, 0.6) !important;
}

/* Terms row */
.terms-row {
  padding: 4px 0;
}

.terms-text {
  font-size: 0.78rem;
  color: rgba(148, 163, 184, 0.75);
  line-height: 1.6;
}

.terms-link {
  color: #c4b5fd;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.25s ease;
}

.terms-link:hover {
  color: #f0abfc;
  text-decoration: underline;
}

/* Submit button */
.btn-submit {
  background: linear-gradient(
    120deg,
    #6366f1 0%,
    #8b5cf6 50%,
    #a855f7 100%
  ) !important;
  background-size: 200% auto !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  letter-spacing: 0.01em;
  text-transform: none !important;
  height: 52px !important;
  box-shadow: 0 14px 34px -10px rgba(139, 92, 246, 0.75),
    inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
}

.btn-submit:hover {
  background-position: right center !important;
  transform: translateY(-2px);
  box-shadow: 0 20px 46px -10px rgba(139, 92, 246, 0.95),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}

.btn-submit:active {
  transform: translateY(0);
}

/* ===================== DIVIDER ===================== */
.divider {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 26px 0 20px;
}

.divider-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(148, 163, 184, 0.25),
    transparent
  );
}

.divider-text {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: rgba(148, 163, 184, 0.55);
}

/* ===================== SIGNIN PROMPT ===================== */
.signin-prompt {
  text-align: center;
}

.signin-prompt p {
  font-size: 0.9rem;
  color: rgba(148, 163, 184, 0.85);
  margin: 0;
  font-weight: 400;
}

.signin-link {
  display: inline-flex;
  align-items: center;
  color: #c4b5fd;
  font-weight: 700;
  text-decoration: none;
  margin-left: 4px;
  transition: color 0.25s ease, text-shadow 0.25s ease;
}

.signin-link:hover {
  color: #f0abfc;
  text-shadow: 0 0 14px rgba(240, 171, 252, 0.6);
}

.signin-link :deep(.v-icon) {
  transition: transform 0.25s ease;
}

.signin-link:hover :deep(.v-icon) {
  transform: translateX(4px);
}

/* ===================== RESPONSIVE ===================== */
@media (max-width: 600px) {
  .register-inner {
    padding: 20px 12px;
  }
  .register-header {
    padding: 32px 24px 16px;
  }
  .register-body {
    padding: 4px 24px 32px;
  }
  .avatar {
    width: 62px;
    height: 62px;
    border-radius: 18px;
  }
  .avatar :deep(.v-icon) {
    font-size: 26px !important;
  }
  .register-title {
    font-size: 1.5rem;
  }
  .orb {
    filter: blur(70px);
    opacity: 0.4;
  }
  .orb-1,
  .orb-2 {
    width: 320px;
    height: 320px;
  }
  .orb-3 {
    width: 260px;
    height: 260px;
  }
  .field-wrap {
    margin-bottom: 14px;
  }
}
</style>
