$(document).ready(function(){
    

  $("#form_id").submit(function(event){
    event.preventDefault();
    var email = $("input[name='email']",this).val();
    var password = $("input[name='password']",this).val();
    
      eel.random_login(email,password)(function(done){
        console.log(done+"ppppppppppppppp")

      if(done=="success"){
        var url = "traker.html";


      $(location).prop('href', url);

      }

      if(done == "email"){
        alert("please enter the email")
      }

      else if(done == "password"){
        alert("please enter the password")
      }

      else if(done == "email & password"){
        alert("please enter the email and password")
      }
      else if(done == "Your shift is not started"){
        alert("Your shift is not started")
      }

      else if(done == "Your shift is ended"){
        alert("Your shift is ended")
      }

      else if(done == "Email is Invalid"){
        alert("Email is Invalid")
      }

      else{
        $('.email').val('');
        $('.password').val('');

      }
    })
    
  });


});

