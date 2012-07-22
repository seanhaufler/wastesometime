var ToolBarView = Backbone.View.extend({
    el: 'body',
    initialize: function(opts) {
        this.html = _.template($('#toolbar-template').html());
        this.url = opts.url;
        //this.collection = opts.collection;
        this.render();
    },
    render: function() {
        $('#container').hide()
        $(this.html({url: this.url})).appendTo(this.$el);
    }
});