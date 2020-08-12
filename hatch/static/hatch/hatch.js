function mix_stat(stat1, stat2) {
  var fields = ['attack', 'defense', 'special_attack',
    'special_attack_acc_rounds', 'special_defense', 'speed',
    'hp'];
  console.log(stat1);
  console.log(stat2);
  var res = {};
  for (field of fields) {
    //console.log(field);
    //console.log(stat1[field])
    res[field] = ran_mix(stat1['data'][field], stat2['data'][field]);
  }
  var name1, name2, r1, r2;
  r1 = (1 + Math.random() * 3.5) / 5;
  r2 = (1 + Math.random() * 3.5) / 5;
  console.log(r1);
  console.log(r2);
  if (Math.random < 0.5) {
    name1 = stat1['data']['name'];
    name2 = stat2['data']['name'];
  }
  else {
    name1 = stat2['data']['name'];
    name2 = stat1['data']['name'];
  }
  console.log(name1.slice(0, Math.floor(r1 * name1.length)));
  console.log(name2.slice(-Math.floor(r2 * name2.length)));
  res['name'] = name1.slice(0, Math.floor(r1 * name1.length)) + 
  name2.slice(-Math.floor(r2 * name2.length));
  console.log(res['name']);

  return res;
}

function ran_mix(val1, val2) {
  var val_min = Math.min(val1, val2);
  var val_max = Math.max(val1, val2);
  return Math.floor(Math.random() * (val_max - val_min) + val_min);
}

$(document).ready(function(){
  console.log(pokemon_1);
  console.log(pokemon_2);
  var scan_dict = {'1': pokemon_1, '2': pokemon_2};
  var stat_list = [];
  var final_stat = [];
  const forLoop = async _ => {
    console.log('Start')
    for (key in scan_dict) {
      var box_id = key;
      console.log('box: ' + box_id);
      var pokemon_id = scan_dict[key];
      var replaced_sprite_url = sprite_url.replace("100001", pokemon_id.toString()).replace("100002", "2");
      var replaced_stat_url = stat_url.replace("100001", pokemon_id.toString());
      var full_replaced_sprite_url = window.location.origin + replaced_sprite_url;
      var full_replaced_stat_url = window.location.origin + replaced_stat_url;
      console.log(full_replaced_sprite_url);
    
      console.log(box_id);
      const sprite_link = await $.get(full_replaced_sprite_url)
      
      console.log(sprite_link);
      console.log('inside_get: ' + box_id);
      console.log("#pokemon_img_" + box_id);
      $("#pokemon_img_" + box_id).attr({
        "src": sprite_link,
        "width": "90%",
        "height": "90%"
      });

      // get stat and change DOM elements
      const data = await $.get(full_replaced_stat_url);
      console.log(data);
      stat_list.push(data);
      $('#table_' + box_id).append('<tr><td>HP</td><td>123</td></tr>');
      $('#table_' + box_id).append('<tr><td>CP</td><td>123</td></tr>');
    }
    console.log('End');

    console.log(stat_list);
    var mix_stat_res = mix_stat(stat_list[0], stat_list[1]);
    console.log(mix_stat_res);
    var full_post_url = window.location.origin + post_url;
    await $.post(full_post_url, mix_stat_res);

  }

  forLoop();

  
});
