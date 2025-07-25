<template>
  <v-app>
    <v-navigation-drawer
      v-if="authStore.isAuthenticated"
      v-model="drawer"
      app
      clipped
      color="surface"
    >
      <v-list>
        <v-list-item
          prepend-avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSgsRIV6Utl2UgUgLGQOCdQVBvA0trMZNisibqApn1HwFxHuw70gl92t35-2Qi8bcXzoE&usqp=CAU"
          :title="authStore.user?.name"
          :subtitle="authStore.user?.email"
        />
      </v-list>

      <v-divider />

      <v-list density="compact" nav>
        <v-list-item
          prepend-icon="mdi-chat"
          title="Chat"
          value="chat"
          @click="navigateTo('/chat')"
        />
        <v-list-item
          prepend-icon="mdi-history"
          title="History"
          value="history"
          @click="navigateTo('/history')"
        />
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      v-if="authStore.isAuthenticated"
      app
      clipped-left
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>Travel Documentation Assistant</v-toolbar-title>
      <v-spacer />
      <v-btn icon @click="authStore.logout()">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <slot />
    </v-main>

    <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="4000">
      {{ snackbarText }}
      <template #actions>
        <v-btn variant="text" @click="snackbar = false"> Close </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup>
const authStore = useAuthStore();
const drawer = ref(false);
const snackbar = ref(false);
const snackbarText = ref("");
const snackbarColor = ref("success");

onMounted(() => {
  authStore.initAuth();
});
</script>
