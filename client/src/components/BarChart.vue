<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
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
      backgroundColor,
	  pointBorderColor,
      borderWidth,  
    } = this.chartColors;

    this.renderChart(
      {
        labels: this.labels,
        datasets: [{
          label: this.legendLabel,
          data: this.data,
          borderColor: borderColor,
          backgroundColor: backgroundColor,
		  pointBorderColor: pointBorderColor,
		  borderWidth: borderWidth			
       }]
      },
      this.options
    );
  }
};  
</script>