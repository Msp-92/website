<!DOCTYPE html>
<html <?php language_attributes(); ?>>

<head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
   <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
   <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
   <?php wp_head(); ?>
</head>

<body>
   <div class="top-bar">
      <div class="container">
         <div class="row">
            <div class="col-md-12">
               <div class="data">
                  <?php

                  $headers = get_theme_mod("headers", false);
                  foreach ($headers as $header) :
                     if (array_key_exists('text', $header) && !empty($header['text'])) :
                  ?>
                        <span><i class="<?php echo (isset($header['icon']) && !empty($header['icon'])) ? $header['icon'] : null ?>"></i><?php echo $header['text'] ?></span>
                  <?php
                     endif;
                  endforeach;
                  ?>



               </div>
            </div>
         </div>
      </div>
   </div>
   <div class="main-menu">
      <div class="container">
         <div class="row">
            <div class="col-md-9 col-sm-8 col-xs-8">
               <div class="menu-items">
                  <?php wp_nav_menu(array(
                     'theme_location' => 'Main_Menu',
                     'depth' => '3',
                  )); ?>
               </div>
            </div>
            <div class="col-md-3 col-sm-4 col-xs-4 text-left">
               <div class="logo-box">
                  <?php the_custom_logo(); ?>
               </div>
            </div>
         </div>
      </div>
   </div>