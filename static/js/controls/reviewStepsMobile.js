$(document).ready(function() {
	G.addControl("ReviewStepsMobile", Control.sub({
	    inherited: {
	        content: 
        	 	{
        	 		html: "center",
        	 		content:
        	 			[
	            	     {
			                	html: "div", 
			                	ref: "wrapper",
			                	css: {
			                		'width': 310
			                	},
			                	content: 
			                		{
			      	                	html: "div", 
			    	                	ref: "header",
			    	                	css: {
			    	    					"vertical-align": "middle",
			    	    					"padding-bottom": "30px",
			    	    					"color": "white",
			    	    					"font-size": "34px",
			    	    					"text-align": "center"
			    	                	},
			    	                	content: "What do you think of us?"
			                		}			                		
			            	},
			            	{
								html: "div",
								ref: "content",
								css: {
									"width": 310
								},
								content:
							          [
							      		{
							      			html: "div",
							      			ref: "step left",
							      			css: {
							      				'width': 310
							      			},
							      			content:
							      				[
								 					{
								 						html: "div",
								 						attr: {
								 							'class': "smallText"
								 						},
								 						css: {
								 							"margin-left": "40px",
								 							'font-size': 12,
								 							'padding-bottom': 7
								 						},
								 						content: "Tap over the stars to set your rating."
								 					},
								 					{
								 						control: G.controls.StarRating,
								 						ref: "starRating"
								 					}		 	         				
							 					]	
							      		},
							      		{
							      			html: "div",
							      			ref: "step",
							      			css: {
							      				'width': 310
							      			},							      			
							      			content:
							 					{
							 						control: G.controls.TextArea,
							 						ref: "feedback",
							 						rows: 7,
							 						placeHolderText: "Type your feedback here..."
							 					}		
							      		},
							      		{
							      			html: "div",
							      			ref: "step right",	
							      			css: {
							      				'width': 310
							      			},							      			
							      			content:
							      				[
								 					{
								 						html: "h3",
								 						ref: "checkboxHeader",
								 						content: "What did you do today?",
								 						css: {
								 							"margin-left": "24px",
								 							'font-size': 20
								 						}
								 					},									
								 					{
								 						html: "ul",
								 						ref: "options",
								 						attr: {
								 							'class': "options"
								 						},
								 						content:
								 							[
								 							 	{
								 							 		control: G.controls.CheckBox,
								 							 		ref: "opt1",
								 							 		css: {
								 							 			"display": "inline"
								 							 		}
								 							 	},
								 							 	{
								 							 		control: G.controls.CheckBox,
								 							 		ref: "opt2",
								 							 		css: {
								 							 			"display": "inline"
								 							 		}									 							 		
								 							 	},
								 							 	{
								 							 		control: G.controls.CheckBox,
								 							 		ref: "opt3",
								 							 		css: {
								 							 			"display": "inline"
								 							 		}									 							 		
								 							 	},
								 							 	{
								 							 		control: G.controls.CheckBox,
								 							 		ref: "opt4",
								 							 		css: {
								 							 			"display": "inline"
								 							 		}									 							 		
								 							 	}									 							 	
								 							]
								 					},
								 					{
								 						html: "h3",
								 						ref: "emailHeader",
								 						content: "What is your email address?",
								 						css: {
								 							"margin-left": "24px",
								 							"margin-bottom": "13px",
								 							'font-size': 20
								 						}
								 					},									 					
								 					{
								 						control: G.controls.TextField,
								 						ref: "email",
								 						withCustomErrorDisplay: true,
								 						validateEmail: true,
								 						placeHolderText: "Enter email address"
								 					}		 	         				
							      				]
							      		},
							      		{
							      			html: "div",
							      			ref: "errorMessage",
							      			attr: {
							      				'class': "message error"
							      			},
							      			css: {
							      				"display": "hidden",
							      				'width': 310
							      			},
							      			content: 
							      				[
								      				{
								      					html: "img",
								      					attr: {
								      						'align': "absmiddle",
								      						'src': "/static/images/error.png"
								      					}
								      				},							      				 
							      				 	{
							      				 		html: "span",
							      				 		content: "Please complete the required steps.",
							      				 		css: {
							      				 			'font-size': 14
							      				 		}
							      				 	}					      				 	
							      				]
							      		},
							      		{
						      				html: 'ul',
						      				ref: 'publicPermissionList',
						      				css: {
						      					"margin": 0,
						      					'font-size': 14
						      				},
						      				content: 
						      					{
				 							 		control: G.controls.CheckBox,
				 							 		ref: 'publicPermission',
				 							 		checkedOnDefault: true, 
				 							 		css: {
				 							 			"display": "inline",
				 							 			'color': '#FFFFFF',
					 							 	    'float': 'left',
					 							 	    'list-style-type': 'none',
					 							 	    'width': 304
				 							 		}	
						      					},
						      				css: {
						      					'clear': 'both',
						      					'width': 300,
						      					'padding-top': 15,
						      					'margin-left': 0
						      				}
							      		},
							      		{
					 						control: G.controls.SubmitButton,
					 						ref: "submitButton",
					 						content: "Send&nbsp;Review",
					 						css: {
					 		    				"background-image": "linear-gradient(top, #ffd182, #c2920f)",
					 		    				"background-image": "-moz-linear-gradient(top, #ffd182, #c2920f)",
					 		    				"font-size": "18px",
					 		    				'margin': 0,
					 		    				'margin-top': 10,
					 		    				'margin-left': 35,
					 		    				'margin-bottom': 38,
					 		    				"font-family": "arial",
					 		    				"float": "left",
					 		    				"height": "47px"
					 		    			}
							      		}
									]  	        			
							}			            	
        	 			]	
        	 	}
	    },
	    displayDevice: Control.property(),
	    involvementOptions: Control.property(),
	    businessName: Control.property(),
	    withPublicSharingCheckbox: Control.property(),
	    inputsValid: function(inpList) {
	    	var allInpsValid = true;
	    	for (var i=0; i<inpList.length; i++) {
	    		if (!inpList[i]) {
	    			allInpsValid = false;
	    		}
	    	}
	    	return allInpsValid;
	    },
	    initialize: function() {
	    	var self = this;    	
	    	this.inDocument(function() {
	    		$('body').css({
	    			'height': '100%',
	    			'max-width': 310
	    		});
	    		$('.textArea').css({
	    			'width': 260
	    		});	
	    		$('.textField').css({
	    			'width': 260
	    		});
	    		$('.publicPermission li').css({
	    			'width': 304
	    		});
	    		$('.step').css({
	    			'height': 153,
	    			'width': 304,
	    			'margin-right': 0,
	    			'background': 'none',
	    			'margin-left': 0
	    		});
	    		$('.step.left').css({
	    			'left': 140,
	    			'height': 150
	    		});
	    		$('.step.right').css({
	    			'height': 260
	    		});
	    		$('.step.left .errorBorder').css({
	    			'width': 270
	    		})
	    		if (!self.withPublicSharingCheckbox()) {
	    			self.$publicPermissionList().remove();
	    		}
	    		
	    		var toggleHeadWrapper = function(action) {
	    			if (action == "hide" && self.$wrapper().css("display") != "none") {
    					self.$wrapper().animate({
        		              height: "toggle", 
        		              opacity: 1
        		            }, 500);		    				
	    			} else if (action == "show" && self.$wrapper().css("display") == "none") {
    					self.$wrapper().animate({
      		              height: "toggle", 
      		              opacity: 1
      		            }, 500);		    				
	    			}  	    			
	    		}	    

	    		self.$opt1().content(this.involvementOptions()[0] || null);
	    		self.$opt2().content(this.involvementOptions()[1] || null);
	    		self.$opt3().content(this.involvementOptions()[2] || null);
	    		self.$opt4().content(this.involvementOptions()[3] || null);

	    		if (self.displayDevice() == 'tablet') {
		    		self.$feedback().click(function() {
		    			toggleHeadWrapper('hide');
		    		})	
	    		}
	    		var bizName = self.businessName();
	    		self.$publicPermission().content('I allow ' + bizName + ' to post my review publicly on their website');
	    		var submitReview = function() {
	    			var allInpsValid = self.inputsValid([
					    self.$starRating().getValidInput(),
				        self.$email().getValidInput(),
				        self.$feedback().getValidInput()
					]);
					if (allInpsValid) {
						self.$submitButton().disable();
						self.$errorMessage().hide();
						biz_involvement = $.map([self.$opt1().getValidInput(), 
						                       self.$opt2().getValidInput(),
						                       self.$opt3().getValidInput(),
						                       self.$opt4().getValidInput()], function(n) {
							if (n) {
								return " " + n;
							}
						}).join();
						
						var publicPermission = false;
						if (self.withPublicSharingCheckbox()) {
							publicPermission = encodeURIComponent(self.$publicPermission().isChecked());
						}
						
						$.get("?email=" + encodeURIComponent(self.$email().getValidInput()) + 
							"&business_involvement=" + encodeURIComponent(biz_involvement) +
							"&starRating=" + encodeURIComponent(self.$starRating().getValidInput()) +
							"&agree_public_share=" + publicPermission +
							"&feedback=" + encodeURIComponent(self.$feedback().getValidInput()), function(data) {
			                
							if (data.message == "successful") {
			                	$("div.content").empty().append(
			                    		$("<div>").css({
			                    			"height": "100%",
			                    			"margin-top": "100px"
			                    		}).append(
			                    			$("<div>").css({
			                    				"font-size": "70px",
			                    				"color": "white"
			                    			}).append(
			                    				'Thank you for visiting <br/>' + bizName + '!'
			                    			),
			                    			$("<div>").css({
			                    				'font-size': '30px',
			                    				'color': "lightBlue",
			                    				'margin-top': '42px'
			                    			}).append(
			                    				'If there is anything we can do to make your experience more enjoyable,</br>please do not hesitate to speak to the office staff.'		                			
			                    			)
			                    		)
			                    	);	
			                	setTimeout("location.reload(true);",7000);
			                } else {
			                	alert("Sorry there was an error");
			                	self.$submitButton().enable();
			                }
			            }, "json") 		    				
					} else {
						if (self.$errorMessage().css("display") == "none") {
							self.$errorMessage().animate({
		  		              height: "toggle", 
		  		              opacity: 1
		  		            }, 500);	    					
						}
					}	    			
	    		}
	    		self.$email().click(function() {
	    			toggleHeadWrapper('show');	
	    		}).bind("keydown", function(e) { 
	    	        if (e.keyCode == 13) {
	    	        	submitReview()
	    	        }          
	    	    });
	    		self.$starRating().click(function() {
	    			toggleHeadWrapper('show');
	    		});
	    		self.$options().click(function() {
	    			toggleHeadWrapper('show');
	    		});
	    		self.$submitButton().click(function() {
	    			toggleHeadWrapper('show');
	    			submitReview();
	    		});
	    	})
	    }
	}));
});