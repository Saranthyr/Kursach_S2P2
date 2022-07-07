document.getElementById('button').addEventListener('click', async function sd() {
        var op = document.getElementById('old_pwd').value;
        var np = document.getElementById('new_pwd').value;
        var npr = document.getElementById('new_pwd_rep').value;
        let fd = new FormData();
        fd.append("old_pwd", op);
        fd.append("new_pwd", np);
        fd.append("new_pwd_repeat", npr);
        let response = await fetch('/{{ username }}/settings', {method: 'POST', body: fd});
    });
    document.getElementById('logout').addEventListener('click', async function sd() {
        let response = await fetch('/logout', {method: 'POST', body: ''});
        if (response.status == 302) {
            var url = await response.json();
            var url = url['url'];
            window.location.replace(url);
        };
    })