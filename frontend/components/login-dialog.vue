<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-card-title>Entrar</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-text-field label="Nome do usuário" required v-model="username" />
          <v-text-field label="Senha" type="password" required v-model="password" @keyup.enter="login()" />
          <small class="erro" v-if="error">Usuário ou senha errado</small>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn class="blue--text darken-1" text @click="close()">Cancelar</v-btn>
        <v-btn class="blue--text darken-1" text @click="login()" :loading="loading" :disabled="loading">Entrar</v-btn>
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
    async login () {
      this.loading = true
      this.error = false
      const profile = await api.login(this.username, this.password)
      if (profile) {
        this.$store.commit('auth/setCurrentUser', profile.user)
        this.$store.commit('auth/setCidade', profile.cidade)
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
