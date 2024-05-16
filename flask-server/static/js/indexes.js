const email = document.getElementById('email');
const verifyCodeButton = document.getElementById('verify-code-button');
const verificationCodeInput = document.getElementById('verification_code');
let otp_val;

verifyCodeButton.addEventListener('click', (e) => {
  e.preventDefault();

  otp_val = Math.floor(Math.random() * 100000) + 400000;
  let bodyy = `Your code is: ${otp_val}`;

  Email.send({
    SecureToken: "f4b20c1a-4d06-407f-91ea-11dca5a51448",
    To: email.value,
    From: "skniveditha69@gmail.com",
    Subject: "Test",
    Body: bodyy
  }).then(message => {
    if (message === "OK") {
      alert("Mail sent");
      document.getElementById('verification-code-container').style.display = 'block';
      document.getElementById('authenticate-button').style.display = 'block';
      verifyCodeButton.disabled = true;
    } else {
      alert("Error sending mail");
    }
  });
});

function authenticate() {
  const userEnteredCode = verificationCodeInput.value;

  if (userEnteredCode == otp_val) {
    // If the entered code matches the generated code
    document.getElementById('verify-code-button').style.display = 'none';
    document.getElementById('authenticate-button').style.display = 'none';
    document.getElementById('new-password-group').style.display = 'block';
    document.getElementById('confirm-password-group').style.display = 'block';
    document.getElementById('submit-group').style.display = 'block';
  } else {
    alert("Verification code is incorrect");
  }
}
document.getElementById('authenticate-button').addEventListener('click', authenticate);