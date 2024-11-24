<script setup lang="ts">
import { ref, onMounted } from 'vue';

let fullName = "Your Full Name"
let emailAdress = "Your Email Address"
let password = ref("Your Password")
console.log("🚀 ~ password:", password.value)

// const reversedStr = password.split('').reverse().join('');
// console.log("🚀 ~ reversedStr:", reversedStr)


// let circle = document.querySelector('.circle')
// circle.onclick = () => {
//     circle.classList.add(".circle-right")
// }

// посмотреть типы ts



onMounted(() => {
    const script = document.createElement("script");
    script.src = "https://accounts.google.com/gsi/client";
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);

});


function switcher() {
    let cardFront = document.querySelector('.card-front')
    // console.log("🚀 ~ switcher ~ cardFront:", cardFront)

    let cardBack = document.querySelector('.card-back')
    // console.log("🚀 ~ switcher ~ cardBack:", cardBack)

    cardFront.classList.toggle('hide');
    cardBack.classList.toggle('show');

    let circle = document.querySelector('.circle')
    // console.log("🚀 ~ switcher ~ circle:", circle)
    circle.classList.toggle('circle-right')

    /* дописываем логику дальше здесь */

}

function validateEmail(email) {
    console.log("🚀 ~ validateEmail ~ email:", email)
    let emailRegex = /\w+@gmail\.com/gm;

    let checkResult = emailRegex.test(email)
    console.log("🚀 checkResult (validateEmail):", checkResult)

    return checkResult;

}


function validatePassword(password: string) {
    // let test = password.length;

    // console.log('- password -', password);
    // console.log('- password -', typeof password);
    
    // console.log(password.length >= 8)
    return password.length >= 8;
}

function validateName(name) {
    let nameRegex = /^[^\d]+$/;

    let checkResultNamme = nameRegex.test(name)
    console.log("🚀 ~ validateName ~ checkResultNamme:", checkResultNamme)

    return checkResultNamme;
}


onMounted(() => {
    let formSignUp = document.querySelector('.form')
    // console.log("🚀 ~ form:", formSignUp)
    let formLogIn = document.querySelector('.form-back')
    // console.log("🚀 ~ onMounted ~ formBack:", formLogIn)




    formSignUp.onsubmit = async function (event) {
        event.preventDefault();

        /* работа с DOM */

        // const newNameInput = document.querySelector("#new-name");
        // console.log('- newNameInput -', newNameInput);

        // let value = newNameInput.placeholder;
        // console.log('- value -', value);


        const newName = document.getElementById('new-name').value
        // console.log("🚀 ~ submitForm ~ newName:", newName)

        const newEmail = document.getElementById('new-email').value
        // console.log("🚀 ~ submitForm ~ newEmail:", newEmail)

        const newPassword = document.getElementById('new-password').value
        // console.log("🚀 ~ submitForm ~ newPassword:", newPassword)

        let newNameInput = document.querySelector('.new-name-input')
        // console.log("🚀 ~ newNameInput:", newNameInput)

        let newPasswordInput = document.querySelector('.new-password-input')
        // console.log("🚀 ~ newPasswordInput:", newPasswordInput)

        let newEmailInput = document.querySelector('.new-email-input')
        // console.log("🚀 ~ newEmailInput:", newEmailInput)


        let nameCheck = validateName(newName);
        console.log('- nameCheck -', nameCheck);

        let passwordCheck = validatePassword(newPassword);
        console.log("🚀 ~ passwordCheck:", passwordCheck);

        let emailCheck = validateEmail(newEmail);
        console.log("🚀 ~ emailCheck:", emailCheck);


        // validateEmail(newEmail)
        // validatePassword(newPassword)


        if (nameCheck == true) {
            console.log('done');
            newNameInput.classList.remove('input-switcher')
        }
        else {
            newNameInput.classList.add('input-switcher')
        }

        if (passwordCheck == true) {
            console.log('done');
            newPasswordInput.classList.remove('input-switcher')
        }
        else {
            newPasswordInput.classList.add('input-switcher')
        }

        if (emailCheck == true) {
            console.log('done');
            newEmailInput.classList.remove('input-switcher')
        }
        else {
            newEmailInput.classList.add('input-switcher')
        }



        // try {
        //     let response = await fetch('http://127.0.0.1:8000/register', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify({
        //             full_name: newName,
        //             email: newEmail,
        //             password: newPassword,
        //         }),
        //     });

        //     let result = await response.json()
        //     console.log("🚀 Sign-up successful:", result)
        // }
        // catch (error) {
        //     console.log(error.message);
        // }

    }

    formLogIn.onsubmit = async function (event) {

        event.preventDefault();

        const email = document.getElementById('email').value
        console.log("🚀 ~ onMounted ~ email:", email)

        const password = document.getElementById('password').value
        console.log("🚀 ~ onMounted ~ password:", password)

        // try {
        //     let response = await fetch('http://127.0.0.1:8000/login', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify({
        //             email: email,
        //             password: password,
        //         }),
        //     });

        //     let result = await response.json()
        //     console.log("🚀 Log-in successful:", result)

        // }
        // catch (error) {
        //     console.log(error.message);
        // }

    }

});


async function getData(url) {
    try {
        let response = await fetch(url)
        let data = await response.json()
        console.log("🚀 ~ getData ~ data:", data)

        return data
    }
    catch (error) {
        console.log(error.message);
    }

}

getData('http://127.0.0.1:8000/users')





</script>

<template>
    <div class="container-fluid">
        <div class="row full-height justify-content-center">
            <div class="col text-center py-5">
                <div class="main">
                    <h4 class="px-3">
                        <span class="px3">Sign up</span><span class="px-3">Log in</span>
                    </h4>

                    <section class="switch d-flex justify-content-center py-3">
                        <div class="rectangle">
                            <div class="circle" @click="switcher"></div>
                        </div>

                    </section>

                    <!-- { будет такой класс : если условие } -->
                    <!-- <section class="d-flex justify-content-center py-3" @click="togglePosition">
                        <div class="rectangle">
                            <div :class="{ 'circle-right': isRight == true }" class="circle"></div>
                        </div>
                    </section> -->



                    <div class="card card-front mx-auto">
                        <div class="section mb-3">

                            <h5 class="mt-3">Sign up</h5>
                            <form class="form mt-3">
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputEmail1" class="form-label">{{ fullName }}</label>
                                    <input type="Full name" placeholder="Full name" class="new-name-input form-control"
                                        id="new-name" aria-describedby="emailHelp">


                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>

                                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone
                                        else.
                                    </div> -->
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">{{ emailAdress }}</label>
                                    <input type="Email adress" placeholder="Email Address"
                                        class="new-email-input form-control" id="new-email">
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">{{
                                        password.split('').reverse().join('') }}</label>
                                    <input type="Password" placeholder="Password"
                                        class="new-password-input form-control" id="new-password">
                                </div>

                                <!-- Маршрутизатор Google кнопки -->
                                <!-- <div id="g_id_onload"
                                    data-client_id="220369524095-ronkp3q52co9g90dvs9bm7l522bgsj6a.apps.googleusercontent.com"
                                    data-context="signin" data-ux_mode="redirect" data-login_uri="http://localhost:8000"
                                    data-itp_support="true">
                                </div> -->

                                <!-- Google кнопка -->
                                <!-- <section class="d-flex justify-content-center mb-3">

                                    <div class="g_id_signin text-center" data-type="standard" data-shape="rectangular"
                                        data-theme="filled_blue" data-text="signin_with" data-size="large"
                                        data-locale="uk" data-logo_alignment="left">
                                    </div>
                                </section> -->


                                <!-- <p>
                                    <button class="btn btn-success">Sign in with Google</button>
                                </p> -->

                                <button type="submit" class="btn btn-primary">Submit</button>
                                <p class="mb-0 mt-4 text-center">
                                    <a class="fp">Forgot your password?</a>
                                </p>

                            </form>
                        </div>

                    </div>

                    <div class="card card-back mx-auto">
                        <div class="section mb-3">
                            <h4 class="my-3">Log in</h4>
                            <form class="form-back">
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputEmail1" class="form-label">Email address</label>
                                    <input type="email" placeholder="Email address" class="form-control" id="email"
                                        aria-describedby="emailHelp">
                                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with
                                                anyone
                                                else.
                                            </div> -->
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">Password</label>
                                    <input type="password" placeholder="Password" class="form-control" id="password">
                                </div>

                                <!-- Google кнопка -->
                                <!-- <section class="d-flex justify-content-center mb-3">

                                    <div class="g_id_signin text-center" data-type="standard" data-shape="rectangular"
                                        data-theme="filled_blue" data-text="signin_with" data-size="large"
                                        data-locale="uk" data-logo_alignment="left">
                                    </div>
                                </section> -->

                                <button type="submit" class="btn btn-primary">Submit</button>
                                <p class="mb-0 mt-4 text-center">
                                    <a class="fp">Forgot your password?</a>
                                </p>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
.fp {
    cursor: pointer;
}


.input-switcher {
    border-color: rgb(211, 21, 21);
    box-shadow: rgba(240, 10, 21, 0.25) 0px 0px 0px 0.25rem;
}

.switch .rectangle {
    --height: 30px;

    height: var(--height);
    width: calc(var(--height)*2.5);

    background-color: aqua;
    border-radius: 20px;

}

.switch .circle {
    --circle-size: 25px;

    width: var(--circle-size);
    height: var(--circle-size);

    background-color: brown;
    border-radius: 50%;
    margin: 2.25px 0 0 3px;

    cursor: pointer;
    transition: transform 0.3s ease;
}

.circle-right {
    transform: translateX(45px);
}

/* Карточки */
.card {
    max-width: 70%;
    transition: .6s;
}

.card-back {
    opacity: 0;
    height: 0;
    position: relative;
    z-index: 1;
}

.show {
    opacity: 1;
    height: auto;
}

.hide {
    opacity: 0;
    height: 0;
}

.g_id_signin {
    max-width: 50%;
}

/* .circle {
    width: 35px;
    height: 35px;
    background-color: brown;
    border-radius: 50%;
    position: absolute;
    left: 5px;
    transition: transform 0.3s ease;

}

.rectangle {
    width: 100px;
    height: 40px;
    background-color: blue;
    border-radius: 20px;
    position: relative;
    display: flex;
    align-items: center;
} */

/* 
.circle-right {
    transform: translateX(55px);
} */
</style>
