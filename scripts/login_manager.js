function login (username, password){
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({"username":username, "password":password});
    var requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    //stores username in local storage for use in score
    localStorage.setItem("username", username);
    fetch("https://bjpskapus9.execute-api.us-east-1.amazonaws.com/dev/app/user/login", requestOptions)
    .then(response => response.text())
    .then(result => {
        // indicate whether the user was successfully logged in
        // store username as global variable
        // console.log(result);
        console.log(JSON.parse(result).body.success)
        if(JSON.parse(result).body.success){
            redirect_user();
        }else{
            alert("bad login")
        }
    }).catch(error => console.log('error', error));
}

function redirect_user(){
    window.location.href = "../gamepage.html";
}