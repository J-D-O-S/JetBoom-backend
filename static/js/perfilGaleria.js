window.onload = function () {
	const containerPerfilPicture = document.querySelector(".seleccion_foto_perfil");
	const btnUploadImage = document.getElementById("id_foto_perfil");

	if (containerPerfilPicture && btnUploadImage) {
		containerPerfilPicture.addEventListener("click", function () {
			btnUploadImage.click();
		});

		btnUploadImage.addEventListener("change", function () {
			this.form.submit();
		});
	}

	const containerPortadaPicture = document.querySelector(".seleccion_foto_portada");
	const btnUploadImagePortada = document.getElementById("id_foto_portada");

	if (containerPortadaPicture && btnUploadImagePortada) {
		containerPortadaPicture.addEventListener("click", function () {
			btnUploadImagePortada.click();
		});

		btnUploadImagePortada.addEventListener("change", function () {
			this.form.submit();
		});
	}
};
