<!--header -->
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	 <link rel="stylesheet" href="{% static "css/style.css" %}" />
	<title>{{title}}</title>
</head>

<body>

<div align="center">
<h1>{{header}}</h1>
</div>

<!--body -->
<div id="box">
	<div id="button"><a href='/'>Home</a></div>
	<div id="button"><a href='/create'>Create project</a></div>
	<div id="button"><a href='/collaborate'>Collaborate</a></div>
	<div id="button"><a href='/plist'>Project list</a></div>
	<div id="button"><a href='/about'>About</a></div>
	
	<div id="button" style="float:right;"><a href='/register'>Register</a></div>
	<div id="button" style="float:right;"><a href='/login'>Login</a></div>
	
	<!--header -->