function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "sanjay" && password == "123456"){
alert ("Login successfully");
window.location.href = 'https://36inc.in/';
  }
  else{
    alert("Invalid username or password");
    }
  return false;
  }
