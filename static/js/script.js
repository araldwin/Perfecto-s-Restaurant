$(function () {
  validate("username", "username-check");
  validate("password", "pass-check");

  let login_button = $("#login-button");
  if (login_button) {
    $(login_button).on("click", function (e) {
      e.preventDefault();
      login();
    });
  }

  let register_button = $("#register-button");
  if (register_button) {
    $(register_button).on("click", function (e) {
      e.preventDefault();
      openRegisterModal();
    });
  }
});

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

function login() {
  var username = $("#username").val();
  var password = $("#password").val();
  var csrf_el = document.getElementsByName("csrfmiddlewaretoken");
  var csrf_value = csrf_el[0].getAttribute("value");

  $.ajax({
    url: "/login_user",
    type: "post",
    data: {
      username: username,
      password: password,
      csrfmiddlewaretoken: csrf_value,
    },
    success: function (data) {
      $("#response-message").text(data);
      if (data === "Success") {
        $("#response-message").addClass("text-success");
        window.location.replace("/");
      } else {
        $("#response-message").addClass("text-warning");
      }
    },
    error: function (data, textStatus, errorThrown) {
      $("#response-message").text(errorThrown).addClass("text-danger");
    },
  });
}

function openRegisterModal() {
  $.ajax({
    url: "/register_user",
    type: "get",
    success: function (data) {
      $("#modals-container").html(data);
      $("#registerModal").modal("show");
    },
  });
}
