<?php include "blog.php" ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <div class="refs">
        <a href="login.html">Login</a>
        <a href="register.html">Register</a>
        <?php if (isset($_SESSION['username'])): ?>
        <a href="logout.php">Logout</a>
    <?php endif; ?>
    </div>
    <br><br><br><br>
    <div class="container">
        <h1>Welcome to this Pen Test website!</h1>
        <h2>Made by Ambriel</h2>
        <h3>
            The goal of this is to try and bruteforce and get user information
            (Username, email and Passwords/Hashes) from the SQL database.
        </h3>

      <!-- this is just to check if the user is logged in, then they can add a post to the blog -->
        <?php if (isset($_SESSION['username'])): ?>
            <div class="blog-form">
                <h3>Post a new blog:</h3>
                <form action="index.php" method="POST">
                    <textarea name="content" rows="5" cols="50" required></textarea><br>
                    <button type="submit">Submit</button>
                </form>
            </div>
        <?php else: ?>
            <p>Please log in to post a blog.</p>
        <?php endif; ?>

        <hr>

        <!-- this just a function to show the user the posts that have been posted -->
        <h3>Blog Posts:</h3>
        <?php while ($row = $result->fetch_assoc()): ?>
            <div class="blog-post">
                <p><strong><?php echo htmlspecialchars($row['username']); ?></strong> posted on <?php echo $row['created_at']; ?>:</p>
                <p><?php echo nl2br(htmlspecialchars($row['content'])); ?></p>
                <hr>
            </div>
        <?php endwhile; ?>
    </div>
</body>
</html>
