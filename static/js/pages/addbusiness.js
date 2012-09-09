$(document).ready(function() {
	G.addControl("AddBiz", Page.sub({
		inherited: {
			content: 
				{       
	            	control: G.controls.Form, 
	            	ref: "AddBizForm",
	            	formFields: [
	            		{
	            			inpControl: G.controls.TextField.create()
	            				.label('Name')
	            				.id('name')
	            				.required(true)
	    				},
	            		{
	            			inpControl: G.controls.TextField.create()
	            				.label('Email')
	            				.id('email')
	            				.validateEmail(true)
	            				.errorMessage('Enter a valid email')
	            				.required(true)
	    				},
	            		{
	            			inpControl: G.controls.TextField.create()
	            				.label('Kioware passcode')
	            				.id('kioware_passcode')
	            				.required(true)
	    				},	    				
	            		{
	            			inpControl: G.controls.TextField.create()
	            				.label('Involvement option 1')
	            				.id('io1')
	            				.charLimit(16)
	    				},
	    				{
	            			inpControl: G.controls.TextField.create()
	            				.label('Involvement option 2')
	            				.id('io2')
	            				.charLimit(16)
	    				},
	    				{
	            			inpControl: G.controls.TextField.create()
	            				.label('Involvement option 3')
	            				.id('io3')
	            				.charLimit(16)
	    				},
	    				{
	            			inpControl: G.controls.TextField.create()
	            				.label('Involvement option 4')
	            				.id('io4')
	            				.charLimit(16)
	    				},
	            		{
	            			inpControl: G.controls.TextField.create()
	            				.label('Url')
	            				.id('url')
	            				.required(true)
	    				},
	            		{
	            			inpControl: G.controls.SelectField.create()
	            				.label('With public sharing checkbox')
	            				.id('with_public_sharing_checkbox')
	            				.required(true)
	            				.content(['Yes', 'No'])
	    				}
	            	]
				}					
		},
		initialize: function() {
			var self = this;
			this.$AddBizForm().onSubmission(function() {
				var formData = self.$AddBizForm().formVals();
				biz_involvement = $.map([formData.io1.getValidInput(), 
				                         formData.io2.getValidInput(),
				                         formData.io3.getValidInput(),
				                         formData.io4.getValidInput()], function(n) {
					if (n) {
						return n;
					}
				}).join("|");	
				$.get("?email=" + encodeURIComponent(formData.email.getValidInput()) + 
					  "&name=" +  encodeURIComponent(formData.name.getValidInput()) +
					  "&involvementOptions=" + encodeURIComponent(biz_involvement) + 
					  "&kioware_passcode=" + encodeURIComponent(formData.kioware_passcode.getValidInput()) +
					  "&with_public_sharing_checkbox=" + encodeURIComponent(formData.with_public_sharing_checkbox.getValidInput()) +
					  "&url=" +   encodeURIComponent(formData.url.getValidInput()), function(data) {
	                if (data.message == "Successful") {
	                	alert('Successful and Saved');
	                	self.$AddBizForm().clearForm()
	                } else {
	                	alert('Something went wrong');
	                }
	            }, "json");		
			})
		}
	}))	
})