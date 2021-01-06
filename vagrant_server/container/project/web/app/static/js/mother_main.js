window.onload = function() {
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
      var   search_socketText = $('#mother_socket_value').val(),
            search_tipsetText = $('#mother_TipSet_value').val(),
            search_factorText = $('#mother_form_factor_value').val(),
            search_low_price = $('#mother_low_price').val(),
            search_high_price = $('#mother_high_price').val(),
            targetText,
            targetPrice;
      search_low_price = parseInt(search_low_price, 10);
      search_high_price = parseInt(search_high_price, 10);
      const words = search_socketText.split(',');
            
            
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
        if (targetText.indexOf(search_socketText) != -1 || targetText.indexOf(words[0]) != -1 || targetText.indexOf(words[1]) != -1) {
          if (targetText.indexOf(search_tipsetText) != -1) {
            if (targetText.indexOf(search_factorText) != -1) {
                  ; //  何もしない
            } else {
              $(this).addClass('hidden');
            }
          } else {
            $(this).addClass('hidden');
          }
        } else {
          $(this).addClass('hidden');
        }
      });
      height_repair();
    };

    searchWord2 = function(){
      var   search_socketText = $('#mother_socket_value').val(),
            search_tipsetText = $('#mother_TipSet_value').val(),
            search_factorText = $('#mother_form_factor_value').val(),
            search_low_price = $('#mother_low_price').val(),
            search_high_price = $('#mother_high_price').val(),
            targetText,
            targetPrice;
      search_low_price = parseInt(search_low_price, 10);
      search_high_price = parseInt(search_high_price, 10);
      const words = search_socketText.split(',');
            
      $('.card').each(function(element){
        targetText = $(this).text();

        // 検索対象となるリストに入力された文字列が存在するかどうかを判断
        if (targetText.indexOf(search_socketText) != -1 || targetText.indexOf(words[0]) != -1 || targetText.indexOf(words[1]) != -1) {
          if (targetText.indexOf(search_tipsetText) != -1) {
            if (targetText.indexOf(search_factorText) != -1) {
              $(this).removeClass('hidden');
            } else {
              $(this).addClass('hidden');
            }
          } else {
            $(this).addClass('hidden');
          }
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
    $('#Search3').on('change', searchWord2);
});
