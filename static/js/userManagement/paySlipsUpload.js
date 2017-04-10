/**
 * Created by oliverqueen on 3/31/2017.
 */
$(document).ready(function(){
    var alreadySentUsersList = [];
    $(".upload-payslips-in-bulk").click(function(){
        var FormId = $(this).attr("data-id");
        if($("#pay-slips-file").val() == "")
        {
            alert("please select the file first.");
        }
        else{
            var formData = new FormData($(this).closest("#"+FormId)[0]);
            startProcessing(formData);
        }
    });

    function startProcessing(formData)
    {
        $('#ajax-processing-modal').modal({backdrop: 'static', keyboard: false}, 'show');
        var bulkPayslipsCallBacks =
        {
            "success": function(data){
                console.log(data.jsonData);
                $('#ajax-processing-modal').modal('hide');
                $('#success-modal').modal('show');
                sendPaySlipsInBulk(data.jsonData);
            },
            "error": function(data){
                $('#ajax-processing-modal').modal('hide');
                $("#error-msg-data").text(data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                if(data.responseJSON.errorData.other){
                    $("#misc-error-msg-data").text(data.responseJSON.errorData.other)
                }
                $('#error-processing-modal').modal('show');
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/payslips-in-bulk",formData,bulkPayslipsCallBacks, true)
    }

    function sendPaySlipsInBulk(extractedData){
        var bulkPayslipsEmailsCallBacks = {
            "success": function(data){
                $('#success-modal').modal('hide');
                alreadySentUsersList = data.alreadySent;
                console.log(alreadySentUsersList);
                sendEmailsToUsers(data.userData);

            },
            "error": function(data){
                $('#success-modal').modal('hide');
                $("#error-msg-data").text(data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                if(data.responseJSON.errorData.other){
                    $("#misc-error-msg-data").text(data.responseJSON.errorData.other)
                }
                $('#error-processing-modal').modal('show');
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/send-payslips-emails-in-bulk",extractedData,bulkPayslipsEmailsCallBacks, false)
    }

    function sendEmailsToUsers(mailsData){
        $('.emails-count').text("Sending "+mailsData.length+ " emails please wait...");
        $('#mails-processing-modal').modal({backdrop: 'static', keyboard: false}, 'show');
        var processEmailsCallBacks = {
            "success": function(data){
                $('#mails-processing-modal').modal('hide');
                if(alreadySentUsersList>0){
                    $("#already-sent-users").text("already sent users :" + alreadySentUsersList);
                    $("#mails-success-report-modal").modal('show');
                }
                else{
                    $("#mails-success-report-modal").modal('show');
                }
            },
            "error": function(data){
                $('#mails-processing-modal').modal('hide');
                if(data.responseJSON.errorData){
                    $("#misc-error-msg-data-for-mail").text(data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg)
                }
                $("#mails-error-modal").modal('show');
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/process-emails-to-users",mailsData,processEmailsCallBacks, false)
    }
});