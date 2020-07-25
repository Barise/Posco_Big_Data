<template>
  <div class="footer-widget">
    <h3 class="widget-title">{{ title }}</h3>
    <div class="section-divider"></div>
    <ul class="list-items">
      <li>
        <span class="mr-1 font-weight-medium text-color">Address:</span>
        {{ address }}
      </li>
      <li>
        <span class="mr-1 font-weight-medium text-color">Email:</span>
        <a v-bind:href="'mailto:' + email">{{ email }}</a>
      </li>
      <li>
        <span class="mr-1 font-weight-medium text-color">Phone:</span>
        <a v-bind:href="'tel:' + number">{{ number }}</a>
      </li>
      <li>
        <span class="mr-1 font-weight-medium text-color">Fax:</span>
        <a v-bind:href="'tel:' + fax">{{ fax }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "FooterWidget4",
  data() {
    return {
      title: "Contact Us",
      address: "포항산업과학 연구소.",
      email: "PoscoA03@posco.com",
      number: "+010 3999 0952",
      fax: "+82 399 9909520",
    };
  },
};
</script>

<style scoped></style>
