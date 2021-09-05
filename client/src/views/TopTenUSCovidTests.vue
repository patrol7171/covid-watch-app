<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>Top Ten States for COVID-19 Test Totals</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row">		
			<div class="col-md-6" v-if="dataTop10TotalTests.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10TotalTests"
				  :labels="labelsTop10TotalTests"
				  :data="dataTop10TotalTests"
				  :options="chartOptions"
				  :chartColors="top10TotalTestsChartColors"
				/>
			</div>			
			<div class="col-md-6" v-if="dataTop10NewTests.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10NewTests"
				  :labels="labelsTop10NewTests"
				  :data="dataTop10NewTests"
				  :options="chartOptions"
				  :chartColors="top10NewTestsChartColors"
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
			legendLabelTop10TotalTests: '',
			labelsTop10TotalTests: [],
			dataTop10TotalTests: [],
			top10TotalTestsChartColors: {
				backgroundColor: 'rgba(245, 156, 108, 0.4)',
				borderColor: 'rgba(255, 117, 26, 1)',	
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
			},			
			legendLabelTop10NewTests: '',
			labelsTop10NewTests: [],
			dataTop10NewTests: [],
			top10NewTestsChartColors: {
				backgroundColor: 'rgba(245, 156, 108, 0.4)',
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
		const { data } = await axios.get("/topTenUSCovidTests");
		this.legendLabelTop10TotalTests = data.legendLabel1;
		this.labelsTop10TotalTests = data.labels1;
		this.dataTop10TotalTests = data.data1;		
		this.legendLabelTop10NewTests = data.legendLabel2;
		this.labelsTop10NewTests = data.labels2;
		this.dataTop10NewTests = data.data2;
		this.timestamp = data.timestamp;		
	}
};
</script>

