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
        showProcessingModal('Analyzing the data...','');
        var bulkPayslipsCallBacks =
        {
            "success": function(data){
                setTimeout(function(){
                    closeProcessingModal();
                    //showSuccessModal('Successfully analyzed the data', 'please wait still some process to be done.');
                    console.log(data.jsonData);
                    sendPaySlipsInBulk(data.jsonData);
                }, 2000);
            },
            "error": function(data){
                setTimeout(function(){
                    closeProcessingModal();
                    if(data.responseJSON.errorData){
                        showErrorModal('Errors found while processing', data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                    }
                    else{
                        showErrorModal('Something went wrong.', 'please try again later');
                    }
                }, 2000);

            }
        };
        hrmutils.getResponse("POST","ops-hr/api/payslips-in-bulk",formData,bulkPayslipsCallBacks, true)
    }

    function sendPaySlipsInBulk(extractedData){
        setTimeout(function(){
            showProcessingModal('Preparing data for payslips..', 'wait for a moment');
        }, 1000);
        var bulkPayslipsEmailsCallBacks = {
            "success": function(data){
                setTimeout(function(){
                    closeProcessingModal();
                    //showSuccessModal('Successfully processed the data..', 'please wait we are about to send mails to the employees.')
                    alreadySentUsersList = data.alreadySent;
                    console.log(alreadySentUsersList);
                    sendEmailsToUsers(data.userData);
                }, 2000);
            },
            "error": function(data){
                setTimeout(function () {
                    closeProcessingModal();
                    if(data.responseJSON.errorData){
                        showErrorModal('Errors found while processing', data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                    }
                    else{
                        showErrorModal('Something went wrong.');
                    }
                }, 2000);
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/send-payslips-emails-in-bulk",extractedData,bulkPayslipsEmailsCallBacks, false)

    }

    function sendEmailsToUsers(mailsData){
        setTimeout(function(){
            showProcessingModal("Sending "+mailsData.length+ " emails...",'this will take a moment. please wait.');
        }, 1000);
        var processEmailsCallBacks = {
            "success": function(data){
                setTimeout(function(){
                    closeProcessingModal();
                    if(alreadySentUsersList){
                        showSuccessModal('emails are successfully sent.', "already sent users :" + alreadySentUsersList);
                    }
                    else {
                        showSuccessModal('emails are successfully sent.');
                    }
                }, 2000);
            },
            "error": function(data){
                setTimeout(function(){
                    closeProcessingModal();
                    if(data.responseJSON.errorData){
                        showErrorModal('Errors found while sending emails', data.responseJSON.errorData.errorCode + ":" + data.responseJSON.errorData.errorMsg);
                    }
                    else{
                        showErrorModal('Something went wrong.', 'please try again later. thank you');
                    }
                }, 2000);
            }
        };
        hrmutils.getResponse("POST","ops-hr/api/process-emails-to-users",mailsData,processEmailsCallBacks, false);
    }
});