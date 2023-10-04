// A script that fetches from given url & displays value of hello from that fetch in the HTML tag DIV#hello.

$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
