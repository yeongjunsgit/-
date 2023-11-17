import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
export const useArticleStore = defineStore('articles', () => {
  const router = useRouter()

  const token = ref(null)
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const signUp = function(payload){
    // 구조분해할당
    const {username,password1,password2} = payload
    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      // 단축 속성
      data:{
        username,password1,password2
      }
    })
    .then((res) =>{
      console.log('회원가입 완료')
      console.log(res)
      router.push({name:'HomeView'})
 
    })
    .catch((err) => {
      console.log(err)
    })
    
  }
  
  const login = function (payload) {
    const { username, password } = payload
    axios ({
      method: 'post',
      url:`${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인이 완료되었습니다.')
        console.log(token.value)
        token.value = res.data.key
        console.log(token.value)
        router.push({name:'HomeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/lists/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createArticles = function (payload) {
    const { title, content } = payload
    axios({
      method: 'post',
      url: `${API_URL}/articles/lists/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        title: title,
        content: content
      },
    })
      .then((res) => {
        console.log('게시글이 작성되었습니다.')
        router.push({name:'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { articles, signUp, login, token, getArticles, API_URL, createArticles }
}, { persist: true })
