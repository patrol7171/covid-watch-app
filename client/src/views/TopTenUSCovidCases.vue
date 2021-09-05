<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>Top Ten States for COVID-19 Case Totals</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row">		
			<div class="col-md-6" v-if="dataTop10TotalCases.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10TotalCases"
				  :labels="labelsTop10TotalCases"
				  :data="dataTop10TotalCases"
				  :options="chartOptions"
				  :chartColors="top10TotalCasesChartColors"
				/>
			</div>			
			<div class="col-md-6" v-if="dataTop10NewCases.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10NewCases"
				  :labels="labelsTop10NewCases"
				  :data="dataTop10NewCases"
				  :options="chartOptions"
				  :chartColors="top10NewCasesChartColors"
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
			legendLabelTop10TotalCases: '',
			labelsTop10TotalCases: [],
			dataTop10TotalCases: [],
			top10TotalCasesChartColors: {
				backgroundColor: 'rgba(172, 13, 13, 0.4)',
				borderColor: 'rgba(255, 117, 26, 1)',
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
			},			
			legendLabelTop10NewCases: '',
			labelsTop10NewCases: [],
			dataTop10NewCases: [],
			top10NewCasesChartColors: {
				backgroundColor: 'rgba(172, 13, 13, 0.4)',
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
		const { data } = await axios.get("/topTenUSCovidCases");
		this.legendLabelTop10TotalCases = data.legendLabel1;
		this.labelsTop10TotalCases = data.labels1;
		this.dataTop10TotalCases = data.data1;		
		this.legendLabelTop10NewCases = data.legendLabel2;
		this.labelsTop10NewCases = data.labels2;
		this.dataTop10NewCases = data.data2;
		this.timestamp = data.timestamp;		
	}
};
</script>