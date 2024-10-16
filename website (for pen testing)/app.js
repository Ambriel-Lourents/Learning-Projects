function login() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username === "admin" && password === "password") {
    alert("Login successful! Redirecting to admin panel.");
  } else {
    alert("Login failed. Please check your username and password.");
  }
}
