---
symbol: "YAP1"
type: "gene"
col: 6049
ensembl_id: "ENSG00000137693"
name: "Yes1 associated transcriptional regulator"
location: "11q22.1"
module: 217
arm: "+"
pooled_cpm: 312.21
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# YAP1

*Yes1 associated transcriptional regulator* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.35× (z +8.9, q 4e-16, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.220× (z -30.6, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIPK3]] (+0.61, fdr 1e-05), [[LINC01145-1]] (+0.59, fdr 3e-05), [[SLC26A2]] (+0.59, fdr 3e-05); moves opposite to [[KCTD21]] (-0.60, fdr 7e-05), [[ADAMTS16]] (-0.60, fdr 1e-05), [[SAMD4B]] (-0.59, fdr 4e-05).
> It is in [[Module 217]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +8.9 | 4e-16 | 46/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +7.0 | 7e-10 | 39/47 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 6e-09 | 39/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.6 | 7e-09 | 34/47 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +6.2 | 5e-08 | 40/47 (NCI-H2030, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.5 | 4e-06 | 31/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 9e-05 | 32/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 6e-04 | 22/47 (SNU-1, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 0.001 | 26/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.010 | 23/47 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.037 | 18/47 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.052 | 14/47 (HT-29, A-427, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.070 | 18/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.11× | +3.1 | 0.073 | 0/47 | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.086 | 19/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.099 | 3/47 (A-427, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.220×** | -30.6 | 0e+00 | 47/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.220×** | -30.6 | 0e+00 | 47/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.265×** | -26.8 | 0e+00 | 47/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.537×** | -12.6 | 5e-34 | 45/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.546×** | -12.2 | 2e-32 | 45/47 (NCI-H23, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -10.1 | 4e-22 | 43/46 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.608×** | -10.0 | 9e-22 | 43/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.614×** | -9.8 | 6e-21 | 45/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.649×** | -8.4 | 3e-15 | 36/43 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -6.2 | 3e-08 | 35/47 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.558×** | -6.0 | 8e-08 | 46/48 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -5.8 | 3e-07 | 32/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.746×** | -5.4 | 2e-06 | 28/44 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -5.0 | 2e-05 | 31/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.796×** | -4.6 | 2e-04 | 28/47 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.657×** | -4.4 | 5e-04 | 36/47 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -4.1 | 0.001 | 20/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -4.0 | 0.002 | 24/47 (SW480, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.685×** | -3.9 | 0.003 | 29/47 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.732×** | -3.2 | 0.034 | 25/47 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 290 | 14 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 2.06× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.259× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 211 | 10 (4 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.27× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.233× (z -20.4) |
| [[SW480 (line)]] | alt | 529 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0665× (z -37.4) |
| [[NCI-H2030 (line)]] | alt | 388 | 3 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.07× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.225× (z -22.6) |
| [[NCI-H2347 (line)]] | alt | 331 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -25.4) |
| [[CFPAC-1 (line)]] | alt | 315 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -25.2) |
| [[HepG2_C3A (line)]] | wt | 365 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0693× (z -34.8) |
| [[SNU-1 (line)]] | wt | 395 | 6 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.49× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.240× (z -15.3) |
| [[BT-474 (line)]] | alt | 535 | 4 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.11× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -26.2) |
| [[C32 (line)]] | wt | 342 | 2 | 7 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.01× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 283 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.17× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.128× (z -28.0) |
| [[SW48 (line)]] | wt | 567 | 1 | 8 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.43× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.0820× (z -26.3) |
| [[AsPC-1 (line)]] | alt | 269 | 3 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.182× (z -23.4) |
| [[HT-29 (line)]] | alt | 302 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -19.7) |
| [[NCI-H23 (line)]] | alt | 476 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -24.6) |
| [[PANC-1 (line)]] | alt | 372 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.92× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -21.8) |
| [[A549 (line)]] | wt | 221 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.07× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.148× (z -26.0) |
| [[LS 180 (line)]] | wt | 318 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.159× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 230 | 2 (2 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.200× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 302 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -22.7) |
| [[SNU-423 (line)]] | alt | 241 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -22.4) |
| [[HOP62 (line)]] | alt | 182 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -28.5) |
| [[LoVo (line)]] | wt | 187 | 1 (1 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.230× (z -22.1) |
| [[LOX-IMVI (line)]] | wt | 352 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -23.1) |
| [[RKO (line)]] | wt | 270 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.94× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -20.4) |
| [[SW 900 (line)]] | alt | 238 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -22.3) |
| [[SW1417 (line)]] | alt | 589 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -27.7) |
| [[COLO 205 (line)]] | alt | 438 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -23.2) |
| [[HCT15 (line)]] | alt | 288 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 262 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -26.5) |
| [[J82 (line)]] | alt | 151 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -17.8) |
| [[KATO III (line)]] | alt | 505 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -24.5) |
| [[RPMI-7951 (line)]] | alt | 238 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -17.7) |
| [[SW 1271 (line)]] | alt | 619 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -11.5) |
| [[A-427 (line)]] | wt | 1,000 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -21.0) |
| [[HS-578T (line)]] | alt | 235 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -24.3) |
| [[hTERT-HPNE (line)]] | wt | 242 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 198 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -20.1) |
| [[A-172 (line)]] | wt | 126 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -16.5) |
| [[A498 (line)]] | wt | 149 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -16.2) |
| [[AN3 CA (line)]] | alt | 292 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -12.6) |
| [[C-33 A (line)]] | alt | 277 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -20.2) |
| [[CHP-212 (line)]] | wt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -11.1) |
| [[H4 (line)]] | wt | 196 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -16.0) |
| [[SW 1088 (line)]] | alt | 230 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0769× (z -14.0) |
| [[NCI-H661 (line)]] | alt | 334 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIPK3]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LINC01145-1]] | +0.59 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SLC26A2]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PTPN2]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ARID1B]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[CFLAR]] | +0.57 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[TNS2]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MAP3K1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 | STRING 407 |
| [[LINC00623]] | +0.56 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[STXBP5-AS1]] | +0.55 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[ZBTB2]] | +0.55 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[CAV1]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD21]] | -0.60 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[ADAMTS16]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.59 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SEC22B]] | -0.57 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PCYT1A]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.57 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[TMOD1]] | -0.56 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[AAK1]] | -0.56 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[GCKR]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TVP23C-CDRT4]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[LINC02693]] | -0.55 | -0.22 / -0.63 | both halves | 6e-04 |  |
| [[CLN8]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.6, 16.0); signed map (26.3, -18.3). **Vector** length 124, 49.2% of its response variance represented; |z| ≥ 3 in 1,707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.3 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.0 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.8 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.2 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.1 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.9 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.9 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.3 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.5 | -12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.4 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | Yes1 associated transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:102,110,447-102,233,424 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YAP65, YAP-1 |
| Gene groups (HGNC) | TEAD interacting region 3, omega loop domain containing |
| Reactome | 27 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; Zygotic genome activation (ZGA); Formation of axial mesoderm |
| Matched by | ensembl_id |

**Function**, from UniProt [P46937](https://www.uniprot.org/uniprotkb/P46937) (Transcriptional coactivator YAP1):

> Transcriptional regulator with dual roles as a coactivator and corepressor. Critical downstream regulatory target in the Hippo signaling pathway, crucial for organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The Hippo signaling pathway core involves a kinase cascade featuring STK3/MST2 and STK4/MST1, along with its regulatory partner SAV1, which phosphorylates and activates LATS1/2 in complex with their regulatory protein, MOB1. This activation leads …

**Summary**, from NCBI Gene [10413](https://www.ncbi.nlm.nih.gov/gene/10413):

> This gene encodes a downstream nuclear effector of the Hippo signaling pathway which is involved in development, growth, repair, and homeostasis. This gene is known to play a role in the development and progression of multiple cancers as a transcriptional regulator of this signaling pathway and may function as a potential target for cancer treatment. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:16262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16262) · Entrez [10413](https://www.ncbi.nlm.nih.gov/gene/10413) · UniProt [P46937](https://www.uniprot.org/uniprotkb/P46937) · Ensembl [ENSG00000137693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137693)

## Data

Gene col 6049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6049); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6049]; `tensor/DDL_lfc|DDL_z.npy` [6049]; `embed/gene_vectors.npy` [6049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6049 or target_col == 6049). Every well: [[YAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
