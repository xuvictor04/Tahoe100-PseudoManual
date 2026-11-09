---
symbol: "RBM33"
type: "gene"
col: 11583
ensembl_id: "ENSG00000184863"
name: "RNA binding motif protein 33"
location: "7q36.3"
module: 130
arm: "+"
pooled_cpm: 226.46
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# RBM33

*RNA binding motif protein 33* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.48× (z +13.1, q 1e-36, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.441× (z -13.2, q 9e-37, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.676× (z -9.2, q 3e-18, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUM2]] (+0.70, fdr 7e-06), [[VAPA]] (+0.68, fdr 7e-06), [[SIAH1]] (+0.67, fdr 7e-06); moves opposite to [[EHD4]] (-0.62, fdr 2e-05), [[KCTD5]] (-0.61, fdr 1e-05), [[MYO9B]] (-0.61, fdr 9e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLK2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.48×** | +13.1 | 1e-36 | 48/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +12.4 | 1e-32 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.51×** | +11.0 | 7e-26 | 45/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +10.4 | 5e-23 | 43/48 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +8.8 | 1e-16 | 44/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 3e-12 | 45/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 3e-11 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +5.5 | 2e-06 | 34/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.5 | 4e-04 | 30/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.5 | 5e-04 | 30/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.010 | 29/48 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.025 | 24/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.047 | 30/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.088 | 23/48 (LS 180, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.441×** | -13.2 | 9e-37 | 42/44 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.516×** | -11.0 | 8e-26 | 46/49 (NCI-H2347, NCI-H23, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.526×** | -10.7 | 1e-24 | 47/48 (A549, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.556×** | -9.8 | 2e-20 | 47/48 (A549, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -9.2 | 3e-18 | 45/49 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.588×** | -8.9 | 7e-17 | 48/48 (SW480, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.704×** | -5.6 | 1e-06 | 43/47 (CHP-212, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -5.5 | 3e-06 | 43/48 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -5.3 | 7e-06 | 37/48 (SNU-423, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -5.2 | 1e-05 | 37/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.749×** | -4.8 | 8e-05 | 41/48 (NCI-H661, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -4.4 | 4e-04 | 25/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.646×** | -3.8 | 0.006 | 35/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.020 | 28/48 (MIA PaCa-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.3 | 0.032 | 16/48 (A-172, NCI-H661, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.068 | 25/47 (AsPC-1, A498, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.879× | -3.0 | 0.081 | 5/48 (AsPC-1, SW 1271, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.707×** | -3.0 | 0.081 | 26/48 (COLO 205, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.711×** | -3.0 | 0.088 | 24/48 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 206 | 10 (2 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.5) |
| [[SW480 (line)]] | alt | 284 | 6 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.6) |
| [[A549 (line)]] | wt | 223 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -21.5) |
| [[LOX-IMVI (line)]] | wt | 231 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 232 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 242 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 256 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 262 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -25.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 238 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +13.9) | — |
| [[H4 (line)]] | wt | 150 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 162 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.473× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 132 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 261 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 188 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.7) |
| [[SW1417 (line)]] | alt | 380 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 267 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.1) |
| [[LS 180 (line)]] | wt | 173 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 183 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.576× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 266 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.60× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 236 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 226 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 238 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 236 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.23× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.468× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 312 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 230 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.18× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 298 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -22.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 471 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.1× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 208 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.91× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.1) |
| [[HT-29 (line)]] | alt | 281 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.10× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 213 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.08× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 246 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 221 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 173 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 217 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[J82 (line)]] | alt | 161 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 282 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 151 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.23× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 147 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.56× (z +8.9) | — |
| [[A-172 (line)]] | wt | 129 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -11.8) |
| [[CHP-212 (line)]] | wt | 223 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.3) |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 178 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.30× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 236 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.06× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~9% of this change |
| [[AN3 CA (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM2]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[VAPA]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SIAH1]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CHASERR]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MTMR3]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[ATG2B]] | +0.65 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[KCTD3]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[WAC]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RAB21]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CARF]] | +0.63 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KAT6A]] | +0.62 | +0.39 / +0.69 | both halves | 5e-05 |  |
| [[DYRK1A]] | +0.62 | +0.71 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[KCTD5]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.61 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[LRRFIP1]] | -0.60 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[ST3GAL1]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE28]] | -0.56 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[CMIP]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MPP3]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[TMEM184B]] | -0.54 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[DGKD]] | -0.54 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SEPTIN10]] | -0.53 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[SLC35E1]] | -0.53 | -0.23 / -0.52 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLK2]] | C | TLK2's natural level strengthens RBM33's drug response | TLK2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.8, 0.6); signed map (29.8, -24.2). **Vector** length 83.8, 34.9% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.9 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +10.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | -1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.4 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.6 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:155,644,451-155,781,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686F102, MGC20460, DKFZp434D1319; previously PRR8 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EV2](https://www.uniprot.org/uniprotkb/Q96EV2) (RNA-binding protein 33):

> RNA reader protein, which recognizes and binds specific RNAs, thereby regulating RNA metabolic processes, such as mRNA export, mRNA stability and/or translation. Binds a subset of intronless RNAs containing GC-rich elements, such as NORAD, and promotes their nuclear export by recruiting target RNAs to components of the NXF1-NXT1 RNA export machinery. Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, promoting their demethylation by ALKBH5. Acts as an molecular …

**Summary**, from NCBI Gene [155435](https://www.ncbi.nlm.nih.gov/gene/155435):

> Enables N6-methyladenosine-containing RNA reader activity and lncRNA binding activity. Involved in RNA export from nucleus and regulation of mRNA stability. Located in cytoplasm. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27223) · Entrez [155435](https://www.ncbi.nlm.nih.gov/gene/155435) · UniProt [Q96EV2](https://www.uniprot.org/uniprotkb/Q96EV2) · Ensembl [ENSG00000184863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184863)

## Data

Gene col 11583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11583); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11583]; `tensor/DDL_lfc|DDL_z.npy` [11583]; `embed/gene_vectors.npy` [11583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11583 or target_col == 11583). Every well: [[RBM33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
