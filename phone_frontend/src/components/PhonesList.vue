<template>
  <div class="text-center">
    <div>
      <head-in/>
    </div>
    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="secondary"
      @click="loader = 'loading'"
    >
      Accept Terms
    </v-btn>

    <v-btn
      :loading="loading5"
      :disabled="loading5"
      color="blue-grey"
      class="ma-2 white--text"
      fab
      @click="getPhones"
    >
      <v-icon dark>
        mdi-cloud-upload
      </v-icon>
    </v-btn>
    <div>
      <table-list/>
    </div>
  </div>
</template>

<script>

import headIn from './HeadIn'
import TableList from './PhonesLista.vue'
  export default {
    components: {
      headIn,
      TableList
    },
    data () {
      return {
        loader: null,
        loading: false,
        loading2: false,
        loading3: false,
        loading4: false,
        loading5: false,
        users : []
      }
    },
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      },
    },
    methods : {
      getPhones () {
        const baseURI = 'http://localhost:8000/api/v1/phones/'
          this.$http.get(baseURI)
          .then((result) => {
            console.log(result)
          })
      }
    }
  }
</script>

<style>
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>