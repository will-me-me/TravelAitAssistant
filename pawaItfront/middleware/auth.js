export default defineNuxtRouteMiddleware(async (to, from) => {
  const authStore = useAuthStore();
  await authStore.initAuth();

  if (!authStore.isAuthenticated) {
    return navigateTo("/login");
  }
});
