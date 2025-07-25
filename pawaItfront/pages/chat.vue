<template>
  <v-container fluid class="chat-container pa-0">
    <v-row no-gutters class="fill-height">
      <!-- Chat History Sidebar -->
      <v-col cols="12" md="4" lg="3" class="sidebar">
        <v-card class="h-100" flat>
          <v-card-title class="d-flex align-center pa-4">
            <v-icon class="mr-2">mdi-history</v-icon>
            Chat History
          </v-card-title>

          <v-divider />

          <v-card-text
            class="pa-0 scroll-y"
            style="height: calc(100vh - 120px)"
          >
            <v-list>
              <v-list-item
                v-for="query in travelStore.queries"
                :key="query.id"
                @click="travelStore.selectQuery(query)"
                :class="{
                  'v-list-item--active':
                    travelStore.currentQuery?.id === query.id,
                }"
                lines="two"
              >
                <template #prepend>
                  <v-avatar color="primary" size="40">
                    <v-icon>mdi-chat</v-icon>
                  </v-avatar>
                </template>

                <v-list-item-title class="text-wrap">
                  {{ truncateText(query.query, 60) }}
                </v-list-item-title>

                <v-list-item-subtitle>
                  {{ formatDate(query.created_at) }}
                </v-list-item-subtitle>

                <template #append>
                  <v-menu>
                    <template v-slot:activator="{ props }">
                      <v-btn
                        icon="mdi-dots-vertical"
                        variant="text"
                        v-bind="props"
                      ></v-btn>
                    </template>

                    <v-list>
                      <v-list-item @click.stop="handleDelete(query.id)">
                        <v-list-item-title>Delete</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </template>
              </v-list-item>
            </v-list>

            <div
              v-if="travelStore.queries.length === 0"
              class="text-center pa-8"
            >
              <v-icon size="48" color="grey-lighten-1" class="mb-4"
                >mdi-chat-outline</v-icon
              >
              <p class="text-grey-darken-1">No conversations yet</p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Chat Interface -->
      <v-col cols="12" md="8" lg="9" class="chat-main">
        <v-card class="h-100 d-flex flex-column" flat>
          <!-- Chat Header -->
          <v-card-title class="d-flex align-center pa-4 bg-primary text-white">
            <v-icon class="mr-2">mdi-robot</v-icon>
            Travel Assistant
            <v-spacer />
            <v-btn icon variant="text" color="white" @click="startNewChat">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-card-title>

          <v-divider />

          <!-- Chat Messages -->
          <v-card-text
            ref="chatContainer"
            class="flex-grow-1 pa-0 scroll-y chat-messages"
            style="height: calc(100vh - 200px)"
          >
            <div v-if="!travelStore.currentQuery" class="welcome-message">
              <div class="text-center pa-8">
                <v-avatar size="100" color="primary" class="mb-6">
                  <v-icon size="50" color="white">mdi-airplane</v-icon>
                </v-avatar>
                <h2 class="text-h4 font-weight-bold mb-4">
                  Welcome to Travel Assistant
                </h2>
                <p class="text-h6 text-grey-darken-1 mb-6">
                  Ask me about visa requirements, travel documentation, and
                  more!
                </p>

                <v-row justify="center">
                  <v-col cols="12" md="8">
                    <div class="d-flex flex-wrap justify-center ga-2">
                      <v-chip
                        v-for="example in exampleQueries"
                        :key="example"
                        color="primary"
                        variant="outlined"
                        @click="query = example"
                        class="ma-1"
                      >
                        {{ example }}
                      </v-chip>
                    </div>
                  </v-col>
                </v-row>
              </div>
            </div>

            <div v-else class="pa-4">
              <!-- User Message -->
              <div class="d-flex justify-end mb-4">
                <v-card
                  class="user-message"
                  color="primary"
                  max-width="80%"
                  rounded="lg"
                >
                  <v-card-text class="text-white">
                    {{ travelStore.currentQuery.query }}
                  </v-card-text>
                </v-card>
              </div>

              <!-- AI Response -->
              <div class="d-flex justify-start mb-4">
                <v-card
                  class="ai-message"
                  color="surface"
                  max-width="80%"
                  rounded="lg"
                  elevation="1"
                >
                  <v-card-text>
                    <div class="d-flex align-center mb-2">
                      <v-avatar size="24" color="primary" class="mr-2">
                        <v-icon size="12" color="white">mdi-robot</v-icon>
                      </v-avatar>
                      <span class="text-subtitle-2 font-weight-bold"
                        >Travel Assistant</span
                      >
                    </div>
                    <div
                      class="response-content"
                      v-html="formatResponse(travelStore.currentQuery.response)"
                    />
                  </v-card-text>
                </v-card>
              </div>
            </div>

            <!-- Loading Message -->
            <div
              v-if="travelStore.loading"
              class="d-flex justify-start mb-4 pa-4"
            >
              <v-card
                class="ai-message"
                color="surface"
                max-width="80%"
                rounded="lg"
                elevation="1"
              >
                <v-card-text>
                  <div class="d-flex align-center">
                    <v-progress-circular
                      indeterminate
                      color="primary"
                      size="20"
                      width="2"
                      class="mr-3"
                    />
                    <span>Thinking...</span>
                  </div>
                </v-card-text>
              </v-card>
            </div>
          </v-card-text>

          <!-- Input Area -->
          <v-divider />
          <v-card-actions class="pa-4">
            <v-form @submit.prevent="handleSubmit" class="w-100">
              <v-row no-gutters align="center">
                <v-col>
                  <v-textarea
                    v-model="query"
                    placeholder="Ask about travel requirements..."
                    variant="outlined"
                    rows="1"
                    auto-grow
                    max-rows="4"
                    hide-details
                    class="mr-2"
                    @keydown.enter.prevent="handleSubmit"
                  />
                </v-col>
                <v-col cols="auto">
                  <v-btn
                    type="submit"
                    color="primary"
                    icon
                    size="large"
                    :disabled="!query.trim() || travelStore.loading"
                    :loading="travelStore.loading"
                  >
                    <v-icon>mdi-send</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
definePageMeta({
  middleware: "auth",
});

const travelStore = useTravelStore();
const query = ref("");
const chatContainer = ref(null);

const exampleQueries = [
  "Kenya to Ireland visa requirements",
  "US to Japan travel documents",
  "COVID-19 travel restrictions",
  "Passport renewal process",
];

const handleDelete = async (queryId) => {
  try {
    await travelStore.deleteQuery(queryId);
  } catch (error) {
    console.error("Error deleting query:", error);
  }
};

const handleSubmit = async () => {
  if (!query.value.trim()) return;

  try {
    await travelStore.submitQuery(query.value);
    query.value = "";
    nextTick(() => {
      scrollToBottom();
    });
  } catch (error) {
    console.error("Error submitting query:", error);
  }
};

const startNewChat = () => {
  travelStore.currentQuery = null;
  query.value = "";
};

const truncateText = (text, maxLength) => {
  return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
};

const formatDate = (dateString) => {
  if (!dateString) return "";
  return new Date(dateString).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const formatResponse = (text) => {
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n\n/g, "</p><p>")
    .replace(/\n/g, "<br>")
    .replace(/^/, "<p>")
    .replace(/$/, "</p>");
};

const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

onMounted(() => {
  travelStore.fetchHistory();
});
</script>

<style scoped>
.chat-container {
  height: 100vh;
}

.sidebar {
  border-right: 1px solid rgba(0, 0, 0, 0.12);
}

.chat-messages {
  overflow-y: auto;
}

.welcome-message {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-message {
  margin-left: auto;
}

.ai-message {
  margin-right: auto;
}

.response-content {
  line-height: 1.6;
}

.response-content p {
  margin-bottom: 1rem;
}

.response-content strong {
  font-weight: 600;
  color: rgb(var(--v-theme-primary));
}
</style>
