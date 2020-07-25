<template>
  <div class="contact-item mb-4">
    <h3 class="widget-title font-size-20">Where We live</h3>
    <ul class="list-items mt-3">
      <li><span class="mr-1 font-weight-medium text-color">Address:</span>{{address}}</li>
      <li><span class="mr-1 font-weight-medium text-color">Email:</span><a href="#">{{email}}</a></li>
      <li><span class="mr-1 font-weight-medium text-color">Phone:</span><a href="#">{{number}}</a></li>
      <li><span class="mr-1 font-weight-medium text-color">Fax:</span><a href="#">{{fax}}</a></li>
    </ul>
  </div>
</template>

<script>
    export default {
      name: "ContactPlace",
      data() {
        return {
          address: "2750 Quadra Street Victoria, Canada.",
          email: "hello@example.com",
          number: "+44 587 154756",
          fax: "+55 785 4578964"
        }
      }
    }
</script>

<style scoped>

</style>
