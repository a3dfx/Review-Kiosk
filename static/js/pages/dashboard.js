$(document).ready(function() {
	G.addControl("Dashboard", Page.sub({
		inherited: {
			content: 
				[
					{
						html: "div",
						ref: "title",
						css: {
							'padding-bottom': "20px",
							'padding-top': '30px',
							'font-weight': 'bold',
							'font-size': '30px',
							'font-family': 'arial'
						}
					},
					{
						html: "div",
						ref: "dashboard",
						css: {
							'font-family': 'arial'
						}
					}					
				]
		},
		title: Control.property(function(text) {
	    	if (text == undefined) {
	    		return text
	    	} else {
	    		this.$title().content(text)
	    		return this
	    	}	 			
		}),
		statsTable: Control.property(function(stats) {
			var table = $("<table>").append(
				$("<tr>").append(
					$("<td>").css({
						"font-weight": "bold"
					}).text(
						"Business Name"
					),
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Review Count"
					),
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Star Rating Average"
					),
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Url Path"
					)							
				)			
			);
			if (stats) {
				$.each(stats, function() {
					var stat = this;
					$.each(stat, function() {
						table.append(
							$("<tr>").append(
								$("<td>").append(
									this.name
								),
								$("<td>").css({
									"padding-left": "20px",
									"text-align": "right"
								}).append(
									this.rvrCount
								),
								$("<td>").css({
									"text-align": "right",
									"padding-left": "20px"
								}).append(
									this.starAvg
								),
								$("<td>").css({
									"text-align": "right",
									"padding-left": "20px"
								}).append(
									this.url
								)							
							)
						)
					})
				})
			}
			this.$dashboard().content(table)
		})
	}))	
})