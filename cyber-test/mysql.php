<?php
/**
 * Secure User Query Script
 * Demonstrates prepared statements and proper error handling
 */

// Load database credentials from external config (outside web root)
require_once(__DIR__ . '/../config/database.php');

// Create database connection
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check connection (without exposing details)
if ($conn->connect_error) {
    error_log("Database connection failed: " . $conn->connect_error);
    die("An error occurred. Please try again later.");
}

// Validate and sanitize input
if (!isset($_GET['id']) || !is_numeric($_GET['id'])) {
    http_response_code(400);
    die("Invalid request.");
}

$id = intval($_GET['id']);

// Use prepared statement to prevent SQL injection
$stmt = $conn->prepare("SELECT name FROM users WHERE id = ?");
if (!$stmt) {
    error_log("Prepare failed: " . $conn->error);
    die("An error occurred. Please try again later.");
}

// Bind parameter (i = integer)
$stmt->bind_param("i", $id);

// Execute query
if (!$stmt->execute()) {
    error_log("Execute failed: " . $stmt->error);
    die("An error occurred. Please try again later.");
}

// Get result
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    // Escape output to prevent XSS
    echo "User: " . htmlspecialchars($row["name"], ENT_QUOTES, 'UTF-8');
} else {
    echo "No user found.";
}

// Clean up
$stmt->close();
$conn->close();
?>