<?php
  if (!isset($GLOBALS['THRIFT_ROOT']))
      $GLOBALS['THRIFT_ROOT'] = getenv('PHPTHRIFT_ROOT');

  require_once dirname(__FILE__).'/ThriftClient.php';

  function connect(){
    try {     
      $client = new Hypertable_ThriftClient("localhost", 15867);
    }
    catch (\Hypertable_ThriftGen\ClientException $e) {
      echo "error: $e->message\n";
      exit(1);
    }

    return $client;
  }
?>
