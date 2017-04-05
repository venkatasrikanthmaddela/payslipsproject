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
                    if (window.location.pathname == "/") {
                        window.location = "/hr-action/dashboard";
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
});