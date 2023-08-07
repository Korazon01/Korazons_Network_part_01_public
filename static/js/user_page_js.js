document.getElementById('button_text__user_page').addEventListener('click',() => off_on('text__user_page'))
document.getElementById('functional_button__user_page').addEventListener('click',() => off_on('the_edit__user_page'))
document.getElementById('the_edit_name').addEventListener('click',() => off_on('new_name_div__user_page'))
document.getElementById('the_edit_text').addEventListener('click',() => off_on('new_text_div__user_page'))
document.getElementById('the_edit_password').addEventListener('click',() => off_on('new_password_div__user_page'))




function off_on(the_obj){
    var element = document.getElementById(the_obj)

    if(element.style.display != 'block'){
        element.style.display = 'block'

    }else{
        element.style.display = 'none'

    }

}



















