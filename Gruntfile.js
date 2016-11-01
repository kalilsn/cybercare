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
            dist: {
                src: 'styles.css',
                dest: 'dist/styles.css'
            }
        },

        processhtml: {
            dist: {
                files: {
                    'dist/index.html': 'index.html'
                }
            }
        },
        
        ngtemplates: {
            options: {
                module: "cybercare",
            },
            dist: {
                src: "templates/*.html",
                dest: "tmp/templates.js"
            }
        },

        concat: {
            dist: {
                src: ['tmp/lib.js', 'app.js', 'components/**/*.js', '<%= ngtemplates.dist.dest %>'],
                dest: 'dist/app.js'
            }
        },

        copy: {
            dist: {
                files: [
                    {src: '*.{py,txt,md,json}', dest: 'dist/'},
                ]
            }
        },

        bower_concat: {
            dist: {
                dest: {
                    'js': 'tmp/lib.js',
                    'css': 'dist/lib.css'
                },
                callback: function(mainFiles, component) {
                    return mainFiles.map(function(filepath) {
                        // Use minified files if available
                        var min = filepath
                            .replace(/\.js$/, '.min.js')
                            .replace(/\.css$/, '.min.css');
                        return grunt.file.exists(min) ? min : filepath;
                    });
                }
            }
        },

        clean: {
            tmp: ['tmp'],
            dist: ['dist/**/*']
        },

        run: {
            db: {
                cmd: "python",
                args: ["create_database.py"],

                options: {
                    cwd: "dist"
                }
            }
        },
       
        replace: {
            python: {
                src: ['dist/app.py'],
                dest: 'dist/app.py',
                replacements: [
                    {from: /# DEV([\s\S]*?)# ENDDEV/g, to: ""},
                    {from: /# BUILD\n# ([\s\S]*?)# ENDBUILD/g, to: "$1"},
                    {from: /@/g, to: "@app."}
                ]
            }
        }

    });

    grunt.registerTask('default', 'watch');
    grunt.registerTask('build', ['clean:dist', 'postcss', 'bower_concat', 'ngtemplates', 'concat', 'processhtml', 'copy', 'replace', 'run:db', 'clean:tmp']);

};