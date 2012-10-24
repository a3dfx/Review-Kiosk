$(document).ready(function() {
	G.addControl("TextField", Control.sub({
	    inherited: {
	        content: 
	        	[	  
	        	 	{
	        	 		html: "img",
	        	 		ref: "errorMarker",
	        	 		attr: {
	        	 			src: "/static/images/error-marker.png"
	        	 		},
	        	 		css: {
	        	 			"display": "none"
	        	 		}
	        	 	},	        	 
		        	{
		            	html: "input",
		            	ref: "textField"	        		
		        	},
	  	            {
	  	            	html: "div",
	  	            	ref: "errorContainer",
	  	            	content: "Invalid input",
	  	            	css: {
	  	            		"font-size": "12px",
	  	            		"color": "red",
	  	            		"display": "none",
	  	            		"padding-top": "3px",
	  	            		"vertical-align": "middle"
	  	            	}
	  	            }		        	
	        	]                  
	    },
	    cssTextField: Control.chain('$textField', 'css'),
	    label: Control.property(),
	    id: Control.property(),
	    cssErrorMarker: Control.chain('$errorMarker', 'css'),
	    errorMessage: Control.property(),
	    validateEmail: Control.property(),
	    required: Control.property(),
	    withCustomErrorDisplay: Control.property(),  
	    charLimit: Control.property(),	   
	    
	    placeHolderText: Control.property(function(text) {
	    	if (text == undefined) {
	    		return text
	    	} else {
	    		this.$textField().content(text)
	    		return this
	    	}	    	
	    }),
	    content: function(content) {
	    	if (content == undefined) {
	    		return this.$textField().content()
	    	} else {
	    		this.$textField().content(content)
	    		return this
	    	}
	    },
	    validateRequiredField: function() {
	    	var inputValid = false;
	    	this.errorMessage('Invalid input');
	        if (this.validateEmail()) {
	        	this.errorMessage('Invalid email address');
	        	var emailPattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
	        	inputValid = emailPattern.test(this.$textField().content());
	        } else {
	        	var pattern = new RegExp(/<(.|\n)*?>/g);
	        	if (!pattern.test(this.$textField().content()) &&
	        		this.$textField().content() != this.placeHolderText()) {
	        		inputValid = this.$textField().content().length > 0
	        	}       	
	        }
    		if (this.charLimit()) {
    			if (this.$textField().content().length <= this.charLimit()) {
    				inputValid = true;
    			} else {
    				inputValid = false;
    				this.errorMessage('Value entered above character limit of ' + this.charLimit());
    			}
    		}	        
	        if (inputValid) {
	        	if (this.withCustomErrorDisplay()) {
		        	this.$errorMarker().hide();
		        	this.$textField().css({
		        		"border": "2px solid #AAAAAA"
		        	});	 	        		
	        	} else {       		        
	        		this.$errorContainer().hide();
	        	}
	        	return this.$textField().content();
	        } else {
	        	if (this.withCustomErrorDisplay()) {
		        	this.$textField().css({
		        		"border": "4px solid #FDC038"
		        	});	        	
		        	this.$errorMarker().fadeIn('slow'); 	        		
	        	} else {
	        		this.$errorContainer().show().content(this.errorMessage());        		        		
	        	}	        	
	        	null
	        }	    	
	    },
	    validateNotRequiredField: function() {
	    	if (this.$textField().content() == this.placeHolderText()) {
	    		return null;
	    	} else {
	        	var pattern = new RegExp(/<(.|\n)*?>/g);
	        	if (!pattern.test(this.$textField().content())) {
	        		return this.$textField().content();
	        	} else {
	        		return null;
	        	}	    		
	    	}
	    },
	    getValidInput: function() {
	    	if (this.required()) {
	    		return this.validateRequiredField();
	    	} else {
	    		return this.validateNotRequiredField();
	    	}
	    },
	    initialize: function() {
	    	var self = this;
	    	this.$textField().focus(function() {
	    		if (self.$textField().content() == self.placeHolderText()) {
	    			self.$textField().content(null);
	    		}
	    	}).blur(function() {
	    		if (!self.$textField().content()) {
	    			self.$textField().content(self.placeHolderText());
	    		}	    		
	    	});
	    }	    
	}));
});