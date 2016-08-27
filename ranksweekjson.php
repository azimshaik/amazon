<?php header('Access-Control-Allow-Origin: *'); ?>
<?php
 
// Create connection
$con=mysqli_connect("localhost","azim","Az09347108396*","amazon");
 
// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
// This SQL statement selects ALL from the table 'Locations'
$sql1 = "SELECT * FROM `kindleranks` WHERE 1";
$sql2 = "SELECT * FROM `kindleranks` WHERE `id` not in (1,2,3,4,5,6,7,8,9)"; 
$sql = "SELECT avg(amz_best_seller_rank) as amz_best_seller_rank, avg(kin_inf_management) as kin_inf_management, avg(books_business) as books_business, avg(books_inf_management) as books_inf_management , date FROM `kindleranks` WHERE  date between curdate()-7 and curdate() group by date;";
// Check if there are results
if ($result = mysqli_query($con, $sql))
{
	// If so, then create a results array and a temporary one
	// to hold the data
	$resultArray = array();
	$tempArray = array();
 
	// Loop through each row in the result set
	while($row = $result->fetch_object())
	{
		// Add each row into our results array
		$tempArray = $row;
	    array_push($resultArray, $tempArray);
	}
 
	// Finally, encode the array to JSON and output the results
	echo json_encode($resultArray);
}
 
// Close connections
mysqli_close($con);
?>
