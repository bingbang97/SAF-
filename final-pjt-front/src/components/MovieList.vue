<template>
	<swiper class="swiper" ref="mySwiper" 
		
		:options="swiperOptions" 
		@slideChange="slideChangeTransitionStart"
	>
		<MovieListItem
			v-for="movie in movies"
			:key="movie.id"
			:movie="movie"
		/>
	</swiper>
</template>


<script>
	import Vue from 'vue'
	import VueAwesomeSwiper from 'vue-awesome-swiper'
	import 'swiper/css/swiper.css'
	// import 'swiper/css/swiper.min.css'
	Vue.use(VueAwesomeSwiper);

	import {Swiper} from 'vue-awesome-swiper'

	import MovieListItem from '@/components/MovieListItem'

	export default {
		name: 'MovieList',
		components: {
			Swiper,
			MovieListItem,
		},
		methods: {
			slideChangeTransitionStart() {
				// console.log(this.swiper.activeIndex); //현재 index값 얻기
			}
		},
		props: {
			movies:Array,
		},
		data() {
			return {
				swiperOptions: {
					breakpoints: {
						1024: {
							slidesPerView: 8,
							spaceBetween: 10
						},
						800: {
							slidesPerView: 4,
							spaceBetween: 10
						},
						640: {
							slidesPerView: 3,
							spaceBetween: 10
						},
						320: {
							slidesPerView: 1,
							spaceBetween: 10
						}
					}                  
				},
			}
		},

		//참조하고 있는 값이 변경될 때마다 정의된 계산식에 따라 값을 출력
		computed: {
			swiper() {
				return this.$refs.mySwiper.$swiper;
			}
		},

		//el이 새로 생성된 vm.$el로 인스턴스가 마운트 된 직후
		mounted() {
			//console.log('Current Swiper instance object', this.swiper)
			//this.swiper.slideTo(3, 1000, false)
		}


	}
</script>

<style>
	.swiper {
		width:100%;
		padding:px 0;
		/* border:1px solid black; */
		border-radius:5px;
		box-shadow:0 0 20px transparent inset;
	}
</style>