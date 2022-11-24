<template>
	<swiper class="swiper" ref="mySwiper" 
		
		:options="swiperOptions" 
		@slideChange="slideChangeTransitionStart"
	>
		<ProfileMovieListItem
			v-for="movie in recommendMovies"
			:key="movie.movie"
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

	import ProfileMovieListItem from '@/components/ProfileMovieListItem'

	export default {
		name: 'MovieList',
		components: {
			Swiper,
			ProfileMovieListItem,
		},
		methods: {
			slideChangeTransitionStart() {
				// console.log(this.swiper.activeIndex); //현재 index값 얻기
			}
		},
		props: {
			recommendMovies:Array,
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
					},
					initialSlide : (this.recommendMovies.length) /2,
          // loop: true,
					centeredSlides: true,                  
				},
			}
		},

		//참조하고 있는 값이 변경될 때마다 정의된 계산식에 따라 값을 출력
		computed: {
			swiper() {
				return this.$refs.mySwiper.$swiper;
			}
		},
		created(){
			// console.log(this.recommendMovies.length)
			
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