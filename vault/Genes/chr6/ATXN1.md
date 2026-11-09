---
symbol: "ATXN1"
type: "gene"
col: 4573
ensembl_id: "ENSG00000124788"
name: "ataxin 1"
location: "6p22.3"
module: 175
arm: "+"
pooled_cpm: 483.98
n_lines_expressing: 44
n_dd_up: 2
n_dd_down: 39
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 24
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ATXN1

*ataxin 1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.54× (z +7.0, q 2e-09, up in 38 of 41 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.47× (z +4.9, q 3e-04, up in 36 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 2 lines (NCI-H23 2.69×, NCI-H460 2.62×; ⚠ cell-cycle shift, explains ~27% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 1.84×, LoVo 1.71×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.25×; ⚠ cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (21 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.292× (z -20.4, q 0e+00, down in 42 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.516× (z -15.5, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB20]] (+0.59, fdr 9e-05), [[FER]] (+0.53, fdr 1e-04), [[LYST]] (+0.52, fdr 2e-05); moves opposite to [[PRMT7]] (-0.58, fdr 3e-05), [[ALG6]] (-0.56, fdr 2e-05), [[GK5]] (-0.53, fdr 4e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRKCA]] → it (grade B ⚠); 24 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 2 lines (NCI-H23 2.69×, NCI-H460 2.62×; ⚠ cell-cycle shift, explains ~27% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 1.84×, LoVo 1.71×); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 2.25×; ⚠ cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +7.0 | 2e-09 | 38/41 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 3e-04 | 36/41 (NCI-H23, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.22× | +3.3 | 0.14 | 21/41 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.45× | +3.3 | 0.14 | 22/42 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.23× | +3.2 | 0.14 | 22/44 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.43× | +3.1 | 0.17 | 19/42 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.20 | 17/42 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 23 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.292×** | -20.4 | 0e+00 | 42/42 (HT-29, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.314×** | -19.2 | 0e+00 | 42/42 (HT-29, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.306×** | -18.9 | 0e+00 | 41/41 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -15.5 | 0e+00 | 39/43 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.413×** | -14.6 | 0e+00 | 42/42 (HT-29, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.413×** | -14.1 | 3e-43 | 35/39 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.458×** | -12.0 | 4e-31 | 38/39 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.418×** | -11.0 | 2e-26 | 41/43 (SW480, C32, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.664×** | -9.6 | 8e-20 | 28/42 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.529×** | -8.0 | 6e-14 | 42/42 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.632×** | -7.6 | 2e-12 | 38/42 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.438×** | -7.2 | 4e-11 | 29/34 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.660×** | -6.6 | 2e-09 | 32/41 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.692×** | -5.9 | 2e-07 | 34/42 (C32, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.700×** | -5.7 | 5e-07 | 33/44 (SNU-423, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.532×** | -5.5 | 2e-06 | 37/42 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.3 | 4e-06 | 26/42 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.579×** | -4.7 | 6e-05 | 32/42 (NCI-H460, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **0.822×** | -4.5 | 1e-04 | 24/42 (SW480, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.5 | 2e-04 | 26/42 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.765×** | -4.2 | 5e-04 | 23/43 (HOP62, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -4.2 | 7e-04 | 29/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[EX229 (drug)]] 5 µM |  | **0.619×** | -4.1 | 7e-04 | 30/42 (SW48, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.631×** | -4.0 | 0.001 | 26/42 (NCI-H1792, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.857× | -3.6 | 0.006 | 10/43 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.008 | 30/41 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.016 | 22/42 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.016 | 25/43 (NCI-H460, SW48, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.757×** | -3.3 | 0.016 | 25/42 (NCI-H460, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 798 | 0 | 18 (15 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -22.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -20.4) |
| [[KATO III (line)]] | alt | 875 | 0 | 13 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.4) |
| [[PANC-1 (line)]] | alt | 563 | 0 | 13 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -23.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -17.0) |
| [[HOP62 (line)]] | alt | 643 | 1 (1 ⚠) | 11 (10 ⚠) | [[Harringtonine (drug)]] 5 µM 2.25× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -16.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 784 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -24.4) |
| [[SW480 (line)]] | alt | 866 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -24.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -22.1) |
| [[HepG2_C3A (line)]] | wt | 1,172 | 0 | 11 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.190× (z -19.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.3) |
| [[HT-29 (line)]] | alt | 1,065 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -27.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 331 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -9.3) |
| [[SNU-423 (line)]] | alt | 905 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -17.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 522 | 1 (1 ⚠) | 9 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.62× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -18.3) |
| [[A549 (line)]] | wt | 319 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 418 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -17.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.6) |
| [[Hs 766T (line)]] | wt | 373 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.414× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 395 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.7) |
| [[LoVo (line)]] | wt | 369 | 1 | 8 (8 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.71× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SK-MEL-2 (line)]] | alt | 448 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.3) |
| [[SNU-1 (line)]] | wt | 186 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.265× (z -11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.386× (z -8.6) |
| [[A-172 (line)]] | wt | 341 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 467 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -24.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 487 | 1 (1 ⚠) | 7 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.69× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 487 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -19.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.269× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 457 | 1 (1 ⚠) | 6 (5 ⚠) | [[Trametinib (drug)]] 5 µM 2.25× (z +8.5) ⚠ cell-cycle shift, explains ~66% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -14.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -8.7) |
| [[LS 180 (line)]] | wt | 598 | 1 | 6 (6 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.274× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 341 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -20.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.8) |
| [[J82 (line)]] | alt | 387 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -13.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 513 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -14.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 415 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -11.6) |
| [[A498 (line)]] | wt | 224 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.0) |
| [[COLO 205 (line)]] | alt | 719 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -20.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 593 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.1) |
| [[HCT15 (line)]] | alt | 493 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW 1271 (line)]] | alt | 743 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -12.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 1,097 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.9) |
| [[CHP-212 (line)]] | wt | 447 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.182× (z -15.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -12.4) |
| [[HS-578T (line)]] | alt | 680 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -14.3) |
| [[BT-474 (line)]] | alt | 488 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.6) |
| [[SW1417 (line)]] | alt | 279 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -11.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 249 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -10.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 333 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 263 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 537 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 96.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 79.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 55.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 469 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 524 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB20]] | +0.59 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[FER]] | +0.53 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[LYST]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[EBF1]] | +0.52 | +0.50 / +0.43 | both halves | 4e-05 |  |
| [[LINC01619]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[RPS6KA3]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PRKCA]] | +0.51 | +0.48 / +0.43 | both halves | 4e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[KIAA1217]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ACVR1C]] | +0.49 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[FRYL]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[NR3C1]] | +0.48 | +0.40 / +0.46 | both halves | 5e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[AHR]] | +0.48 | +0.36 / +0.41 | both halves | 9e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT7]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ALG6]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[GK5]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SNX4]] | -0.50 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[SFXN2]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DUSP11]] | -0.49 | -0.32 / -0.42 | both halves | 2e-04 | STRING 492 |
| [[SNRPA1]] | -0.49 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PRKX]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[ABCB10]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[NSUN2]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TAF5L]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MRPL3]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCA]] | B | PRKCA activity raises ATXN1's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 4.79× lower at baseline in the lines without PRKCA | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[AHR]] | B | AHR activity raises ATXN1's level | lines that do not express AHR (7) vs lines expressing it (43) | 4.48× lower at baseline in the lines without AHR | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[TOP2A]] | B | TOP2A activity raises ATXN1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYTL2]] | C | SYTL2 activity raises ATXN1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 4.69× lower at baseline in the lines without SYTL2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent; co-absent with the target |
| [[SSUH2]] | C | SSUH2 activity raises ATXN1's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 7.76× lower at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 22, C 2. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | ATXN1 activity raises PLD1's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 4.40× lower at baseline in the lines without ATXN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[KIAA1217]] | B | ATXN1 activity raises KIAA1217's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 5.24× lower at baseline in the lines without ATXN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[PRKCA]] | B | ATXN1 activity raises PRKCA's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without ATXN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[POLR1B]] | B | ATXN1 activity lowers POLR1B's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.09× higher at baseline in the lines without ATXN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[MARCKS]] | B | ATXN1 activity raises MARCKS's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without ATXN1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | ATXN1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 0.86× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[WDR3]] | B | ATXN1 activity lowers WDR3's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.80× higher at baseline in the lines without ATXN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[MTERF3]] | B | ATXN1 activity lowers MTERF3's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.74× higher at baseline in the lines without ATXN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | B | ATXN1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 0.55× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[SFXN2]] | B | ATXN1 activity lowers SFXN2's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without ATXN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[WDR5]] | B | ATXN1 activity lowers WDR5's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without ATXN1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[RNF138]] | B | ATXN1 activity lowers RNF138's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.53× higher at baseline in the lines without ATXN1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction -0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.2, -15.9); signed map (8.3, 21.1). **Vector** length 101, 39.4% of its response variance represented; |z| ≥ 3 in 1,764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.2 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -18.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.9 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.7 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -3.6 | -14.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:16,299,112-16,761,491 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S504E, ATX1; previously SCA1 |
| Gene groups (HGNC) | Ataxin 1 family |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [P54253](https://www.uniprot.org/uniprotkb/P54253) (Ataxin-1):

> Chromatin-binding factor that repress Notch signaling in the absence of Notch intracellular domain by acting as a CBF1 corepressor. Binds to the HEY promoter and might assist, along with NCOR2, RBPJ-mediated repression. Binds RNA in vitro. May be involved in RNA metabolism. In concert with CIC and ATXN1L, involved in brain development (By similarity).

**Summary**, from NCBI Gene [6310](https://www.ncbi.nlm.nih.gov/gene/6310):

> The autosomal dominant cerebellar ataxias (ADCA) are a heterogeneous group of neurodegenerative disorders characterized by progressive degeneration of the cerebellum, brain stem and spinal cord. Clinically, ADCA has been divided into three groups: ADCA types I-III. ADCAI is genetically heterogeneous, with five genetic loci, designated spinocerebellar ataxia (SCA) 1, 2, 3, 4 and 6, being assigned to five different chromosomes. ADCAII, which always presents with retinal degeneration (SCA7), and …

**Accessions** — [HGNC:10548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10548) · Entrez [6310](https://www.ncbi.nlm.nih.gov/gene/6310) · UniProt [P54253](https://www.uniprot.org/uniprotkb/P54253) · Ensembl [ENSG00000124788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124788)

## Data

Gene col 4573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4573); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4573]; `tensor/DDL_lfc|DDL_z.npy` [4573]; `embed/gene_vectors.npy` [4573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4573 or target_col == 4573). Every well: [[ATXN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
