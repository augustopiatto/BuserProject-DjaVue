<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-card-title>Cadastro</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-text-field label="Nome" required v-model="first_name" />
          <v-text-field label="Sobrenome" required v-model="last_name" />
          <v-text-field label="Cidade" required v-model="cidade" />
          <v-text-field label="Nome do usuário" required v-model="username" />
          <v-text-field label="E-mail" required v-model="email" />
          <v-text-field label="Senha" type="password" required v-model="password" @keyup.enter="signup()" />
          <small class="erro" v-if="error">Usuário já cadastrado</small>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn class="blue--text darken-1" text @click="close()">Cancelar</v-btn>
        <v-btn class="blue--text darken-1" text @click="signup()" :loading="loading" :disabled="loading">Cadastrar</v-btn>
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
      first_name: '',
      last_name: '',
      cidade: '',
      email: '',
      username: '',
      password: '',
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
    async signup () {
      this.loading = true
      this.error = false
      const user = await api.signup(this.first_name, this.last_name, this.cidade, this.username, this.email, this.password)
      if (user) {
        this.visible = false
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
