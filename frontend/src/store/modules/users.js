import axios from 'axios'
import { LOGIN, ME } from "@/util/constants/Urls"
import Router from "@/router/index"

const state = () => ({
    status:  null,
    token: "",
    user:  {}
  })

  const mutations = {
    auth_request(state){
      state.status = "loading"
    },
    auth_success(state, token, ){ //user
      state.status = "success"
      state.token = token
      //state.user = user
    },
    auth_error(state){
      state.status = "error"
    },
    logout(state){
      state.status = null
      state.token = ""
      state.user = {}
    },
    current_user(state, user){
        state.user = user
    }
  }
  const actions =  {
    login({commit, dispatch}, data) {
      return new Promise((resolve, reject) => {
        commit("auth_request")
        axios({url: LOGIN, data: data, method: "POST"})
        .then(r => {
          const token = r.data.auth_token
          //sessionStorage.setItem("token", token)
          axios.defaults.headers.common['Authorization'] = `Token ${token}`
          commit("auth_success", token)
          dispatch("getUserDetails")
          Router.push("/about")
          resolve(r)
        })
        .catch(e => {
          commit("auth_error")
          sessionStorage.removeItem("token")
          reject(e)
        })
      })
    },
    logout({commit}) {
      commit("logout")
      //sessionStorage.removeItem("token")
      //TODO token destroy
      delete axios.defaults.headers.common["Authorization"]
    },
    getUserDetails({commit}){
        return new Promise((resolve, reject) => {
            axios({url: ME, method: "GET"})
            .then(r => {
                commit("current_user", r.data)
                resolve(r)
            })
            .catch(e => {
                reject(e)
            })
        })
    }
  }
  const getters = {
    currentUser: state => {
        return state.user
    }
  }

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }
