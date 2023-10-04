// A script that updates text of <header> elem to New Header!!! when user clicks on DIV#update_header.

$('div#update_header').click(function () {
  $('header').text('New Header!!!');
});
