//是否显示导航栏
 var showNavBar = true;
 //是否展开导航栏
 var expandNavBar = true;
 var currentIndex = 0;
 var currentScrollHigh = 0;
 var currentContentScrollHigh = 0;
 function sleep(numberMillis) {
    var now = new Date();
    var exitTime = now.getTime() + numberMillis;
    while (true) {
        now = new Date();
        if (now.getTime() > exitTime)
        return;
        }
}


$(window).onbeforeunload = function(){
currentIndex = 0;
}


 $(window).load(function(){
    var h1s = $("body").find("h1");
    var h2s = $("body").find("h2");
    var h3s = $("body").find("h3");
    var h4s = $("body").find("h4");
    var h5s = $("body").find("h5");
    var h6s = $("body").find("h6");

    var headCounts = [h1s.length, h2s.length, h3s.length, h4s.length, h5s.length, h6s.length];
    var vH1Tag = null;  // 显示的最高层级
    var vH2Tag = null;   // 显示的最低层级
var sum = 0;


    for(var i = 0; i < headCounts.length; i++){
          if(headCounts[i] > 0){
          for( var y = 0; y < headCounts[i]; y++)
                 sum = sum + 1;
          }
    }
    for(var i = 0; i < headCounts.length; i++){
        if(headCounts[i] > 0){
            if(vH1Tag == null){
                vH1Tag = 'h' + (i + 1);
            }else{
                vH2Tag = 'h' + (i + 1);
            }
        }
    }
    if(vH1Tag == null){
        return;
    }

    $("body").prepend('<div class="BlogAnchor">' +
        //'<span style="color:red;position:absolute;top:-6px;left:0px;cursor:pointer;" οnclick="$(\'.BlogAnchor\').hide();">×</span>' +
        '<p>' +
            '<b id="AnchorContentToggle" title="收起" style="cursor:pointer;">--------------目录--------------</b>' +
        '</p>' +
        '<div class="AnchorContent" id="AnchorContent"> </div>' +
    '</div>' );

    var vH1Index = 0;
    var vH2Index = 0;


    var vIndexH1 = 0;
    var vIndexH2 = 0;
    var vIndexH3 = 0;
    var vIndexH4 = 0;
    var vIndexH5 = 0;
    var vIndexH6 = 0;
    var headerALL = [];
    var headerIDALL = [];
    var headerHightALL = [];
    $("body").find("h1,h2,h3,h4,h5,h6").each(function(i,item){

        var id = '';
        var name = '';
        var tag = $(item).get(0).tagName.toLowerCase();
        var className = '';
        // i=0 tag=h1          i=1 tag=h2     i=2 tag=h2

        if(tag == "h1"){
            id = name = ++vIndexH1;
    vIndexH2 = 0;
    vIndexH3 = 0;
    vIndexH4 = 0;
    vIndexH5 = 0;
    vIndexH6 = 0;
    className = 'item_h1';

//alert("tag ="+ tag +"----   i = "+ i + " name ="+ name +"    className= "+ className);
//tag =h1----   i = 0 name =1    className= item_h1
        }else if(tag == "h2"){

            id = vIndexH1 + '_' + ++vIndexH2;
            name = vIndexH1 + '.' + vIndexH2;
            className = 'item_h2';
    vIndexH3 = 0;
    vIndexH4 = 0;
    vIndexH5 = 0;
    vIndexH6 = 0;

       }else if(tag == "h3"){
            id = vIndexH1 + '_' + vIndexH2+ '_' + ++vIndexH3;
            name = vIndexH1 + '.' + vIndexH2+ '.' + +vIndexH3;
            className = 'item_h3';
    vIndexH4 = 0;
    vIndexH5 = 0;
    vIndexH6 = 0;

       }

       else if(tag == "h4"){
            id = vIndexH1 + '_' + vIndexH2+ '_'  +vIndexH3 +'_'+ ++vIndexH4 ;
            name =  vIndexH1 + '.' + vIndexH2+ '.'  +vIndexH3 +'.'+  vIndexH4 ;
            className = 'item_h4';
    vIndexH5 = 0;
    vIndexH6 = 0;
       }

       else if(tag == "h5"){
            id = vIndexH1 + '_' + vIndexH2+ '_'  +vIndexH3 +'_' +vIndexH4+'_'+ ++vIndexH5;
            name = vIndexH1 + '.' + vIndexH2+ '.'  +vIndexH3 +'.' +vIndexH4+'.'+ vIndexH5;
            className = 'item_h5';
            vIndexH6 = 0;
       }

       else if(tag == "h6"){
            id = vIndexH1 + '_' + vIndexH2+ '_'  +vIndexH3 +'_' +vIndexH4+'_' +vIndexH5+'_'+ ++vIndexH6;
            name = vIndexH1 + '.' + vIndexH2+ '.'  +vIndexH3 +'.' +vIndexH4+'.' +vIndexH5+'.'+ vIndexH6;
            className = 'item_h6';

       }
        if(name.length > 2){

        var mFirstName = name.substring(0,2);
        while(mFirstName == "0."){
        name = name.substring(2,name.length);
        mFirstName = name.substring(0,2);
         }

        }
        $(item).attr("id","wow"+id+"_index_"+i);
        $(item).addClass("wow_head");
        var itemHeight = $(item).offset().top
        $("#AnchorContent").css('max-height', ($(document).height()) + 'px');
        $("#AnchorContent").css('height', ($(window).height()) + 'px');
        $("#AnchorContent").css('overflow','auto');
        $("#AnchorContent").append('<li><a class="nav_item '+className+' anchor-link"  href="#wow'+id+'_index_'+i+'" link="#wow'+id+'" index="'+i+'">'+name+" "+$(this).text()+" "+'</a></li>');
        var str = "#wow"+id+"_index_"+i;
        headerALL.push($(item));
        headerIDALL.push(str);
        console.log("  i = "+ i +"   id =" + id +"  itemHeight = "+ itemHeight);
    });

    // 1
    // 1.1
    // 1.1.1
    // 1.1.1.1
    // 1.1.1.1.1
    // 1.1.1.1.1.1
    $("#AnchorContentToggle").click(function(){
        var text = $(this).html();
        if(text=="目录"){
            $(this).html("目录");
            $(this).attr({"title":"展开"});
        }else{
            $(this).html("目录");
            $(this).attr({"title":"收起"});
        }
        $("#AnchorContent").toggle();
    });


$(".anchor-link").click(function(){

        //$("html,body").animate({scrollTop: $($(this).attr("link")).offset().top}, 10);
        var index  = $(this).attr("index");
                $(".BlogAnchor li .nav_item.current").removeClass('current');
                $(headerNavs[index]).addClass('current');
                      var scrollTop = $(window).scrollTop(); // 获得将要到达的点离顶距离
                      currentScrollHigh = scrollTop;
                      currentContentScrollHigh = headerHightALL[index];
      var value = headerTops[index];
      currentIndex = value;
      console.log("index = "+ index+ "  headerTops["+index+"] ="+ value + "scrollTop="+ scrollTop);
    });





    var headerNavs = $(".BlogAnchor li .nav_item");
    var headerTops = [];
    var mHeight = 0;
    $(".wow_head").each(function(i, n){
    var value = $(n).offset().top;

        headerTops.push($(n).offset().top);
         console.log("i = "+ i+ "  offset().top ="+ value);
    });
    headerTops.push($(document).height());

window.onresize = function(){

headerTops = [];
$.each(headerNavs, function(i, n){
$(n).trigger("click");
document.querySelector(headerIDALL[i]).scrollIntoView(true);
//var high = $(n).offset().top;
var scrollTop = $(window).scrollTop();
headerTops.push(scrollTop);
console.log("headerNavs_index="+i +"   scrollTop="+scrollTop +"  headerTops="+headerTops[i]);
}
);
headerTops.push($(document).height());

//$("#AnchorContent").height($(window).height());
$("#AnchorContent").css('height', ($(window).height()) + 'px');
var xcontentWidth =  $("#AnchorContent").width();
var xWidth = $(window).width();
var xlength = xWidth - xcontentWidth;
$("body").css("marginLeft",xcontentWidth+'px');
$("body").css("max-width",xlength);

$(headerNavs[currentIndex]).trigger("click");
document.querySelector(headerIDALL[i]).scrollIntoView(true);


}









$(window).scroll(function(){
        var scrollTop = $(window).scrollTop(); // 获得将要到达的点离顶距离

        $.each(headerTops, function(i, n){
            if( (scrollTop >= (headerTops[i])  && scrollTop < (headerTops[i+1] -1))  ){
                console.log("headerTops[i-1]"+headerTops[i-1]+"headerTops[i]"+headerTops[i]+"  scrollTop ="+ scrollTop+"  headerTops[i+1]= "+headerTops[i+1] +"  i ="+i);
                $(".BlogAnchor li .nav_item.current").removeClass('current');
                $(headerNavs[i]).addClass('current');
                currentScrollHigh = scrollTop;
                currentContentScrollHigh = headerHightALL[i];
                currentIndex = i;
                var mxxHeight = $("#AnchorContent").height()
                var mscrollTop1 = $("#AnchorContent").scrollTop();  // 当前标签的高度
            console.log("zukgit2 currentIndex="+ currentIndex );
                console.log("zukgit2 windows.scrollTop="+ scrollTop );
                console.log("zukgit2 $(window).height()="+ $(window).height() );
                console.log("zukgit2 currentContentScrollHigh="+ currentContentScrollHigh );
                console.log("zukgit2 AnchorContent.mscrollTop="+ mscrollTop1 );
                console.log("zukgit2 AnchorContent.high="+ mxxHeight );
                if((currentContentScrollHigh - mscrollTop1)>  ($(window).height()/2)){ //↓ // 如果当前index超出  界面的高度
                //var sum =   Math.floor(headerHightALL(i) / $(window).height());
                var dif = currentContentScrollHigh - mscrollTop1;
                $("#AnchorContent").animate({scrollTop: (currentContentScrollHigh)}, 50);
                console.log("  i(zukgit3) = "+ i +"   currentContentScrollHigh =" + currentContentScrollHigh +"  mscrollTop1 = "+ mscrollTop1);
                console.log(" $(window).height()="+ $(window).height() );

                } else if( ( mscrollTop1 - currentContentScrollHigh )>  0 ){  //↑
                $("#AnchorContent").animate({scrollTop: currentContentScrollHigh-($("#AnchorContent").height()/3)}, 50);
                console.log("  i(zukgit4) = "+ i +"   currentContentScrollHigh =" + currentContentScrollHigh +"  mscrollTop1 = "+ mscrollTop1);
                console.log(" $(window).height()="+ $(window).height() +"   $(#AnchorContent).height()="+mxxHeight);
                }

                return false;
            }
        }
        );
        if(scrollTop == 0){
        $("#AnchorContent").animate({scrollTop: 0}, 50);
        }
        if(scrollTop == $(document).height()){
        $("#AnchorContent").animate({scrollTop: headerHightALL[headerHightALL.length-1]}, 50);
        }
    });


$.each(headerNavs, function(i, n){
var high = $(n).offset().top;
headerHightALL.push(high);
console.log("high"+high);
}
);


headerTops = [];
$.each(headerNavs, function(i, n){

$(n).trigger("click");
document.querySelector(headerIDALL[i]).scrollIntoView(true);

var scrollTop = $(window).scrollTop();

headerTops.push(scrollTop);
console.log("headerNavs_index="+i +"   scrollTop="+scrollTop +"  headerTops="+headerTops[i]);

}
);



headerTops.push($(document).height());
$(headerNavs[0]).trigger("click");
document.querySelector(headerIDALL[0]).scrollIntoView(true);




var xcontentWidth =  $("#AnchorContent").width();
var xWidth = $(window).width();
var xlength = xWidth - xcontentWidth;
$("body").css("marginLeft",xcontentWidth+'px');
$("body").css("max-width",xlength);

    if(!showNavBar){
        $('.BlogAnchor').hide();
    }
    if(!expandNavBar){
        $(this).html("目录▼");
        $(this).attr({"title":"展开"});
        //$("#AnchorContent").hide();
    }
 });