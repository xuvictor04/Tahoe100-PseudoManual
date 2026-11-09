---
symbol: "TMTC3"
type: "gene"
col: 6292
ensembl_id: "ENSG00000139324"
name: "transmembrane O-mannosyltransferase targeting cadherins 3"
location: "12q21.32"
module: 25
arm: "+"
pooled_cpm: 47.99
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TMTC3

*transmembrane O-mannosyltransferase targeting cadherins 3* — 12q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.36× (z +20.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.706× (z -6.0, q 1e-06, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.321×, HOP62 0.415×, J82 0.499×, SNU-423 0.523×, …; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.0990×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.413×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 1088 0.0662×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOCS2]] (+0.65, fdr 2e-05), [[API5]] (+0.65, fdr 3e-05), [[DLD]] (+0.64, fdr 2e-05); moves opposite to [[POLG2]] (-0.60, fdr 2e-05), [[PSD]] (-0.60, fdr 3e-05), [[USP36]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +20.6 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +20.4 | 0e+00 | 47/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +20.0 | 0e+00 | 47/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +18.2 | 0e+00 | 39/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +17.4 | 0e+00 | 34/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +10.8 | 3e-25 | 40/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +9.5 | 1e-19 | 33/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.6 | 5e-16 | 31/48 (KATO III, HOP62, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +8.1 | 2e-14 | 31/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +8.1 | 2e-14 | 39/48 (HT-29, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +7.3 | 1e-11 | 29/48 (A-427, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.37×** | +7.0 | 1e-10 | 27/44 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.7 | 1e-09 | 29/48 (HT-29, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +6.5 | 2e-09 | 29/48 (NCI-H460, A549, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +6.4 | 5e-09 | 31/48 (SW48, AsPC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +5.0 | 2e-05 | 17/47 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +4.9 | 3e-05 | 23/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 11/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.003 | 16/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.034 | 8/48 (SW480, SW48, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.051 | 7/48 (HT-29, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6292.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.321×, HOP62 0.415×, J82 0.499×, SNU-423 0.523×, …; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.0990×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.413×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW 1088 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.706×** | -6.0 | 1e-06 | 28/48 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -5.9 | 1e-06 | 24/48 (NCI-H2347, CHP-212, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.8 | 2e-04 | 24/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.791×** | -4.4 | 0.002 | 20/48 (A-427, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.901× | -3.5 | 0.049 | 11/49 (A-172, Hs 766T, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.17 | 7/48 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 55.4 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.61× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 51.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.27× (z +9.9) | — |
| [[J82 (line)]] | alt | 40.6 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 36.8 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.413× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 57.0 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.39× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 64.4 | 5 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.33× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 40.8 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 45.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 41.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 36.5 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.40× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.92× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 47.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.38× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.54× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 56.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +13.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 46.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.43× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 49.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 34.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 51.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 60.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 83.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +12.9) | — |
| [[RKO (line)]] | wt | 46.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.33× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 49.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.4) | — |
| [[A549 (line)]] | wt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +13.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 53.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 50.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.43× (z +9.0) | — |
| [[A-427 (line)]] | wt | 69.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[H4 (line)]] | wt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 61.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.55× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0990× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 67.9 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0662× (z -9.2) |
| [[SW1417 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.347× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS2]] | +0.65 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[API5]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[DLD]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[EXT2]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[EXOC5]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.62 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[OPA1]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.60 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[PHF6]] | +0.60 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[SYNJ2BP]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ELMOD2]] | +0.59 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[RAD23B]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLG2]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PSD]] | -0.60 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[USP36]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[IL34]] | -0.58 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MIA]] | -0.58 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[BOLA1]] | -0.57 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[THUMPD3-AS1]] | -0.57 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ARMC5]] | -0.56 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[SPATC1]] | -0.56 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[F12]] | -0.55 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[TGIF2-RAB5IF]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NEK8]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.0, -15.4); signed map (-16.9, -42.8). **Vector** length 105, 27.8% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +17.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -12.7 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.0 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -4.2 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.2 | -4.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane O-mannosyltransferase targeting cadherins 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.32 — chr12:88,142,296-88,199,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90492, SMILE |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Transmembrane O-mannosyltransferase targeting cadherins |
| Reactome | 8 pathways, smallest: Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Regulation of CDH1 Expression and Function; Regulation of Expression and Function of Type I Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZXV5](https://www.uniprot.org/uniprotkb/Q6ZXV5) (Protein O-mannosyl-transferase TMTC3):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. The 4 members of the TMTC family are O-mannosyl-transferases dedicated primarily to the cadherin superfamily, each member seems to have a distinct role in decorating the cadherin domains with O-linked mannose glycans at specific regions. Also acts as O-mannosyl-transferase on other proteins such as PDIA3. Involved in the positive regulation of proteasomal protein degradation in the endoplasmic reticulum (ER), and …

**Summary**, from NCBI Gene [160418](https://www.ncbi.nlm.nih.gov/gene/160418):

> This gene encodes a protein that belongs to the transmembrane and tetratricopeptide repeat-containing protein family. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:26899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26899) · Entrez [160418](https://www.ncbi.nlm.nih.gov/gene/160418) · UniProt [Q6ZXV5](https://www.uniprot.org/uniprotkb/Q6ZXV5) · Ensembl [ENSG00000139324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139324)

## Data

Gene col 6292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6292); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6292]; `tensor/DDL_lfc|DDL_z.npy` [6292]; `embed/gene_vectors.npy` [6292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6292 or target_col == 6292). Every well: [[TMTC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMTC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
