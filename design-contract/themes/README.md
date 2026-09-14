# Theme resolution

Resolve design values in this order:

`base theme → optional preset theme → client theme → explicit client override`

Shared foundation files define semantic roles and scales. Client brand literals must live only in client/theme override files. Theme presets may change personality (density, radius, typography family slot, imagery and motion) but must not change component APIs.
