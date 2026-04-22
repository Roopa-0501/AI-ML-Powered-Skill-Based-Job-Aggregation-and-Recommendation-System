export default function Navbar() {

const showContact = () => {
alert("Contact us at: skillweave.support@gmail.com");
};

  return (
    <div className="navbar">
      <h2 className="logo">SkillWeave</h2>

      <div className="nav-links">
        <a href="#">Home</a>
        <a href="#" onClick={showContact}>Contact</a>
      </div>
    </div>
  );
}
