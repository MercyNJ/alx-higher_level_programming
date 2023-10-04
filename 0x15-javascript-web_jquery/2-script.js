// A script that updates the text color of the <header> element to red.
// When user clicks on tag div.

$(document).ready(function () {
  $('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
