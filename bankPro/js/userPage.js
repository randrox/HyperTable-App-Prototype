
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

function getPersonData(setData){
  $.ajax({
    url:'php/userPage.php?option=personData',
          success: setData
  });
}

function getTransfersData(setMovementsData){
  $.ajax({
    url:'php/userPage.php?option=transfersData',
          success: setMovementsData
  });
}

function setMovementsData(result){

}

function setData(result){
  $personData = result.split("-");

  document.getElementById("personName").innerHTML = $personData[0] + " " + $personData[1]; //Set idErr text
  document.getElementById("personName").style.display = "inline"; //Make idErr visible

  document.getElementById("balance").innerHTML = "$" + $personData[2]; //Set idErr text
  document.getElementById("balance").style.display = "inline"; //Make idErr visible
}

$(document).ready(function(){
  getPersonData(setData);
});
