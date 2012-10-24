$(document).ready(function() {
    G.addControl("Home", Page.sub({
        inherited: {
            content:
                {
                    html: "div",
                    ref: "content",
                    css: {
                        "text-align": "center"
                    },
                    content:
                        {
                            html: "div",
                            ref: "review_section",
                            css: {
                                "margin-top": "50px"
                            }
                        }
            }
        },
        pageData: function(data) {
            if (data == undefined) {
                return data
            } else {
            	if (data.user_on_iphone) {
            		$reviewStep = G.controls.ReviewStepsMobile;
            	} else if (data.user_on_nexus) {
            		$reviewStep = G.controls.ReviewStepsNexus;
            		this.$review_section().css({ 'margin-top': 0});
            	} else {
            		$reviewStep = G.controls.ReviewStep
            	}           	
                this.$review_section().content(
                        $reviewStep.create().properties({
                            displayDevice: data.displayDevice,
                            involvementOptions: data.involvementOptions,
                            businessName: data.businessName,
                            business_code: data.business_code,
                            withPublicSharingCheckbox: data.withPublicSharingCheckbox                      	
                        })
                    );
                return this
            }
        },
        initialize: function() {
//            G.doTimer();
//            this.$content().click(function() {
//                G.restartTimeout();
//            });
        }
    }))
})
