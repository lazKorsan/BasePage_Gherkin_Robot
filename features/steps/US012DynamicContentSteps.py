from behave import given, then
from pages.DynamicContentPage import DynamicContentPage

# 'given' yerine 'when' veya 'and' daha anlamlı olabilir ama mevcut yapıyı bozmuyorum.
@given(u'Navigate Dynamic Content Page')
def step_impl(context):
    # Her senaryo için yeni bir sayfa nesnesi oluşturmak daha güvenli olabilir.
    # Bu, context'in testler arasında kirlenmesini önler.
    context.dynamic_content_page = DynamicContentPage()
    context.dynamic_content_page.navigate_dynamic_content()


# Bu adımı 'then' olarak değiştirmek BDD prensiplerine daha uygun olur.
@given(u'Verify Dynamic Content Changed')
def step_impl(context):
    """
    Sayfa içeriğinin değişip değişmediğini doğrular ve BDD adımını buna göre
    başarılı veya başarısız yapar.
    """
    is_content_changed = context.dynamic_content_page.verify_dynamic_content_changed()
    
    # assert, testin sonucunu belirler.
    # Eğer is_content_changed False ise, test bu adımda kalacaktır.
    assert is_content_changed, "Dinamik içerik beklendiği gibi değişmedi!"
