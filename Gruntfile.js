module.exports = function (grunt) {
    let build = [
        'copy',
        'sass',
    ];

    grunt.initConfig({
        copy: {
            fonts: {
                files: [{
                    expand: true,
                    cwd: 'node_modules/microns/fonts',
                    src: [
                        'microns.eot',
                        'microns.svg',
                        'microns.ttf',
                        'microns.woff',
                        'microns.woff2'
                    ],
                    dest: 'static/fonts/microns/'
                }]
            }
        },
        sass: {
            dist: {
                files: {
                    'static/css/style.css': 'assets/custom/css/style.scss'
                }
            }
        },
        watch: {
            styles: {
                files: ['assets/custom/css/**/*.scss'],
                tasks: ['sass:dist']
            }
        }
    })

    grunt.loadNpmTasks("grunt-contrib-copy")
    grunt.loadNpmTasks("grunt-contrib-sass")
    grunt.loadNpmTasks("grunt-contrib-watch")

    grunt.registerTask('build', build)
    grunt.registerTask('default', build.concat('watch'))
};