function send_text(){
    var text1 = 'hogehoge'
    var text2 = 'fugafuga'

    // FormData初期化
    var fData = new FormData();

    fData.append('text1', text1);
    fData.append('text2', text2);

    // ajax送信
    $.ajax({
        //配信元のhttpsサーバーに返す場合
        url: '/register',                            
        //別サーバー（今回でいう画像処理サーバー）に返す場合
        //url: 'https://192.168.0.100:12345/register',   
        type: 'POST',
        data: fData ,
        contentType: false,
        processData: false,
        success: function(data, dataType) {
            //非同期で通信成功時に読み出される [200 OK 時]
            console.log('Success', data);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            //非同期で通信失敗時に読み出される
            console.log('Error : ' + errorThrown);
        }
    });
}