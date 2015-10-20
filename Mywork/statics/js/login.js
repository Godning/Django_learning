var btn = document.getElementById('btn');  
var re = document.getElementById('re');  
var user = document.getElementById('user');  
var password = document.getElementById('password'); 
var userlabel = document.getElementById('userlabel'); 
var pwdlabel = document.getElementById('pwdlabel'); 
btn.onclick = function(){  
    var isValidate=false;  
    if (!user.value.match(/^\S{2,20}$/)) {
    	userlabel.innerHTML = '<font color="red">请填写账号</font>';
        user.className = 'userRed';  
        user.focus();  
        return;  
    } else {  
    	userlabel.innerHTML ='';
        user.className = 'text';  
        isValidate=true;  
    }  
  
    if (password.value.length<3 || password.value.length>20) { 
    	pwdlabel.innerHTML = '<font color="red">请填写密码</font>';
        password.className = 'userRed';  
        password.focus();  
        return;  
    } else {  
    	pwdlabel.innerHTML ='';
        password.className = 'text';  
        isValidate=true;  
    }  
    
	if (isValidate) {
		$.get('/auth/?username='+document.getElementById('user').value+'&password='+document.getElementById('password').value,{},function(user){
			console.log(user);
			var con = document.getElementById('con'); 
			if (user){
				con.innerHTML = '<font color="green">登录成功，跳转中...</font>'; 
				//alert("登录成功，跳转中...")
	        	location = '/index/'; // 登录成功后指定跳转页面
			}else{
				con.innerHTML = '<font color="red">帐号或密码错误！</font>';
			}
		});
	}
}

	
re.onclick = function(){  
	 user.value="";  
	 password.value="";
}