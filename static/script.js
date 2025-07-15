function updateFields() {
  const course = document.getElementById("course").value;
  const qualWrap = document.getElementById("qualification-wrapper");
  const cgpaWrap = document.getElementById("cgpa-wrapper");
  const yearDiv = document.getElementById("academic-year-div");

  yearDiv.innerHTML = ""; // Clear year field

  if (course === "Other") {
    qualWrap.style.display = "none";
    cgpaWrap.style.display = "none";
  } else {
    qualWrap.style.display = "block";
    cgpaWrap.style.display = "block";
  }
}

function syncQualification() {
  const level = document.getElementById("qualification-level").value;
  const status = document.getElementById("qualification-status").value;
  const hidden = document.getElementById("qualification");
  const yearDiv = document.getElementById("academic-year-div");
  const course = document.getElementById("course").value;

  if (level && status) {
    hidden.value = `${level} - ${status}`;
  }

  // Only show year if Pursuing
  if (status === "Pursuing") {
    let options = "";

    if (course === "Arts" || course === "Other") {
      options = `
        <option>1st Year</option>
        <option>2nd Year</option>
        <option>3rd Year</option>`;
    } else if (course === "Medicine") {
      options = `
        <option>1st Year</option>
        <option>2nd Year</option>
        <option>3rd Year</option>
        <option>4th Year</option>
        <option>5th Year</option>`;
    } else {
      options = `
        <option>1st Year</option>
        <option>2nd Year</option>
        <option>3rd Year</option>
        <option>4th Year</option>`;
    }

    yearDiv.innerHTML = `
      <label for="year" class="form-label">Academic Year</label>
      <select class="form-control" name="year" id="year" required>
        ${options}
      </select>`;
  } else {
    yearDiv.innerHTML = "";
  }
}


