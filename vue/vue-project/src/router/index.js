import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import NearBankView from '@/views/NearBankView.vue'
import ExCalculView from '@/views/ExCalculView.vue'
import DepositSavingsRateView from '@/views/DepositSavingsRateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
      path: '/exchange',
      name: 'ExCalculView',
      component: ExCalculView
    },
    {
      path: '/rate',
      name: 'DepositSavingsRateView',
      component: DepositSavingsRateView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
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
   
  ]
})

export default router
