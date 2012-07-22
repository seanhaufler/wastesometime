/** Wastesometi.me top-level namespace */
var wst = {}

/** Centralized event routing trick. */
wst.Events = _.extend({}, Backbone.Events);

/** Represents an article. */
wst.Article = Backbone.Model.extend({
    
});

/** Represents a video. */
wst.Video = Backbone.Model.extend({
});

/** Represents a collection of articles. */
wst.ArticleCollection = Backbone.Collection.extend({
    initialize: function(models, opts) {
        this.queryParams = {}
        this.queryParams.minLen = opts.minLen;
        this.queryParams.maxLen = opts.maxLen;
    },
    model: wst.Article,
    url: function() {
        return '/articles/?' + $.params(this.queryParams, true);
    }
});

/** Represents a collection of videos. */
wst.VideoCollection = Backbone.Collection.extend({
    initialize: function(models, opts) {
        this.queryParams = {}
        this.queryParams.minTime = opts.minTime;
        this.queryParams.maxTime = opts.maxTime;
    },
    model: wst.Video,
    url: function() {
        return '/videos/?' + $.params(this.queryParams, true);
    } 
});

/** Represents the underlying timer. */
wst.Timer = Backbone.Model.extend({
});

/** Represents a timer view. */
wst.TimerView = Backbone.Model.extend({
});

/** App container. */
wst.App = Backbone.View.extend({

    initialize: function() {
        var that = this;
        // jQuery
        this.$timeSubmit = $('#timeSubmit');
        this.$timeInput = $('#timeInput');

        this.$timeSubmit.click(function() {
            var time = parseInt(that.$timeInput.val());
            console.log(time);
        });
    }
})