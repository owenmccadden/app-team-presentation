var create_score = (username)=>{
    // instantiate a headers object
    var myHeaders = new Headers();
    // add content type header to object
    myHeaders.append("Content-Type", "application/json");
    // using built in JSON utility package turn object to string and store in a variable
    var raw = JSON.stringify({"username":username});
    // create a JSON object with parameters for API call and store in a variable
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
    fetch("https://bjpskapus9.execute-api.us-east-1.amazonaws.com/dev/app/score/new", requestOptions)
    .then(response => response.text())
    .then(result => {
        // indicate success or failure to front-end
        console.log(result);
        // console.log(JSON.parse(result).body.success);
    }).catch(error => console.log('error', error));
}

var create_account = (username, password, email)=>{
    create_user(username, password, email);
    // create_score(username);
    window.location.replace("../index.html");
}

var create_user = (username, password, email)=>{
    // instantiate a headers object
    var myHeaders = new Headers();
    // add content type header to object
    myHeaders.append("Content-Type", "application/json");
    // using built in JSON utility package turn object to string and store in a variable
    var raw = JSON.stringify({"username":username, "password":password, "email":email});
    // create a JSON object with parameters for API call and store in a variable
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // make API call with parameters and use promises to get response
    fetch("https://bjpskapus9.execute-api.us-east-1.amazonaws.com/dev/app/user/new", requestOptions)
    .then(response => response.text())
    .then(result => {
        // if false prompt user to try again with a new username
        // if true store username as global variable for future use 
        console.log(result);
        console.log(JSON.parse(result).body.success);
        var myHeaders = new Headers();
        // add content type header to object
        myHeaders.append("Content-Type", "application/json");
        // using built in JSON utility package turn object to string and store in a variable
        var raw = JSON.stringify({"username":username});
        // create a JSON object with parameters for API call and store in a variable
        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };
        // make API call with parameters and use promises to get response
        fetch("https://bjpskapus9.execute-api.us-east-1.amazonaws.com/dev/app/score/new", requestOptions)
        .then(response => response.text())
        .then(result => {
            // indicate success or failure to front-end
            console.log(result);
            window.location.replace("../index.html");
            // console.log(JSON.parse(result).body.success);
        }).catch(error => console.log('error', error));
    }).catch(error => console.log('error', error));
}