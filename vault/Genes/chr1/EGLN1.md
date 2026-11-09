---
symbol: "EGLN1"
type: "gene"
col: 5754
ensembl_id: "ENSG00000135766"
name: "egl-9 family hypoxia inducible factor 1"
location: "1q42.2"
module: 144
arm: "+"
pooled_cpm: 184.99
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# EGLN1

*egl-9 family hypoxia inducible factor 1* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.2× (z +19.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.385× (z -14.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.437× (z -13.5, q 7e-39, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK4]] (+0.78, fdr 7e-06), [[PDK1]] (+0.76, fdr 7e-06), [[IPMK]] (+0.69, fdr 7e-06); moves opposite to [[SLC35C2]] (-0.52, fdr 3e-05), [[DELE1]] (-0.47, fdr 2e-04).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMAD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.2×** | +19.8 | 0e+00 | 49/49 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.63×** | +11.0 | 1e-25 | 45/48 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +8.3 | 2e-14 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 1e-08 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 6e-08 | 30/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.2 | 7e-08 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.81×** | +5.0 | 4e-05 | 37/48 (SHP-77, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.017 | 25/48 (BT-474, AN3 CA, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.068 | 8/48 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.072 | 25/48 (A549, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.2 | 0.073 | 22/48 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.085 | 24/49 (C-33 A, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -14.9 | 0e+00 | 44/44 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.437×** | -13.5 | 7e-39 | 47/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -11.4 | 1e-27 | 44/48 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.499×** | -11.3 | 2e-27 | 46/49 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -10.2 | 3e-22 | 32/48 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -9.5 | 1e-19 | 41/47 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -7.1 | 1e-10 | 37/48 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.682×** | -6.0 | 2e-07 | 28/48 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.708×** | -5.4 | 4e-06 | 31/47 (A-427, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.7 | 2e-04 | 30/48 (NCI-H661, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.5 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -4.0 | 0.003 | 22/48 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.789×** | -3.8 | 0.005 | 26/48 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.792×** | -3.7 | 0.011 | 28/48 (C32, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.6 | 0.014 | 17/48 (SW1417, C32, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.768×** | -3.1 | 0.062 | 18/48 (CHP-212, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.069 | 21/48 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.878× | -3.0 | 0.071 | 7/48 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.775×** | -3.0 | 0.075 | 20/49 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.836× | -2.9 | 0.080 | 18/48 (SW 1271, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 629 | 2 | 11 (8 ⚠) | [[PH-797804 (drug)]] 5 µM 17.5× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 167 | 2 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -25.0) |
| [[SW480 (line)]] | alt | 106 | 8 (3 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +20.1) | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -9.3) |
| [[A-427 (line)]] | wt | 470 | 2 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.207× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 204 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.02× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 196 | 2 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.246× (z -18.6) |
| [[LS 180 (line)]] | wt | 125 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.342× (z -12.0) |
| [[SW48 (line)]] | wt | 218 | 1 | 7 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.08× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 145 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.30× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 314 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.04× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 142 | 4 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -8.7) |
| [[C-33 A (line)]] | alt | 378 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.31× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 208 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.8) |
| [[HOP62 (line)]] | alt | 184 | 5 | 1 | [[TAK-901 (drug)]] 5 µM 28.5× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.327× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 296 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 181 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +15.1) | [[Harringtonine (drug)]] 5 µM 0.233× (z -15.1) |
| [[RKO (line)]] | wt | 193 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -23.7) |
| [[SW 900 (line)]] | alt | 212 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.3) |
| [[A498 (line)]] | wt | 133 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.1) | [[Auranofin (drug)]] 5 µM 0.432× (z -10.6) |
| [[HCT15 (line)]] | alt | 228 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.2) |
| [[HT-29 (line)]] | alt | 128 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.00× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -9.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.436× (z -9.1) |
| [[LoVo (line)]] | wt | 134 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.443× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 160 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 16.8× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.425× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 155 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.6× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.281× (z -16.9) |
| [[Panc 03.27 (line)]] | alt | 138 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.98× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -9.6) |
| [[PANC-1 (line)]] | alt | 113 | 4 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 15.2× (z +15.8) | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 184 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -8.8) |
| [[A-172 (line)]] | wt | 254 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 166 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.0× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 234 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.412× (z -10.3) |
| [[CHP-212 (line)]] | wt | 256 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.0) |
| [[H4 (line)]] | wt | 152 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.6× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 154 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.1× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 248 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.5) |
| [[HS-578T (line)]] | alt | 128 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.5× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 77.4 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.76× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 239 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.1× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.464× (z -8.6) |
| [[SHP-77 (line)]] | alt | 205 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.9) |
| [[AN3 CA (line)]] | alt | 276 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.5) |
| [[BT-474 (line)]] | alt | 53.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.5) |
| [[COLO 205 (line)]] | alt | 131 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.23× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 185 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.89× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 172 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.9× (z +11.3) | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -13.6) |
| [[SNU-423 (line)]] | alt | 182 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 31.1× (z +16.7) | — |
| [[J82 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +14.8) | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.165× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK4]] | +0.78 | +0.85 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PDK1]] | +0.76 | +0.81 / +0.75 | both halves | 7e-06 | STRING 514 |
| [[IPMK]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MXI1]] | +0.67 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[BNIP3]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 | STRING 673 |
| [[ZNF292]] | +0.64 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PDK3]] | +0.64 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.64 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.64 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[FAM13A]] | +0.63 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RBPJ]] | +0.63 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[HERC3]] | +0.62 | +0.75 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C2]] | -0.52 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[DELE1]] | -0.47 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity raises EGLN1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without SMAD9 | 0.070 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -18.0); signed map (-35.1, 24.6). **Vector** length 128, 46.8% of its response variance represented; |z| ≥ 3 in 1,302 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +19.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +7.1 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.7 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +11.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.8 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.0 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | egl-9 family hypoxia inducible factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,363,751-231,422,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SM-20, PHD2, ZMYND6, HIFPH2; previously C1orf12 |
| Gene groups (HGNC) | Zinc fingers MYND-type; Egl-9 family hypoxia inducible factors |
| Reactome | 4 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZT9](https://www.uniprot.org/uniprotkb/Q9GZT9) (Egl nine homolog 1):

> Cellular oxygen sensor that catalyzes, under normoxic conditions, the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. Hydroxylates a specific proline found in each of the oxygen-dependent degradation (ODD) domains (N-terminal, NODD, and C-terminal, CODD) of HIF1A. Also hydroxylates HIF2A. Has a preference for the CODD site for both HIF1A and HIF1B. Hydroxylated HIFs are then targeted for proteasomal degradation via the von Hippel-Lindau …

**Summary**, from NCBI Gene [54583](https://www.ncbi.nlm.nih.gov/gene/54583):

> The protein encoded by this gene catalyzes the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. HIF is a transcriptional complex that plays a central role in mammalian oxygen homeostasis. This protein functions as a cellular oxygen sensor, and under normal oxygen concentration, modification by prolyl hydroxylation is a key regulatory event that targets HIF subunits for proteasomal destruction via the von Hippel-Lindau ubiquitylation complex. …

**Accessions** — [HGNC:1232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1232) · Entrez [54583](https://www.ncbi.nlm.nih.gov/gene/54583) · UniProt [Q9GZT9](https://www.uniprot.org/uniprotkb/Q9GZT9) · Ensembl [ENSG00000135766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135766)

## Data

Gene col 5754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5754); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5754]; `tensor/DDL_lfc|DDL_z.npy` [5754]; `embed/gene_vectors.npy` [5754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5754 or target_col == 5754). Every well: [[EGLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
