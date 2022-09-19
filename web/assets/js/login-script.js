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
      else{
        alert("please enter valid details")
        $('.email').val('');
        $('.password').val('');

      }
    })
    
  });


});

