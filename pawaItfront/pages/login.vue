<template>
  <v-container fluid class="fill-height login-page">
    <v-row justify="center" align="center" class="fill-height">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="elevation-8" rounded="lg">
          <v-card-title class="text-center pa-8">
            <div class="w-100">
              <v-avatar size="80" color="primary" class="mb-4">
                <v-icon size="40" color="white">mdi-airplane</v-icon>
              </v-avatar>
              <h1 class="text-h4 font-weight-bold">Welcome Back</h1>
              <p class="text-subtitle-1 text-grey-darken-1 mt-2">
                Sign in to your account
              </p>
            </div>
          </v-card-title>

          <v-card-text class="pa-8">
            <v-form @submit.prevent="handleLogin" ref="form">
              <v-text-field
                v-model="email"
                label="Email"
                type="email"
                prepend-inner-icon="mdi-email"
                variant="outlined"
                :rules="emailRules"
                required
                class="mb-4"
              />

              <v-text-field
                v-model="password"
                label="Password"
                :type="showPassword ? 'text' : 'password'"
                prepend-inner-icon="mdi-lock"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"
                variant="outlined"
                :rules="passwordRules"
                required
                class="mb-6"
              />

              <v-btn
                type="submit"
                color="primary"
                size="large"
                rounded
                block
                :loading="loading"
                class="mb-4"
              >
                Sign In
              </v-btn>
            </v-form>

            <v-divider class="my-6" />

            <div class="text-center">
              <p class="text-body-2">
                Don't have an account?
                <nuxt-link
                  to="/register"
                  class="text-primary font-weight-bold text-decoration-none"
                >
                  Create one
                </nuxt-link>
              </p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
definePageMeta({
  layout: false,
});

const authStore = useAuthStore();
const form = ref(null);
const email = ref("");
const password = ref("");
const showPassword = ref(false);
const loading = ref(false);

const emailRules = [
  (v) => !!v || "Email is required",
  (v) => /.+@.+\..+/.test(v) || "Email must be valid",
];

const passwordRules = [
  (v) => !!v || "Password is required",
  (v) => v.length >= 8 || "Password must be at least 8 characters",
  (v) => /[a-zA-Z]/.test(v) || "Password must contain letters",
  (v) => /\d/.test(v) || "Password must contain numbers",
  (v) =>
    /[!@#$%^&*(),.?":{}|<>]/.test(v) ||
    "Password must contain special characters",
  (v) => !v || !v.includes(" ") || "Password cannot contain spaces",
];

const handleLogin = async () => {
  const { valid } = await form.value.validate();
  if (!valid) return;

  loading.value = true;
  try {
    await authStore.login(email.value, password.value);
    await navigateTo("/chat");
  } catch (error) {
    // Handle error
    console.error("Login failed:", error);
  } finally {
    loading.value = false;
  }
};

// Auto-login for demo
onMounted(() => {
  email.value = "demo@example.com";
  password.value = "password123";
});
</script>

<style scoped>
.login-page {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}
</style>
