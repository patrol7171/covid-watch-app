<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>Total of COVID-19 Tests in the US By State</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row" v-if="dataTestTotals.length > 0">
			<line-chart
			  :legendLabel="legendLabelTestTotals"
			  :labels="labelsTestTotals"
			  :data="dataTestTotals"
			  :options="chartOptions"
			  :chartColors="caseTotalsChartColors"
			/>
		</div>			
	</div>
</template>

<script>
import axios from "axios";
import LineChart from '@/components/LineChart'

export default {
	components: {
		LineChart
	},
	data() {
		return {
			timestamp: '',
			legendLabelTestTotals: '',
			labelsTestTotals: [],
			dataTestTotals: [],
			caseTotalsChartColors: {
				backgroundColor: 'rgba(217, 118, 66, 0.3)',
				borderColor: 'rgba(255, 117, 26, 1)',
			},						
			chartOptions: {
				responsive: true,
				maintainAspectRatio: false,
				scales: {
					yAxes: [{
						ticks: {
							beginAtZero: true,
							autoSkip: false,
						},
							gridLines: {
							display: true
						}
					}],
					xAxes: [{
						gridLines: {
							display: true,
						},
						ticks: {
							stepSize: 1,
							autoSkip: false,
							maxRotation: 65,
							minRotation: 65,
						}
					}]
				},				
			}
		};
	},
	async created() {
		const { data } = await axios.get("/totalUSCovidTests");
		this.legendLabelTestTotals = data.legendLabel;
		this.labelsTestTotals = data.labels;
		this.dataTestTotals = data.data;	
		this.timestamp = data.timestamp;
	}
};
</script>