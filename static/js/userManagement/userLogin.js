/**
 * Created by oliverqueen on 3/29/2017.
 */
$(document).ready(function(){
    $(".admin-login").click(function(){
        loginData = {
            "username":$(".user-name-field").val(),
            "password":$(".password-field").val()
        };
        if(loginData.username && loginData.password){
            loginCallBacks = {
                "success": function(data){
                    window.hrmutils.myAccount.setAccountMail(data['email']);
                    window.hrmutils.myAccount.setAccountName(data["result"]);
                    window.hrmutils.setNewCSRFToken();
                    if (window.location.pathname == "/sign-in") {
                        window.location = "/";
                    }
                },
                "error": function(data){
                    alert(data.responseJSON.error);
                }
            };
            hrmutils.getResponse("POST","account/api/admin-login",loginData,loginCallBacks,false);
        }
        else{
            alert("Please fill all the values.Thank you");
        }
    });

    $(".sign-up").click(function(){
        var formId = $(this).attr("data-form-id");
        var formData = new FormData($(this).closest("#"+formId)[0]);
        if($('#user-name').val()==""||$("#email-id").val()==""||$("#password").val()==""){
            alert("please fill all the details")
        }
        else{
            SignUpData = {
                "username":$('#user-name').val(),
                "email":$("#email-id").val(),
                "password":$("#password").val()
            };
            signUpCallBacks = {
                    "success": function(data){
                        window.hrmutils.myAccount.setAccountMail(data['email']);
                        window.hrmutils.myAccount.setAccountName(data["result"]);
                        window.hrmutils.setNewCSRFToken();
                        if (window.location.pathname == "/sign-up") {
                            window.location = "/";
                        }
                    },
                    "error": function(data){
                        alert(data.responseJSON.error);
                    }
                };
            hrmutils.getResponse("POST","account/api/sign-up",SignUpData,signUpCallBacks,false);
        }
    });
});