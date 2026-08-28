/* ===========================================================================
 * GS NET ACADEMY — testimonial / result carousel
 * ---------------------------------------------------------------------------
 * The ONLY JavaScript file on the site. It turns every result strip into a
 * smooth, never-ending marquee:
 *
 *   • the images glide continuously instead of jumping card by card
 *   • the row loops for ever — the last poster is followed by the first again
 *   • it pauses while the mouse is over it, or while a finger is on it
 *   • it pauses when the tab is in the background, so nothing runs wasted
 *   • the visitor can still swipe or scroll it by hand at any time
 *   • if someone has "reduce motion" switched on, it stays still
 *
 * IT NEEDS NOTHING IN THE HTML except the strip having class "tab-panel"
 * (the result rows already do). To use it on another row, just add that class
 * — or list your own selector in STRIPS below.
 *
 * SPEED — pixels per second. Higher = faster.
 * ========================================================================= */

(function () {
  "use strict";

  var SPEED = 34;                    // pixels per second
  var STRIPS = ".tab-panel";         // which rows to animate

  /* Respect the visitor's "reduce motion" setting. */
  var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function setup(strip) {
    var original = Array.prototype.slice.call(strip.children);
    if (original.length < 2) return;               // nothing to loop

    /* Scroll-snap fights a smooth glide — turn it off on this row. */
    strip.classList.remove("snap-x", "snap-mandatory");
    original.forEach(function (li) { li.classList.remove("snap-start"); });

    /* Duplicate the row once. The copy is what makes the loop seamless:
       when we have scrolled past the originals we jump back by exactly that
       width, and because the copy looks identical the jump is invisible. */
    original.forEach(function (li) {
      var clone = li.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");   // screen readers skip the copy
      clone.querySelectorAll("img").forEach(function (img) { img.setAttribute("loading", "lazy"); });
      strip.appendChild(clone);
    });

    if (still) return;                             // motion off → leave it parked

    var paused = false;
    var last = null;
    var carry = 0;                                 // sub-pixel remainder

    var pause = function () { paused = true; };
    var play  = function () { paused = false; last = null; };

    strip.addEventListener("mouseenter", pause);
    strip.addEventListener("mouseleave", play);
    strip.addEventListener("touchstart", pause, { passive: true });
    strip.addEventListener("touchend", play, { passive: true });
    strip.addEventListener("focusin", pause);
    strip.addEventListener("focusout", play);

    function step(now) {
      requestAnimationFrame(step);

      /* Skip while hidden, paused, or on the very first frame. */
      if (paused || document.hidden || strip.offsetParent === null) { last = now; return; }
      if (last === null) { last = now; return; }

      var dt = (now - last) / 1000;
      last = now;
      if (dt > 0.25) return;                       // came back from a background tab

      var half = strip.scrollWidth / 2;            // width of the originals
      if (half < 1) return;

      carry += SPEED * dt;
      var move = Math.floor(carry);                // scrollLeft only takes whole pixels
      if (move < 1) return;
      carry -= move;

      var next = strip.scrollLeft + move;
      /* Past the originals? Rewind by exactly their width — looks continuous. */
      strip.scrollLeft = next >= half ? next - half : next;
    }

    requestAnimationFrame(step);
  }

  function init() {
    document.querySelectorAll(STRIPS).forEach(setup);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
