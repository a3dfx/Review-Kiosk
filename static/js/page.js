$(document).ready(function() {
	G.addControl("CustomPage", Page.sub({
	    inherited: {
	        content: [
  	            { 
	            	html: "div", 
	            	ref: "Page_Nav_Bar",
	            	css: {
	            		"width": "100%",
	            		"height": "200px",
	            		"background-color": "#E3E3E3"
	            	}
	            },	                  
	            { 
	            	html: "div", 
	            	ref: "Page_content",
	            	css: {
	            		"width": "100%",
	            		"padding-top": "100px",
	            		"text-align": "center"
	            	}
	            }
	        ]
	    },
	    initialize: function() {
	    	$("#root").append(
	    		this
	    	)
	    },
	    content: Control.chain( "$Page_content", "content" ),
	    navBar: Control.chain( "$Page_Nav_Bar", "content" )
	}));
});