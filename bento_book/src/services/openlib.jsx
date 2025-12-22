export const getCoverUrl = async function({title}) {
  try {
    
    const res = await fetch(`https://openlibrary.org/search.json?title=${title}`);
    const data = await res.json();
    console.log('fetched data:', data);

    
    const cover_edition_key = data.docs?.[0]?.cover_edition_key;
    console.log('fetched cover_edition_key:', cover_edition_key);
    if (!cover_edition_key) throw new Error('No ISBN found');
    const cover = `https://covers.openlibrary.org/b/olid/${cover_edition_key}-L.jpg`;
    console.log('constructed cover URL:', cover);
    return cover;

  } 
  catch 
  {
    return 'placeholder.jpg';
  }
};

