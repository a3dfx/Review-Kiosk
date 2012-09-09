$(document).ready(function() {
	G.addControl("Home", G.controls.CustomPage.sub({
		initialize: function() {
			var pageContent = $("<div>").append(
				$("<div>").css({
					"vertical-align": "middle",
					"padding-top": "50px",
					"color": "white",
					"font-size": "50px"
				}).append(
					"Tell people what you think"
				),
				$("<div>").css({
					"vertical-align": "middle",
					"padding": "20px",
					"padding-bottom": "50px",
					"color": "lightblue",
					"font-size": "20px"
				}).append(
					"Select a review site to continue"
				)
			);
			this.$Page_content().css({
			    "border-top": "1px solid #A3A19E",
			    "box-shadow": "0 1px 1px 0 #FFFFFF",
			    "width": "100%",
			    "height": "100%",
			    "bottom": "0",
			    "background-image": "url('/static/images/background.jpg')",
			    "background-repeat": "no",
			    "background-repeat": "repeat-x"
			});	
			this.content(
				$("<center>").append(
					$("<div>").css({
						"margin-top": "-36px"
					}).append(
						$("<img>").attr({
							src: "/static/images/horizontal_divide_flip.png"
						})
					),	
					pageContent,
					G.controls.IconTable.create()
						.items([
						    G.controls.SiteLink.create()
								.icon("/static/images/logo_google.png")
								.linkTo("/google"),
							G.controls.SiteLink.create()
								.icon("/static/images/logo_citysearch.png")
								.linkTo("/citysearch"),
							G.controls.SiteLink.create()
								.icon("/static/images/logo_yahoo.png")
								.linkTo("/yahoo"),
							G.controls.SiteLink.create()
								.icon("/static/images/logo_bing.png")
								.linkTo("bing")
						])
				)
			);
		}
	}))	
})