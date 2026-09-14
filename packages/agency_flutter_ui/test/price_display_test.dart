import 'package:agency_flutter_ui/agency_flutter_ui.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('renders current price and optional mrp', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: PriceDisplay(price: 90, mrp: 100))));
    expect(find.text('₹90.00'), findsOneWidget);
    expect(find.text('₹100.00'), findsOneWidget);
  });
}
