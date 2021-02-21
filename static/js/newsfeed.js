
window.onload = function() {
    var news_string = document.getElementById("newsfeed-fetch").textContent;

    items = news_string.split(",,,");

    var articles = [];
    var urls = [];
    var img_urls = [];

    for(let i = 0; i < items.length; i += 1) 
    {
        let item = items[i].split("::");
        if (item.length < 2) continue;
        let urls_ = item[1].split("---");
        articles.push(item[0]);
        urls.push(urls_[0]);
        img_urls.push(urls_[1]);
    }

    
    document.getElementById("img1").src = img_urls[0];
    var offset_index = 0;

    const imgs = [document.getElementById("img1"), document.getElementById("img2"), 
                    document.getElementById("img3"), document.getElementById("img4")];
    const titles = [document.getElementById("art1"), document.getElementById("art2"), 
                    document.getElementById("art3"), document.getElementById("art4")];

    for (let i = 0; i < 4; i++)
    {
        imgs[i].src = img_urls[(i + offset_index) % img_urls.length];
        titles[i].textContent = articles[(i + offset_index) % img_urls.length];
        titles[i].href = urls[(i + offset_index) % img_urls.length];
    }


    hoverIn = function(i)
    {
        imgs[i].style = "filter: grayscale(0);";
        titles[i].style = "color: #018779;";
    }
    hoverOut = function(i)
    {
        imgs[i].style = "filter: grayscale(1);";
        titles[i].style = "color: #eeeeee;";
    }

    var updateFeed = setInterval(function() {
        for (let i = 0; i < 4; i++)
        {
            imgs[i].style = "filter: opacity(0) grayscale(1);";
        }

        offset_index++;
        for (let i = 0; i < 4; i++)
        {
            imgs[i].src = img_urls[(i + offset_index) % img_urls.length];
            titles[i].textContent = articles[(i + offset_index) % img_urls.length];
            titles[i].href = urls[(i + offset_index) % img_urls.length];
        }
        setTimeout(function() {
            for (let i = 0; i < 4; i++)
        {
            imgs[i].style = "filter: opacity(1) grayscale(1);";
        }
        }, 300)
    }, 8000);
}





