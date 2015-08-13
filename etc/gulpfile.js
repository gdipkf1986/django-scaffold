/**
 * Created by Jovi on 10/5/2015.
 * 0. Run less or sass
 * 1. Optimize pics
 * 2. Generate css sprite
 * 3. Auto prefix in css
 * 4. Compact css and js and generate map.json
 * 5. uglify compacted files
 */

var cfg = {
    'src': 'static/'
    , 'dist': 'dist/'
};

var gulp = require('gulp');
var sourcemaps = require('gulp-sourcemaps');


/*********************************************************/
/** 1. Optimize pics **/
var imagemin = require('gulp-imagemin');
gulp.task('image', function () {
    gulp.src(cfg.src + '/images/**/*.*')
        .pipe(imagemin({progressive: true}))
        .pipe(gulp.dest(cfg.dist + '/images'))
});


/*********************************************************/
/** 4. compact css and js and generate map.json **/

var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var less = require('gulp-less');
var sass = require('gulp-ruby-sass');
var prefix = require('gulp-autoprefixer');
var concat = require('gulp-concat');



gulp.task('sass', function () {
    return sass(cfg.src + '/sass/', {sourcemap: true})
        .on('error', function (err) {
            console.error('Error', err.message);
        })

        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(cfg.src + '/css/'));
});




gulp.task('css_scripts', function () {

    gulp.src([cfg.src + '/scripts/*.js'])
        .pipe(sourcemaps.init())
        .pipe(concat('all.js'))
        .pipe(uglify())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(cfg.dist + '/scripts/'));

    gulp.src([cfg.src + "/css/**/*.css", '!'+cfg.src+'/css/site.css'])
        .pipe(sourcemaps.init())
        .pipe(concat('all.css'))
        .pipe(prefix("last 1 version", "> 1%", "ie 8", "ie 7"))
        .pipe(minifyCSS())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(cfg.dist + '/css/'));

});


/***********************************************************************/


gulp.on('stop', function () {
    process.nextTick(function () {
        process.exit(0);
    });
});

gulp.task('auto', function () {
    gulp.watch(cfg.src + '/scripts/*.js', ['css_scripts'])
});


//gulp.task('default', ['script', 'auto']);
gulp.task('default', ['sass', 'css_scripts', 'image']);