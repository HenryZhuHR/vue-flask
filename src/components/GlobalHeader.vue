<template>
  <div>{{title}}</div>
</template>

<script>
export default {
    name: 'AppHeader',
    data() {
        return {
            defaultitle: "Hello Vue!"
        }
    },
    props: {
        title: {
            type: String,
            default:'人工智能'
        }
    }
}
</script>

<style>

</style>