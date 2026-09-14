import 'package:flutter/material.dart';

enum PriceDisplayVariant { standard, discounted, tiered, negotiated }

class PriceDisplay extends StatelessWidget {
  const PriceDisplay({
    super.key,
    required this.price,
    this.currencySymbol = '₹',
    this.mrp,
    this.variant = PriceDisplayVariant.standard,
    this.label,
  });

  final double price;
  final String currencySymbol;
  final double? mrp;
  final PriceDisplayVariant variant;
  final String? label;

  @override
  Widget build(BuildContext context) {
    final style = Theme.of(context).textTheme.titleMedium;
    return Semantics(
      label: label ?? 'Price $currencySymbol${price.toStringAsFixed(2)}',
      child: Wrap(
        crossAxisAlignment: WrapCrossAlignment.center,
        spacing: 8,
        children: [
          Text('$currencySymbol${price.toStringAsFixed(2)}', style: style),
          if (mrp != null && mrp! > price)
            Text(
              '$currencySymbol${mrp!.toStringAsFixed(2)}',
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    decoration: TextDecoration.lineThrough,
                  ),
            ),
        ],
      ),
    );
  }
}
