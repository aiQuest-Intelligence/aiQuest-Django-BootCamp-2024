from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    #path("",views.home, name="home"),
    path("",views.ProductView.as_view(), name="home"),
    path('product_details/<int:pk>',views.ProductDetailView.as_view(),name='product_details'),
    path('vegetable/',views.vegetable, name='vegetable'),
    path('vegetable/<slug:data>',views.vegetable, name='vegetabledata'),
    path('fruit/',views.fruit, name='fruit'),
    path('fruit/<slug:data>',views.fruit, name='fruitdata'),
    path('juice/',views.juice, name='juice'),
    path('juice/<slug:data>',views.juice, name='juicedata'),
    path('product_grid/',views.product_grid, name='product_grid'),
    path('tea/',views.tea, name='tea'),
    path('tea/<slug:data>',views.tea, name='teadata'),
    path('bread/',views.bread, name='bread'),
    path('bread/<slug:data>',views.bread, name='breaddata'),
    path('jam/',views.jam, name='jam'),
    path('jam/<slug:data>',views.jam, name='jamdata'),
    path('add-to-cart/',views.add_to_cart, name='add_to_cart'),
    path('cart/',views.show_cart, name='show_cart'),


    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


    path('product_checkout/',views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('blog/',views.blog, name='blog'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('address/',views.address, name='address'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='password/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='password/passwordchangedone.html'), name='passwordchangedone'),



    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),


    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),

    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name="password_reset_complete"),

    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
