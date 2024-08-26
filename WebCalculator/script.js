function showProgress(){
    document.querySelector("#progress-text").innerHTML = "👷‍♂️🚧 In progress 👷‍♂️🚧";
};

function changeMode(){
    const MODEBTN = document.querySelector("#btn-mode");
    if (MODEBTN.innerHTML == "Toggle Dark Mode"){
        document.querySelector("#color-mode").innerHTML = `
        * {
            font-family: 'Roboto Mono';
            font-weight: 400;
            color: #e7f1f0;
            background-color: #23242a;

            margin:0;
            padding:0;
        }
        `;
        MODEBTN.innerHTML = "Toggle Light Mode";
    } else if (MODEBTN.innerHTML == "Toggle Light Mode"){
        document.querySelector("#color-mode").innerHTML = `
        * {
            font-family: 'Roboto Mono';
            font-weight: 400;
            color: #e8e6fb;
            background-color: #9287ec;

            margin:0;
            padding:0;
        }
        `;
        MODEBTN.innerHTML = "Toggle Dark Mode";
    } else {
        console.log("Error")
    };
};