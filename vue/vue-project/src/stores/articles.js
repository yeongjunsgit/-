import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useArticleStore = defineStore('articles', () => {
  const articles = ref([
    // {
    // title:'제목1',
    // content:'내용1'
    // },
    // {
    // title:'제목2',
    // content:'내용2'
    // },
    // {
    // title:'제목3',
    // content:'내용3'
    // },
    // {
    // title:'제목4',
    // content:'내용4'
    // },
  ])
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
 
    })
    .catch((err) => {
      console.log(err)
    })
    
  }
  
  return { articles,signUp }
})
