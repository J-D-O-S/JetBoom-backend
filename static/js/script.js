// window.onload = function () {
// 	let btn_close_userInfo, btn_change_theme;
// 	const body = document.querySelector("body");
// 	const userInfo = document.querySelector(".user-info");

// 	userInfo.addEventListener("click", function () {
// 		userInfo.classList.add("info-show");

// 		btn_close_userInfo = document.querySelector(".close-user-info");
// 		if (btn_close_userInfo) {
// 			btn_close_userInfo.addEventListener("click", function (e) {
// 				e.stopPropagation();
// 				userInfo.classList.remove("info-show");
// 			});
// 		}

// 		btn_change_theme = document.querySelector(".cambiar-tema");
// 		if (btn_change_theme) {
// 			btn_change_theme.addEventListener("click", function (e) {
// 				e.stopPropagation();
// 				toggleTheme();
// 			});
// 		}
// 	});

// 	function toggleTheme() {
// 		const htmlElement = document.documentElement;
// 		const setStyles = htmlElement.style;
// 		const getStyles = getComputedStyle(htmlElement);
// 		const oscuro = getStyles.getPropertyValue("--oscuro").toString();
// 		const gris = getStyles.getPropertyValue("--gris").toString();
// 		let theme = htmlElement.getAttribute("data-theme");
// 		theme = theme === "dark" ? "light" : "dark";
// 		htmlElement.setAttribute("data-theme", theme);
// 		if (theme === "dark") {
// 			setStyles.setProperty("--background-theme", oscuro);
// 		} else {
// 			setStyles.setProperty("--background-theme", gris);
// 		}
// 		applyThemeBody(theme);
// 	}

// 	function applyThemeBody(theme) {
// 		if (theme === "dark" && body) {
// 			body.classList.add("dark");
// 			body.classList.remove("light");
// 		} else {
// 			body.classList.add("light");
// 			body.classList.remove("dark");
// 		}
// 	}
// };

window.onload = function () {
	let btn_close_userInfo;
	const body = document.querySelector("body");
	const userInfo = document.querySelector(".user-info");

	userInfo.addEventListener("click", function () {
		userInfo.classList.add("info-show");

		btn_close_userInfo = document.querySelector(".close-user-info");
		if (btn_close_userInfo) {
			btn_close_userInfo.addEventListener("click", function (e) {
				e.stopPropagation();
				userInfo.classList.remove("info-show");
			});
		}
	});

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
};
