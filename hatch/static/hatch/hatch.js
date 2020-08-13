function mixStat(stat1, stat2) {
  var fields = ['attack', 'defense', 'special_attack',
    'special_attack_acc_rounds', 'special_defense', 'speed',
    'hp', 'weight', 'height', 'base_exp', 'cost'];
  console.log(stat1);
  console.log(stat2);
  var res = {};
  for (field of fields) {
    console.log(field);
    console.log(stat1[field]);
    console.log(stat2[field])
    res[field] = ranMix(stat1[field], stat2[field]);
  }
  var name1, name2, r1, r2;
  r1 = (1 + Math.random() * 3.5) / 5;
  r2 = (1 + Math.random() * 3.5) / 5;
  //console.log(r1);
  //console.log(r2);
  if (Math.random() < 0.5) {
    name1 = stat1['name'];
    name2 = stat2['name'];
  }
  else {
    name1 = stat2['name'];
    name2 = stat1['name'];
  }
  console.log(name1 + name2);
  //console.log(name1.slice(0, Math.floor(r1 * name1.length)));
  //console.log(name2.slice(-Math.floor(r2 * name2.length)));
  res['name'] = name1.slice(0, Math.floor(r1 * name1.length)) + 
  name2.slice(-Math.floor(r2 * name2.length));
  //console.log(res['name']);

  return res;
}

function ranMix(val1, val2) {
  var val_min = Math.min(val1, val2);
  var val_max = Math.max(val1, val2);
  return Math.floor(Math.random() * (val_max - val_min) + val_min);
}

// Building sprites with stats data
const forLoop = async (pokemon_1, pokemon_2) => {
  var scan_dict = {'1': pokemon_1, '2': pokemon_2};
  var stat_list = [];
  console.log('Start');
  for (key in scan_dict) {
    var box_id = key;
    //console.log('box: ' + box_id);
    var pokemon_id = scan_dict[key];
    var replaced_sprite_url = sprite_url.replace("100001", pokemon_id.toString()).replace("100002", "2");
    var replaced_stat_url = stat_url.replace("100001", pokemon_id.toString());
    var replaced_pokemon_url = pokemon_url.replace("100001", pokemon_id.toString());
    var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
    var full_replaced_stat_url = window.location.origin + replaced_stat_url;
    var full_replaced_pokemon_url= window.location.origin + replaced_pokemon_url
    //console.log(full_replaced_sprite_url);
  
    //console.log(box_id);
    const sprite_link = await $.get(full_replaced_sprite_url)
    
    //console.log(sprite_link);
    //console.log('inside_get: ' + box_id);
    //console.log("#pokemon_img_" + box_id);
    $("#pokemon_img_" + box_id).attr({
      "src": sprite_link,
      "width": "130vmin",
    });

    // get stat and change DOM elements
    const data = await $.get(full_replaced_stat_url);
    
    // get pokemon weight, height .. 
    const data2 = await $.get(full_replaced_pokemon_url);
    const data_final = Object.assign({}, data['data'], data2['data']);
    console.log('after await data');
    console.log(data_final);
    stat_list.push(data_final);
  }
  console.log('End');
  
  return stat_list;
}

const changeStat = (table, field_show, mix_stat) => {
  table.empty();
  table.append('<tr><th colspan="3">' + mix_stat['name'] + '</th></tr>');
  for (field of field_show) {
    table.append('<tr><td>' + field + '</td><td>' + mix_stat[field] + '</td></tr>');
  }
  
};

const addFormElements = (form, field_all, mix_stat, p1, p2) => {
  for (field of field_all) {
    form.append('<input type="hidden" name="' + field + '" value="' + mix_stat[field] + '">')
  }
  form.append('<input type="hidden" name="pokemon_1" value="' + p1 + '">');
  form.append('<input type="hidden" name="pokemon_2" value="' + p2 + '">');
};

$(document).ready(async function(){

  var field_all = ['attack', 'defense', 'special_attack',
  'special_attack_acc_rounds', 'special_defense', 'speed',
  'hp', 'name', 'weight', 'height', 'base_exp', 'cost'];
  var field_show = ['attack', 'defense', 'special_attack',
  'special_defense', 'speed','hp'];

  //console.log(pokemon_1);
  //console.log(pokemon_2);
  var stat_list = [];
  var final_stat = [];

  
  // call for loop, return the result pair
  stat_list = await forLoop(pokemon_1, pokemon_2);
  //console.log("After promise");
  //console.log(stat_list);

  // mix the data and change DOM elements
  var mix_stat_res = await mixStat(stat_list[0], stat_list[1]);
  //console.log(mix_stat_res);
  //console.log(post_url);
  

  var table_1 = await $("#table_1");
  await changeStat(table_1, field_show, stat_list[0]);
  var table_2 = await $("#table_2");
  await changeStat(table_2, field_show, stat_list[1]);
  var table_mix = await $("#result_table");
  await changeStat(table_mix, field_show, mix_stat_res);
  var form = await $("form");
  await addFormElements(form, field_all, mix_stat_res, pokemon_1, pokemon_2);
  

  // set post data using js
  /* deprecated, using django post form instead
  $("#confirm").click(function() {
    console.log("Confirm clicked");
    var full_post_url = window.location.origin + post_url;
    console.log(full_post_url);
    console.log(csrf_token);
    var to_send = Object.assign({}, mix_stat_res, {"csrfmiddlewaretoken": encodeURIComponent(csrf_token)});
    $.post(full_post_url, to_send);
  });
  */

  // set change data
  $("#change").click(function() {
    console.log("Change clicked");
    var table_mix = $("#result_table");
    var mix_stat_res = mixStat(stat_list[0], stat_list[1]);
    changeStat(table_mix, field_show, mix_stat_res);
    var form = $("form");
    addFormElements(form, field_all, mix_stat_res, pokemon_1, pokemon_2);
  });

  
});
