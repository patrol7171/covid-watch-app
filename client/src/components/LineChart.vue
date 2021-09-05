<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    legendLabel: {
      type: String
    },
    labels: {
      type: Array
    },
    data: {
      type: Array
    },	
    options: {
      type: Object
    },
    chartColors: {
      type: Object
    }
  },
  mounted() {
    const {
      borderColor,
      backgroundColor
    } = this.chartColors;

    this.renderChart(
      {
        labels: this.labels,
        datasets: [{
          label: this.legendLabel,
          data: this.data,
          borderColor: borderColor,
          backgroundColor: backgroundColor
        }]
      },
      this.options
    );
  }
};
</script>
