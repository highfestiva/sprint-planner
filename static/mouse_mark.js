$(function () {
  var isMouseDown = false,
      isFree = false,
      isWorking;
  $(".ppl_dates_table td")
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
  $("th.col")
    .mousedown(function () {
      var setFree = !$(this).hasClass("free");
      var index = $(this).index() + 1;
      $("th:nth-child("+index+")").toggleClass("free", setFree);
      $("td:nth-child("+index+")").toggleClass("free", setFree);
    });
});
