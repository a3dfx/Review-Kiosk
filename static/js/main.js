$(document).ready(function() {

	G.addControl("SiteLink", Control.sub({
		inherited: {
			content: {
				html: "<img/>",
				ref: "icon",
				css: {
					"cursor": "pointer",
					"height": "80px",
					"width": "80px"
				}
			}
		},
		initialize: function() {
			var self = this;
			this.click(function() {
				document.location = self.linkTo();
			});
		},
		icon: Control.chain("$icon", "attr/src"),
		linkTo: Control.property()
	}));

	G.addControl("home", G.controls.CustomPage.sub({
		initialize: function() {	
			this.content(
				$("<div>").append(
					G.controls.SiteLink.create()
						.icon("/static/images/icons/google.png")
						.linkTo("http://www.google.com"),
					G.controls.SiteLink.create()
						.icon("/static/images/icons/citysearch.png")
						.linkTo("http://www.google.com"),
					G.controls.SiteLink.create()
						.icon("/static/images/icons/yahoo.png")
						.linkTo("http://www.google.com")				
				)
			);
			this._super();
		}
	}))	

});