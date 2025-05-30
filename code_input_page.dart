import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class CodeInputPage extends StatefulWidget {
  const CodeInputPage({super.key});

  @override
  State<CodeInputPage> createState() => _CodeInputPageState();
}

class _CodeInputPageState extends State<CodeInputPage> {
  final TextEditingController _codeController = TextEditingController();
  String _validationResult = '';
  bool? _isValid;

  Future<void> validateCode() async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:5000/validate_code'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'code': _codeController.text}),
    );

    final data = jsonDecode(response.body);
    setState(() {
      if (data['status'] == 'valid') {
        _isValid = true;
        _validationResult = data['message'];
      } else {
        _isValid = false;
        _validationResult = data['errors'] ?? 'Unknown error';
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[50],
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Enter Validation Code',
              style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 20),
            TextField(
              controller: _codeController,
              maxLines: null,
              keyboardType: TextInputType.multiline,
              decoration: const InputDecoration(
                labelText: 'Validation Code',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: validateCode,
              child: const Text('Validate Code'),
            ),
            const SizedBox(height: 20),
            if (_isValid != null)
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    _isValid! ? Icons.check_circle : Icons.cancel,
                    color: _isValid! ? Colors.green : Colors.red,
                  ),
                  const SizedBox(width: 10),
                  Text(
                    _isValid! ? 'Code is valid' : 'Code is invalid',
                    style: TextStyle(
                      color: _isValid! ? Colors.green : Colors.red,
                      fontSize: 18,
                    ),
                  ),
                ],
              ),
            const SizedBox(height: 10),
            if (_validationResult.isNotEmpty)
              Text(
                _validationResult,
                style: const TextStyle(fontSize: 14),
                textAlign: TextAlign.center,
              ),
          ],
        ),
      ),
    );
  }
}


