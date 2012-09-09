G.addControl("SiteLink", Control.sub({
	inherited: {
		content: {
			html: "<img/>",
			ref: "icon",
			css: {
				"cursor": "pointer",
				"height": "300px",
				"width": "300px"
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