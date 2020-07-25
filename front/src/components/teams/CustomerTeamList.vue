<template>
  <div class="row mt-5">
    <div v-for="(team, index) in teams" v-bind:key="index" class="col-lg-6">
      <div class="team-item">
        <div class="team-avatar">
          <img v-bind:src="team.img" alt="Team" />
          <div class="team-social">
            <ul class="social-links">
              <li v-for="(social, index) in team.socials" v-bind:key="index">
                <a v-bind:href="social.url">
                  <font-awesome-icon :icon="['fab', social.icon]" />
                </a>
              </li>
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
  name: "CustomerTeamList",
  data() {
    return {
      teams: [
        {
          img: require("@/assets/images/team.jpg"),
          name: "강태훈",
          designation: "Throat Specialist",
          content:
            "Libero perspiciatis sequi delectus, maxime, voluptatum minima nam amet ultrices",
          socials: [
            {
              icon: "facebook-f",
              url: "https://facebook.com",
            },
            {
              icon: "twitter",
              url: "https://twitter.com",
            },
            {
              icon: "linkedin-in",
              url: "https://linkedin.com",
            },
            {
              icon: "instagram",
              url: "https://instagram.com",
            },
          ],
        },
        {
          img: require("@/assets/images/team2.jpg"),
          name: "최형찬",
          designation: "Cardiologist",
          content:
            "Libero perspiciatis sequi delectus, maxime, voluptatum minima nam amet ultrices",
          socials: [
            {
              icon: "facebook-f",
              url: "https://facebook.com",
            },
            {
              icon: "twitter",
              url: "https://twitter.com",
            },
            {
              icon: "linkedin-in",
              url: "https://linkedin.com",
            },
          ],
        },
        {
          img: require("@/assets/images/team3.jpg"),
          name: "이지현",
          designation: "Rehabilitation Therapy",
          content:
            "Libero perspiciatis sequi delectus, maxime, voluptatum minima nam amet ultrices",
          socials: [
            {
              icon: "facebook-f",
              url: "https://facebook.com",
            },
            {
              icon: "twitter",
              url: "https://twitter.com",
            },
            {
              icon: "linkedin-in",
              url: "https://linkedin.com",
            },
            {
              icon: "instagram",
              url: "https://instagram.com",
            },
          ],
        },
        {
          img: require("@/assets/images/team4.jpg"),
          name: "김태호",
          designation: "Throat Specialist",
          content:
            "Libero perspiciatis sequi delectus, maxime, voluptatum minima nam amet ultrices",
          socials: [
            {
              icon: "facebook-f",
              url: "https://facebook.com",
            },
            {
              icon: "twitter",
              url: "https://twitter.com",
            },
            {
              icon: "linkedin-in",
              url: "https://linkedin.com",
            },
            {
              icon: "instagram",
              url: "https://instagram.com",
            },
          ],
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
