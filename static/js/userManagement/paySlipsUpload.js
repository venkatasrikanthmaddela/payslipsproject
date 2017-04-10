/**
 * Created by oliverqueen on 3/31/2017.
 */
$(document).ready(function(){
    var alreadySentUsersList = [];
    $(".upload-payslips-in-bulk").click(function(){
        var FormId = $(this).attr("data-id");
        console.log($("#pay-slips-file").val());
        if($("#pay-slips-file").val() != ""){
            var formData = new FormData($(this).closest("#"+FormId)[0]);
            //$('#ajax-processing-modal').modal('show');
            var bulkPayslipsCallBacks = {
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
        else{
            alert("please select the file first.");
        }
    });
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
        $('#mails-processing-modal').modal('show');
        var processEmailsCallBacks = {
            "success": function(data){
                $('#mails-processing-modal').modal('hide');
                $("#mails-success-report-modal").show()
            },
            "error": function(data){
                $('#mails-processing-modal').modal('hide');
                $("#mails-error-modal").modal('show');
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/process-emails-to-users",mailsData,processEmailsCallBacks, false)
    }
});