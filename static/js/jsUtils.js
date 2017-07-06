/**
 * Created by srikanthmv on 15/8/16.
 */
( function (hrmutils, $) {
    hrmutils.baseurl = '';
    hrmutils.getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    hrmutils.setNewCSRFToken = function () {
        var updatedToken = hrmutils.getCookie('csrftoken');
        $('form .csrfToken').each(function (index, value) {
            $(this).val(updatedToken);
        });
    };

    hrmutils.getResponse = function (reqType, path, sendData, callbacks ,isFormData) {

        isFormData = isFormData || false ;
        var response = {
            type: reqType,
            url: hrmutils.baseurl + path,
            //data: JSON.stringify(sendData),
            headers: {
                "X-CSRFToken": hrmutils.getCookie('csrftoken')
            },

            contentType: 'application/json'
        };
//        if (reqType != "GET") {
            if(isFormData){
                response["contentType"] = false;
                response["processData"] = false;
                response["data"] = sendData;
            }
            else{
                response["dataType"] = "json";
                response["data"] = JSON.stringify(sendData)
            }
//        }

        if (callbacks != undefined) {
            if (callbacks["success"]) {
                response["success"] = function (data, textStatus, jqXHR) {
                    callbacks["success"](data, textStatus, jqXHR);
                };
            }
            if (callbacks["error"]) {
                response["error"] = function (data, textStatus, jqXHR) {
                    callbacks["error"](data, textStatus, jqXHR);
                };
            }
        }
        $.ajax(response);
    };

}(window.hrmutils = window.hrmutils || {}, jQuery) );

function checklogin(){
    if(window.hrmutils.myAccount.accountMail)
    {
        return true;
    }
    else{
        return false;
    }
}

( function (myAccount, $) {
    myAccount.accountName = "";
    myAccount.accountMail = "";
    myAccount.setAccountName = function (userName) {
        myAccount.accountName = userName;
    };
    myAccount.setAccountMail = function (email) {
        myAccount.accountMail = email;
    };

}(window.hrmutils.myAccount = window.hrmutils.myAccount || {}, jQuery));


function showProcessingModal(heading, message){
    $("#processingModalHeading").text(heading);
    $("#processingModalMessage").text(message);
    $("#processingModal").modal({backdrop: 'static', keyboard: false}, 'show');
}

function showErrorModal(heading, message){
    $("#errorModalHeading").text(heading);
    $("#errorModalMessage").text(message);
    $("#errorModal").modal('show');
}

function showSuccessModal(heading, message){
    $("#successModalHeading").text(heading);
    $("#successModalMessage").text(message);
    $("#successModal").modal({backdrop: 'static', keyboard: false}, 'show')
}

function closeProcessingModal(){
    $("#processingModal").modal('hide');
}

function closeSuccessModal(){
    $("#successModal").modal('hide');
}

function closeErrorModal(){
    $("#errorModal").modal('hide');
}