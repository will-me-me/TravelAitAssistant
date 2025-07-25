<template>
  <v-container fluid class="fill-height register-page">
    <v-row justify="center" align="center" class="fill-height">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="elevation-8" rounded="lg">
          <v-card-title class="text-center pa-8">
            <div class="w-100">
              <v-avatar size="80" color="primary" class="mb-4">
                <v-icon size="40" color="white">mdi-account-plus</v-icon>
              </v-avatar>
              <h1 class="text-h4 font-weight-bold">Create Account</h1>
              <p class="text-subtitle-1 text-grey-darken-1 mt-2">
                Join our travel community
              </p>
            </div>
          </v-card-title>

          <v-card-text class="pa-8">
            <v-form @submit.prevent="handleRegister" ref="form">
              <v-text-field
                v-model="name"
                label="Full Name"
                prepend-inner-icon="mdi-account"
                variant="outlined"
                :rules="nameRules"
                required
                class="mb-4"
              />

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
                class="mb-4"
              />

              <v-text-field
                v-model="confirmPassword"
                label="Confirm Password"
                :type="showConfirmPassword ? 'text' : 'password'"
                prepend-inner-icon="mdi-lock-check"
                :append-inner-icon="
                  showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'
                "
                @click:append-inner="showConfirmPassword = !showConfirmPassword"
                variant="outlined"
                :rules="confirmPasswordRules"
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
                Create Account
              </v-btn>
            </v-form>

            <v-divider class="my-6" />

            <div class="text-center">
              <p class="text-body-2">
                Already have an account?
                <nuxt-link
                  to="/login"
                  class="text-primary font-weight-bold text-decoration-none"
                >
                  Sign in
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
.register-page {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}
</style>
