window.onload = function () {
    document.querySelectorAll(".utility").forEach(function (node) {
        var vid = document.createElement('video');
        var source = document.createElement('source');
        source.setAttribute('src', "../static/vids/" + node.textContent);
        if (node.textContent.split('.')[1] == '3gp') {
            source.setAttribute('type', 'video/3gpp');
        }
        if (node.textContent.split('.')[1] == '3gpp2') {
            source.setAttribute('type', 'video/3gpp2');
        }
        if (node.textContent.split('.')[1] == 'mpeg') {
            source.setAttribute('type', 'video/mpeg');
        }
        if (node.textContent.split('.')[1] == 'mp4') {
            source.setAttribute('type', 'video/mp4');
        }
        if (node.textContent.split('.')[1] == 'ogg') {
            source.setAttribute('type', 'video/ogg');
        }
        if (node.textContent.split('.')[1] == 'mov') {
            source.setAttribute('type', 'video/quicktime');
        }
        vid.appendChild(source);
        vid.addEventListener('loadedmetadata', function (e) {
            node.textContent += '. . . . . . . . . . . . height: ' + e.target.videoHeight + ', width: ' + e.target.videoWidth + ', duration (in seconds): ' + e.target.duration
        })
    })
}