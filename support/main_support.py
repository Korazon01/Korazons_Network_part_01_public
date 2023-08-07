import mysql.connector

def restart():
    global base , cursor
    base = mysql.connector.connect(user='your_user', password='Your_password', host='your_host',database='your_database')
    cursor = base.cursor()

restart()

def find_session(id):
    global base, cursor

    def func():
        global base, cursor
        cursor.execute(f"SELECT the_session FROM korazons_network_sessions WHERE id = {id}")

    try:func()
    except:
        restart()
        func()

    result = cursor.fetchone()

    return result[0]


def find_info(id):
    global base, cursor

    def func():
        global base, cursor
        cursor.execute(f"SELECT * FROM korazons_network_info WHERE id = {id}")

    try:func()
    except:
        restart()
        func()

    result = cursor.fetchone()

    return result


def edit_info(id,new_info,what_edit):
    global base, cursor

    if not edit_info_check(new_info,what_edit):return

    def func():
        global base, cursor


        if what_edit == 'name':

            cursor.execute(f"UPDATE korazons_network_enter SET name = '{new_info}' WHERE id = {id}")
            cursor.execute(f"UPDATE korazons_network_info SET name = '{new_info}' WHERE id = {id}")


        elif what_edit == 'password':
            cursor.execute(f"UPDATE korazons_network_enter SET password = '{new_info}' WHERE id = {id}")
            cursor.execute(f"UPDATE korazons_network_info SET password = '{new_info}' WHERE id = {id}")


        else:

            cursor.execute(f"UPDATE korazons_network_info SET the_text = '{new_info}' WHERE id = {id}")

    try:
        func()
    except:
        restart()
        func()

    base.commit()

    return True


def edit_info_check(new_info,what_edit):
    global base, cursor

    if what_edit == 'text':
        return True

    def func():
        global base, cursor

        if what_edit == 'name':
            cursor.execute(f"SELECT * FROM  korazons_network_enter WHERE name = '{new_info}'")

        elif what_edit == 'password':
            cursor.execute(f"SELECT * FROM  korazons_network_enter WHERE password = '{new_info}'")


    try:
        func()
    except:
        restart()
        func()

    result = cursor.fetchone()

    if not result:return True
    return False











