$(document).ready(function() {
	G.addControl("Reviews", Page.sub({
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
						ref: "reviews",
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
		dataTable: Control.property(function(data) {
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
						"Reviewer Email"
					),
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Business Involvement"
					),
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Feedback"
					),					
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Star Rating"
					),					
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Agreed to share on Site"
					),					
					$("<td>").css({
						"font-weight": "bold",
						"padding-left": "20px"
					}).text(
						"Date"
					)							
				)			
			);
			if (data) {
				$.each(data, function() {
					var review = this;
					$.each(review, function() {
						table.append(
							$("<tr>").append(
								$("<td>").css({
									'padding': 10
								}).append(
									this.business_name
								),
								$("<td>").css({
									'padding': 10
								}).append(
									this.reviewer_email
								),								
								$("<td>").css({
									'padding': 10
								}).append(
									this.business_involvement
								),
								$("<td>").css({
									'padding': 10,
									'width': 300
								}).append(
									this.feedback
								),								
								$("<td>").css({
									"text-align": "right",
									"padding": 10,
									"padding-left": "20px"
								}).append(
									this.star_rating
								),								
								$("<td>").css({
									'padding': 10
								}).append(
									this.agree_public_share
								),								
								$("<td>").css({
									'padding': 10
								}).append(
									this.date
								)						
							)
						)
					})
				})
			}
			this.$reviews().content(table)
		})
	}))	
})