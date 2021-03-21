from rest_framework import serializers
from core.models import JobOffer, Industry, Region


class IndustrySerializer(serializers.ModelSerializer):
    """Serializer for industry"""
    class Meta:
        model = Industry
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RegionSerializer(serializers.ModelSerializer):
    """Serializer for region"""
    class Meta:
        model = Region
        fields = ('id', 'name')
        read_only_fields = ('id',)


class JobOfferSerializer(serializers.ModelSerializer):
    """Serializer for Job Offers"""
    industries = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Industry.objects.all()
    )
    regions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Region.objects.all()
    )
    class Meta:
        model = JobOffer
        fields = (
            'id', 'title', 'regions', 'industries', 'position', 'created', 'contract', 'salary', \
                'level_of_degree', 'more_details'
        )
        read_only_fields = ('id', 'created')


class JobOfferDetailSerializer(JobOfferSerializer):
    """Serializer for Job Offer details"""
    industry = IndustrySerializer(many=True, read_only=True)
    region = RegionSerializer(many=True, read_only=True)
