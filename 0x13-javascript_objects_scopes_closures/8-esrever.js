#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length;
  const newList = [];
  let j = 0;

  for (let i = listLength - 1; i >= 0; i--) {
    newList[j++] = list[i];
  }
  return (newList);
};
