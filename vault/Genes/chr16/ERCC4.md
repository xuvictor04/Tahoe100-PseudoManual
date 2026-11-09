---
symbol: "ERCC4"
type: "gene"
col: 10629
ensembl_id: "ENSG00000175595"
name: "ERCC excision repair 4, endonuclease catalytic subunit"
location: "16p13.12"
module: 11
arm: "+"
pooled_cpm: 16.7
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ERCC4

*ERCC excision repair 4, endonuclease catalytic subunit* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +20.5, q 0e+00, up in 44 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.160×, PANC-1 0.302×, HEC-1-A 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.124×, PANC-1 0.289×, A-427 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.203×, NCI-H460 0.319×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.279×, NCI-H460 0.310×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7]] (+0.81, fdr 7e-06), [[NME6]] (+0.80, fdr 7e-06), [[MRFAP1L1]] (+0.78, fdr 7e-06); moves opposite to [[CD81]] (-0.67, fdr 1e-05), [[TMED4]] (-0.67, fdr 7e-06), [[NTAN1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MICE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +20.5 | 0e+00 | 44/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.94×** | +19.0 | 0e+00 | 44/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.62×** | +17.1 | 0e+00 | 45/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.05×** | +15.4 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +10.1 | 4e-22 | 43/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +9.3 | 1e-18 | 33/43 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.49×** | +5.5 | 3e-06 | 29/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +5.5 | 3e-06 | 23/47 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 6e-06 | 23/47 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 24/47 (BT-474, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.43×** | +5.0 | 3e-05 | 21/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +4.9 | 4e-05 | 25/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 8e-05 | 20/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 23/48 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.3 | 6e-04 | 18/48 (Hs 766T, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.002 | 15/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 17/47 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.035 | 9/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.042 | 11/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.067 | 11/47 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.090 | 5/47 (HEC-1-A, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 0.160×, PANC-1 0.302×, HEC-1-A 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.124×, PANC-1 0.289×, A-427 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.203×, NCI-H460 0.319×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.279×, NCI-H460 0.310×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.642× | -3.2 | 0.46 | 8/46 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.796× | -3.1 | 0.46 | 15/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.8 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.203× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 20.1 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 18.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 17.1 | 4 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.69× (z +12.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -9.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 24.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 15.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +16.8) | — |
| [[A498 (line)]] | wt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.88× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 10.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.6) | — |
| [[A549 (line)]] | wt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 8.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0745× (z -11.6) |
| [[HS-578T (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.68× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 5.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.3) | — |
| [[RKO (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0874× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +8.7) | — |
| [[SW48 (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +8.7) | — |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[NME6]] | +0.80 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.78 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[RPP38]] | +0.77 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.77 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[METTL18]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[EID2]] | +0.75 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[RTL6]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.74 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[THAP5]] | +0.74 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[UTP3]] | +0.73 | +0.81 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD81]] | -0.67 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[TMED4]] | -0.67 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[NTAN1]] | -0.65 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[GM2A]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CD46]] | -0.64 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.63 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[GMCL1]] | -0.63 | -0.75 / -0.52 | both halves | 1e-05 |  |
| [[VAMP1]] | -0.63 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.63 | -0.71 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICE]] | B | MICE activity lowers ERCC4's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without MICE | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[EID2]] | C | EID2 activity raises ERCC4's level | lines that do not express EID2 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.2, 6.7); signed map (1.4, -21.2). **Vector** length 103, 25.5% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.4 | +19.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.1 | +15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +17.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +20.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.8 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 4, endonuclease catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:13,920,138-13,952,348 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAD1, FANCQ; previously XPF |
| Gene groups (HGNC) | FA complementation groups; Xeroderma pigmentosum complementation groups; ERCC excision repair associated |
| Hallmark sets | DNA_REPAIR |
| Reactome | 12 pathways, smallest: Fanconi Anemia Pathway; HDR through Single Strand Annealing (SSA); Dual Incision in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92889](https://www.uniprot.org/uniprotkb/Q92889) (DNA repair endonuclease XPF):

> Catalytic component of a structure-specific DNA repair endonuclease responsible for the 5-prime incision during DNA repair, and which is essential for nucleotide excision repair (NER) and interstrand cross-link (ICL) repair.

**Summary**, from NCBI Gene [2072](https://www.ncbi.nlm.nih.gov/gene/2072):

> The protein encoded by this gene forms a complex with ERCC1 and is involved in the 5' incision made during nucleotide excision repair. This complex is a structure specific DNA repair endonuclease that interacts with EME1. Defects in this gene are a cause of xeroderma pigmentosum complementation group F (XP-F), or xeroderma pigmentosum VI (XP6).[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:3436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3436) · Entrez [2072](https://www.ncbi.nlm.nih.gov/gene/2072) · UniProt [Q92889](https://www.uniprot.org/uniprotkb/Q92889) · Ensembl [ENSG00000175595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175595)

## Data

Gene col 10629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10629); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10629]; `tensor/DDL_lfc|DDL_z.npy` [10629]; `embed/gene_vectors.npy` [10629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10629 or target_col == 10629). Every well: [[ERCC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
