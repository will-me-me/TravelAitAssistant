<template>
  <v-container class="pa-6">
    <div class="d-flex align-center mb-6">
      <v-icon class="mr-3" size="32" color="primary">mdi-history</v-icon>
      <h1 class="text-h4 font-weight-bold">Query History</h1>
    </div>

    <v-row>
      <v-col
        v-for="query in travelStore.queries"
        :key="query.id"
        cols="12"
        md="6"
        lg="4"
      >
        <v-card class="history-card h-100" hover @click="viewQuery(query)">
          <v-card-title class="d-flex align-center">
            <v-icon class="mr-2" color="primary">mdi-chat</v-icon>
            <span class="text-truncate">{{
              truncateText(query.query, 50)
            }}</span>
          </v-card-title>

          <v-card-text>
            <p class="text-body-2 text-grey-darken-1 mb-3">
              {{ truncateText(query.response, 150) }}
            </p>

            <div class="d-flex align-center text-caption text-grey-darken-2">
              <v-icon size="16" class="mr-1">mdi-clock</v-icon>
              {{ formatDate(query.created_at) }}
            </div>
          </v-card-text>

          <v-card-actions>
            <v-spacer />
            <v-btn
              color="primary"
              variant="text"
              @click.stop="viewQuery(query)"
            >
              View Details
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <div v-if="travelStore.queries.length === 0" class="text-center py-16">
      <v-icon size="100" color="grey-lighten-2" class="mb-4"
        >mdi-history</v-icon
      >
      <h2 class="text-h5 font-weight-bold mb-2">No History Yet</h2>
      <p class="text-body-1 text-grey-darken-1 mb-6">
        Start a conversation to see your query history here
      </p>
      <v-btn color="primary" @click="navigateTo('/chat')">
        Start Chatting
      </v-btn>
    </div>
  </v-container>
</template>

<script setup>
definePageMeta({
  middleware: "auth",
});

const travelStore = useTravelStore();

const viewQuery = (query) => {
  travelStore.selectQuery(query);
  navigateTo("/chat");
};

const truncateText = (text, maxLength) => {
  return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
};

const formatDate = (dateString) => {
  if (!dateString) return "";
  return new Date(dateString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

onMounted(() => {
  travelStore.fetchHistory();
});
</script>

<style scoped>
.history-card {
  transition: transform 0.2s ease;
  cursor: pointer;
}

.history-card:hover {
  transform: translateY(-2px);
}
</style>
