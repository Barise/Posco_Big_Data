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
      name: "FooterWidget2",
      data() {
        return {
          title: 'Privacy & Tos',
          links: [
            {
              list: 'Advertiser agreement',
              url: '#'
            },
            {
              list: 'Developer agreement',
              url: '#'
            },
            {
              list: 'Privacy Policy',
              url: '#'
            },
            {
              list: 'Technology Privacy',
              url: '#'
            },
            {
              list: 'Acceptable user policy',
              url: '#'
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
