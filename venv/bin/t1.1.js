var page = require('webpage').create();
url = 'https://c.open.163.com/mob/video.htm?plid=MD8VG7QS8&mid=MD8VHFF15#share-mob';
page.open(url, function(status) {
    console.log("Status: " + status);
    if (status === "success") {
        var out = document.getElementsByTagName("video")[0].src;
        // page.render('example.png');
        console.log(out);
    }
    phantom.exit();
});