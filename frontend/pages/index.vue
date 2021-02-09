<template>
  <div class="main">
    <div>
      <h1 class="textinho">Bem vindo(a) ao FAMASS!<br> Aqui você pode encontrar o seu ídolo quando desejar!!!</h1>
    </div>
    <v-layout class="corpoprincipal">
      <div class="i-container">
        <div class="i-icon-start">
          <v-icon color="black">mdi-magnify</v-icon>
        </div>
        <input type="text" id="pesquisa_famoso" v-model="fam" placeholder="Digite o famoso" class="i-field">
      </div>
      <div class="i-container">
        <div class="i-icon-start">
          <v-icon color="black">mdi-magnify</v-icon>
        </div>
        <input type="text" id="pesquisa_cidade" v-model="cid" placeholder="Digite a cidade" class="i-field">
      </div>
      <div class="i-container">
        <div class="i-icon-start">
          <v-icon color="black">mdi-magnify</v-icon>
        </div>
        <v-menu
          ref="menu1"
          v-model="menu1"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              clearable
              color="black"
              style="margin-top: 0px;"
              class="i-field"
              v-model="dateFormatted"
              v-bind="attrs"
              @blur="date = parseDate(dateFormatted)"
              v-on="on"
            />
          </template>
          <v-date-picker
            color="black"
            v-model="date"
            no-title
            @input="menu1 = false"
          >
            <v-btn
              text color="white" @click="menu1 = false"
            >
              Cancel
            </v-btn>
            <v-spacer />
            <v-btn
              text color="white" @click="clear()"
            >
              Clear
            </v-btn>
          </v-date-picker>
        </v-menu>
      </div>
    </v-layout>
    <div class="corporesto">
      <v-btn color="black" class="botao preto" @click="pesquisar()">
        Pesquisar
      </v-btn>
      <label class="resultado" v-for="localiza in resultado" :key="localiza.data">
        {{localiza.famoso}} estará em {{localiza.cidade}} no dia {{(new Date(localiza.data).getDate()+1)+'/'+((new Date(localiza.data).getMonth()+1).toString().length === 1 ? '0'+ (new Date(localiza.data).getMonth()+1) : new Date(localiza.data).getMonth()+1)+'/'+new Date(localiza.data).getFullYear()}}
      </label>
    </div>
  </div>
</template>

<script>

import AppApi from '~api'

export default {
  data: vm => ({
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false,
    menu2: false,
    visible: false,
    fam: '',
    cid: '',
    date: '',
    resultado: ''
  }),
  computed: {
    computedDateFormatted () {
      return this.formatDate(this.date)
    }
  },
  watch: {
    date (val) {
      this.dateFormatted = this.formatDate(this.date)
    }
  },
  methods: {
    clear () {
      this.date = ''
    },
    formatDate (date) {
      if (!date) {
        return null
      }
      const [year, month, day] = date.split('-')
      return `${day}/${month}/${year}`
    },
    parseDate (date) {
      if (!date) {
        return null
      }
      const [month, day, year] = date.split('/')
      return `${year}-${day.padStart(2, '0')}-${month.padStart(2, '0')}`
    },
    pesquisar () {
      AppApi.localiza(this.fam, this.cid, this.date)
        .then(result => {
          this.resultado = result
        })
    },
    change () {
      if (this.visible === true) {
        this.visible = false
      } else {
        this.visible = true
      }
    }
  }
}
</script>

<style>
  #input-45 {
    color: rgb(120, 120, 120);
    margin-top: -5px;
  }
  .main {
    height: 75vh;
  }
  .textinho {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    height: 15%;
    text-align: center;
  }
  .corpoprincipal {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    height: 15%;
    margin-top: 20px;
  }
  .corporesto {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    height: 65%;
  }
  .botao.preto {
    display: flex;
    margin-top: 40px;
    height: 60px;
    width: 150px;
    background-color: black;
  }
  .resultado {
    margin-top: 30px;
    font-size: 26px;
    color: white;
  }
  .i-container {
    position: relative;
    vertical-align: baseline;
    box-sizing: border-box;
    font-family: Roboto,sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: normal;
  }
  .i-icon-start {
    align-items: center;
    display: flex;
    justify-content: center;
    height: 100%;
    position: absolute;
    padding: 10px;
    vertical-align: baseline;
    box-sizing: border-box;
  }
  .i-field {
    padding-left: 40px;
    background-color: #fff;
    border-radius: 5px;
    height: 44px;
    overflow: hidden;
    width: 100%;
    color: #000000;
    box-sizing: border-box;
    font-family: Roboto,sans-serif;
    font-size: 16px;
    font-weight: 400;
    display: inline-block;
    text-align: start;
    appearance: textfield;
  }
</style>
