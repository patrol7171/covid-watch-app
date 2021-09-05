<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>Top Ten States for COVID-19 Death Totals</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row">		
			<div class="col-md-6" v-if="dataTop10TotalDeaths.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10TotalDeaths"
				  :labels="labelsTop10TotalDeaths"
				  :data="dataTop10TotalDeaths"
				  :options="chartOptions"
				  :chartColors="top10TotalDeathsChartColors"
				/>
			</div>			
			<div class="col-md-6" v-if="dataTop10NewDeaths.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10NewDeaths"
				  :labels="labelsTop10NewDeaths"
				  :data="dataTop10NewDeaths"
				  :options="chartOptions"
				  :chartColors="top10NewDeathsChartColors"
				/>
			</div>
		</div>		
	</div>
</template>

<script>
import axios from "axios";
import BarChart from '@/components/BarChart'

export default {
	components: {
		BarChart
	},
	data() {
		return {
			timestamp: '',
			legendLabelTop10TotalDeaths: '',
			labelsTop10TotalDeaths: [],
			dataTop10TotalDeaths: [],
			top10TotalDeathsChartColors: {
				backgroundColor: 'rgba(240, 201, 41, 0.4)',
				borderColor: 'rgba(255, 117, 26, 1)',
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
			},			
			legendLabelTop10NewDeaths: '',
			labelsTop10NewDeaths: [],
			dataTop10NewDeaths: [],
			top10NewDeathsChartColors: {
				backgroundColor: 'rgba(240, 201, 41, 0.4)',
				borderColor: 'rgba(255, 117, 26, 1)',
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
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
							maxRotation: 60,
							minRotation: 60,
						}
					}]
				},				
			}
		};
	},
	async created() {
		const { data } = await axios.get("/topTenUSCovidDeaths");
		this.legendLabelTop10TotalDeaths = data.legendLabel1;
		this.labelsTop10TotalDeaths = data.labels1;
		this.dataTop10TotalDeaths = data.data1;		
		this.legendLabelTop10NewDeaths = data.legendLabel2;
		this.labelsTop10NewDeaths = data.labels2;
		this.dataTop10NewDeaths = data.data2;
		this.timestamp = data.timestamp;
	}
};
</script>