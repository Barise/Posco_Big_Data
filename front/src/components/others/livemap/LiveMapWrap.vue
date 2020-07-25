<template>
  <div class="row mt-5">
    <div class="col-lg-12">
      <div class="map-container">
        <LiveCovidMap />
        <h3 class="widget-title pt-3">
          {{caption}}
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
    import LiveCovidMap from "../../contact/maps/LiveCovidMap";
    export default {
      name: "LiveMapWrap",
      components: {LiveCovidMap},
      data() {
        return {
          caption: 'Note: If you want to see the data you hover on the red circle bubble'
        }
      }
    }
</script>

<style scoped>

</style>
