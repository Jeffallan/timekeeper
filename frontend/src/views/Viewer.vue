<template>
<div>
<h1 class="text-center">Viewer</h1>
  <div class="">
    <Player desc="camera name"
            source="https://dm0qx8t0i9gc9.cloudfront.net/watermarks/videoNIHmZbghlilb1qj7b/videoblocks-vr-360-asteroid-in-space-fly-to-earth-virtual-reality-video-elements-of-this-image-furnished-by-nasa_SyM_7GcTe__79f08c24e047d1fb1798f870a370cfcf__P640.mp4"/>
  </div>
</div>
  
</template>

<script>

import Player from "@/components/Player.vue"

export default {
    name: "Viewer", 
        components: {
            Player
        },

}
</script>

<style scoped>
    
</style>