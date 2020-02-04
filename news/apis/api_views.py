from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from news.apis.serializers import CategoryListSerializer, NewsSerializer
from django.utils.text import slugify
from rest_framework_simplejwt.authentication import JWTAuthentication

class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class NewsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class NewsRetriveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class NewsCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = NewsSerializer
    # model = serializer_class.Meta.model
    # queryset = model.objects.all()

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data["title"]
        slug = slugify(title)
        author = self.request.user
        serializer.save(author=author, slug=slug)
        return serializer