---
symbol: "SUMF2"
type: "gene"
col: 4948
ensembl_id: "ENSG00000129103"
name: "sulfatase modifying factor 2"
location: "7p11.2"
module: 29
arm: "+"
pooled_cpm: 49.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SUMF2

*sulfatase modifying factor 2* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +16.5, q 0e+00, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Omeprazole (drug)]] 0.5 µM: 1.24× (z +3.3, q 0.063, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 3.49×, LoVo 4.71×, KATO III 3.87×, HOP62 4.17×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 5.22×, SK-MEL-2 4.72×, HEC-1-A 2.97×, A498 2.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.41×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.337× (z -23.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCN2]] (+0.70, fdr 7e-06), [[SIAE]] (+0.67, fdr 7e-06), [[ATP6AP2]] (+0.67, fdr 7e-06); moves opposite to [[NSRP1]] (-0.69, fdr 7e-06), [[DNTTIP2]] (-0.68, fdr 7e-06), [[GLRX2]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4948.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HEC-1-A 3.49×, LoVo 4.71×, KATO III 3.87×, HOP62 4.17×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 5.22×, SK-MEL-2 4.72×, HEC-1-A 2.97×, A498 2.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.41×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +16.5 | 0e+00 | 46/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +14.1 | 6e-43 | 37/39 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +11.1 | 2e-26 | 40/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.34×** | +4.6 | 6e-04 | 28/47 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.5 | 1e-03 | 27/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.32×** | +4.3 | 0.002 | 27/48 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.033 | 16/35 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.063 | 15/48 (COLO 205, PANC-1, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.17 | 11/47 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.337×** | -23.9 | 0e+00 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.387×** | -14.7 | 0e+00 | 44/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.542×** | -8.9 | 1e-16 | 42/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.650×** | -6.2 | 6e-08 | 31/48 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.762×** | -4.2 | 0.003 | 25/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.755×** | -4.1 | 0.004 | 22/47 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.005 | 28/48 (A-172, C32, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -3.6 | 0.026 | 18/48 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.598×** | -3.5 | 0.026 | 20/47 (SK-MEL-2, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.786×** | -3.5 | 0.029 | 21/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.059 | 11/47 (KATO III, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.812× | -3.0 | 0.12 | 15/48 (SNU-1, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.6) |
| [[SW480 (line)]] | alt | 61.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.9) |
| [[A498 (line)]] | wt | 65.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 69.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -8.8) |
| [[HOP62 (line)]] | alt | 38.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.8) |
| [[KATO III (line)]] | alt | 96.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.2) |
| [[LoVo (line)]] | wt | 27.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 37.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0401× (z -30.9) |
| [[PANC-1 (line)]] | alt | 70.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -23.4) |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.7) |
| [[A549 (line)]] | wt | 42.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 34.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.8) |
| [[J82 (line)]] | alt | 52.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.9) |
| [[NCI-H2347 (line)]] | alt | 56.7 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.2) ⚠ cell-cycle shift, explains ~1% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.6) |
| [[A-172 (line)]] | wt | 58.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.6) |
| [[A-427 (line)]] | wt | 79.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.3) |
| [[C32 (line)]] | wt | 74.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -15.7) |
| [[H4 (line)]] | wt | 67.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.0) |
| [[Hs 766T (line)]] | wt | 34.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -13.3) |
| [[HT-29 (line)]] | alt | 44.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.9) |
| [[LS 180 (line)]] | wt | 43.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 42.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.1) |
| [[RKO (line)]] | wt | 39.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -9.1) |
| [[SNU-1 (line)]] | wt | 38.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.5) |
| [[SNU-423 (line)]] | alt | 60.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.1) |
| [[SW1417 (line)]] | alt | 64.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.8) |
| [[SW48 (line)]] | wt | 60.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.5) |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.2) |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.3) |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.9) |
| [[HS-578T (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.6) |
| [[SHP-77 (line)]] | alt | 74.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.5) |
| [[SW 1088 (line)]] | alt | 67.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0755× (z -12.3) |
| [[SW 900 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[SIAE]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ATP6AP2]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SELENON]] | +0.65 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[PPT1]] | +0.65 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[TMED10]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ASAH1]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism |
| [[GAA]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[DDOST]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.61 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[SOD3]] | +0.60 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GINM1]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.69 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[DNTTIP2]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[GLRX2]] | -0.65 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[CCDC137]] | -0.64 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.63 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[UBXN4]] | -0.62 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[DAXX]] | -0.62 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PPID]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[C3orf20]] | -0.59 | -0.69 / -0.39 | both halves | 6e-05 |  |
| [[SLC22A1]] | -0.58 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SNRNP27]] | -0.57 | -0.71 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.6, -19.0); signed map (-25.8, -37.3). **Vector** length 82.7, 20.9% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.5 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -23.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sulfatase modifying factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:56,064,002-56,080,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566I1024 |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBJ7](https://www.uniprot.org/uniprotkb/Q8NBJ7) (Inactive C-alpha-formylglycine-generating enzyme 2):

> Lacks formylglycine generating activity and is unable to convert newly synthesized inactive sulfatases to their active form. Inhibits the activation of sulfatases by SUMF1.

**Summary**, from NCBI Gene [25870](https://www.ncbi.nlm.nih.gov/gene/25870):

> The catalytic sites of sulfatases are only active if they contain a unique amino acid, C-alpha-formylglycine (FGly). The FGly residue is posttranslationally generated from a cysteine by enzymes with FGly-generating activity. The gene described in this record is a member of the sulfatase-modifying factor family and encodes a protein with a DUF323 domain that localizes to the lumen of the endoplasmic reticulum. This protein has low levels of FGly-generating activity but can heterodimerize with …

**Accessions** — [HGNC:20415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20415) · Entrez [25870](https://www.ncbi.nlm.nih.gov/gene/25870) · UniProt [Q8NBJ7](https://www.uniprot.org/uniprotkb/Q8NBJ7) · Ensembl [ENSG00000129103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129103)

## Data

Gene col 4948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4948); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4948]; `tensor/DDL_lfc|DDL_z.npy` [4948]; `embed/gene_vectors.npy` [4948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4948 or target_col == 4948). Every well: [[SUMF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUMF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
