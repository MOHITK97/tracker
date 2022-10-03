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
      if(done == "Your shift is not started"){
        alert("Your shift is not started now")
        $('.email').val('');
        $('.password').val('');
      }

      else if(done == "Your shift is ended"){
        alert("Your shift is Completed now")
        $('.email').val('');
        $('.password').val('');
      }

      else if(done == "Email is Invalid"){
        alert("Email is Invalid")
        $('.email').val('');
        $('.password').val('');
      }

      else{
        // alert("Credentials are incorrect")
        $('.email').val('');
        $('.password').val('');

      }
    })
    
  });


});

