/* Rizoivan CMS — mejoras de UX del admin (progressive enhancement) */
(function () {
    "use strict";

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function isTyping(el) {
        if (!el) return false;
        var tag = (el.tagName || "").toLowerCase();
        return tag === "input" || tag === "textarea" || tag === "select" || el.isContentEditable;
    }

    /* "/" enfoca la búsqueda del changelist o el filtro del sidebar */
    document.addEventListener("keydown", function (e) {
        if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) return;
        if (isTyping(document.activeElement)) return;
        var target = document.querySelector("#searchbar") || document.querySelector("#nav-filter");
        if (!target) return;
        e.preventDefault();
        target.focus();
        target.select && target.select();
    });

    /* Esc limpia el campo de búsqueda actual */
    document.addEventListener("keydown", function (e) {
        if (e.key !== "Escape") return;
        var el = document.activeElement;
        if (isTyping(el) && (el.id === "searchbar" || el.id === "nav-filter")) {
            el.value = "";
            if (el.id === "nav-filter") el.dispatchEvent(new Event("input", { bubbles: true }));
            el.blur();
        }
    });

    /* sombra en el header al hacer scroll (sensación de profundidad) */
    var header = document.getElementById("header");
    if (header && !reduceMotion) {
        var onScroll = function () {
            header.style.boxShadow = window.scrollY > 4
                ? "0 10px 30px -24px rgba(15,23,42,.65)"
                : "none";
        };
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();
    }

    /* animación de entrada de las tarjetas del dashboard */
    if (!reduceMotion) {
        var cards = document.querySelectorAll(".kpi-card, .panel, .admin-hero");
        cards.forEach(function (card, i) {
            card.style.opacity = "0";
            card.style.transform = "translateY(8px)";
            card.style.transition = "opacity .35s ease " + (i * 40) + "ms, transform .35s ease " + (i * 40) + "ms";
            requestAnimationFrame(function () {
                requestAnimationFrame(function () {
                    card.style.opacity = "1";
                    card.style.transform = "none";
                });
            });
        });
    }

    /* etiquetas de columna para el modo apilado en móvil (td::before usa attr()) */
    document.querySelectorAll("#content table").forEach(function (table) {
        var heads = Array.prototype.map.call(
            table.querySelectorAll("thead th"),
            function (th) { return th.textContent.trim(); }
        );
        table.querySelectorAll("tbody tr").forEach(function (tr) {
            Array.prototype.forEach.call(tr.children, function (cell, i) {
                if (heads[i]) cell.setAttribute("data-label", heads[i]);
            });
        });
    });

    /* los inputs editables no deben ensanchar la tabla (que quepa sin scroll
       en tablet; el CSS les da el 100% del ancho de su celda cuando hay sitio) */
    document.querySelectorAll(
        '#changelist table input[type="text"], #changelist table input[type="number"]'
    ).forEach(function (input) {
        if (!input.size || input.size > 12) input.size = 12;
    });

    /* aviso al salir con cambios sin guardar en formularios del admin */
    var forms = document.querySelectorAll("#content form[action*='/admin/']");
    forms.forEach(function (form) {
        var dirty = false;
        form.addEventListener("input", function () { dirty = true; });
        form.addEventListener("change", function () { dirty = true; });
        form.addEventListener("submit", function () { dirty = false; });
        window.addEventListener("beforeunload", function (e) {
            if (!dirty) return;
            e.preventDefault();
            e.returnValue = "";
        });
    });

    /* ----------------------------------------------------------- móvil --- */
    var main = document.getElementById("main");
    var toggle = document.getElementById("toggle-nav-sidebar");
    var mqAncho = window.matchMedia("(max-width: 1024px)");

    function drawerActivo() {
        return mqAncho.matches || document.body.classList.contains("rz-drawer-nav");
    }

    if (main) {
        if (mqAncho.matches) main.classList.remove("shifted");

        /* tocar el fondo (scrim) cierra el cajón */
        document.addEventListener("click", function (e) {
            if (!drawerActivo() || !main.classList.contains("shifted")) return;
            if (e.target === main || (e.target.classList && e.target.classList.contains("nav-drawer-scrim"))) {
                toggle && toggle.click();
            }
        });

        /* Esc también lo cierra */
        document.addEventListener("keydown", function (e) {
            if (e.key === "Escape" && drawerActivo() && main.classList.contains("shifted")) toggle && toggle.click();
        });
    }

    /* Si la tabla de la lista no cabe en pantalla, el sidebar pasa a cajón
       para que la lista se despliegue con todas sus columnas a la vista. */
    function ajustarListaAncha() {
        var results = document.querySelector("#changelist .results");
        var table = results && results.querySelector("table");
        if (!table) { document.body.classList.remove("rz-drawer-nav"); return; }
        document.body.classList.remove("rz-drawer-nav");
        var noCabe = table.scrollWidth > results.clientWidth + 1;
        if (noCabe && window.matchMedia("(min-width: 1025px)").matches) {
            document.body.classList.add("rz-drawer-nav");
            if (main) main.classList.remove("shifted");
        }
    }
    ajustarListaAncha();
    window.addEventListener("resize", ajustarListaAncha);
})();
