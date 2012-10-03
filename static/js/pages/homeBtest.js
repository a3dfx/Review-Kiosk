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
                $reviewStep = data.user_on_iphone ? G.controls.ReviewStepsMobile : G.controls.ReviewStep;
                this.$review_section().content(
                        $reviewStep.create()
                            .displayDevice(data.displayDevice)
                            .involvementOptions(data.involvementOptions)
                            .businessName(data.businessName)
                            .business_code(data.business_code)
                            .withPublicSharingCheckbox(data.withPublicSharingCheckbox)
                    );
                return this
            }
        },
        initialize: function() {
            G.doTimer();
            this.$content().click(function() {
                G.restartTimeout();
            });
        }
    }))
})
