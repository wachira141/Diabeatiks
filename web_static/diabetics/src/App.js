import {
Route,
Routes,
} from 'react-router-dom'

import {
  Landing,
  DoctorsCorner,
  Footer,
} from './Pages'

function App() {
  return (
    <div className="app">
      <Routes>
        <Route exact path='/' element={<Landing />}></Route>
        <Route exact path='/services' element={ <DoctorsCorner />}></Route>
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
