<template>
  <ion-page>
    <ion-fab vertical="top" horizontal="end" slot="fixed">
      <ion-fab-button>
        <ion-icon :icon="add"></ion-icon>
      </ion-fab-button>
      <ion-fab-list side="bottom">
        <ion-fab-button href="/post/create">
          <ion-icon :icon="clipboard"></ion-icon>
        </ion-fab-button>
      </ion-fab-list>
    </ion-fab>
    <ion-content :fullscreen="true">
      <NewsFeedCard v-for="(number, idx) in numbers" :key="idx" />
    </ion-content>
  </ion-page>
</template>

<script>
import { defineComponent } from 'vue';
import { IonPage, IonContent, IonFab, IonFabButton } from '@ionic/vue';
import { add, clipboard } from 'ionicons/icons';
import NewsFeedCard from '@/components/NewsfeedCard.vue'

export default  defineComponent({
  name: 'Tab1Page',
  components: { IonContent, IonPage, IonFab, IonFabButton, NewsFeedCard },
  data () {
    return {
      numbers: [1, 2, 3, 4, 5, 6]
    }
  },
  setup () {
    return {
      add, clipboard
    }
  }
});
</script>
