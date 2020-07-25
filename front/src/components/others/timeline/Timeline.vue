<template>
  <div class="row mt-5">
    <div class="col-lg-8 mx-auto">
      <div class="timeline-wrap">
        <ul class="road-map">
          <li class="happening" v-for="(item, index) in items" v-bind:key="index">
            <div class="happening-period">
              <p class="happening__desc">{{item.date}}</p>
            </div>
            <div class="happening-detail">
              <p class="happening__desc">{{item.title}}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Timeline",
  data() {
    return {
      items: [
        {
          date: "Dec 31",
          title: "China alerts who to several pneumonia cases"
        },
        {
          date: "Jan 7",
          title: "France confirms europe's first case"
        },
        {
          date: "Jan 11",
          title: "China announces first death"
        },
        {
          date: "Jan 13",
          title: "Who reports care in thailand the first outside china"
        },
        {
          date: "Jan 30",
          title: "Who declares outbreak a global health emergency"
        },
        {
          date: "Feb 2",
          title: "First death outside china recorded in the philippines"
        },
        {
          date: "Feb 7",
          title: "Chinese team & whistleblower li wenliang dies"
        },
        {
          date: "Feb 11",
          title: "Who names virus COVID-19"
        },
        {
          date: "Feb 14",
          title: "Egypt confirms africa's first case"
        }
      ]
    };
  }
};
</script>

<style scoped>
</style>
