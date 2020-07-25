<template>
  <div class="accordion-wrap">
    <BulmaAccordion
      :dropdown="false"
      :icon="'custom'"
      :caretAnimation="{
        duration: '.2s',
        timerFunc: 'ease-in-out'
    }"
      :slide="{
        duration: '.2s',
        timerFunc: 'ease'
    }"
    >
      <!-- The wrapper component for all the items -->
      <BulmaAccordionItem v-for="(item, index) in items" v-bind:key="index">
        <h4 slot="title">
          {{item.title}} <span class="plus"><vue-icon name="plus"></vue-icon></span>
        </h4>
        <div slot="content" class="card-body">
          {{item.content}}
        </div>
      </BulmaAccordionItem>
    </BulmaAccordion>
  </div>
</template>

<script>
  import { BulmaAccordion, BulmaAccordionItem } from 'vue-bulma-accordion';

    export default {
      name: "Accordion",
      data() {
        return {
          items: [
            {
              title: "What is a novel coronavirus?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            },
            {
              title: "How Is This Coronavirus Spread?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            },
            {
              title: "What Are The Symptoms Of COVID-19?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            },
            {
              title: "Should I wear a mask to protect myself?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            },
            {
              title: "Should I Be Tested For COVID-19?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            },
            {
              title: "What is the source of the virus?",
              content: "Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.Proce Aran Manu Proucs Rahe Conen Cuve Manu Produ Rahe Cuvaes Man",
            }
          ]
        }
      },
      components: {
        BulmaAccordion,
        BulmaAccordionItem
      }
    }
</script>

<style scoped>

</style>
