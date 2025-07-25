import { defineStore } from "pinia";
import { useAuthStore } from "@/stores/auth";

export const useTravelStore = defineStore("travel", {
  state: () => ({
    queries: [],
    currentQuery: null,
    loading: false,
    error: null,
  }),

  actions: {
    async submitQuery(query) {
      this.loading = true;
      this.error = null;

      try {
        const config = useRuntimeConfig();
        const authStore = useAuthStore();
        const token = authStore.token;
        const response = await $fetch(`${config.public.apiBase}/travel/query`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: { query },
        });

        this.currentQuery = response;
        this.queries.unshift(response);
        return response;
      } catch (error) {
        this.error = error?.data?.detail || "Failed to process query";
        throw error;
      } finally {
        this.loading = false;
      }
    },

    async fetchHistory() {
      try {
        const config = useRuntimeConfig();
        // const token =  // Replace with actual token retrieval logic
        const authStore = useAuthStore();
        const token = authStore.token;
        const history = await $fetch(
          `${config.public.apiBase}/travel/history`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );
        console.log(
          "Fetched history:",
          history.length,
          "user_id:",
          authStore.user.id
        );
        const currentUserHistory = history.filter(
          (item) => item.user_id === authStore.user.id
        );
        console.log("Filtered history for current user:", currentUserHistory);
        this.queries = currentUserHistory;
      } catch (error) {
        console.error("Failed to fetch history:", error);
      }
    },

    async deleteQuery(chatId) {
      try {
        const config = useRuntimeConfig();
        const authStore = useAuthStore();
        const token = authStore.token;

        const res = await $fetch(
          `${config.public.apiBase}/travel/documentation/${chatId}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );
        console.log("Query deleted successfully:", res);
        this.queries = this.queries.filter((query) => query.id !== chatId);
        this.currentQuery = null; // Reset current query after deletion
        return res;
      } catch (error) {
        console.error("Failed to delete query:", error);
        this.error = error?.data?.detail || "Failed to delete query";
        throw error;
      }
    },

    selectQuery(query) {
      this.currentQuery = query;
    },
  },
});
