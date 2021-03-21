from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import JobOffer, Industry, Region
from . import serializers


class BaseJobOfferViewSet(viewsets.GenericViewSet, \
    mixins.ListModelMixin, mixins.CreateModelMixin):
    """Viewset for job from user"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current auth user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned.only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(joboffers__isnull=False)
        
        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class IndustryViewSet(BaseJobOfferViewSet):
    """Manage industry in the database"""
    queryset = Industry.objects.all()
    serializer_class = serializers.IndustrySerializer


class RegionViewSet(BaseJobOfferViewSet):
    """Manage region in the database"""
    queryset = Region.objects.all()
    serializer_class = serializers.RegionSerializer


class JobOfferViewSet(viewsets.ModelViewSet):
    """Manage job offers in the database"""
    serializer_class = serializers.JobOfferSerializer
    queryset = JobOffer.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the job offers for the auth user"""
        industries = self.request.query_params.get('industries')
        regions = self.request.query_params.get('regions')
        queryset = self.queryset
        if industries:
            industry_ids = self._params_to_ints(industries)
            queryset = queryset.filter(industries__id__in=industry_ids)
        if regions:
            region_ids = self._params_to_ints(regions)
            queryset = queryset.filter(regions__id__in=region_ids)

        return queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        """Return appropriate serializer"""
        if self.action == 'retrieve':
            return serializers.JobOfferDetailSerializer
        
        return self.serializer_class
    
    def perform_create(self, serilaizer):
        """Create a new job offer"""
        serilaizer.save(user=self.request.user)
