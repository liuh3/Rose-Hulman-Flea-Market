var rh = rh || {};
rh.fm = rh.fm || {};

rh.fm.loginRose = function() {
	const
	registryToken = "772c16ee-3f8f-4484-8929-5cb5143da656";

	$('#login').click(function() {
		Rosefire.signIn(registryToken, function(error, rosefireUser) {
			if (error) {
				console.log("Error with Rosefire sign in");
				return;
			}
			window.location.replace("/login?token=" + rosefireUser.token);
		});
	});

};

rh.fm.enableButtons = function() {
	$('.insert-item').click(function() {
		var item_url = $('#image_url').val();
		var item_name = $('#item_name').val();
		var item_description = $('#item_description').val();
		var item_price = $('#item_price').val();
		console.log(item_url);
	});

	$("#attach-img-btn").click(function() {
		rh.fm.triggerFileInput();
	});

	$("#remove-img-btn").click(function() {
		$(this).hide();
		$("#current-img").hide();
		$("input[name=original_blob_key]").val("").prop("disabled", true);
		$("#attach-img-btn").text("Attach image");
	});

	$("#img-input").change(
			function(event) {
				console.log("image file changed");
				$("#attach-img-btn").text("Image saved");
				let
				file = event.target.files[0];
				var data = {
					message : file.name + " has been saved",
					timeout : 4000,
					actionHandler : rh.fm.triggerFileInput,
					actionText : "Edit"
				};
				document.querySelector('#snackbar-container').MaterialSnackbar
						.showSnackbar(data);
			});
};

rh.fm.triggerFileInput = function() {
	document.getElementById("img-input").click();
};

$(document).ready(function() {
	rh.fm.loginRose();
	rh.fm.enableButtons();
});
