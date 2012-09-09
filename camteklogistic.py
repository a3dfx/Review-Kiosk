import logging
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import mail
from google.appengine.api.datastore import Key
from google.appengine.ext.webapp.util import run_wsgi_app
import random
import datetime
import hashlib
import simplejson

from google.appengine.api import mail

class User(db.Model):
    name = db.StringProperty()
    email = db.StringProperty()
    password = db.StringProperty()
    valid = db.BooleanProperty()

class Session(db.Model):
    user_name = db.StringProperty()
    session_id = db.StringProperty()
    add_dt = db.DateTimeProperty(auto_now=True)

class Part(db.Model):
    desctwo = db.StringProperty()
    price = db.StringProperty()
    
class InvPart(db.Model):
    name = db.StringProperty()
    qty = db.IntegerProperty()
    location = db.StringProperty()
    shelf = db.StringProperty()

class PartOrder(db.Model):
    orderkey = db.IntegerProperty()
    user = db.StringProperty()
    part = db.TextProperty()
    partlog = db.TextProperty()
    purchase_order = db.StringProperty()
    service_ticket = db.StringProperty()
    quotation_num = db.StringProperty()
    contract = db.StringProperty()
    customer = db.StringProperty()
    urgency = db.StringProperty()
    status = db.StringProperty()
    date = db.DateProperty()
    completion_date = db.DateProperty()
    pending = db.BooleanProperty()
    user_status = db.BooleanProperty()
    

class OrderByItem(db.Model):
    orderkey = db.IntegerProperty()
    user = db.StringProperty()
    part = db.StringProperty()
    part_log = db.TextProperty()
    part_index = db.IntegerProperty() 
    price = db.StringProperty()
    customer = db.StringProperty()
    purchase_order = db.StringProperty()
    service_ticket = db.StringProperty()
    quotation_num = db.StringProperty()
    contract = db.StringProperty()
    date = db.DateProperty()
    openqty = db.IntegerProperty() 
    orderedqty = db.IntegerProperty()  
    startqty = db.IntegerProperty() 
    
class Address(db.Model):
    name = db.StringProperty()
    company = db.StringProperty()
    country = db.StringProperty()
    address = db.StringProperty()
    addresstwo = db.StringProperty()
    city = db.StringProperty()
    zip = db.StringProperty()
    phone = db.StringProperty()
    state = db.StringProperty()

def complete_list_divider(page_num, list_complete_orders):
    
    complete_order_list = '<a id="totalordercount">' + str(len(list_complete_orders)) + '</a>'
    

    for order in list_complete_orders[(page_num - 1)*7:(page_num*7)]:
    
        query4 = OrderByItem.all()
        list_of_parts_by_order = query4.order('part_index').filter('orderkey = ', order.orderkey).fetch(50)
        
        part_qty_table = '<table class="parttable"><tbody>'
        for part in list_of_parts_by_order:
            part_qty_table += str(part.part_log)
        part_qty_table += '</tbody></table>'     
             
        complete_order_list += '<tr><td>%s</td><td>%s</td><td style="width:40">%s</td><td style="width:40">%s</td><td>%s</td><td>%s</td><td>%s</td><td class="partcell">%s</td><td style="width:10">%s</td><td>%s</td><td>%s</td></tr>' % (order.orderkey, order.user, order.customer, order.contract, order.purchase_order, order.service_ticket, order.quotation_num, part_qty_table, order.urgency, order.date, order.completion_date)           
    
    return complete_order_list

def page_count_maker(page_num, list_complete_orders):    
    pageview = ''
    pagecount = 0
    for i in xrange(len(list_complete_orders)):
        if i % 7 == 0:
            pagecount += 1
            if pagecount == page_num:
                pageview += ' <td class="pagenumtd" style="font-size:18px">' + str(pagecount) + '</td>'
            else:
                pageview += ' <td class="pagenumtd"><a class="pagenums" href="/complete?page=' + str(pagecount) + '">' + str(pagecount) + '</a></td>' 
            
    
    if pagecount == 1:
        pageview += '</td></tr></tbody></table>' 
    else:            
        if pagecount == page_num:            
            pageview += '</td></tr></tbody></table>'
            pageview = '<table class="pagenumtable"><tbody><tr><td class="pagenumtd"><a class="pagenums" href="/complete?page=' + str(page_num - 1) + '">previous</a></td>' + pageview
        else:
            pageview += ' <td class="pagenumtd"><a class="pagenums" href="/complete?page=' + str(page_num + 1) + '">next</a></td></tr></tbody></table>'
            pageview = '<table class="pagenumtable"><tbody><tr>' + pageview
    
    return pageview    
                            

    
# property converter function
def pc(prop):
    new_prop = ''
    if prop == "Contract":
        new_prop = "contract"
    if prop == "User":
        new_prop = "user"
    if prop == "Customer":
        new_prop = "customer"
    return new_prop
    
def filter_table_maker(filter_option_list, filter_by_list, filters_added):
    complete_orders = ''
    query = PartOrder.all()
    
    for i in xrange(int(filters_added) + 1):
        if int(filters_added) == 0:
            fop = pc(filter_option_list)
            fby = filter_by_list
        else:
            fop = pc(filter_option_list.split('$')[i])
            fby = filter_by_list.split('$')[i]
            
        query = query.order('orderkey').filter('pending = ', False).filter(fop + ' = ', fby)
    
    complete_orders_by_filter = query.fetch(10000)    

    complete_orders = '<a id="totalordercount">' + str(len(complete_orders_by_filter)) + '</a>'  
    for order in complete_orders_by_filter:
    
        query4 = OrderByItem.all()
        list_of_parts_by_order = query4.order('part_index').filter('orderkey = ', order.orderkey).fetch(50)
        
        part_qty_table = '<table class="parttable"><tbody>'
        for part in list_of_parts_by_order:
            part_qty_table += str(part.part_log)
        part_qty_table += '</tbody></table>'     
             
        complete_orders += '<tr><td>%s</td><td>%s</td><td style="width:40">%s</td><td style="width:40">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td style="width:10">%s</td><td>%s</td><td>%s</td></tr>' % (order.orderkey, order.user, order.customer, order.contract, order.purchase_order, order.service_ticket, order.quotation_num, part_qty_table, order.urgency, order.date, order.completion_date)

    return complete_orders      
        
def filter_option_maker(type, filter_option_list, filter_by_list, filters_added):
    filters_added = int(filters_added) - 1
    type_options = ''
    type_array = []
    query = PartOrder.all()
    
    if filters_added == -1:
        query = query.order('orderkey').filter('pending = ', False)
    else:
        for i in xrange(filters_added + 1):
            if filters_added == 0:
                fop = pc(filter_option_list)
                fby = filter_by_list
            else:
                fop = pc(filter_option_list.split('$')[i])
                fby = filter_by_list.split('$')[i]
                
            query = query.order('orderkey').filter('pending = ', False).filter(fop + ' = ', fby)
    
    order_list = query.fetch(10000)
    
    for order in order_list:
        if type == "customer":
            type_array.append(order.customer)
        elif type == "contract":
            type_array.append(order.contract)
        elif type == "user":
            type_array.append(order.user)        
    type_set = list(set(type_array))
    type_set.sort()
    for unit in type_set:
        type_options += "<option>" + unit + "</option>"

    filters_added += 1    
    if type_options:
        page = '  --  <a class="filterpath" id="filterdescby' + str(filters_added) + '"><select id="filter_by' + str(filters_added) + '">' + type_options + '</select></a> >>> <a id="filteraddbutton' + str(filters_added) + '"><input type="button" value="Add Filter" onclick="filter_adder(' + str(filters_added) + ')"/></a> <br/><br/>'
    else:
        page = ''   
    return page

def login_code(user_cookie):
    
    queryz = Session.all()
    log_section = ''
    session = queryz.order('-add_dt').filter('session_id = ', user_cookie).fetch(1)
    reg_section = """
            Name:  <input type="text" id="usernamelogin" style="width:80px" /><span>&nbsp&nbsp</span>
            Password:  <input type="password" id="passwordlogin" style="width:80px" />
            <input type="button" onclick="user_submit('login')" value="Log in" id="loginsubmit" />
            <div id="loginstatusdiv">
            </div>  
        """
    returning_user = '' 
    if user_cookie:
        if session:
            returning_user = session[0].user_name
            if returning_user != "No Name":
                query = User.all()
                user = query.filter('name = ', returning_user).fetch(1)[0]
                if user.valid == False:
                    reg_section = '<font size="3" color=red>Waiting for site admin to validate your account... &nbsp&nbsp<a href="#" id="logout">Logout</a></span></font>'
                    returning_user = ''
                else:
                    reg_section = '<font size="3">Welcome, ' + returning_user + '&nbsp|&nbsp&nbsp<a href="#" id="logout">Logout</a></span></font>'
             
    return [reg_section, returning_user] 
    
def cookie_bake():                
    session_id = "name=%s" % str(random.randint(1000000000, 100000000000))
    return session_id

    
def parts_info_edit(fetch_length, part_selected, selected_parts):
    if fetch_length:
        page = ""
        for i in xrange(fetch_length):
            if selected_parts[i].shelf:
                page += '<a id="partinfo%s">%s - %s - %s - %s <br/></a>' % (str(i), part_selected, selected_parts[i].location, selected_parts[i].shelf, str(selected_parts[i].qty))    
            else:
                page += '<a id="partinfo%s">%s - %s - %s <br/></a>' % (str(i), part_selected, selected_parts[i].location, str(selected_parts[i].qty))    
    else:
        page = '%s' % (part_selected)
    return page
    
def parts_info_shipped(fetch_length, part_selected, selected_parts):
    if fetch_length:
        page = ""
        for i in xrange(fetch_length):
            page += '<div id="partshipdiv%s"><a id="partship%s">%s</a> - <a id="locationship%s">%s</a> - <a id="qtyship%s">%s</a></div>' % (str(i), str(i), part_selected, str(i), selected_parts[i].location, str(i), str(selected_parts[i].qty))    
    else:
        page = "<b>Part not in inventory</b>"
    return page    

def	parts_info_cart(fetch_length, selected_parts):
    if fetch_length:

        key = db.Key.from_path('Part', selected_parts[0].name)
        part = db.get(key)
        if part:
            price = part.price
            page = "</br><b>Price:</b> $%s<br/><br/>" % (price)
        else:
            page = "</br><b>Price:</b> Not Available<br/><br/>"
        for i in xrange(fetch_length):
            if selected_parts[i].shelf:
                page += 'Location: %s <br/> Itur: <a id="itur">%s</a> <br/> Qty: %s <br/><br/>' % (selected_parts[i].location, selected_parts[i].shelf, str(selected_parts[i].qty))
            else:
                page += 'Location: %s <br/> Qty: %s <br/><br/>' % (selected_parts[i].location, str(selected_parts[i].qty))
    else:
        page = "<br/><br/><b>Part not in database</b>"
    return page

    
def make_secure_password(plaintext, salt=None):
    salt = salt or ''.join(
        random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for i in range(5)
    )  
    return '$'.join((
        'sha1',
        salt,
        hashlib.sha1((salt + plaintext).encode()).hexdigest()
    )) 

def check_user_password(hashpass, password):
    algo, salt, hsh = hashpass.split('$')
    return hashpass == make_secure_password(password, salt) 

error_page = """
                <html>
                    <head>
                        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                        <script src="/static/main.js"></script>
                        <script src="/static/login.js"></script>
                        <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                        <title>
                            Camtek Logistics
                        </title>
                    </head>            
                        <body>
                        <center>
                                <div id="mainheader"></div>
                            </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                            <br/>
                            <br/>
                            <center><span style="color:red">You must be logged in to visit this page</span>
                            <br/><br/><a href="/login">Don't have an account? Register here</a>
                            </center>
                        </body>
                    </html>
                
                """ 
    
	
class MainPage(webapp.RequestHandler):
    def get(self):
        query = Session.all()
        reg_section = ''
        log_section = ''

        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie) 

        
        page = """
                <html>
                    <head>
                        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                        <script src="/static/order.js"></script>
                        <script src="/static/main.js"></script>
                        <script src="/static/login.js"></script>
                        <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                        <title>
                            Camtek Logistics Home
                        </title>
                    </head>            
                        <body>
                        <center>
                            <div id="mainheader"></div>
                            </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                            <center>
                            <table>
                                <tbody>
                            <tr><td><img src="/static/eagle.png"></td>
                            <td align=center><font size="8" face="Century Gothic">The Eagle</font><br/>
                            <font size="3"><i>Camtek's Logistics Application</i></font></td></tr>
                            </tbody></table>
                            
                        <table class="bordermain" border="0" style="vertical-align:bottom;background-color:#8B8DEB;cell-spacing:20px;height:400px;" align=CENTER>
                        <tbody><tr>                           
                        <td>    
                        <table class="border" border="0" style="vertical-align:bottom;background-color:#D2D7EA;width:250px" align=CENTER>
                        <tbody><tr>
                            <td class="homepage"><img src="/static/art.png"></td>
                        </tr>
                        </tbody></table>
                        </td>
                        <td>
                        <table class="border" border="0" style="vertical-align:bottom;background-color:#D2D7EA;width:280px" align=CENTER>
                        <tbody><tr>    
                            <td class="homepage"><font face="arial">
                            Welcome to The Eagle, Camtek's logistics application. This application is devoted to automizing and organizing part orders
                            made by Camtek engineers and associates.<br/><br/>
                            The Eagle provides an interface for users to update orders in real-time, make part orders, track pending orders and view a list of parts.<br/><br/>
                            The system sends users automatic email updates with the progress of their pending orders.<br/><br/>
                            Put simply, The Eagle makes part ordering a whole lot easier.</font>
                            
                        </tr>
                        </tbody></table>   
                            </center>
                        </td>                
                        <td>
                        <table class="border" border="0" style="vertical-align:bottom;background-color:#D2D7EA;width:250px" align=CENTER>
                        <tbody><tr>    
                            <td class="homepage">
                            <span style="font-size:20;" face="arial"><b>Register Today</b></span> <br/><br/>
                            Name: <br/><input type="text" id="usernameregister" style="width:200px" /><br/><br/>
                            Email: <br/><input type="text" id="emailregister" style="width:200px" /><br/><br/>
                            Password: <br/><input type="password" id="passwordregister" style="width:200px" /><br/><br/>
                            Verify Password: <br/><input type="password" id="passwordregisterverify" style="width:200px" /><br/><br/>
                            <input type="button" onclick="user_submit('register')" value="Register" id="registersubmit" />
                            <br/><br/>
                            <div id="registerstatusdiv">
                            </div>                          
                        </tr>
                        </tbody></table>   
                            </center>
                        </td>
                                
                        </tr>
                        </tbody></table>
                        <div align=center id="footer">
                            <br/>
                            <font size="3" color=gray><span>&copy; 2011 </span> Lior Gotesman</font>
                        </div>
                        </body>
                    </html>
                
                """  % {
                "reg_section":reg_section
            }


        self.response.out.write(page)  
             
        
class Order(webapp.RequestHandler):
    def get(self):
        
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
        
        if returning_user:
            part_selected = self.request.get("part")
            throughajax = self.request.get("throughajax")
            part_added = self.request.get("part_added")
            desctwo_fetch = self.request.get("desctwo")
            list_change = self.request.get("list_change")
            change_count = self.request.get("change_count")
            
            address_changed = self.request.get("address_changed")
            
            
            query = InvPart.all()
            
            list_of_parts = query.fetch(1000)
            list_of_parts.sort(key=lambda part: part.name)
            list_of_part_names = ["<option>" + part.name + "</option>" for part in list_of_parts]
            list_of_qty = ["<option>" + str(qty) + "</option>" for qty in xrange(1, 21)]
            
            query1 = PartOrder.all()
            last_order_key = query1.order('-orderkey').fetch(1)[0].orderkey
            new_order_key = str(last_order_key + 1)
            
            query2 = User.all()
            user_email = query2.filter('name = ', returning_user).fetch(1)[0].email
            
            query3 = InvPart.all()
            
            query4 = Address.all()
            list_of_addresses = query4.fetch(1000)
            list_of_addresses.sort(key=lambda address: address.name)
            list_of_address_names = ["<option>" + address.name + "</option>" for address in list_of_addresses] 

            query5 = Address.all()            
            list_of_addresses1 = query5.fetch(1000)
            list_of_addresses1.sort(key=lambda address: address.company)
            list_of_address_companies = ["<option>" + address.company + "</option>" for address in list_of_addresses1]

            if address_changed:
                filter_by = self.request.get("filter_by")
                value = self.request.get("value")
                query6 = Address.all()
                contact = query6.filter(filter_by + ' = ', value).fetch(1)
                address_data = simplejson.dumps({"name":contact[0].name, "company":contact[0].company, "country":contact[0].country, "address":contact[0].address, "addresstwo":contact[0].addresstwo, "city":contact[0].city, "state":contact[0].state, "zip":contact[0].zip, "phone":contact[0].phone}, sort_keys=True)
                self.response.out.write(address_data)
            
            elif part_selected and not desctwo_fetch:
                selected_parts = query3.filter('name = ', part_selected).fetch(10)
                page = parts_info_cart(len(selected_parts), selected_parts)	
                
                self.response.out.write(page)
            elif desctwo_fetch:
                key = db.Key.from_path('Part', part_selected)
                part_name = db.get(key)
                if part_name:
                    desctwo = part_name.desctwo
                    page = "<i>" + desctwo + "</i>"
                    if not desctwo:
                        page = "No 2nd description"
                else:
                    page = "No 2nd description"

                self.response.out.write(page)            
            elif part_added or list_change:
                if int(change_count) % 2 == 0:
                    page = """<select id="partbox"><option></option><option>*** Add part manually ***</option><option></option>%(list_of_part_names)s</select>
                    """ % {
                                "list_of_part_names":list_of_part_names,
                                "list_of_qty":list_of_qty
                            }
                    self.response.out.write(page)    
                else:
                    query = Part.all()
                    list_of_parts = query.fetch(10000)
                    list_of_parts.sort(key=lambda part: part.key().name())
                    list_of_part_names = ["<option>" + part.key().name() + "</option>" for part in list_of_parts]
                    page = """<select id="partbox"><option></option><option>*** Add part manually ***</option><option></option>%(list_of_part_names)s</select>
                        """ % {
                            "list_of_part_names":list_of_part_names,
                            "list_of_qty":list_of_qty
                        }                    
                
                    self.response.out.write(page)        
            else:
                page = """
                
                    <html>
                        <head>
                            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                            <script src="/static/order.js"></script>
                            <script src="/static/main.js"></script>
                            <script src="/static/login.js"></script>
                            <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                            <title>
                                Order Form
                            </title>
                        </head>            
                            <body>
                            <center>
                                <div id="mainheader"></div>
                            </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                            <br/>
                            <center>
                                <span style="font-size:30;color:darkblue;">%(returning_user)s's order number: %(new_order_key)s</span>
                            </center>
                            <br/>
                            <table class="borderorder" border="0" align=CENTER>
                                <tbody>
                                <tr><td style="vertical-align:top">
                            <table class="step1" width="750px" align=center>
                                <tbody>
                                <tr><td colspan="2" class="step1td" style="text-align:center;padding:5px;">
                                    <font size="4" face="arial">Step 1 - Order information</font><br/><font size="2" color=gray>* Denotes required field</font><br/>                             
                                </td></tr><tr>
                                    <td style="vertical-align:top;padding-left:60px;padding-top:9px">
                                        <center>
                                            <br/>Enter Order Information<br/>
                                            <hr />

                                        </center>
                                        <font color="#3C3B3B">
                                        *Customer Name: <br/><a id="customerselectarea"><select id="customerbox"><option></option><option>*** Add manually ***</option><option></option><option>For stock</option><option>For office demo tool</option><option></option><option>3M</option><option>Accurate Circuit </option><option>Accurate Circuit Engineering</option><option>American Circuit Technology</option><option>Amitron</option><option>Candor Industries Inc. - Renewal</option><option>Cartel Electronic</option><option>Compro Business Services</option><option>Cosmotronics co</option><option>Cree</option><option>Crimp</option><option>DRS Sensors</option><option>Dynamic &amp; Proto</option><option>Endicott Interconnect</option><option>Fineline Circuits</option><option>Firan Technology</option><option>Global Innovation</option><option>Holaday Circuits</option><option>ISU Petasys Corp.</option><option>KCA</option><option>Kodak</option><option>Metaplast</option><option>MicroConnex</option><option>Minco</option><option>Multek -MN</option><option>Multicircuits</option><option>Peregrine Semiconductor</option><option>PhoTronics</option><option>Price Printed Circuits</option><option>RF Micro Devices</option><option>SVTC Technologies, LLC</option><option>Samtec</option><option>Sierra Proto Exp</option><option>Sierra Proto</option><option>Streamline Circuits</option><option>TTM Technologies</option><option>Texas Instruments Inc.</option><option>Texas Instruments Inc</option><option>The Bernd Group</option><option>Unicircuit Inc.</option><option>United Electronics</option><option>Universal </option><option>Vermont Circuits</option><option>Viasystems Corp.</option><option>W-Tek</option><option>Winonics (Brea) Renewal</option></select></a><br><br>
                                        *Machine Type and Serial#: <br/><input type="text" style="width:150px" id="machinebox"><br><br>          
                                        *Contract Status: <br/><select id="contractbox"><option></option><option>Service Contract</option><option>Warranty</option><option>Time and Material</option><option>Part Purchase Only</select><br><br>              
                                        *CIS Service Ticket #: <br/><input type="text" style="width:150px" id="scbox"><br><br> 
                                        <div id="po_sc_div" style="padding-left:60px;"></div>
                                        *Urgency Level: <br/><select id="urgentbox"><option></option><option>Machine down</option><option>High</option><option>Low</option></select><br/><br/><br/>
                                        Extra Notes<br><textarea style="width: 240px; height: 100px;" id="notebox" name="comments"></textarea><br/><br/>                                     
                                        </font>
                                        </td>         
                                        <td style="vertical-align:top;margin-left:30px">
                                        <table style="margin-left:50px"><tr><td colspan="2" style="vertical-align:top;">
                                            <center>
                                                <br/>Enter Ship-To Address <a id="address_button"></a><br/><hr /></tr></td>
                                            <tbody>
                                                <tr><td class="addresstable">*Name:</td> <td class="addresstable1" id="name_field"><select id="dnameselect"><option>Select</option>%(list_of_address_names)s</select><td/></tr> 
                                                <tr><td class="addresstable">*Company:</td> <td class="addresstable1" id="company_field"><select id="dcompanyselect"><option>Select</option>%(list_of_address_companies)s</select><td/></tr>  
                                                <tr><td class="addresstable">*Country:</td> <td class="addresstable1"><input type="text" style="width:100px" id="dcountry"><td/></tr>  
                                                <tr><td class="addresstable">*Address 1:</td> <td class="addresstable1"><input type="text" style="width:200px" id="daddress1"><td/></tr>  
                                                <tr><td class="addresstable"><span>&nbsp</span>Address 2:</td> <td class="addresstable1"><input type="text" style="width:200px" id="daddress2"><td/></tr>  
                                                <tr><td class="addresstable">*City:</td> <td class="addresstable1"><input type="text" style="width:150px" id="dcity"><td/></tr> 
                                                <tr><td class="addresstable">*State:</td> <td class="addresstable1"><input type="text" style="width:50px" id="dstate"><td/></tr>
                                                <tr><td class="addresstable">*Zip Code:</td> <td class="addresstable1"><input type="text" style="width:75px" id="dzip"><td/></tr>
                                                <tr><td class="addresstable">*Phone #:</td> <td class="addresstable1"><input type="text" style="width:100px" id="dphone"><td/></tr>
                                                <tr><td class="addresstable">*Shipper:</td> <td class="addresstable1"><select id="dshipper"><option>Select</option><option>Fedex</option><option>UPS</option></select><td/></tr>                                                
                                                <tr><td class="addresstable">*Service Type:</td> <td class="addresstable1"><select id="dservice"><option>Select</option><option>First overnight</option><option>Priority overnight</option><option>Standard overnight</option><option>2Day</option><option>2Day AM</option><option>Express Saver</option><option>Ground</option></select><td/></tr>
                                        </tbody></table>
                                            </center>                                        
                                        <div style="margin-left:80px"><br/><input type="checkbox" id="saveaddress"><font color=darkblue> Save new contact to address book</font></div>    
                                        </td>
                                        </td></tr>
                                        <tr><td>
                                        
                                        </tbody></table> 
                                        <br/><br/>
                            <table class="step2" border="0" style="vertical-align:top;">
                                <tbody> 
                                <tr><td colspan="2" class="step1td" style="text-align:center;padding:5px;">
                                    <font size="4" face="arial">Step 2 - Add parts to cart</font><br/>                             
                                </td></tr><tr>
                                    <tr><td style="vertical-align: top;">  
                                        <br/>
                                        <div style="margin-left:50px;vertical-align:top;" id="cartbox" width="720px">
                                        <center>
                                        <a id="liststatus" style="font-size:12;color:red"></a>
                                        </center>
                                        Part and Part Description: <a id="inputfield"><select id="partbox"><option></option><option>*** Add part manually ***</option><option></option>%(list_of_part_names)s</select></a>           
                                            Qty: <select id="qtybox">%(list_of_qty)s</select>
                                            <input type="button" value="Add To Cart" id="partaddbutton" onclick="new_part()"</br>
                                            <form>
                                            <a id="inventoryradio"></a>
                                            <input type="radio" id="radioparts" name="partlist" value="allparts" /><span style="font-size:12">All Parts</span>
                                            </form>                                                                       
                                    </td></tr>

                                    
                                    <tr><td align=center>
                                        <table class="partinfo" border="0" align=LEFT>
                                            <tbody>
                                            <td><div id="infotitle" align="CENTER"></td>
                                            <tr>
                                            <td></td>
                                            <td align="RIGHT" style="text-align:left;" id="desctwo"></td>
                                            </tr>
                                            <td style="vertical-align:top">
                                            <div id="partinfodiv" style="margin-left:10px;"></div></td>
                                            <td><div id="part_picture"></div></td>
                                            <td><a id="loadingimg"></a></td>
                                            </tr><td>
                                            <td style="vertical-align: top;">
                                            </td><td style="vertical-align: bottom;">
                                            </td>
                                            </tr>
                                        </tbody></table>
                                    </td></tr>

                                    <tr><td>
                                        <table border="0" style="vertical-align:top;">
                                            <tbody><tr>                                    
                                                <td style="vertical-align:top">
                                                    <img style="margin-left: 75px" src="/static/cartpic.PNG"><i><font size="5">Your cart</font></i>:<br><br>
                                                    <div id="partcartdiv" style="margin-left: 210px;">   
                                                    </div>
                                                    <div style="margin-left:275px;" id="emptycart"><font color="gray">Your cart is empty</font></div>  
                                            </td>    
                                            </tr>
                                            <tr>
                                            <br/>
                                            <br/>
                                            <td>
                                            <br/>
                                            <br/>
                                            <input type="button" onclick="submit_request()" value="Submit order" id="submit_button">
                                            </td></tr>
                                        </tbody></table>                                    
                            </td>
                        </tbody></table> 


                            <div id="returningusername">%(returning_user)s</div>
                            <div id="returninguseremail">%(user_email)s</div>                            
                            <div id="nextorderkeydiv">%(new_order_key)s</div>
                            </div>
                        </body>   
                    </html>
                    
                    """ % {
                        "list_of_part_names": list_of_part_names,
                        "list_of_qty":list_of_qty,
                        "new_order_key":new_order_key,
                        "reg_section":reg_section,
                        "returning_user":returning_user,
                        "user_email":user_email,
                        "list_of_address_names":list_of_address_names,
                        "list_of_address_companies":list_of_address_companies
                    }
                    
                self.response.out.write(page)
        else:
            page = error_page % {
                        "reg_section":reg_section
                    }
                
            
            self.response.out.write(page)

class OrderSubmit(webapp.RequestHandler):
    def get(self):
        
        email = self.request.get("email")
        name = self.request.get("name")
        customer = self.request.get("customer")
        machine = self.request.get("machine")
        contract = self.request.get("contract")
        partslog = self.request.get("partslog")	
        partsemail = self.request.get("partsemail")
        urgent = self.request.get("urgent")
        note = self.request.get("note")
        po = self.request.get("po")
        sc = self.request.get("sc")
        quote = self.request.get("quote")
        tracking = self.request.get("tracking")
        
        dname = self.request.get("dname")
        company = self.request.get("company")
        country = self.request.get("country")
        address1 = self.request.get("address1")
        address2 = self.request.get("address2")
        city = self.request.get("city")	
        state = self.request.get("state")
        zip = self.request.get("zip")
        phone = self.request.get("phone")
        shipper = self.request.get("shipper")
        service = self.request.get("service")
        save_contact = self.request.get("save_contact")
        
        parts_to_part_log = self.request.get("parts_to_part_log")
        qty_to_part_log = self.request.get("qty_to_part_log")
        
        part_list = parts_to_part_log.split("$")
        qty_list = qty_to_part_log.split("$")
        
        order = PartOrder()
        query = PartOrder.all()
        last_order_key = query.order('-orderkey').fetch(1)[0].orderkey
        nok = last_order_key + 1
    
        if parts_to_part_log:
            for i in xrange(len(part_list)):
                item = OrderByItem()
                
                key = db.Key.from_path('Part', part_list[i])
                partstock = db.get(key)
                if partstock:
                    item.price = "$" + partstock.price
                else:
                    item.price = "Not Available"       
                    
                item.part_log = '<tr><td class="parttd" id="order%sdiv%s"><a id="order%spart%s">%s</a><a id="t%spart%s"></a></td><td class="qtycell" id="part%sqty%s">%s</td></tr>' % (nok, i + 1, nok, i + 1, part_list[i], nok, i + 1, nok, i + 1, int(qty_list[i]))
                item.part = part_list[i]
                item.openqty = int(qty_list[i])
                item.orderedqty = int(qty_list[i])
                item.startqty = int(qty_list[i])
                item.part_index = i
                item.date = datetime.datetime.now().date()
                item.user = name
                item.customer = customer
                item.contract = contract
                item.purchase_order = po
                item.service_ticket = sc
                item.quotation_num = quote
                item.orderkey = nok
                
                item.put()

        

        contact = Address()
            
        if save_contact == "true":
            contact.name = dname
            contact.company = company
            contact.country = country
            contact.address = address1
            contact.addresstwo = address2
            contact.city = city
            contact.state = state
            contact.zip = zip
            contact.phone = phone
            
            contact.put()
        
        
        order.pending = True
        order.date = datetime.datetime.now().date()
        order.completion_date = datetime.datetime.now().date()
        order.user = name
        order.customer = customer
        order.contract = contract
        order.part = partslog
        order.partlog = partsemail
        order.urgency = urgent
        order.purchase_order = po
        order.service_ticket = sc
        order.quotation_num = quote
        order.user_status = False
        order.orderkey = last_order_key + 1

        order.put()
        
        lioremail = "Camtek Logistics <liorgott@gmail.com>"
        
        if mail.is_email_valid(email):
            subject = "Hi, %s, here is your order with ID %s" % (name, str(order.orderkey))
            body = """
Order Information 
 
    Customer...%(customer)s
    Machine...%(machine)s
    Contract...%(contract)s
    Purchase Order #...%(po)s
    Service Ticket #...%(sc)s
    Quotation #...%(quote)s
    Shipping Account #...%(tracking)s
    Parts...%(partsemail)s
    Urgency...%(urgent)s

Ship-to Address

    Name...%(dname)s
    Company...%(company)s
    Country:...%(country)s
    Address1...%(address1)s
    Address2...%(address2)s
    State...%(state)s
    City...%(city)s	
    Zip...%(zip)s
    Phone...%(phone)s
    Shipper...%(shipper)s
    Service...%(service)s

Extra Notes: %(note)s

            """ % {
                "customer":customer,
                "machine":machine,
                "contract":contract,
                "partsemail":partsemail,
                "urgent":urgent,
                "po":po,
                "sc":sc,
                "quote":quote,
                "note":note,
                "tracking":tracking,
                "dname":dname,
                "company":company,
                "country":country,
                "address1":address1,
                "urgent":urgent,
                "address2":address2,
                "city":city,
                "state":state,
                "zip":zip,
                "phone":phone,
                "shipper":shipper,
                "service":service                
            }
            
            mail.send_mail(lioremail, email, subject, body)
            
            subject = "%s made a new order with ID %s" % (name, str(order.orderkey))
            mail.send_mail(lioremail, lioremail + ", <howardk@camtekusa.com>" , subject, body)            
            




class ListEdit(webapp.RequestHandler):
    def get(self):
        part_selected = self.request.get("selected_part")
        modification_selected = self.request.get("mod")
        mod_loc = self.request.get("loc")
        mod_part = self.request.get("part")
        mod_qty = self.request.get("qty")
        new_itur = self.request.get("new_itur")
        new_location_picked = "True"
        part_modified = ""
        page = ""
        query = InvPart.all()
        
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie) 
        
        if returning_user:
            if mod_loc:
                part_modified = "True"
                mod_entity = query.filter('name = ', mod_part).filter('location = ', mod_loc).fetch(1)
                if mod_entity:
                    new_location_picked = ""
                  
                    
            list_of_parts = query.fetch(1000)
            list_of_parts.sort(key=lambda part: part.name)
            list_of_part_names = ["<option>" + part.name + "</option>" for part in list_of_parts]
            


                    
            if part_selected:
                query1 = InvPart.all()
                parts_to_delete = query1.filter('name = ', part_selected).filter('qty < ', 1).fetch(10)
                if parts_to_delete:
                    for key in parts_to_delete:
                        db.delete(key) 
                        
                selected_parts = query.filter('name = ', part_selected).fetch(10)
                page = parts_info_edit(len(selected_parts), part_selected, selected_parts)
                self.response.out.write(page) 

            elif part_modified:
                if new_location_picked:
                    if modification_selected == "increase":
                        p = InvPart()
                        p.name = mod_part
                        p.location = mod_loc
                        p.qty = int(mod_qty)
                        db.put(p)
                        page = "<br/>%s has been added to inventory in %s's warehouse with qty %s" % (p.name, p.location, str(p.qty))
                    elif modification_selected == "reduction":
                        page = '<script>alert("Part does not exist in that location, cannot reduce")</script>' 
                    elif modification_selected == "itur_change":
                        page = '<script>alert("Part does not exist in that location, cannot change itur")</script>' 
                else:
                    if modification_selected == "increase":
                        old_qty = mod_entity[0].qty   
                        new_qty = old_qty + int(mod_qty)
                        mod_entity[0].qty = new_qty
                        db.put(mod_entity)
                        page = "<br/>%s now has the qty %s in %s's warehouse" % (mod_part, str(new_qty),  mod_loc)
                    elif modification_selected == "reduction":
                        old_qty = mod_entity[0].qty  
                        new_qty = old_qty - int(mod_qty)
                        mod_entity[0].qty = new_qty
                        db.put(mod_entity)
                        page = "<br/>%s now has the qty %s in %s's warehouse" % (mod_part, str(new_qty), mod_loc)   
                    elif modification_selected == "itur_change":
                        mod_entity[0].shelf = new_itur
                        db.put(mod_entity)
                        page = "<br/>%s now has the itur %s" % (mod_part, new_itur)
                        
                self.response.out.write(page)             
            else:
                page = """
                
                    <html>
                        <head>
                            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                            <script src="/static/edit.js"></script>
                            <script src="/static/main.js"></script>
                            <script src="/static/login.js"></script>
                            <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                            <title>
                                Part List Edit
                            </title>
                        </head>
                        <body>
                            <center>
                                <div id="mainheader"></div>
                            </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                            <br/>
                            <br/>
                            <table class="border" align=CENTER width=700px style="background-color: #D8D3F8;"><tbody><tr><td>
                            <font size="6" face="arial">Edit Parts List</font><br><br>
                            <div style="vertical-align:top;">
                                Part to edit: <div id="partlistdiv"><select id="partbox"><option></option><option>*** Add part manually ***</option><option></option>%(list_of_part_names)s</select></div><br/>
                                <form>
                                <a id="inventoryradio"></a>
                                <input type="radio" id="radioparts" name="partlist" value="allparts" /><span style="font-size:12">All Parts</span>
                                </form><br/>
                                <div id="selectedpartdiv" style="margin-left:10px">
                                </div><br/>
                                <div id="edit_options">
                                </div>
                                <br/>
                                <div id="editdiv">
                                </div>
                                <div id="modnotification">
                                </div>
                            </div>
                            </td></tr>
                            </tbody></table>
                        </body>
                    </html> 
                """ % {
                    "list_of_part_names":list_of_part_names,
                    "reg_section":reg_section
                }
            
                self.response.out.write(page)
        else:
            page = error_page % {
                        "reg_section":reg_section,
                        "log_section":log_section
                    }
                
            
            self.response.out.write(page)            
                

class UserPage(webapp.RequestHandler):
    def get(self):
    
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)  
        qty_open = self.request.get('qty_value')
        order_id = self.request.get('id')
        part_index = self.request.get('part_index') 
        part_returned = self.request.get('part_shipped') 
        
        
        
        query = PartOrder.all()
        query1 = PartOrder.all()
        query2 = PartOrder.all()
        

        
        if returning_user:
            
            if part_returned:
                query3 = OrderByItem.all()
                part_edited = query3.filter('orderkey = ', int(order_id)).filter('part = ', part_returned).fetch(1)[0]
                data = str(part_edited.startqty)
                self.response.out.write(data)
            else:
                order_submitted = self.request.get("order_submitted")
                newly_registered_user = self.request.get("reg")
                if newly_registered_user:
                    welcome_note = '<font size="20" color=red>Thank you for registering, %s</font><br/>Use this page to track/update your pending orders or view completed ones.<br/>' % (returning_user)
                else:
                    welcome_note = ''
                
                if order_submitted:
                    order_submitted = '<font size="20" color=red>Your order has been entered</font><br/>Add a tracking number to any parts you decide to return.'
                else:
                    order_submitted = ''
                
                list_pending_orders = query.order('orderkey').filter('pending = ', True).filter('user = ', returning_user).fetch(100)
                list_complete_orders = query1.order('completion_date').filter('pending = ', False).filter('user = ', returning_user).fetch(100)
                first_pending_order_key = query2.order('orderkey').filter('pending = ', True).fetch(1)
                
                
                if first_pending_order_key:
                    first_pending_order_key = first_pending_order_key[0].orderkey
                else:
                    first_pending_order_key = ''
                    
                pending_orders = ''
                complete_orders = ''
                
                order_count = 0
                for order in list_pending_orders:
                    order_count += 1
                
                    query4 = OrderByItem.all()
                    list_of_parts_by_order = query4.order('part_index').filter('orderkey = ', order.orderkey).fetch(50)
                    
                    part_qty_table = '<table class="parttable"><tbody>'
                    for part in list_of_parts_by_order:
                        part_qty_table += str(part.part_log)
                    part_qty_table += '</tbody></table>' 
                    
                    if order_submitted and order_count == len(list_pending_orders):
                        row_color = 'style="background-color:#E6E5EE;"'
                    else:
                        row_color = ''
                    
                    pending_orders += '<tr %s><td id="order%s">%s</td><td id="user%s">%s</td><td style="width:40">%s</td><td id="contract%s" style="width:40px">%s</td><td id="purchase%s">%s</td><td id="service%s">%s</td><td id="quote%s">%s</td><td class="partcell" id="parts%s">%s</td><td style="width:350px"><a id="editbuttoninsert%s"></a></td><td style="width:10">%s</td><td id="status%s" style="width:130">%s</td><td>%s</td><td id="user_status%s">%s</td></tr>' % (row_color, order.orderkey, order.orderkey, order.orderkey, order.user, order.customer, order.orderkey, order.contract,  order.orderkey, order.purchase_order, order.orderkey, order.service_ticket, order.orderkey, order.quotation_num, order.orderkey, part_qty_table, order.orderkey, order.urgency, order.orderkey, order.status, order.date, order.orderkey, order.user_status)
                
                
                for order in list_complete_orders:
                    
                    query9 = OrderByItem.all()
                    list_of_parts_by_order = query9.order('part_index').filter('orderkey = ', order.orderkey).fetch(50)
                    
                    part_qty_table_comp = '<table class="parttable"><tbody>'
                    for part in list_of_parts_by_order:
                        part_qty_table_comp += str(part.part_log)
                    part_qty_table_comp += '</tbody></table>'     

                        
                    complete_orders += '<tr><td>%s</td><td>%s</td><td style="width:40">%s</td><td style="width:40">%s</td><td>%s</td><td>%s</td><td>%s</td><td class="partcell">%s</td><td style="width:10">%s</td><td>%s</td><td>%s</td></tr>' % (order.orderkey, order.user, order.customer, order.contract, order.purchase_order, order.service_ticket, order.quotation_num, part_qty_table_comp, order.urgency, order.date, order.completion_date)
                
                    
                page = """
                    
                        <html>
                            <head>
                                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                                <script src="/static/userpage.js"></script>
                                <script src="/static/main.js"></script>
                                <script src="/static/login.js"></script>
                                <link rel="stylesheet" type="text/css" href="/static/mystyleorder.css" />
                                <title>
                                    User Page
                                </title>
                            </head>
                            <body>
                                <a id="user_name">%(returning_user)s</a>
                                <center>
                                    <div id="mainheader"></div>
                                </center>
                                <div id="regsectiondiv" align="RIGHT">
                                    <div class="regdiv">%(reg_section)s</div>
                                </div>
                                <br/>
                                <br/>
                                
                                <center>
                                    %(welcome_note)s
                                    %(order_submitted)s
                                    <div><font size="4" face="arial" color=darkblue>%(returning_user)s's Pending Orders</font><br><br></div> 
                                    <div id="pendingorderdiv">         
                                        <table><tbody>
                                                                               
                                            <tr style="background-image:url('/static/bannerorder.png')"><td>Order#</td><td>User</td><td>Customer</td>
                                            <td>Contract</td><td>PO#</td><td>ST#</td><td>Q#</td><td>Parts Ordered &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=darkred>Open Quantity</font></td><td>Add Tracking# for Parts Returned</td><td>Urgency</td><td>Comments</td>
                                            <td>Order Date</td><td>Order Status</td></tr>
                                        %(pending_orders)s
                                        <tbody></table>  
                                    </div>
                                <br/><br/>
                                </center>
                                
                                <center>
                                    
                                    <div id="completeorderdiv">
                                        <table><tbody>
                                        <div><font size="4" face="arial" color=darkblue>%(returning_user)s's Complete Orders</font><br><br></div>
                                        <tr style="background-color:#99DDAA"><td>Order#</td><td>User</td><td>Customer</td>
                                        <td>Contract</td><td>PO#</td><td>ST#</td><td>Q#</td><td>Parts Ordered &nbsp&nbsp|&nbsp&nbsp <font color=darkred>Open Quantity</font></td><td>Urgency</td>
                                        <td>Order Date</td><td>Completion Date</td></tr>
                                        %(complete_orders)s
                                        <tbody></table>  
                                    </div> 
                                    </center>
                                    <div id="firstorderkey">
                                        %(first_pending_order_key)s
                                    </div> 

                                       
                            </body>
                        </html>
                        
                    """ % {
                        "pending_orders":pending_orders,
                        "complete_orders":complete_orders,
                        "first_pending_order_key":first_pending_order_key,
                        "reg_section":reg_section,
                        "returning_user":returning_user,
                        "order_submitted":order_submitted,
                        "welcome_note":welcome_note
                    }
                    
                self.response.out.write(page)
        else:
            page = error_page % {
                    "reg_section":reg_section
                }
            self.response.out.write(page)
            
class Admin(webapp.RequestHandler):
    def get(self):
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
        
        ordernum = self.request.get('order')
        partnum = self.request.get('div')
        updated_order_id = self.request.get('id')
        prop_updated = self.request.get('property')
        new_prop_value = self.request.get('update')
        part_shipped = self.request.get('part_shipped')
        order_status_change = self.request.get('status_change')
        new_tracking_number = self.request.get('tracking_number')
        qty_shipped = self.request.get('qty_shipped')
        tracking_clear = self.request.get('tracking_clear')
        user_changed = self.request.get('user_changed')
        user_shipped = self.request.get('user_shipped')
        qty_value =  self.request.get('qty_value')
        part_value = self.request.get('part_value')
        part_index = self.request.get('part_index')
        
        page = ''

        query = PartOrder.all()
        query1 = PartOrder.all()
        query3 = PartOrder.all()
        list_pending_orders = query.order('orderkey').filter('pending = ', True).fetch(100)
        list_complete_orders = query1.order('completion_date').filter('pending = ', False).fetch(100)
        first_pending_order_key = query3.order('orderkey').filter('pending = ', True).fetch(1)
        
        if returning_user:
            if first_pending_order_key:
                first_pending_order_key = first_pending_order_key[0].orderkey
            else:
                first_pending_order_key = ''
                
            pending_orders = ''
            for order in list_pending_orders:
            
                query4 = OrderByItem.all()
                list_of_parts_by_order = query4.order('part_index').filter('orderkey = ', order.orderkey).fetch(50)
                
                if order.user_status == True:
                    user_complete = "<font color=red><i>User ready to complete</i></font>"
                else:
                    user_complete = ' '
                
                part_qty_table = '<table class="parttable"><tbody>'
                for part in list_of_parts_by_order:
                    part_qty_table += str(part.part_log)
                part_qty_table += '</tbody></table>'     
                 
                pending_orders += '<tr><td id="order%s">%s</td><td id="user%s">%s</td><td style="width:40">%s</td><td id="contract%s" style="width:40">%s</td><td id="purchase%s">%s</td><td id="service%s">%s</td><td id="quote%s">%s</td><td class="partcell" id="parts%s" width="200px">%s</td><td style="width:300px"><a id="editbuttoninsert%s"></a></td><td style="width:10">%s</td><td id="comment%s" style="width:110">%s</td><td>%s</td><td width="75px" id="status%s">%s</td></tr>' % (order.orderkey, order.orderkey, order.orderkey, order.user, order.customer, order.orderkey, order.contract,  order.orderkey, order.purchase_order, order.orderkey, order.service_ticket, order.orderkey, order.quotation_num, order.orderkey, part_qty_table, order.orderkey, order.urgency, order.orderkey, order.status, order.date, order.orderkey, user_complete)
          
            
            if prop_updated:
                order_edited = query.filter('orderkey = ', int(updated_order_id)).fetch(1)[0]
                orderbypart_edited_list = query4.filter('orderkey = ', int(updated_order_id)).fetch(50)
                if prop_updated == "comment":
                    order_edited.status = new_prop_value
                    body = "A new comment has been added: %s" % (new_prop_value) 
                if prop_updated == "purchase":
                    order_edited.purchase_order = new_prop_value
                    for part in orderbypart_edited_list:
                        part.purchase_order = new_prop_value
                        part.put()
                    body = "Purchase Order Number has been changed to: %s" % (new_prop_value) 
                if prop_updated == "service":
                    order_edited.service_ticket = new_prop_value
                    for part in orderbypart_edited_list:
                        part.service_ticket = new_prop_value
                        part.put()
                    body = "Service Ticket Number has been changed to: %s" % (new_prop_value) 
                if prop_updated == "quote":
                    order_edited.quotation_num = new_prop_value
                    for part in orderbypart_edited_list:
                        part.quotation_num = new_prop_value
                        part.put()                    
                    body = "Quotation Number has been changed to: %s" % (new_prop_value)                     
                if prop_updated == "tracking":
                    query = OrderByItem.all()
                    part_edited = query.filter('orderkey = ', int(updated_order_id)).filter('part = ', part_shipped).fetch(1)[0]
                    part_edited.part_log = '<tr><td class="parttd" id="order%sdiv%s">%s</td><td class="qtycell" id="part%sqty%s">%s</tr>' % (updated_order_id, part_index, part_value, updated_order_id, part_index, qty_value)
                    if tracking_clear:
                        part_edited.openqty = part_edited.startqty
                        page = str(part_edited.startqty)
                        self.response.out.write(page)
                    else:
                        part_edited.openqty = int(qty_value)
                    body = "Part %s with quantity %s has been shipped with tracking number: %s" % (part_shipped, qty_shipped, new_tracking_number)     
                    query2 = InvPart.all()
                    selected_parts = query2.filter('name = ', part_shipped).fetch(10)
                    page = parts_info_shipped(len(selected_parts), part_shipped, selected_parts)	+ "<br/><br/>" 
                    part_edited.put()    
                order_edited.put()
                
                lioremail = "Camtek Logistics <liorgott@gmail.com>"
                
                if not tracking_clear:
                    if user_changed:
                        query4 = User.all()
                        user = query4.filter('name = ', user_changed).fetch(1)
                        returning_user_email = user[0].email
                        
                        subject = "%s made an update to order ID %s" % (user_changed, updated_order_id)
                        
                        mail.send_mail(lioremail, lioremail + ",<howardk@camtekusa.com>", subject, body)                        
                    else:
                        query4 = User.all()
                        user = query4.filter('name = ', user_shipped).fetch(1)
                        returning_user_email = user[0].email
                        subject = "Logistics Admin made an update to your order ID %s" % (updated_order_id)
                        mail.send_mail(lioremail, returning_user_email, subject, body)
                                
                    self.response.out.write(page)
                
            elif order_status_change:
                order_edited = query.filter('orderkey = ', int(updated_order_id)).fetch(1)[0]
                query5 = OrderByItem.all()
                list_of_parts_by_order = query5.filter('orderkey = ', int(updated_order_id)).fetch(50)
                if order_status_change == "complete":
                    order_edited.pending = False
                    order_edited.completion_date = datetime.datetime.now().date()
                    order_edited.put()
                elif order_status_change == "cancel":
                    db.delete(order_edited)
                    db.delete(list_of_parts_by_order)
                elif order_status_change == "user_status_complete":
                    order_edited.user_status = True
                    order_edited.put()
                    lioremail = "Camtek Logistics <liorgott@gmail.com>"
                    query6 = User.all()
                    user = query6.filter('name = ', user_changed).fetch(1)
                    returning_user_email = user[0].email
                    
                    subject = "%s is ready to complete order ID %s" % (user_changed, updated_order_id)
                    body = "Complete the order"
                    
                    mail.send_mail(lioremail, lioremail, subject, body)                     
            else:
                page = """
                    
                        <html>
                            <head>
                                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                                <script src="/static/admin.js"></script>
                                <script src="/static/main.js"></script>
                                <script src="/static/login.js"></script>
                                <link rel="stylesheet" type="text/css" href="/static/mystyleorder.css" />
                                <title>
                                    Admin
                                </title>
                            </head>
                            <body> 
                                <center>
                                    <div id="mainheader"></div>
                                </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                                <br/>
                                <br/>
                                <center>
                                <font size="6" face="arial">Pending Orders</font><br><br>
                                    <div id="pendingorderdiv">
                                        <table class="adminpendingorders"><tbody>                            
                                        <tr style="background-image:url('/static/bannerorder.png')"><td>Order#</td><td>User</td><td>Customer</td>
                                        <td>Contract</td><td>PO#</td><td>ST#</td><td>Q#</td><td>Parts Ordered &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=darkred>Open Quantity</font></td><td>Tracking# Edit</td><td>Urgency</td><td>Comments</td>
                                        <td>Order Date</td><td>Order Status</td></tr>
                                        %(pending_orders)s
                                        <tbody></table>
                                    </div>
                                <br/><br/>
                                    <center>
                                    <div id="loadingdiv">
                                        <img src="/static/loading.gif">
                                    </div>
                                    <div id="partshippeddiv">
                                    </div>
                                    </center>
                                </center>    
                                <div id="firstorderkey">
                                    %(first_pending_order_key)s
                                </div>
                                
                                    
                            </body>
                        </html>
                        
                    """ % {
                        "pending_orders":pending_orders,
                        "first_pending_order_key":first_pending_order_key,
                        "reg_section":reg_section
                    }
                
                self.response.out.write(page)
        else:
            page = error_page % {
                        "reg_section":reg_section
                    }
                
            
            self.response.out.write(page) 

class Login(webapp.RequestHandler):
    def get(self): 
        page = ''
        query = User.all()
        query2 = User.all()
        query3 = Session.all()
        

        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
   
        
        name = self.request.get('username')
        email = self.request.get('email')
        user_pass = self.request.get('password')
        input_type = self.request.get('input_type')

        if name:
            existing_email = query.filter('email = ', email).fetch(1)
            existing_user_name = query2.filter('name = ', name).fetch(1)
            if input_type == "register": 
                if existing_user_name:
                    page = '<span style="color:red;">There already exists an account with that name</span>'            
                elif existing_email:
                    page = '<span style="color:red;">There already exists an account with that email</span>'
                elif input_type == "register": 
                    password = make_secure_password(user_pass)
                    cookie_header = cookie_bake()
                    self.response.headers.add_header("set-cookie", cookie_header)                    
                    p = User()
                    p.name = name
                    p.email = email
                    p.password = password
                    p.valid = False
                    p.put()
                    
                    q = Session()
                    q.session_id = cookie_header
                    q.user_name = name
                    q.put()
                    
                    lioremail = "Camtek Logistics <liorgott@gmail.com>"
                    subject = "New account registered"
                    body = """
                    
Name: %(name)s 

Email: %(email)s
                        
                        """ % {
                            "name":name,
                            "email":email
                        }
                        
                    mail.send_mail(lioremail, lioremail, subject, body)
                    
            else:
                if existing_user_name:
                    hashpass = existing_user_name[0].password
                    password_valid = check_user_password(hashpass, user_pass)
                    if password_valid:
                        user_name = existing_user_name[0].name
                        cookie_header = cookie_bake()
                        self.response.headers.add_header("set-cookie", cookie_header)
                        q = Session()
                        q.session_id = cookie_header
                        q.user_name = name
                        q.put()                       
                    else:
                        page = '<span style="color:red;">Invalid password and/or name</span>'
                else:
                    page = '<span style="color:red;">Invalid password and/or name</span>'
                    
            
            self.response.out.write(page)             
                
        else:
            page = """
            
                <html>
                    <head>
                        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                        <script src="/static/login.js"></script>
                        <script src="/static/main.js"></script>
                        <script src="/static/login.js"></script>
                        <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                        <title>
                            Login
                        </title>
                    </head>
                    <body>
                        <center>
                            <div id="mainheader"></div>
                        </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                        <br/>
                        <br/>
                        <table class="border" border="0" style="vertical-align:bottom;background-color:#D2D7EA;width:250px" align=CENTER>
                        <tbody><tr>
                            <td style="width:300px">
                            <span style="font-size:20;font-family:arial;" face="arial"><b>REGISTER</b></span> <br/><br/>
                            Name: <br/><input type="text" id="usernameregister" style="width:200px" /><br/><br/>
                            Email: <br/><input type="text" id="emailregister" style="width:200px" /><br/><br/>
                            Password: <br/><input type="password" id="passwordregister" style="width:200px" /><br/><br/>
                            Verify Password: <br/><input type="password" id="passwordregisterverify" style="width:200px" /><br/><br/>
                            <input type="button" onclick="user_submit('register')" value="Register" id="registersubmit" />
                            <br/><br/>
                            <div id="registerstatusdiv">
                            </div>                          
                        </tr>
                        </tbody></table>                       
                    </body>
                </html> 
                
                """ % {
                    "reg_section":reg_section
                }

    
            self.response.out.write(page)            

class CompleteOrders(webapp.RequestHandler):
    def get(self):
        filter_choice_made = self.request.get("filter_choice")   
        filter_by = self.request.get("filter_by")
        filters_added = self.request.get("filters_added")
        
        filter_option_list = self.request.get("filter_option")
        filter_by_list = self.request.get("filter_by")
        total_filters_made = self.request.get("filter_count")
        filter_made = self.request.get("filter")
        
        page_num = self.request.get("page")

        page = ''
        
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
        
        if returning_user:
            
            if filter_choice_made == "Customer":
                page = filter_option_maker("customer", filter_option_list, filter_by_list, filters_added)
                self.response.out.write(page) 
                    
            elif filter_choice_made == "User":
                page = filter_option_maker("user", filter_option_list, filter_by_list, filters_added)
                self.response.out.write(page) 

            elif filter_choice_made == "Contract":      
                page = filter_option_maker("contract", filter_option_list, filter_by_list, filters_added)
                self.response.out.write(page) 
                
            elif filter_choice_made == "*Choose Filter*":
                page = ''
                self.response.out.write(page) 
                          
            
            else:
                query = PartOrder.all()
                list_complete_orders = query.order('-orderkey').filter('pending = ', False).fetch(10000)

                page_num = int(page_num) if page_num else 1                
            

                complete_order_list = complete_list_divider(page_num, list_complete_orders)
                pageview = page_count_maker(page_num, list_complete_orders)                
                
                if filter_made:
                    complete_order_list = filter_table_maker(filter_option_list, filter_by_list, total_filters_made)
                    pageview = ''
                    page = """
                        <table class="completeorderdiv"><tbody>
                        <tr style="background-color:#99DDAA"><td>Order#</td><td>User</td><td>Customer</td>
                        <td>Contract</td><td>PO#</td><td>ST#</td><td>Q#</td><td>Parts Ordered &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=darkred>Open Quantity</font></td><td>Urgency</td>
                        <td>Order Date</td><td>Completion Date</td></tr>
                        %(complete_order_list)s
                        <tbody></table>  
                        <br/>
                        %(pageview)s                                    
                        
                        """ % {
                            "complete_order_list":complete_order_list,
                            "pageview":pageview
                        }
                        
                    self.response.out.write(page) 
                    
                else:
                    page = """
                        <html>
                            <head>
                                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                                <script src="/static/complete.js"></script>
                                <script src="/static/main.js"></script>
                                <script src="/static/login.js"></script>
                                <link rel="stylesheet" type="text/css" href="/static/mystyleorder.css" />
                                <title>
                                    Order List
                                </title>
                            </head>            
                                <body>
                                <center>
                                        <div id="mainheader"></div>
                                    </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                                    <br/>
                                    <br/>
                                <center>
                                <table class="filter">
                                <tbody>
                                <tr><td class="filter" id="filter0" align=LEFT><font size="5">Filter by </font> >>> </td></tr>
                                </td></tr>
                                </tbody></table>

                                <div id="filterdesc">
                                </div>
                                <div id="ordercount"></div>
                                <div id="completeorderlist">
                                    <table class="completeorderdiv"><tbody>
                                    <tr style="background-color:#99DDAA"><td>Order#</td><td>User</td><td>Customer</td>
                                    <td>Contract</td><td>PO#</td><td>ST#</td><td>Q#</td><td>Parts Ordered &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=darkred>Open Quantity</font></td><td>Urgency</td>
                                    <td>Order Date</td><td>Completion Date</td></tr>
                                    %(complete_order_list)s
                                    <tbody></table>
                                    <br/>
                                    %(pageview)s                                    
                                </div>
                                </center>
                                </body>
                            </html>
                        
                        """ % {
                                "reg_section":reg_section,
                                "complete_order_list":complete_order_list,
                                "pageview":pageview
                            }
                                
                    self.response.out.write(page) 
        else:
            page = error_page % {
                    "reg_section":reg_section
                }   
            self.response.out.write(page) 
        
class AdminChoice(webapp.RequestHandler):
    def get(self):
        admin_password = self.request.get("admin_password")
        
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
        
        if returning_user:
            if returning_user == "Admin":
                message = '<input type="button" value="Order Control" onclick="admin()"><input type="button" value="Part List Edit" onclick="edit()"><input type="button" value="User Control" onclick="usercontrol()">'           
            else:
                message = '<span style="color:red">You must be an admin to enter this page</span>'
                
        else:
            message = '<span style="color:red">You must be an admin to enter this page</span>'
        
        page = """
            <html>
                <head>
                    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                    <script src="/static/main.js"></script>
                    <script src="/static/adminchoice.js"></script>
                    <script src="/static/login.js"></script>
                    <link rel="stylesheet" type="text/css" href="/static/mystyle.css" />
                    <title>
                        Admin Choice
                    </title>
                </head>            
                    <body>
                    <center>
                            <div id="mainheader"></div>
                        </center>
                            <div id="regsectiondiv" align="RIGHT">
                                <div class="regdiv">%(reg_section)s</div>
                            </div>
                        <br/>
                        <br/>
                        <div id="autocomplete"></div>
                        <center>
                        %(message)s
                        </center>
                    </body>
                </html>
            
            """ % {
                    "reg_section":reg_section,
                    "message":message
                }   
        self.response.out.write(page)
        
class Logout(webapp.RequestHandler):
    def get(self): 
        user_cookie = self.request.headers.get("cookie")
        query = Session.all()
        if user_cookie:
            returning_user = query.order('add_dt').filter('session_id = ', user_cookie).fetch(10000)
            db.delete(returning_user)           

class PartsViewer(webapp.RequestHandler):
    def get(self):
        make_all_parts = self.request.get("make_all_parts")
        user_cookie = self.request.headers.get("cookie")
        location_filtered = self.request.get("location_filtered")
        
        reg_section, returning_user = login_code(user_cookie)
        
        locations_list = ["", "California", "California Damaged", "Dallas", 
				"Dallas Damaged", "TTM", "Nevo", "Basil", "David",
				"Faisal", "Roni", "Harold", "Alex", "Madukar", "Andy",
				"Antony", "Tom", "Shong", "All Warehouses"]
        locations_options = ''        
        
        inv_parts_list = ""
        
        if returning_user:
            
            if make_all_parts:
                table_of_parts = ''
                query = Part.all()
                parts_list = query.fetch(100000)
                parts_list.sort(key=lambda part: part.key().name())
                page = """<tr style="background-image:url('/static/bannerorder.png')"><td>Part Name</td><td>Second Description</td><td>Price</td></tr>
                """
                for part in parts_list:
                    page += '<tr><td class="parts" width="150px">%s</td><td class="parts" width="110px">%s</td><td class="parts" width="70px">$%s</td></tr>' % (part.key().name(), part.desctwo, part.price)
                
                self.response.out.write(page)
    
            else:
                
                
                
                for location in locations_list:
                    locations_options += "<option>" + location + "</option>"
                
                query = InvPart.all()
                
                if location_filtered:
                    inv_parts_list = query.filter('location = ', location_filtered).fetch(10000)
                    if len(inv_parts_list) == 0:
                        tabledesc = "<font color=red>No parts in " + location_filtered + "'s warehouse</font>"
                    else:
                        tabledesc = "Parts in " + location_filtered + "'s warehouse"
                else:
                    inv_parts_list = query.fetch(10000)
                    tabledesc = "Parts in the USA"
                
                inv_parts_list.sort(key=lambda part: part.name)
                inv_parts_list.sort(key=lambda part: part.location)
                
                table_of_parts = """
                                <tr style="background-image:url('/static/bannerorder.png')"><td>Location</td><td>Part Name</td><td>Second Description</td><td>Quantity</td>
                                <td>Itur</td><td>Price</td></tr>
                """
                
                for part in inv_parts_list:
                    key = db.Key.from_path('Part', part.name)
                    partstock = db.get(key)
                    if partstock:
                        price = "$" + partstock.price
                        desctwo = partstock.desctwo
                    else:
                        price = "Not Available"
                        
                    table_of_parts += '<tr><td class="parts">%s</td><td class="parts">%s</td><td class="parts">%s</td><td class="parts">%s</td><td class="parts">%s</td><td class="parts" width="70px">%s</td></tr>' % (part.location, part.name, desctwo,  part.qty, part.shelf, price)
            
                page = """
                    <html>
                        <head>
                            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                            <script src="/static/main.js"></script>
                            <script src="/static/parts.js"></script>
                            <script src="/static/login.js"></script>
                            <link rel="stylesheet" type="text/css" href="/static/mystyleorder.css" />
                            <title>
                                Complete Parts List
                            </title>
                        </head>            
                            <body>
                            <center>
                                    <div id="mainheader"></div>
                                </center>
                                    <div id="regsectiondiv" align="RIGHT">
                                        <div class="regdiv">%(reg_section)s</div>
                                    </div>
                                <center>
                                <font size="6">
                                <a id="tabledesc">%(tabledesc)s</a>
                                </font>
                                <div id="tableswitchbutton"></div>
                                </br>
                                    <div class="filteroption" align=CENTER id="filteroptions"><td border="0" width="200px"><a id="filterselection">
                                        Filter by location: <select id="filterselect">%(locations_options)s</select></a>
                                    </td><td><a id="buttoninsert"></a></td></div>
                                <table id="tableofparts" class="parts" width="800px"><tbody>                            
                                    %(table_of_parts)s
                                <tbody></table>
                                </center>
                                <center>
                                </center>
                            </body>
                        </html>
                    
                    """ % {
                            "table_of_parts":table_of_parts,
                            "reg_section":reg_section,
                            "locations_options":locations_options,
                            "tabledesc":tabledesc
                        }   
                self.response.out.write(page)
                
        else:
            page = error_page % {
                    "reg_section":reg_section
                }   
            self.response.out.write(page)

            
class File(webapp.RequestHandler):
    def get(self): 
        import csv
        file_requested = self.request.get("file_requested")
        
        
        if file_requested == "orders":
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=Completed_Orders.csv'

            query = PartOrder.all()
            list_complete_orders = query.order('orderkey').filter('pending = ', False).fetch(10000)   
        
            writer = csv.writer(self.response.out,dialect='excel')
            writer.writerow(['Order#', 'User', 'Customer', 'Contract', 'PO#', 'ST#', 'Q#', 'Parts Ordered', 'Urgency', 'Order Date', 'Completion Date'])

            for order in list_complete_orders:
                if not order.partlog:
                    order.partlog = ''
                writer.writerow([order.orderkey, order.user, order.customer, order.contract, order.purchase_order, order.service_ticket, order.quotation_num, order.partlog, order.urgency, order.date, order.completion_date])                   
        
        elif file_requested == "invparts":
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=Inventory_Parts_List.csv' 
        
            writer = csv.writer(self.response.out,dialect='excel')
            writer.writerow(['Location', 'Part name', 'Second Description', 'Quantity', 'Itur', 'Price'])

            query = InvPart.all()
            inv_parts_list = query.fetch(10000)
            inv_parts_list.sort(key=lambda part: part.name)
            inv_parts_list.sort(key=lambda part: part.location)
            
            for part in inv_parts_list:
                key = db.Key.from_path('Part', part.name)
                partstock = db.get(key)
                if partstock:
                    price = "$" + partstock.price
                    desctwo = partstock.desctwo
                else:
                    price = "Not Available"
                    desctwo = ""
                writer.writerow([part.location, part.name, desctwo, part.qty, part.shelf, price])
                
        elif file_requested == "allparts":
        
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=All_parts_list.csv' 
        
            writer = csv.writer(self.response.out,dialect='excel')
            writer.writerow(['Part name', 'Second Description', 'Price'])
            
            query = Part.all()
            parts_list = query.fetch(100000)
            parts_list.sort(key=lambda part: part.key().name())
  
            for part in parts_list:
                writer.writerow([part.key().name(), part.desctwo, part.price])
               
        elif file_requested == "consumptionreport":
        
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=Item_Consumption_Report.csv'

            query = OrderByItem.all()
            list_complete_orders = query.order('orderkey').fetch(10000)   
        
            writer = csv.writer(self.response.out,dialect='excel')
            writer.writerow(['Order#', 'User', 'Customer', 'Contract', 'PO#', 'ST#', 'Q#', 'Part', 'Price', 'Ordered Qty', 'Shipped Qty', 'Order Date'])

            for order in list_complete_orders:
                writer.writerow([order.orderkey, order.user, order.customer, order.contract, order.purchase_order, order.service_ticket, order.quotation_num, order.part, order.price, order.startqty, order.startqty - order.openqty, order.date])                   
        
class UserControl(webapp.RequestHandler):
    def get(self):
        
        user_cookie = self.request.headers.get("cookie")
        reg_section, returning_user = login_code(user_cookie)
        
        user_to_validate = self.request.get("make_valid")
        
        if user_to_validate:
            query1 = User.all()
            user = query1.filter("name = ", user_to_validate).fetch(1)[0]
            user.valid = True
            db.put(user)
            
            lioremail = "Camtek Logistics <liorgott@gmail.com>"

            user_email = user.email
            
            subject = "Your account has been validated." 
            body = "You may now navigate The Eagle: http://camteklogistics.appspot.com/"
            
            mail.send_mail(lioremail, user_email, subject, body) 
        
        query = User.all()
        user_list = query.fetch(100)
        user_table = '<table class="usertable"><tbody><tr style="background-color:#99DDAA"><td>Name</td><td>Email</td><td>Validity</td></tr>'
        i = 0
        for user in user_list:
            user_table += "<tr><td id='username%s'>%s</td><td>%s</td><td id='uservalidity%s'>%s</td></tr>" % (i, user.name, user.email, i, user.valid)
            i += 1
        user_table += "</tbody></table>"
            
        
        if returning_user:
            page = """
                <html>
                    <head>
                        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
                        <script src="/static/main.js"></script>
                        <script src="/static/usercontrol.js"></script>
                        <script src="/static/login.js"></script>
                        <link rel="stylesheet" type="text/css" href="/static/mystyleorder.css" />
                        <title>
                            User Control
                        </title>
                    </head>            
                        <body>
                        <center>
                                <div id="mainheader"></div>
                            </center>
                                <div id="regsectiondiv" align="RIGHT">
                                    <div class="regdiv">%(reg_section)s</div>
                                </div>
                            <br/>
                            <br/>
                            <center>
                                %(user_table)s
                            </center>
                        </body>
                </html>
                    """ % {
                            "reg_section":reg_section,
                            "user_table":user_table
                        }   
            self.response.out.write(page)
                
        else:
            page = error_page % {
                    "reg_section":reg_section
                }   
            self.response.out.write(page)

            
class HimHerMe(webapp.RequestHandler):
    def get(self):
        
        page = """
<html>
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script> 
        <script src="/static/hhmheader.js"></script>
        <script src="/static/hhm.js"></script>
        <link rel="stylesheet" type="text/css" href="/static/hhmstyle.css" />          
        <title>
            HHM
        </title>
    </head>
    <body>
    </body>
</html>        
        """
    
        self.response.out.write(page)
        
        
        
class HimHerMe2(webapp.RequestHandler):
    def get(self):
        
        
        page = """
<html>
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script> 
        <script src="/static/hhmheaderpractice.js"></script>
		<script src="/static/hhmobjects.js"></script>	
        <script src="/static/hhm2.js"></script> 
		<link rel="stylesheet" type="text/css" href="/static/hhm2style.css" />  
        <link rel="stylesheet" type="text/css" href="/static/hhmstyle.css" />  		
        <title>
            HHM2
        </title>
    </head>
    <body>
    <script type="text/javascript">
        profile_stats = {"name": "Tom G.", 
        "picture": "/static/tom.png",
        "category": "Automotive, Language, Business",
        "date": "Sept. 13, 2010",
        "projectspermonth": "13",
        "projects": "156",
        "rank": "83",
        "customer_rank": "3.5 of 5",
        "fee": "$50 per hour",
        "min_time": "30 min",
        "keywords": "cars, Spanish, engine, English, taxes, insurance, oil change, resume, cover letter, editing"}
    </script>
    </body>
</html>        
        """
    
        self.response.out.write(page)
        
       
                    
            
application = webapp.WSGIApplication(
                                     [
                                         ('/', MainPage),
                                         ('/order', Order),
                                         ('/order/submit', OrderSubmit),
                                         ('/edit', ListEdit),
                                         ('/admin', Admin),
                                         ('/userpage', UserPage),
                                         ('/login', Login),
                                         ('/complete', CompleteOrders),
                                         ('/adminpage', AdminChoice),
                                         ('/log_out', Logout),
                                         ('/parts', PartsViewer),
                                         ('/file', File),
                                         ('/usercontrol', UserControl),
                                         ('/hhm', HimHerMe),
                                         ('/hhm2', HimHerMe2)
                                     ],
                                     debug=True)                                     

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
	main()