<?php
  include("connection.php");
  $client = connect();
  session_start();
  $personID = session_id();


  if ($personID != ""){
    $ns = $client->namespace_open("Bank");

    $personData = $client->hql_query($ns, "SELECT * FROM person WHERE ROW = '".$personID."'");
    $results = "";
    foreach ($personData->cells as $cell){

        $results .= $cell->value . "-";
    }
    echo $results;
    $client->namespace_close($ns);
  }else{

    echo "error";
  }

?>
