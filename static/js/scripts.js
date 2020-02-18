$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);


    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var user_id  = submit_btn.data("user_name");
        console.log(product_id );
        console.log(user_id);

        var data = {};
        data.product_id = product_id;
        data.user_id = user_id;
         var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

         var url = form.attr("action");

        console.log(data)
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 alert('Заявка на участие отправлена')


             },
             error: function(){
                 console.log("error")
             }
         })







    });


    var form = $('#buying_doc');
    console.log(form);

    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var submit_btn = $('#submit_btn_doc');
        var product_id =  submit_btn.data("product_id");
        var user_id  = submit_btn.data("user_name");
        console.log(product_id );
        console.log(user_id);

        var data = {};
        data.product_id = product_id;
        data.user_id = user_id;
         var csrf_token = $('#buying_doc [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

         var url = form.attr("action");

        console.log(data)
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 alert('Заявка на участие отправлена')


             },
             error: function(){
                 console.log("error")
             }
         })







    });















});