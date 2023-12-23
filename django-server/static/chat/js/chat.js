window.addEventListener("DOMContentLoaded", function () {
    var app = new Vue({
        delimiters: ["[[", "]]"],
        el: "#app-history",
        data: {
            statements: [],
            inputMessage: "",
            sentMessages: 0,
        },
        computed: {
            waitting: function () {
                return this.sentMessages > 0;
            },
        },
        methods: {
            submit: function (e) {
                // 입력창 텍스트 가져오기
                var message = this.inputMessage;

                // 입력창 비우기
                this.inputMessage = "";

                // 서버로 전달
                chatSocket.send(
                    JSON.stringify({
                        message,
                    })
                );

                // 가상DOM으로 전달
                this.statements.push({
                    type: "querry",
                    message,
                    time: new Date(),
                });

                this.sentMessages += 1;
            },
        },
    });

    const roomName = "basic";
    const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + roomName + "/");

    // 서버에서 메시지 수용
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        // 가상DOM으로 전달
        app.statements.push({
            type: "answer",
            message: data.message,
            avatar: "gpt_logo.svg",
            time: new Date(),
        });

        app.sentMessages -= 1;
    };

    chatSocket.onclose = function (e) {
        console.error("Chat socket closed unexpectedly");
    };

    /* chat-history 드래그로 리스트 확인 기능 */
    new PerfectScrollbar(document.querySelector(".chat-history-body"), {
        wheelPropagation: !1,
        suppressScrollX: !0,
    });
});
