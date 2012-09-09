$(document).ready(function() {
	G.addControl("BackButton", BasicButton.sub({
		initialize: function() {
			var self = this;
			this.hover(
				function() {
					self.css({
						"text-shadow": "0 1px 3px #A3A19E"
					})
				},
				function() {
					self.css({
						"text-shadow": "none"
					})
				}				
			);
			this.click(function() {
				history.go(-1)
			});
		}
	}))
});