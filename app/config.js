http = require('http');

var config = {
  endpoints: {
    VIDEOS: '/videos.json?',
    ARTICLES: '/articles.json?'
  },
  base: 'http://wastesometi.me'
}

var rest = {
  /**
   * @param min {number}
   * @param max {number}
   */
  queryVideos: function(min, max) {
    var options = {
      host: config.base,
      port: 80,
      path: this.buildUrl(min, max, config.endpoints.VIDEOS),
      method: 'GET'
    };
    this.sendRequest(options);
  },

  /**
   * @param min {number}
   * @param max {number}
   */
  queryArticles: function(min, max) {
    var options = {
      host: config.base,
      port: 80,
      path: this.buildUrl(min, max, config.endpoints.ARTICLES),
      method: 'GET'
    };
    this.sendRequest(options);
  },

  /**
   * @param min {number}
   * @param max {number}
   * @param endpoint {string}
   */
  buildUrl: function(min, max, endpoint) {
    return endpoint + 'min=' + min + '&max=' + max;
  },

  sendRequest: function(options) {
    var req = http.request(options, function(res) {
      console.log('STATUS: ' + res.statusCode);
      console.log('HEADERS: ' + JSON.stringify(res.headers));
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
        console.log('BODY: ' + chunk);
        return chunk;
      });
    }).end();
    return; // undefined on error
  }
}

module.exports = rest;
