<template>
  <v-dialog v-model="visible" max-width="1000px">
    <v-card>
      <v-card-title>Cadastrar cidade</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-text-field label="Nome da cidade" required v-model="nome" />
          <v-textarea outlined label="Breve descrição" required v-model="descricao" />
          <input style="margin-top: 10px;" type="file" @change="processFile($event)">
          <small class="erro" v-if="error">FALHOU</small>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn class="blue--text darken-1" text @click="close()">Cancelar</v-btn>
        <v-btn class="blue--text darken-1" text @click="add_cidade()" :loading="loading" :disabled="loading">Cadastrar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

import api from '~api'

export default {
  data () {
    return {
      visible: false,
      loading: false,
      imagem: '',
      nome: '',
      descricao: '',
      wikip: '',
      error: false
    }
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    processFile (event) {
      this.imagem = event.target.files[0]
    },
    add_cidade () {
      this.loading = true
      this.error = false
      const status = api.add_cidade(this.imagem, this.nome, this.descricao, this.wikip).then(() => {
        document.location.reload()
      })
      if (status) {
        this.close()
      } else {
        this.error = true
      }
      this.loading = false
    }
  }
}
</script>

<style scoped>
  .erro {
    color: rgb(225, 0, 255);
    font-size: 16px;
  }
</style>
