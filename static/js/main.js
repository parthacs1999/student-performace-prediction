// Small UI interactions: button pulse and smooth focus
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.btn, .btn.primary').forEach(btn => {
        btn.addEventListener('click', function (e) {
            this.classList.add('active');
            setTimeout(() => this.classList.remove('active'), 300);
        })
    })
    // Simple client-side validation: ensure required selects/inputs are filled
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (e) {
            const required = form.querySelectorAll('[required]');
            for (let el of required) {
                if (el.value === '' || el.value === null) {
                    e.preventDefault();
                    el.focus();
                    return false;
                }
            }
        })
    }
})
