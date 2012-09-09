$(document).ready(function() {
	G.addControl("Home", G.controls.CustomPage.sub({
		initialize: function() {	
			this.content(
				$("<div>").append(
					G.controls.SiteLink.create()
						.icon("/static/images/reicons/logo_google.png")
						.linkTo("http://www.google.com"),
					G.controls.SiteLink.create()
						.icon("/static/images/reicons/logo_citysearch.png")
						.linkTo("http://www.google.com"),
					G.controls.SiteLink.create()
						.icon("/static/images/reicons/logo_yahoo.png")
						.linkTo("http://www.yahoo.com"),
					G.controls.SiteLink.create()
						.icon("/static/images/reicons/logo_bing.png")
						.linkTo("http://www.bing.com")							
				)
			);
			this._super();
		}
	}))	
})