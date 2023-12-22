window.addEventListener("DOMContentLoaded", function () {
    var app = new Vue({
        delimiters: ["[[", "]]"],
        el: '#chat-log',
        data: {
            statements: [],
        },
    })

    const roomName = "basic";
    const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/");

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        app.statements.push({
            type: 'answer',
            message: data.message,
            avatar: 'gpt_logo.svg',
            time: new Date(),
        });
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

        app.statements.push({
            type: 'querry',
            message,
            time: new Date(),
        });

        messageInputDom.value = "";
    };

    /* chat-history 드래그로 리스트 확인 기능 */
    new PerfectScrollbar(document.querySelector(".chat-history-body"), {
        wheelPropagation: !1,
        suppressScrollX: !0,
    });
});
