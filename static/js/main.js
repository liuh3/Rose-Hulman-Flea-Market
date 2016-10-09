$(document).ready(function() {
    const registryToken = "772c16ee-3f8f-4484-8929-5cb5143da656";
    
    $('#login').click(function() {
    	Rosefire.signIn(registryToken, function(error, rosefireUser) {
    		if (error) {
    			console.log("Error with Rosefire sign in");
    			return;
    		}
    		window.location.replace("/login?token=" + rosefireUser.token);
    	});
    });
});