from rest_framework.routers import SimpleRouter
from data_center.views import InvoiceViewSet, QuotationViewSet

router = SimpleRouter()
router.register("invoices", InvoiceViewSet)
router.register("quotations", QuotationViewSet)

urlpatterns = router.urls
