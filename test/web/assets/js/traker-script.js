 jQuery(document).ready(function() {

  
  localStorage.setItem("total_time_sec", "00");

  localStorage.setItem("total_time_min", "00");
  localStorage.setItem("total_time_hr", "00");

  sec_check=localStorage.getItem("total_time_sec");
  min_check=localStorage.getItem("total_time_min");
  hr_check = localStorage.getItem("total_time_hr");
  res=String(hr_check)+":"+String(min_check)+":"+String(sec_check)+" hrs"

$(".m-title").html(res);
    //Univesal tab Section
    $('.tab-a').click(function(){  
      $(".tab").removeClass('tab-active');
      $(".tab[data-id='"+$(this).attr('data-id')+"']").addClass("tab-active");
      $(".tab-a").removeClass('active-a');
      $(this).parent().find(".tab-a").addClass('active-a');
    });

    $(".activate-button").click(function(){
      $(".trak-info-section").toggleClass("user-active");
      if ($(".user-active")[0]){
    // Do something if class exists

       // 1 second interval 1000
        var set_time_Interval = 1000;
        mySetInterval= setInterval(function () {
        var interval=1
        var total_time_sec = localStorage.getItem("total_time_sec");
        var sum=parseInt(total_time_sec)+interval;

        localStorage.setItem("total_time_sec", sum);
        // alert(total_time);
        sec_check=localStorage.getItem("total_time_sec");
        console.log(sec_check);
        if(sec_check ==60){
          var total_time_min = localStorage.getItem("total_time_min");
          var sum=parseInt(total_time_min)+1;
          localStorage.setItem("total_time_min", sum);

          var total_time_min = localStorage.getItem("total_time_min");

          console.log("1 minute ho gya",total_time_min)

          localStorage.setItem("total_time_sec", 0);
        }
        min_check=localStorage.getItem("total_time_min");

        if(min_check ==60){
          var total_time_hr = localStorage.getItem("total_time_hr");
          var sum=parseInt(total_time_hr)+1;
          localStorage.setItem("total_time_hr", sum);

          var total_time_hr = localStorage.getItem("total_time_hr");

          console.log("hour ho gya",total_time_hr)

          localStorage.setItem("total_time_min", 0);
        }
        sec_check=localStorage.getItem("total_time_sec");
        min_check=localStorage.getItem("total_time_min");
        hr_check = localStorage.getItem("total_time_hr");
        if(sec_check.length==1){
          sec_check="0"+String(sec_check);
          }
        if(min_check.length==1){
          min_check="0"+String(min_check);
          }
        if(hr_check.length==1){
          hr_check="0"+String(hr_check);
          }

        console.log(sec_check.length);
        res=String(hr_check)+":"+String(min_check)+":"+String(sec_check)+" hrs"


        $(".m-title").html(res);
          }, set_time_Interval);


        alert("active");
        eel.start_thread()(function(done){
          if(done=="success"){
            alert("going good")
          }
            })


      } else {
          // Do something if class does not exist
            alert("deactive")
            clearInterval(mySetInterval);
            eel.stop()(function(done){
                if(done=="success"){
                  alert("jjjjjjjjj")
                }
                  })
            }

          });

       });



// Onclick of the button
document.querySelector("button").onclick = function () {  
  // Call python's random_python function
  eel.random_python()(function(number){                      
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerHTML = number;
  })
}



$(document).ready(function(){
  $("#form_id").submit(function(event){
    event.preventDefault();
    var email = $("input[name='email']",this).val();
    var password = $("input[name='password']",this).val();
    
    eel.random_login(email,password)(function(done){

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

$(document).ready(function(){
  $(".activate-button").click(function(){
    eel.breakstart()(function(msg){

      if (msg == "start"){
        alert("you cannot take a break in last 1 hour")}
      else{
        alert("you cannot take a break in first 1 hour")
      }

    }
  )
  
});
});
