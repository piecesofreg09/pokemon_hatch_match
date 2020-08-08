/*
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed hahahahahahahahahahahaha.";
}
*/
$(document).ready(function(){
  // for test purposes
  $("#click").click(function(){
    $('#demo').text("Paragraph changed hahahahahahahahahahahaha.");
  });
  
  var pokemons2_url_js = window.location.origin + pokemons_s2_url;
  $.get(pokemons2_url_js, function(data, status){
    // for select box 1
    console.log(data);

    var new_data = data['results'].map(function(objj) {
      let tempv = {"id": objj.id, "text": objj.id + " - " + objj.text};
      return tempv;
    });
    console.log(data);
    $('.js_pokemon_select1').select2({
      placeholder: "Select pokemon 1",
      allowClear: true,
      data: new_data
    });

    // for select box 2
    $('.js_pokemon_select2').select2({
      placeholder: "Select pokemon 2",
      allowClear: true,
      data: new_data
    });
  });
  

  $('.js_pokemon_select1').on('select2:select', function (e) {
    var data = e.params.data;
    var id = data.id;
    var replaced_sprite_url = sprite_url.replace("100001", id.toString()).replace("100002", "2");
    //console.log(replaced_sprite_url);
    var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
    //console.log(full_replaced_sprite_url);
    $.get(full_replaced_sprite_url, function(data, status){
      console.log(data);
      $("#question_mark_1").hide();
      $("#pokemon_img_1").animate({
        opacity: 0
      }, 1);
      $("#pokemon_img_1").attr({
        "src": data,
        "width": "90%",
        "height": "90%"
      });
      $("#pokemon_img_1").animate({
        opacity: 1
      }, 1500);
    });
  });

  

  $('.js_pokemon_select2').on('select2:select', function (e) {
    var data = e.params.data;
    var id = data.id;
    var replaced_sprite_url = sprite_url.replace("100001", id.toString()).replace("100002", "2");
    //console.log(replaced_sprite_url);
    var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
    //console.log(full_replaced_sprite_url);
    $.get(full_replaced_sprite_url, function(data, status){
      console.log(data);
      $("#question_mark_2").hide();
      $("#pokemon_img_2").animate({
        opacity: 0
      }, 1);
      $("#pokemon_img_2").attr({
        "src": data,
        "width": "90%",
        "height": "90%",
      });
      
      $("#pokemon_img_2").animate({
        opacity: 1
      }, 1500);
      
    });
  });
});
