## Sprint 1: Initial Setup (Date: December 1, 2024 - December 7, 2024)
### **Sprint Goal**
- Set up the foundational project structure.
- Integrate React frontend with Flask backend.
- Establish the GitHub repository and organize tasks.

### **Tasks**
1. Initialize the GitHub repository and push the project.
2. Create project backlog and Scrum board.
3. Set up Flask API for `/api/movies`.
4. Integrate React frontend with Flask backend.
5. Test and verify the basic end-to-end connection.

### **Meeting Notes**
- **Kickoff Meeting**: 
  - Discussed overall project goals and decided on the technology stack.
  - Divided tasks among team members.
- **Daily Stand-ups**:
  - **Day 2**: Flask API successfully initialized.
  - **Day 4**: React and Flask integration faced minor CORS issues, resolved by enabling Flask-CORS.
  - **Day 6**: Initial testing completed, but `/api/similarity` still needed attention.

### **Outcome**
- Successfully set up the foundational structure and ensured basic connectivity between React and Flask.

---

## Sprint 2: Core Functionality (Date: December 8, 2024 - December 14, 2024)
### **Sprint Goal**
- Develop and deploy the core recommendation system.
- Implement fuzzy matching and TMDB API integration.
- Optimize the similarity matrix computation.

### **Tasks**
1. Implement content-based recommendation algorithm using cosine similarity.
2. Add fuzzy matching for better search results.
3. Integrate TMDB API for fallback recommendations.
4. Deploy the app locally for testing.
5. Write test cases to validate recommendation results.

### **Meeting Notes**
- **Planning Meeting**: 
  - Prioritized fuzzy matching and TMDB API integration.
  - Decided to deploy the local app after successful testing.
- **Daily Stand-ups**:
  - **Day 2**: Content-based recommendation system completed.
  - **Day 3**: Fuzzy matching implemented, minor performance issues noted.
  - **Day 5**: TMDB API integrated and tested successfully.
  - **Day 7**: Unit tests written and passed, ready for deployment.

### **Outcome**
- Fully functional recommendation system completed.
- Local deployment validated with accurate search and fallback results.

---

## Sprint 3: Finalization and Deployment (Date: December 15, 2024 - December 20, 2024)
### **Sprint Goal**
- Finalize the project with UI improvements and pipeline automation.
- Deploy the app to a public server.
- Conduct end-to-end testing and finalize documentation.

### **Tasks**
1. Improve UI/UX for the search and recommendation pages.
2. Set up GitHub Actions for CI/CD pipeline.
3. Deploy the app to a public cloud platform (e.g., Heroku or AWS).
4. Conduct extensive end-to-end testing.
5. Write final project documentation (e.g., README, user manual).

### **Meeting Notes**
- **Planning Meeting**: 
  - Decided on UI improvements to enhance user experience.
  - Set up deployment goals and assigned them to the DevOps team.
- **Daily Stand-ups**:
  - **Day 2**: GitHub Actions pipeline set up for testing and deployment.
  - **Day 4**: UI/UX changes completed and tested.
  - **Day 6**: Successfully deployed the app to Heroku, tested live version.

### **Outcome**
- Completed deployment to the public server.
- Final documentation written and added to GitHub repository.

---

## Project Retrospective
### **What Went Well**
- Strong coordination between team members ensured timely completion of tasks.
- Robust testing eliminated major bugs before deployment.
- Fuzzy matching and TMDB API integration enhanced the functionality.

### **What Could Be Improved**
- Encountered delays due to initial unfamiliarity with TMDB API.
- Some UI features could have been implemented earlier in the project.

### **Final Status**
- Deadline Met: December 21, 2024.
- The project is now live and fully functional.

---
