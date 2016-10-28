module.exports = function(grunt) {
    require('load-grunt-tasks')(grunt);
    
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        watch: {

            css: {
                files: 'assets/styles.css',
                options: {
                    livereload: true
                },
                tasks: ['postcss:dev']
            },

            self: {
                files: 'Gruntfile.js'
            },

            livereload: {
                files: '**/*.{html,js}',
                options: {
                    livereload: true
                }
            }
        },

        postcss: {
            options: {
                map: true,
                processors: [
                    require('postcss-cssnext')(),
                    require('postcss-flexbugs-fixes')()
                ]
            },
            dev: {
                files: 'styles.css'
            }
        },

    });

    grunt.registerTask('default', 'watch');

};