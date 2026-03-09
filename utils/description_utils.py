"""
╔══════════════════════════════════════════════════════════════════════╗
║              description_utils.py  — UI Test Element Inspector       ║
║              Selenium tabanlı gelişmiş element analiz aracı          ║
╚══════════════════════════════════════════════════════════════════════╝

Kullanım:
    description_utils(driver, locator, highlight_colour="#FFD700", circle_colour="#FF4500")
"""

import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementNotVisibleException,
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)


# ──────────────────────────────────────────────────────────────────────
#  ANSI Renk Kodları (Konsol çıktısı için)
# ──────────────────────────────────────────────────────────────────────
class _C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    BG_DARK = "\033[40m"


def _banner(text: str, colour=_C.CYAN):
    width = 68
    print(f"\n{colour}{_C.BOLD}{'═' * width}{_C.RESET}")
    print(f"{colour}{_C.BOLD}  {text}{_C.RESET}")
    print(f"{colour}{_C.BOLD}{'═' * width}{_C.RESET}")


def _section(title: str):
    print(f"\n{_C.YELLOW}{_C.BOLD}  ▶  {title}{_C.RESET}")
    print(f"{_C.DIM}  {'─' * 60}{_C.RESET}")


def _ok(msg: str):
    print(f"  {_C.GREEN}✔  {msg}{_C.RESET}")


def _fail(msg: str):
    print(f"  {_C.RED}✘  {msg}{_C.RESET}")


def _info(label: str, value):
    print(f"  {_C.CYAN}{label:<28}{_C.RESET}{_C.WHITE}{value}{_C.RESET}")


def _warn(msg: str):
    print(f"  {_C.YELLOW}⚠  {msg}{_C.RESET}")


# ══════════════════════════════════════════════════════════════════════
#  ANA FONKSİYON
# ══════════════════════════════════════════════════════════════════════
def description_utils(
    driver,
    locator,
    highlight_colour: str = "#FFD700",
    circle_colour:    str = "#FF4500",
    hover:            bool = True,
    scroll:           bool = True,
    wait_timeout:     int  = 10,
):
    """
    Parameters
    ----------
    driver           : Selenium WebDriver instance
    locator          : WebElement  VEYA  (By.XX, "değer") tuple'ı
    highlight_colour : Element çerçeve rengi   (ör. "#FFD700", "red")
    circle_colour    : Animasyon dairesi rengi (ör. "#FF4500", "blue")
    hover            : True ise ActionChains hover yapılır
    scroll           : True ise element görünür olana kadar scroll edilir
    wait_timeout     : Element bekleme süresi (saniye)
    """

    _banner("🔍  ELEMENT INSPECTOR  —  description_utils", _C.MAGENTA)

    # ── 0. Elementi çöz ──────────────────────────────────────────────
    element = _resolve_element(driver, locator, wait_timeout)
    if element is None:
        _fail("Element bulunamadı veya zaman aşımına uğradı. İşlem durduruldu.")
        return

    # ── 1. Scroll ────────────────────────────────────────────────────
    if scroll:
        _do_scroll(driver, element)

    # ── 2. Hover ─────────────────────────────────────────────────────
    if hover:
        _do_hover(driver, element)

    # ── 3. Highlight ─────────────────────────────────────────────────
    _do_highlight(driver, element, highlight_colour)

    # ── 4. Dairesel Animasyon ─────────────────────────────────────────
    _do_circle_animation(driver, element, circle_colour, repeat=3)

    # ── 5. "İnsan gözü ile analiz" efekti ────────────────────────────
    _human_scan_effect(driver, element, highlight_colour)

    # ── 6. Tıklanabilirlik / Görünürlük / Yazılabilirlik ──────────────
    props = _test_interactions(driver, element)

    # ── 7. Tip tespiti ────────────────────────────────────────────────
    el_type = _detect_type(element)

    # ── 8. Locator kombinasyonları ────────────────────────────────────
    locators = _generate_locators(driver, element)

    # ── 9. Koordinatlar ───────────────────────────────────────────────
    coords = _get_coordinates(element)

    # ── 10. Sayfa URL ─────────────────────────────────────────────────
    page_url = driver.current_url

    # ── 11. Link bilgisi ──────────────────────────────────────────────
    link_target = _get_link_target(driver, element, el_type)

    # ── 12. Ekstra özellikler ─────────────────────────────────────────
    extras = _extra_properties(driver, element)

    # ══ SONUÇ RAPORU ══════════════════════════════════════════════════
    _print_report(
        element, el_type, props, locators,
        coords, page_url, link_target, extras,
        highlight_colour, circle_colour,
    )

    # Highlight kaldır (temiz bırak)
    _remove_highlight(driver, element)

    _banner("✅  ANALİZ TAMAMLANDI", _C.GREEN)
    return {
        "element":      element,
        "type":         el_type,
        "properties":   props,
        "locators":     locators,
        "coordinates":  coords,
        "page_url":     page_url,
        "link_target":  link_target,
        "extras":       extras,
    }


# ══════════════════════════════════════════════════════════════════════
#  YARDIMCI FONKSİYONLAR
# ══════════════════════════════════════════════════════════════════════

# ── 0. Element Çözümleme ─────────────────────────────────────────────
def _resolve_element(driver, locator, timeout):
    """WebElement veya (By, value) tuple kabul eder."""
    try:
        from selenium.webdriver.remote.webelement import WebElement
        if isinstance(locator, WebElement):
            _ok("Locator: Doğrudan WebElement alındı.")
            return locator
        if isinstance(locator, tuple) and len(locator) == 2:
            by, value = locator
            _ok(f"Locator: ({by}, '{value}') bekleniyor...")
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            _ok("Element DOM'da bulundu.")
            return element
        _fail(f"Geçersiz locator formatı: {type(locator)}")
        return None
    except TimeoutException:
        _fail(f"Timeout ({timeout}s): Element bulunamadı → {locator}")
        return None
    except Exception as e:
        _fail(f"Element çözümlenirken hata: {e}")
        return None


# ── 1. Scroll ────────────────────────────────────────────────────────
def _do_scroll(driver, element):
    _section("Scroll İşlemi")
    try:
        # Önce elementin görünür olup olmadığını kontrol et
        rect = driver.execute_script(
            "const r = arguments[0].getBoundingClientRect();"
            "return {top: r.top, bottom: r.bottom, "
            "vh: window.innerHeight};",
            element,
        )
        in_view = 0 <= rect["top"] and rect["bottom"] <= rect["vh"]
        if not in_view:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior:'smooth',"
                "block:'center',inline:'center'});",
                element,
            )
            time.sleep(0.6)
            _ok("Element görünür alana smooth-scroll ile getirildi.")
        else:
            _ok("Element zaten görünür alanda, scroll gerekmedi.")
    except Exception as e:
        _warn(f"Scroll sırasında hata: {e}")


# ── 2. Hover ─────────────────────────────────────────────────────────
def _do_hover(driver, element):
    _section("Hover İşlemi")
    try:
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(0.4)
        _ok("Hover uygulandı (ActionChains).")
    except Exception as e:
        _warn(f"Hover sırasında hata: {e}")


# ── 3. Highlight ─────────────────────────────────────────────────────
_ORIGINAL_STYLE_KEY = "__desc_original_style__"


def _do_highlight(driver, element, colour, border_px=3, duration=0.8):
    _section(f"Highlight  [{colour}]")
    try:
        original = element.get_attribute("style") or ""
        driver.execute_script(
            f"arguments[0].setAttribute('{_ORIGINAL_STYLE_KEY}', arguments[1]);",
            element, original,
        )
        driver.execute_script(
            "arguments[0].style.outline = arguments[1];"
            "arguments[0].style.outlineOffset = '2px';"
            "arguments[0].style.transition = 'outline 0.2s ease';",
            element,
            f"{border_px}px solid {colour}",
        )
        time.sleep(duration)
        _ok(f"Element {border_px}px {colour} çerçeve ile işaretlendi.")
    except Exception as e:
        _warn(f"Highlight sırasında hata: {e}")


def _remove_highlight(driver, element):
    try:
        original = driver.execute_script(
            f"return arguments[0].getAttribute('{_ORIGINAL_STYLE_KEY}');",
            element,
        )
        if original is not None:
            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);"
                f"arguments[0].removeAttribute('{_ORIGINAL_STYLE_KEY}');",
                element, original,
            )
    except Exception:
        pass


# ── 4. Dairesel Animasyon ─────────────────────────────────────────────
def _do_circle_animation(driver, element, colour, repeat=3):
    _section(f"Dairesel Animasyon  [{colour}]  ×{repeat}")
    js_animation = """
    (function(el, colour, repeat) {
        var rect  = el.getBoundingClientRect();
        var scrollX = window.scrollX || window.pageXOffset;
        var scrollY = window.scrollY || window.pageYOffset;
        var cx = rect.left + scrollX;
        var cy = rect.top  + scrollY + rect.height / 2;
        var W  = rect.width;

        var circle = document.createElement('div');
        circle.id  = '__desc_circle__';
        Object.assign(circle.style, {
            position:     'absolute',
            width:        '24px',
            height:       '24px',
            borderRadius: '50%',
            background:   colour,
            opacity:      '0.85',
            zIndex:       '999999',
            pointerEvents:'none',
            boxShadow:    '0 0 8px 3px ' + colour,
            top:  (cy - 12) + 'px',
            left: (cx - 12) + 'px',
            transition:   'none',
        });
        document.body.appendChild(circle);

        var step   = 0;
        var steps  = 40;
        var delay  = 18;    // ms per step  → ~720ms per sweep
        var run    = 0;

        function sweep() {
            if (run >= repeat) {
                circle.remove();
                return;
            }
            if (step <= steps) {
                var progress = step / steps;
                // Yavaş başla, orta hızlan, sona doğru yavaşla (ease)
                var eased    = 0.5 - Math.cos(Math.PI * progress) / 2;
                var x        = cx + eased * W;
                var bounce   = Math.sin(Math.PI * progress) * 8;
                circle.style.left = (x - 12) + 'px';
                circle.style.top  = (cy - 12 - bounce) + 'px';
                step++;
                setTimeout(sweep, delay);
            } else {
                step = 0;
                run++;
                // Kısa paus sonra tekrar
                setTimeout(sweep, 120);
            }
        }
        sweep();
    })(arguments[0], arguments[1], arguments[2]);
    """
    try:
        driver.execute_script(js_animation, element, colour, repeat)
        # Animasyonun bitmesini bekle: repeat * (steps*delay + 120ms pause)
        wait_time = repeat * (40 * 0.018 + 0.15) + 0.3
        time.sleep(wait_time)
        _ok(f"Dairesel animasyon {repeat}× tamamlandı.")
    except Exception as e:
        _warn(f"Animasyon sırasında hata: {e}")


# ── 5. İnsan-gözü tarama efekti ──────────────────────────────────────
def _human_scan_effect(driver, element, colour):
    _section("İnsan Gözü Tarama Efekti")
    js_scan = """
    (function(el, colour) {
        var rect = el.getBoundingClientRect();
        var scrollX = window.scrollX || window.pageXOffset;
        var scrollY = window.scrollY || window.pageYOffset;

        // Tarama çizgisi
        var line = document.createElement('div');
        line.id  = '__desc_scanline__';
        Object.assign(line.style, {
            position:   'absolute',
            width:      '2px',
            height:     rect.height + 'px',
            background: 'linear-gradient(to bottom, transparent, '
                        + colour + ', transparent)',
            opacity:    '0.9',
            zIndex:     '999998',
            pointerEvents: 'none',
            top:  (rect.top  + scrollY) + 'px',
            left: (rect.left + scrollX) + 'px',
            transition: 'left 0.05s linear',
        });
        document.body.appendChild(line);

        // Vurgulanan alanı gösteren yarı-şeffaf kutu
        var box = document.createElement('div');
        Object.assign(box.style, {
            position:   'absolute',
            width:      rect.width  + 'px',
            height:     rect.height + 'px',
            background: colour,
            opacity:    '0',
            zIndex:     '999997',
            pointerEvents: 'none',
            top:  (rect.top  + scrollY) + 'px',
            left: (rect.left + scrollX) + 'px',
            transition: 'opacity 0.3s ease',
        });
        document.body.appendChild(box);

        var steps = 30;
        var step  = 0;
        var W     = rect.width;

        function scan() {
            if (step <= steps) {
                var x = rect.left + scrollX + (step / steps) * W;
                line.style.left    = x + 'px';
                box.style.opacity  = String(0.08 * Math.sin(Math.PI * step / steps));
                step++;
                setTimeout(scan, 20);
            } else {
                // Flaş efekti
                box.style.opacity = '0.18';
                setTimeout(function() {
                    box.style.opacity = '0';
                    setTimeout(function() {
                        line.remove();
                        box.remove();
                    }, 300);
                }, 250);
            }
        }
        scan();
    })(arguments[0], arguments[1]);
    """
    try:
        driver.execute_script(js_scan, element, colour)
        time.sleep(1.2)
        _ok("Tarama efekti tamamlandı.")
    except Exception as e:
        _warn(f"Tarama efekti sırasında hata: {e}")


# ── 6. Etkileşim Testleri ────────────────────────────────────────────
def _test_interactions(driver, element) -> dict:
    _section("Etkileşim Testleri")
    results = {}

    # Görünürlük
    try:
        visible = element.is_displayed()
        results["visible"] = visible
        (_ok if visible else _fail)(f"Görünürlük  (is_displayed)   → {visible}")
    except Exception as e:
        results["visible"] = False
        _fail(f"Görünürlük testi hata: {e}")

    # Etkinlik (enabled)
    try:
        enabled = element.is_enabled()
        results["enabled"] = enabled
        (_ok if enabled else _fail)(f"Etkinlik    (is_enabled)     → {enabled}")
    except Exception as e:
        results["enabled"] = False
        _fail(f"Etkinlik testi hata: {e}")

    # Seçilmiş mi (checkbox/radio için)
    try:
        selected = element.is_selected()
        results["selected"] = selected
        _info("Seçili      (is_selected)   →", selected)
    except Exception as e:
        results["selected"] = None

    # Tıklanabilirlik
    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(element)
        )
        results["clickable"] = True
        _ok(f"Tıklanabilir (EC.clickable)  → True")
    except Exception:
        results["clickable"] = False
        _fail(f"Tıklanabilir (EC.clickable)  → False")

    # Yazılabilirlik
    tag   = (element.tag_name or "").lower()
    itype = (element.get_attribute("type") or "").lower()
    readonly  = element.get_attribute("readonly")
    disabled  = element.get_attribute("disabled")
    writable_tags   = {"input", "textarea"}
    writable_types  = {
        "text", "email", "password", "number", "search",
        "tel", "url", "date", "time", "datetime-local",
        "month", "week", "color", "", None,
    }
    is_writable = (
        tag in writable_tags
        and itype in writable_types
        and readonly is None
        and disabled is None
    )
    results["writable"] = is_writable
    (_ok if is_writable else _info)(
        "Yazılabilir (writable)       →", is_writable
    )

    # CSS pointer-events
    try:
        ptr = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).pointerEvents;",
            element,
        )
        results["pointer_events"] = ptr
        colour = _C.GREEN if ptr != "none" else _C.RED
        print(f"  {colour}{'CSS pointer-events':<28}{_C.RESET}{_C.WHITE}{ptr}{_C.RESET}")
    except Exception:
        results["pointer_events"] = "unknown"

    # Opacity / z-index
    try:
        opacity = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).opacity;",
            element,
        )
        zindex = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).zIndex;",
            element,
        )
        results["opacity"] = opacity
        results["z_index"] = zindex
        _info("CSS opacity              →", opacity)
        _info("CSS z-index              →", zindex)
    except Exception:
        pass

    return results


# ── 7. Tip Tespiti ────────────────────────────────────────────────────
def _detect_type(element) -> str:
    _section("Element Tip Tespiti")
    tag   = (element.tag_name or "").lower()
    itype = (element.get_attribute("type") or "").lower()
    role  = (element.get_attribute("role") or "").lower()

    button_tags  = {"button", "a"}
    button_types = {"button", "submit", "reset", "image"}
    button_roles = {"button", "link", "menuitem", "tab"}
    input_tags   = {"input", "textarea", "select"}
    input_types  = {
        "text", "email", "password", "number", "search",
        "tel", "url", "date", "time", "datetime-local",
        "month", "week", "color",
    }

    if (tag in button_tags
            or itype in button_types
            or role  in button_roles):
        label = "BUTTON / Tıklanabilir Element"
        colour = _C.BLUE
    elif tag in input_tags or itype in input_types:
        label = "INPUT / Yazma Kutusu"
        colour = _C.MAGENTA
    elif tag in {"select"}:
        label = "SELECT / Açılır Menü"
        colour = _C.CYAN
    elif tag in {"img", "svg", "canvas"}:
        label = "MEDIA / Görsel Element"
        colour = _C.YELLOW
    elif tag in {"form"}:
        label = "FORM"
        colour = _C.GREEN
    else:
        label = f"DİĞER  ({tag})"
        colour = _C.WHITE

    print(f"\n  {colour}{_C.BOLD}  ┌─ ELEMENT TİPİ ──────────────────────────────┐")
    print(f"  │  {label:<44}│")
    print(f"  │  tag={tag!r:12}  type={itype!r:12}  role={role!r}  │")
    print(f"  └─────────────────────────────────────────────┘{_C.RESET}")
    return label


# ── 8. Locator Kombinasyonları ────────────────────────────────────────
def _generate_locators(driver, element) -> list:
    _section("Locator Kombinasyonları (Güçlüden → Zayıfa)")
    locators = []

    def _add(strength, by_name, value, unique=None):
        locators.append({
            "strength": strength,
            "by":       by_name,
            "value":    value,
            "unique":   unique,
        })

    # 1. data-testid / data-cy / data-qa
    for attr in ("data-testid", "data-cy", "data-qa", "data-test", "data-id"):
        val = element.get_attribute(attr)
        if val:
            css = f'[{attr}="{val}"]'
            _add(10, f"CSS[{attr}]", css, _is_unique(driver, By.CSS_SELECTOR, css))

    # 2. ID
    el_id = element.get_attribute("id")
    if el_id:
        _add(9, "ID", el_id, _is_unique(driver, By.ID, el_id))
        _add(9, "CSS #id", f"#{el_id}", _is_unique(driver, By.CSS_SELECTOR, f"#{el_id}"))

    # 3. Name
    name = element.get_attribute("name")
    if name:
        css_name = f'[name="{name}"]'
        _add(8, "NAME", name, _is_unique(driver, By.NAME, name))
        _add(8, "CSS[name]", css_name, _is_unique(driver, By.CSS_SELECTOR, css_name))

    # 4. aria-label / aria-labelledby
    for attr in ("aria-label", "aria-labelledby", "aria-describedby"):
        val = element.get_attribute(attr)
        if val:
            css = f'[{attr}="{val}"]'
            _add(7, f"CSS[{attr}]", css, _is_unique(driver, By.CSS_SELECTOR, css))

    # 5. Placeholder
    placeholder = element.get_attribute("placeholder")
    if placeholder:
        css_ph = f'[placeholder="{placeholder}"]'
        xpath_ph = f'//*[@placeholder="{placeholder}"]'
        _add(6, "CSS[placeholder]", css_ph,
             _is_unique(driver, By.CSS_SELECTOR, css_ph))
        _add(6, "XPATH[@placeholder]", xpath_ph,
             _is_unique(driver, By.XPATH, xpath_ph))

    # 6. Link text (a etiketi için)
    if element.tag_name.lower() == "a":
        try:
            text = element.text.strip()
            if text:
                _add(5, "LINK_TEXT", text,
                     _is_unique(driver, By.LINK_TEXT, text))
                _add(5, "PARTIAL_LINK_TEXT",
                     text[:min(20, len(text))],
                     None)
        except Exception:
            pass

    # 7. Text içeriği XPath
    try:
        text = element.text.strip()
        if text and len(text) <= 80:
            safe = text.replace('"', "'")
            xpath_text = f'//*[normalize-space(text())="{safe}"]'
            _add(5, "XPATH[text()]", xpath_text,
                 _is_unique(driver, By.XPATH, xpath_text))
    except Exception:
        pass

    # 8. tag + class kombinasyonu
    try:
        tag    = element.tag_name.lower()
        cls    = element.get_attribute("class") or ""
        # İlk anlamlı class
        cls_parts = [c for c in cls.split() if c and len(c) > 1
                     and not re.match(r'^[0-9_-]', c)]
        if cls_parts:
            css_cls = f'{tag}.{".".join(cls_parts[:3])}'
            _add(4, "CSS tag.class", css_cls,
                 _is_unique(driver, By.CSS_SELECTOR, css_cls))
    except Exception:
        pass

    # 9. XPath mutlak
    try:
        xpath_abs = driver.execute_script("""
            function getXPath(el) {
                if (el.id) return '//*[@id="' + el.id + '"]';
                if (el === document.body) return '/html/body';
                var ix = 0;
                var siblings = el.parentNode ? el.parentNode.childNodes : [];
                for (var i = 0; i < siblings.length; i++) {
                    var sib = siblings[i];
                    if (sib === el) {
                        var p = getXPath(el.parentNode);
                        return p + '/' + el.tagName.toLowerCase()
                               + '[' + (ix + 1) + ']';
                    }
                    if (sib.nodeType === 1
                            && sib.tagName === el.tagName) ix++;
                }
            }
            return getXPath(arguments[0]);
        """, element)
        if xpath_abs:
            _add(2, "XPATH Mutlak", xpath_abs,
                 _is_unique(driver, By.XPATH, xpath_abs))
    except Exception:
        pass

    # 10. CSS Selector (tam yol)
    try:
        css_full = driver.execute_script("""
            function getCSS(el) {
                if (el.id) return '#' + el.id;
                var path = [];
                while (el && el.nodeType === 1) {
                    var sel = el.nodeName.toLowerCase();
                    if (el.id) { sel = '#' + el.id; path.unshift(sel); break; }
                    var sib = el, nth = 1;
                    while ((sib = sib.previousElementSibling))
                        if (sib.nodeName === el.nodeName) nth++;
                    if (nth !== 1) sel += ':nth-of-type(' + nth + ')';
                    path.unshift(sel);
                    el = el.parentElement;
                }
                return path.join(' > ');
            }
            return getCSS(arguments[0]);
        """, element)
        if css_full:
            _add(1, "CSS Tam Yol", css_full,
                 _is_unique(driver, By.CSS_SELECTOR, css_full))
    except Exception:
        pass

    # Sıralama ve yazdırma
    locators.sort(key=lambda x: x["strength"], reverse=True)
    strength_labels = {
        10: "★★★★★ (MÜKEMMEL)",
        9:  "★★★★☆ (ÇOK GÜÇLÜ)",
        8:  "★★★★☆ (GÜÇLÜ)",
        7:  "★★★☆☆ (İYİ)",
        6:  "★★★☆☆ (ORTA-İYİ)",
        5:  "★★★☆☆ (ORTA)",
        4:  "★★☆☆☆ (ZAYIF)",
        3:  "★★☆☆☆ (ZAYIF)",
        2:  "★☆☆☆☆ (ÇOK ZAYIF)",
        1:  "☆☆☆☆☆ (KÖTÜ)",
    }
    for i, loc in enumerate(locators, 1):
        sl = strength_labels.get(loc["strength"], "?")
        u  = "✔ Tekil" if loc["unique"] is True  else \
             "✘ Tekil Değil" if loc["unique"] is False else "?"
        print(f"  {_C.CYAN}{i:2}. [{sl}]{_C.RESET}  "
              f"{_C.YELLOW}{loc['by']:<22}{_C.RESET}"
              f"{_C.WHITE}{loc['value'][:70]}{_C.RESET}"
              f"  {_C.DIM}[{u}]{_C.RESET}")
    return locators


def _is_unique(driver, by, value) -> bool:
    try:
        els = driver.find_elements(by, value)
        return len(els) == 1
    except Exception:
        return None


# ── 9. Koordinatlar ───────────────────────────────────────────────────
def _get_coordinates(element) -> dict:
    _section("Element Koordinatları")
    try:
        loc  = element.location
        size = element.size
        x1, y1 = loc["x"],           loc["y"]
        x2, y2 = loc["x"] + size["width"], loc["y"]
        x3, y3 = loc["x"] + size["width"], loc["y"] + size["height"]
        x4, y4 = loc["x"],           loc["y"] + size["height"]
        cx     = loc["x"] + size["width"]  // 2
        cy     = loc["y"] + size["height"] // 2
        coords = {
            "top_left":     (x1, y1),
            "top_right":    (x2, y2),
            "bottom_right": (x3, y3),
            "bottom_left":  (x4, y4),
            "center":       (cx, cy),
            "width":        size["width"],
            "height":       size["height"],
        }
        print(f"  {_C.CYAN}Sol Üst   (x1,y1){_C.RESET}  → {_C.WHITE}({x1}, {y1}){_C.RESET}")
        print(f"  {_C.CYAN}Sağ Üst   (x2,y2){_C.RESET}  → {_C.WHITE}({x2}, {y2}){_C.RESET}")
        print(f"  {_C.CYAN}Sağ Alt   (x3,y3){_C.RESET}  → {_C.WHITE}({x3}, {y3}){_C.RESET}")
        print(f"  {_C.CYAN}Sol Alt   (x4,y4){_C.RESET}  → {_C.WHITE}({x4}, {y4}){_C.RESET}")
        print(f"  {_C.CYAN}Merkez    (cx,cy){_C.RESET}  → {_C.WHITE}({cx}, {cy}){_C.RESET}")
        print(f"  {_C.CYAN}Boyut     W×H    {_C.RESET}  → "
              f"{_C.WHITE}{size['width']}×{size['height']} px{_C.RESET}")
        return coords
    except Exception as e:
        _warn(f"Koordinat alınamadı: {e}")
        return {}


# ── 11. Link Hedefi ──────────────────────────────────────────────────
def _get_link_target(driver, element, el_type) -> str | None:
    _section("Link / Yönlendirme Bilgisi")
    try:
        tag  = element.tag_name.lower()
        href = element.get_attribute("href")
        onclick = element.get_attribute("onclick") or ""
        data_href = element.get_attribute("data-href") or \
                    element.get_attribute("data-url") or ""

        # <a> linki
        if href:
            _ok(f"href  → {href}")
            return href

        # onclick içinde URL
        match = re.search(
            r"(?:window\.location|location\.href)\s*=\s*['\"]([^'\"]+)['\"]",
            onclick,
        )
        if match:
            _ok(f"onclick URL → {match.group(1)}")
            return match.group(1)

        # data-href
        if data_href:
            _ok(f"data-href → {data_href}")
            return data_href

        # form action (submit button)
        try:
            form = element.find_element(By.XPATH, "ancestor::form[1]")
            action = form.get_attribute("action")
            if action:
                _info("Form action        →", action)
                return action
        except Exception:
            pass

        _info("Link hedefi        →", "YOK / Bulunamadı")
        return None
    except Exception as e:
        _warn(f"Link bilgisi alınamadı: {e}")
        return None


# ── 12. Ekstra Özellikler ─────────────────────────────────────────────
def _extra_properties(driver, element) -> dict:
    _section("Ekstra Element Özellikleri")
    extras = {}

    # DOM nitelikleri
    attrs_to_check = [
        "class", "style", "title", "tabindex",
        "autocomplete", "autofocus", "required",
        "maxlength", "minlength", "pattern",
        "min", "max", "step", "accept",
        "multiple", "form", "formaction",
        "target", "rel", "download",
    ]
    for attr in attrs_to_check:
        val = element.get_attribute(attr)
        if val:
            extras[attr] = val
            _info(attr, val[:80])

    # İç metin
    try:
        text = element.text.strip()
        inner_html = driver.execute_script(
            "return arguments[0].innerHTML;", element
        )
        inner_text = driver.execute_script(
            "return arguments[0].innerText;", element
        )
        if text:
            extras["text"] = text
            _info("Görünen Metin", text[:80])
        if inner_html:
            extras["innerHTML_length"] = len(inner_html)
            _info("innerHTML uzunluğu", f"{len(inner_html)} karakter")
    except Exception:
        pass

    # Computed style — önemli CSS özellikleri
    important_css = [
        "display", "visibility", "position",
        "cursor", "overflow", "background-color",
        "color", "font-size", "border",
    ]
    css_vals = {}
    for prop in important_css:
        try:
            val = driver.execute_script(
                f"return window.getComputedStyle(arguments[0])"
                f"['{prop}'];",
                element,
            )
            if val and val not in ("", "none", "auto", "normal", "0px"):
                css_vals[prop] = val
                _info(f"CSS {prop}", val[:60])
        except Exception:
            pass
    extras["computed_css"] = css_vals

    # Shadow DOM kontrolü
    try:
        shadow = driver.execute_script(
            "return arguments[0].shadowRoot;", element
        )
        extras["has_shadow_dom"] = shadow is not None
        if shadow:
            _warn("⚡ Shadow DOM mevcut! Locator çalışmayabilir.")
        else:
            _info("Shadow DOM", "Yok")
    except Exception:
        pass

    # iframe içinde mi?
    try:
        in_iframe = driver.execute_script(
            "return window.self !== window.top;",
        )
        extras["in_iframe"] = in_iframe
        if in_iframe:
            _warn("⚡ Element bir iframe içinde!")
        else:
            _info("iframe içinde", "Hayır")
    except Exception:
        pass

    # DOM derinliği
    try:
        depth = driver.execute_script("""
            var d = 0, el = arguments[0];
            while (el.parentElement) { d++; el = el.parentElement; }
            return d;
        """, element)
        extras["dom_depth"] = depth
        _info("DOM Derinliği", depth)
    except Exception:
        pass

    # Çocuk element sayısı
    try:
        children = driver.execute_script(
            "return arguments[0].children.length;", element
        )
        extras["children_count"] = children
        _info("Çocuk Element Sayısı", children)
    except Exception:
        pass

    # Accessibility
    try:
        role  = element.get_attribute("role")       or ""
        label = element.get_attribute("aria-label") or ""
        if role:
            _info("ARIA role", role)
        if label:
            _info("ARIA label", label)
        extras["aria_role"]  = role
        extras["aria_label"] = label
    except Exception:
        pass

    return extras


# ── ÖZET RAPOR ────────────────────────────────────────────────────────
def _print_report(
    element, el_type, props, locators,
    coords, page_url, link_target, extras,
    highlight_colour, circle_colour,
):
    _banner("📋  ÖZET RAPOR", _C.MAGENTA)

    _info("Element Tipi       ", el_type)
    _info("Sayfa URL          ", page_url)
    _info("Görünür            ", "✔" if props.get("visible")   else "✘")
    _info("Etkin              ", "✔" if props.get("enabled")   else "✘")
    _info("Tıklanabilir       ", "✔" if props.get("clickable") else "✘")
    _info("Yazılabilir        ", "✔" if props.get("writable")  else "✘")

    if coords:
        _info(
            "Koordinatlar       ",
            f"(x1,y1)={coords.get('top_left')}  "
            f"(x2,y2)={coords.get('top_right')}  "
            f"(x3,y3)={coords.get('bottom_right')}  "
            f"(x4,y4)={coords.get('bottom_left')}",
        )
        _info("Boyut              ",
              f"{coords.get('width')}×{coords.get('height')} px")

    if link_target:
        _info("Hedef Link         ", link_target)
    else:
        _info("Hedef Link         ", "—")

    _info("Highlight Rengi    ", highlight_colour)
    _info("Daire Rengi        ", circle_colour)

    if locators:
        best = locators[0]
        _info(
            "En İyi Locator     ",
            f"{best['by']} → {best['value'][:60]}",
        )

    if extras.get("has_shadow_dom"):
        _warn("Shadow DOM tespit edildi!")
    if extras.get("in_iframe"):
        _warn("Element iframe içinde!")


# ══════════════════════════════════════════════════════════════════════
#  DOĞRUDAN ÇAĞRI ÖRNEĞİ
# ══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    """
    Örnek kullanım:

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from description_utils import description_utils

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # (By, value) tuple ile:
    result = description_utils(
        driver,
        locator=(By.ID, "content"),
        highlight_colour="#00BFFF",
        circle_colour="#FF6347",
    )

    # WebElement ile:
    el = driver.find_element(By.NAME, "q")
    result = description_utils(driver, el, "#FFD700", "#32CD32")

    driver.quit()
    """
    print("description_utils.py hazır. Yukarıdaki örnek kullanımı inceleyin.")
