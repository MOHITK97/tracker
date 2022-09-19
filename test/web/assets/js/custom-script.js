
 jQuery(document).ready(function() {


    //Univesal tab Section
    $('.tab-a').click(function(){  
      $(".tab").removeClass('tab-active');
      $(".tab[data-id='"+$(this).attr('data-id')+"']").addClass("tab-active");
      $(".tab-a").removeClass('active-a');
      $(this).parent().find(".tab-a").addClass('active-a');
    });

    //Primary slider in Blue color
    const primarysliders = document.querySelectorAll('.primary-slider');
        Array.prototype.forEach.call(primarysliders,(slider)=>{
        slider.querySelector('input').addEventListener('input', (event)=>{
        slider.querySelector('span').innerHTML = event.target.value;
        applyprimaryFill(event.target);
        });
        applyprimaryFill(slider.querySelector('input'));
    });
 
    function applyprimaryFill(slider) {
        const percentage = 100*(slider.value-slider.min)/(slider.max-slider.min);
        slider.style.background = `linear-gradient(90deg, #3D9EFF ${percentage}%, #E5E8ED ${percentage+0.1}%)`;
    }

    //Secondry slider in Orange color
    const secondrysliders = document.querySelectorAll('.secondry-slider');
        Array.prototype.forEach.call(secondrysliders,(slider)=>{
        slider.querySelector('input').addEventListener('input', (event)=>{
        slider.querySelector('span').innerHTML = event.target.value;
        applysecondryFill(event.target);
        });
        applysecondryFill(slider.querySelector('input'));
    });
 
    function applysecondryFill(slider) {
        const secondrypercentage = 100*(slider.value-slider.min)/(slider.max-slider.min);
        slider.style.background = `linear-gradient(90deg, #FF973D ${secondrypercentage}%, #E5E8ED ${secondrypercentage+0.1}%)`;
    }

 });

