<template>
  <div class="landing-page">
    <!-- Hero Section -->
    <v-container fluid class="hero-section pa-0">
      <v-row no-gutters class="fill-height">
        <v-col cols="12" class="d-flex align-center">
          <v-container>
            <v-row justify="center" align="center" class="text-center">
              <v-col cols="12" md="8" lg="6">
                <v-fade-transition appear>
                  <div>
                    <h1 class="display-1 font-weight-bold mb-4 text-primary">
                      Travel Documentation Assistant
                    </h1>
                    <h2
                      class="headline font-weight-regular mb-6 text-grey-darken"
                    >
                      Get AI-powered insights on visa requirements and travel
                      documentation for any destination
                    </h2>
                    <div
                      class="d-flex flex-column flex-sm-row justify-center ga-4"
                    >
                      <v-btn
                        size="large"
                        color="primary"
                        rounded
                        @click="navigateTo('/register')"
                      >
                        <v-icon left>mdi-account-plus</v-icon>
                        Get Started
                      </v-btn>
                      <v-btn
                        size="large"
                        color="primary"
                        rounded
                        @click="navigateTo('/login')"
                      >
                        <v-icon left>mdi-login</v-icon>
                        Sign In
                      </v-btn>
                    </div>
                  </div>
                </v-fade-transition>
              </v-col>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </v-container>

    <!-- Features Section -->
    <v-container class="py-16">
      <v-row>
        <v-col cols="12" class="text-center mb-8">
          <h2 class="display-1 font-weight-bold mb-4">
            Why Choose Our Assistant?
          </h2>
          <p class="text-h6 text-grey-darken-1">
            Powered by advanced AI technology
          </p>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          md="4"
          v-for="feature in features"
          :key="feature.title"
        >
          <v-card class="feature-card h-100" elevation="2" hover>
            <v-card-text class="text-center pa-8">
              <v-avatar size="80" class="mb-4" color="primary">
                <v-icon size="40" color="white">{{ feature.icon }}</v-icon>
              </v-avatar>
              <h3 class="text-h5 font-weight-bold mb-3">{{ feature.title }}</h3>
              <p class="text-body-1 text-grey-darken-1">
                {{ feature.description }}
              </p>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <!-- CTA Section -->
    <v-container fluid class="cta-section py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8" class="text-center">
            <h2 class="display-1 font-weight-bold mb-4 text-white">
              Ready to Plan Your Next Trip?
            </h2>
            <p class="text-h6 mb-8 text-grey-lighten-2">
              Join thousands of travelers who trust our AI assistant
            </p>
            <v-btn
              size="x-large"
              color="accent"
              rounded
              @click="navigateTo('/register')"
            >
              Start Planning Now
              <v-icon right>mdi-arrow-right</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false,
});

const features = [
  {
    icon: "mdi-robot",
    title: "AI-Powered",
    description:
      "Advanced Claude AI provides accurate and up-to-date travel documentation requirements",
  },
  {
    icon: "mdi-clock-fast",
    title: "Real-time Updates",
    description:
      "Get the latest visa requirements, travel advisories, and documentation changes",
  },
  {
    icon: "mdi-shield-check",
    title: "Reliable Information",
    description:
      "Comprehensive travel guidance with official source recommendations",
  },
];
</script>

<style scoped>
.landing-page {
  min-height: 100vh;
}

.hero-section {
  min-height: 70vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.feature-card {
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-4px);
}

.cta-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
