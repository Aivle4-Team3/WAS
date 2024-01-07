const fileDOM = document.querySelector("#uploadAvatar");
const preview = document.querySelector("#uploadedAvatar");

fileDOM.addEventListener("change", () => {
    const reader = new FileReader();
    reader.onload = ({ target }) => {
        preview.src = target.result;
    };
    reader.readAsDataURL(fileDOM.files[0]);
});

const originalAvatarUrl = preview.src;
const resetDom = document.querySelector("#resetAvatar");
resetDom.addEventListener("click", () => {
    preview.src = originalAvatarUrl;
});
