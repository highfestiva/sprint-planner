$(function () {
  var isMouseDown = false,
      isFree = false,
      isWorking;
  $("#ppl_dates_table td")
    .mousedown(function () {
      isMouseDown = true;
      $(this).toggleClass("working");
      isFree = $(this).hasClass("free");
      isWorking = $(this).hasClass("working");
      return false;
    })
    .mouseover(function () {
      if (isMouseDown) {
        if (isFree || !$(this).hasClass("free")) {
          $(this).toggleClass("working", isWorking);
        }
      }
    });

  $(document)
    .mouseup(function () {
      isMouseDown = false;
    });

  // click date column
  $("#ppl_dates_table th.col")
    .mousedown(function () {
      var index = $(this).index() + 1;
      $(this).toggleClass("free");
      var setFree = $(this).hasClass("free");
      $("#ppl_dates_table td:nth-child("+index+")").toggleClass("free", setFree);
    });
});
