var modalx = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

// 모달 열기 함수
function openModal() {
    modalx.style.display = "block";
}

// 닫기 버튼 클릭 시 모달 닫기
span.onclick = function () {
    modalx.style.display = "none";
};

// 모달 외부 클릭 시 모달 닫기
window.onclick = function (event) {
    if (event.target == modalx) {
        modalx.style.display = "none";
    }
};
