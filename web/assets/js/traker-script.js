function call(time){
mtime=time;
var hr=time/60;
// console.log("hr",hr)
var hr=parseInt(hr);
var ch=hr*60
var min=mtime-ch

console.log("min",min)
if(hr<10){
  hr="0"+hr
}

if(min<10){
  min="0"+min
}
console.log(hr+":"+min,"0000000000000000000000000000")

return hr+":"+min


}



$(window).load(function() {

  eel.breaktimeleft()(function(brleft){
    localStorage.setItem("brleft", brleft);
    console.log(brleft,"brleftbrleft")


   })

    
 eel.cwwd()(function(token){
      // alert(token)
    var settings = {
      "url": "https://timedoctor.niraginfotech.com/api/user/dashboard",
      "method": "GET",
      "timeout": 0,
      "headers": {
        "Authorization": "Bearer "+String(token)
      },
    };

    $.ajax(settings).done(function (response) {
      var checks=response.success;
      console.log(response)
      //   console.log(response.getYesterDayHours[0].minutes)
      //   console.log(response.getThisWeekHours[0].minutes)
      //   console.log(response.getThisMonthHours[0].minutes)
      if(checks==true){
        if(response.getTodayHours[0].minutes==0){
          localStorage.setItem("getTodayHours", "00:00");
        }
        else{
          localStorage.setItem("getTodayHours", call(response.getTodayHours[0].minutes));
        }

        if(response.getYesterDayHours[0].minutes==0){
          localStorage.setItem("getYesterDayHours", "00:00");
        }
        else{
          localStorage.setItem("getYesterDayHours", call(response.getYesterDayHours[0].minutes));
        }

        if(response.getThisWeekHours[0].minutes==0){
          localStorage.setItem("getThisWeekHours", "00:00");
        }
        else{
          localStorage.setItem("getThisWeekHours", call(response.getThisWeekHours[0].minutes));
        }

        if(response.getThisMonthHours[0].minutes==0){
          localStorage.setItem("getThisMonthHours", "00:00");
        }
        else{
          localStorage.setItem("getThisMonthHours", call(response.getThisMonthHours[0].minutes));
        }

        

        
        // localStorage.setItem("getYesterDayHours", call(response.getYesterDayHours[0].minutes));
        // localStorage.setItem("getThisWeekHours", call(response.getThisWeekHours[0].minutes));
        // localStorage.setItem("getThisMonthHours", call(response.getThisMonthHours[0].minutes));



        
      }
      else{
        console.log("not working")
      }
    });




      var settings = {
      "url": "https://timedoctor.niraginfotech.com/api/user/get/tracking/time",
      "method": "GET",
      "timeout": 0,
      "headers": {
        "Authorization": "Bearer "+String(token)
      },
    };



    $.ajax(settings).done(function (response) {
      if(response.isStarted!=false){
     
      localStorage.setItem("today", "yes");
  }
  else{
   localStorage.setItem("today", "no");
  }
  });

     })
}); 




 jQuery(document).ready(function() {

  // localStorage.setItem("total_time_sec", "00");
  // localStorage.setItem("total_time_min", "00");
  // localStorage.setItem("total_time_hr", "00");


    
    
    var url  = window.location.href;  
    check =url.includes("traker.html");
    if(check==true){
      window.resizeTo(570, 410);
      
    }
    setTimeout(function(){
      var today=localStorage.getItem("today");

      if(today=="yes"){
      var getTodayHours=localStorage.getItem("getTodayHours");
      var hr=getTodayHours.split(":")[0]
      var min=getTodayHours.split(":")[1]
      var sec="00"


      var sec_check=localStorage.setItem("total_time_sec",sec);
      var min_check=localStorage.setItem("total_time_min",min);
      var hr_check = localStorage.setItem("total_time_hr",hr);
      

      }
      else{
        var getTodayHours="00:00"
        var hr=getTodayHours.split(":")[0]
        var min=getTodayHours.split(":")[1]
        var sec="00"
        var sec_check=localStorage.setItem("total_time_sec",sec);
        var min_check=localStorage.setItem("total_time_min",min);
        var hr_check = localStorage.setItem("total_time_hr",hr);
      }


      var sec_check="00"
      var getYesterDayHours=localStorage.getItem("getYesterDayHours");
      var getThisWeekHours = localStorage.getItem("getThisWeekHours");
      var getThisMonthHours = localStorage.getItem("getThisMonthHours");

      $("#yesterday .time").html(getYesterDayHours+" hr")
      $("#thisweek .time").html(getThisWeekHours+" hr")
      $("#thismonth .time").html(getThisMonthHours+" hr")

      var brleft = localStorage.getItem("brleft");

       $("#brleft .brleft").html("00:"+brleft+" min");

    
    

    res=getTodayHours+":"+String(sec_check)+" hrs"

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
          // console.log(sec_check);
          if(sec_check ==60){
            var total_time_min = localStorage.getItem("total_time_min");
            var sum=parseInt(total_time_min)+1;
            localStorage.setItem("total_time_min", sum);

            var total_time_min = localStorage.getItem("total_time_min");

            // console.log("1 minute ho gya",total_time_min)

            localStorage.setItem("total_time_sec", 0);
          }
          min_check=localStorage.getItem("total_time_min");

          if(min_check ==60){
            var total_time_hr = localStorage.getItem("total_time_hr");
            var sum=parseInt(total_time_hr)+1;
            localStorage.setItem("total_time_hr", sum);

            var total_time_hr = localStorage.getItem("total_time_hr");

            // console.log("hour ho gya",total_time_hr)

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

          // console.log(sec_check.length);
          // var getTodayHours=localStorage.getItem("getTodayHours");

          res=String(hr_check)+":"+String(min_check)+":"+String(sec_check)+" hrs"
          // res=getTodayHours+":"+String(sec_check)+" hrs"

          $(".m-title").html(res);
            }, set_time_Interval);


          // alert("active");
          eel.start_thread()(function(done){
            if(done=="error"){
              $(".trak-info-section").toggleClass("user-active");
              clearInterval(mySetInterval);
              alert("your shift is not started yet")

              // console.log("gg")
            }
              })


        } else {
            // Do something if class does not exist
              // alert("deactive")
              clearInterval(mySetInterval);
              eel.stop()(function(done){
                  if(done=="success"){
                    // alert("jjjjjjjjj")
                    // console.log("gg")
                    
                  }

                  if(done=="noo"){
                    $(".trak-info-section").toggleClass("user-active");
                    alert("you can not take break at that time")
                    
                  }

                  if(done=="not"){
                    $(".trak-info-section").toggleClass("user-active");
                    alert("This is not your shift time")
                    
                  }
                    })
                }

      });

     } , 5000);

     });







 jQuery(document).ready(function() {
  $('.Logout').click(function(){  
        eel.logout()(function(done){
        if(done=="success"){
          // alert("jjjjjjjjj")
          // console.log("gg")
          var url = "traker-login.html";

          $(location).prop('href', url);
        }
          })
      });
 });






function onReady() {
    window.open("http://localhost:1111/","myWindow","dialog=yes,resizable=0");
}

$(document).ready(function(){
  $(".toaster").hide()
  eel.expose(say_hello_js); // Expose this function to Python
  eel.expose(get_timer_js);
  function say_hello_js(x) {
      if (x == "done"){
          // document.getElementById("error").style.display = 'block';
          
         //document.getElementById("error").fadeOut(3000);
          //$(".toaster").fadeOut(5000)
          //$('.toaster').fadeIn('fast').delay(1000).fadeOut('fast');
          //$('.toaster').fadeIn('fast').delay(1000).fadeOut('fast');
          $('.toaster').fadeIn('slow').delay(3000).hide(0);
          //$('.toaster').fadeIn('slow').delay(1000).hide(0);
          console.log("i am in if condition" + x);
      }else{
          $(".toaster").hide()
          //document.getElementById("error").style.display = 'none';
          console.log("i am in else condition" + x);
      }
  }
  say_hello_js("Javascript World!");

  function get_timer_js(key_press,mouse_click){
    // console.log("+++++++++++ key_press" + key_press)
    // console.log("+++++++++++ mouse_click" + mouse_click)
    if ((key_press == 0 ) && (mouse_click == 0)){
      console.log("+++++++++++ now i am here")
      swal({
        title: 'Are you still working ?',
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        type: 'warning',
        buttonsStyling: false
    }).then(function (yes) {
        // Called if you click Yes.
        if (yes) {
            // Make Ajax call.
            swal('Your Work is continues', '', 'success');
        }
    },
    function (no) {
        // Called if you click No.
        if (no == 'cancel') {
            swal('Your work has been stoped', '', 'error');
        }
    });

      console.log("i am in if condition"+ x)
    }else{
      console.log("i am in else condition")
    }
  }
  $(".open_window").on("click",function(){
    window.open('https://reliable-stroopwafel-6da05f.netlify.app/users')
})

})

