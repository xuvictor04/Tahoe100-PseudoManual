---
symbol: "ODC1"
type: "gene"
col: 3716
ensembl_id: "ENSG00000115758"
name: "ornithine decarboxylase 1"
location: "2p25.1"
module: 158
arm: "+"
pooled_cpm: 53.52
n_lines_expressing: 48
n_dd_up: 49
n_dd_down: 14
n_dd_up_clean: 26
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# ODC1

*ornithine decarboxylase 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.20× (z +31.1, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.583× (z -6.3, q 2e-07, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM7A-DT]] (+0.56, fdr 1e-05), [[LINC00941]] (+0.56, fdr 3e-05), [[MAP2K3]] (+0.56, fdr 1e-05); moves opposite to [[LIN54]] (-0.55, fdr 1e-05), [[TTC28-AS1]] (-0.55, fdr 3e-05), [[NSD3]] (-0.53, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.20×** | +31.1 | 0e+00 | 45/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.83×** | +21.2 | 0e+00 | 45/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.31×** | +19.3 | 0e+00 | 46/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.77×** | +18.8 | 0e+00 | 45/46 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **4.11×** | +17.0 | 0e+00 | 41/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.25×** | +16.8 | 0e+00 | 45/46 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **2.48×** | +15.4 | 0e+00 | 43/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.40×** | +14.7 | 0e+00 | 43/46 (HOP62, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **3.26×** | +13.7 | 1e-40 | 37/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.98×** | +13.1 | 1e-37 | 44/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.81×** | +12.4 | 1e-33 | 39/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.81×** | +12.4 | 1e-33 | 39/46 (AsPC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.00×** | +12.2 | 9e-33 | 38/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.10×** | +11.0 | 1e-26 | 45/47 (SW48, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +10.5 | 2e-24 | 41/45 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +10.3 | 4e-23 | 42/46 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **2.15×** | +9.2 | 1e-18 | 38/46 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.02×** | +8.5 | 9e-16 | 40/46 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.0 | 6e-14 | 37/46 (HEC-1-A, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +7.5 | 2e-12 | 33/45 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.83×** | +7.3 | 9e-12 | 39/47 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +7.0 | 4e-11 | 35/46 (HOP62, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.75×** | +6.4 | 3e-09 | 36/46 (A-427, PANC-1, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.67×** | +6.2 | 1e-08 | 38/45 (LOX-IMVI, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.583×** | -6.3 | 2e-07 | 30/45 (A549, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.668×** | -5.0 | 2e-04 | 29/47 (NCI-H1573, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.751×** | -4.8 | 2e-04 | 26/46 (NCI-H1573, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.680×** | -4.7 | 4e-04 | 28/45 (A549, AsPC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.677×** | -4.5 | 8e-04 | 24/46 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.765×** | -4.0 | 0.007 | 21/46 (NCI-H2030, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.797×** | -3.8 | 0.011 | 21/46 (NCI-H2030, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.022 | 20/47 (NCI-H2030, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.565×** | -3.5 | 0.025 | 18/46 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.737×** | -3.5 | 0.025 | 20/47 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.785×** | -3.5 | 0.025 | 20/46 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -3.4 | 0.029 | 21/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.596×** | -3.2 | 0.057 | 18/48 (NCI-H2030, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.2 | 0.057 | 14/46 (NCI-H460, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.8 | 20 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.4) | — |
| [[SW480 (line)]] | alt | 78.5 | 16 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +17.3) | — |
| [[A-172 (line)]] | wt | 27.1 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +24.8) | — |
| [[PANC-1 (line)]] | alt | 55.6 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +20.5) | — |
| [[KATO III (line)]] | alt | 52.9 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +17.2) | — |
| [[HOP62 (line)]] | alt | 36.7 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +21.9) | — |
| [[HS-578T (line)]] | alt | 39.5 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +19.7) | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +23.3) | — |
| [[A549 (line)]] | wt | 44.6 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +17.1) | [[Cobimetinib (drug)]] 5 µM 0.210× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 45.8 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +15.7) | — |
| [[AsPC-1 (line)]] | alt | 83.3 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +25.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +16.7) | — |
| [[NCI-H23 (line)]] | alt | 76.2 | 6 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +10.3) | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -14.1) ⚠ position not correctable |
| [[LoVo (line)]] | wt | 69.3 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 47.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +15.6) | — |
| [[SNU-423 (line)]] | alt | 19.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +19.0) | — |
| [[SW 900 (line)]] | alt | 40.5 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +19.2) | — |
| [[SW48 (line)]] | wt | 102 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.18× (z +11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 22.3× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +21.3) | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +19.6) | — |
| [[NCI-H2347 (line)]] | alt | 58.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 14.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.6× (z +18.1) | — |
| [[HCT15 (line)]] | alt | 47.8 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.45× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 74.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +16.3) | — |
| [[J82 (line)]] | alt | 19.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 103 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.27× (z +9.0) | — |
| [[A498 (line)]] | wt | 27.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +21.2) | — |
| [[H4 (line)]] | wt | 19.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 26.0× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 7.70× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +17.3) | — |
| [[Hs 766T (line)]] | wt | 18.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 54.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 60.6 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.84× (z +11.7) | [[Trametinib (drug)]] 5 µM 0.204× (z -10.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.292× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 158 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.94× (z +9.0) | [[Adagrasib (drug)]] 0.05 µM 0.623× (z -14.6) ⚠ position not correctable |
| [[RKO (line)]] | wt | 89.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 99.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +24.2) | — |
| [[A-427 (line)]] | wt | 184 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.37× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 72.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.62× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.8) | — |
| [[AN3 CA (line)]] | alt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM7A-DT]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.56 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MAP2K3]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.55 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PHLDA1]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[NT5E]] | +0.53 | +0.53 / +0.39 | both halves | 6e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[EPHA2]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[TMEM185B]] | +0.52 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[FOSL1]] | +0.52 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[LIF]] | +0.52 | +0.54 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[C6orf141]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZFP41]] | +0.51 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN54]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TTC28-AS1]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[NSD3]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SOS1]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ZNF652]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TULP3]] | -0.50 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ETFDH]] | -0.50 | -0.59 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[CEP57]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[COG7]] | -0.49 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RABL6]] | -0.49 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[MFSD8]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PPM1B]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ODC1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ODC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCP1]] | B | CDCP1 activity lowers ODC1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.07× higher at baseline in the lines without CDCP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.5, 2.2); signed map (10.0, 45.0). **Vector** length 88.2, 30.5% of its response variance represented; |z| ≥ 3 in 1,800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.8 | +15.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.5 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +13.1 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.4 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +6.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.3 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ornithine decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,439,968-10,448,327 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ODC |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Decarboxylases |
| Hallmark sets | FATTY_ACID_METABOLISM, IL2_STAT5_SIGNALING, G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: Regulation of ornithine decarboxylase (ODC); Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P11926](https://www.uniprot.org/uniprotkb/P11926) (Ornithine decarboxylase):

> Catalyzes the first and rate-limiting step of polyamine biosynthesis that converts ornithine into putrescine, which is the precursor for the polyamines, spermidine and spermine. Polyamines are essential for cell proliferation and are implicated in cellular processes, ranging from DNA replication to apoptosis.

**Summary**, from NCBI Gene [4953](https://www.ncbi.nlm.nih.gov/gene/4953):

> This gene encodes the rate-limiting enzyme of the polyamine biosynthesis pathway which catalyzes ornithine to putrescine. The activity level for the enzyme varies in response to growth-promoting stimuli and exhibits a high turnover rate in comparison to other mammalian proteins. Originally localized to both chromosomes 2 and 7, the gene encoding this enzyme has been determined to be located on 2p25, with a pseudogene located on 7q31-qter. Multiple alternatively spliced transcript variants …

**Accessions** — [HGNC:8109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8109) · Entrez [4953](https://www.ncbi.nlm.nih.gov/gene/4953) · UniProt [P11926](https://www.uniprot.org/uniprotkb/P11926) · Ensembl [ENSG00000115758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115758)

## Data

Gene col 3716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3716); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3716]; `tensor/DDL_lfc|DDL_z.npy` [3716]; `embed/gene_vectors.npy` [3716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3716 or target_col == 3716). Every well: [[ODC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
