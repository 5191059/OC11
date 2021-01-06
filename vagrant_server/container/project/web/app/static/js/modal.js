//modal
$(function(){
    for(var i=1; i<11; i++){
        //ボタンをクリックしたら
        $("#btn" + ( "00" + i ).slice( -2 )).click(function(){
            //body内の最後に<div id="modal-bg"></div>を挿入
            $("body").append('<div id="modal-bg"></div>');
    
            //画面中央を計算する関数を実行
            modalResize();
    
            //モーダルウィンドウを表示
            $("#modal-bg,#modal-main").fadeIn("slow");
    
            //画面のどこかをクリックしたらモーダルを閉じる
            $("#modal-bg,#modal").click(function(){
                $("#modal,#modal-bg").fadeOut("slow",function(){
                    //挿入した<div id="modal-bg"></div>を削除
                    $('#modal-bg').remove();
                    $('#body').css({
                        "position": "relative",
                        "overflow": "visible"
                    })
                });
    
            });
    
            //画面の左上からmodal-mainの横幅・高さを引き、その値を2で割ると画面中央の位置が計算できます
            $(window).resize(modalResize);
            function modalResize(){
        
                var w = $(window).width();
                var h = $(window).height();
        
                var cw = $("#modal").outerWidth();
                var ch = $("#modal").outerHeight();
        
                //取得した値をcssに追加する
                $("#modal").css({
                    "left": ((w - cw)/2) + "px",
                    "top": ((h - ch)/2) + "px"
                });
            }
        });
    }
});