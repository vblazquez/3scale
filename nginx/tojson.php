<?php 

$xml_content = file_get_contents("http://" . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'] );
$xml = simplexml_load_string($xml_content);
$json = json_encode($xml);

print_r($json);

