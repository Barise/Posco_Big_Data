<template>
  <div class="comments-wrap mt-5">
    <h2 class="widget-title font-size-22">4 Comments</h2>
    <div class="title-shape"></div>
    <ul class="comments-list padding-top-40px">
      <li>
        <div v-for="(comment, index) in comments" v-bind:key="index" :class="'comment comments-'+comment.reply">
          <img class="avatar__img" alt="Comment" :src="comment.img">
          <div class="comment-body">
            <div class="meta-data">
              <span class="comment__author">
                {{comment.name}}
              </span>
              <span class="comment__date">
                {{comment.date}}
              </span>
            </div>
            <p class="comment-content">
              {{comment.content}}
            </p>
            <div class="comment-reply d-flex justify-content-between align-items-center">
              <a class="template-btn comment__btn" href="#">
                <font-awesome-icon :icon="['fas', 'reply']"></font-awesome-icon> Reply
              </a>
            </div>
          </div>
        </div><!-- end comment -->
      </li>
    </ul>
    <div class="btn-box padding-top-20px text-center">
      <Button url="#" title="Load More" />
    </div><!-- end btn-box -->
  </div>
</template>

<script>
    import Button from "../../common/Button";
    export default {
      name: "CommentLists",
      components: {
        Button
      },
      data() {
        return {
          comments: [
            {
              img: require("@/assets/images/small-team1.jpg"),
              name: "Adam Smith",
              date: "17 Dec, 2018 - 4:00 AM",
              content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. Curabitur non nulla sit amet nisl tempus",
              reply: ""
            },
            {
              img: require("@/assets/images/small-team2.jpg"),
              name: "Julian Smith",
              date: "17 Dec, 2018 - 4:00 AM",
              content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. Curabitur non nulla sit amet nisl tempus",
              reply: "reply"
            },
            {
              img: require("@/assets/images/small-team3.jpg"),
              name: "Matt Derry",
              date: "17 Dec, 2018 - 4:00 AM",
              content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. Curabitur non nulla sit amet nisl tempus",
              reply: ""
            }
          ]
        }
      }
    }
</script>

<style scoped>

</style>
