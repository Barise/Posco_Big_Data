<template>
  <div class="service-item pr-4">
    <h3 class="widget-title padding-bottom-15px">
      {{title}}
    </h3>
    <ul class="list-items">
      <li v-for="(list, index) in lists" v-bind:key="index">{{list.title}}</li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "AboutOneLeft",
      data() {
        return {
          title: 'When and how to use masks',
          lists: [
            {
              title: 'Praesent laoreet sit amet nunc sed porttitor. In felis est, interdum ac lorem ut, volutpat venenatis ante'
            },
            {
              title: 'Etiam sodales tincidunt nibh, at vestibulum massa molestie nec.'
            },
            {
              title: 'Proin ullamcorper nunc sed finibus aliquam. Etiam semper velit quis tellus scelerisque, ut auctor nulla vestibulum.'
            },
            {
              title: 'Maecenas eget nibh sed odio commodo convallis. Sed rutrum arcu non tortor porttitor'
            },
            {
              title: 'Nam nec libero nulla. Aenean euismod leo eu eros sollicitudin'
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
