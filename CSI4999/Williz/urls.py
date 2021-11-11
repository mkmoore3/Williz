from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/email/<email>", views.profile, name="profile"),
    path("resetPassword/", views.resetPassword, name="resetPassword"),
    path("resetPassword_Handler/", views.resetPassword_Handler, name="resetPassword_Handler"),
    path("resetPasswordVerify/", views.resetPasswordVerify, name="resetPasswordVerify"),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("verify/email/<verify_string>", views.email_verification_page, name="verify email"),
    path("profile/edit_user_info", views.edit_user_info, name="update"),
    path("register_user_handler/", views.register_user_handler, name="register_user_handler"),
    path("login_handler/", views.login_handler, name="login_handler"),
    path("createListing/email/<email>", views.create_listing, name="createListing"),
    path("create_listing_handler/", views.create_listing_handler, name="create_listing_handler"),
    path("accountRequests/", views.accountRequests, name="accountRequests"),
    path("delete_user_account/<user_id>", views.delete_user_account, name="delete_user_account"),
    path("change_verification/email/<email>", views.change_verification, name="changeVerification"),
    path("searchListings/", views.searchListings, name="searchListings"),
    path("searchListings_handler/", views.searchListings_handler, name="searchListings_handler"),
    path("listing/<state>/<zip>/<city>/<street>/<house_num>", views.listing, name="listing"),
    path("listing/update/<state>/<zip>/<city>/<street>/<house_num>", views.updateListing, name="updateListing"),
    path("update/<state>/<zip>/<city>/<street>/<house_num>", views.update, name="update"),
    path("listing/admin/update/<state>/<zip>/<city>/<street>/<house_num>", views.admin_listing_update,
         name="adminUpdateListing"),
    path("listing/confirm/delete/<state>/<zip>/<city>/<street>/<house_num>", views.delete_listing_confirmation,
         name="confirmDeleteListing"),
    path("listing/delete", views.delete_listing_handler, name="deleteListing"),
    path("listing/image_handler/<state>/<zip>/<city>/<street>/<house_num>", views.listing_image_handler,
         name="listing_image_handler"),
    path("listing/upload_images/<state>/<zip>/<city>/<street>/<house_num>", views.listing_image_upload,
         name="listing_image_upload"),
    path("listing/app_img_handler/<state>/<zip>/<city>/<street>/<house_num>", views.appraisal_image_handler,
         name="listing_image_handler"),
    path("listing/app_images/<state>/<zip>/<city>/<street>/<house_num>", views.appraisal_image_upload,
         name="listing_image_upload"),
    path("listing/upload/pdf/handler/<state>/<zip>/<city>/<street>/<house_num>",
         views.pdf_upload_handler, name="MikeCares(somewhat)"),
    path("listing/upload/pdf/<state>/<zip>/<city>/<street>/<house_num>", views.appraisal_pdf_upload,
         name="pdfHandler"),
    path("listing/update/appraiser/<state>/<zip>/<city>/<street>/<house_num>", views.set_appraiser,
         name="set_appraiser"),
    path("listing/update/appraiser/handler/<state>/<zip>/<city>/<street>/<house_num>", views.set_appraiser_handler,
         name="set_appraiser"),
    path("listing/complete/<state>/<zip>/<city>/<street>/<house_num>", views.complete_listing, name="complete")
]
