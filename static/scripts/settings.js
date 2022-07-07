window.onload = function () {
    document.getElementById('button').addEventListener('click', async function sd() {

            var op = document.getElementById('old_pwd').value;
            var np = document.getElementById('new_pwd').value;
            var npr = document.getElementById('new_pwd_rep').value;
            let fd = new FormData();
            fd.append("old_pwd", op);
            fd.append("new_pwd", np);
            fd.append("new_pwd_repeat", npr);
            let response = await fetch(window.location.href, {method: 'POST', body: fd});
            if (response.status == 265) {
                alert('Current password does not match')
            }
            if (response.status == 255) {
                alert('New password does not match')
            }
    });
}