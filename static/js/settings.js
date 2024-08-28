const preferencesColorScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
const darkSchemeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
const superElement = document.documentElement;
superElement.style.transition = "all 0.5s ease-in-out";
let themeSelected =
	getAttributeDataTheme(superElement) === undefined
		? preferencesColorScheme
		: getAttributeDataTheme(superElement);

function applyTheme(theme) {
	superElement.setAttribute("data-theme", theme);
	toggleTheme();
}

function getAttributeDataTheme(element) {
	let value = element.getAttribute("data-theme");
	return value;
}

if (themeSelected === "dark") {
	applyTheme("dark");
} else {
	applyTheme("light");
}

darkSchemeMediaQuery.addEventListener("change", (event) => {
	if (!event.matches) {
		applyTheme("dark");
		superElement.style.setProperty("--background_theme", "var(--oscuro)");
	} else {
		applyTheme("light");
		superElement.style.setProperty("--background_theme", "var(--gris)");
	}
});

function toggleTheme() {
	const setStyles = superElement.style;
	const getStyles = getComputedStyle(superElement);
	const negro = getStyles.getPropertyValue("--oscuro").toString();
	const gris = getStyles.getPropertyValue("--gris").toString();
	let theme = superElement.getAttribute("data-theme");
	theme = theme === "dark" ? "light" : "dark";
	superElement.setAttribute("data-theme", theme);
	if (theme === "dark") {
		setStyles.setProperty("--background-theme", negro);
	} else {
		setStyles.setProperty("--background-theme", gris);
	}
	applyThemeBody(theme);
}

function applyThemeBody(theme) {
	const body = document.querySelector(".body");
	if (theme === "dark" && body) {
		body.classList.add("dark");
		body.classList.remove("light");
	} else {
		body.classList.add("light");
		body.classList.remove("dark");
	}
}
