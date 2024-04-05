<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $phone = $_POST["phone"];
    $country = $_POST["country"];
    $message = $_POST["message"];

    // Process the form data (e.g., send an email, save to a database, etc.)
    // You can customize this part based on your requirements.

    // Example: Sending an email
    $to = "madeccco@gmail.com";
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nPassword: $password\nPhone: $phone\nCountry: $country\nMessage:\n$message";
    mail($to, $subject, $body);

    // Redirect to a thank-you page or display a success message
    header("Location: thank_you.html");
    exit;
}
?>
