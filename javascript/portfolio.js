(function () {
    'use strict';
    var menu = document.querySelector('.menu-toggle');
    var navigation = document.querySelector('.site-navigation');
    if (menu && navigation) {
        menu.hidden = false;
        navigation.classList.add('menu-ready');
        function closeMenu() {
            menu.setAttribute('aria-expanded', 'false');
            navigation.classList.remove('is-open');
        }
        menu.addEventListener('click', function () {
            var open = menu.getAttribute('aria-expanded') !== 'true';
            menu.setAttribute('aria-expanded', String(open));
            navigation.classList.toggle('is-open', open);
        });
        navigation.addEventListener('click', function (event) {
            if (event.target.closest('a')) closeMenu();
        });
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
                closeMenu();
                menu.focus();
            }
        });
    }
    var filters = document.querySelector('.project-filters');
    if (filters) {
        filters.hidden = false;
        filters.addEventListener('click', function (event) {
            var button = event.target.closest('button[data-filter]');
            if (!button) return;
            var count = 0;
            filters.querySelectorAll('button').forEach(function (item) {
                item.setAttribute('aria-pressed', String(item === button));
            });
            document.querySelectorAll('.project-card').forEach(function (card) {
                card.hidden = button.dataset.filter !== 'all' && card.dataset.category !== button.dataset.filter;
                if (!card.hidden) count += 1;
            });
            document.querySelector('.filter-status').textContent = count + ' projects shown.';
        });
    }
    // Retain incoming URLs from the original single-page academic archive.
    var legacy = {
        '#education': '/research/#background',
        '#articles': '/research/#articles',
        '#conferences': '/research/#conferences'
    };
    function followLegacyAnchor() {
        if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
            var destination = legacy[window.location.hash];
            if (destination) window.location.replace(destination);
        }
    }
    window.addEventListener('hashchange', followLegacyAnchor);
    followLegacyAnchor();
})();
