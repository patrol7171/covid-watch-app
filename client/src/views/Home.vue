<template>
	<div class="container">
		<div class="row mt-1">
			<div class="col">
				<h3>COVID-19 Top Ten Stats for the US</h3>
				<small class="fw-lighter fst-italic">Last updated: {{ timestamp }}</small>
			</div>
		</div>
		<div class="row">		
			<div class="col-md-4" v-if="dataTop10CaseTotals.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10CaseTotals"
				  :labels="labelsTop10CaseTotals"
				  :data="dataTop10CaseTotals"
				  :options="chartOptions"
				  :chartColors="top10CaseTotalsChartColors"
				/>
			</div>			
			<div class="col-md-4" v-if="dataTop10DeathTotals.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10DeathTotals"
				  :labels="labelsTop10DeathTotals"
				  :data="dataTop10DeathTotals"
				  :options="chartOptions"
				  :chartColors="top10DeathTotalsChartColors"
				/>
			</div>
			<div class="col-md-4" v-if="dataTop10TestTotals.length > 0">			
				<bar-chart
				  :legendLabel="legendLabelTop10TestTotals"
				  :labels="labelsTop10TestTotals"
				  :data="dataTop10TestTotals"
				  :options="chartOptions"
				  :chartColors="top10TestTotalsChartColors"
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
			legendLabelTop10CaseTotals: '',
			labelsTop10CaseTotals: [],
			dataTop10CaseTotals: [],
			top10CaseTotalsChartColors: {
				backgroundColor: 'rgba(172, 13, 13, 0.3)',
				borderColor: 'rgba(255, 117, 26, 1)',	
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
			},			
			legendLabelTop10DeathTotals: '',
			labelsTop10DeathTotals: [],
			dataTop10DeathTotals: [],
			top10DeathTotalsChartColors: {
				backgroundColor: 'rgba(240, 201, 41, 0.3)',
				borderColor: 'rgba(255, 117, 26, 1)',	
				pointBorderColor: '#2554FF',
				borderWidth: 1,				
			},			
			legendLabelTop10TestTotals: '',
			labelsTop10TestTotals: [],
			dataTop10TestTotals: [],
			top10TestTotalsChartColors: {
				backgroundColor: 'rgba(217, 118, 66, 0.3)',
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
							maxRotation: 65,
							minRotation: 65,
						}
					}]
				},
				plugins: {
					title: {
						display: true,
						text: 'Test Title',
						padding: {
							top: 3,
							bottom: 5
						}
					}
				},				
			}
		};
	},
	async created() {
		const { data } = await axios.get("/home");
		this.legendLabelTop10CaseTotals = data.legendLabel1;
		this.labelsTop10CaseTotals = data.labels1;
		this.dataTop10CaseTotals = data.data1;		
		this.legendLabelTop10DeathTotals = data.legendLabel2;
		this.labelsTop10DeathTotals = data.labels2;
		this.dataTop10DeathTotals = data.data2;
		this.legendLabelTop10TestTotals = data.legendLabel3;
		this.labelsTop10TestTotals = data.labels3;
		this.dataTop10TestTotals = data.data3;		
		this.timestamp = data.timestamp;
	}
};
</script>