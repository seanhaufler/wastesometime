
var HomePage = Backbone.View.extend({

  events: {
    "click .button": "transition"
  },

  initialize: function() {
    this.innerScroll = $('#innerScroll', this.el);
    this.scrollBar = $('#scrollBar', this.el);
    this.number = $('#timeCounter .number', this.el);
    this.plural = $('#timeCounter .plural', this.el);
    var self = this;
    this.scrollBar.slider({ value: 100,
      min: 0,
      max: 500,
      step: 2,
      slide: function(event, ui) {
        self.minutes = parseInt(ui.value/5* .6);
        self.innerScroll.css('width', ui.value/5 + '%');
        self.number.text( self.minutes );
        var degrees = parseInt(ui.value/5*.6*6);
        $('#hourRotator').css({
            "-webkit-transform": "rotate(" + degrees/12 + "deg)",
              "-moz-transform": "rotate(" + degrees/12 + "deg)",
                "transform": "rotate(" + degrees/12 + "deg)"
        });
        $('#minuteRotator').css({
            "-webkit-transform": "rotate(" + degrees + "deg)",
              "-moz-transform": "rotate(" + degrees + "deg)",
                "transform": "rotate(" + degrees + "deg)"
        });
      }});

  },

  animateHomePage: function() {
    var self = this;
    $('#container').animate({
      top: '-=1000'
    }, 2000, function() {
      self.generateToolbar();
    });
  },

  generateToolbar: function() {
    var url = 'http://techcrunch.com';
    this.toolbar = new ToolBarView({url: url});


  },

  pluralize: function() {
    if (this.minutes === 1) {
      this.plural.text(' minute');
    } else {
      this.plural.text(' minutes');
    }
  },

  transition: function() {
    console.log('asdfasdfasd');
    this.animateHomePage();

  }
}, {
  getInstance: function() {
    if (this.instance_) return this.instance_;
    this.instance_ = new HomePage({
      el: '#container'
    });
    return this.instance;
  }
});

var Content = Backbone.Model.extend({
    initialize: function() {
        if (this.set('duration')) {
            this.set('type', 'video');
        } else {
            this.set('type', 'article');
        }
    }
});

var Bucket = Backbone.Collection.extend({
    initialize: function(models, opts) {
        this.maxTime = opts.maxTime;
    },
    url: function() {
        return '/search/?maxTime=' + this.maxTime;
    }
});