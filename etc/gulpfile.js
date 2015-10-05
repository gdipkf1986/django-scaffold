/**
 * 1. compile scss
 * 2. compact css with sourcemap
 * 3. compact js
 * 4. minimize pics
 * */

'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var template = require('gulp-template');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var spritesmith = require('gulp.spritesmith');
var imagemin = require('gulp-imagemin');
var merge = require('merge-stream');
var md5 = require('gulp-md5');
var uglify = require('gulp-uglify');
var babel = require('gulp-babel');

gulp.task('sprite', function () {
    var sprite_data = gulp.src('./static_resources/images/**/icon_*.{png,jpg}')
        .pipe(spritesmith({
            imgName: 'icons.png',
            cssName: 'icons.scss',
            imgPath: '../images/icons.png',
            padding: 5
        }));

    var img_stream = sprite_data.img.pipe(imagemin())
        .pipe(gulp.dest('./static/images/'));

    var css_stream = sprite_data.css
        .pipe(gulp.dest('./static_resources/scss/')); // output scss for next step

    return merge(img_stream, css_stream);
});



gulp.task('scss', function () {

    var src = ['./static_resources/scss/variables.scss', './scss/base.scss', './scss/*.scss'];
    gulp.src(src)
        .pipe(sourcemaps.init())
        .pipe(concat('all.min.scss'))
        //.pipe(template({'variable_name': variable_value})) // pass varilabes to scss
        .pipe(sass.sync({includePaths: ['./scss/'], outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(autoprefixer({browsers: ['> 1%', 'IE 7'], cascade: false}))
        //.pipe(md5())  // need update template reference after rename css file with md5 tag.
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./static/css'))

});



gulp.task('js', function () {
    gulp.src('./static_resoures/js/*.js')
        .pipe(sourcemaps.init())
        .pipe(concat('all.min.js'))
        //.pipe(babel()) // enable this if you are need transfer es6 to es5
        .pipe(uglify())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./static/js'))
});



gulp.task('watch', function () {
    console.log('watching scss files');
    gulp.watch('./scss/*.scss', ['scss']);
    gulp.watch('./js/*.js', ['js'])
});


gulp.task('dev', ['sprite', 'watch']);
gulp.task('prod', ['sprite', 'scss', 'js']);

gulp.task('default', function () {
    var argv = require('yargs').argv;
    if (argv.dev) {
        gulp.run('dev');
    } else {
        gulp.run('prod');
    }
});
