<?php
session_start();

//Connect to the database duh.
$conn = new mysqli('localhost','root','', 'user_system');
if ($conn->connect_error){
    die("Connection failed:" . $conn->connect_error);
}

//This is to save user blogs in the db.
if ($_SERVER['REQUEST_METHOD'] &&$_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['username'])){
    $content  = $_POST['content'];
    $username = $_SESSION['username'];

    $stmt = $conn->prepare("INSERT INTO posts (username, content) VALUES (?, ?)");
    $stmt->bind_param("ss",$username, $content);
    $stmt->execute();
    $stmt->close();
}

$result = $conn->query("SELECT username, content, created_at FROM posts ORDER BY created_at DESC");
?>