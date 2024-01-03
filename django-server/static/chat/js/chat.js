window.addEventListener("DOMContentLoaded", function () {
    var app = new Vue({
        delimiters: ["[[", "]]"],
        el: "#app-history",
        data: {
            // 메시지 내용 기록 { type, message, avatar, time }
            statements: [],
            // 현재 입력 중인 메시지
            inputMessage: "",
            // 서버의 답변을 기다리고 있는 메시지 수
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
                    time: new Date().toLocaleTimeString(),
                });

                this.sentMessages += 1;
            },
        },
        mounted() {
            /* chat-history 드래그로 리스트 확인 기능 */
            new PerfectScrollbar(this.$refs.chatHistoryBody, {
                wheelPropagation: !1,
                suppressScrollX: !0,
            });
        },
        updated() {
            i = this.$refs.chatHistoryBody;
            i.scrollTo(0, i.scrollHeight);
        },
    });
    const video_id = this.document.querySelector('#app-history').dataset.videoId;
    const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" + video_id + "/");

    // 서버에서 메시지 수용
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        // 가상DOM으로 전달
        app.statements.push({
            type: "answer",
            message: data.message,
            avatar: "gpt_logo.svg",
            time: new Date().toLocaleTimeString(),
        });

        app.sentMessages -= 1;
    };

    chatSocket.onclose = function (e) {
        console.error("Chat socket closed unexpectedly");
    };
});
