<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>Total of COVID-19 Deaths in the US By State</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row" v-if="dataDeathTotals.length > 0">
			<line-chart
			  :legendLabel="legendLabelDeathTotals"
			  :labels="labelsDeathTotals"
			  :data="dataDeathTotals"
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
			legendLabelDeathTotals: '',
			labelsDeathTotals: [],
			dataDeathTotals: [],
			caseTotalsChartColors: {
				backgroundColor: 'rgba(240, 201, 41, 0.3)',
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
		const { data } = await axios.get("/totalUSCovidDeaths");
		this.legendLabelDeathTotals = data.legendLabel;
		this.labelsDeathTotals = data.labels;
		this.dataDeathTotals = data.data;
		this.timestamp = data.timestamp;
	}
};
</script>