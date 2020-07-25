<template>
  <div class="row mt-5">
    <div v-for="(team, index) in teams" v-bind:key="index" class="col-lg-6">
      <div class="team-item">
        <div class="team-avatar">
          <img v-bind:src="team.img" alt="team" />
          <div class="team-social">
            <ul class="social-links">
              <li
                v-for="(social, index) in team.socials"
                v-bind:key="index"
              ></li>
            </ul>
          </div>
        </div>
        <div class="team-detail">
          <h3 class="team__title">
            <router-link to="/team-single">{{ team.name }}</router-link>
          </h3>
          <p class="team__meta">{{ team.designation }}</p>
          <div class="section-block"></div>
          <p class="team__meta pt-3">{{ team.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyTeamList",
  data() {
    return {
      teams: [
        {
          img: require("@/assets/images/a03_th.jpg"),
          name: "강태훈",
          designation: "팀장",
          content: "발표",
        },
        {
          img: require("@/assets/images/a03_hc.jpg"),
          name: "최형찬",
          designation: "팀원",
          content: "데이터 분석",
        },
        {
          img: require("@/assets/images/a03_jh.jpg"),
          name: "이지현",
          designation: "팀원",
          content: "데이터 분석",
        },
        {
          img: require("@/assets/images/a03_teo.jpg"),
          name: "김태호",
          designation: "팀원",
          content: "Web",
        },
      ],
    };
  },
};
</script>

<style scoped>
.col-lg-6 {
  padding: 12px !important;
}
</style>
