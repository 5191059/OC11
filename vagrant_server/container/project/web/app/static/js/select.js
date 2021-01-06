$(function(){
  var selectBox = $("ul.select_box")
  var selectItems = $("ul.select_box li")
  var display = $(".display_selectedItem");

  display.on("click",function(){
      selectBox.show();
  });

  selectItems.on("click",function(){
      selectItems.removeClass("selected").css("background","#fff");
      $(this).addClass("selected").css("background","#f8f8f8");
      selectedImage = $(this).children('img').attr('src');
      
      selectedItem = $("li.selected").text();
      
      $(".display_selectedItem .selected_img").attr('src', selectedImage);
      
      selectBox.hide();
      display.html('<img class="selected_img" src='+ selectedImage +'>' + selectedItem);
  })
});
