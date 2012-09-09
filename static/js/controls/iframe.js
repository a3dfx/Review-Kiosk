$(document).ready(function() {
	G.addControl("Iframe", Control.sub({
		inherited: {
			content: {
				html: "<iframe/>",
				ref: "iframe",
				css: {
					"height": "100%",
					"width": "100%",
					"margin-top": "71px"
				}
			}
		},
		src: Control.chain("$iframe", "attr/src"),
		content: Control.chain("$iframe", "content")
	}));
});