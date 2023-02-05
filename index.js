const yts = require('yt-search')
const fs = require('fs')

let rawdata = fs.readFileSync('top500.json');
let albums = JSON.parse(rawdata);

const index = Math.ceil(Math.random() * albums.length)

const album = albums[index]
const artist = album.Artist || ''
const albumName = album.Album || ''

console.log("Your random album for today: ")
console.log(album)

getLink(artist, albumName)
  .then(link => console.log(link))

async function getLink(artist, album) {
  const query = artist + ' ' + album + ' full album'

  const opts = { query }
  const r = await yts(opts)
  const topID = r.playlists[0]?.listId

  return `https://music.youtube.com/playlist?list=${topID}`
}
