window.onload = function () {
    document.getElementById('upsc').addEventListener('click', function () {
        if (document.getElementById('upsc').checked) {
            document.getElementById('quality').setAttribute("style", 'display: flex');
            document.getElementById('qual_label').setAttribute("style", 'display: flex');
        }
        else {
            document.getElementById('quality').setAttribute("style", 'display: none');
            document.getElementById('qual_label').setAttribute("style", 'display: none');
        }
    })
    document.getElementById('file').addEventListener('input', function () {
        var file = document.getElementById('file').files[0];
        var url = URL.createObjectURL(file);
        var vid = document.createElement('video');
        vid.setAttribute('src', url);
        vid.addEventListener('loadedmetadata', function (e) {
            alert('Uploaded video parameters \n height: ' + e.target.videoHeight + ', width: ' + e.target.videoWidth + ', duration (in seconds): ' + e.target.duration + ', file size (in MB): ' + file.size/1024/1024)
        })
    })
    document.getElementById('button').addEventListener('click', async function sd() {
        var file = document.getElementById('file').files[0];
        let fd = new FormData();
        if (document.getElementById('upsc').checked == true) {
            fd.append("upscale", "up");
            fd.append("quality", document.getElementById("quality").value);
        }
        fd.append("file", file);
        fd.append("filename", document.getElementById('file').value);
        fd.append("ext", document.getElementById("ext").value);
        if (document.getElementById('time').checked == true) {
            if (document.getElementById('start_time').value != '') {
                fd.append("time_start", document.getElementById("start_time").value);
            }
            if (document.getElementById('type').value == 'end_time') {
                fd.append("endtime", document.getElementById('end_time').value)
            }
            else {
                fd.append("length", document.getElementById('fragment_length').value)
            }
        }
        let response = await fetch('/feat/convert', {method: 'POST', body: fd});
    })
    document.getElementById('time').addEventListener('click', function () {
        if (document.getElementById('time').checked) {
            document.getElementById('start_time').setAttribute("style", 'display: flex');
            document.getElementById('start_time_label').setAttribute("style", 'display: flex');
            document.getElementById('type_label').setAttribute("style", 'display: flex');
            document.getElementById('type').setAttribute("style", 'display: flex');
        }
        else {
            document.getElementById('start_time').setAttribute("style", 'display: none');
            document.getElementById('start_time_label').setAttribute("style", 'display: none');
            document.getElementById('type_label').setAttribute("style", 'display: none');
            document.getElementById('type').setAttribute("style", 'display: none');
        }
        document.getElementById('type').addEventListener('change', function (){
            console.log(document.getElementById('type').value);
            if (document.getElementById('type').value == 'end_time') {
                document.getElementById('end_time').setAttribute("style", 'display: flex');
                document.getElementById('fragment_length').setAttribute("style", 'display: none');
            }
            else{
                document.getElementById('fragment_length').setAttribute("style", 'display: flex');
                document.getElementById('end_time').setAttribute("style", 'display: none');
            }
    })
    })
}