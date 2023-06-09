# final-pjt

박소현  & 이병수 1학기 최종 프로젝트

# README

## 팀원 정보 및 업무 분담 내역

| 이병수          | 박소현   |
| --------------- | -------- |
| 팀장            | 팀원     |
| ERD             | Coummity |
| DB 설계 및 구축 | CSS      |
| 알고리즘 구현   | 발표     |



## 개발목표

유저에게 다양한 형태의 영화 추천 기능 구현

유저간의 자유로운 소통을 위한 커뮤니티 기능 구현

유저의 활동기록이 남는 개인 프로필 기능 구현

원활하고 깔끔한 형태의 웹 구현

### 개발환경

Django & Vue 2



## 목표 서비스 구현 및 실제 구현 정도

1. Account

   1-1 회원가입 / 로그인 / 로그아웃 / 회원탈퇴 / 비밀번호 변경

   - Token을 활용하여 회원가입 / 로그인 / 로그아웃 / 비밀번호 변경 구현
   - 추가 Serializer 이용하여 회원탈퇴 구현
   - 모델을 변경하여 회원가입 시 별도로 선호 장르를 3가지 수집하여 추후 알고리즘에 활용

   1-2 Error메시지

   - 회원 가입 시 입력내용이 형식에 맞지 않을 때 상황에 맞는 안내 문구 출력
   - 로그인이 불가능 한 경우 경고 문구 출력

2. Movie

   2-1 Carousel

   - 현재 영화관 상영작 중 인기 상영작 유튜브 예고편 재생

   2-2 영화 리스트

   - 자체 알고리즘을 통해 선별된 영화의 리스트를 Swiper로 출력

     * 2-2-1 top 20 tmdb의 popularity 기준 상위 20개

     * 2-2-2 현재 시각을 받아 시간대 별 해당하는 장르 추천 / 정렬 기준은 tmdb popularity 기준

     * 2-2-3 회원 가입 시 받은 유저의 선호 장르를 통해 선호 장르에 해당하는 영화 추천 / 정렬 기준은 tmdb popularity 기준

     * 2-2-4 사이트에서 평점을 준 유저가 5명 이상이며, 유저들의 평균 평점이 3.5점인 영화들에 대하여 추천

3. Community : 유저간 게시글과 댓글을 통한 자유로운 의견 교환을 위한 자유 게시판

   3-1 community

   - bootstrap table을 이용하여 구성
   - title을 통하여 article의 세부 정보페이지로 이동
   - article의 username을 통해 유저 정보 페이지로 이동

   3-2 article & comment

   - CRUD 구성을 기본적으로 제공하여 유저간의 자유로운 소통 구현
   - comment의 경우, 업데이트 형태를 요청 된 경우에만 수정모드로 토글하여 전체적인 가시성 향상

4. Profile :  유저의 활동 기록

   4-1 좋아하는 장르

   - 가입 시 입력한 장르 출력

   4-2 작성한 게시글

   - 유저가 작성한 게시글의 제목을 출력, 클릭시 해당 게시글로 이동

   4-3 좋아요를 남긴 게시글

   - 유저가 좋아요를 표시한 게시글의 제목을 출력, 클릭시 해당 게시글로 이동

   4-4 평점을 남긴 영화 리스트

   - 영화 중 평점을 남긴 영화 리스트를 swiper형식을 활용하여 출력 및  클릭 시 영화 세부정보 페이지로 이동

+목표와 달랐던 점

1. 알고리즘

   - 좋은 평점을 준 영화들과 비슷한 영화 추천 역 참조 모델 설계 실수로 인하여 시간 부족으로 인하여 미 구현

   → 보완 : 가입시 정해진 장르를 선택할 수 있게 하여 이와 관련된 알고리즘 구현

2. Home

   - 캐러샐 특성과 아이프레임 특성의 충돌로 인하여 깔끔한 유튜브 송출 화면 구현에 어려움을 겪음

   → 추후 swiper를 활용하여 구현을 해볼 예정

3. chrome 8.0 이상의 cookie 기본 설정 충돌로 인하여 콘솔에서 경고 발생

## 데이터베이스 모델링(ERD)

![Untitled__1_](/uploads/50eddeb0bdb47e4fc769b40956557674/Untitled__1_.png)

![Untitled__2_](/uploads/cfeaa5aeb0db9bc8f3e074a55f1d2d55/Untitled__2_.png)

## 영화 추천 알고리즘에 대한 기술적 설명

1. Django에서 현재 시간을 받아들여 현재 시간에 추천할 영화를 추천함 
   * 주말 / 평일 구분
   * 평일의 경우 새벽 / 아침 / 점심 / 저녁을 기준으로 4개의 시간대로 구분하여 각각에 맞는 장르에 해당하는 영화를 출력함
2. 회원가입 시 유저가 좋아하는 장르를 받아 인기도 상위 영화 순서중 좋아하는 장르가 포함된 영화 출력
3. 사이트 자체 회원들 중 일정 인원 수, 일정 평점 이상의 영화를 출력, 데이터가 모자랄 경우 tmdb 기준 상위 영화를 출력
   * 유저들의 정보가 충분히 모이지 않았을 경우 tmdb의 popularity 기준 상위 영화들을 출력할 수 있도록 설정

## 서비스 대표 기능에 대한 설명

1. Movie
   1. Carousel을 통한 현재 영화관 인기 상영작의 예고편 재생을 통하여,  트렌드 파악 및 기본적인 정보 제공
   2. 현재 시간에 맞는 영화 추천을 통하여, 사용경험 상향
   3. 유저들의 평가에 의해 추천되는 영화리스트, 이를 통해 함께 가꾸어 나가는 영화 정보 소통의 장이 될 수 있음.
2. Community
   * 유저간 자유로운 소통이 가능한 자유 게시판
3. Profile
   * 기본적인 유저의 정보를 파악
   * 본인의 프로필인 경우 비밀번호변경과 회원 탈퇴를 추가적으로 지원
