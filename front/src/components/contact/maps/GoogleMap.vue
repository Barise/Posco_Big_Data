<template>
  <div class="map-container">

    <GmapMap
      id="map"
      :center="{lat:40.712776, lng:-74.005974}"
      :zoom="12"
      map-type-id="terrain"
      :options="{
          styles: mapStyles
        }"
    >
      <GmapMarker
        ref="myMarker"
        :position="google && new google.maps.LatLng(40.712776, -74.005974)"
      />
    </GmapMap>
  </div>
</template>

<script>
  import { gmapApi } from "vue2-google-maps";

    export default {
      name: "GoogleMap",
      data() {
        return {
          mapStyles: [{
            "featureType": "water",
            "elementType": "geometry",
            "stylers": [{
              "color": "#e9e9e9"
            }, {
              "lightness": 17
            }]
          },
            {
              "featureType": "landscape",
              "elementType": "geometry",
              "stylers": [{
                "color": "#f5f5f5"
              },
                {
                  "lightness": 20
                }
              ]
            },
            {
              "featureType": "road.highway",
              "elementType": "geometry.fill",
              "stylers": [{
                "color": "#ffffff"
              },
                {
                  "lightness": 17
                }
              ]
            },
            {
              "featureType": "road.highway",
              "elementType": "geometry.stroke",
              "stylers": [{
                "color": "#ffffff"
              },
                {
                  "lightness": 29
                }, {
                  "weight": 0.2
                }
              ]
            },
            {
              "featureType": "road.arterial",
              "elementType": "geometry",
              "stylers": [{
                "color": "#ffffff"
              },
                {
                  "lightness": 18
                }
              ]
            },
            {
              "featureType": "road.local",
              "elementType": "geometry",
              "stylers": [{
                "color": "#ffffff"
              },
                {
                  "lightness": 16
                }
              ]
            },
            {
              "featureType": "poi",
              "elementType": "geometry",
              "stylers": [{
                "color": "#f5f5f5"
              },
                {
                  "lightness": 21
                }
              ]
            },
            {
              "featureType": "poi.park",
              "elementType": "geometry",
              "stylers": [{
                "color": "#dedede"
              },
                {
                  "lightness": 21
                }
              ]
            }, {
              "elementType": "labels.text.stroke",
              "stylers": [{
                "visibility": "on"
              }, {
                "color": "#ffffff"
              }, {
                "lightness": 16
              }]
            }, {
              "elementType": "labels.text.fill",
              "stylers": [{
                "saturation": 36
              }, {
                "color": "#333333"
              }, {
                "lightness": 40
              }]
            }, {
              "elementType": "labels.icon",
              "stylers": [{
                "visibility": "off"
              }]
            }, {
              "featureType": "transit",
              "elementType": "geometry",
              "stylers": [{
                "color": "#f2f2f2"
              }, {
                "lightness": 19
              }]
            }, {
              "featureType": "administrative",
              "elementType": "geometry.fill",
              "stylers": [{
                "color": "#fefefe"
              }, {
                "lightness": 20
              }]
            }, {
              "featureType": "administrative",
              "elementType": "geometry.stroke",
              "stylers": [{
                "color": "#fefefe"
              }, {
                "lightness": 17
              }, {
                "weight": 1.2
              }]
            }
          ]
        }
      },
      computed: {
        google: gmapApi
      }
    }
</script>

<style scoped>

</style>
