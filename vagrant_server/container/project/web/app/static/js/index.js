var modal = document.getElementById('modal');
var modalBlock = document.getElementById('modalBlock');
var body = document.getElementById('body');

function Ifrm(html) {
    modalBlock.innerHTML = '';

    var ifrm = document.createElement("iframe");
    ifrm.src = html;
    ifrm.width = 1000;
    ifrm.height = 700;
    body.style.position = 'sticky';
    body.style.overflow = 'hidden';

    modalBlock.appendChild(ifrm);
    modal.style.display = 'block';
};

let html_file = [
    "sub/01s",
    "sub/02s",
    "sub/03s",
    "sub/04s",
    "sub/05s",
    "sub/06s",
    "sub/07s",
    "sub/08s",
    "sub/09s",
    "sub/10s"
]

for(let i=1; i<=html_file.length; i++){
    $("#btn"+( "00" + i ).slice( -2 )).on('click', function(){
        Ifrm(html_file[i-1]);
    });
};

function closeModal() {
    body.style.position = 'relative';
    body.style.overflow = 'visible';
    modal.style.display = 'none';
    $('#modal-bg').remove();
}


function calc_sum(){
    var sum = document.getElementById("sum");
    var cpu_price = document.getElementById("cpu_price");
    var cpu_cooler_price = document.getElementById("cooler_price");
    var memory_price = document.getElementById("memory_price");
    var mother_price = document.getElementById("mother_price");
    var ssd_price = document.getElementById("ssd_price");
    var hdd_price = document.getElementById("hdd_price");
    var case_price = document.getElementById("case_price");
    var power_price = document.getElementById("power_price");
    var case_fan_price = document.getElementById("case_fan_price");


    sum.innerText = 0
    let pricelst = [cpu_price, cpu_cooler_price, memory_price,
        mother_price, ssd_price, hdd_price, case_price, power_price, case_fan_price]
    
    for(let i=0; i < pricelst.length; i++){
        if(isNaN(parseInt(pricelst[i].innerText.replace('¥', ''), 10))){
            sum.innerText = parseInt(sum.innerText, 10) + 0
        }
        else{
            sum.innerText = parseInt(sum.innerText, 10) + parseInt(pricelst[i].innerText.replace('¥', ''), 10)
        }
    }
    sum.innerText = '¥' + parseInt(sum.innerText, 10).toLocaleString();
};

// // 値段計算の処理

// var firstchange =  [true, true, true, true, true, true, true, true, true];

// function cpu_price_change(price){
//     firstchange[0] = true;
//     change_cpu_price();
// }

// function cpu_cooler_price_change(price){
//     firstchange[1] = true;
//     change_cpu_cooler_price();
// }

// function memory_price_change(price){
//     firstchange[2] = true;
//     change_memory_price();
// }

// function mother_price_change(price){
//     firstchange[3] = true;
//     change_mother_price();
// }

// function ssd_price_change(price){
//     firstchange[4] = true;
//     change_ssd_price();
// }

// function hdd_price_change(price){
//     firstchange[5] = true;
//     change_hdd_price();
// }

// function case_price_change(price){
//     firstchange[6] = true;
//     change_case_price();
// }

// function power_price_change(price){
//     firstchange[7] = true;
//     change_power_price();
// }

// function case_fan_price_change(price){
//     firstchange[8] = true;
//     change_case_fan_price();
// }

// function change_cpu_price(){
//     var value = document.getElementById("cpu_count").value;
//     var cpu_price = document.getElementById("cpu_price");
//     if(firstchange[0]){
//         price1 = parseInt(cpu_price.innerText, 10)
//         cpu_price.innerText = price1;
//         firstchange[0] = false;
//     }else{
//         cpu_price.innerText = price1 * value;
//     }
//     calc_sum();
// };

// function change_cpu_cooler_price(){
//     var value = document.getElementById("cpu_cooler_count").value;
//     var cpu_cooler_price = document.getElementById("cpu_cooler_price");
//     if(firstchange[1]){
//         price2 = parseInt(cpu_cooler_price.innerText, 10)
//         cpu_cooler_price.innerText = price2;
//         firstchange[1] = false;
//     }else{
//         cpu_cooler_price.innerText = price2 * value;
//     }
//     calc_sum();
// };

// function change_memory_price(){
//     var value = document.getElementById("memory_count").value;
//     var memory_price = document.getElementById("memory_price");
//     console.log(memory_price.innerText);
    
//     if(firstchange[2]){
//         price3 = parseInt(memory_price.innerText, 10)
//         memory_price.innerText = price3;
//         firstchange[2] = false;
//     }else{
//         memory_price.innerText = price3 * value;
//     }
//     calc_sum();
// };

// function change_mother_price(){
//     var value = document.getElementById("mother_count").value;
//     var mother_price = document.getElementById("mother_price");
//     if(firstchange[3]){
//         price4 = parseInt(mother_price.innerText, 10)
//         mother_price.innerText = price4;
//         firstchange[3] = false;
//     }else{
//         mother_price.innerText = price4 * value;
//     }
//     calc_sum();
// };

// function change_ssd_price(){
//     var value = document.getElementById("ssd_count").value;
//     var ssd_price = document.getElementById("ssd_price");
//     if(firstchange[4]){
//         price5 = parseInt(ssd_price.innerText, 10)
//         ssd_price.innerText = price5;
//         firstchange[4] = false;
//     }else{
//         ssd_price.innerText = price5 * value;
//     }
//     calc_sum();
// };

// function change_hdd_price(){
//     var value = document.getElementById("hdd_count").value;
//     var hdd_price = document.getElementById("hdd_price");
//     if(firstchange[5]){
//         price6 = parseInt(hdd_price.innerText, 10)
//         hdd_price.innerText = price6;
//         firstchange[5] = false;
//     }else{
//         hdd_price.innerText = price6 * value;
//     }
//     calc_sum();
// };


// function change_case_price(){
//     var value = document.getElementById("case_count").value;
//     var case_price = document.getElementById("case_price");
//     if(firstchange[6]){
//         price7 = parseInt(case_price.innerText, 10)
//         case_price.innerText = price7;
//         firstchange[6] = false;
//     }else{
//         case_price.innerText = price7 * value;
//     }
//     calc_sum();
// };

// function change_power_price(){
//     var value = document.getElementById("power_count").value;
//     var power_price = document.getElementById("power_price");
//     if(firstchange[7]){
//         price8 = parseInt(power_price.innerText, 10)
//         power_price.innerText = price8;
//         firstchange[7] = false;
//     }else{
//         power_price.innerText = price8 * value;
//     }
//     calc_sum();
// };

// function change_case_fan_price(){
//     var value = document.getElementById("case_fan_count").value;
//     var case_fan_price = document.getElementById("case_fan_price");
//     if(firstchange[8]){
//         price9 = parseInt(case_fan_price.innerText, 10)
//         case_fan_price.innerText = price9;
//         firstchange[8] = false;
//     }else{
//         case_fan_price.innerText = price9 * value;
//     }
//     calc_sum();
// };
