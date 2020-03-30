
filtered = []

var displayxitems = function (howmany) {
    $.ajax({
        type: "POST",
        url: "getthismany",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(howmany),
        success: function (result) {
            filtered = result
            makecards(result.filtered, "#tweetrow");
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

var makecards = function (arr, where) {
    $.each(arr, function (i, datum) {
        $(where).append("<div class='row col-md-4' id='row" + i + "'></div>")
        $("#row" + i).append("<div class='card border-primary mb-3' id='card" + i + "' style='width: 300px;'></div>")
        $("#card" + i).append("<a href='../view/"+arr[i]["Id"]+"'><img class='card-img-top cardimage' src='" + arr[i]["Image"] + "' alt='Card image cap'></a>")
        $("#card" + i).append("<div class='card-body' id='cardbody" + i + "'></div>")
        $("#cardbody" + i).append("<h5 class='card-title'>" + arr[i]["Title"] + "</h5>")
        $("#cardbody" + i).append("<p class='card-text'>" + arr[i]["Text"] + "</p>")
    })
}

var searchbykeyword = function (searchword) {
    $(".results").empty()
    $.ajax({
        type: "POST",
        url: "searchbykeyword",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(searchword),
        success: function (result) {
            filtered = result
            if (result.filtered.length == 0) {
                $("#tweetrow").append("No results found")
            }
            else {
                $(".results").append(result.filtered.length + " results found")
                makecards(result.filtered, "#tweetrow");
            }
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

var replaceText = function (keyword) {
    /*
    $("body").find(".highlight").removeClass("highlight");

    var searchword = keyword
    console.log(searchword)
    var custfilter = new RegExp(searchword, "ig");
    var repstr = "" + searchword + "";

    if (searchword != "") {
        $('body').each(function () {
            $(this).html($(this).html().replace(custfilter, repstr));
        })
    }
    */
}

var deleteitem = function(id) {
    $.ajax({
        type: "POST",
        url: "deleteitem",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(id),
        success: function (result) { //takes python result
            $("#row"+id).empty()
            $("#buttonrow"+id).empty()
            //makeTitleTextTweet(result, "#tweetrow")
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

$(document).ready(function () {
    //makecards(leads, "#tweetrow")
    displayxitems(11);
    $(document).on("click", "#submitbutton", function () {
        var keyword = $("#searchbox").val()
        $("#warning").empty();
        $("#tweetrow").empty();
        $(".results").empty();
        if (keyword == '') {
            $("#warning").append("Please enter a valid word!")
        }
        else {
            $("#search_box:text").val("")
            $("#search_box:text").focus()
            searchbykeyword(keyword)
            replaceText(keyword)
        }
    })
    $("#search_box").keyup(function (e) {
        if (e.keyCode == 13) {
            $("#submitbutton").click()
        }
    })
    $(document).on("click", ".deletebutton", function(){
        id = this.id
        console.log(id)
        deleteitem(id)
    })
})
