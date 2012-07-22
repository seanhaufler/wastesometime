
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , less = require('less')
  , lessMiddleware = require('less-middleware')
  , http = require('http')
  , config = require('./app/config.js')
  , underscore = require('underscore')._
  , backbone = require('backbone')
  , $ = require('jquery');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(lessMiddleware({
    src: __dirname + '/public',
    compress: true
  }));
  app.use(app.router);
  app.use(express.static(__dirname + '/public'));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);

// Test to ensure endpoint works
console.log(config.queryVideos(0,1000));

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
