import {
Route,
Routes,
} from 'react-router-dom'

import {
  Landing,
  DoctorsCorner,
  Footer,
} from './Pages'

import {
  Navbar,
} from './Components'

function App() {
  return (
    <div className="app">
      <Navbar />
      <Routes>
        <Route exact path='/' element={<Landing />}></Route>
        <Route exact path='/services' element={ <DoctorsCorner />}></Route>
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
