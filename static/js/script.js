$(function () {
  validate("username", "username-check");
  validate("password", "pass-check");
  function validate(input, validationMessage) {
    let i = $("#" + input);
    let m = $("#" + validationMessage);

    if (i && m) {
      m.hide();
      $(i).keyup(function () {
        if (i.val().length === 0) {
          m.show();
          return false;
        } else {
          m.hide();
        }
      });
    }
  }
});
