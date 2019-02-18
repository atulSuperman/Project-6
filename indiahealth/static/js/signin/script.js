function toggle(e){
    let z = e.innerHTML;
    if(z=='Sign Up'){
        document.querySelector('.sign-user-container-head').innerHTML = "Join Here";
        document.querySelector('.sign-user-container-p').innerHTML = "Welcome here! You can join our org. Hey there! To keep connected with us Please Signup here with your account.";
        e.innerHTML = 'Log In';
        document.querySelector('#cpwd').style.display = 'block';
        document.querySelector('.create-account').innerHTML = 'Sign Up';
        document.querySelector('.sign-user-container-head-2').innerHTML = 'Already have <br>an account?'
        document.querySelector('.sign-user-container-head-2').style.marginTop = '95px';
        document.querySelector('.submit').innerHTML = 'Sign Up';
        document.querySelector('#toggle-sign-user').setAttribute('name','signup');
        document.querySelector('#cpwd').setAttribute('type','password');

    } else {
        document.querySelector('.sign-user-container-head').innerHTML = "Join Here";
        document.querySelector('.sign-user-container-p').innerHTML = "Welcome here! You can join our org. Please login here with your account. Please login here with your.";
        e.innerHTML = 'Sign Up';
        document.querySelector('#cpwd').style.display = 'none';
        document.querySelector('.create-account').innerHTML = 'Log In';
        document.querySelector('.sign-user-container-head-2').innerHTML = 'New User?'
        document.querySelector('.sign-user-container-head-2').style.marginTop = '55px';
        document.querySelector('.submit').innerHTML = 'Log In';
        document.querySelector('#toggle-sign-user').setAttribute('name','signin');
        document.querySelector('#cpwd').setAttribute('type');
    }
    let x = document.querySelector('.sign-user-container-head').innerHTML;
    let y = document.querySelector('.sign-user-container-p').innerHTML;
    z = e.innerHTML;

    console.log(x);
    console.log(y);
    console.log(z);

}
function validate(e){
     let x = document.getElementById('pwd').value;
     let y = document.getElementById('cpwd').value;
//     if(e.target.innerHTML=='Sign Up'){
//         if(x!=y){
//            alert('Password do not match');
//            return false;
//         } else{
//            return true;
//         }
//     }
}