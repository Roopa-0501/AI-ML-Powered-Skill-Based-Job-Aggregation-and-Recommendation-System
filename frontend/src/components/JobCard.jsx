export default function JobCard({ job }) {

  return (
    <div className="job-card">

      <h3>{job.title}</h3>

      <p><b>Company:</b> {job.company}</p>
      <p><b>Location:</b> {job.location}</p>

      <p className="match">
        Match: {job.match_percentage}%
      </p>

      <p>
        <b>Matched Skills:</b>
        {job.matched_skills?.length
          ? job.matched_skills.join(", ")
          : " None"}
      </p>

      <a href={job.url} target="_blank">
        Apply Here
      </a>

    </div>
  );
}