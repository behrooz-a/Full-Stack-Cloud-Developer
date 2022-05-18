<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
  color: white;
}

.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 20px;
}

.left {
  left: 0;
  background-color: #111;
}

.right {
  right: 0;
  background-color: red;
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.centered img {
  width: 150px;
  border-radius: 50%;
}
</style>
</head>
<body>

<div class="split left">
  <div class="centered">
    <img src="uottawa.jpg" alt="uottawa">
    <h2>University account</h2>
    <p>If you have an account please log in here.</p>
    <button type="button">Log in</button>
    <p>If you do not have an account create one here.</p>
    <input type="submit" value="Create a new account" />
  </div>
</div>

<div class="split right">
  <div class="centered">
    <img src="student.jpg" alt="student">
    <h2>Personal account</h2>
    <p>Please use login to your personal email here.</p>
    <label for ="uname">  user name:</label>
    <input type="name"  name="uname" placeholder="user name"><br><br>

    <label for ="psw"> password:</label>
    <input type ="passwords"  name="psw" placeholder="password">
    <br><br>

    <button type="button">Log in</button>
    
  </div>
</div>
     
</body>
</html> 
