from rest_framework import routers
from .api import StartupsViewSet,InvestorsViewSet,MentorsViewSet

router = routers.DefaultRouter()
router.register('api/startups', StartupsViewSet, 'Startups')
router.register('api/investors', InvestorsViewSet, 'Investors')
router.register('api/mentors', MentorsViewSet, 'Mentors')

urlpatterns = router.urls