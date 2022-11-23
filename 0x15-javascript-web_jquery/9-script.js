$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=f', function (result) {
    $('DIV#hello').text(result.hello);
  });
});
