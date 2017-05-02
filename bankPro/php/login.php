<?php
  include("connection.php");
  $client = connect();

  $personID = $_GET['ID'];
  $password = $_GET['password'];


  $ns = $client->namespace_open("Bank");

  $result = $client->hql_query($ns, "SELECT * FROM login WHERE ROW = '".$personID."' AND password = '".$password."'");

  foreach ($result->cells as $cell)
  if (!empty($cell->value)){
    session_id($personID);
    session_start();
    echo getPeopleName($client, $ns, $personID);
  }else{
    echo "error";
  }
  $client->namespace_close($ns);

  function getPeopleName($client, $ns, $personID){
    $personData = $client->hql_query($ns, "SELECT * FROM person WHERE ROW = '".$personID."'");
    $results = "";
    foreach ($personData->cells as $cell){

        $results .= $cell->value . "-";
    }
    echo $results;
 }
?>
