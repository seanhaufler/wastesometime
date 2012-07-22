$(function() {
  var scrollBar = $('#scrollBar');
  scrollBar.slider({ value: 100,
    min: 0,
    max: 500,
    step: 2,
    slide: function(event, ui) {
      $('#innerScroll').css('width', ui.value/5 + '%');
      $('#timeCounter .number').text( parseInt(ui.value/5*.6) );
      if (parseInt(ui.value/5) === 1) {
        $('#timeCounter .plural').text(' minute');
      } else {
        $('#timeCounter .plural').text(' minutes');
      }
      var degrees = parseInt(ui.value/5*.6*6);
      $('#rotator').css({
          "-webkit-transform": "rotate(" + degrees + "deg)",
            "-moz-transform": "rotate(" + degrees + "deg)",
              "transform": "rotate(" + degrees + "deg)"
      });
    }});
});
