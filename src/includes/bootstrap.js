import Popper from '../../node_modules/popper.js/dist/umd/popper.min.js'

global.jQuery = require('jquery');
global.$ = global.jQuery;
global.Popper = Popper;
require("bootstrap");
import '../styles/_bootstrap.scss';