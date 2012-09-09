$(document).ready(function() {
	G.addControl("ReviewSitePage", G.controls.CustomPage.sub({
		site: Control.property(function(site) {
			siteMapping = {
				"google": {
					label: "Google+ Local",
					url: "https://accounts.google.com/ServiceLogin?service=lbc&continue=https://www.google.com/local/add%3Fservice%3Dlbc",
				},
				"citysearch": {
					label: "City Search",
					url: "http://sanfrancisco.citysearch.com/profile/670813190/redwood_city_ca/sweetcakes.html",
				},
				"bing": {
					label: "Bing Local",
					url: "http://www.bing.com/local/details.aspx?lid=YN113x247968113",
				},
				"yahoo": {
					label: "Yahoo Local",
					url: "http://local.yahoo.com/info-77345579-sweetcakes-redwood-city"
				}
			}
		    var $reviewSite = G.controls.Iframe.create().src(siteMapping[site].url);
			
			this.$Page_Nav_Bar().css({
				"background-color": "#333333",
			    "border": "1px solid #A3A19E",
			    "box-shadow": "0 1px 1px 0 #FFFFFF",
			    "font-size": "30px",
			    "width": "100%",
			    "height": "70px",
			    "float": "top",
			    "position": "fixed"
			})
			var $backButton = G.controls.BackButton.create()
				.css({
					"display": "inline",
					"float": "left",
					"height": "70px",
					"background": "#333333",
					"color": "#FABC00",
					"border": "0px",
					"box-shadow": "none",
					"text-shadow": "none",
					"margin-left": "10px"
				})
				.content("Back");
			
			var $logoutButton = G.controls.LogoutButton.create()
				.css({
					"display": "inline",
					"float": "right",
					"height": "70px",
					"background": "#333333",
					"color": "#FABC00",
					"border": "0px",
					"box-shadow": "none",
					"text-shadow": "none",
					"margin-right": "10px"
				})
				.content("Logout");			
			
			var navMessage = $("<div>").css({
				"vertical-align": "middle",
				"padding-top": "17px",
				"margin-right": "150px",
				"color": "white",
				"display": "inline",
				"position": "fixed",
				"left": "44%"
			}).append(
				siteMapping[site].label			
			)
		    this.navBar(
		    	$("<div>").css({
		    		"text-align": "center",
		    		"height": "70px"
		    	}).append(
		    		$backButton,
		    		navMessage,
		    		$logoutButton
		    	)
		    );

		    this.content(
				$reviewSite
			);			
		}),
	}))	
})