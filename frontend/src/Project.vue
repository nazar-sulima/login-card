<script setup>
import { ref, onMounted } from 'vue';


// let circle = document.querySelector('.circle')
// circle.onclick = () => {
//     circle.classList.add(".circle-right")
// }



onMounted(() => {
    const script = document.createElement("script");
    script.src = "https://accounts.google.com/gsi/client";
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);

});


function switcher() {
    let cardFront = document.querySelector('.card-front')
    console.log("🚀 ~ switcher ~ cardFront:", cardFront)

    let cardBack = document.querySelector('.card-back')
    console.log("🚀 ~ switcher ~ cardBack:", cardBack)

    cardFront.classList.toggle('hide');
    cardBack.classList.toggle('show');

    let circle = document.querySelector('.circle')
    console.log("🚀 ~ switcher ~ circle:", circle)
    circle.classList.toggle('circle-right')

    /* дописываем логику дальше здесь */

}




</script>

<template>
    <div class="container-fluid">
        <div class="row full-height justify-content-center">
            <div class="col text-center py-5">
                <div class="main">
                    <h4 class="px-3">
                        <span class="px3">Sing in</span><span class="px-3">Log in</span>
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

                            <h5 class="mt-3">Sing in</h5>
                            <form class="mt-3">
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputEmail1" class="form-label">Your Full Name</label>
                                    <input type="Full name" placeholder="Full name" class="form-control"
                                        id="exampleInputEmail1" aria-describedby="emailHelp">

                                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone
                                        else.
                                    </div> -->
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">Your Email Address</label>
                                    <input type="Email adress" placeholder="Email Address" class="form-control"
                                        id="exampleInputPassword1">
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">Your Password</label>
                                    <input type="Password" placeholder="Password" class="form-control"
                                        id="exampleInputPassword1">
                                </div>

                                <div id="g_id_onload"
                                    data-client_id="220369524095-ronkp3q52co9g90dvs9bm7l522bgsj6a.apps.googleusercontent.com"
                                    data-context="signin" data-ux_mode="redirect" data-login_uri="http://localhost:8000"
                                    data-itp_support="true">
                                </div>


                                <section class="d-flex justify-content-center mb-3">

                                    <div class="g_id_signin text-center" data-type="standard" data-shape="rectangular"
                                        data-theme="filled_blue" data-text="signin_with" data-size="large"
                                        data-locale="uk" data-logo_alignment="left">
                                    </div>
                                </section>


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
                            <form>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputEmail1" class="form-label">Email address</label>
                                    <input type="email" placeholder="Email address" class="form-control"
                                        id="exampleInputEmail1" aria-describedby="emailHelp">
                                    <!-- <div id="emailHelp" class="form-text">We'll never share your email with
                                                anyone
                                                else.
                                            </div> -->
                                </div>
                                <div class="mb-3 mx-3">
                                    <label for="exampleInputPassword1" class="form-label">Password</label>
                                    <input type="password" placeholder="Password" class="form-control"
                                        id="exampleInputPassword1">
                                </div>

                                <section class="d-flex justify-content-center mb-3">

                                    <div class="g_id_signin text-center" data-type="standard" data-shape="rectangular"
                                        data-theme="filled_blue" data-text="signin_with" data-size="large"
                                        data-locale="uk" data-logo_alignment="left">
                                    </div>
                                </section>

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
