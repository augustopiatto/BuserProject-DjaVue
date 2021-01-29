<template>
  <v-app id="inspire">
    <toolbar />
    <v-content>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <lefooter />
  </v-app>
</template>

<script>

import toolbar from '~/components/toolbar.vue'
import lefooter from '~/components/lefooter.vue'

export default {
  components: {
    toolbar,
    lefooter
  },
  data: () => ({
  })
}
</script>
