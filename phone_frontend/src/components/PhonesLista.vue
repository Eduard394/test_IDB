<template>
  <v-card>
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
      :items="contacs"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            filterable: false,
            value: 'first_name',
          },
          { text: 'Last name', value: 'last_name' },
          { text: 'Phone', value: 'phone' },
        ],
        contacs: [],
      }
    },
    mounted () {
        this.getPhones()
    },
    methods : {
      getPhones () {
        const baseURI = 'http://localhost:8000/api/v1/phones/'
          this.$http.get(baseURI)
          .then((result) => {
            console.log(result)
            this.contacs = result.data
          })
      }
    }
  }
</script>