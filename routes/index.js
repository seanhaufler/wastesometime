
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index',
    { title: 'WasteSomeTi.me',
      tagline: 'Waste Time, Responsibly'
    });
};
