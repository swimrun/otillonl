#!/bin/bash

# Start local HTTP server for Ötillö NL website
# This script starts a local web server to view the HTML files

echo "🏊‍♂️ Starting Ötillö NL website server..."
echo ""

# Check if http-server is installed
if ! command -v npx &> /dev/null; then
    echo "❌ Error: npx is not installed. Please install Node.js first."
    echo "   Visit: https://nodejs.org/"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Please run this script from the project directory."
    exit 1
fi

echo "📁 Serving files from: $(pwd)"
echo "🌐 Server will be available at: http://localhost:8080"
echo "📄 Main page: http://localhost:8080/index.html"
echo "📊 Results page: http://localhost:8080/results.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the HTTP server
npx http-server . -p 8080 -o
