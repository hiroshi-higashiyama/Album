<template>
  <div class="columns">
    <div class="column is-three-fifths is-offset-one-fifth">
      <h1 class="title">Login</h1>

      <div class="box">
        <form @submit.prevent="submitForm">
          <div class="field">
            <div class="control has-icons-left">
              <input
                type="email"
                name="email"
                class="input"
                placeholder="Email"
                v-model="username"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-envelope"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <div class="control has-icons-left">
              <input
                type="password"
                name="password"
                class="input"
                placeholder="Password"
                v-model="password"
              />
              <span class="icon is-small is-left">
                <i class="fa fa-lock"></i>
              </span>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field mt-5">
            <div class="control">
              <button class="button is-success">Login</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Login";
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true);

      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again!");
          }
        });

      await axios
        .get("/api/v1/users/me")
        .then((response) => {
          this.$store.commit("setUser", {
            id: response.data.id,
            username: response.data.username,
          });

          localStorage.setItem("username", response.data.username);
          localStorage.setItem("userid", response.data.id);

          this.$router.push("/posts");
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
