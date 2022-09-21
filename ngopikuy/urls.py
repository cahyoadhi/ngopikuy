from django.urls import path
from . import views

# url routing
urlpatterns = [
    path('',views.HomePage,name="homepage"),
    path('about/',views.AboutPage,name="about"),
    path('contact/',views.ContactPage,name="contact"),
    path('login/',views.LoginPage,name="login"),
    path('logout/',views.LogoutUser,name="logout"),
    path('register/',views.RegisterPage,name="register"),  
    path('dashboard/',views.DashBoardPage,name="dashboard"),
    path('orderlist/',views.OrderListPage,name="orderlist"),
    path('order/<pk>/', views.EditOrder, name='order'),    
    path('delete/order/<pk>/', views.DeleteOrder, name='delete_order'),
    path('productlist/',views.ProductListPage,name="productlist"),
    path('stream/', views.PostStreamView.as_view(), name='stream'),
    path('order/<pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('delete/product/<pk>/', views.DeleteProduct, name='delete_product'),
    path('product/<pk>/', views.EditProduct, name='edit_product'),
    path('add_product/', views.AddProduct, name='add_product'),
    path('customer/',views.CustomerPage,name="customer"),
    path('checkout/',views.ChekcoutPage,name="checkout"),
    path('blogs/', views.PostList, name='blogs'),
    path('add_post/', views.AddPostView, name='add_post'),
    path('blogsedit/',views.BlogListPage,name="bloglist"),
    path('edit/<slug:slug>/', views.EditPost, name='edit_post'),
    path('delete/post/<pk>/', views.DeletePost, name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]



