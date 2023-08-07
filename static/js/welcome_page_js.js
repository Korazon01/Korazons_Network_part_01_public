

function check_form(elem){

    var name = elem.name_form__welcome_page.value
    var password = elem.password_form__welcome_page.value
    var choose = elem.choose__welcome_page.value

    if(!name || !password || !choose){
        alert('you have to fill all')
        return false
    }

    if(name.split(' ').length != 1 || password.split(' ').length != 1){
        alert("don't make spaces")
        return false
    }

    if(name.length > 10 || password.length > 10){
        alert('the max long is 10 signs')
        return false
    }

    return true

}




document.getElementById('forgot_pass_button__welcome_page').addEventListener('click',forgot_button)

function forgot_button(){
    console.log('sdf')
    var forgot_div = document.getElementById('forgot_pass_div__welcome_page')

    if(forgot_div.style.display != 'block'){
        forgot_div.style.display = 'block'
        return
    }
    forgot_div.style.display = 'none'
}

















