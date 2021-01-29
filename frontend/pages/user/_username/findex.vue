<template>
  <div>
    <h1>{{nomedofamoso}}</h1>
    <p>{{content}}</p>
  </div>
</template>

<script>

import AppApi from '~api'

export default {
  data () {
    return {
      content: '',
      items: ''
    }
  },
  asyncData (context) {
    return {
      nomedofamoso: context.params.nomedofamoso
    }
  },
  created () {
    AppApi.umfamoso(this.nomedofamoso).then(response => {
      this.items = response.wikip
      if (this.items === null) {
        AppApi.dawikipedia(this.nomedofamoso).then(response => {
          this.content = response.content
        })
      } else {
        this.content = this.items
      }
    })
  }
}
</script>

<style>
</style>
