<script setup>
import { ref, onMounted } from 'vue';

let user = 'Yaroslav'


// let circle = document.querySelector('.circle')
// circle.onclick = () => {
//     circle.classList.add(".circle-right")
// }


onMounted(() => {
    let cardFront = document.querySelector('.card-front')
    console.log("🚀 ~ switcher ~ cardFront:", cardFront)
    
});


function switcher() {
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

                    <section class="switch d-flex justify-content-center py-3" >
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

                    <div class="card mx-auto">
                        <div class="card-front">
                            <div class="section mb-3">

                                <h5 class="mt-3">Sing in</h5>
                                <form class="mt-3">
                                    <div class="mb-3 mx-3">
                                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                                        <input type="email" placeholder="Email address" class="form-control"
                                            id="exampleInputEmail1" aria-describedby="emailHelp">

                                        <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone
                                            else.
                                        </div> -->
                                    </div>
                                    <div class="mb-4 mx-3">
                                        <label for="exampleInputPassword1" class="form-label">Password</label>
                                        <input type="password" placeholder="Password" class="form-control"
                                            id="exampleInputPassword1">
                                    </div>

                                    <button type="submit" class="btn btn-primary">Submit</button>
                                    <p class="mb-0 mt-4 text-center">
                                        <a>Forgot your password?</a>
                                    </p>

                                </form>
                            </div>

                        </div>
                        
                        <div class="card-back">
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

                                    <button type="submit" class="btn btn-primary">Submit</button>
                                    <p class="mb-0 mt-4 text-center">
                                        <a>Forgot your password?</a>
                                    </p>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
.card {
    max-width: 70%;
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
