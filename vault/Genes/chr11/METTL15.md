---
symbol: "METTL15"
type: "gene"
col: 9814
ensembl_id: "ENSG00000169519"
name: "methyltransferase 15, mitochondrial 12S rRNA N4-cytidine"
location: "11p14.1"
module: 213
arm: "+"
pooled_cpm: 236.66
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# METTL15

*methyltransferase 15, mitochondrial 12S rRNA N4-cytidine* — 11p14.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 1.87×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.353× (z -17.8, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.626× (z -11.3, q 7e-28, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCK]] (+0.66, fdr 1e-05), [[PRELID2]] (+0.60, fdr 1e-05), [[ELP4]] (+0.58, fdr 3e-05); moves opposite to [[NATD1]] (-0.48, fdr 4e-05), [[CDYL2]] (-0.48, fdr 4e-05), [[VIPR2]] (-0.45, fdr 2e-04).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 1.87×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.98 | 24/47 (NCI-H2347, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.353×** | -17.8 | 0e+00 | 47/49 (A-427, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.373×** | -16.3 | 0e+00 | 43/44 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.377×** | -15.5 | 0e+00 | 43/45 (SNU-423, HCT15, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.409×** | -15.3 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.432×** | -13.8 | 3e-41 | 47/47 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.470×** | -12.9 | 4e-36 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -12.3 | 8e-33 | 44/47 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -11.3 | 7e-28 | 38/49 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.632×** | -11.1 | 9e-27 | 38/48 (C32, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.525×** | -10.6 | 2e-24 | 45/48 (A498, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.552×** | -10.2 | 1e-22 | 43/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.598×** | -8.8 | 7e-17 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -8.4 | 1e-15 | 41/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -7.9 | 1e-13 | 44/49 (C32, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.645×** | -7.5 | 2e-12 | 44/48 (HOP62, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -6.9 | 2e-10 | 39/48 (HCT15, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -5.8 | 2e-07 | 35/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.528×** | -5.7 | 3e-07 | 32/48 (SNU-1, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.728×** | -5.4 | 1e-06 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -5.2 | 5e-06 | 34/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -4.6 | 9e-05 | 32/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -4.3 | 3e-04 | 23/48 (Hs 766T, hTERT-HPNE, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 8e-04 | 29/47 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.858× | -3.7 | 0.004 | 13/49 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.011 | 26/49 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.013 | 25/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.708×** | -3.1 | 0.031 | 25/49 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 349 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -27.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0994× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 278 | 0 | 17 (15 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -19.0) |
| [[H4 (line)]] | wt | 353 | 0 | 15 (13 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 249 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -19.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -13.5) |
| [[HOP62 (line)]] | alt | 290 | 0 | 13 (13 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0160× (z -28.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 314 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.5) |
| [[PANC-1 (line)]] | alt | 193 | 0 | 13 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -24.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.516× (z -9.2) |
| [[SNU-423 (line)]] | alt | 325 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -24.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.463× (z -10.1) |
| [[SW480 (line)]] | alt | 256 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -24.9) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.390× (z -11.1) |
| [[SNU-1 (line)]] | wt | 327 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0886× (z -15.1) |
| [[A498 (line)]] | wt | 316 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -25.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.9) |
| [[HCT15 (line)]] | alt | 303 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 298 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.9) |
| [[LS 180 (line)]] | wt | 272 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -19.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 222 | 0 | 10 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -17.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.502× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 292 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 251 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -16.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -13.3) |
| [[A-427 (line)]] | wt | 224 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.256× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 169 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -16.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.8) |
| [[HT-29 (line)]] | alt | 261 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 219 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -12.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.5) |
| [[SW48 (line)]] | wt | 232 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -13.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.269× (z -11.7) |
| [[A549 (line)]] | wt | 243 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -19.1) |
| [[BT-474 (line)]] | alt | 158 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -19.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.3) |
| [[C-33 A (line)]] | alt | 246 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.445× (z -9.8) |
| [[Hs 766T (line)]] | wt | 359 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.598× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 243 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.1) |
| [[HS-578T (line)]] | alt | 181 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.288× (z -13.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 244 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.8) |
| [[SW 900 (line)]] | alt | 132 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.203× (z -8.8) |
| [[A-172 (line)]] | wt | 224 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 164 | 1 (1 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.87× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -16.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 235 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 120 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 141 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 261 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -11.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | +0.66 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[PRELID2]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ELP4]] | +0.58 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[IFT43]] | +0.58 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[PDSS2]] | +0.55 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LINC01473]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[EMC2]] | +0.53 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[EXOC4]] | +0.53 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[COX15]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[AP3B1]] | +0.52 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[MBD5]] | +0.52 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[NBAS]] | +0.52 | +0.36 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NATD1]] | -0.48 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CDYL2]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[VIPR2]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[SMURF1]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RAP1GAP2]] | -0.45 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[SSPOP]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CCDC69]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[FURIN]] | -0.44 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[TP53I11]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PPP1R14C]] | -0.44 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[TMEM150C]] | -0.43 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[HES2]] | -0.43 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.4, 28.7); signed map (-20.2, 1.8). **Vector** length 77.6, 31.9% of its response variance represented; |z| ≥ 3 in 1,529 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | -1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.5 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | -0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.9 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.0 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -5.9 | -16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.4 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.7 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 15, mitochondrial 12S rRNA N4-cytidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:28,108,248-28,527,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33979; previously METT5D1 |
| Gene groups (HGNC) | 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NJ78](https://www.uniprot.org/uniprotkb/A6NJ78) (12S rRNA N(4)-cytidine methyltransferase METTL15):

> N4-methylcytidine (m4C) methyltransferase responsible for the methylation of position C839 in mitochondrial 12S rRNA. Involved in the stabilization of 12S rRNA folding, therefore facilitating the assembly of the mitochondrial small ribosomal subunits.

**Summary**, from NCBI Gene [196074](https://www.ncbi.nlm.nih.gov/gene/196074):

> Enables rRNA (cytosine-N4-)-methyltransferase activity. Involved in mitochondrial small ribosomal subunit assembly and rRNA base methylation. Is active in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26606) · Entrez [196074](https://www.ncbi.nlm.nih.gov/gene/196074) · UniProt [A6NJ78](https://www.uniprot.org/uniprotkb/A6NJ78) · Ensembl [ENSG00000169519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169519)

## Data

Gene col 9814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9814); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9814]; `tensor/DDL_lfc|DDL_z.npy` [9814]; `embed/gene_vectors.npy` [9814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9814 or target_col == 9814). Every well: [[METTL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
