<template>
  <div>
    <h1>{{nomedacidade}}</h1>
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
      nomedacidade: context.params.nomedacidade
    }
  },
  created () {
    AppApi.umacidade(this.nomedacidade).then(response => {
      this.items = response.wikip
      if (this.items === null) {
        AppApi.dawikipedia(this.nomedacidade).then(response => {
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
