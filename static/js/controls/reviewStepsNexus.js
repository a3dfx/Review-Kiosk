$(document).ready(function() {
    G.addControl("ReviewStepsNexus", Control.sub({
        inherited: {
            content:
                 {
                     html: "center",
                     content:
                         [
                         {
                                html: "div",
                                ref: "wrapper",
                                css: {
                                    "padding-bottom": "-10px"
                                },
                                content:
                                    {
                                          html: "div",
                                        ref: "header",
                                        css: {
                                            "vertical-align": "middle",
                                            "padding-bottom": "30px",
                                            "color": "white",
                                            "font-size": "40px"
                                        },
                                        content: "What do you think of us?"
                                    }
                            },
                            {
                                html: "div",
                                ref: "content",
                                css: {
                                    "width": "949px"
                                },
                                content:
                                      [
                                          {
                                              html: "div",
                                              ref: "step left",
                                              css: {
                                            	  'height': 290,
                                            	  'width': 300
                                              },
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                          "margin-left": "-16px"
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Rate Us",
                                                                 step: 1,
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
                                                                     'font-size': 22,
                                                                     'padding-top': 0
                                                                 },
                                                                 content: "Tap over the stars to set your rating."
                                                             },
                                                             {
                                                                 control: G.controls.StarRating,
                                                                 ref: "starRating"
                                                        
                                                             }
                                                         ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "step",
                                              css: {
                                            	  'height': 290,
                                            	  'width': 300
                                              },                                              
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                    	'margin-left': -33  
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Review Us",
                                                                 step: 2,
                                                                 css: {
                                                                     "margin-bottom": "20px"
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextArea,
                                                                 ref: "feedback",
                                                                 rows: 8,
                                                                 placeHolderText: "Type your comments here...",
                                                                 cssTextArea: {
                                                                	 'margin-left': 45,
                                                                	 'width': 260
                                                                 },
                                                                 cssErrorMarker: {
                                                                	 'margin-left': 24
                                                                 }
                                                             }
                                                          ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "step right",
                                              css: {
                                            	  'height': 290,
                                            	  'width': 300
                                              },                                              
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                    	'width': 309,
                                                      	'margin-left': -9 
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "About You",
                                                                 step: 3,
                                                                 cssStep: {
                                                                	'left': 199 
                                                                 },
                                                                 cssStepLabel: {
                                                                	 'margin-left': 60
                                                                 },
                                                                 cssStepTitle: {
                                                                	 'margin-bottom': 10
                                                                 },                                                                 
                                                                 css: {
                                                                	 'margin-left': -67,
                                                                     "margin-bottom": "20px"
                                                                 }
                                                             },
                                                             {
                                                                 html: "h3",
                                                                 ref: "emailHeader",
                                                                 content: "What is your email address?",
                                                                 css: {
                                                                     "margin-left": "24px",
                                                                     "margin-bottom": "8px",
                                                                     'font-size': 20,
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextField,
                                                                 ref: "email",
                                                                 cssTextField: {
                                                                	 'width': '263px',
                                                                	 'height': 23
                                                                 },
                                                                 withCustomErrorDisplay: true,
                                                                 required: true,
                                                                 validateEmail: true,
                                                                 placeHolderText: "Enter email address"
                                                             },                                                             
                                                             {
                                                                 html: "h3",
                                                                 ref: "checkboxHeader",
                                                                 content: "What did you do today?",
                                                                 css: {
                                                                	 'font-size': 20,
                                                                	 'margin-bottom': 0,
                                                                     "margin-left": "24px",
                                                                     'margin-top': 15
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextField,
                                                                 ref: "name",
                                                                 required: false,
                                                                 withCustomErrorDisplay: true,
                                                                 placeHolderText: "Enter your first name",
                                                                 cssTextField: {
                                                                	 'width': '263px',
                                                                 },
                                                                 css: {
                                                                    'display': 'none',
                                                                    'padding-bottom': 37
                                                                 }
                                                             },
                                                             {
                                                                 html: "ul",
                                                                 ref: "options",
                                                                 attr: {
                                                                     'class': "options"
                                                                 },
                                                                 css: {
                                                                     "width": "91%",
                                                                     'margin-bottom': 10
                                                                 },
                                                                 content:
                                                                     [
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt1",
                                                                              css: {
                                                                                  "display": "inline",
                                                                              },
                                                                              cssContainer: {
                                                                            	  'width': 152
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt2",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              },
                                                                              cssContainer: {
                                                                            	  'width': 129
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt3",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              },
                                                                              cssContainer: {
                                                                            	  'width': 152
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt4",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              },
                                                                              cssContainer: {
                                                                            	  'width': 129
                                                                              }
                                                                          }
                                                                     ]
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
                                                  'width': 949,
                                                  'margin-top': 5,
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
                                                 "margin-left": "354px",
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
            		'background': 'none',
            		'background-color': '#012A6A'
            	})
            	this.$starRating().cssErrorDisplayWidth('276px');

                var toggleHeadWrapper = function(action) {

                    if (action == "hide" && self.$wrapper().css("display") != "none") {
                        self.$wrapper().animate({
                              height: "toggle",
                              opacity: 1
                            }, 500);
                    } else if (action == "show" && self.$wrapper().css("display") == "none") {
                        self.$wrapper().animate({
                            height: "toggle",
                            opacity: 1
                          }, 500);
                    }
                }
                if (this.involvementOptions()) {
                    self.$opt1().content(this.involvementOptions()[0] || null);
                    self.$opt2().content(this.involvementOptions()[1] || null);
                    self.$opt3().content(this.involvementOptions()[2] || null);
                    self.$opt4().content(this.involvementOptions()[3] || null);
                } else {
                    self.$checkboxHeader().content("What is your first name?").css({
                    	'padding-bottom': 5
                    });
                    self.$options().hide();
                    self.$name().show();
                }

                if (self.displayDevice() == 'tablet') {
                    self.$feedback().click(function() {
                        toggleHeadWrapper('hide');
                    })
                    self.$email().click(function() {
                        toggleHeadWrapper('hide');
                    })                    
                }
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
                        biz_involvement = $.map([self.$opt1().getValidInput(),
                                               self.$opt2().getValidInput(),
                                               self.$opt3().getValidInput(),
                                               self.$opt4().getValidInput()], function(n) {
                            if (n) {
                                return " " + n;
                            }
                        }).join();

                        var publicPermission = false;
                        if (self.withPublicSharingCheckbox()) {
                            publicPermission = encodeURIComponent(self.$publicPermission().isChecked());
                        }

                        $.get("/ajax?email=" + encodeURIComponent(self.$email().getValidInput()) +
                        	"&business_code=" + encodeURIComponent(self.business_code()) + 
                            "&business_involvement=" + encodeURIComponent(biz_involvement) +
                            "&starRating=" + encodeURIComponent(self.$starRating().getValidInput()) +
                            "&agree_public_share=" + publicPermission +
                            "&firstname=" + encodeURIComponent(self.$name().getValidInput()) +
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
                self.$starRating().click(function() {
                    toggleHeadWrapper('show');
                });
                self.$options().click(function() {
                    toggleHeadWrapper('show');
                });
                self.$submitButton().click(function() {
                    toggleHeadWrapper('show');
                    submitReview();
                });
            })
        }
    }));
});
