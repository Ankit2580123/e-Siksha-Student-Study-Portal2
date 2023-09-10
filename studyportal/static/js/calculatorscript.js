const container = document.querySelector(".container"),
      pwShowHide = document.querySelectorAll(".showHidePw"),
      pwFields = document.querySelectorAll(".password"),
      signUp = document.querySelector(".signup-link"),
      login = document.querySelector(".login-link");

    //   js code to show/hide password and change icon
    pwShowHide.forEach(eyeIcon =>{
        eyeIcon.addEventListener("click", ()=>{
            pwFields.forEach(pwField =>{
                if(pwField.type ==="password"){
                    pwField.type = "text";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye-slash", "uil-eye");
                    })
                }else{
                    pwField.type = "password";

                    pwShowHide.forEach(icon =>{
                        icon.classList.replace("uil-eye", "uil-eye-slash");
                    })
                }
            }) 
        })
    })

    // js code to appear signup and login form
    signUp.addEventListener("click", ( )=>{
        container.classList.add("active");
    });
    login.addEventListener("click", ( )=>{
        container.classList.remove("active");
    });
    /**Calculator */
    function chMode() {
        mode.className == 'fa-solid fa-sun'?
        mode.className = 'fa-solid fa-moon':
        mode.className = 'fa-solid fa-sun';

        let body = document.querySelector('body');
        mode.classList.contains('fa-sun') ?
        body.setAttribute('data-theme', 'dark') :
        body.setAttribute('data-theme', 'light') ;
    }
    function calc() {
        var replaced = res.value;
        if (res.value.includes('÷') || res.value.includes('×')) {
            replaced = res.value.replaceAll('×', '*').replaceAll('÷', '/');
            res.value = eval(replaced);
        }
        res.value = eval(replaced);
    }