from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			# La méthode est une méthode sûre
			return True
		else:
			# La méthode n'est pas une méthode sûre
			# Seuls les propriétaires reçoivent des autorisations pour les méthodes dangereuses
			return obj.owner == request.user
