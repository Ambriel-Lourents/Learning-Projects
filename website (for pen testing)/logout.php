<?php 
session_start();

// this would kill the session
session_unset();
session_destroy();

// this is just basic redirection to index.php (MAIN PAGE)
header("Location: index.php");
exit();
?>