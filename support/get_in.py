import mysql.connector


def restart():
    global base , cursor
    base = mysql.connector.connect(user='your_user', password='Your_password', host='your_host',database='your_database')
    cursor = base.cursor()

def find_max():
    global base , cursor , id
    try:
        cursor.execute(f"SELECT MAX(id) FROM korazons_network_enter")
        eins = cursor.fetchone()[0]
        cursor.execute(f"SELECT MAX(id) FROM korazons_network_info")
        zwei = cursor.fetchone()[0]
        cursor.execute(f"SELECT MAX(id) FROM korazons_network_sessions")
        drei = cursor.fetchone()[0]

        if not eins or not zwei or not drei:raise Exception


        for i in [eins,zwei,drei]:
            if eins != i:

                raise Exception

        id = eins

    except:
        id = 1



restart()
find_max()

def authentication_support(name,password,choose):
    global base, cursor, id
    
    result = find_user(name,password)

    if choose == 'in':
        if not result:
            return False
        return result

    if result != False:
        return False

    make_user(name,password)
    return [id,name,password]



def find_user(name,password):
    global base,cursor,id

    def func():
        global base, cursor, id
        cursor.execute(f"SELECT * FROM  korazons_network_enter WHERE name = '{name}' OR password = '{password}'")

    try:func()
    except:
        restart()
        func()

    result = cursor.fetchone()

    if not result:return False
    if result[1] == name and result[2] == password:
        print('yes')
        return result
    print('no')
    return None


def make_user(name,password):
    global base,cursor,id

    def func():
        global base, cursor, id

        cursor.execute(f"INSERT INTO korazons_network_enter(name,password) VALUES('{name}','{password}')")
        cursor.execute(f"INSERT INTO korazons_network_info(name,password,the_text,liked) VALUES('{name}','{password}','',0)")
        cursor.execute(f"INSERT INTO korazons_network_sessions(the_session) VALUES('user_page')")

    try:func()
    except:
        restart()
        func()

    base.commit()

    id+=1
    return True






















