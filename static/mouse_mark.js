function calcManDays(startIndex, endIndex) {
  return [0, 2, 12];
}


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

  // check sprint start
  $(".sprint_start_dates_table input[type=checkbox]").change(function() {
      var starts = [0];
      $(".sprint_start_dates_table input[type=checkbox]").each(function () {
          if (this.checked) {
            var dayIndex = $(this).parent().index() - 1;
            if (dayIndex > 0) {
              starts.push(dayIndex);
            }
          }
        });
      var html = "";
      var prevIndex = 0;
      for (var j = 0; j < starts.length; ++j) {
        dayIndex = starts[j];
        if (dayIndex <= 0) {
          continue;
        }
        html += '<div class="availability"><h3>Sprint ' + j + '</h3>';
        teamManDays = calcManDays(prevIndex, dayIndex);
        for (var i = 0; i < teamManDays.length; ++i) {
          var manDays = teamManDays[i];
          html += "<p>Team " + (i+1) + ": " + manDays + " man-days</p>"
        }
        html += "</div>";
        prevIndex = dayIndex;
      }
      $(".calc").html(html);
    });
});
