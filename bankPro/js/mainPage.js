
//Verify idErr is shown, if so, hide it
function verifyIDErr(){
  if($('#idErr').is(':visible') == true || $('#passwordIdErr').is(':visible') == true){

      hideIDErr();
  }
}

function sendData(loginDone, personID, personPassword){
  $.ajax({
    url:'php/login.php' + '?ID=' + personID + '&password=' + personPassword,
          success: loginDone
  });
}

function loginDone(result){
  var id = $("#userID").val();
  var data = result.split("-");
  if (id[0] == '0'){
    if (result == id.substring(1, id.length)){
        window.location.replace("main.html?id=" + id);
    }
  }
  if (data.length == 4){
      window.location.replace("userPage.html");
  }else{
    document.getElementById("idErr").innerHTML = "ID or password incorrect"; //Set idErr text
    document.getElementById("idErr").style.display = "inline"; //Make idErr visible
    return false;
  }
}

function checkLoginData(){
    var password = $("#password").val(); //Get id's value
    var userID = $("#userID").val();
  //If id is empty
  if (userID == "" || checkString(userID) == false){
    document.getElementById("idErr").innerHTML = "ID can not be empty"; //Set idErr text
    document.getElementById("idErr").style.display = "inline"; //Make idErr visible
    return false;
  }

  if(password == ""){
    document.getElementById("idErr").innerHTML = "Password can not be empty"; //Set idErr text
    document.getElementById("idErr").style.display = "inline"; //Make idErr visible
    return false;
  }
  sendData(loginDone, userID, password);
}
//Checks if id has non numerics characters
function checkString(input){

  for (i = 0; i < input.length; i++){

     var char = input.charCodeAt(i); //Get id[i] char value
     if(char < 48 || char > 57){ //If char isn't a number
       return false;
     }
  }
}

function hideIDErr(){
  document.getElementById("idErr").style.display = "none"; //Make idErr invisible
}

$(document).ready(function(){
  $("#loginButton").on('click', function(){
    checkLoginData();
  });

  $("#userID").on('click', function(){
    hideIDErr();
  });
  $("#password").on('click', function(){
    hideIDErr();
  });
});
