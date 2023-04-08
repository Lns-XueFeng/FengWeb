let btn = document.querySelector('input')
let music = document.querySelector("audio")
btn.onclick = function(){
    if(btn.value=="播放"){
        music.play();
        btn.value = "暂停";
    }
    else{
        music.pause();
        btn.value = "播放";
    }
}

document.getElementById('closeBtn').onclick = function() {
    document.getElementById('myAlert').style.display = 'none';
}