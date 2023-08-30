from rest_framework import serializers

from .models import (
    Domain, 
    Phylum, 
    Class, 
    Order, 
    Family, 
    Genus, 
    Species
    )
                
class SpeciesSerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    class Meta:
        model = Species
        fields = '__all__'

class GenusSerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    species = SpeciesSerializer(many=True)
    class Meta:
        model = Genus
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    genera = GenusSerializer(many=True)
    class Meta:
        model = Family
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    families = FamilySerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    orders = OrderSerializer(many=True)
    class Meta:
        model = Class
        fields = '__all__'

class PhylumSerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source='parent.name', read_only=True)
    classes = ClassSerializer(many=True)
    class Meta:
        model = Phylum
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    phyla = PhylumSerializer(many=True)
    class Meta:
        model = Domain
        fields = '__all__'