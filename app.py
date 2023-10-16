'''
Edited on Mar. 30, 2022

@editor: Anmol Nagpal


*** Issues identified ***

1) Lack of sanitizing of input field. 
    - The input was not being sanitized to remove HTML tags, hence
    it was possible to run JavaScript code directly through the input field. 
    This increases the likelihood of injection attacks occuring in the form of
    XSS (both reflected and stored) as well as SQL injection.
    
    This issue was identified through code review and confirmed via manual 
    pentest. In order to address this, the 'sanitize_input(url)' function was 
    created which essentially removes the '<script>' tag as well as the '<' '>'
    brackets from the url (if they exist). This function is executed before the 
    POST request is processed.

2) Lack of proper URL validation.
    - The url supplied in the input was not being validated to confirm whether
    or not it has an appropriate URL structure. I.e. you are able to pass 
    'h:c.sdfs' into the POST request and the application will process it and 
    store it in the database. This can take up unnecessary storage. Also,
    special characters were accepted in the URL, which is a concern.
    
    This issue was identified through code review and confirmed via manual 
    inspection. In order to address this a python module called 'validators'
    is used. This module has a .url() function that can help validate a supplied
    URL. This is called in the validate_url(url) function and is executed before
    data is passed onto the backend.

3) Lack of specified input size for input field.
    - No input size was declared or specified for the input field, which allows
    an input of any arbitrary length to be used. This can lead to overflow 
    attacks as well as denial of service attacks, as very large inputs may
    be used to exhaust the database.
    
    This issue was identified through code review and confirmed via manual 
    inspection. In order to address this, an input size of 200 characters is 
    declared, and is validated on both the client side and the server side. 
    This is necessary as client side logic can be overcome through breakpoints,
    and so it's integral that the conditions are also specified on the server 
    side. 
    Note: a max length of 200 was specified, which should be enough for majority
    of url's. This number can of course be tailored depending on specific needs.
    
    MAX_URL_LENGTH = 200 
    Client side -> added as a validator in the LinkForm class
    Server side -> added as a condition in the 'validate_url(url)' function

4) Same url storing different shorter urls
    - The same regular url is able to generate (and store) different short urls.
    This takes up unnecessary storage and time, and can lead to collisions down
    the road once enough urls have been stored.
    
    This issue was identified through code review and confirmed via manual 
    inspection. In order to address this, another column in the 'links' table
    was created. This column is responsible for storing the 'shorter_url'. 
    Now, whenever s POST request is made, and assuming the url passes all 
    validation, the application will first check to see if the supplied url 
    already exists 
        - if it does exist it will then return the shorter url;
        - if it doesn't exist then it will store the url and generate the 
        corresponding shorter url for it
        
5) Short urls can create more short urls
    - Once a short url is created it can be re-fed into the POST request to 
    create more short URLs. This is not ideal as it takes up unnecessary storage
    in the database.
    
    This issue was identified through code review and confirmed via manual 
    inspection. In order to address this the program will now check the 
    supplied URL and see if it exists in the 'shorter_url' column of the table.
    If the url exists, another url is not created and a message is displayed
    alerting the user that an invalid URL has been supplied.

6) Lack of Content-Security-Policy (CSP) in the header
    - The Content Security Policy (CSP) is an added layer of security that helps 
    to detect and mitigate Cross-Site Scripting (XSS) and data injection attacks. 
    
    This issue was identified through ZAP (DAST tool). In order to fix this,
    a CSP header has been created and set to 'default-src 'self'', which 
    specify's that all content should come from the site's own origin, and no
    place else.
    
7) Lack of X-Frame-Options in the header
    - X-Frame-Options helps prevent against 'clickjacking' attacks - where 
    clicks in the outer frame can be translated invisibly to clicks on your 
    pages elements
    
    This issue was identified through ZAP (DAST tool). In order to address this,
    an X-Frame-Options header has been created and set to 'SAMEORIGIN'.
    
8) Lack of SameSite session cookie configuration
    - SameSite restricts how cookies are sent with requests from external sites.
    
    This issue was identified through ZAP (DAST tool). In order to address this,
    a 'SESSION_COOKIE_SAMESITE' configuration has been created within the app
    and has been set to 'Lax'.
    
    Note: without specifying this configuration it defaults to 'Lax' regardless.
'''

import short_url
from flask import (
    Flask,
    render_template_string,
    redirect,
    url_for,
    flash,
    make_response
)

from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import wtforms
from wtforms import fields
from sqlalchemy import text
from sqlalchemy.sql import select
import validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

db = SQLAlchemy(app)

MAX_URL_LENGTH = 200

class LinkForm(FlaskForm):
    """ 
    *** Added a max length attribute here for the URL string.
    """
    url = fields.URLField('URL', validators=[wtforms.validators.DataRequired(), 
                                wtforms.validators.Length(max=MAX_URL_LENGTH)])
    submit = fields.SubmitField()


links = db.Table(
    'links',
    db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('url', db.Text),
    db.Column('shorter_url', db.Text)
)


db.create_all()

INDEX_TEMPLATE = '''<html>
    <head>
    </head>
    <body>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                <p>{{ message|safe }}</p>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="/">
            {{ form.url.label }}
            {{ form.url() }}
            {{ form.submit() }}
        </form>
    </body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index_page():
    form = LinkForm()

    if form.validate_on_submit():
        #sanitize the url
        sanitized_url = sanitize_input(form.url.data)
        #check to see if shoter_url is supplied
        exists_shorter_url = select(links).\
                                where(links.c.shorter_url == sanitized_url)
        result = db.engine.execute(exists_shorter_url)
        row_shorter_url = result.fetchone()
        #validate url
        if validate_url(sanitized_url) and row_shorter_url is None:
            exists_url = select(links).where(links.c.url == sanitized_url)
            result = db.engine.execute(exists_url)
            row_url = result.fetchone()
            
            if row_url is None and row_shorter_url is None:
                stmt = links.insert().values(url=text(f'"{sanitized_url}"'))
                result = db.session.execute(stmt)
                db.session.commit()
    
                shorter_url = url_for(
                    '.redirect_page',
                    slug=short_url.encode_url(result.inserted_primary_key[0]),
                    _external=True
                )
                #add shorter URL to database
                stmt = links.update()\
                            .values(shorter_url=shorter_url)\
                            .where(links.c.id == result.inserted_primary_key[0])
                db.session.execute(stmt)
                db.session.commit()
            else:
                shorter_url = row_url.shorter_url
            flash(
                f'Your short url is: {shorter_url}, which redirects'
                f' to {sanitized_url}.'
            )
    
            return redirect(url_for('.index_page'))
        else:
            flash(
                f'Invalid URL! Please try again with a valid URL.'
            )
    template = make_response(render_template_string(INDEX_TEMPLATE, form=form))
    #specify CSP and X-Frame-Options
    template.headers['Content-Security-Policy'] = "default-src 'self'"
    template.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return template


@app.route('/<slug>')
def redirect_page(slug):
    decoded_id = short_url.decode_url(slug)
    stmt = select(links).where(links.c.id == decoded_id)
    result = db.engine.execute(stmt)
    row = result.fetchone()

    return redirect(row.url)


def sanitize_input(url):
    """
    Remove brackets and <script> tags from url
    """
    sanitizers = ['<script>','</script>','<','>']
    for sanitize in sanitizers:
        url = url.replace(sanitize,'')
    return url.strip("/")


def validate_url(url):
    """
    Validate URL length on the server side to protect against breakpoints.
    """
    return (validators.url(url) and len(url) <= MAX_URL_LENGTH)