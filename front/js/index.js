function pushValues(){
    var formElement = document.getElementById(a);
    var request = new XMLHttpRequest();
    a = "http://127.0.0.1:8000/api/"+a+"/";
    request.open("POST", "http://127.0.0.1:8000/api/mentors");
    request.send(new FormData(formElement));
}

function getValues(url){
    const http = new XMLHttpRequest()
    http.open("GET", url)
    http.send()    
    http.onload = () => console.log(http.responseText)
}

function pushValues(a){
    var formElement = document.getElementById(a);
    var request = new XMLHttpRequest();
    a = "http://127.0.0.1:8000/api/"+a+"/";
    request.open("POST", a);
    request.send(new FormData(formElement));
}

function listMentors(startup){
    
}