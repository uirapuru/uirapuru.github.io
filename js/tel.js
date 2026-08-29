// Numer telefonu składany dopiero w przeglądarce.
// W kodzie strony nie ma go w całości, więc roboty zbierające numery go nie znajdą.
(function () {
  var grupy = [[54, 48, 52], [52, 49, 49], [48, 56, 57]];
  var numer = grupy.map(function (grupa) {
    return grupa.map(function (kod) { return String.fromCharCode(kod); }).join('');
  }).join(' ');

  Array.prototype.forEach.call(document.querySelectorAll('[data-telefon]'), function (el) {
    var a = document.createElement('a');
    a.href = 'tel:+48' + numer.replace(/ /g, '');
    a.textContent = numer;
    el.textContent = '';
    el.appendChild(a);
  });
})();
