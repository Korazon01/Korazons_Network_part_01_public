from flask import Flask , request , make_response , redirect , render_template
from support import get_in , main_support
app = Flask(__name__)

@app.route('/')
def distribution():
    if not request.cookies.get('session'):return redirect('/welcome_page')

    the_cookie = request.cookies.get('session')
    direct = main_support.find_session(the_cookie)

    return redirect('/'+str(direct))


@app.route('/welcome_page')
def welcome_page():
    if request.cookies.get('session'):
        return redirect('/')

    return render_template('welcome_page.html')



@app.route('/welcome_page/authentication',methods = ['POST'])
def authentication():
    name = request.form['name_form__welcome_page']
    password = request.form['password_form__welcome_page']
    choose = request.form['choose__welcome_page']

    result = get_in.authentication_support(name,password,choose)

    if not result:
        return redirect('/')

    response = make_response(redirect('/'))
    response.set_cookie('session',f'{result[0]}')

    return response


@app.route('/user_page')
def user_page():

    if not request.cookies.get('session'):return redirect('/')

    the_cookie = int(request.cookies.get('session'))
    info_user = main_support.find_info(the_cookie)

    return render_template('user_page.html',name = info_user[1],password = info_user[2],text = info_user[3],liked = info_user[4])


@app.route('/user_page/get_out',methods = ['GET'])
def get_out():

    if not request.cookies.get('session'): return redirect('/')


    response = make_response(redirect('/'))
    response.set_cookie('session','',0)

    return response


@app.route('/user_page/new_info',methods = ['POST'])
def edit_info():

    id = request.cookies.get('session')

    if 'new_name' in request.form:
        what_edit = 'name'
        new_info = request.form['new_name']
    elif 'new_password' in request.form:
        what_edit = 'password'
        new_info = request.form['new_password']
    else:
        what_edit = 'text'
        new_info = request.form['new_text']

    main_support.edit_info(id,new_info,what_edit)

    return redirect('/')



app.run(host = '0.0.0.0',port = 80)