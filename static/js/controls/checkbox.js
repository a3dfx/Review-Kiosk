$(document).ready(function() {
	G.addControl("CheckBox", Control.sub({
	    inherited: {
	        content:
	        	{
		        	html: "li",
		        	ref: 'container',
		        	content:
			        	[
							{
								html: "input",
								ref: "checkBox",
								attr: {
									'type': "checkbox",
									'value': ""
								},
					        	css: {
						        	'cursor': 'pointer'
						        }							
							},
							{
								html: "label",
								ref: "label",
					        	css: {
						        	'cursor': 'pointer'
						        }
							}
			        	]
	        	}
	    },
	    cssContainer: Control.chain('$container', 'css'),
	    initialize: function() {
	    	var self = this;
	    	this.$label().click(function() {
	    		if (self.$checkBox().attr('checked')) {
	    			self.$checkBox().removeAttr('checked');
	    		} else {
	    			self.$checkBox().attr('checked', 'checked');
	    		}
	    		
	    	});
	    },
	    checkedOnDefault: function(checked) {
	    	if (checked) { this.$checkBox().attr('checked', 'checked'); }
	    },
	    isChecked: function() {
	    	return this.$checkBox().attr('checked') == 'checked';
	    },
	    content: Control.property(function(text) {
	    	if (!text) {
	    		this.css({
	    			'visibility': 'hidden'
	    		})
	    		return  this.$label();
	    	} else {
	    		this.$label().content(text);
	    		return this;
	    	}
	    }),
	    getValidInput: function() {
	    	if (this.$checkBox().attr("checked")) {
	    		return this.content();
	    	} else {
	    		return "";
	    	}
	    }	
	}));
});
