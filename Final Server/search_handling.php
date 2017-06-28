<?php
//file handling


 
//printing data to page

//echo $_POST["name"] . " " . $_POST["age"];


//to open a file with apped permissions
$myfile = fopen("search.txt", "w") or die("Unable to open file!");


//data to be written to the file 
$put_data = $_POST["name"];

//writing contents to file
fwrite($myfile, $put_data);

//closing file
fclose($myfile);
header('Location: search.php'); 

?>
