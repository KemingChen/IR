import re
string = """HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: text/html; charset=iso-8859-1
Date: Tue, 13 Jan 2009 21:48:47 GMT
Server: Apache/1.3.34 (Debian) PHP/5.2.0-8+etch13 mod_ssl/2.8.25 OpenSSL/0.9.8c
Connection: close
Last-Modified: Tue, 09 Dec 2008 20:36:20 GMT
ETag: "64a24-a297-493ed6c4"
Content-Length: 41623

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta http-equiv="Content-Type"
 content="text/html; charset=iso-8859-1">
  <meta name="keywords"
 content="beaded curtain,crystal balls,toys,games,puzzles,accessories,aleister,alien,amber,ant,ant farm,antfarm,ants,antville,arch,aroma,art,astronomy,bag,bath,beacon,bead,beaded,bead curtains,bird,black,black light,blue,bulb,bumpy,butterfly,camp,card,cartography,cast,cat,catch,cauldron,chart,checker,chinese,chinese checker,clear,clever,color,connection,countries,crowley,crystal ball,crystal ball stand,crystalball,curtain,curtains,deck,decor,design science toy,dinosaur,disco,fact,finder,finder,fine,flower,flutterby,fortune,fortune telling,fossil,frog,frog,frogs,future,galaxies,galaxy,game,garden,gem,generation,geoscope,giraffe,glass,globe,gold,green,guide,gyroscope,hoberman,hopscotch,incense,insect,insect in amber,insectlore,iris,iron,jute,kama,ladybug,lava,learning,line,lite,locator,mancala,math,metaphysical,milton,mineral,mirror,novelty,orbitor,party,past,pentagon,perfume,pink,planet,plasma,police,poster,pot,potjie,present,purple,puzzle,rainbow bead,raven,reading,red,regional,rhoma,rock,roger,rogers,rune,science,shade,silver,simulator,smell,smudge,soma,space,space station,specialty,sphere,stands,star,star chart,state,strobe,surf,sutra,tarot,teach,tensegritoy,thoth,tie,titanium,toad,treasure,tree,uncle,uncle milton,us,usa,usgs,white,witch,wood bead,world,zome,zometool,">
  <meta name="description"
 content="Quality gifts, games, toys, crystal balls, games, bead curtains and more from 0-0-0Checkmate.">
  <title>0-0-0Checkmate - Gifts, Games, Toys, Crystal Balls, Bead
Curtains and more!</title>
  <link rel="STYLESHEET" href="/style.css" type="text/css">
  <script language="JavaScript">

	function check(form) {
		if(blankQ(form.find.value)) {
		 	c=prompt("What do you want to find? (Enter a word like crystal, curtain...)","")
			form.find.value=c
		 }
		return true;
	}


	function blankQ(s)	{
		if(s.length==0) return true;
		for(i=0; i< s.length; i++) {
	 		c=s.charAt(i);
 			if ((c != ' ')&& (c != '\n') && (c != '\t')) return false;
		}
	return true;
	}

  </script>
<script language="JavaScript">
function setCookie() {
	cookieVal = 1;
	x = readCookie('cookieVal')
	t=(0+x-9999999)
	if( t > 0 ) { cookieVal = x; }
	return cookieVal;
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}
</script>
</head>
<body onload="setCookie()" leftmargin="0" topmargin="0"
 bgcolor="#ffffff" marginheight="0" marginwidth="0">
<!--Topnav-->
<table border="0" bordercolor="#00ffff" cellpadding="0" cellspacing="0"
 width="100%">
  <tbody>
    <tr>
      <td colspan="4"><img src="http://0-0-0checkmate.com/images/filler.gif" height="5" width="1"></td>
    </tr>
    <tr>
      <td width="8">&nbsp;</td>
      <td valign="top" width="200"><a href="/" target="_top"><img
 src="http://0-0-0checkmate.com/images/mini000.gif" border="0" height="20" hspace="0" vspace="0"
 width="200"></a></td>
      <td bgcolor="#146EB3" valign="top" width="8"><img
 src="http://0-0-0checkmate.com/images/cleft.gif" border="0" height="8" hspace="0" vspace="0"
 width="8"></td>
      <td bgcolor="#146EB3" valign="middle" width="85%">
      <table align="left" border="0" bordercolor="#ff00ff"
 cellpadding="2" cellspacing="0" height="23" width="326">
        <tbody>
          <tr>
            <td class="table"> <font size="1"><a href="http://0-0-0checkmate.com/index3.htm"
 target="main"><font color="WHITE">HOME</font></a><font color="WHITE">&nbsp;&nbsp;|</font>&nbsp;
            <a href="http://0-0-0checkmate.com/WhoWeAre.html" target="main"> <font color="WHITE">OUR
NAME</font></a>&nbsp;<font color="WHITE">|</font>&nbsp; <a
 href="http://0-0-0checkmate.com/schools.html" target="main" border="0"><font color="WHITE">SCHOOLS</font></a>&nbsp;<font
 color="WHITE">|</font>&nbsp; <a
 href="http://CheckmateGroup.biz/aboutco.html" target="main" border="0"><font
 color="WHITE">ABOUT</font></a>&nbsp;<font color="WHITE">|</font>&nbsp;</font></td>
          </tr>
        </tbody>
      </table>
      </td>
    </tr>
    <tr>
      <td colspan="4"><img src="http://0-0-0checkmate.com/images/filler.gif" height="1" width="1"></td>
    </tr>
    <tr>
      <td bgcolor="#146EB3" height="23" valign="top"><img
 src="http://0-0-0checkmate.com/images/cleft.gif" border="0" height="8" hspace="0" vspace="0"
 width="8"></td>
      <td colspan="3" bgcolor="#146EB3" height="23" valign="top">
      <table border="0" bordercolor="white" cellpadding="0"
 cellspacing="0">
        <tbody>
          <tr>
            <td class="table" height="23" valign="top" width="200">
            <form style="margin-top: 2px;" action="/cgi-bin/search.cgi"
 target="main" method="post" onsubmit="return check(this)"><font
 color="#ffffff" size="1">SEARCH</font> <font size="-1"><input
 size="12" name="find" type="text"></font> <input name="CMsessionID"
 value="87512956363" type="hidden"> <input value="Search" name="Search"
 src="http://0-0-0checkmate.com/images/go.gif" alt="Search" align="middle" border="0" height="19"
 type="image" vspace="0" width="19"> </form>
            </td>
            <td bgcolor="#146EB3" valign="middle" width="8"><img
 src="http://0-0-0checkmate.com/images/filler.gif" alt="" align="left" border="0" height="20"
 hspace="0" vspace="0" width="8"> </td>
            <td bgcolor="#146EB3" height="23" valign="top" width="285">
            <table align="left" border="0" bordercolor="#ff00ff"
 cellpadding="3" cellspacing="0">
              <tbody>
                <tr>
                  <td class="table" height="23" valign="top"> <font
 size="1"> <a href="http://0-0-0checkmate.com/Order.html" target="main" border="0"><font
 color="WHITE">FAX ORDER FORM</font></a>&nbsp;<font color="WHITE">|</font>&nbsp;
                  <font size="1"> <a href="http://0-0-0checkmate.com/Mention.html" target="main"><font
 color="WHITE">KUDOS</font></a></font> </font></td>
                </tr>
              </tbody>
            </table>
            </td>
			<td valign="top" bgcolor="146EB3" align="center" width="115"><form action="/cgi-bin/Cart.pl"><input type="image" src="/images/cart.gif" height=20 width=63 onclick="javascript:this.form.user.value=setCookie();"><input type="hidden" name="user" value=''><input type="hidden" name="dest" value="/--subdir--"></form>
 			</td>
          </tr>
        </tbody>
      </table>
      </td>
    </tr>
  </tbody>
</table>
<!--end topnav-->
<!--index3-->
<center><img src="http://0-0-0checkmate.com/0-0-0Checkmatelogo.gif" border="0"><br>
<span style="color: rgb(51, 102, 255); font-weight: bold;">Serving our
Online Customers since 1996 with<br>
a Great variety of Games, Toys, Novelties and Much more!<br>
<br>
</span>
<table style="width: 92%; text-align: left;" border="0" cellpadding="2"
 cellspacing="2">
  <tbody>
    <tr>
      <td style="vertical-align: top;">
      <table style="width: 100%; text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
        <tbody>
          <tr>
            <td style="vertical-align: top;">
            <table
 style="text-align: left; width: 273px; height: 661px;" border="0"
 cellpadding="2" cellspacing="2">
              <tbody>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://checkmategroup.biz/ZoneChart.html" target="_blank"><img
 alt="0-0-0Checkmate Product Gift Selection" src="http://0-0-0checkmate.com/Xleftnav.gif"
 style="border: 0px solid ; width: 273px; height: 106px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><a style="font-weight: bold;font-size: 20px" href="http://checkmategroup.biz/ZoneChart.html" target="_blank"><small><b>CURRENT
DELIVERY SCHEDULE</b></small></a></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><big
 style="color: rgb(204, 0, 0);"><big><span style="font-weight: bold;font-size: 16px">PRoDucT
ZoNE!</span></big></big></td>
                </tr>
                <tr>
<td style="vertical-align: top;"><small><a
style="font-weight: bold;font-size: 10px"
href="http://0-0-0checkmate.com/BlowOutSale/">**Blow-Out SPECIALS!**</a></small><br>
</td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Unusual_Wacky_and_Great_Gifts/">Unique
Great Gift Ideas!</a></small><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Home_Business_Professional_Protection/">Home,
Business, and Professional Protection</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><b><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Cool/">Crystal
Spheres
&amp;
Cool
Stuff</a></b></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/BeadedCurtain/">Beaded
Door and Window Curtains</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><b><font color="#800080"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/DesignScienceToys/">Puzzles
and Toys</a></font></b></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Bugs/">Bugs
and Other Critters</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Butterflies/">Flutterbys,
Ladybugs and Crawlers</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><b><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Hot/">HOT
Effects Wizardry</a></b></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/CardsandCardGames/">Card
Games &amp; Card Decks</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Gonge_Child_Activity_Sets_USA/">Gonge
Child Activity Sets!</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Raised_Relief_Maps/">Raised
Relief
"Bumpy" Maps</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/RavenMaps/">Gorgeous Raven
Shaded Maps</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><b><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Astronomy/">Astronomy
and Star Watching</a></b></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Games/">Unusual
Games</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/JigSaws/">Beautiful
Jigsaw
Puzzles</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/ZoLO_Fun/">ZoLO!</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Fun_Art/">Fun
Art!</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/All_Natural/">Natural
Products Just For You!</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><font color="#ff0000"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Spheres/">Gemstone
and Mineral Spheres</a></font></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="v"><font color="#ff0000"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Pyramids/">Gem Pyramids</a></font></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><font color="#ff0000"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Wands/">Gemstone Wands<br>
                  </a></font></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Kites/">Krazy
Kites</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Poland/">Elegant
Wooden
Boxes</a></font></b></small></td>
                </tr>
                <tr>
				  <td style="vertical-align: top;"><small><b><font
				 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/Clever_Catch_Balls/">A Clever Catch</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><b><font
 face="Abadi MT Condensed"><a
style="font-weight: bold;font-size: 10px"
 href="http://0-0-0checkmate.com/Kaleidoscopes/">Fantastic
Kaleidoscopes</a></font></b></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><big
 style="color: rgb(204, 0, 0);"><big><span style="font-weight: bold;font-size: 16px">InFo
ZoNE!</span></big></big></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
style="font-weight: bold;font-size: 10px"
 href="http://checkmategroup.biz/Ordering.html" target="_blank">Order
By Telephone</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><font size="+1"><a
style="font-weight: bold;font-size: 10px"
 href="http://checkmategroup.biz/aboutco.html" target="_blank">Company
Information</a></font></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
style="font-weight: bold;font-size: 10px"
 href="mailto:Service@CheckmateGroup.biz">Contact Customer Service</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><font size="-1"><a
style="font-weight: bold;font-size: 10px"
 href="http://checkmategroup.biz/schools.html" target="_blank">Purchase
Orders</a></font></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
style="font-weight: bold;font-size: 10px"
 href="http://checkmategroup.biz/Mention.html" target="_blank">As
Mentioned
In....</a></td>
                </tr>
                <tr>
				<td style="vertical-align: top;"><font size="-1"><a
style="font-weight: bold;font-size: 10px"
				 href="http://checkmategroup.biz/Comments.html" target="_blank">Customer Kudos</a></font></td>
				                </tr>

                <tr>
                  <td style="vertical-align: top;">
                  <h5><a
style="font-weight: bold;font-size: 10px" href="http://0-0-0checkmate.com/WhoWeAre.html">Why
the
Name 0-0-0Checkmate?</a></h5>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><span
 style="color: rgb(255, 0, 0); font-weight: bold;font-size: 12px">Absolutely No
Wholesale Sales</span></td>
                </tr>
                <tr align="center">
                  <td style="vertical-align: top;"><big><font size="-2"><big>Copyright&copy;
0-0-0Checkmate, </big></font></big><br>
                  <big><font size="-2"><big>The Checkmate Group, LLC.</big></font></big><br>
                  <big><font size="-2"><big>All
rights
reserved!</big></font></big></td>
                </tr>
              </tbody>
            </table>
            <br>
            </td>
            <td style="vertical-align: top;">
            <table style="width: 100%; text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
              <tbody>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Bugs/" title="Ant Farms, Gel Farms, Insect Habitats, Ladybugs, Butterflies, Underwater Habitats, and more! Lots of styles made just for the bug lover!">Ants, Bugs and Critters</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Ant_Farm_Information.htm"
 target="_blank"><small>-About
Ants-</small></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Xtreme
Ants!, Giant Ant Farm,<br>
NEW! Gel Farm ... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Bugs/" title="Extreme Ant Farm with BMX ANT Race Track!"><img alt="Extreme Ant Farm"
 src="http://0-0-0checkmate.com/Xtreme_Ants.jpg"
 style="border: 0px solid ; width: 100px; height: 88px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Butterflies/" title="Butterflies, Ladybugs, Habitats, Puzzles and much more! Just the right gift for the beautiful bug lover!">More Beautiful &amp;
Cute Insects</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Butterflies,
Ladybugs...MORE!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Butterflies/" title="Wooden Monarch Butterfly Puzzle"><img
 alt="Wooden Monarch Butterfly Puzzle"
 src="http://0-0-0checkmate.com/Wood_Monarch_Butterfly_Puzzle_49242.gif"
 style="border: 0px solid ; width: 68px; height: 88px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Hot/" title="Invisible Paint, GID Paint, Plasma, Nebula, Blacklights, Strobe Lighting, Special Effects and more!">HOT Effects</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Blacklights,
Plasma Balls ...<br>
Much More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Hot/"><img
 alt="Lightcast Light iPod System"
 src="http://0-0-0checkmate.com/Lightcast_Light_iPod_System_12500.gif"
 style="border: 0px solid ; width: 64px; height: 78px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Astronomy/" title="Star Finders, Planispheres, Telescopes, Simulators, Posters and more!">Astronomy and Star Watching</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Star
Theater, Toys, Star Finders... More!</small></small></td>
                </tr>
                <tr align="center">
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Astronomy/" title="Star Theater SE Home Planatarium!"><img
 alt="Star Theater SE Home Planatarium!" src="http://0-0-0checkmate.com/StarTheaterSE_2070.gif"
 style="border: 0px solid ; width: 69px; height: 66px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Raised_Relief_Maps/" title="With BuMpY Raised relief maps, your state, country and world come alive!">Raised Relief
"Bumpy" Maps</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>States,
World, USA... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Raised_Relief_Maps/"><img
 alt="Bumpy Raised Relief Maps" src="http://0-0-0checkmate.com/Virginia_State.jpg"
 style="border: 0px solid ; width: 158px; height: 76px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small>also: <a
 href="http://0-0-0checkmate.com/RavenMaps/" title="Raven Maps have been called the most beautiful maps in the world!">Gorgeous Raven Shaded Maps!</a></small><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Fun_Art/" title="Blow up Scream, Pinhole Cameras, *Build It Yourself* crafts and games, and so much more!" >Fun Art!</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Mona
Lisa, Scream, Let's Build!...More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Fun_Art/" title="Pinhole Camera Kit! Plus, Let's Build or Paint Something plus parody Art"><img
 alt="Pinhole Camera Kit! Plus! Let's Build or Paint Something plus parody Art" src="http://0-0-0checkmate.com/Pinhole_Camera.gif"
 style="border: 0px solid ; width: 100px; height: 100px;"></a><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><big><small><big><b><font
 face="Abadi MT Condensed"><a href="http://0-0-0checkmate.com/Poland/" title="Famous, beautiful, stylish wooden boxes from Poland and more!">Elegant
Wooden Boxes</a></font></b></big></small></big></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Elegant,
Picture, Round, Domed, Design ... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><b><a
 href="http://0-0-0checkmate.com/Odds_N_Ends/" title="Check it out discounts!">Unadvertised
Sale</a></b></td>
                </tr>
              </tbody>
            </table>
            <br>
            </td>
            <td style="vertical-align: top;">
            <table style="width: 100%; text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
              <tbody>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Cool/" title="Featuring the Aurora Crystal Ball! Crystal Balls and Spheres, Stands and so much more!"><img
 alt="Featuring the Aurora Crystal Ball! Crystal Balls and Spheres, Stands and so much more!" src="http://0-0-0checkmate.com/Aurora_Crystal_Ball.gif"
 style="border: 0px solid ; width: 120px; height: 121px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a href="http://0-0-0checkmate.com/Cool/" title="Not Just for Fortune Tellers, any more! Collectors and lovers of fine crystal...available now, Crystal Balls and spheres and unique stand choices. Great selection of colors and styles!">Cool Crystal Gifts</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Crystal
Balls, Stands, Combos... <br>
Much More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small><font
 face="Abadi MT Condensed"><font size="+1"><small><a
 href="http://0-0-0checkmate.com/Crystal_Ball.html" title="Help with sizing! Help with crystal styles!">-Ball
Sizing and Info-</a></small></font></font></small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/CardsandCardGames/" title="Norman Rockwell Saturday Evening Post Playing Cards"><img
 alt="Norman Rockwell Saturday Evening Post Playing Cards, plus Cards, Decks, Games, Toys"
 src="http://0-0-0checkmate.com/Norman_Rockwell_Saturday_Evening_Post_Playing_Cards.gif"
 style="border: 0px solid ; width: 94px; height: 117px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/CardsandCardGames/" title="So fun! Giant Cards, Low Vision Cards, Wizard, Whack Pack, Quickword, Continuo and a lot more!">Card Decks and Games</a> </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Wizard,
Whack Pack,&nbsp; Duo, Continuo, <br>
Quickword, Card Games, More Decks..</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Home_Business_Professional_Protection/" title="Simple, inexpensive and easy way to detect Fake Money!"><img
 alt="Property and Valuables Protection, Detect and Stop Crooks and Thieves, Detect Germs, and so much more!"
 src="http://0-0-0checkmate.com/mini_blacklight_battery_powered.gif"
 style="border: 0px solid ; width: 104px; height: 77px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Home_Business_Professional_Protection/" title="Ultraviolet lights and pens, ink, test kits, and more! Protect your valuables easily and inexpensively! Property and Valuables Protection, Detect and Stop Crooks and Thieves. Also, Germ Detection!">Home
Business Professional Protection</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Property
Protection, Hand-Wash Training ... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://checkmategroup.biz/blacklight_uses.html" title="Money Authentication, ID and Document Verification, Crime Detection, Hunt down germs, Inspect antiques, detect forgeries, Hand stamping for parties and clubs, Mineral ID, some Pet Stains, and so much more!">-Amazing Uses
for Blacklights-</a><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><big><big><b><font
 face="Abadi MT Condensed"><a href="http://0-0-0checkmate.com/ZoLO_Fun/" title="Zolo Creative Play Sculptures! ZoloGoGo, Exobonz, Curious Bonz, SeaBonz, and so much more! Potato-heads move over! There's a new learning toy in town.">ZoLO!</a></font></b></big></big></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>EXoBonZ,
Pop ZoLo, So much Zolo!...&nbsp; More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;">
                  <table style="width: 100%; text-align: left;"
 border="0" cellpadding="2" cellspacing="2">
                    <tbody>
                      <tr>
                        <td
 style="vertical-align: top; text-align: center;"><a
 href="http://0-0-0checkmate.com/ZoLO_Fun/" title="Dragon Bonz, Sky Bonz, Pop Zolo, Bug Bonz and more fun bones!"><img
 alt="ExoBonz, Zolotopia, Wooden Zolo, Zolo-a-Go-Go, Dragon Bonz, Sky Bonz, Pop Zolo, Bug Bonz, Pre-Zolo and more fun bones!"
 src="http://0-0-0checkmate.com/BonzInset.jpg"
 style="border: 0px solid ; width: 49px; height: 107px;"></a></td>
                        <td style="vertical-align: top;"><br>
Wiggly<br>
Ziggly<br>
Oogly<br>
Fun!<br>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><big><b><font
 face="v"><font color="#ff0000"><a
 href="http://0-0-0checkmate.com/Pyramids/" title="Crystal, Mineral and Stone Pyramids">Pyramids</a></font></font></b></big></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><font
 face="Abadi MT Condensed"><font size="-1"><small><a
 href="http://0-0-0checkmate.com/Pyramids/Crystal.html">Crystal</a>, <a
 href="http://0-0-0checkmate.com/Pyramids/Mineral.html">Mineral</a>, <a
 href="http://0-0-0checkmate.com/Pyramids/Meditation.html">Meditation</a>...</small></font></font></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Pyramids/" title="Gorgeous Crystal, Mineral and Stone Pyramids"><img
 alt="Beautiful! Crystal Clear, Mineral & Stone and Aurora Pyramids" src="http://0-0-0checkmate.com/PYBB47960.gif"
 style="border: 0px solid ; width: 66px; height: 58px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;">also: <a
 href="http://0-0-0checkmate.com/Spheres/" title="Beautiful! Crystal Clear, Mineral & Stone and Aurora Spheres"><small>Gorgeous
Mineral <br>
and Crystal Spheres</small></a><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small>also:<a
 href="http://0-0-0checkmate.com/Wands/" title="Lovely Crystal, Mineral and Stone Healing Wands"> Gemstone Wands</a></small><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Unusual_Wacky_and_Great_Gifts/" title="Lots of Great Gift Ideas! Autograph Animals, Rice Bags, Unusual Card Decks, and so much more!">Unusual,
Weird,
Great Gifts!</a><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Unusual,
Weird, Great Gifts... More!</small></small></td>
                </tr>
              </tbody>
            </table>
            <br>
            </td>
            <td style="vertical-align: top;">
            <table style="width: 100%; text-align: left;" border="0"
 cellpadding="2" cellspacing="2">
              <tbody>
                <tr>
                  <td style="vertical-align: top;">
                  <table style="width: 100%; text-align: left;"
 border="0" cellpadding="2" cellspacing="2">
                    <tbody>
                      <tr>
                        <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/BeadedCurtain/"><img
 alt="Beaded Curtains styles acyrlic and wood"
 src="http://0-0-0checkmate.com/BeadCurtainSaleImage.jpg"
 style="border: 0px solid ; width: 124px; height: 135px;"></a></td>
                        <td style="vertical-align: top;"><small><big><b><font
 face="Abadi MT Condensed"><a
 href="http://0-0-0checkmate.com/BeadedCurtain/">Beaded
Door </a><br>
                        <a
 href="http://0-0-0checkmate.com/BeadedCurtain/">and Window
Curtains</a> </font></b></big> </small> </td>
                      </tr>
                    </tbody>
                  </table>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Acrylic,
Wooden, For Small Spaces ... Much More!&nbsp; </small></small><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;">Wooden Puzzles!<br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/DesignScienceToys/"><img
 alt="Puzzles, Toys, Games, Rogers Connectors, Hoberman, Zometool"
 src="http://0-0-0checkmate.com/Labrinyth_4663.gif"
 style="border: 0px solid ; width: 96px; height: 94px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/DesignScienceToys/">Challenging
Puzzles
and Toys</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Puzzles,
Games, Magnetic, Wire</small></small><small><small>... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;">
                  <table style="width: 100%; text-align: left;"
 border="0" cellpadding="2" cellspacing="2">
                    <tbody>
                      <tr>
                        <td
 style="vertical-align: top; text-align: center;"><a
 href="http://0-0-0checkmate.com/Gonge_Child_Activity_Sets_USA/"><span
 style="font-weight: bold;"><img src="http://0-0-0checkmate.com/Baby_Trampoline1.gif"
 alt="Gonge Child Activites, trampoline, go go rollers, balance, coordination"
 style="border: 0px solid ; width: 59px; height: 82px;"></span></a></td>
                        <td style="vertical-align: top;"><small><br>
Long-lasting <br>
Sturdy <br>
High Quality</small></td>
                      </tr>
                    </tbody>
                  </table>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Gonge_Child_Activity_Sets_USA/">Gonge
Child Activity
Sets!</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Trampolines,
Seesaws, Stilts, </small></small><br>
                  <small><small>Balancing Games ... More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><span
 style="color: rgb(0, 153, 0); font-weight: bold;">Always GREAT Pricing!</span>
                  <br>
                  <a
 href="http://0-0-0checkmate.com/DesignScienceToys/Zometools.html"><span
 style="color: rgb(153, 153, 153); font-weight: bold;">Zometool
Construction</span></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/DesignScienceToys/Zometools.html"><img
 alt="Zometool" src="http://0-0-0checkmate.com/Zometool5.gif"
 style="border: 0px solid ; height: 112px; width: 139px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr align="center">
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/JigSaws/"><img
 alt="variety of jigsaw puzzles"
 src="http://0-0-0checkmate.com/Fantasy_Knowledge_College_Jigsaw_Puzzle.gif"
 style="border: 0px solid ; width: 98px; height: 81px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><big><big><b><font
 face="Abadi MT Condensed"><a href="http://0-0-0checkmate.com/JigSaws/">Beautiful
Jigsaw Puzzles</a></font></b></big></big></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small>Animals,
Dragons, Fairies<br>
&nbsp;and Angels... Much More!</small></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><big><b><font
 face="Abadi MT Condensed"><a href="http://0-0-0checkmate.com/Games/">Cool
&amp; Unusual Games</a></font></b></big></small></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;">&nbsp;<small><small>Award
Winners, Backgammon, Chess...&nbsp; More!</small></small><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Games/"><img
 alt="Backgammon, Chess, Checkers, more" src="http://0-0-0checkmate.com/Backgammon_18_2414.gif"
 style="border: 0px solid ; width: 98px; height: 95px;"></a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><br>
                  </td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><a
 href="http://0-0-0checkmate.com/Kites/">Krazy Kites</a></td>
                </tr>
                <tr>
                  <td style="vertical-align: top;"><small><small><span
 style="font-family: abadi mt condensed;">Butterfly, Design It
Yourself, Microlites!...More!</span></small></small></td>
                </tr>
				              </tbody>
				            </table>
				            <br>
				            </td>
				          </tr>
				        </tbody>
				      </table>
				      </td>
				    </tr>
				  </tbody>
</table>
<!--end index3-->
<SCRIPT LANGUAGE=JAVASCRIPT TYPE='TEXT/JAVASCRIPT'>
<!--
function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = '; expires='+date.toGMTString();
	}
	else var expires = '';
	document.cookie = name+'='+value+expires+'; path=/';
}

x='-'+readCookie('originalRef')+'-';
if (x.indexOf('http') < 1) {
	if (document.referrer != '' ) {
		createCookie('originalRef',document.referrer,28)	//give them 28 days
	} else {
	}
}

//-->
</SCRIPT>
</body>
</html>


"""
# HTTP/1.1[^<]*
string = re.compile(r'[\n\r]*').sub('', string)
string = re.compile(r'HTTP/1.1[^<]*').sub('', string)
string = re.compile(r'(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>').sub('', string)
string = re.compile(r'(?i)<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>').sub('', string)
string = re.compile(r'(?i)<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>').sub('', string)
string = re.compile(r'<.*?>').sub(',', string)
print string