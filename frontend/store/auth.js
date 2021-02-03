import api from '~api'

export const state = () => ({
  currentUser: undefined,
  cidade: ''
})

export const mutations = {
  setCurrentUser (state, user) {
    state.currentUser = user
  },
  setCidade (state, cidade) {
    state.cidade = cidade
  }
}

export const getters = {
  loggedIn (state) {
    return !!(state.currentUser && state.currentUser.user.permissions)
  }
}

export const actions = {
  async whoami ({ commit }) {
    const data = await api.whoami()
    if (data.authenticated) {
      commit('setCurrentUser', data.user)
      commit('setCidade', data.cidade)
    } else {
      commit('setCurrentUser', null)
      commit('setCidade', null)
    }
  }
}
