$(document).ready(function() {
    G.addControl("ReviewStep", Control.sub({
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
                                    "padding-bottom": "35px"
                                },
                                content:
                                    {
                                          html: "div",
                                        ref: "header",
                                        css: {
                                            "vertical-align": "middle",
                                            "padding-bottom": "30px",
                                            "color": "white",
                                            "font-size": "60px"
                                        },
                                        content: "What do you think of us?"
                                    }
                            },
                            {
                                html: "div",
                                ref: "content",
                                css: {
                                    "width": "1248px"
                                },
                                content:
                                      [
                                          {
                                              html: "div",
                                              ref: "step left",
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      css: {
                                                          "margin-left": "35px"
                                                      },
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "Rate Us",
                                                                 step: 1,
                                                                 css: {
                                                                     "margin-bottom": "20px",
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
                                                                     "margin-left": "24px"
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
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
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
                                                                 placeHolderText: "Type your comments here..."
                                                             }
                                                          ]
                                                  }
                                          },
                                          {
                                              html: "div",
                                              ref: "step right",
                                              content:
                                                  {
                                                      html: "div",
                                                      ref: "pad",
                                                      content:
                                                          [
                                                              {
                                                                 control: G.controls.ReviewSectionHeader,
                                                                 ref: "reviewSectionHeader",
                                                                 label_text: "About You",
                                                                 step: 3,
                                                                 css: {
                                                                     "margin-bottom": "20px"
                                                                 }
                                                             },
                                                             {
                                                                 html: "h3",
                                                                 ref: "checkboxHeader",
                                                                 content: "What did you do today?",
                                                                 css: {
                                                                     "margin-left": "24px"
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextField,
                                                                 ref: "name",
                                                                 required: false,
                                                                 withCustomErrorDisplay: true,
                                                                 placeHolderText: "Enter your first name",
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
                                                                     "width": "100%"
                                                                 },
                                                                 content:
                                                                     [
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt1",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt2",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt3",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              }
                                                                          },
                                                                          {
                                                                              control: G.controls.CheckBox,
                                                                              ref: "opt4",
                                                                              css: {
                                                                                  "display": "inline"
                                                                              }
                                                                          }
                                                                     ]
                                                             },
                                                             {
                                                                 html: "h3",
                                                                 ref: "emailHeader",
                                                                 content: "What is your email address?",
                                                                 css: {
                                                                     "margin-left": "24px",
                                                                     "margin-bottom": "13px"
                                                                 }
                                                             },
                                                             {
                                                                 control: G.controls.TextField,
                                                                 ref: "email",
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
                                                  "display": "hidden"
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
                                              html: 'ul',
                                              ref: 'publicPermissionList',
                                              css: {
                                                  "margin": 0
                                              },
                                              content:
                                                  {
                                                      control: G.controls.CheckBox,
                                                      ref: 'publicPermission',
                                                      checkedOnDefault: true,
                                                      css: {
                                                          "display": "inline",
                                                          'color': '#FFFFFF',
                                                          'float': 'left',
                                                          'list-style-type': 'none'
                                                      }
                                                  },
                                              css: {
                                                  'clear': 'both',
                                                  'width': 300,
                                                  'padding-top': 15,
                                                  'margin-left': 0
                                              }
                                          },
                                          {
                                             control: G.controls.SubmitButton,
                                             ref: "submitButton",
                                             content: "Send Review",
                                             css: {
                                                 "margin-top": "15px",
                                                 "background-image": "linear-gradient(top, #ffd182, #c2920f)",
                                                 "background-image": "-moz-linear-gradient(top, #ffd182, #c2920f)",
                                                 "font-size": "18px",
                                                 "font-family": "arial",
                                                 "float": "left",
                                                 "margin-left": "515px",
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
                if (!self.withPublicSharingCheckbox()) {
                    self.$publicPermissionList().remove();
                }

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
                }
                var bizName = self.businessName();
                self.$publicPermission().content('I allow ' + bizName + ' to post my review publicly on their website');
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
                self.$email().click(function() {
                    toggleHeadWrapper('show');
                }).bind("keydown", function(e) {
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
