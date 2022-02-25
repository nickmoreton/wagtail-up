const { parallel, series, watch, src, dest } = require("gulp");

// dev
const autoprefixer = require("autoprefixer");
const babel = require("gulp-babel");
const browserSync = require("browser-sync").create();
const del = require("del");
const concat = require("gulp-concat");
const postcss = require("gulp-postcss");
const sass = require("gulp-sass")(require("sass"));

// prod
const terser = require("gulp-terser");
const cssnano = require("cssnano");

// CSS //////////////////////////////////////////////////////////////////////////
function sassTask() {
    return src("./static_src/scss/**/*.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(dest("./app/static_compiled/css"))
        .pipe(browserSync.stream());
}

// JS ////////////////////////////////////////////////////////////////////////////
function jsTask() {
    return src("./static_src/js/**/*.js")
        .pipe(concat("scripts.js"))
        .pipe(dest("./app/static_compiled/js"));
}

// COMMON ////////////////////////////////////////////////////////////////////////
function cleanTask() {
    return del(["./app/static_compiled"]); // delete static_compiled folder
}

// WATCHES ///////////////////////////////////////////////////////////////////////
function serveTask() {
    browserSync.init({
        proxy: "http://127.0.0.1:8000",
        notify: {
            styles: {
                top: "auto",
                left: 0,
                right: "auto",
                bottom: 0,
            },
        },
    });
    watch(["./app/**/*.html", "./app/**/*.py"]).on("change", browserSync.reload);
    watch("./static_src/scss/**/*.scss", sassTask);
    watch("./static_src/js/**/*.js", jsTask).on("change", browserSync.reload);
}

// PREP PROD /////////////////////////////////////////////////////////////////////
function prodStylesTask() {
    return src("./app/static_compiled/css/**/*.css")
        .pipe(postcss([autoprefixer(), cssnano()]))
        .pipe(dest("./app/static_compiled/css"));
}

function prodSciptsTask() {
    return src("./app/static_compiled/js/**/*.js")
        .pipe(
            babel({
                presets: ["@babel/preset-env"],
            })
        )
        .pipe(terser())
        .pipe(dest("./app/static_compiled/js"));
}

// EXPORTS ///////////////////////////////////////////////////////////////////////
exports.clean = cleanTask;
exports.styles = sassTask;
exports.scripts = jsTask;
exports.serve = serveTask;
exports.compressStyles = prodStylesTask;
exports.compressScripts = prodSciptsTask;

exports.default = series(cleanTask, parallel(jsTask, sassTask), serveTask);
exports.build = series(
    cleanTask,
    jsTask,
    sassTask,
    prodStylesTask,
    prodSciptsTask
);
