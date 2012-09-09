$(document).ready(function() {
	G.addControl("SelectField", Control.sub({
	    inherited: {
	        content: 
	        	[	  	        	 
		        	{
		            	html: "select",
		            	ref: "selectField"	        		
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
	    label: Control.property(),
	    id: Control.property(),
	    errorMessage: Control.property(),
	    required: Control.property(),    
	    content: function(options) {
	    	if (options == undefined) {
	    		return this.$selectField().content();
	    	} else {
	    		for (var i=0; i<options.length; i++) {
    				this.$selectField().append(
    					$("<option>").append(options[i])
    				)
	    		}
	    		return this
	    	}
	    },
	    getValidInput: function() {
	    	var inputValid = false;
	    	this.errorMessage('Invalid input');
        	var pattern = new RegExp(/<(.|\n)*?>/g);
        	if (!pattern.test(this.$selectField().val())
        		&& this.$selectField().val()) {
        		inputValid = true;
        	}   
	        if (inputValid) {      		        
	        	this.$errorContainer().hide();
	        	return this.$selectField().val();
	        } else {
	        	this.$errorContainer().show().content(this.errorMessage());        		        			        	
	        	null
	        }
	    }    
	}));
});