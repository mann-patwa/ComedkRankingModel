class college {
  constructor(id, college_info) {
    this.id = id;
    this.college_info = college_info;
  }
}

class Student {
  constructor(id, rank, preferences) {
    this.id = id;
    this.rank = rank;
    this.preferences = preferences;
    this.alloted = {};
  }
}
branches_list = ["ec", "cs", "is"];
rank_list = [];
var student_list = [];
var colleges_list = [];

for (let i = 1; i < 101; i++) {
  rank_list.push(i);
}
rank_list.sort(() => (Math.random() > 0.5 ? 1 : -1));
function random_number_generator(start, end) {
  return Math.floor(Math.random() * end) + start;
}

// making students

for (let i = 1; i < 101; i++) {
  var preferences = [];
  for (let i = 0; i < 3; i++) {
    var college_id = random_number_generator(1, 10);
    var branch =
      branches_list[Math.floor(Math.random() * branches_list.length)];
    preferences.push({ college_id: college_id, branch: branch });
  }
  var a_student = new Student(i, rank_list[i - 1], preferences);
  student_list.push(a_student);
}
// MAKING COLLEGES
for (let i = 1; i < 11; i++) {
  var acol = new college(i, {
    cs: {
      branch: "cs",
      seats: 4,
    },
    ec: {
      branch: "ec",
      seats: 4,
    },
    is: { branch: "is", seats: 4 },
  });
  colleges_list.push(acol);
}
var test_student = student_list[0];
var test_college = colleges_list[0];

// this is the ascending order of the ranks of students
student_list.sort((a, b) => a.rank - b.rank);
// THIS LOOP IS ITERATING OVER EVERY STUDENT FROM RANK 1 TO LAST AND ALLOTING THEM SEATS
for (let i = 0; i < student_list.length; i++) {
  //THIS LIST is iterating over the preferences of the students
  for (
    let pref_index = 0;
    pref_index < test_student.preferences.length;
    pref_index++
  ) {
    var selected_college_id =
      student_list[i].preferences[pref_index].college_id;
    var selected_branch = student_list[i].preferences[pref_index].branch;
    var selected_college = colleges_list[selected_college_id - 1];
    // this loop is for every preference, it is finding the branch in the selected college and checking if seats are there to allot
    // for (let x = 0; x < test_college.college_info.length; x++) {
    var selected_part_of_college =
      selected_college.college_info[selected_branch];
    if (selected_part_of_college.seats != 0) {
      student_list[i].alloted = {
        college_id: selected_college_id,
        branch: selected_branch,
      };
      selected_part_of_college.seats--;
      break;
    }
    // checking if the preference is alloted or to go to next priority
    if (student_list[i].alloted == {}) {
      continue;
    } else {
      break;
    }
  }
}
// printing the student list with alloted college
for (let i = 0; i < student_list.length; i++) {
  console.log(student_list[i]);
}
