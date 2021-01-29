<template>
  <div class="corpo">
    <div class="divisao">
      <h1 class="titulo">Sobre o</h1>
      <h2 class="titulo2">&nbsp;Famass</h2>
    </div>
    <div>
      <p class="paragrafo">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Criado em 2021, durante um projeto do curso BuserCamp, Augusto teve a ideia de mostrar aos fãs os locais onde seus ídolos iriam passar, baseado em informações obtidas com seus acessores.
      </p>
    </div>
  </div>
</template>

<script>
</script>

<style>
  @font-face {
    font-family: 'Dancing Script';
    font-style: normal;
    font-weight: 400;
    src: local('Dancing Script'), local('Dancing Script'),
          url('https://fonts.gstatic.com/s/dancingscript/v15/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7B1i03Sup8.woff2') format('woff2');
    }
  .titulo {
    color: #ffffff;
    font-size: 36px;
    font-weight: 400;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    }
    .titulo2 {
    color: #ffffff;
    font-size: 44px;;
    font-family: 'Dancing Script';
    font-weight: 700;
    display: flex;
    justify-content: center;
    align-items: center;
    }
  .corpo {
    display: flex;
    flex-direction: column;
  }
  .paragrafo {
    margin-top: 30px;
    padding: 5px;
    font-size: 20px;
  }
  .divisao {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
</style>
