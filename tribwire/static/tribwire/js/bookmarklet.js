//(function (){

  var v = "1.7.2";

  if (window.jQuery === undefined || window.jQuery.fn.jquery < v) {
    var done = false;
    var script = document.createElement("script");
    script.src = "//ajax.googleapis.com/ajax/libs/jquery/" + v + "/jquery.min.js";
    script.onload = script.onreadystatechange = function(){
      if (!done && (!this.readyState || this.readyState == "loaded" || this.readyState == "complete")) {
        done = true;
        initMyBookmarklet();
      }
    };
    document.getElementsByTagName("head")[0].appendChild(script);
  } else {
    initMyBookmarklet();
  }


  function initMyBookmarklet(){
    var 
        method = {},
        $modal,
        $overlay,
        $content,
        $close;

    // Horizontally center the modal in the viewport
    method.center = function () {
      var top, left;

      top = Math.max($modal.outerHeight() - $(window).height(), 0);
      left = Math.max($(window).width() - $modal.outerWidth(), 0) / 2;

      $modal.css({
        top:top + $(window).scrollTop(), 
        left:left + $(window).scrollLeft()
      });
    };


    method.open = function (settings) {
      $content.empty().append(settings.content);

      $modal.css({
          width: settings.width || 'auto', 
          height: settings.height || 'auto'
      });

      method.center();
      $(window).bind('resize.modal', method.center);
      $modal.show();
      $overlay.show();
    };

    // Close the modal
    method.close = function () {
      $modal.hide();
      $overlay.hide();
      $content.empty();
      $(window).unbind('resize.modal');
    };

    function generateModal() {

      // Generate the HTML and add it to the document
      $overlay = $('<div id="overlay"></div>');
      $modal = $('<div id="modal"></div>');
      $content = $('<div id="content"></div>');
      $close = $('<a id="close" href="#">close</a>');

      $modal.hide();
      $overlay.hide();
      $modal.append($content, $close);

      $close.click(function(e){
        e.preventDefault();
        method.close();
      });
      return $modal;
    }

    $modal = generateModal();
    $('body').append($overlay, $modal);                       
    // Wait until the DOM has loaded before querying the document
    $.get('new_wire.html', function(data){
      method.open({content: data});
      $modal.find('form').on('submit', function (e) {
        e.preventDefault();
        var $form = $(this);
        $.ajax({
          type: 'POST',
          url: $form.attr('action'),
          crossDomain: true,
          data: $form.serialize(),
          dataType: 'json'
        })
      });
    });
  }

//})();