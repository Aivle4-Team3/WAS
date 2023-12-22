window.addEventListener("DOMContentLoaded", function () {
    const roomName = "robby";

    const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/");

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        answer_html = `<li class="chat-message">
            <div class="d-flex overflow-hidden">
              <div class="user-avatar flex-shrink-0 me-3">
                <div class="avatar avatar-sm">
                  <img src="./Chat - Apps _ Sneat - Django Admin Template_files/2.png" alt="Avatar" class="rounded-circle">
                </div>
              </div>
              <div class="chat-message-wrapper flex-grow-1">
                <div class="chat-message-text">
                  <p class="mb-0">${data.message}</p>
                </div>
                <div class="text-muted mt-1">
                  <small>10:02 AM</small>
                </div>
              </div>
            </div>
          </li>`;
        document.querySelector("#chat-log").innerHTML += answer_html;
    };

    chatSocket.onclose = function (e) {
        console.error("Chat socket closed unexpectedly");
    };

    document.querySelector("#chat-message-input").focus();
    document.querySelector("#chat-message-input").onkeyup = function (e) {
        if (e.keyCode === 13) {
            // enter, return
            document.querySelector("#chat-message-submit").click();
        }
    };

    document.querySelector("#chat-message-submit").onclick = function (e) {
        e.preventDefault();
        const messageInputDom = document.querySelector("#chat-message-input");
        const message = messageInputDom.value;

        chatSocket.send(
            JSON.stringify({
                message: message,
            })
        );
        

        problem_html = `<li class="chat-message chat-message-right">
            <div class="d-flex overflow-hidden">
              <div class="chat-message-wrapper flex-grow-1">
                <div class="chat-message-text">
                  <p class="mb-0">${message}</p>
                </div>
                <div class="text-end text-muted mt-1">
                  <i class="bx bx-check-double text-success"></i>
                  <small>10:00 AM</small>
                </div>
              </div>
              <div class="user-avatar flex-shrink-0 ms-3">
                <div class="avatar avatar-sm">
                  <img src="./Chat - Apps _ Sneat - Bootstrap 5 HTML Admin Template - Pro_files/1.png" alt="Avatar" class="rounded-circle">
                </div>
              </div>
            </div>
          </li>`;
        document.querySelector("#chat-log").innerHTML += problem_html;

        messageInputDom.value = '';
        new PerfectScrollbar(document.querySelector(".chat-history-body"), {
            wheelPropagation: !1,
            suppressScrollX: !0,
        })
    };
});
