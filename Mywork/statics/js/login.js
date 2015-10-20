var btn = document.getElementById('btn');
var re = document.getElementById('re');
var user = document.getElementById('user');
var password = document.getElementById('password');
btn.onclick = function(){
	var isValidate=false;
	if (!user.value.match(/^\S{2,20}$/)) {
		user.className = 'userRed';
		user.focus();
		return;
	} else {
		user.className = 'text';
		isValidate=true;
	}

	if (password.value.length<3 || password.value.length>20) {
		password.className = 'userRed';
		password.focus();
		return;
	} else {
		password.className = 'text';
		isValidate=true;
	}
	if (isValidate) {
		ajax.get('login.php?user='+document.getElementById('user').value+'&password='+document.getElementById('password').value, function(data){
			var con = document.getElementById('con');
			eval(data);
			if (login) {
				con.innerHTML = '<font color="green">登录成功，跳转中...</font>';
				location = 'xx.php'; // 登录成功后指定跳转页面
			} else {
				con.innerHTML = '<font color="red">帐号或密码错误！</font>';
			}
		});
	}
	
}
re.onclick = function(){
	user.value="";
	password.value="";
}