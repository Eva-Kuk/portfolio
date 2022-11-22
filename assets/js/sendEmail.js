//Send email from the contact form
//create sendMail() function

function sendMail(contactForm) {
    emailjs.send('gmail', 'contact_form', {
        "form_name": contactForm.name.value,
        "form_email": contactForm.email.value,
        "form_subject": contactForm.subject.value,
        "message": contactForm.message.value
    })
        .then(
            // Alert sent if email is successful
            function () {
                //CREDIT: Stack Overflow, for the alert solution
                alert("Your email has been sent successfully, I will be in touch with you as soon as possible");
                window.location.reload(true);
            },
            // Alert sent if email fails
            function () {
                alert("Unfortunately your email was not sent, please try again");
                window.location.reload(true);
            });
    // immediately stops reloading the page
    return false;
}