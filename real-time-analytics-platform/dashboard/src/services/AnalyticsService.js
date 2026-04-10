import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class AnalyticsService {
  static async getSummary() {
    const response = await axios.get(`${API_BASE_URL}/api/analytics/summary`);
    return response.data;
  }

  static async getEventsByType(eventType) {
    const response = await axios.get(`${API_BASE_URL}/api/analytics/events/${eventType}`);
    return response.data;
  }

  static async getUserEvents(userId) {
    const response = await axios.get(`${API_BASE_URL}/api/analytics/users/${userId}`);
    return response.data;
  }
}

export default AnalyticsService;