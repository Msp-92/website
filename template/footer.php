<div class="footer_box">
   <div class="container">
      <div class="row">
         <div class="col-md-7 col-sm-12">
            <div class="col-md-4 col-sm-4">
               <div class="footer-menu">
                  <span class="title">دسترسی سریع</span>
                  <?php wp_nav_menu(array(
                     'theme_location'=>'Footer_one',
                     'depth'=>'1',
                     )); ?>
               </div>
            </div>
            <div class="col-md-4 col-sm-4">
               <div class="footer-menu">
                  <span class="title">دسته بندی موضوعی</span>
                  <?php wp_nav_menu(array(
                     'theme_location'=>'Footer_two',
                     'depth'=>'1',
                     )); ?>
               </div>
            </div>
            <div class="col-md-4 col-sm-4">
               <div class="footer-menu">
                  <span class="title">دسترسی سریع</span>
                  <?php wp_nav_menu(array(
                     'theme_location'=>'Footer_three',
                     'depth'=>'1',
                     )); ?>
               </div>
            </div>
         </div>
         <div class="col-md-5 col-sm-12">
            <?php if(is_active_sidebar('fdesc')){
               dynamic_sidebar('fdesc');
               } ?>  
               <div class="footer_social">
                  <?php wp_nav_menu(array(
                        'theme_location'=>'Footer_Social',
                        'depth'=>'1',
                  )); ?>
               </div>
         </div>
         <div class="col-md-12 text-center">
            <div class="copy-r">
               <span>
               &copy; حقوق انتشار برای سئو 90 محفوط است
               </span>
            </div>
         </div>
      </div>
   </div>
</div>
</body>
</html>