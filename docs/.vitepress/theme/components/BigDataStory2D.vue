<template>
  <StoryCanvas2D :story="story" :scenes="scenes" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import StoryCanvas2D from './StoryCanvas2D.vue'
import { stories, type StoryVariant } from './three/bigdata-story'
import { storyScenes } from './three/bigdata-scenes'

const props = defineProps<{ variant: StoryVariant }>()

const story = computed(() => stories[props.variant])
const scenes = computed(() => storyScenes[props.variant])
</script>
