var SelectionPageView = Backbone.View.extend({

  el: 'body',
  initialize: function(options) {
    this.template = _.template($('#fuck-this-template').html());
    this.options = options;
    this.minutes = options.content.maxTime;
    this.render();
  },

  getHostname: function(str) {
    return (str.match(/:\/\/(.[^/]+)/)[1]).replace('www.','');
  }

  render: function() {
    $('#container').hide();
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
