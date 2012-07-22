/** Wastesometi.me top-level namespace */
var wst = {}

/** Centralized event routing trick. */
var wst.Events = _.extend({}, Backbone.Events);

/** Represents an article. */
var wst.Article = Backbone.Model.extend({
    
});

/** Represents a video. */
var wst.Video = Backbone.Model.extend({
});

/** Represents a collection of articles. */
var wst.ArticleCollection = Backbone.Collection.extend({
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
var wst.VideoCollection = Backbone.Collection.extend({
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
var wst.Timer = Backbone.Model.extend({
});

/** Represents a timer view. */
var wst.TimerView = Backbone.Model.extend({
});

/** App container. */
var wst.App = Backbone.View.extend({
    initialize: function() {
        
    }
})