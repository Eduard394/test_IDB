<template>
  <div class="d-flex flex-column justify-space-between align-center">
    <v-slider
      v-model="width"
      class="align-self-stretch"
      min="200"
      max="500"
      step="1"
    ></v-slider>

    <v-img
      :aspect-ratio="16/9"
      :width="width"
      src="@/assets/contacts.png"
    ></v-img>
  </div>
</template>

<script>
  export default {
    data: () => ({
      width: 600,
    }),
  }
</script>