<template>
  <v-list :items="items" two-line>
    <div class="aaaaa">
      <div class="feed">
        <span>
          ESTE É SEU FEED:
        </span>
      </div>
      <div>
        <span style="font-size: 34px; color: rgb(190, 190, 190); margin-left: 10px;">
          Os famosos que estarão em {{cidade}}
        </span>
      </div>
    </div>
    <template v-for="(item, index) in items">
      <v-divider
        :key="index"
      />
      <v-list-item
        :key="item.title"
      >
        <v-list-item-avatar>
          <v-img :src="item.fimagem" style="height: 70px; max-width: 100px; width: 70px;" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="nome name">
            {{item.famoso}}
          </v-list-item-title>
          <v-list-item-subtitle class="texti textin">
            Data: {{new Date(item.data).getDate()+'/'+((new Date(item.data).getMonth()+1).toString().length === 1 ? '0'+ (new Date(item.data).getMonth()+1) : new Date(item.data).getMonth()+1)+'/'+new Date(item.data).getFullYear()}}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
  </v-list>
</template>

<script>

import AppApi from '~api'

export default {
  components: {
  },
  data () {
    return {
      items: [],
      fam: '',
      cid: '',
      dat: ''
    }
  },
  computed: {
    cidade () {
      return this.$store.state.auth.cidade
    }
  },
  created () {
    AppApi.mypage(this.cidade).then(result => {
      this.items = result
    })
  }
}

</script>

<style>
  .aaaaa {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .nome.name {
    font-size: 24px;
    text-decoration: none;
    color: white;
  }
  .texti.textin {
    font-size: 18px;
    margin-left: 10px;
  }
  .feed {
    display: flex;
    justify-content: center;
    font-size: 40px;
    margin-left: 10px;
  }
</style>
