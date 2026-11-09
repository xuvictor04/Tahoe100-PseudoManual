---
symbol: "SAMD8"
type: "gene"
col: 8004
ensembl_id: "ENSG00000156671"
name: "sterile alpha motif domain containing 8"
location: "10q22.2"
module: 3
arm: "+"
pooled_cpm: 113.39
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SAMD8

*sterile alpha motif domain containing 8* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.41× (z +13.0, q 1e-35, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.472× (z -20.0, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.811× (z -5.4, q 6e-06, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 0.0825×, SW 900 0.242×, NCI-H2347 0.336×, SNU-423 0.346×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.0980×, SW 900 0.184×, CFPAC-1 0.266×, SNU-423 0.365×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.274×, RPMI-7951 0.214×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF181]] (+0.60, fdr 2e-05), [[ING2]] (+0.60, fdr 1e-05), [[SIRT6]] (+0.60, fdr 2e-05); moves opposite to [[NUP210]] (-0.57, fdr 3e-05), [[HNRNPA3]] (-0.56, fdr 4e-05), [[CPSF6]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +13.0 | 1e-35 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +9.4 | 2e-18 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +7.5 | 1e-11 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.3 | 6e-11 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +6.8 | 1e-09 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.4 | 1e-08 | 28/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +5.8 | 7e-07 | 27/48 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.7 | 9e-07 | 26/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +5.2 | 1e-05 | 24/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.4 | 7e-04 | 17/48 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.012 | 21/48 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.021 | 16/47 (SK-MEL-2, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.022 | 14/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.4 | 0.023 | 11/49 (CFPAC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.09× | +3.4 | 0.025 | 3/48 (Hs 766T, AN3 CA, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.049 | 16/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.08× | +2.9 | 0.082 | 2/48 (SW 900, SW48) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8004.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 0.0825×, SW 900 0.242×, NCI-H2347 0.336×, SNU-423 0.346×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.0980×, SW 900 0.184×, CFPAC-1 0.266×, SNU-423 0.365×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.274×, RPMI-7951 0.214×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.472×** | -20.0 | 0e+00 | 43/49 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.459×** | -20.0 | 0e+00 | 40/44 (C-33 A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -11.4 | 1e-27 | 34/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -11.0 | 6e-26 | 4/50 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -7.9 | 2e-13 | 31/47 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.778×** | -6.4 | 1e-08 | 28/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.811×** | -5.4 | 6e-06 | 27/48 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.870× | -3.7 | 0.014 | 15/48 (RKO, AsPC-1, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.875× | -3.6 | 0.021 | 9/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.911× | -3.5 | 0.021 | 2/48 (LOX-IMVI, NCI-H661) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.876× | -3.5 | 0.021 | 20/48 (SW 900, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.091 | 8/48 (SW48, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 126 | 26 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 112 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.495× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 124 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 155 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 159 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -17.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 93.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -10.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.472× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 113 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.7) | — |
| [[A-172 (line)]] | wt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 167 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -13.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 132 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 130 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 52.6 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0825× (z -30.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -15.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -21.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -13.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -13.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.514× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 94.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 122 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0980× (z -25.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 89.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.482× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.465× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.509× (z -9.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -17.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF181]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ING2]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SIRT6]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[HMGCL]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[POLD4]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FBXL15]] | +0.53 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[IL17RA]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TUBA4A]] | +0.53 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[KATNA1]] | +0.53 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[NUDT22]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[CPT2]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP210]] | -0.57 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CPSF6]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TFDP1]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ILF3]] | -0.52 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[CAD]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[G3BP1]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MTHFD1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[UNG]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPR]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[LRPPRC]] | -0.50 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.50 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SAMD8's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.363). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.1, -28.5); signed map (-14.9, 0.6). **Vector** length 103, 27.5% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +9.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.8 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.0 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.7 | -20.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.6 | -20.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:75,099,586-75,182,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25082, SMSr |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LT4](https://www.uniprot.org/uniprotkb/Q96LT4) (Sphingomyelin synthase-related protein 1):

> Has phospholipase C (PLC) activity. Shows specificity for phosphatidylethanolamine (1,2-diacyl-sn-glycero-3-phosphoethanolamine, PE), hydrolyzing PE to produce phosphoethanolamine and diacylglycerol (1,2-diacyl-sn-glycerol, DAG). This reaction might act as a regulatory switch to activate serine palmitoyltransferase (SPT) and promote sphingolipid metabolism (By similarity). Can also function as a ceramide phosphoethanolamine (N-acylsphingoid 1-phosphoethanolamine, CPE) synthase when …

**Summary**, from NCBI Gene [142891](https://www.ncbi.nlm.nih.gov/gene/142891):

> Predicted to enable ceramide cholinephosphotransferase activity; ceramide phosphoethanolamine synthase activity; and sphingomyelin synthase activity. Involved in ceramide biosynthetic process and regulation of ceramide biosynthetic process. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26320) · Entrez [142891](https://www.ncbi.nlm.nih.gov/gene/142891) · UniProt [Q96LT4](https://www.uniprot.org/uniprotkb/Q96LT4) · Ensembl [ENSG00000156671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156671)

## Data

Gene col 8004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8004); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8004]; `tensor/DDL_lfc|DDL_z.npy` [8004]; `embed/gene_vectors.npy` [8004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8004 or target_col == 8004). Every well: [[SAMD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
