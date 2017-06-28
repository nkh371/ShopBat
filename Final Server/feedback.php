<!DOCTYPE html>
<html>
<head>
    <title>Feedback</title>
    <link rel="icon" type="image/gif/png" href="icon.png">
    <link rel="stylesheet" type="text/css" href="feedback.css">
</head>
<body>
    <div id="container">
        <h3>Your Feedback is very Important to us.</h3>
        <form action="feedback_handling.php" method="POST">
            
        
        <p>Q.- How oftenly do you use Shop Bat extension ?</p>
        <p>Your Answer</p>
        <input type="radio" name="q1" value="always">Always<br/>
        <input type="radio" name="q1" value="sometimes">Sometimes<br/>
        <input type="radio" name="q1" value="never">Never<br/>

        <p>Any other Feedback you want to give us</p>
        <textarea id="textarea" name="text" placeholder="Enter your text here"></textarea>
        <br/>
        <br/>
        <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>