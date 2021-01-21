function change_money(id_value){
  var selectBox = $("#price"+ id_value)
  var selectItems = $("#price"+ id_value + " li")
  var display = $("#" + id_value + " .display_selectedItem");

  $("ul.select_box").hide();
  selectBox.show();

  selectItems.on("click",function(){
    selectItems.removeClass("selected").css("background","#fff");
    $(this).addClass("selected").css("background","#f8f8f8");
    selectedImage = $(this).children('img').attr('src');
    console.log(selectedImage);
    // next_link = change_link(selectedImage);
      
    selectedItem = $(this).text();
      
    $("img"+ id_value +".display_selectedItem .selected_img").attr('src', selectedImage);
      
    selectBox.hide();
    display.html('<img class="selected_img" src='+ selectedImage +'>' + selectedItem);
  })
};

function change_link(src){
  if (src.indexOf('d.png') == 0) {
    return 'url[0]'
  } else if (src.indexOf('a.png') == 0) {
    return 'url[1]'
  } else if (src.indexOf('k.png') == 0) {
    return 'url[2]'
  } else if (src.indexOf('s.png') == 0){
    return 'url[3]'
  };
};