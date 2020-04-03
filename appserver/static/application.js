
var butt = document.getElementsByClassName( 'splButton-primary' );
butt[0].style.backgroundColor = '#be454c';

var title = document.getElementsByTagName( 'h1' );
if ( title[0].innerHTML == 'mcrn_syslog' )
    {
     title[0].innerHTML = 'MARTIAN CONGRESSIONAL REPUBLIC NAVY :: CORVETTE SYSTEM LOG SETTINGS';
     title[0].style.textAlign = 'center';
     title[0].style.color = '#ffffff';
     title[0].style.marginTop = '0px';
     var div = document.getElementsByClassName( 'ManagerBar' );
     div[0].style.backgroundColor = '#b14c29';
     var bar = document.getElementsByClassName( 'editFormWrapper' );
     bar[0].style.borderTop = '0px';
     var form = document.getElementsByClassName( 'entityEditForm' );
     form[0].style.boxShadow = '0 0px 0px';
     var buttonDiv = document.getElementsByClassName( 'jmFormActions' );
     buttonDiv[0].style.borderTop = '0px';
     document.body.style.backgroundColor = '#5e4d45';
    }

