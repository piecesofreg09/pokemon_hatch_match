
/*
Based on the data selected, manipulate the DOM elements. This function is called
when selection is triggered.
*/ 
function post_select_select2(e, pokemon_box_id) {
  var data = e.params.data;
  var id = data.id;
  var replaced_sprite_url = sprite_url.replace("100001", id.toString()).replace("100002", "2");
  var replaced_stat_url = stat_url.replace("100001", id.toString());
  var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
  var full_replaced_stat_url = window.location.origin + replaced_stat_url;
  
  // get sprite and change DOM elements
  $.get(full_replaced_sprite_url, function(data, status){
    console.log(data);
    $("#question_mark_" + pokemon_box_id).hide();
    $("#pokemon_" + pokemon_box_id).val(id);
    $("#pokemon_img_" + pokemon_box_id).animate({
      opacity: 0
    }, 1);
    $("#pokemon_img_" + pokemon_box_id).attr({
      "src": data,
      "width": "90%",
      "height": "90%"
    });
    $("#pokemon_img_" + pokemon_box_id).animate({
      opacity: 1
    }, 1000);
  });

  // get stat and change DOM elements
  $.get(full_replaced_stat_url, function(data, status){
    console.log(data);
    $("#pokemon_" + pokemon_box_id + "_name").text(data.data.name);
    $("#pokemon_" + pokemon_box_id + "_hp").text(data.data.hp);
    $("#pokemon_" + pokemon_box_id + "_attack").text(data.data.attack);
    $("#pokemon_" + pokemon_box_id + "_defense").text(data.data.defense);
  });
}

/*
Based on the data selected, manipulate the DOM elements. This function is called
when there is existing value
*/ 
function post_select_existing_value(pokemon_id, pokemon_box_id) {
  var id = pokemon_id;
  var replaced_sprite_url = sprite_url.replace("100001", id.toString()).replace("100002", "2");
  var replaced_stat_url = stat_url.replace("100001", id.toString());
  var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
  var full_replaced_stat_url = window.location.origin + replaced_stat_url;
  
  // get sprite and change DOM elements
  $.get(full_replaced_sprite_url, function(data, status){
    console.log(data);
    $("#question_mark_" + pokemon_box_id).hide();
    $("#pokemon_" + pokemon_box_id).val(id);
    $("#pokemon_img_" + pokemon_box_id).animate({
      opacity: 0
    }, 1);
    $("#pokemon_img_" + pokemon_box_id).attr({
      "src": data,
      "width": "90%",
      "height": "90%"
    });
    $("#pokemon_img_" + pokemon_box_id).animate({
      opacity: 1
    }, 1);
  });

  // get stat and change DOM elements
  $.get(full_replaced_stat_url, function(data, status){
    console.log(data);
    $("#pokemon_" + pokemon_box_id + "_name").text(data.data.name);
    $("#pokemon_" + pokemon_box_id + "_hp").text(data.data.hp);
    $("#pokemon_" + pokemon_box_id + "_attack").text(data.data.attack);
    $("#pokemon_" + pokemon_box_id + "_defense").text(data.data.defense);
  });
}


$(document).ready(function(){
  // for test purposes
  $("#click").click(function(){
    $('#demo').text("Paragraph changed.");
  });
  
  const json_poke_from_django = JSON.parse(document.getElementById('pokemon_data').textContent);
  
  $('.js_pokemon_select1').select2({
    placeholder: "Select pokemon 1",
    allowClear: true,
    data: json_poke_from_django["results"]
  });

  // for select box 2
  $('.js_pokemon_select2').select2({
    placeholder: "Select pokemon 2",
    allowClear: true,
    data: json_poke_from_django["results"]
  });

  $('.js_pokemon_select1').on('select2:select', function(e) {
    post_select_select2(e, "1");
  });
  $('.js_pokemon_select2').on('select2:select', function(e) {
    post_select_select2(e, "2");
  });

  if ($("#pokemon_1").val() > 0) {
    console.log("in existing values.")
    post_select_existing_value($("#pokemon_1").val(), "1");
    var idd = json_poke_from_django['results'][$("#pokemon_1").val() - 1]['id'];
    $('.js_pokemon_select1').val(idd).trigger('change');
  }

  if ($("#pokemon_2").val() > 0) {
    post_select_existing_value($("#pokemon_2").val(), "2");
    var idd = json_poke_from_django['results'][$("#pokemon_2").val() - 1]['id'];
    $('.js_pokemon_select2').val(idd).trigger('change');
  }

  console.log("show pokemon 1 value: " + $("#pokemon_1").val());
  console.log("show pokemon 2 value: " + $("#pokemon_2").val());
  console.log("from django data:");
  
});
