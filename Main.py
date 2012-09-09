from google.appengine.ext import webapp
from HtmlTemplate import HtmlTemplate
from google.appengine.ext import db
import simplejson

myTemplate = HtmlTemplate()

myTemplate.addHeaders([
    "http://quickui.org/release/quickui.catalog.css",
    "/static/css/main.css",
    "http://code.jquery.com/jquery-1.7.2.min.js",
    "http://quickui.org/release/quickui.js",
    "http://quickui.org/release/quickui.catalog.js",
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
    "/static/js/pages/page.js",
    "/static/js/controls/submitButton.js",
    "/static/js/controls/textField.js",
    "/static/js/controls/TextArea.js",
    "/static/js/controls/reviewSectionHeader.js",    
    "/static/js/controls/reviewStep.js",
    "/static/js/controls/sitelink.js",
    "/static/js/pages/home.js",
    "/static/js/controls/reviewtextbox.js",
    "/static/js/pages/homeBtest.js",
    "/static/js/controls/iframe.js",
    "/static/js/controls/logoutbutton.js",
    "/static/js/controls/backbutton.js",
    "/static/js/pages/reviewsite.js"
])

class Review(db.Model):
    reviewer_id = db.StringProperty()
    review = db.StringProperty()
    star_rating = db.FloatProperty()
    add_dt = db.DateTimeProperty(auto_now=True)
    
class Reviewer(db.Model):
    email = db.StringProperty()
    add_dt = db.DateTimeProperty(auto_now=True)

class MainPage(webapp.RequestHandler):
    def get(self, resource):
        
        user_email = self.request.get('email')
        if user_email:
            reviewer = Reviewer()
            reviewer.email = user_email
            response = simplejson.dumps({"email":user_email}, sort_keys=True)
            self.response.out.write(response)
        else:
            if resource:
                if resource == "btest":
                    script = "G.controls.HomeB.create()"  
                else:              
                    script = "G.controls.ReviewSitePage.create()"
            else:
                script = "G.controls.Home.create()"
                    
            self.response.out.write(myTemplate.addScript(script).buildPage())  