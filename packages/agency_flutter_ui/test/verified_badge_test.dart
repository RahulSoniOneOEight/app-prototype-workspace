import 'package:agency_flutter_ui/agency_flutter_ui.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('renders verified label', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: VerifiedBadge())));
    expect(find.text('Verified'), findsOneWidget);
    expect(find.byIcon(Icons.verified_outlined), findsOneWidget);
  });
}
