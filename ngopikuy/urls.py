from django.urls import path
from .controllers import views, authentication, employee, customer, blogs

# url routing
urlpatterns = [
    path('',views.HomePage,name="homepage"),
    path('about/',views.AboutPage,name="about"),
    path('contact/',views.ContactPage,name="contact"),
    path('login/',authentication.LoginPage,name="login"),
    path('logout/',authentication.LogoutUser,name="logout"),
    path('register/',authentication.RegisterPage,name="register"),  
    path('dashboard/',employee.DashBoardPage,name="dashboard"),
    path('orderlist/',employee.OrderListPage,name="orderlist"),
    path('productlist/',employee.ProductListPage,name="productlist"),
    path('stream/', employee.PostStreamView.as_view(), name='stream'),
    path('order/<pk>/', employee.OrderDetail.as_view(), name='order_detail'),
    path('delete/product/<pk>/', employee.DeleteProduct, name='delete_product'),
    path('product/<pk>/', employee.EditProduct, name='edit_product'),
    path('add_product/', employee.AddProduct, name='add_product'),
    path('customer/',customer.CustomerPage,name="customer"),
    path('checkout/',customer.ChekcoutPage,name="checkout"),
    path('blogs/', blogs.PostList, name='blogs'),
    path('add_post/', blogs.AddPostView, name='add_post'),
    path('blogsedit/',blogs.BlogListPage,name="blogsedit"),
    path('edit/<slug:slug>/', blogs.EditPost, name='edit_post'),
    path('<slug:slug>/', blogs.PostDetail.as_view(), name='post_detail'),
]

