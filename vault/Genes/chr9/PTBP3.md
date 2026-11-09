---
symbol: "PTBP3"
type: "gene"
col: 4050
ensembl_id: "ENSG00000119314"
name: "polypyrimidine tract binding protein 3"
location: "9q32"
module: 156
arm: "+"
pooled_cpm: 300.82
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# PTBP3

*polypyrimidine tract binding protein 3* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.29× (z +8.1, q 2e-13, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (NCI-H460 2.04×, PANC-1 1.97×, SW480 1.84×, KATO III 1.72×, …); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 1.76×, SW480 1.66×, PANC-1 1.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H460 1.64×, SW480 1.54×, PANC-1 1.54×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.677× (z -17.3, q 0e+00, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD2AP]] (+0.55, fdr 3e-05), [[PICALM]] (+0.54, fdr 2e-05), [[CMTM6]] (+0.54, fdr 2e-05); moves opposite to [[NGDN]] (-0.55, fdr 1e-05), [[CUL7]] (-0.55, fdr 5e-05), [[LRRC41]] (-0.55, fdr 7e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (NCI-H460 2.04×, PANC-1 1.97×, SW480 1.84×, KATO III 1.72×, …); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 1.76×, SW480 1.66×, PANC-1 1.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H460 1.64×, SW480 1.54×, PANC-1 1.54×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +8.1 | 2e-13 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +7.3 | 9e-11 | 27/47 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +6.6 | 1e-08 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.6 | 3e-06 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +5.3 | 1e-05 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +5.0 | 5e-05 | 21/48 (A498, RPMI-7951, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +4.0 | 0.006 | 10/47 (HOP62, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.12× | +3.6 | 0.026 | 11/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.11× | +3.4 | 0.037 | 18/49 (SW480, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.4 | 0.045 | 13/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.11× | +3.2 | 0.080 | 9/48 (H4, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -17.3 | 0e+00 | 34/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -15.5 | 0e+00 | 39/47 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.710×** | -10.7 | 1e-24 | 33/48 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.739×** | -9.5 | 4e-19 | 32/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -8.3 | 2e-14 | 31/48 (A498, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -8.1 | 6e-14 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.779×** | -7.8 | 4e-13 | 28/48 (SW1417, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.815×** | -6.2 | 5e-08 | 25/48 (SW 900, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.822×** | -6.2 | 5e-08 | 26/48 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.818×** | -6.1 | 8e-08 | 25/50 (SW 900, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.825×** | -6.0 | 9e-08 | 25/48 (SW 900, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -5.7 | 4e-07 | 24/48 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.840× | -5.5 | 2e-06 | 22/48 (SW 900, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.831×** | -4.8 | 5e-05 | 24/48 (COLO 205, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -4.8 | 7e-05 | 15/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.876× | -4.1 | 0.001 | 16/49 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.882× | -3.9 | 0.003 | 8/48 (SNU-423, BT-474, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.007 | 16/48 (LOX-IMVI, J82, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.862× | -3.3 | 0.023 | 10/49 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.890× | -3.2 | 0.035 | 7/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.875× | -3.0 | 0.069 | 13/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.935× | -3.0 | 0.072 | 7/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.928× | -2.8 | 0.096 | 5/49 (BT-474, SW 1088, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 378 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -11.4) |
| [[COLO 205 (line)]] | alt | 740 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -18.1) |
| [[SW480 (line)]] | alt | 275 | 4 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -13.4) |
| [[LS 180 (line)]] | wt | 520 | 2 (1 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.50× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -18.4) |
| [[A498 (line)]] | wt | 643 | 2 (2 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.97× (z +9.8) ⚠ cell-cycle shift, explains ~5% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -19.5) |
| [[A549 (line)]] | wt | 491 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -30.9) |
| [[LoVo (line)]] | wt | 436 | 2 (2 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.52× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 229 | 5 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +14.8) | [[Auranofin (drug)]] 5 µM 0.628× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 377 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -16.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -15.9) |
| [[SW 900 (line)]] | alt | 347 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 363 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -23.5) |
| [[HepG2_C3A (line)]] | wt | 455 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -13.5) |
| [[J82 (line)]] | alt | 483 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -13.2) |
| [[PANC-1 (line)]] | alt | 211 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.642× (z -9.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 306 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.1) |
| [[SW1417 (line)]] | alt | 378 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -13.1) |
| [[HS-578T (line)]] | alt | 203 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +9.7) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -9.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 317 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -23.6) |
| [[SNU-423 (line)]] | alt | 405 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.92× (z +9.1) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -15.0) |
| [[C-33 A (line)]] | alt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.25× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 161 | 2 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +11.4) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[CFPAC-1 (line)]] | alt | 284 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -16.5) |
| [[HCT15 (line)]] | alt | 409 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -17.9) |
| [[HOP62 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.556× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 344 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 268 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.521× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 309 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -10.0) |
| [[A-427 (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 291 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -12.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -13.5) |
| [[H4 (line)]] | wt | 157 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.530× (z -9.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 294 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -14.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 208 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.91× (z +8.5) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 205 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.32× (z +8.6) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[A-172 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 257 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD2AP]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PICALM]] | +0.54 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CMTM6]] | +0.54 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[ZDHHC2]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TMEM14C]] | +0.49 | +0.24 / +0.46 | both halves | 5e-04 |  |
| [[HYCC1]] | +0.49 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[CPT1A]] | +0.49 | +0.29 / +0.39 | both halves | 3e-04 |  |
| [[TACC1]] | +0.48 | +0.35 / +0.32 | both halves | 2e-04 |  |
| [[ARHGEF12]] | +0.48 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[GNG12]] | +0.48 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ROCK2]] | +0.48 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[SESTD1]] | +0.47 | +0.59 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGDN]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CUL7]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[LRRC41]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[TRMT44]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TM9SF4]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[TMEM101]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ORC2]] | -0.51 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[APTX]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PTCD1]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SPAG7]] | -0.51 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[PSMB5]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PTBP3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction -0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.8, 10.5); signed map (-13.7, 30.9). **Vector** length 117, 35.3% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.4 | -15.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -7.4 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | -7.0 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | polypyrimidine tract binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:112,217,716-112,333,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp781I1117; previously ROD1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95758](https://www.uniprot.org/uniprotkb/O95758) (Polypyrimidine tract-binding protein 3):

> RNA-binding protein that mediates pre-mRNA alternative splicing regulation. Plays a role in the regulation of cell proliferation, differentiation and migration. Positive regulator of EPO-dependent erythropoiesis. Participates in cell differentiation regulation by repressing tissue-specific exons. Promotes FAS exon 6 skipping. Binds RNA, preferentially to both poly(G) and poly(U).

**Summary**, from NCBI Gene [9991](https://www.ncbi.nlm.nih.gov/gene/9991):

> The protein encoded by this gene binds RNA and is a regulator of cell differentiation. The encoded protein preferentially binds to poly(G) and poly(U) sequences in vitro. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:10253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10253) · Entrez [9991](https://www.ncbi.nlm.nih.gov/gene/9991) · UniProt [O95758](https://www.uniprot.org/uniprotkb/O95758) · Ensembl [ENSG00000119314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119314)

## Data

Gene col 4050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4050); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4050]; `tensor/DDL_lfc|DDL_z.npy` [4050]; `embed/gene_vectors.npy` [4050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4050 or target_col == 4050). Every well: [[PTBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
