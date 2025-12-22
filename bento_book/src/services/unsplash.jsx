export const getImageUrls =  async function(title) {
  
    const n = Math.random()*9;
    const YOUR_ACCESS_KEY = 'slwSBXDzIMkpHtwcBuPStrwLnQ-GFI_FUdgPG0HeE6o';
    const BASE_URL = 'https://api.unsplash.com/search/photos';
    const query = `?query=${title}`
    const client_id = `&client_id=${YOUR_ACCESS_KEY}`
    const url = BASE_URL+query+client_id;

    try{
        const response = await fetch(url)
        const data = await response.json()
        console.log(data)
        const imageUrl = data.results[0].urls.regular
        return imageUrl
    }
    catch (err)
  {
    console.log(err)
    return 'placeholder2.jpg';
  }
  };/*
  ;*/
