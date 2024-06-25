odoo.define('pasar.pendaftaran', function(require)    
{
 "use strict";
  $(document).ready(function() {
  $(function(){
  //your js or jquery script , for instance :
 
  });
});


})
function filter_kota(){
  alert($('#ktp_kota_id').val());
  // alert(i);
}
function changeKecamatan(a){
    var keyword = document.getElementById("ktp_kecamatan_id").value;
    var desa = document.getElementById("ktp_desa_id");
    $('#ktp_desa_id').prop('selectedIndex', 0);
    for (var i = 0; i < desa.length; i++) {
        var parent_desa = desa.options[i].getAttribute("data_parent");
        if (parent_desa == keyword) {
            $(desa.options[i]).removeAttr('disabled').show();
        }
        else {
            $(desa.options[i]).attr('disabled', 'disabled').hide();
        }
    }

}
function changeKecamatan2(a){
    var keyword = document.getElementById("tg_kecamatan_id").value;
    var desa = document.getElementById("tg_desa_id");
    $('#tg_desa_id').prop('selectedIndex', 0);
    for (var i = 0; i < desa.length; i++) {
        var parent_desa = desa.options[i].getAttribute("data_parent");
        if (parent_desa == keyword) {
            $(desa.options[i]).removeAttr('disabled').show();
        }
        else {
            $(desa.options[i]).attr('disabled', 'disabled').hide();
        }
    }

}
function changeFunc(i) {
  // console.log('sas');
  // var selectBox = document.getElementById("sesuai");
  // var selectedValue = selectBox.options[selectBox.selectedIndex].value;
  // alert(i);
  if(i.value==0){
    // document.getElementById('div').style.display = "block";
    document.getElementById('tg_street').value = "";
    document.getElementById('tg_street').readOnly = false;
//    document.getElementById('tg_street2').value = "";
//    document.getElementById('tg_street2').readOnly = false;
//    document.getElementById('tg_propinsi_id').value = "";
//    document.getElementById('tg_propinsi_id').removeAttribute("disabled");
//    document.getElementById('tg_kota_id').value = "";
//    document.getElementById('tg_kota_id').removeAttribute("disabled");
//    document.getElementById('tg_kecamatan_id').value = "";
//    document.getElementById('tg_kecamatan_id').removeAttribute("disabled");
//    document.getElementById('tg_desa_id').value = "";
//    document.getElementById('tg_desa_id').readOnly = false;
  } else{
    // document.getElementById('div').style.display = "none";
    document.getElementById("tg_street").value = document.getElementById("ktp_alamat").value;
    document.getElementById("tg_street").readOnly= true;
//    document.getElementById("tg_street2").value = document.getElementById("ktp_rt_rw").value;
//    document.getElementById('tg_street2').readOnly = true;
//    document.getElementById("tg_propinsi_id").value = document.getElementById("ktp_propinsi_id").value;
//    document.getElementById('tg_propinsi_id').setAttribute("disabled", "disabled");
//    document.getElementById("tg_kota_id").value = document.getElementById("ktp_kota_id").value;
//    document.getElementById('tg_kota_id').setAttribute("disabled", "disabled");
//    document.getElementById("tg_kecamatan_id").value = document.getElementById("ktp_kecamatan_id").value;
//    document.getElementById('tg_kecamatan_id').setAttribute("disabled", "disabled");
//    document.getElementById("tg_desa_id").value = document.getElementById("ktp_desa_id").value;
//    document.getElementById('tg_desa_id').setAttribute("disabled", "disabled");

   }
 }