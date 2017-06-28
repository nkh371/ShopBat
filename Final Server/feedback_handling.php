<?php
//file handling


 
//printing data to page

//echo $_POST["name"] . " " . $_POST["age"];


//to open a file with apped permissions
$myfile = fopen("feedback.txt", "a") or die("Unable to open file!");


//data to be written to the file 
$put_data1 = $_POST["q1"];
$put_data2= $_POST["text"];
$n = "\n";

//writing contents to file
fwrite($myfile, $put_data1);
fwrite($myfile, $n);
fwrite($myfile, $put_data2);
fwrite($myfile, $n);
fwrite($myfile, $n);
//closing file
fclose($myfile);
header('Location: feedback.php'); 

?>
