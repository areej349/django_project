function addcart()
{
    $.ajax({
            url:'/addtocart/',
            type:'get',

            success:function(result){
                console.log(result.cart_count)
                $('.cart-count').text(result.cart_count)

                Swal.fire({
                    title: 'نجاح!',
                    text: 'تمت الإضافة إلى السلة بنجاح',
                    icon: 'success',
                    timer: 2000, // يختفي تلقائيًا بعد 2 ثانية
                    timerProgressBar: true
                });
            }

    });
}   

