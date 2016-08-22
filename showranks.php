<?php
$username = "azim";
$password = "Az09347108396*";
$hostname = "localhost"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password,'amazon') 
or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";
?>

<html>
<head>
</head>
<body>
<h1>PHP connect MySQL</h1>
<?php
$query = "select * from `paperbackranks` where 1;";
mysql_query($dbhandle,$query) or die ('error querying database');
$result = mysql_query($db, $query);
$row = mysql_fetch_array($result);

while($row = mysql_fetch_array($result)){
echo $row['amz_best_seller_rank'].''.$row['date'].'<br/>';
}
?>
</body>
</html>
