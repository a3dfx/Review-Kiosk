$(document).ready(function() {
	G.addControl("ReviewTextBox", AutoSizeTextBox.sub({
		placeholder: "Enter your review here",
		initialize: function() {
			var self = this;
			self.$textBox().css({
				"background": "none repeat scroll 0 0 #FFFFFF",
			    "border": "2px solid #000000",
			    "border-radius": "4px 4px 4px 4px",
			    "color": "#999999",
			    "display": "inline",
			    "font-size": "14px",
			    "padding": "11px",
				"width": "300px",
				"height": "300px"			    
			})
		}
	}));
});