import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  signup (first_name, last_name, username, email, password) {
    return post('/api/signup', {first_name, last_name, username, email, password})
  },
  add_famoso (imagem, nome, descricao) {
    return post('/api/addfamoso', {imagem, nome, descricao})
  },
  add_cidade (imagem, nome, descricao) {
    return post('/api/addcidade', {imagem, nome, descricao})
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  umfamoso (nome) {
    return get(`/api/fnome/${nome}`)
  },
  umacidade (nome) {
    return get(`/api/cnome/${nome}`)
  },
  lista_famosos () {
    return get('/api/famosos')
  },
  lista_cidades () {
    return get('/api/cidades')
  },
  dawikipedia (nome) {
    return get(`/api/${nome}`)
  },
  localiza (famoso, cidade, data) {
    if (famoso !== '' && cidade !== '' && data === '') {
      return get(`/api/localiza/famoso=${famoso}/cidade=${cidade}`)
    } else if (famoso !== '' && cidade === '' && data !== '') {
      return get(`/api/localiza/famoso=${famoso}/data=${data}`)
    } else if (famoso === '' && cidade !== '' && data !== '') {
      return get(`/api/localiza/cidade=${cidade}/data=${data}`)
    }
  }
}
