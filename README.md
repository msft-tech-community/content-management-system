# Content Management System
*A CDN simulation platform for the Microsoft Tech Community*

A simple CDN prototype using Flask and Azure Blob Storage to deliver content faster across India.

## Project Flow

```
User Upload → Image Compression → Azure Blob Storage → Fast Content Delivery
     ↓              ↓                    ↓                      ↓
   Flask API    PIL/Pillow         Indian Region         Sub-200ms Response
   Endpoints    Algorithms          Optimization            Time
```

**Detailed Flow:**
1. User uploads content through Flask API endpoints
2. System applies compression algorithms to reduce file size
3. Compressed files are stored in Azure Blob Storage (optimized for India)
4. Content is delivered to users with minimal latency
5. Performance metrics are tracked and monitored

## Project Structure (just for reference)

```
content-management-system/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py              # Home and health check endpoints
│   │   └── upload.py            # File upload endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── azure_storage.py     # Azure Blob Storage integration
│   │   └── image_compression.py # Compression algorithms
│   ├── templates/               # HTML templates
│   └── static/                  # CSS, JS, images
├── config/
│   ├── __init__.py
│   ├── development.py
│   └── production.py
├── tests/
├── requirements.txt
├── app.py                       # Main Flask application
└── README.md
```

## What This Project Does

This is a basic CDN system that stores files in Azure cloud storage and serves them through a Flask web server. Instead of loading everything from one server, files are distributed across Azure's network to reduce loading times.

## Why We Built This

Most websites serve images and files directly from their main server. This gets slow when users are far away or when lots of people visit at once. CDNs solve this by putting copies of your content closer to users.

Our project shows how this works on a smaller scale like a mini version of what big companies like Netflix or YouTube use.

## Current Development Phase

### Team Responsibilities

**Backend Development (Saisha)**
- Flask API setup with modular structure
- Core endpoints: `/`, `/health_check`
- Template and static file configuration
- Repository setup and initial codebase

**Cloud Infrastructure (Aniket)**
- Azure Blob Storage research and setup
- Cost-efficient configuration for Indian region
- Latency optimization strategies
- Documentation with implementation screenshots

**Image Processing (Yuvraj)**
- Compression algorithm research
- Testing compression ratios without quality loss
- Performance benchmarking on different image types
- Optimal compression percentage analysis

**UI/UX Design (Abhishek)**
- Figma design system creation
- User interface mockups
- User experience flow design

**Web Development (Shlok)**
- Frontend implementation (upcoming)
- Integration with Flask backend

## Technologies

- **Backend**: Flask (Python)
- **Cloud Storage**: Azure Blob Storage
- **Image Processing**: PIL/Pillow
- **Frontend**: HTML/CSS/JavaScript
- **Design**: Figma
- **Deployment**: Azure App Service

## Goals

- Load files in under 200ms within India
- Handle 1000+ concurrent requests
- Reduce hosting costs by 40%
- Achieve 99.9% uptime
- Cut bandwidth usage by 50% through compression

## Contributing

1. **Fork** this repository
2. **Clone** your fork: `git clone https://github.com/msft-tech-community/content-management-system`
3. **Create** a new branch: `git checkout -b feature-name`
4. **Make** your changes and test them
5. **Commit**: `git commit -m "Add your feature"`
6. **Push** to your fork: `git push origin feature-name`
7. **Create** a Pull Request

### Development Setup (Coming Soon)
- Prerequisites and installation guide
- Local development environment setup
- Testing guidelines

---

*Built with ❤️ for the Microsoft Tech Community*