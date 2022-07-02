<template>
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
      :items="contacs"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<!--
<template>
    <v-data-table :headers="headers" :items="contacs">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.first_name}}</td>
            <td>{{row.item.last_name}}</td>
            <td>{{row.item.phone}}</td>
            <td>
                <v-btn class="mx-2" fab dark small color="pink" @click="onButtonClick(row.item)">
                    <v-icon dark>mdi-heart</v-icon>
                </v-btn>
            </td>
          </tr>
      </template>
    </v-data-table>
</template> -->

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
      },
      onButtonClick(item){
          console.log(item)
      }
    }
  }
</script>