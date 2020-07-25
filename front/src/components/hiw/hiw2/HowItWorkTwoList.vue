<template>
  <div class="row mt-5">

    <div class="col-lg-4 column-td-6" v-for="(item, index) in items" v-bind:key="index">
      <div class="info-box info-box-layout-3">
        <div class="info__icon">
          <img :src="item.img" alt="How It Work">
        </div>
        <h3 class="info__title">{{item.title}}</h3>
        <span class="info__number">{{item.number}}</span>
      </div>
    </div>

  </div>
</template>

<script>
    export default {
      name: "HowItWorkTwoList",
      data() {
        return {
          items: [
            {
              img: require('@/assets/images/wash-hand-img-1.png'),
              title: 'Wet Hands',
              number: '01'
            },
            {
              img: require('@/assets/images/wash-hand-img-2.png'),
              title: 'Apply Soup',
              number: '02'
            },
            {
              img: require('@/assets/images/wash-hand-img-3.png'),
              title: 'Rub Palm to palm',
              number: '03'
            },
            {
              img: require('@/assets/images/wash-hand-img-4.png'),
              title: 'Lather The Back of Both Hands',
              number: '04'
            },
            {
              img: require('@/assets/images/wash-hand-img-5.png'),
              title: 'Rub The Back of Fingers on The Opposing Palm',
              number: '05'
            },
            {
              img: require('@/assets/images/wash-hand-img-6.png'),
              title: 'Base of Thumbs',
              number: '06'
            },
            {
              img: require('@/assets/images/wash-hand-img-7.png'),
              title: 'Wash Fingernails And Fingertips',
              number: '07'
            },
            {
              img: require('@/assets/images/wash-hand-img-8.png'),
              title: 'Rinse Hands',
              number: '08'
            },
            {
              img: require('@/assets/images/wash-hand-img-9.png'),
              title: 'Use The Towel to Rurn off The Foucet',
              number: '09'
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
