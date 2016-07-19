from flask.ext.assets import Bundle


def bundles():
    bundles = {

    # Css Material Admin -------------------------------------------------------------------------------------------

        # app_css
        # 'app_css': Bundle(
        #     'css/app.min.1.css',
        #     'css/app.min.2.css',
        #     output='gen/app_min.css'
        # ),

        # #vendor_login_css
        # 'vendor_login_css': Bundle(
        #     'vendors/bower_components/animate.css/animate.min.css',
        #     output='gen/vendor_login.css'
        # ),

        #vendor_login_css
        # 'main_css': Bundle(
        #     'vendors/bower_components/animate.css/animate.min.css',
        #     "vendors/bower_components/bootstrap-sweetalert/lib/sweet-alert.css",
        #     "vendors/bower_components/malihu-custom-scrollbar-plugin/jquery.mCustomScrollbar.min.css",
        #     "vendors/bootgrid/jquery.bootgrid.min.css",            
        #     output='gen/main.css'
        # ),


        # javascript Material Admin-------------------------------------------------------------------------------------------

        #vendor_login_js
        # 'vendor_login_js': Bundle(
        #     'vendors/bower_components/jquery/dist/jquery.min.js',
        #     'vendors/bower_components/bootstrap/dist/js/bootstrap.min.js',
        #     'vendors/bower_components/Waves/dist/waves.min.js',
        #     output='gen/vendor_login.js'
        # ),

        #functions_js
        # 'functions_js': Bundle(
        #     'js/functions.js',
        #     "vendors/bower_components/malihu-custom-scrollbar-plugin/jquery.mCustomScrollbar.concat.min.js",
        #     # "vendors/bower_components/bootstrap-sweetalert/lib/sweet-alert.min.js",
        #     "vendors/bootstrap-growl/bootstrap-growl.min.js",
        #     "vendors/bower_components/Waves/dist/waves.min.js",
        #     "vendors/bootgrid/jquery.bootgrid.updated.min.js",
        #     output='gen/functions.js'
        # )

    }

    return bundles
