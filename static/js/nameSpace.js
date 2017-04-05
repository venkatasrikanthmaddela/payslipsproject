/**
 * Created by oliverqueen on 3/29/2017.
 */

( function (myAccount, $) {
    myAccount.accountName = "";
    myAccount.accountMail = "";
    myAccount.setAccountName = function (userName) {
        myAccount.accountName = userName;
    };
    myAccount.setAccountMail = function (email) {
        myAccount.accountMail = email;
    };

}(window.pmproject.myAccount = window.pmproject.myAccount || {}, jQuery));