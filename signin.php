<?php
session_start();

$con=mysqli_connect('148.72.232.176:3306','login_and_signup','Abhi84200@1','dball');
mysqli_select_db($con,'signin.php');

$name=$_POST['name'];
$email=$_POST['email'];
$clg_name=$_POST['clg_name'];
$passwords=$_POST['passwords']

$s= " select * from usertable where email='$email' && password='$passwords';
$result=mysqli_query($con,$s);
$num=mysqli_num_rows($result);

if($num==1){
   header('location:index.html');
}
else
{
    header('location: login.html');
}
?>
