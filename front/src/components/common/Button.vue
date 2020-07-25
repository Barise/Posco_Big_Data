<template>
  <router-link v-bind:to="url" class="template-btn" :class="classname">
    {{title}}
  </router-link>
</template>

<script>
    export default {
      name: "Button",
      props: [ 'title', 'url', 'classname' ],
      data() {
        return {

        }
      },
      methods: {

      }
    }
</script>

<style scoped>

  .template-btn {
    text-transform: uppercase;
    background-color: #3CAAF7;
    color: #fff;
    font-weight: 500;
    letter-spacing: 0.1px;
    padding: 0 30px 0 30px;
    line-height: 53px;
    position: relative;
    z-index: 1;
    display: inline-block;
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    -ms-transition: all 0.3s;
    -o-transition: all 0.3s;
    transition: all 0.3s;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px; }
  .template-btn:hover {
    color: #fff;
    background-color: #2973CC; }

  .icon-btn {
    width: 110px;
    height: 110px;
    background-color: #3CAAF7;
    line-height: 110px;
    margin-top: 20px;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
    color: #fff;
    display: inline-block;
    font-size: 30px;
    position: relative;
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    -ms-transition: all 0.3s;
    -o-transition: all 0.3s;
    transition: all 0.3s; }
  .icon-btn:hover {
    background-color: #2973CC;
    color: #fff; }
</style>
