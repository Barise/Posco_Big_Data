<template>
  <div class="footer-widget">
    <h3 class="widget-title">
      {{title}}
    </h3>
    <div class="section-divider"></div>
    <ul class="list-items">
      <li v-for="(link, index) in links" v-bind:key="index"><a v-bind:href="link.url">{{link.list}}</a></li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "FooterWidget3",
      data() {
        return {
          title: 'Useful links',
          links: [
            {
              list: 'Situation Reports',
              url: '#'
            },
            {
              list: 'Advice For Public',
              url: '#'
            },
            {
              list: 'Prevention',
              url: '#'
            },
            {
              list: 'Coronavirus Symptoms',
              url: '#'
            },
            {
              list: 'Donor & Partners',
              url: '#'
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
