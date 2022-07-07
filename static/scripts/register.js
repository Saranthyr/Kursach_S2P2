document.getElementById('button').addEventListener('click', async function sd() {
    let fd = new FormData();
    if ((document.getElementById('username').value == '') || (document.getElementById("pwd").value == '') || (document.getElementById("pwd_rep").value == '')) {
        alert('Missing username and/or password!');
    }
    else {
        fd.append("username", document.getElementById('username').value);
        fd.append("pwd", document.getElementById("pwd").value);
        fd.append("pwd_rep", document.getElementById("pwd_rep").value);

        let response = await fetch('/register', {method: 'POST', body: fd});
        if (response.status == 254 {
            alert('User already exists');
        }
        if (response.status == 255) {
            alert("Passwords don't match");
        }
        if (response.status == 200) {
            var url = await response.json();
            var url = url['url'];
            window.location.replace(url);
        }
    }
})