$(document).ready(function() {
	G.addControl("ReviewSectionHeader", Control.sub({
	    inherited: {
	        content: 
	        	{ 
	            	html: "div",
	            	css: {
	            		"display": "inline"
	            	},
	            	content: 
		            	[
		            		{
		            			html: "div",
		            			ref: "stepTitle",
		            			content:
		            				[
										{
											html: "h1",
											ref: "stepNum"
										},
										{
											html: "h2",
											ref: "label_text"
										}
		            				]
		            		}
	            	    ]

	            }	            
	    },
	    cssStep: Control.chain('$stepNum', 'css'),
	    cssStepLabel: Control.chain('$label_text', 'css'),
	    cssStepTitle: Control.chain('$stepTitle', 'css'),
	    label_text: Control.property(function(text) {
	    	if (text == undefined) {
	    		return  this.$label_text();
	    	} else {
	    		this.$label_text().content(text);
	    		return this;
	    	}
	    }),  
	    step: Control.property(function(step) {
	    	if (step == undefined) {
	    		return  this.$stepNum();
	    	} else {
	    		this.$stepNum().content(step);
	    		return this;
	    	}
	    })   
	}));
});