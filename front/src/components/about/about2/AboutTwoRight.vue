<template>
  <div class="service-item pl-4">
    <h3 class="widget-title padding-bottom-15px line-height-33">
      {{title}}
    </h3>
    <ul class="list-items">
      <li v-for="(list, index) in lists" v-bind:key="index">{{list.title}}</li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: "AboutTwoRight",
      data() {
        return {
          title: 'When and how to wear medical masks to protect against coronavirus',
          lists: [
            {
              title: 'Sit amet faucibus elit blandit. Integer non elit a magna tincidunt tincidunt. Nullam eleifend fermentum finibus.'
            },
            {
              title: 'Fusce varius et sem sed sollicitudin. Duis viverra, urna in mattis congue, ipsum tortor'
            },
            {
              title: 'Duis eget ligula convallis, feugiat sem quis, aliquam augue. Duis viverra aliquet erat. Pellentesque quis mattis sapien'
            },
            {
              title: 'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque fringilla.'
            },
            {
              title: 'Suspendisse vel nunc ligula. Cras hendrerit sit amet risus ut malesuada. In rutrum, erat sed porta lobortis, tellus libero pretium nunc'
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
