<?php
  include("connection.php");
  $client = connect();

  function print_cell( &$cell ) {
    echo "{Cell: {Key: row=" . $cell->key->row . "' column_family='" .
      $cell->key->column_family . "' column_qualifier=";
    if (!empty($cell->key->column_qualifier))
      echo "'" . $cell->key->column_qualifier . "'";
    else
      echo "null";
    echo " ' flag=" . $cell->key->flag . "} value=";
    if (!empty($cell->value))
      echo "'" . $cell->value . "'";
    else
      echo "null";
    echo "\n";
  }

  $ns = $client->namespace_open("Test");

  $result = $client->hql_query($ns, "SELECT * FROM users WHERE ROW = 'person500'");

  foreach ($result->cells as $cell)
  if (!empty($cell->value))
    echo "'" . $cell->value . "'";

  $client->namespace_close($ns);


?>
