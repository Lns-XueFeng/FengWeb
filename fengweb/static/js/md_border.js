document.oncopy = function(event) {
    if (window.event) {
        event = window.event;
    }
    try {
        let the = event.srcElement;
        if (!((the.tagName == "INPUT" && the.type.toLowerCase() == "text") || the.tagName == "TEXTAREA")) {
            return false;
        }
        return true;
    } catch (e) {
        return false;
    }
}

setTimeout(function() {
if ($('#menu').length) {
  return;
}
let leftWidth = 250;
let hList = $('h1,h2,h3,h4,h5,h6')
let hListDomeString = '';
let blankDom = '<span style="width: 20px;" ></span>';
let blankDomMap = {
  'H1': 1,
  'H2': 2,
  'H3': 3,
  'H4': 4,
  'H5': 5,
  'H6': 6,
}
for (let i = 0; i < hList.length; i++) {
  let h = hList[i];
  let tagName = h.tagName;
  let innerText = h.innerText;

  hListDomeString += '<div>' +
  '<div style="width: '+ 10*blankDomMap[tagName] +'px;display: inline-block" ></div>' +
  '<a href="#' + h.id + '" style="" >' + innerText + '</a></div>'
}

$('body').html(
'<div id="menu" style="display: flex; overflow: hidden;">' + '<div style="width: ' + leftWidth + 'px;flex-shrink: 0;">' +
  '<div style="position:fixed; top:0;left:0;width:'+leftWidth+'px;height: 100vh;overflow:auto;font-size:14px;">'
   + '<h3 style="margin-left:10px;">^_^笔记文档目录^_^</h3>' + hListDomeString + '</div>' + '</div>' + '<div style="width: 4px; flex-shrink: 0; background: #efefef;"></div>' +
    '<div style="flex: 1;">' + $('body').html() + '</div>' + '</div>'
)
}, 500)