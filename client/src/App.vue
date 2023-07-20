<template>
	<div id="app">	
		<div class="container">
			<section class="section-content pt-5">
				<div class="row">
					<aside class="col-lg-3">
						<div class="logo-div text-center mb-4">
							<div class="row">
								<div class="col-md-3">
									<img src="./assets/images/covid19_img1.png" alt="logo" width="75" height="60">
								</div>
								<div class="col-md-9 pt-3">
									<h3>COVID WATCH</h3>
								</div>
							</div>
						</div>									
						<nav class="sidebar card py-3">
							<ul class="nav flex-column">
								<li class="nav-item">
									<router-link to="/" class="nav-link">Covid-19 US Statistics Snapshot</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/topTenUSCovidCases" class="nav-link">Top 10 US Covid Case Totals</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/totalUSCovidCases" class="nav-link">Total US Covid Cases</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/topTenUSCovidDeaths" class="nav-link">Top 10 US Covid Death Totals</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/totalUSCovidDeaths" class="nav-link">Total US Covid Deaths</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/topTenUSCovidTests" class="nav-link">Top 10 US Covid Test Totals</router-link>
								</li>
								<li class="nav-item">
									<router-link to="/totalUSCovidTests" class="nav-link">Total US Covid Tests</router-link>
								</li>
							</ul>
						</nav>
					</aside>
					<main class="col-lg-9">
						<h6 class="main-title pt-2">Data is courtesy of the <a href='https://www.worldometers.info/coronavirus/' target='_blank'>Coronavirus World-O-Meter</a> </h6>
						<div class="container">
							<div class="row">
								<div class="col-12">
									<router-view />
								</div>
							</div>
						</div>
					</main>
				</div>
			</section>
		</div>
		<footer class="footer mt-auto py-4 text-center">
			<div class = "container">
				<div class="row">
					<div class="col-sm-12">
						<small>Covid Watch &copy; <span id="year">2023</span></small><br>
						<small>Designed by <a href="https://devpatrol1.github.io" class="external" target="_blank">P. Rollins</a></small>
					</div>
				</div>
			</div>
		</footer>
	</div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');

.sidebar {
	border: 2px solid #660808;
	background: #ff751a;
}
.sidebar .nav-link {
    font-weight: 500;
    color: #660808;
}
.sidebar .nav-link:hover {
    background: var(--bs-light);
    color: var(--bs-warning);
}
.sidebar .router-link-exact-active{
	background: #FBE6C2;
	color: #ff751a;
}

.logo-div {
	background: #fff;
	border: 5px double #ff751a;
	color: #ff751a;
	text-shadow: 0 0 5px #f0c929;
	width: 100%;
	font-family: 'Fredoka One', cursive;
	font-weight: 400;
	padding: .5rem;
}

.main-title a {
	color: #333;
	text-decoration: none;
}
.main-title a:hover {
	color: #ff751a;
}

.footer {
	position: fixed;
	bottom: 0;
	width: 100%;
	color: #ff751a;
	background: #fcf1de;
}
.footer a {
	color: #ff751a;
	text-decoration: none;
	font-weight: 500;
}
.footer a:hover {
    color: var(--bs-warning);
}
</style>
