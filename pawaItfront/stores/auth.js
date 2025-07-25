import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: process.client ? localStorage.getItem("access_token") : null,
    user: process.client
      ? JSON.parse(localStorage.getItem("user") || "null")
      : null,
    isAuthenticated: process.client
      ? !!localStorage.getItem("access_token")
      : false,
  }),

  actions: {
    async login(email, password) {
      try {
        const config = useRuntimeConfig();
        const response = await $fetch(`${config.public.apiBase}/users/login/`, {
          method: "POST",
          body: { email, password },
        });
        console.log("response", response);
        this.token = response.access_token;
        this.user = response.user;
        this.isAuthenticated = true;

        if (process.client) {
          localStorage.setItem("access_token", this.token);
          localStorage.setItem("user", JSON.stringify(this.user));
        }

        return response;
      } catch (error) {
        throw error;
      }
    },

    async register(userData) {
      try {
        const config = useRuntimeConfig();
        const response = await $fetch(
          `${config.public.apiBase}/users/create_user/`,
          {
            method: "POST",
            body: userData,
          }
        );
        console.log("response", response);

        this.token = response.access_token;
        this.user = response.user;
        this.isAuthenticated = true;
        console.log({ token: this.token, user: this.user });

        if (process.client) {
          localStorage.setItem("access_token", this.token);
          localStorage.setItem("user", JSON.stringify(this.user));
        }

        return response;
      } catch (error) {
        throw error;
      }
    },

    async logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;

      if (process.client) {
        localStorage.removeItem("access_token");
        localStorage.removeItem("user");
      }

      await navigateTo("/login");
    },

    async initAuth() {
      if (process.client) {
        const token = localStorage.getItem("access_token");
        const user = localStorage.getItem("user");
        if (token && user) {
          this.token = token;
          this.user = JSON.parse(user);
          this.isAuthenticated = true;
        }
      }
    },
  },
});
