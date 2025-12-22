import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import BookInput from './components/BookInput.jsx'
import { getCoverUrl } from './services/openlib.jsx';
import BentoCard from './components/BentoCard.jsx'
import { getImageUrls } from './services/unsplash.jsx'
function App() {
  const [title, setTitle] = useState('');
  const [desc1, setDesc1] = useState('');
  const [desc2, setDesc2] = useState('');
  const [desc3, setDesc3] = useState('');
  const [desc4, setDesc4] = useState('');
  const [desc5, setDesc5] = useState('');
  const [Url, setimgUrl] = useState('/placeholder2.jpg');
  const [finalurls, setFinalurls] = useState([]);
  const [showCollage, setShowCollage] = useState(false);
  const handleCover = async () => {

     console.log("clicked, title is:", title);

    if (!title) return;
    try {    
        console.log('fetching cover for title:', title);    
        const url = await getCoverUrl({title}); 
        console.log('fetched coverUrl:', url);     // your service function
        setimgUrl(url);    
        setFinalurls(prev => [...prev, url]);                       // save to state to render
    } catch (err) {
        console.error(err);
        setimgUrl('/placeholder.jpg');
    }
  };

 const handleSearch = async (title) => {

     console.log("clicked, search is:", title);

    if (!title) return;
    try {    
        console.log('fetching images for search:', title);    
        const imgurl = await getImageUrls(title); 
        console.log('fetched image Url:', imgurl);     // your service function
        setimgUrl(imgurl); 
        setFinalurls(prev => [...prev, imgurl]);                          // save to state to render
    } catch (err) {
        console.error(err);
    }
  } ;



  return (
    <>
      <script> console.log('start here');</script>
      <BookInput value={title} onChange={setTitle} placeholder="Book Title" />
      <button onClick={handleCover}>Get Cover</button>
      <br />
      <BookInput value={desc1} onChange={setDesc1} placeholder="Description 1" />
      <button onClick={() => {handleSearch (desc1)}}>Get Image 1</button>
      <br />
      <BookInput value={desc2} onChange={setDesc2} placeholder="Description 2" />
      <button onClick={() => {handleSearch (desc2)}}>Get Image 2</button>
      <br />
      <BookInput value={desc3} onChange={setDesc3} placeholder="Description 3" />
      <button onClick={() => {handleSearch (desc3)}}>Get Image 3</button>
      <br />
      <BookInput value={desc4} onChange={setDesc4} placeholder="Description 4" />
      <button onClick={() => {handleSearch (desc4)}}>Get Image 4</button>
      <br />
      <BookInput value={desc5} onChange={setDesc5} placeholder="Description 5" />
      <button onClick={() => {handleSearch (desc5)}}>Get Image 5</button>


      
      <script> console.log('rendering with title:', title);</script>
    
  
      
      
      
      
      
      <script> console.log('rendering with searched image:', title);</script>
      
      <div  className = 'first-show'>
      <BentoCard   imageUrl={Url} />
      </div>

      

      <button onClick={() => setShowCollage(true)}> Show Collage </button>

      
      {showCollage && (
        <div className='collage'>
        {finalurls.slice(0, 6).map((url, index) => (
      <div key={`bento-${index}`} className="collage-item">
        <BentoCard imageUrl={url} />
        </div>
        ))}
        </div>
        
      )}
       

  
    </>
  );
}

export default App
