var gulp = require('gulp'),
    del = require('del');


gulp.task('clean', function() {
	/*
	 * Task for cleaning app directory
	 * from compiled js files
	*/
	del("frontend/app/*.js*");
	del("frontend/app/modules/**/*.js*");
})
