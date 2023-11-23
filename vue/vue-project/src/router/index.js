import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import NearBankView from '@/views/NearBankView.vue'
import ExCalculView from '@/views/ExCalculView.vue'
import RecommendView from '@/views/RecommendView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileFinChangeView from '@/views/ProfileFinChangeView.vue'
import ProfileSurveyView from '@/views/ProfileSurveyView.vue'
import ProfileAgeRecomView from '@/views/ProfileAgeRecomView.vue'
import ProfileSurveyRecomView from '@/views/ProfileSurveyRecomView.vue'
import LoginView from '@/views/LoginView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityCreateView from '@/views/CommunityCreateView.vue'
import CommunityUpdateView from '@/views/CommunityUpdateView.vue'
import RecomFinanPrdtView from '@/views/RecomFinanPrdtView.vue'
import RecomYearSavView from '@/views/RecomYearSavView.vue'
import RecomSavingPrdtView from '@/views/RecomSavingPrdtView.vue'
import RecomHomeLoanView from '@/views/RecomHomeLoanView.vue'
import RecomDepositLoanView from '@/views/RecomDepositLoanView.vue'
import DetailFinanView from '@/views/DetailFinanView.vue'
import DetailSavingView from '@/views/DetailSavingView.vue'
import DetailYearSavingView from '@/views/DetailYearSavingView.vue'
import DetailHomeLoanView from '@/views/DetailHomeLoanView.vue'
import DetailDepositLoanView from '@/views/DetailDepositLoanView.vue'


import { useArticleStore } from '@/stores/articles'
import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/community',
      name: 'CommunityView',
      component: CommunityView
    },
    {
      path: '/community/:id',
      name: 'CommunityDetailView',
      component: CommunityDetailView
    },
   
    {
      path: '/create',
      name: 'create',
      component: CommunityCreateView
    },

    {
      path: '/update/:id',
      name: 'update',
      component: CommunityUpdateView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        const article_id = to.params.id
        // console.log(store.token)
        const article = ref(null)

        axios({
          method: 'get',
          url: `${store.API_URL}/articles/lists/`,
          headers: {
            Authorization: `Token ${store.token}`
          }
        })
          .then((res) => {
            article.value = res.data.filter((data) => data.id === Number(article_id))

            const article_user = ref(null)
            const user = store.mypk
            article_user.value = article.value[0].user.id

            if (article_user.value != user) {
              window.alert('내가 작성한 글이 아닙니다.')
              router.push({ name: 'CommunityDetailView',params: article_id })
            }
            
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    {
      path: '/exchange',
      name: 'ExCalculView',
      component: ExCalculView
    },
    {
      path: '/rate',
      name: 'recommendView',
      component: RecommendView,
      children:[
        {
          path: '/finanprdt',
          name: 'RecomFinanPrdtView',
          component: RecomFinanPrdtView
        },
        {
          path: '/yearsave',
          name: 'RecomYearSavView',
          component: RecomYearSavView
        },
        {
          path: '/save',
          name: 'RecomSavingPrdtView',
          component: RecomSavingPrdtView
        },
        {
          path: '/homeloan',
          name: 'RecomHomeLoanView',
          component: RecomHomeLoanView
        },
        {
          path: '/depositloan',
          name: 'RecomDepositLoanView',
          component: RecomDepositLoanView
        },
      ]
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView,
      children: [{
           path: '/agerecommend/:age',
           name: 'ProfileAgeRecomView',
           component: ProfileAgeRecomView
         },
         {
          path: '/surveyrecommend',
          name: 'ProfileSurveyRecomView',
          component: ProfileSurveyRecomView
        },]

    },
    {
      path: '/profile/:id',
      name: 'ProfileFinChangeView',
      component: ProfileFinChangeView
    },
    {
      path: '/profile/survey',
      name: 'ProfileSurveyView',
      component: ProfileSurveyView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/nearbank',
      name: 'NearBankView',
      component: NearBankView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path: '/finan_prdt/:fin_prdt_cd',
      name: 'DetailFinanView',
      component: DetailFinanView
    },
    {
      path: '/saving_prdt/:fin_prdt_cd',
      name: 'DetailSavingView',
      component: DetailSavingView
    },
    
    {
      path: '/yearsaving_prdt/:fin_prdt_cd',
      name: 'DetailYearSavingView',
      component: DetailYearSavingView
    },

    {
      path: '/homeloan_prdt/:fin_prdt_cd',
      name: 'DetailHomeLoanView',
      component: DetailHomeLoanView
    },

    {
      path: '/depositloan_prdt/:fin_prdt_cd',
      name: 'DetailDepositLoanView',
      component: DetailDepositLoanView
    },
    
    
    
   
  ]
})

export default router
