import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
export const useArticleStore = defineStore('articles', () => {
  const router = useRouter()
  const myname = ref(null)
  const mypk = ref(null)
  const doSurvey = ref(null)
  const isLogin = ref(null)
  const token = ref(null)
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const signUp = function(payload){
    // 구조분해할당
    const {username, password1, password2, age, salary, money, nickname} = payload
    // console.log('store의 회원가입까지 왔습니다.',typeof(financial_products))
    // console.log(payload)
    axios({
      method:'post',
      url:`${API_URL}/dj-rest-auth/registration/`,
      // 단축 속성
      data:{
        username, password1, password2, age, salary, money, nickname
      }
    })
    .then((res) =>{
      console.log('회원가입 완료')
      console.log(res)
      router.push({name:'LoginView'})
      
    })
    .catch((err) => {
      console.log(err)
    })
    
  }

  const changeInfo = function(payload){
    // 구조분해할당
    const { age, salary, money, nickname} = payload

    axios({
      method:'put',
      url:`${API_URL}/accounts/user-detail/${myname.value}/`,
      // 단축 속성
      data:{
        age, salary, money, nickname
      }
      
    })
    .then((res) =>{
      console.log('수정 완료')
      console.log(res)
      router.push(`/profile/${myname}`)
      
    })
    .catch((err) => {
      console.log(err)
    })
    
  }


  const login = function (payload) {
    const { username, password } = payload
    // console.log('스토어도착')
    // console.log(username, password)
    axios ({
      method: 'post',
      url:`${API_URL}/dj-rest-auth/login/`,
      data: {
        username, password
      }
    })
    .then((res) => {
      // 로그인 후 토큰 값 저장
      console.log('로그인이 완료되었습니다.')
      isLogin.value = true
      token.value = res.data.key
      // 유저 데이터 가져오기
        axios ({
          method: 'get',
          url:`${API_URL}/dj-rest-auth/user/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
        .then((res) =>{
          console.log(res.data)
          myname.value = res.data.username
          mypk.value = res.data.pk
          isLogin.value=true

        })
        .catch((err) => {
          console.log(err)
        })
        console.log(res)
        // mypk.value = res.data.
        router.push({name:'HomeView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const logout = function(){
    axios ({
      method: 'post',
      url:`${API_URL}/dj-rest-auth/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res)=>{
      console.log('로그아웃 성공')
      myname.value = null
      mypk.value = null
      token.value = null
      isLogin.value = false
    })
    .catch((err)=>{
      console.log(err)
      window.alert('로그아웃 실패')
      window.alert(`${token.value}`)
    })
  }


  const changePassword = function(payload){
    const {new_password1,new_password2} = payload
    axios({
      method:'post',
      url:`${API_URL}/dj-rest-auth/password/change/`,
      data:{
        new_password1,new_password2
      },
      headers: {
        Authorization: `Token ${token.value}`
      }

    })
    .then((res)=> {
      console.log('비밀번호 변경 성공')
    })
    .catch((err)=>{
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
    // console.log(payload)
    axios({
      method: 'post',
      url: `${API_URL}/articles/lists/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        title: title,
        content: content,
        // user: mypk.value,
      },
    })
      .then((res) => {
        console.log(res)
        console.log('게시글이 작성되었습니다.')
        router.push({name:'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
        console.log(payload)
      })
  }
  
  const updateArticle = function (payload) {
    const { title, content, article_id, user, article_user } = payload
    if (user != article_user) {
      window.alert('님이 작성한 글이 아닙니다.')
    } else {
      axios({
        method: 'put',
        url: `${API_URL}/articles/manage/${article_id}/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
        data: {
          title: title,
          content: content,
          user: user,
        },
      })
        .then((res) => {
          console.log('게시글이 수정되었습니다.')
          router.push({name:'CommunityDetailView', params:article_id})
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
  
  const deleteArticle = function (payload) {
    const { article_id,article_user, user } = payload
    if (user !=article_user ) {
      window.alert('내가 작성한 글이 아닙니다.')
    } else {
    axios({
      method: 'delete',
      url: `${API_URL}/articles/manage/${article_id}/`,
      data: {
        user: user,
      },
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then((res) => {
      // console.log('왜안됨')
      // console.log(articles.value)
      // articles.value = articles.value.filter((item) => item.id !== article_id);

      console.log('게시글이 삭제되었습니다.')
      router.push({name:'CommunityView'})
    })
    .catch((err) => {
        console.log(articles.value)
        console.log(err)
      })
    }
  }

  const exchangedata = ref(null)
  const getExchangeData = function(){
    axios({
      method:'get',
      url:`${API_URL}/exchangerate/get_data/`
    })
    .then((res)=>{
      console.log('여기는 스토어')
      console.log(res.data)
      exchangedata.value=res.data.data
      
    })
    .catch((err)=>{
      console.log(err)
    })
  }
  
  const findPrdt = function(type,fin_prdt_cd){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/fin_prct/opject_${type}_product/${fin_prdt_cd}`
    })
    .then((res)=>{
      console.log('여기는 스토어')
      console.log(res.data)
      return res.data
    })
    .catch((err)=>{
      console.log('여기는 스토어 오류')
      console.log(err)
      return err
    })
  }

  const changeUserdetail = function(payload){
    const {username, password1, password2, age, salary, money, nickname} = payload
    axios({
      method:'put',
      url:`${API_URL}/dj-rest-auth/user-detail/${myname.value}/`,
      data:{
        username, password1, password2, age, salary, money, nickname
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res)=>{
      console.log(res.data)
    })
    .catch((err)=>{
      console.log(err)
    })
  }
  return { doSurvey,isLogin,articles, signUp, login, token, getArticles, API_URL,
    createArticles, myname, mypk, updateArticle, deleteArticle, getExchangeData, exchangedata,
    logout, findPrdt, changePassword, changeInfo}
}, { persist: true })
