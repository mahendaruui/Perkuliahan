import DefaultTheme from 'vitepress/theme'
import FlipBookReader from './components/FlipBookReader.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('FlipBookReader', FlipBookReader)
  }
}
