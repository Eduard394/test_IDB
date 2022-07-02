<template>
  <div class="text-center">
    <div>
      <head-in/>
    </div>
    <div class="justify-end">
      <v-row justify="start">
        <v-dialog
          v-model="dialog"
          persistent
          max-width="600px"
        >
          <v-card>
            <v-card-title>
              <span class="text-h5">Add contact</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="12"
                  >
                    <v-text-field
                      label="First name*"
                      required
                      v-model="register.first_name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="Last name*"
                      required
                      v-model="register.last_name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="Phone*"
                      type="number"
                      required
                      v-model="register.phone"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="red darken-1"
                text
                @click="dialog = false"
              >
                Close
              </v-btn>
              <v-btn
                color="green darken-1"
                text
                @click="saveRegister"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-row justify="start" class="mr-4">
          <v-card-text>
            <div class="text-h6 pa-1">Contacts</div>
          </v-card-text>
        </v-row>
        <v-row justify="end" class="mr-4 mt-1">
          <v-btn
            color="primary"
            dark
            @click.stop="dialog = true"
          >
            Add contact
          </v-btn>
        </v-row>
      </v-row>
    </div>
    
    <div>
      <v-divider class="pa-6" v-show="false"></v-divider>
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
        users : [],
        dialog: false,
        register: {
          first_name: '',
          last_name: '',
          phone: null
        }
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
      },
      saveRegister () {
        console.log('la dta ', this.register)
        this.dialog = false
        const baseURI = 'http://localhost:8000/api/v1/phones/'
          this.$http.post(baseURI,this.register)
          .then((result) => {
            console.log(result)
          })
      },
      validateData () {
        if(this.register.first_name == ''){
          return false
        }
        
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