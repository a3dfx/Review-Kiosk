import logging
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import mail
from google.appengine.api import datastore_errors
from google.appengine.api.datastore import Key
from google.appengine.ext.webapp.util import run_wsgi_app
import random
import datetime
import hashlib
import simplejson
from google.appengine.api import mail
from HtmlTemplate import HtmlTemplate

class Reviewer(db.Model):
    email = db.StringProperty()
    business_involvement = db.StringProperty()
    agree_public_share = db.BooleanProperty(True)
    name = db.StringProperty()
    add_dt = db.DateTimeProperty(auto_now=True)

class Business(db.Model):
    name = db.StringProperty()
    url = db.StringProperty()
    offer = db.StringProperty()
    email = db.StringProperty()
    kioware_passcode = db.StringProperty()
    involvement_options = db.StringProperty()
    with_public_sharing_checkbox = db.BooleanProperty(True)
    active = db.BooleanProperty(True)
    add_dt = db.DateTimeProperty(auto_now=True)

class Review(db.Model):
    reviewer = db.ReferenceProperty(Reviewer)
    feedback = db.TextProperty()
    star_rating = db.FloatProperty()
    business = db.ReferenceProperty(Business)
    add_dt = db.DateTimeProperty(auto_now=True)

class Ajax(webapp.RequestHandler):
    def get(self):

        business_code = self.request.get('business_code')
        user_email = self.request.get('email')
        star_rating = self.request.get('starRating')
        feedback = self.request.get('feedback')
        firstname = self.request.get('firstname')
        business_involvement = self.request.get('business_involvement')
        with_public_sharing_checkbox = self.request.get('agree_public_share')
        message = "successful"
        biz = Business.all().filter("url = ", business_code).get()
        if biz:
            if user_email:
                rvr = Reviewer.all().filter("email = ", user_email).get()

                if not rvr:
                    rvr = Reviewer(
                        email=user_email,
                        business_involvement=business_involvement,
                        agree_public_share= with_public_sharing_checkbox == 'true',
                        name=firstname
                    )
                    rvr.save()
                if star_rating and feedback:
                    r = Review(
                        reviewer=rvr,
                        star_rating=float(star_rating),
                        feedback=feedback,
                        business=biz
                    )
                    r.save()
                else:
                    message = "Error: Missing or rating and feedback"
        else:
            message = "Error: Business code invalid"
        response = simplejson.dumps({"message":message}, sort_keys=True)
        self.response.out.write(response)


class MainPage(webapp.RequestHandler):
    def get(self, resource):

        myTemplate = HtmlTemplate()

        myTemplate.addHeaders([
            "http://quickui.org/release/quickui.catalog.css",
            "http://code.jquery.com/jquery-1.7.2.min.js",
            "http://quickui.org/release/quickui.js",
            "/static/quickuicatalog.js",
            "/static/starrating/jquery.MetaData.js",
            "/static/starrating/jquery.rating.js",
            "/static/starrating/jquery.rating.css",
            "/static/Archive/rating_screen_v1/js/jquery.rateit.js",
            "/static/Archive/rating_screen_v1/css/rateit.css",
            "/static/Archive/rating_screen_v1/css/styles.css",
            "/static/Archive/rating_screen_v1/css/bigstars.css",
            "/static/Archive/rating_screen_v1/css/antenna.css",
            "/static/Archive/rating_screen_v1/css/shCore.css",
            "/static/Archive/rating_screen_v1/css/shCoreDefault.css",
            "/static/js/G.js",
            "/static/js/controls/starrating.js",
            "/static/js/controls/starRatingLarge.js",
            "/static/js/controls/checkbox.js",
            "/static/js/controls/submitButton.js",
            "/static/js/controls/textField.js",
            "/static/js/controls/emailTextField.js",
            "/static/js/controls/TextArea.js",
            "/static/js/controls/reviewSectionHeader.js",
            "/static/js/controls/reviewStep.js",
            "/static/js/controls/reviewStepsMobile.js",
            "/static/js/controls/reviewStepsNexus.js",
            "/static/js/controls/sitelink.js",
            "/static/js/controls/reviewtextbox.js",
            "/static/js/pages/home.js"
        ])

        path = self.request.url.split('/')[3]
        displayDevice = 'tablet' if path == 't' else 'monitor'
        biz = Business.all().filter("url = ", resource).get()
        if biz:
            uastring = self.request.headers.get('user_agent')
            user_on_iphone = "Mobile" in uastring
            user_on_nexus = "Nexus 7" in uastring
            pageData = simplejson.dumps({'involvementOptions': biz.involvement_options.split('|') if biz.involvement_options else False,
                                         'businessName': biz.name,
                                         'withPublicSharingCheckbox': biz.with_public_sharing_checkbox,
                                         'user_on_iphone': user_on_iphone,
                                         'user_on_nexus': user_on_nexus,
                                         'business_code': resource,
                                         'displayDevice':  displayDevice}, sort_keys=True)
            script = """
                $(document).ready(function() {
                    $("#root").append(
                        G.controls.Home.create()
                            .pageData(%s)
                    )
                });
            """ % pageData
            self.response.out.write(myTemplate.addScript(script).buildPage())
        else:
            self.redirect('/notfound')

class PageNotFound(webapp.RequestHandler):
    def get(self):

        myTemplate = HtmlTemplate()

        myTemplate.addHeaders([
            "http://code.jquery.com/jquery-1.7.2.min.js",
            "/static/Archive/rating_screen_v1/css/styles.css"
        ])

        script = """
            $(document).ready(function() {
                $("#root").append(
                    $("<center>").append(
                        $("<div>").css({
                            'padding': '100px',
                            'color': 'white',
                            'font-size': '40px'
                        }).append('Not a valid Url')
                    )
                )
            });
        """
        self.response.out.write(myTemplate.addScript(script).buildPage())

class AddBusiness(webapp.RequestHandler):
    def get(self):

        myTemplate = HtmlTemplate()

        myTemplate.addHeaders([
            "http://quickui.org/release/quickui.catalog.css",
            "http://code.jquery.com/jquery-1.7.2.min.js",
            "http://quickui.org/release/quickui.js",
            "http://quickui.org/release/quickui.catalog.js",
            "/static/js/G.js",
            "/static/js/controls/submitButton.js",
            "/static/js/controls/textField.js",
            "/static/js/controls/select.js",
            "/static/js/controls/form.js",
            "/static/js/pages/addbusiness.js"
        ])

        email = self.request.get('email')
        name = self.request.get('name')
        offer = self.request.get('offer')
        url = self.request.get('url')
        kioware_passcode = self.request.get('kioware_passcode')
        involvementOptions = self.request.get('involvementOptions')
        with_public_sharing_checkbox = self.request.get('with_public_sharing_checkbox')

        if name:
            biz = Business(
                name=name,
                url=url,
                offer=offer,
                email=email,
                involvement_options=involvementOptions,
                kioware_passcode=kioware_passcode,
                with_public_sharing_checkbox= with_public_sharing_checkbox == 'Yes',
                active=True
            )
            biz.save()
            response = simplejson.dumps({"message":'Successful'}, sort_keys=True)
            self.response.out.write(response)
        else:
            script =  """
                $(document).ready(function() {
                    $("#root").append(
                        G.controls.AddBiz.create()
                    )
                });
            """

            self.response.out.write(myTemplate.addScript(script).buildPage())

class Dashboard(webapp.RequestHandler):
    def get(self):

        myTemplate = HtmlTemplate()

        myTemplate.addHeaders([
            "http://quickui.org/release/quickui.catalog.css",
            "http://code.jquery.com/jquery-1.7.2.min.js",
            "http://quickui.org/release/quickui.js",
            "http://quickui.org/release/quickui.catalog.js",
            "/static/js/G.js",
            "/static/js/pages/dashboard.js"
        ])


        biz_query = db.Query(Business).filter("active =", True).fetch(1000000)

        def getBizStats(days_back=0):
            bizs = {}
            for biz in biz_query:
                bizs[str(biz.key())] = {
                    'name': biz.name,
                    'url': biz.url,
                    'starSum': 0,
                    'rvrCount': 0,
                    'starAvg': 0,
                    'kioPass': biz.kioware_passcode
                }
            if days_back:
                n_days_ago = datetime.datetime.now() - datetime.timedelta(days = days_back)
                rvrs = db.Query(Review).filter("add_dt >", n_days_ago).fetch(1000000)
            else:
                rvrs = db.Query(Review).fetch(1000000)

            rvrsList = [rvr for rvr in rvrs]

            while rvrsList:
                rvr = rvrsList.pop()
                if rvr.business.active:
                    biz = bizs[str(rvr.business.key())]
                    biz['starSum'] += rvr.star_rating
                    biz['rvrCount'] += 1
                    biz['starAvg'] = round(biz['starSum'] / biz['rvrCount'], 2)

            return bizs

        stats = simplejson.dumps({"stats":getBizStats()}, sort_keys=True)
        statsPastDay = simplejson.dumps({"stats":getBizStats(1)}, sort_keys=True)

        script =  """
            $(document).ready(function() {
                $("#root").append(
                    $("<div>").css({
                        'font-size': '50px',
                        'padding': '25px',
                        'padding-left': '0px',
                        'text-align': 'left',
                        'font-family': 'arial'
                    }).append(
                        'Review Data'
                    ),
                    G.controls.Dashboard.create()
                        .statsTable(%s)
                        .title('All Time'),
                    G.controls.Dashboard.create()
                        .statsTable(%s)
                        .title('Past Day')
                )
            });
        """ % (stats, statsPastDay)

        self.response.out.write(myTemplate.addScript(script).buildPage())

class Reviews(webapp.RequestHandler):
    def get(self):

        myTemplate = HtmlTemplate()

        myTemplate.addHeaders([
            "http://quickui.org/release/quickui.catalog.css",
            "http://code.jquery.com/jquery-1.7.2.min.js",
            "http://quickui.org/release/quickui.js",
            "http://quickui.org/release/quickui.catalog.js",
            "/static/js/G.js",
            "/static/js/pages/reviews.js"
        ])


        biz_query = db.Query(Business).filter("active =", True).fetch(1000000)
        rvr_query = db.Query(Review).order('-add_dt').fetch(1000000)
        rvrer_query = db.Query(Reviewer).fetch(1000000)

        rows_by_review = []
        biz_map = {}
        rvrer_map = {}
        for biz in biz_query:
            biz_map[str(biz.key())] = {
                'name': biz.name
            }

        for rvrer in rvrer_query:
            rvrer_map[str(rvrer.key())] = {
                'email': rvrer.email,
                'agree_public_share': str(rvrer.agree_public_share),
                'business_involvement': rvrer.business_involvement
            }

        for rvr in rvr_query:
            try: 
                rvr.reviewer
                if rvr.business.active:
                    if biz_map[str(rvr.business.key())]['name'] != 'test':
                        rows_by_review.append(
                            {
                                'business_name': biz_map[str(rvr.business.key())]['name'],
                                'date': str(rvr.add_dt),
                                'star_rating': rvr.star_rating,
                                'reviewer_email': rvrer_map[str(rvr.reviewer.key())]['email'],
                                'agree_public_share': rvrer_map[str(rvr.reviewer.key())]['agree_public_share'],
                                'business_involvement': rvrer_map[str(rvr.reviewer.key())]['business_involvement'],
                                'feedback': rvr.feedback
                            }
                        )
            except datastore_errors.ReferencePropertyResolveError:
                logging.error('ReferenceProperty error')
            

        data = simplejson.dumps({"rows": rows_by_review}, sort_keys=True)

        script =  """
            $(document).ready(function() {
                $("#root").append(
                    G.controls.Reviews.create()
                        .dataTable(%s)
                        .title('Reviews')
                )
            });
        """ % data

        self.response.out.write(myTemplate.addScript(script).buildPage())

class Change(webapp.RequestHandler):
    def get(self):

        print 'hi'

class ValidateCode (webapp.RequestHandler):
    def get(self):

        code = self.request.get('code')
        biz = Business.all().filter('url = ', code).get()
        if biz == None:
            self.response.out.write(simplejson.dumps({"valid": False}))
        else:
            self.response.out.write(simplejson.dumps(
                {
                    "valid": True,
                    "business_name": biz.name,
                    "involvement": [op for op in biz.involvement_options.split('|')]
                }))

application = webapp.WSGIApplication(
                                     [
                                         ('/ajax', Ajax), 
                                         ('/addbiz', AddBusiness),
                                         ('/dashboard', Dashboard),
                                         ('/makechange', Change),
                                         ('/validatecode', ValidateCode),
                                         ('/notfound', PageNotFound),
                                         ('/reviewsdata', Reviews),
                                         ('/', PageNotFound),
                                         ('/m/([^/]+)?', MainPage),
                                         ('/t/([^/]+)?', MainPage)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
