<?php
$ip = $_POST["ip"];
$route =  $_POST["route"];
$username = "azim";
$password = "Az09347108396*";
$hostname = "localhost";
$dbname = "amazon";

//connection to the database
$conn = mysql_connect($hostname, $username, $password);


$sql = "insert into `ips` (`ip`,`port`,`date`,`tstamp`)values('".$ip."','".$route."','".date("Y-m-d")."',CURRENT_TIMESTAMP);";
mysql_select_db("amazon",$conn);
//  mysql_select_db("inmoti6_mysite", $con);

$retval = mysql_query( $sql, $conn );
echo "Entered data successfully\n";
mysql_close($conn);

?>
