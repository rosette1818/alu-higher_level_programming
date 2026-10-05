#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((result, element) => [element, ...result], []);
};
