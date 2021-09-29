<template>
  <div class="mb-5">
    <div class="circle-frame d-flex justify-content-center">
      <div class="circle position-absolute"></div>
    </div>
    <div class="d-flex justify-content-center position-relative">
      <div class="d-flex align-items-center justify-content-center frame">
        <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div id="banner-img1" class="carousel-item banner-img-display active">
              <div class="carousel-caption">
                <p class="content">또 보겠지만 그래도 편지 해 줘</p>
                <p class="content">기다리는 시간이 행복해지거든</p>
              </div>
            </div>
            <div id="banner-img2" class="carousel-item banner-img-display">
              <div class="carousel-caption">
                <p class="title">태양이 바다에 미광을 비추면 나는 너를 생각한다</p>
                <p class="title">희미한 달빛이 샘물 위에 떠있으면 나는 너를 생각한다</p>
              </div>
            </div>
            <div id="banner-img3" class="carousel-item banner-img-display">
              <div class="carousel-caption">
                <p class="content">잘 지내나요?</p>
                <p class="content">저는 잘 지내요</p>
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Banner',
}
</script>

<style scoped>
@font-face {
  font-family: 'Treegarden';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/naverfont_10@1.0/Treegarden.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.circle-frame {
  padding-bottom: 15px;
}

.circle{
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: rgb(255, 43, 43);
  box-shadow: 0px 2px 5px rgb(83, 83, 83);
  z-index: 1;
}

#carouselExampleControls.carousel.slide {
  width: 600px;
}

.frame {
  background-color: white;
  width: 650px;
  height: 460px;
  box-shadow: 0px 2px 5px rgb(114, 114, 114);
}

.banner-img-display {
  height: 400px;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
}

#banner-img1 {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/Dear John.jpg');
}

#banner-img2 {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/클래식.jpg');
}

#banner-img3 {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/러브레터.jpg');
}

.title {
  font-family: 'Treegarden';
  font-size: 25px;
  color: white;
  text-align: left;
}

.content {
  font-family: 'Treegarden';
  font-size: 35px;
  color: white;
  text-align: left;
}

</style>