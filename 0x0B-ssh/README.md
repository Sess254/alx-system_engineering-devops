<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
 <h1> Configuration management </h1>
 <p>
 0. Use a private key
mandatory
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:
 <ul>
  <li>Only use ssh single-character flags</li>
  <li>You cannot use -l</li>
  <li>You do not need to handle the case of a private key protected by a passphrase</li>
 </ul>
 </p>

  <p>
 1. Create an SSH key pair
mandatory
Write a Bash script that creates an RSA key pair.

Requirements:
 <ul>
  <li>Name of the created private key must be school</li>
  <li>Number of bits in the created key to be created 4096</li>
  <li>The created key must be protected by the passphrase betty</li>
 </ul>
 </p>

  <p>
 2. Client configuration file
mandatory
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:
<ul>
  <li>Your SSH client configuration must be configured to use the private key ~/.ssh/school</li>
  <li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
 </ul>
 </p>

</body>
</html>
