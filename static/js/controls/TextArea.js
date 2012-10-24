$(document).ready(function() {
	G.addControl("TextArea", Control.sub({
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
		            	html: "textarea",
		            	ref: "textArea",
		            	attr: {
		            		'rows': "12",
		            		'cols': "50"
		            	}
		            },
	  	            {
	  	            	html: "div",
	  	            	ref: "errorContainer",
	  	            	content: "Leave a review",
	  	            	css: {
	  	            		"font-size": "16px",
	  	            		"color": "red",
	  	            		"padding-top": "26px",
	  	            		"display": "none"
	  	            	}
	  	            }	        	 
	        	]	                  
	    },
	    cssErrorMarker: Control.chain('$errorMarker', 'css'),
	    cssTextArea: Control.chain('$textArea', 'css'),
	    initialize: function() {
	    	var self = this;
	    	this.$textArea().focus(function() {
	    		if (self.$textArea().content() == self.placeHolderText()) {
	    			self.$textArea().content(null);
	    		}
	    	}).blur(function() {
	    		if (!self.$textArea().content()) {
	    			self.$textArea().content(self.placeHolderText());
	    		}	    		
	    	});
	    },
	    placeHolderText: Control.property(function(text) {
	    	if (text == undefined) {
	    		return text
	    	} else {
	    		this.$textArea().content(text)
	    		return this
	    	}	    	
	    }),	  
	    rows: Control.property(function(rows) {
	    	if (rows == undefined) {
	    		return rows
	    	} else {
	    		this.$textArea().attr('rows', rows);
	    		return this
	    	}	    	
	    }),		    
	    content: function(content) {
	    	if (content == undefined) {
	    		return this.$textArea().content()
	    	} else {
	    		this.$textArea().content(content)
	    		return this
	    	}
	    },
	    getValidInput: function() {
	        var pattern = new RegExp(/<(.|\n)*?>/g);
	        if (!pattern.test(this.$textArea().content()) && 
	        	this.$textArea().content().length > 0 &&
	        	this.$textArea().content() != this.placeHolderText()) {	
	        	this.$textArea().css({
	        		"border": "2px solid #AAAAAA"
	        	});
	        	this.$errorMarker().hide();
	        	return this.$textArea().content()
	        } else { 
	        	this.$textArea().css({
	        		"border": "4px solid #FDC038"
	        	});
	        	this.$errorMarker().fadeIn('slow');
	        	null
	        }
	    }	    
	}));
});