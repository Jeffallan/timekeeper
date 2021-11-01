<template>
  <div>
  <p class="player">{{ desc }}</p>
  <div :id=el_id class="player"></div>
  </div>
</template>

<script>
import Clappr from "clappr"
import Video360 from "clappr-video360"

export default {
  name: "Player",
  props: {
    desc: {
      type: String,
    },
    el_id: {
      type: String,
      default: "player",
      required: true,
    },
    source: {
      type: String,
      required: true,
      default: ""
    }
  },
  data: () => ({
      player: null,
    }),
  mounted(){
    var player = new Clappr.Player({
                        source: this.source, 
                        parentId: `#${this.el_id}`,
                        plugins: {
                           container: [Video360],
                            },
                        });
    
    this.player = player
    this.player.getPlugin('click_to_pause').disable();
    
  },
  beforeUnmount() {
      this.player.destroy();
      this.player = null;
    },
}
</script>

<style >
  .player {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  canvas { 
        height: auto !important;
        width: 100% !important;
        }
</style>