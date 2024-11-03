<script setup lang="ts">
import { onMounted, ref } from 'vue';

defineProps<{
  msg: string
}>()

let userName = ref("Yaroslav")

function changeName(event: any) {
  userName.value = userName.value.toUpperCase();
  console.log("🚀 ~ changeName ~ userName:", userName);
  console.log('- event -', event.target);
  event.target.disabled = true
}


onMounted(() => {
  let h1 = document.querySelector('.h1');
  console.log("🚀 ~ onMounted ~ h1:", h1)
})
onMounted

let h2 = ref()
console.log("🚀 ~ h2:", h2);

onMounted(() => {
  console.log("🚀 ~ h2:", h2)
});
</script>

<template>
  <h1 class="h1 display-3 text-center mt-5">Welcom back, {{ userName }}</h1>

  <h2 ref="h2" class="h2 display-3 text-center mt-5">Lorem ipsum dolor sit amet.</h2>

  
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
