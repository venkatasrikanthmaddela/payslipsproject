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
            $("#pay-slips-file").val("");
            startProcessing(formData);
        }
    });
    $(".see-preview").click(function(){
        initializeTable();
        closePreviewModal();
        $("#tableContainer").show();
        $('html, body').animate({
            scrollTop: $("#tableContainer").offset().top
        }, 2000);
    });

    $(".click-to-send").click(function(){
        sendEmailsToUsers(window.hrmutils.payslipData.previewData);
    });

    $(document.body).on('click', '.view-payslip', function(){
        showErrorModal("Announcement", "sorry. the payslip preview feature is still in development stage. inconvenience regretted.")
        //var employeeEmailId = $(this).attr("data-user-email");
        //for(var eachPaySlipData in window.hrmutils.payslipData.previewData){
        //    if(window.hrmutils.payslipData.previewData[eachPaySlipData]["email id"]== employeeEmailId){
        //        getHtmlTemplate(window.hrmutils.payslipData.previewData[eachPaySlipData])
        //    }
        //}
    });

    function getHtmlTemplate(employeeData){
        var htmlPreviewCallBacks = {
            "success": function(data){
                //showPaySlipPreviewModal(data["employeeData"]);
                $("#paySlipPreviewBody").html(data["htmlData"]);
                var doc = new jsPDF();
                var specialElementHandlers = {
                    '#paySlipPreviewBody': function (element, renderer) {
                        return true;
                    }
                };
                doc.fromHTML($('#paySlipPreviewBody').html(), 15, 15, {
                    'width': 170,
                    'elementHandlers': specialElementHandlers
                });
                doc.save('sample-file.pdf');
            },
            "error": function(){
                alert("error");
            }
        };
        window.hrmutils.getResponse("POST", 'ops-hr/api/payslip-html-preview', {"employeeData":employeeData}, htmlPreviewCallBacks, false)
    }

    function initializeTable(){
        var data = window.hrmutils.payslipData.previewData;
        $("#paySlipsPreviewTable tbody > tr").remove();
        for(var each_obj in data){
            drawTable(data[each_obj]);
        }
        $('#paySlipsPreviewTable').DataTable();
    }

    function drawTable(rowData){
        var row = $("<tr />");
        $("#paySlipsPreviewTable").append(row);
        row.append($("<td>" + rowData['employee name'] + "</td>"));
        row.append($("<td>" + rowData['employee number'] + "</td>"));
        row.append($("<td>" + rowData['email id'] + "</td>"));
        row.append($("<td>" + rowData['otherCalculations']['grossEarnings'] + "</td>"));
        row.append($("<td>" + rowData['otherCalculations']['totalNetPay'] + "</td>"));
        row.append($("<td>" + '<a class="btn btn-sm btn-outline-default view-payslip" data-user-email='+rowData['email id']+'>view payslip</a>' + "</td>"));
    }

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
                    var currentUserData = data.userData;
                    for(var obj_str in currentUserData){
                        console.log(currentUserData[obj_str]["email id"]);
                        if(($.inArray(currentUserData[obj_str]["email id"], window.hrmutils.payslipData.currentEmails)== -1)){
                            window.hrmutils.payslipData.currentEmails.push(currentUserData[obj_str]["email id"]);
                            window.hrmutils.payslipData.previewData.push(currentUserData[obj_str]);
                        }
                    }
                    previewEmails();
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

    function previewEmails(ExtractedData){
        setTimeout(function(){
            showPreviewModal();
        }, 1000);
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