const darkSchemeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
const superElement = document.documentElement;
superElement.style.transition = "all 0.5s ease-in-out";

// Al cargar la página, aplicar el tema almacenado en localStorage o el preferido por el navegador
applyStoredOrPreferredTheme();

darkSchemeMediaQuery.addEventListener("change", (event) => {
	if (!event.matches) {
		applyTheme("light");
		superElement.style.setProperty("--background_theme", "var(--gris)");
	} else {
		applyTheme("dark");
		superElement.style.setProperty("--background_theme", "var(--oscuro)");
	}
});

function applyStoredOrPreferredTheme() {
	const storedTheme = localStorage.getItem("theme");
	const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
	const themeToApply = storedTheme || (prefersDarkScheme ? "dark" : "light");

	applyTheme(themeToApply);
}

function applyTheme(theme) {
	superElement.setAttribute("data-theme", theme);
	localStorage.setItem("theme", theme);
	toggleTheme(theme);
}

function toggleTheme(theme) {
	const setStyles = superElement.style;
	const getStyles = getComputedStyle(superElement);
	const oscuro = getStyles.getPropertyValue("--oscuro").toString();
	const gris = getStyles.getPropertyValue("--gris").toString();
	// let theme = superElement.getAttribute("data-theme");
	// theme = theme === "dark" ? "light" : "dark";
	superElement.setAttribute("data-theme", theme);
	localStorage.setItem("theme", theme);
	if (theme === "dark") {
		setStyles.setProperty("--background-theme", oscuro);
	} else {
		setStyles.setProperty("--background-theme", gris);
	}
	applyThemeBody(theme);
}

function applyThemeBody(theme) {
	const body = document.querySelector("body");
	if (theme === "dark" && body) {
		body.classList.add("dark");
		body.classList.remove("light");
	} else {
		body.classList.add("light");
		body.classList.remove("dark");
	}
}
