<template>
  <div class="main">
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
        <input type="text" id="pesquisa_data" v-model="dat" placeholder="Digite a data" class="i-field">
      </div>
    </v-layout>
    <div class="corporesto">
      <v-btn color="black" class="botao preto" @click="pesquisar()">
        Pesquisar
      </v-btn>
      <label class="resultado" v-for="localiza in resultado" :key="localiza.data">
        {{localiza.famoso}} estará em {{localiza.cidade}} no dia {{localiza.data}}
      </label>
    </div>
  </div>
</template>

<script>

import AppApi from '~api'

export default {
  data () {
    return {
      fam: '',
      cid: '',
      dat: '',
      resultado: ''
    }
  },
  methods: {
    pesquisar () {
      AppApi.localiza(this.fam, this.cid, this.dat)
        .then(result => {
          this.resultado = result
        })
    }
  }
}
</script>

<style>
  .main {
    height: 80vh;
  }
  .corpoprincipal {
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    height: 35%;
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
    display: block;
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
