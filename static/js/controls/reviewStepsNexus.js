$(document).ready(function() {
    G.addControl("ReviewStepsNexus", Control.sub({
        inherited: {
            content:
                 {
                     html: "div",
                     content:
                         [
                            {
                                html: "div",
                                ref: "content",
                                css: {
                                	'background': 'url("../../static/images/background.jpg") repeat-x fixed left top transparent',
	                                'border': '1px solid transparent',
	                                'height': '966px',
	                                'overflow': 'hidden',                               	
                                    "width": "600px",
                                    'padding-top': 40,
                                    'padding-left': 9,
                                },
                                content:
                                      [
                                          {
                                              html: "div",
                                              ref: "step left",
                                              css: {
                                            	  'height': 255,
                                            	  'width': 570,
                                            	  'margin-bottom': 47
                                              },
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                          "margin-left": "119px"
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Rate Us",
                                                                 step: 1,
                                                                 cssStepLabel: {
                                                                	'font-size': 32,
                                                                	'margin-top': -10
                                                                 },
                                                                 cssStepTitle: {
                                                                	'margin-bottom': 7 
                                                                 },
                                                                 css: {
                                                                     "margin-bottom": "7px",
                                                                     "margin-left": "0px",
                                                                     "margin-right": "35px"
                                                                 }
                                                             },
                                                             {
                                                                 html: "div",
                                                                 attr: {
                                                                     'class': "smallText"
                                                                 },
                                                                 css: {
                                                                     "margin-left": "24px",
                                                                     'font-size': 17,
                                                                     'padding-top': 0
                                                                 },
                                                                 content: "Tap over the stars to set your rating."
                                                             },
                                                             {
                                                                 control: G.controls.StarRatingLarge,
                                                                 css: {
                                                                	'width': 420,
                                                                	'margin-left': -67,
                                                                	'margin-top': -11
                                                                 },
                                                                 ref: "starRating"
                                                        
                                                             }
                                                         ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "step",
                                              css: {
                                            	  'height': 242,
                                            	  'width': 570,
                                            	  'margin-bottom': 47
                                              },                                              
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                    	'margin-left': 119  
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Your Comments",
                                                                 step: 2,
                                                                 cssStepLabel: {
                                                                 	'font-size': 32,
                                                                	'margin-top': -10
                                                                  },                                                                 
                                                                 css: {
                                                                	 'margin-left': -6,
                                                                     "margin-bottom": "20px"
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextArea,
                                                                 ref: "feedback",
                                                                 rows: 5,
                                                                 placeHolderText: "Type your comments here...",
                                                                 cssTextArea: {
                                                                	 'margin-left': -91,
                                                                	 'width': 500
                                                                 },
                                                                 cssErrorMarker: {
                                                                	 'margin-left': -111
                                                                 }
                                                             }
                                                          ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "step right",
                                              css: {
                                            	  'height': 168,
                                            	  'width': 570
                                              },                                              
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                    	'width': 309,
                                                      	'margin-left': 119 
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Your Email",
                                                                 step: 3,
                                                                 cssStep: {
                                                                	'left': 199 
                                                                 },
                                                                 cssStepLabel: {
                                                                	 'font-size': 32,
                                                                	 'margin-left': 60,
                                                                 	 'margin-top': -10
                                                                 },
                                                                 cssStepTitle: {
                                                                	 'margin-bottom': 10
                                                                 },                                                                 
                                                                 css: {
                                                                	 'margin-left': -61,
                                                                     "margin-bottom": "20px"
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextField,
                                                                 ref: "email",
                                                                 cssTextField: {
                                                                	 'width': 325,
                                                                	 'height': 23,
                                                                	 'margin-left': -14
                                                                 },
                                                                 cssErrorMarker: {
                                                                	'margin-left': -35 
                                                                 },
                                                                 withCustomErrorDisplay: true,
                                                                 required: true,
                                                                 validateEmail: true,
                                                                 placeHolderText: "Enter email address"
                                                             }                                                             
                                                          ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "errorMessage",
                                              attr: {
                                                  'class': "message error"
                                              },
                                              css: {
                                                  "display": "hidden",
                                                  'width': 570,
                                                  'margin-left': 8,
                                                  'background': 'none repeat scroll 0 0 rgba(0, 0, 0, 0.5)'
                                              },
                                              content:
                                                  [
                                                      {
                                                          html: "img",
                                                          attr: {
                                                              'align': "absmiddle",
                                                              'src': "/static/images/error.png"
                                                          }
                                                      },
                                                       {
                                                           html: "span",
                                                           css: {
                                                        	 'font-size': 17  
                                                           },
                                                           content: "Please complete the required steps before continuing."
                                                       }
                                                  ]
                                          },
                                          {
                                             control: G.controls.SubmitButton,
                                             ref: "submitButton",
                                             content: "Send Review",
                                             css: {
                                                 "margin-top": "20px",
                                                 "background-image": "linear-gradient(top, #ffd182, #c2920f)",
                                                 "background-image": "-moz-linear-gradient(top, #ffd182, #c2920f)",
                                                 "font-size": "18px",
                                                 "font-family": "arial",
                                                 "float": "left",
                                                 "margin-left": "168px",
                                                 "height": "47px"
                                             }
                                          }
                                    ]
                            }
                         ]
                 }
        },
        displayDevice: Control.property(),
        involvementOptions: Control.property(),
        businessName: Control.property(),
        business_code: Control.property(),
        withPublicSharingCheckbox: Control.property(),
        inputsValid: function(inpList) {
            var allInpsValid = true;
            for (var i=0; i<inpList.length; i++) {
                if (!inpList[i]) {
                    allInpsValid = false;
                }
            }
            return allInpsValid;
        },
        initialize: function() {
            var self = this;
            this.inDocument(function() {
            	$('body').css({
            		'background': 'none'
            	})
            	this.$starRating().cssErrorDisplayWidth('420px');

                var bizName = self.businessName();
                var submitReview = function() {
                    var allInpsValid = self.inputsValid([
                        self.$starRating().getValidInput(),
                        self.$email().getValidInput(),
                        self.$feedback().getValidInput(),
                    ]);
                    if (allInpsValid) {
                        self.$submitButton().disable();
                        self.$errorMessage().hide();

                        var publicPermission = false;
                        if (self.withPublicSharingCheckbox()) {
                            publicPermission = encodeURIComponent(self.$publicPermission().isChecked());
                        }

                        $.get("/ajax?email=" + encodeURIComponent(self.$email().getValidInput()) +
                        	"&business_code=" + encodeURIComponent(self.business_code()) + 
                            "&starRating=" + encodeURIComponent(self.$starRating().getValidInput()) +
                            "&agree_public_share=" + publicPermission +
                            "&feedback=" + encodeURIComponent(self.$feedback().getValidInput()), function(data) {

                            if (data.message == "successful") {
                                $("div.content").empty().append(
                                        $("<div>").css({
                                            "height": "100%",
                                            "margin-top": "100px"
                                        }).append(
                                            $("<div>").css({
                                                "font-size": "70px",
                                                "color": "white"
                                            }).append(
                                                'Thank you for visiting <br/>' + bizName
                                            ),
                                            $("<div>").css({
                                                'font-size': '30px',
                                                'color': "lightBlue",
                                                'margin-top': '42px'
                                            }).append(
                                                'If there is anything we can do to make your experience more enjoyable,</br>please do not hesitate to speak to the office staff.'
                                            )
                                        )
                                    );
                                setTimeout("location.reload(true);",7000);
                            } else {
                                alert("Sorry there was an error");
                                self.$submitButton().enable();
                            }
                        }, "json")
                    } else {
                        if (self.$errorMessage().css("display") == "none") {
                            self.$errorMessage().animate({
                                height: "toggle",
                                opacity: 1
                              }, 500);
                        }
                    }
                }
                self.$email().bind("keydown", function(e) {
                    if (e.keyCode == 13) {
                        submitReview()
                    }
                });
                self.$submitButton().click(function() {
                    submitReview();
                });
            })
        }
    }));
});
