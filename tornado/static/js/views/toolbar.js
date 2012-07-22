var ToolBarView = Backbone.View.extend({
    el: 'body',
    initialize: function(opts) {
        this.html = _.template($('#toolbar-template').html());
        this.url = opts.url;
        //this.collection = opts.collection;
        this.render();
    },
    render: function() {
        $('#container').hide();
        console.log(this.url);
        this.$el.css('padding', '0px');
        this.$el.css('width', '100%');
        this.$el.css('height', '100%');
        console.log(this.$el);
        console.log(this.$el.css('padding'));
        $(this.html({url: this.url})).appendTo(this.$el);
    }
});