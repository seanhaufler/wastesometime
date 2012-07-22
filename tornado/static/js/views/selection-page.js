var SelectionPageView = Backbone.View.extend({

  el: 'body',
  initialize: function(options) {
    this.template = _.template($('#fuck-this-template').html());
    this.options = options;
    this.minutes = parseInt(options.content.maxTime/60);
    this.render();
    this.decorate();
  },

  decorate: function() {
    var self = this;
    $('.content-list').click(function() {
      var node = $(this);
      var url = node.find('.url').text();
      self.toolbar = new ToolBarView({
        url: url,
        time: self.minutes
      });
    });
  },

  getHostname: function(str) {
    var re = new RegExp('^(?:f|ht)tp(?:s)?\://([^/]+)', 'im');
    return str.match(re)[1].toString().split('.')[1] //[1].toString();
  },

  render: function() {
    $('#container').hide();
    var self = this;
    if (this.options.content.length > 0) {
      var listObj = {
        list: this.options.content.map(function (model) {
          return {
            url: model.get('url'),
            iconUrl: model.get('iconUrl'),
            title: model.get('title')
          }
        }),
        minutes: this.minutes
      };
      console.log(listObj);

      $(this.template(listObj)).appendTo(this.$el).hide().fadeIn(800);
      }
  }
});
