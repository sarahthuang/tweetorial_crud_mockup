$(function () {
    $("#resizable").resizable();
});

var clearAll = function () {
    $("#ipt_title").val('')
    $("#ipt_author").val('')
    $("#ipt_date").val('')
    $("#ipt_text").val('')
    $("#ipt_leadtypes").val('')
    $("#ipt_image").val('')
    $("#ipt_link").val('')
    $("#ipt_title").focus()
}

var addlink = function (link) {
    $("#ClickHere").append("New item created!")
    $("#LinkDiv").append("<a href='"+link+"' data-role='button' button type='button' class='btn btn-primary'>See it here</button>")
}

$(document).ready(function(){
    $("#addbutton").click(function () {
    /* Empty all warning fields */
        $("#inputrow").find('span').remove()
        $("#ClickHere").empty()
        $("#LinkDiv").empty()

        /* Capture all input values */
        title = $.trim($("#ipt_title").val())
        author = $.trim($("#ipt_author").val())
        date = $.trim($("#ipt_date").val())
        text = $.trim($("#ipt_text").val())
        leadtypes = $.trim($("#ipt_leadtypes").val())
        image = $.trim($("#ipt_image").val())
        link = $.trim($("#ipt_link").val())

        /* Add actual empty fields to an array */
        var emptyInputFields = []
        emptyInputFields.push({ "Title": title })
        emptyInputFields.push({ "Author": author })
        emptyInputFields.push({ "Date": date })
        emptyInputFields.push({ "Text": text })
        emptyInputFields.push({ "LeadTypes": leadtypes })
        emptyInputFields.push({ "Image": image })
        emptyInputFields.push({ "Link": link })
        
        $.each(emptyInputFields, function (index, value) {
            var key = Object.keys(emptyInputFields[index])
            var val = Object.values(emptyInputFields[index])
            if (val == "") {
                var area = String(key)
                $("#" + area).append("<span style='font-size: 10px; color: red;'>*please fill this in!</span>")
            }
        });

        if (title && author && date && text && leadtypes && image && link) {
            $("#invalidinput").empty()
            var newtweet = {
                "Title": title,
                "Author": author,
                "Date": date,
                "Text": text,
                "LeadTypes":
                    [
                        {
                            "Type": leadtypes,
                            "marked_as_deleted": false
                        }
                    ],
                "Image": image,
                "Link": link
            }
            console.log(leadtypes)
            $.ajax({
                type: "POST",
                url: "createtweet",
                dataType: "json",
                contentType: "application/json;charset=utf-8",
                data: JSON.stringify(newtweet),
                success: function (result) { 
                    view = result["link"]
                    addlink(view)
                    clearAll()
                },
                error: function (request, status, error) {
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            })
        }
    }) 
})