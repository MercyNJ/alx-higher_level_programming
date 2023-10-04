// A script that adds the class red to the <header> elem when use clicks on tag DIV#red_header.

$('div#red_header').click(function () {
  $('header').addClass('red');
});
