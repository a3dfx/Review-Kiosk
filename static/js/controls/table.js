G.addControl("IconTable", Control.sub({
	inherited: {
		content: {
			html: "div",
			ref: "table",
			css: {
				"text-align": "center",
				"width": "100%"
			}
		}
	},
	initialize: function() {
		var self = this;
		this.inDocument(function() {
			for (var i=0; i<self.items().length; i++) {
				this.$table().append(
					self.items()[i].css({
						"display": "inline-block",
						"margin": "10px",
						"margin-bottom": "150px",
						"margin-top": "50px"
					})
				);
			}
		})
	},
	items: Control.property(),
	rowCount: Control.property(),
    content: Control.chain( "$table", "content" )
}));