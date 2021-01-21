window.onload = function() {
  var tmp = document.getElementsByClassName("info");
  var tmp2 = document.getElementsByClassName("hex");
  var tmp3 = document.getElementsByClassName('select_box');
  var tmp4 = document.getElementsByClassName('card');
  var tmp5 = document.getElementsByClassName('display_selectedItem');
  var moji = "fanID";
  
  for(var i=0;i<=tmp.length-1;i++){
      //id追加
      tmp[i].setAttribute("id",moji+i);
      tmp2[i].setAttribute("id",'hex' + i);
      tmp3[i].setAttribute("id","price" + i)
      tmp4[i].setAttribute("id", i)
      tmp5[i].setAttribute("id", i)
  }
    height_repair();
};
  
function height_repair(){
    var tmp = document.getElementsByClassName("card");
    var tmp2 = document.getElementsByClassName("card hidden");
  
    $('#background').css({
      "height": 820 + 510 * Math.ceil((tmp.length - tmp2.length) / 4)
    })
};
  
  
$(function () {
      searchWord = function(){
        var   search_sizeText = $('#fan_size_value').val(),
              search_low_price = $('#fan_low_price').val(),
              search_high_price = $('#fan_high_price').val(),
              targetText,
              targetPrice;
        search_low_price = parseInt(search_low_price, 10);
        search_high_price = parseInt(search_high_price, 10);
        const words = search_sizeText.split(',');
              
              
        $('.display_selectedItem').each(function(element){
          targetPrice = parseInt($(this).text().replace('¥', ''), 10);
          
          if (isNaN(search_low_price) == false){
            if (isNaN(search_high_price) == false){
              if (targetPrice >= search_low_price && targetPrice <= search_high_price) {
                $(this).parent().parent().removeClass('hidden');
              } else {
                $(this).parent().parent().addClass('hidden');
              }
            } else {
              if (targetPrice >= search_low_price){
                $(this).parent().parent().removeClass('hidden');
              } else {
                $(this).parent().parent().addClass('hidden');
              }
            }
          } else if (isNaN(search_high_price) == false) {
            if (targetPrice <= search_high_price){
              $(this).parent().parent().removeClass('hidden');
            } else {
              $(this).parent().parent().addClass('hidden');
            }
          } else {
            $(this).parent().parent().removeClass('hidden');
          };
        });
  
        $('.card').each(function(element){
          targetText = $(this).text();
  
          // 検索対象となるリストに入力された文字列が存在するかどうかを判断
          if (targetText.indexOf(words[0]) != -1 || targetText.indexOf(words[1]) != -1) {
            ; //  何もしない
          } else {
            $(this).addClass('hidden');
          }
        });
        height_repair();
      };

      searchWord = function(){
        var   search_sizeText = $('#fan_size_value').val(),
              search_low_price = $('#fan_low_price').val(),
              search_high_price = $('#fan_high_price').val(),
              targetText,
              targetPrice;
        search_low_price = parseInt(search_low_price, 10);
        search_high_price = parseInt(search_high_price, 10);
        const words = search_sizeText.split(',');
              
          
        $('.card').each(function(element){
          targetText = $(this).text();
  
          // 検索対象となるリストに入力された文字列が存在するかどうかを判断
          if (targetText.indexOf(words[0]) != -1 || targetText.indexOf(words[1]) != -1) {
            $(this).removeClass('hidden');
          } else {
            $(this).addClass('hidden');
          }
        });      
        $('.display_selectedItem').each(function(element){
          targetPrice = parseInt($(this).text().replace('¥', ''), 10);
          
          if (isNaN(search_low_price) == false){
            if (isNaN(search_high_price) == false){
              if (targetPrice >= search_low_price && targetPrice <= search_high_price) {
                ; //  何もしない
              } else {
                $(this).parent().parent().addClass('hidden');
              }
            } else {
              if (targetPrice >= search_low_price){
                ; //  何もしない
              } else {
                $(this).parent().parent().addClass('hidden');
              }
            }
          } else if (isNaN(search_high_price) == false) {
            if (targetPrice <= search_high_price){
              ; //  何もしない
            } else {
              $(this).parent().parent().addClass('hidden');
            }
          } else {
            ; //  何もしない
          };
        });
        height_repair();
      };
      // searchWordの実行
      $('#Search1').on('change', searchWord);
      $('#Search2').on('change', searchWord2);
});
  