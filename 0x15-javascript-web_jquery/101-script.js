// A script that  adds, removes and clears LI elements from a list when the user clicks on specific events.

$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    const $list = $('ul.my_list');
    const $lastItem = $list.children('li:last');
    $lastItem.remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
