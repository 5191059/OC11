window.onload = function() {
    var tmp = document.getElementsByClassName("info");
    var tmp2 = document.getElementsByName("button");
    var tmp3 = document.getElementsByClassName('card');
    var moji = "coolerID";

    for(var i=0;i<=tmp.length-1;i++){
        //id追加
        tmp[i].setAttribute("id",moji+i);
        tmp2[i].setAttribute("id", i);
        tmp3[i].setAttribute("id","img" + i)
    }
    height_repair();
};

function height_repair(){
  var tmp = document.getElementsByClassName("button");
  var tmp2 = document.getElementsByClassName("button hidden");

  $('#background').css({
    "height": 450 + 147.5 * (tmp.length - tmp2.length)
  })
};

function addPro(id_value){

    var text = document.getElementById('coolerID' + id_value);
    var image = document.getElementById('img' + id_value);
    var name = text.getElementsByTagName('h1').item(0).innerText;
    var src = image.getElementsByTagName('img').item(0).src;
    var price = text.getElementsByTagName('h3').item(0).innerText;

    var cooler_price = parent.document.getElementById("cooler_price");
    cooler_price.innerText = price;

    var Name = parent.document.getElementById('cooler_txt');
    Name.innerText = name;

    var Src = parent.document.getElementById('cooler_img');
    Src.src = src ;

    parent.calc_sum();

    parent.closeModal();
}

$(function () {
    searchWord = function(){
      var   search_socketText = $('#cooler_socket_value').val(),
            search_heightText = $('#cooler_height_value').val(),
            search_low_price = $('#cooler_low_price').val(),
            search_high_price = $('#cooler_high_price').val(),
            targetText,
            targetPrice;
      search_low_price = parseInt(search_low_price, 10);
      search_high_price = parseInt(search_high_price, 10);
            
            
      $('.price').each(function(element){
        targetPrice = parseInt($(this).text().replace('¥', ''), 10);
        
        if (isNaN(search_low_price) == false){
          if (isNaN(search_high_price) == false){
            if (targetPrice >= search_low_price && targetPrice <= search_high_price) {
              $(this).parent().parent().parent().removeClass('hidden');
            } else {
              $(this).parent().parent().parent().addClass('hidden');
            }
          } else {
            if (targetPrice >= search_low_price){
              $(this).parent().parent().parent().removeClass('hidden');
            } else {
              $(this).parent().parent().parent().addClass('hidden');
            }
          }
        } else if (isNaN(search_high_price) == false) {
          if (targetPrice <= search_high_price){
            $(this).parent().parent().parent().removeClass('hidden');
          } else {
            $(this).parent().parent().parent().addClass('hidden');
          }
        } else {
          $(this).parent().parent().parent().removeClass('hidden');
        };

      });
      $('.card').each(function(element){
        targetText = $(this).text();

        // 検索対象となるリストに入力された文字列が存在するかどうかを判断
        if (targetText.indexOf(search_socketText) != -1) {
          if (targetText.indexOf(search_heightText) != -1) {
            ; //  何もしない
          } else {
            $(this).parent().addClass('hidden');
          }
        } else {
          $(this).parent().addClass('hidden');
        }
      });
      height_repair();
    };
    // searchWordの実行
    $('#Search1').on('change', searchWord);
    $('#Search2').on('change', searchWord);
});
