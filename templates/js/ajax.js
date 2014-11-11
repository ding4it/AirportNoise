var request;
function creatRequest()
{
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
		request=new XMLHttpRequest();
	}
	else
  	{// code for IE6, IE5
  		request=new ActiveXObject("Microsoft.XMLHTTP");
  	}
}

  function getData()
  {
  	creatRequest();
  	request.onreadystatechange=function()
 	{
  		if (xmlhttp.readyState==4 && xmlhttp.status==200)
    	{
    		data = request.responseXML;
    		
    	}
  	}
  	var url = "getData";
  	request.open("GET",url,true);
  	request.send();
  	return request.responseXML;
  }