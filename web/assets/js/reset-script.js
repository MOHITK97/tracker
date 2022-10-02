$(document).ready(function(){
    console.log("+++++++ working")
    $("#form_id_rest").submit(function(e) {
        e.preventDefault();
        var rest_email =$("input[name = 'rest_email']",this).val();
        console.log("++++++++++ email value",rest_email)
            eel.reset_password(rest_email)(function(done){
            if (done=="success"){
                alert("Rest link sent on your mail")
            }else{
                alert("Something went wrong")
            }
        });
    });
});

function goHome(){
    window.location="traker-login.html"
}