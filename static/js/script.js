window.onload = function () {
	let btn_close_userInfo;
	const body = document.querySelector("body");
	const userInfo = document.querySelector(".user-info");

	// Al cargar la página, aplicar el tema almacenado en localStorage o el preferido por el navegador
	applyStoredOrPreferredTheme();

	if (userInfo) {
		userInfo.addEventListener("click", function () {
			console.log("click");
			userInfo.classList.add("info-show");

			btn_close_userInfo = document.querySelector(".close-user-info");
			if (btn_close_userInfo) {
				btn_close_userInfo.addEventListener("click", function (e) {
					e.stopPropagation();
					userInfo.classList.remove("info-show");
				});
			}
		});
	}

	// Delegación de eventos para manejar el cambio de tema
	body.addEventListener("click", function (e) {
		const btn_change_theme = e.target.closest(".cambiar-tema");
		if (btn_change_theme) {
			e.stopPropagation();
			toggleTheme();
		}
	});

	function toggleTheme() {
		const htmlElement = document.documentElement;
		const setStyles = htmlElement.style;
		const getStyles = getComputedStyle(htmlElement);
		const oscuro = getStyles.getPropertyValue("--oscuro").toString();
		const gris = getStyles.getPropertyValue("--gris").toString();
		let theme = htmlElement.getAttribute("data-theme");
		theme = theme === "dark" ? "light" : "dark";
		htmlElement.setAttribute("data-theme", theme);
		localStorage.setItem("theme", theme);
		if (theme === "dark") {
			setStyles.setProperty("--background-theme", oscuro);
		} else {
			setStyles.setProperty("--background-theme", gris);
		}
		applyThemeBody(theme);
	}

	function applyThemeBody(theme) {
		if (theme === "dark" && body) {
			body.classList.add("dark");
			body.classList.remove("light");
		} else {
			body.classList.add("light");
			body.classList.remove("dark");
		}
	}

	function applyStoredOrPreferredTheme() {
		const storedTheme = localStorage.getItem("theme");
		const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
		const themeToApply = storedTheme || (prefersDarkScheme ? "dark" : "light");

		document.documentElement.setAttribute("data-theme", themeToApply);
		applyThemeBody(themeToApply);
		const setStyles = document.documentElement.style;
		const getStyles = getComputedStyle(document.documentElement);
		const oscuro = getStyles.getPropertyValue("--oscuro").toString();
		const gris = getStyles.getPropertyValue("--gris").toString();
		if (themeToApply === "dark") {
			setStyles.setProperty("--background-theme", oscuro);
		} else {
			setStyles.setProperty("--background-theme", gris);
		}
	}

	// funcionalidades para el formulario de galeria para poder subir imagenes
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

	const containerGaleriaPicture = document.querySelector(".seleccion_foto_galeria");
	const btnUploadImageGaleria = document.getElementById("id_foto_galeria");

	if (containerGaleriaPicture && btnUploadImageGaleria) {
		containerGaleriaPicture.addEventListener("click", function () {
			btnUploadImageGaleria.click();
		});

		btnUploadImageGaleria.addEventListener("change", function () {
			this.form.submit();
		});
	}
};
