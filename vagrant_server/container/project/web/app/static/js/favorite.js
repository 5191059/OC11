function favorite(id_value, name, user_id){
    var tmp6 = document.getElementsByClassName('triangle2');
  
    for(var i=0;i<=tmp6.length-1;i++){
        //id追加
        tmp6[i].setAttribute("id", i)
    }
    console.log(id_value, name, user_id);
    
    var selectproductImg = document.getElementById("hex" + id_value);
    var selectproduct = document.getElementById(name + id_value);
    console.log(selectproduct);
    console.log(selectproductImg);
    
    var Product_name = selectproduct.getElementsByTagName('h1').item(0).innerText;
    var Product_src = selectproductImg.getElementsByTagName('img').item(0).src;
    
    var fData = new FormData();
    
    fData.append('Product_name', Product_name);
    fData.append('Product_src', Product_src);
    fData.append('User_id', user_id);
    
        
    $.ajax({
        //配信元のhttpsサーバーに返す場合
        url: '/push',                       
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

    console.log(Product_name);
    console.log(Product_src);
    
  };