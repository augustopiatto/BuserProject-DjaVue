<template>
  <v-app-bar color="black" dark fixed app clipped-right>
    <v-toolbar-title>
      <span>
        <router-link :to="{name: 'index'}" class="texto">
          Famass
        </router-link>
      </span>
    </v-toolbar-title>
    <v-spacer />
    <v-btn height="100%" color="black" :to="{name: 'famosos'}"><v-icon class="icones">mdi-account-heart</v-icon>Famosos</v-btn>
    <v-btn height="100%" color="black" :to="{name: 'cidades'}"><v-icon class="icones">mdi-city</v-icon>Cidades</v-btn>
    <v-btn height="100%" color="black" :to="{name: 'sobre'}"><v-icon class="icones">mdi-information</v-icon>Sobre</v-btn>
    <v-btn v-if="!logged_user" height="100%" color="black" @click="open_login_dialog($event)">Entrar</v-btn>
    <v-btn v-if="!logged_user" height="100%" color="black" @click="open_signup_dialog($event)">Cadastrar</v-btn>

    <!-- <template v-slot:activator="{ on }"><v-btn v-on="on"> -->
    <v-menu v-if="logged_user" offset-y>
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on" class="ma-0 ml-5">
          <v-avatar size="36px">
            <img src="https://graph.facebook.com/4/picture?width=300&height=300">
          </v-avatar>
        </v-btn>
      </template>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-item>
            <v-list-item-avatar>
              <v-avatar>
                <img src="https://graph.facebook.com/4/picture?width=300&height=300">
              </v-avatar>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-item-title>
              <v-list-item-subtitle>{{logged_user.username}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider />
        <v-list>
          <v-list-item @click="logout()">
            <v-list-item-content>
              <v-list-item-title>Sair</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-menu>
    <login-dialog ref="login_dialog" />
    <signup-dialog ref="signup_dialog" />
  </v-app-bar>
</template>

<script>

import loginDialog from '~/components/login-dialog.vue'
import signupDialog from '~/components/signup-dialog.vue'
import Snacks from '~/helpers/Snacks.js'
import api from '~api'

export default {
  components: {
    loginDialog,
    signupDialog
  },
  props: ['state'],
  computed: {
    logged_user () {
      return this.$store.state.auth.currentUser
    }
  },
  methods: {
    open_login_dialog (evt) {
      this.$refs.login_dialog.open()
      evt.stopPropagation()
    },
    open_signup_dialog (evt) {
      this.$refs.signup_dialog.open()
      evt.stopPropagation()
    },
    async logout () {
      await api.logout()
      this.$store.commit('auth/setCurrentUser', null)
      Snacks.show(this.$store, {text: 'Até logo!'})
    }
  }
}
</script>

<style scoped>
  @font-face {
    font-family: 'Dancing Script';
    font-style: normal;
    font-weight: 400;
    src: local('Dancing Script'), local('Dancing Script'),
          url('https://fonts.gstatic.com/s/dancingscript/v15/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7B1i03Sup8.woff2') format('woff2');
  }
  .texto {
    color: #FFD700;
    font-size: 45px;
    text-align: left;
    background-color: black;
    font-family: 'Dancing Script';
    font-style: normal;
    font-weight: 700;
    text-decoration: none;
    }
    .icones {
      margin-right: 10px;
      display: flex;
      align-content: center;
    }
</style>
