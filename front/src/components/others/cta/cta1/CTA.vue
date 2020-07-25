<template>
  <div class="emergency-wrap">
    <div class="btn-box text-right">
      <h3 class="widget-title font-size-16 padding-bottom-15px text-white">
        {{title}}
      </h3>
      <a :href="'tel:'+number" class="template-btn contact-btn">
        <span class="btn-icon icon-element">
          <v-icon name="phone"></v-icon>
        </span>
        {{number}}
      </a>
    </div>
  </div>
</template>

<script>
    export default {
      name: "CTA",
      data() {
        return {
          title: 'Emergency Contact',
          number: '(91) 8547 632521'
        }
      }
    }
</script>

<style scoped>

</style>
