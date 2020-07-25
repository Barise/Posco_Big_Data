<template>
  <div class="contact-item mt-4 mb-4">
    <h3 class="widget-title font-size-20">Opening Hours</h3>
    <ul class="list-items mt-3">
      <li v-for="(list, index) in lists" v-bind:key="index"><span class="mr-1 font-weight-medium text-color">{{list.weekName}}:</span> {{list.time}}</li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "ContactHours",
      data() {
        return {
          lists: [
            {
              weekName: "Monday",
              time: "8AM - 6AM"
            },
            {
              weekName: "Tuesday",
              time: "8AM - 6AM"
            },
            {
              weekName: "Wednesday",
              time: "8AM - 6AM"
            },
            {
              weekName: "Thursday",
              time: "8AM - 6AM"
            },
            {
              weekName: "Friday - Sunday",
              time: "Closed"
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
