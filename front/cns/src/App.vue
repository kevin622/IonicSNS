<template>
  <ion-app>
    <ion-router-outlet />
  </ion-app>
</template>

<script>
import { IonApp } from '@ionic/vue';
import { IonRouterOutlet } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  components: {
    IonApp,
    IonRouterOutlet
  }
});
</script>