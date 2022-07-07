document.getElementById('button').addEventListener('click', async function sd() {
    let fd = new FormData();
    if ((document.getElementById('username').value == '') || (document.getElementById("pwd").value == '')) {
        alert('Missing username and/or password!');
    }
    else {
        fd.append("username", document.getElementById('username').value);
        fd.append("password", document.getElementById("pwd").value);
        let response = await fetch('/login', {method: 'POST', body: fd});
        if (response.status == 215) {
            alert('Wrong password!');
        }
        if (response.status == 225) {
            alert('Wrong username!');
        }
        if (response.status == 200) {
            var url = await response.json();
            var url = url['url'];
            window.location.replace(url);
        }
    }
})