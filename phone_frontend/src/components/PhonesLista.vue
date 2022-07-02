<!-- <template>
  <v-card class="pt-6">
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search for contact by name"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="contacts"
      :search="search"
    ></v-data-table>
    <v-card-actions v-if="contacts.length > 0">
        <v-btn small color="error" @click="removeAllTutorials">
        Remove All
        </v-btn>
    </v-card-actions>
  </v-card>
</template> -->

<template>
  <v-row align="center" class="list px-3 mx-auto">
    <v-col cols="12" sm="12">
      <v-card class="mx-auto" tile>
        <v-card-title>Contacts</v-card-title>
        <v-data-table
          :headers="headers"
          :items="contacts"
          disable-pagination
          :hide-default-footer="true"
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small class="mr-2" @click="editTutorial(item)">mdi-pencil</v-icon>
            <!-- <v-icon small @click="deleteTutorial(item.id)">mdi-delete</v-icon> -->
          </template>
        </v-data-table>
        <v-card-actions v-if="contacts.length > 0">
          <v-btn small color="error" @click="removeAllTutorials">
            Remove All
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-col cols="12" sm="12">
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
                @click="editRegister"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </div>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Fitst name',
            align: 'start',
            filterable: false,
            value: 'first_name',
          },
          { text: 'Last name', value: 'last_name' },
          { text: 'Phone', value: 'phone' },
          { text: 'Actions', align: 'center', value: 'actions'}, 
        ],
        contacts: [],
        title: 'Holass',
        dialog: false,
        register: {
        }
      }
    },
    mounted () {
        this.getPhones()
    },
    methods : {
      getPhones () {
        let baseURI = 'http://localhost:8000/api/v1/phones/'
          this.$http.get(baseURI)
          .then((result) => {
            console.log(result)
            this.contacts = result.data
          })
      },
      onButtonClick(item){
          console.log(item)
      },
      editTutorial(item) {
        this.register = item
        console.log(item)
        this.dialog = true
    },
    removeAllTutorials() {
      this.contacts = []
    },
    editRegister () {
        this.dialog = false
        let baseURI = 'http://localhost:8000/api/v1/phones/'+ this.register.id
          this.$http.put(baseURI,this.register)
          .then((result) => {
            console.log(result)
          })
      },
    }
  }
</script>