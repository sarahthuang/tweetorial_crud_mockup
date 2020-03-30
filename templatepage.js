
/* Create a div whose contents are element, in where, with id id */
var makediv = function (element, where, id) {
    $("#row" + where).append("<div class='col-md-12 zero_padding' id='"+id+"'>" + element + "</div>");
}

/* Display all the types of leads in the LeadTypes array */
var makeleadtypes = function () {
/* ajax call to get all marked_as_deleted = false entries */
    id = tweet["Id"];
    $.ajax({
        type: "POST",
        url: "/getnondeleted",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(id),
        success: function (result) {
            var objlen = result["result"].length
            for (var i = 0; i < objlen; i++) {
                $("#typerow_" + i).empty()
                if (result["result"][i]["marked_as_deleted"] == true) { /* If deleted, add undo delete button */
                    console.log("deleted")
                    $("#typerow_" + i).append("<button type='button' id='undo_" + i + "' class='btn btn-warning undodeletebutton center inline'>undo delete</button>")
                }
                else { /* If not deleted, add content and delete button */
                    console.log("not deleted")
                    $("#typerow_" + i).append("<div class='inline zero_padding' style='padding-right: 10px' id='type_" + i + "' style='padding-bottom: 5px'>" + (i + 1) + ". " + result["result"][i]["Type"] + "</div>")
                    $("#typerow_" + i).append("<button type='button' id='" + i + "' class='btn btn-warning deletebutton center inline'>delete</button>")

                }
            }
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    
    $("#row" + id).append("<div class='col-md-12 zero_padding' id='LeadTypesRow'></div>");
    /* Add the lead type and a button to delete the item */
    for (var i = 0; i < tweet["LeadTypes"].length; i++) {
        $("#LeadTypesRow").append("<div class='col-md-12 zero_padding' id='typerow_" + i + "'></div>")
        $("#typerow_" + i).append("<div class='inline zero_padding' style='padding-right: 10px' id='type_" + i + "' style='padding-bottom: 5px'>" + (i + 1) + ". " + tweet["LeadTypes"][i]["Type"] + "</div>")
        $("#typerow_" + i).append("<button type='button' id='"+i+"' class='btn btn-warning deletebutton center inline'>delete</button>")
    }
}

/* Delete a lead type when a deletebutton is clicked */
var deletetype = function (index) {
    var deleteidarr = [index, id]
    /* ajax call sending id, index to be marked as deleted */
    $.ajax({
        type: "POST",
        url: "/deleteleadtype",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(deleteidarr),
        success: function (result) {
            ;
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });  
}

/* Undo a delete on a lead type */
var undodeletetype = function (index) {
    var undodeleteidarr = [index, id]
    /* ajax call sending id, index to be marked as deleted */
    $.ajax({
        type: "POST",
        url: "/undodeleteleadtype",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(undodeleteidarr),
        success: function (result) {
            $("#undo_" + index).remove()
            $("#typerow_" + index).append("<div class='inline zero_padding' style='padding-right: 10px' id='type_" + index + "' style='padding-bottom: 5px'>" + (parseInt(index) + 1) + ". " + result["typetoreturn"] + "</div>")
            $("#typerow_" + index).append("<button type='button' id='" + index + "' class='btn btn-warning deletebutton center inline'>delete</button>")
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });  
}

/* Initial page display */
var displaytweet = function(tweet, where) {
    id = tweet["Id"]
    $(where).append("<div class='row col-md-12 zero_padding' id='row"+id+"'></div>") 
    makediv("<img src='"+tweet["Image"]+"' width='300' height='300' alt='image link broken'>", id, "Image")

    /* Edit the title */
    makediv("Title: " + tweet["Title"], id, "Title")
    $("#row" + id).append("<button type='button' id='editTitle' class='inline btn btn-primary'>Edit title</button>")

    /* Edit the author */
    makediv("Author: " + tweet["Author"], id, "Author")
    $("#row" + id).append("<button type='button' id='editAuthor' class='inline btn btn-primary'>Edit author</button>")

    makediv("Date created: " + tweet["Date"], id, "Date")
    makediv("Lead text: " + tweet["Text"], id, "Text")

    /* Lead Types section */
    $("#row" + id).append("<div>List of Tweetorial Lead Types!</div>")
    makeleadtypes()

    /* Add a link to the Tweetorial Thread */
    $("#row" + id).append("<div class='col-md-12 zero_padding' id='Link'><a href='"+tweet["Link"]+"'>Link to Tweetorial Thread</ a></div >");
    /* $("#row" + id).append("<a href='../edit/" + id + "' data-role='button' button type='button' class='btn btn-primary infobutton col-md-1 zero_padding' id='" + id + "'>Edit title</button>") */
}

/* Editing a new title */
var submitTitle = function (newTitle) {
    var titleidarr = [newTitle, id]
    $.ajax({
        type: "POST",
        url: "/edit_Title", 
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(titleidarr),
        success: function (result) { 
            ;
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });  
}

/* Discarding edits to the title */
var discardTitle = function (oldtitle, addback) {
    $("#newTitle").remove()
    $("#submitTitle").remove()
    $("#discardTitle").remove()
    $("#emptyTitleWarning").remove()
}

/* Editing a new author */
var submitAuthor = function (newAuthor) {
    console.log(newAuthor)
    var authoridarr = [newAuthor, id]
    console.log(authoridarr)
    $.ajax({
        type: "POST",
        url: "/edit_Author",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(authoridarr),
        success: function (result) {
            ;
        },
        error: function (request, status, error) {
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });  
}

/* Discarding edits to the author */
var discardAuthor = function (oldAuthor, addback) {
    $("#newAuthor").remove()
    $("#submitAuthor").remove()
    $("#discardAuthor").remove()
    $("#emptyAuthorWarning").remove()
}

$(document).ready(function () {
    displaytweet(tweet, "#tweetrow")

    /* Manage interface display when user wants to change the title */
    $(document).on("click", "#editTitle", function () {
        $("#editTitle").remove()
        var title = $("#Title").text()

        /* From https://stackoverflow.com/questions/3421999/jquery-remove-only-text-content-from-a-div/3422046 */
        /* Removes contents of a div */
        $('#Title').contents().filter(function () {
            return this.nodeType === 3;
        }).remove();

        $("#Title").append("<input type='text' id='newTitle' placeholder='" + title + "'>");
        $("#newTitle").focus()
        $("#Title").append("<a href ='../view/" + id + "' data-role='button' button type = 'button' class='btn btn-primary' id = 'submitTitle'>Submit</a>");
        $("#Title").append("<a href ='../view/" + id + "' data-role='button' button type = 'button' class='btn btn-primary' id = 'discardTitle'>Discard</a>");

        $(document).on("click", "#submitTitle", function () {
            $("#emptyTitleWarning").remove()
            if ($("#newTitle").val() != '') {
                submitTitle($("#newTitle").val())
            }
            else {
                /* Append warning for empty */
                $("#Title").append("<span id='emptyTitleWarning' style='font-size: 10px; color: red;'>*please fill this in!</span>")
            }
        });
        $(document).on("click", "#discardTitle", function () {
            discardTitle(title, "Title")
        });
    })

    /* Manage interface display when user wants to change the author */
    $(document).on('click', '#editAuthor', function () {
        $('#editAuthor').remove()
        var author = $("#Author").text()
        $('#Author').contents().filter(function () {
            return this.nodeType === 3;
        }).remove();

        $("#Author").append("<input type='text' id='newAuthor' placeholder='" + author + "'>");
        $("#newAuthor").focus()
        $("#Author").append("<a href ='../view/" + id + "' data-role='button' button type = 'button' class='btn btn-primary' id = 'submitAuthor'>Submit</a>");
        $("#Author").append("<a href ='../view/" + id + "' data-role='button' button type = 'button' class='btn btn-primary' id = 'discardAuthor'>Discard</a>")

        $(document).on("click", "#submitAuthor", function () {
            $("#emptyAuthorWarning").remove()
            if ($("#newAuthor").val() != '') {
                submitAuthor($("#newAuthor").val())
            }
            else {
                /* Append warning for empty */
                $("#Author").append("<span id='emptyAuthorWarning' style='font-size: 10px; color: red;'>*please fill this in!</span>")
            }
        });
        $(document).on("click", "#discardAuthor", function () {
            discardAuthor(author, "Author")
        });
    })

    /* Manage interface display when the user wants to delete a list item */
    $(document).on('click', ".deletebutton", function () {
        var index = this.id
        deletetype(index)
        $("#type_" + index).remove() /* remove or hide? */
        $("#" + index).remove()
        $("#typerow_" + index).append("<button type='button' id='undo_" + index + "' class='btn btn-warning undodeletebutton center inline'>undo delete</button>")
    });

    /* Manage interface display when the user wants to undo a delete on a list item */
    $(document).on('click', ".undodeletebutton", function () {
        var index = this.id
        index = index.substring(index.length - 1, index.length)
        undodeletetype(index)
        /* Add back a delete button and the content type that was deleted */
    });
})