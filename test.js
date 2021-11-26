const fs = require('fs')

const str = fs.readFileSync('./index.txt').toString()

let urlList = str.match(/href=\"(.*?)\"/g)

for (let index = 0; index < urlList.length; index++) {
  urlList[index] = 'https://' + urlList[index].replace('href="//', '')
  urlList[index] = urlList[index].replace('\"', '')
}

console.log(urlList);

fs.writeFileSync('test.json', JSON.stringify(urlList))