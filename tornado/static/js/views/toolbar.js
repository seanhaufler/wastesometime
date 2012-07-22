var ToolBarView = Backbone.View.extend({
    el: 'body',
    initialize: function(opts) {
        this.html = _.template($('#toolbar-template').html());
        this.url = opts.url;
        this.totalTime = opts.time
        //this.collection = opts.collection;
        this.render();
        this.$countdown = $('#countdown');
        this.setTimeAmount(this.totalTime);
        var self = this;
        setInterval(function() {
            if (self.totalTime <= 0) {
                // put whatever you want here.
                alert("YOU ARE OUT OF TIME!!!");
            } else {
                self.totalTime = self.totalTime - 1;
                self.setTimeAmount(self.totalTime);
            }
        }, 1000 * 60);
        this.decorate();
    },
    decorate: function() {
      this.boredButton = $('#boredImage');
      var self = this;
      console.log('bored');
      console.log(this.boredButton);
      this.boredButton.click(function() {
        console.log('click');
        var bucket = new Bucket(false, self.totalTime);
        bucket.fetch({ success: function() {
        new SelectionPageView({ content: bucket });
        }
      });

      });
    },
    render: function() {
        $('#container').hide();
        console.log(this.url);
        this.$el.css('padding', '0px');
        this.$el.css('width', '100%');
        this.$el.css('height', '100%');
        console.log(this.$el);
        console.log(this.$el.css('padding'));
        this.$el.empty();
        $(this.html({url: this.url})).appendTo(this.$el);
    },
    setTimeAmount: function(amt) {
        if (amt === 1) {
            this.$countdown.text("1 minute left");
        } else {
            this.$countdown.text(amt + " minutes left");
        }
    },
 });
