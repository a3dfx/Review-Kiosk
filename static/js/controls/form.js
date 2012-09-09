$(document).ready(function() {
	G.addControl("Form", Control.sub({
	    inherited: {
	        content:
	        	[
	        	 	{
	        	 		html: "form",
	        	 		ref: "form",
	        	 		content: 
	         	 			{
	        	 				html: "table",
	        	 				ref: "formTable"
	        	 			}
	        	 	},  
					{
						control: G.controls.SubmitButton,
						ref: 'submitButton'
					}	        	 	
	        	]      	              
	    },
	    formVals: Control.property(),
	    onSubmission: Control.property(),	    
	    inputsValid: function(inpList) {
	    	var allInpsValid = true;
	    	for (var i=0; i<inpList.length; i++) {
	    		if (!inpList[i]) {
	    			allInpsValid = false;
	    		}
	    	}
	    	return allInpsValid;
	    },	  
	    formFields: Control.property(function(fields) {
	    	var controls = {};
	    	var self = this;
	    	$.each(fields, function() {
	    		self.$formTable().append(
	    			$("<tr>").append(
	    				$("<td>").css({
	    					"padding": "15px"
	    				}).append(
	    					this.inpControl.label()
	    				),
	    				$("<td>").append(
	    					control = this.inpControl
	    				)
	    			)
	    		)
	    		controls[control.id()] = control
	    	});
	    	self.formVals(controls);
	    }),
	    clearForm: function() {
	    	$.each(this.formVals(), function() {
	    		this.content('');
	    	})
	    },	    
	    initialize: function() {
	    	var self = this;
	    	this.$submitButton().click(function() {
	    		var validInputs = [] 
	    		$.each(self.formVals(), function() {
	    			if (this.required()) {
	    				validInputs.push(this.getValidInput());
	    			} else if (this.getValidInput() != '') {
	    				validInputs.push(this.getValidInput());
	    			}
	    		});
    			var allInpsValid = self.inputsValid(validInputs);
    			if (allInpsValid) {
					self.onSubmission()();  				
    			}
	    	})
	    }
	}));
});