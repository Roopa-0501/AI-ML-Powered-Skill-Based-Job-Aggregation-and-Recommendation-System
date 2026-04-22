export default function ResultPanel({ data }) {

if (!data) {
return ( <div className="result-panel"> <h3>No Results Yet</h3> </div>
);
}

return ( <div className="result-panel">

  <h3>Predicted Category: {data.category}</h3>
  <h3>Recommended Role: {data.role}</h3>

  <h4>Skills:</h4>
  <div className="skills">
  {data.skills.map((skill, index) => (
    <span key={index} className="skill-tag">{skill}</span>
  ))}
</div>

  <h4>Recommended Jobs:</h4>

  {data.jobs.length === 0 && <p>No matching jobs found</p>}

  {data.jobs.map((job, index) => (
    <div key={index} className="job-card">

      <h4>{job.title}</h4>
      <p>{job.company}</p>
      <p>{job.location}</p>

      <p className="match">
        Match: {job.match_percentage}%
      </p>

      <a href={job.url} target="_blank" rel="noreferrer">
        Apply Now
      </a>

    </div>
  ))}

</div>


);
}
