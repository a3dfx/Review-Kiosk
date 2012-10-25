$(document).ready(function() {
	G.addControl("StarRatingLarge", Control.sub({
	    inherited: {
	        content: 
	        	[	   
	        	 	{
	        	 		html: "img",
	        	 		ref: "errorMarker",
	        	 		attr: {
	        	 			'src': "/static/images/error-marker.png"
	        	 		},
	        	 		css: {
	        	 			"display": "none"
	        	 		}
	        	 	},	
	        	 	{
	        	 		html: "div",
	        	 		ref: "errorBorder",
	        	 		css: {
	        	 			"border": "0px"
	        	 		},
	        	 		content: 
	    	        	 	{
	    	        	 		html: "ul",
	    	        	 		attr: {
	    	        	 			'class': "nostyle",
	    	        	 			'id': "examples"
	    	        	 		},
	    	        	 		content: 
	    	        	 			{
	    	        	 				html: "li",
	    	        	 				content:
	    	        	 					[
	    		        	 					{
	    		        	 						html: "div",
	    		        	 						attr: {
	    		        	 							'class': "rateit bigstars2",
	    		        	 							"data-rateit-starwidth": "75",
	    		        	 							"data-rateit-starheight": "75",
	    		        	 							"data-rateit-step": ".5"
	    		        	 						},
	    		        	 						css: {
	    		        	 							margin: 0
	    		        	 						}
	    		        	 					},
	    	        	 						{
	    	        	 							html: "div",
	    	        	 							attr: {
	    	        	 								'class': "ratingLabels"
	    	        	 							},
	    	        	 							content: 
	    	        	 								[
	    	        	 								 	{
	    	        	 								 		html: "div",
	    	        	 								 		content: "Poor",
	    	        	 								 		css: {
	    	        	 								 			'margin-left': 36
	    	        	 								 		},
	    	        	 								 		attr: {
	    	        	 								 			'class': "poor"
	    	        	 								 		}
	    	        	 								 	},
	    	        	 								 	{
	    	        	 								 		html: "div",
	    	        	 								 		content: "Average",
	    	        	 								 		css: {
	    	        	 								 			'margin-left': 92
	    	        	 								 		},
	    	        	 								 		attr: {
	    	        	 								 			'class': "Average"
	    	        	 								 		}
	    	        	 								 	},
	    	        	 								 	{
	    	        	 								 		html: "div",
	    	        	 								 		content: "Excellent",
	    	        	 								 		css: {
	    	        	 								 			'margin-left': 91
	    	        	 								 		},
	    	        	 								 		attr: {
	    	        	 								 			'class': "excellent"
	    	        	 								 		}
	    	        	 								 	}	        	 								 	
	    	        	 								]
	    	        	 						}		        	 					
	    	        	 					]
	    	        	 			}
	    	        	 	}	        	 			
	        	 	},
	  	            {
	  	            	html: "div",
	  	            	ref: "errorContainer",
	  	            	content: "Pick a star rating",
	  	            	css: {
	  	            		"font-size": "16px",
	  	            		"color": "red",
	  	            		"padding-top": "91px",
	  	            		"display": "none"
	  	            	}
	  	            }
	        	]                 
	    },
	    initialize: function() {
	    	var self = this;
	    	if (self.noErrorImage()) {
	    		self.$errorMarker().remove();
	    	}		    	
	    	this.inDocument(function() {
	    		$('div.rateit').rateit();
	    	})
	    	self.click(function() {
	    		self.getValidInput();
	    	})
	    },
	    noErrorImage: Control.property(),
	    cssErrorDisplayWidth: Control.chain('$errorBorder', 'css/width'),
	    getValidInput: function() {
	    	var starsGiven = Math.round(5 * (parseFloat($('.rateit-selected').css("width").replace("px", ""))/375)*100)/100
	    	if (starsGiven % 1) {
	    		var starFrac = Math.round((starsGiven % 1)*100)/100;
	    		if (starFrac == .24) {
	    			starsGiven += .01;
	    		} else {
	    			starsGiven -= .01;
	    		}
	    	}
	    	if (starsGiven > 0) {
	        	this.$errorMarker().hide();	
	        	this.$errorBorder().css({
	        		"border": "0px"
	        	});
	        	return starsGiven;
	        } else {
	        	this.$errorMarker().fadeIn('slow');	
	        	this.$errorBorder().css({
	        		"border": "4px solid #FDC038"
	        	});        	
	        	null
	        }
	    }	    
	}));
});