<template>
  <v-list :items="items" two-line>
    <div class="aaaa">
      <span class="subtitulo">Cidades</span>
      <v-btn v-if="logged_user && logged_user.permissions.ADMIN" color="green" style="min-width:0px; width:25px; min-height:0px; height: 25px;" @click="open_add_cidade($event)"><v-icon>mdi-plus</v-icon></v-btn>
      <addcidade ref="add_cidade" />
    </div>
    <template v-for="(item, index) in items">
      <v-divider
        :key="index"
      />
      <v-list-item
        :key="item.title"
      >
        <v-list-item-avatar>
          <v-img :src="item.imagem" class="foto picture" />
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>
            <router-link :to="{name: 'nomedacidade', params: {nomedacidade: item.nome}}" class="nome name">
              {{item.nome}}
            </router-link>
          </v-list-item-title>
          <v-list-item-subtitle class="text texto">
            {{item.descricao}}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
  </v-list>
</template>

<script>

import addcidade from '~/components/add-cidade.vue'
import AppApi from '~api'

export default {
  components: {
    addcidade
  },
  data () {
    return {
      items: [],
      visible: false,
      loading: false,
      error: false
    }
  },
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  created () {
    AppApi.lista_cidades().then(response => {
      this.items = response
    })
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    open_add_cidade (evt) {
      this.$refs.add_cidade.open()
      evt.stopPropagation()
    }
  }
}

</script>

<style>
  .aaaa {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    margin-left: 10px;
  }
  .subtitulo {
    font-size: 34px;
    color: rgb(190, 190, 190);
    display: flex;
    align-items: center;
    margin-right: 10px;
  }
  .nome.name {
    font-size: 24px;
    text-decoration: none;
    color: white;
  }
  .text.texto {
    font-size: 18px;
  }
  .foto.picture {
    height: 100px;
  }
</style>
