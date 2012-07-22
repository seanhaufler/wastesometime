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
        return '/articles/?' + $.param(this.queryParams, true);
    },
    getRandom: function() {
        return this.at(Math.floor(Math.random()*this.length));
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
        return '/videos/?' + $.param(this.queryParams, true);
    } 
});

/** Represents the underlying timer. */
wst.Timer = Backbone.Model.extend({
});

/** Represents a timer view. */
wst.TimerView = Backbone.Model.extend({
});

wst.TimeInputView = Backbone.View.extend({
    el: '#input',
    initialize: function() {
        var that = this;
        // jQuery
        this.$timeSubmit = $('#timeSubmit');
        this.$timeInput = $('#timeInput');
        
        this.$timeSubmit.click(function() {
            var time = parseInt(that.$timeInput.val());
            wst.Events.trigger("app:timeChosen", time)
        });
    },
    show: function() {
        this.$el.show();
    },
    hide: function(millis) {
        this.$el.hide(millis || 0);
    }
});
wst.PickerView = Backbone.Model.extend({
    el: '#picker',
    initialize: function (opts) {
    }
});
wst.Picker
/** App container. */
wst.App = Backbone.View.extend({

    initialize: function() {
        this.timeInput = new wst.TimeInputView();
        
        // Events
        wst.Events.on("app:timeChosen", this.loadChoices, this);
    },
    loadChoices: function(time) {
        console.log(time)
        this.timeInput.hide(1000);
//        this.articles = new wsc.ArticleCollection(false, {
    }
});