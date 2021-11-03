<template>
  <v-container fluid>
    <div class="text-h2 text-center">Music bot gwiezdnej floty</div>
    <v-row class="mt-4" align="center" justify="center">
      <v-col cols="6">
        <v-card class="pa-2">
          <v-text-field
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            label="hasło"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
          />
          <v-btn @click="reboot()">Ożyw czarodzieja</v-btn>

          <v-progress-linear
            :active="progress"
            absolute
            bottom
            indeterminate
            color="cyan"
          />
        </v-card>
      </v-col>
    </v-row>
    <v-snackbar :color="snackbarColor" v-model="snackbar"
      ><div class="text-h5 text-center">{{ snackbarText }}</div></v-snackbar
    >
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data() {
    return {
      password: "",
      snackbarText: "fail",
      snackbarColor: "error",
      snackbar: false,
      showPassword: false,
      progress: false,
    };
  },

  methods: {
    reboot() {
      let data = new FormData();
      data.append("csrfmiddlewaretoken", this.$cookies.get("csrftoken"));
      data.append("password", this.password);

      this.progress = true
      this.axios.post("/reboot/", data).then((res) => {
        if (res.data.status == "success") {
          this.snackbarText = "Ożywiony";
          this.snackbarColor = "success";
          this.snackbar = true;
        } else {
          this.snackbarText = "dupa";
          this.snackbarColor = "error";
          this.snackbar = true;
        }
        this.progress = false
      });
    },
  },
};
</script>

<style scoped>
.stretch {
  height: 100vh;
}
</style>