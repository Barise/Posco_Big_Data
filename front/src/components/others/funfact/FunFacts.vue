<template>
  <div class="row mt-5">
    <div
      class="col-lg-3"
      v-for="(funfact, index) in funfacts"
      v-bind:key="index"
    >
      <div v-bind:class="'counter-item counter-item-color-' + index">
        <h4 class="counter__title">
          <ICountUp
            :delay="funfact.delay"
            :endVal="funfact.endval"
            :options="{
              useEasing: true,
              useGrouping: true,
              separator: '',
              decimal: '',
              prefix: '',
              suffix: '',
            }"
          />
        </h4>
        <p class="counter__meta">
          {{ funfact.desc }}
        </p>
      </div>
      <!-- end counter-item -->
    </div>
    <!-- end col-lg-3 -->
  </div>
</template>

<script>
import ICountUp from "vue-countup-v2";

export default {
  name: "FunFacts",
  components: {
    ICountUp,
  },
  data() {
    return {
      funfacts: [
        {
          delay: 0,
          endval: 14938,
          desc: "현재 고객수",
        },
        {
          delay: 0,
          endval: 538,
          desc: "2분기 신규가입자",
        },
        {
          delay: 0,
          endval: 278,
          desc: "가입승인 대기자",
        },
        {
          delay: 0,
          endval: 78,
          desc: "혈액검사 대상자",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style scoped></style>
