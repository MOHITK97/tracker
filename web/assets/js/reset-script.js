$(document).ready(function(){
    console.log("+++++++ working")
    $("#form_id_rest").submit(function(event) {
        event.preventDefault();
        var rest_email =$("input[name = 'rest_email']",this).val();
        console.log("++++++++++ email value",rest_email)
            eel.reset_password(rest_email)(function(done){
            if (done){
                alert(done)
                $('.rest_email').val('');
                window.location="traker-login.html"
            }else{
                alert("Something went wrong")
                $('.rest_email').val('');
            }
        });
    });
});

function goHome(){
    window.location="traker-login.html"
}