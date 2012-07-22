
var HomePage = Backbone.View.extend({

  events: {
    "click .button": "transition"
  },

  initialize: function() {
    this.innerScroll = $('#innerScroll', this.el);
    this.scrollBar = $('#scrollBar', this.el);
    this.number = $('#timeCounter .number', this.el);
    this.plural = $('#timeCounter .plural', this.el);
    this.minutes = 20;
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
      self.generateSelectionPageView();
    });
  },

  generateToolbar: function() {
    var url = 'http://techcrunch.com';
    this.toolbar = new ToolBarView({url: url});
  },

  generateSelectionPageView: function() {
    this.selectionPage = new SelectionPageView({ content: this.content });
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
    var self = this;
    this.content = new Bucket(false, { maxTime: this.minutes });
    this.content.fetch({ success: function() {
      self.animateHomePage();
    }});
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
      console.log(this);
        if (this.set('duration')) {
            this.set('type', 'video');
            this.set('iconUrl', '/static/images/video_icon.png');
            this.set('url', this.get('links'));
        } else {
            this.set('type', 'article');
            this.set('iconUrl', '/static/images/article_icon.png');
        }
    }
});

var Bucket = Backbone.Collection.extend({
    initialize: function(models, opts) {
      this.maxTime = opts.maxTime;
    },
    model: Content,
    url: function() {
        return '/search/?maxTime=' + this.maxTime;
    }
});
