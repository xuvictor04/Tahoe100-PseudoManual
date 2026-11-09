---
symbol: "SFN"
type: "gene"
col: 10651
ensembl_id: "ENSG00000175793"
name: "stratifin"
location: "1p36.11"
module: 34
arm: "+"
pooled_cpm: 30.42
n_lines_expressing: 30
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 17
direction_downstream: 13
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SFN

*stratifin* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.62× (z +8.5, q 7e-15, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -7.3, q 1e-10, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDFI]] (+0.61, fdr 7e-06), [[GJB3]] (+0.59, fdr 1e-05), [[TMBIM1]] (+0.56, fdr 1e-05); moves opposite to [[HNMT]] (-0.55, fdr 1e-05), [[PCM1]] (-0.53, fdr 4e-05), [[HOXA3]] (-0.51, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[KRT16]] → it (grade B ⚠); 13 go from it, the strongest it → [[ORMDL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.62×** | +8.5 | 7e-15 | 25/28 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +8.5 | 7e-15 | 23/26 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.51×** | +8.1 | 7e-14 | 25/28 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +7.5 | 8e-12 | 17/28 (AsPC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.29×** | +6.5 | 7e-09 | 23/28 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.20×** | +6.4 | 1e-08 | 13/25 (NCI-H1573, AsPC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.95×** | +5.4 | 6e-06 | 12/25 (A549, Panc 03.27, …) | inconsistent across doses | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +5.3 | 9e-06 | 18/28 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.2 | 1e-05 | 18/28 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 17/28 (HT-29, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +4.5 | 3e-04 | 18/28 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.004 | 18/28 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.011 | 19/28 (HT-29, CFPAC-1, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.021 | 16/28 (HT-29, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.46×** | +3.3 | 0.033 | 15/28 (CFPAC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.037 | 13/28 (A498, A-427, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.047 | 13/28 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.064 | 12/28 (NCI-H2347, SW48, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.069 | 13/28 (NCI-H2030, NCI-H460, …) | rises with dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.069 | 11/28 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.36×** | +2.9 | 0.083 | 14/28 (HT-29, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -7.3 | 1e-10 | 19/28 (HCT15, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.633×** | -4.1 | 0.011 | 19/28 (LoVo, HCT15, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.337×** | -3.7 | 0.037 | 19/28 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.701× | -3.1 | 0.23 | 15/28 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.406× | -3.1 | 0.23 | 11/28 (HCT15, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 30.4 | 8 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 4.74× (z +11.5) | — |
| [[SW48 (line)]] | wt | 167 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -18.3) |
| [[LoVo (line)]] | wt | 109 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.8) |
| [[LS 180 (line)]] | wt | 56.0 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.28× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 14.1 | 4 (3 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 8.35× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 80.8 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 104 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 12.0× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 8.11× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 3 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 7.22× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.7) |
| [[A498 (line)]] | wt | 17.4 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +10.0) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.11× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.86× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.7) |
| [[KATO III (line)]] | alt | 25.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.51× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.3) |
| [[SW480 (line)]] | alt | 29.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.68× (z +9.6) | — |
| [[A-427 (line)]] | wt | 72.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.8) |
| [[A549 (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0900× (z -9.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 16.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.58× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 85.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -20.7) |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.4) |
| [[RKO (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -11.3) |
| [[A-172 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDFI]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GJB3]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 442 |
| [[TMBIM1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ADCY7]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[KRT16]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | STRING 421 |
| [[TNFAIP1]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[LHFPL2]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[S100A11]] | +0.54 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LINC01564]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[BICDL1]] | +0.52 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[FAM83H]] | +0.52 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNMT]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PCM1]] | -0.53 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[HOXA3]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DEPTOR]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[SORL1]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SELENOP]] | -0.49 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[ZNF608]] | -0.47 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[PPFIBP2]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FAAH2]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ACADSB]] | -0.46 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[HSD17B11]] | -0.46 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[LINC00992]] | -0.46 | -0.37 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT16]] | B | KRT16 activity raises SFN's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.07× lower at baseline in the lines without KRT16 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[LINC01564]] | B | LINC01564 activity strengthens SFN's drug response | lines that do not express LINC01564 (7) vs lines expressing it (21) | the lines without LINC01564 respond 0.50× as strongly (z diff +2.18); strongest at Auranofin 5 µM: 1.06x vs 2.25x (z diff +4.9) | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KRT6A]] | B | KRT6A activity raises SFN's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 5.72× lower at baseline in the lines without KRT6A | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[BICDL1]] | B | BICDL1 activity raises SFN's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 3.13× lower at baseline in the lines without BICDL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[MPP7]] | B | MPP7 activity raises SFN's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without MPP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[KLHL32]] | B | KLHL32 activity raises SFN's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without KLHL32 | 0.053 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises SFN's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.85× lower at baseline in the lines without ALS2CL | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[STON2]] | B | STON2 activity strengthens SFN's drug response | lines that do not express STON2 (8) vs lines expressing it (20) | the lines without STON2 respond 0.54× as strongly (z diff +1.98); strongest at Auranofin 5 µM: 0.96x vs 2.43x (z diff +5.7) | 0.069 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3; target measured in part of the lines; artifact flags |
| [[SRC]] | B | SRC activity raises SFN's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[S100A14]] | C | S100A14 activity raises SFN's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 5.19× lower at baseline in the lines without S100A14 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[MDFI]] | C | MDFI activity raises SFN's level | lines that do not express MDFI (25) vs lines expressing it (25) | 4.16× lower at baseline in the lines without MDFI | 0.007 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises SFN's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 5.31× lower at baseline in the lines without GJB3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ORMDL2]] | B | SFN activity raises ORMDL2's level | lines that do not express SFN (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without SFN | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[BICDL1]] | B | SFN activity raises BICDL1's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.01× lower at baseline in the lines without SFN | 0.018 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[NUMBL]] | B | SFN activity lowers NUMBL's level | lines that do not express SFN (20) vs lines expressing it (30) | 1.56× higher at baseline in the lines without SFN | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[DEPTOR]] | B | SFN activity raises DEPTOR's level | lines that do not express SFN (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without SFN | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[EPHA2-AS1]] | C | SFN activity raises EPHA2-AS1's level | lines that do not express SFN (20) vs lines expressing it (30) | 2.41× lower at baseline in the lines without SFN | 0.022 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[SORL1]] | C | SFN activity raises SORL1's level | lines that do not express SFN (20) vs lines expressing it (30) | 4.75× lower at baseline in the lines without SFN | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[FAM83H]] | C | SFN activity raises FAM83H's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without SFN | 0.039 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[LINC01564]] | C | SFN activity raises LINC01564's level | lines that do not express SFN (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without SFN | 0.039 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[CRYBG2]] | C | SFN activity raises CRYBG2's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.65× lower at baseline in the lines without SFN | 0.051 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[GJB3]] | C | SFN activity raises GJB3's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.77× lower at baseline in the lines without SFN | 0.058 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[FAAH2]] | C | SFN activity raises FAAH2's level | lines that do not express SFN (20) vs lines expressing it (30) | 4.08× lower at baseline in the lines without SFN | 0.066 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |
| [[S100A14]] | C | SFN activity raises S100A14's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.79× lower at baseline in the lines without SFN | 0.067 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.384). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.0, 50.9); signed map (-6.2, 42.3). **Vector** length 105, 37.2% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.1 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -7.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | stratifin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,863,149-26,864,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YWHAS |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Reactome | 36 pathways, smallest: Regulation of GBP-mediated host defense; Regulation of localization of FOXO transcription factors; SARS-CoV-2 targets host intracellular signalling and regulatory pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P31947](https://www.uniprot.org/uniprotkb/P31947) (14-3-3 protein sigma):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Promotes cytosolic retention of GBP1 GTPase by binding to phosphorylated GBP1, thereby inhibiting the innate immune response. Also acts as a TP53/p53-regulated inhibitor of G2/M progression. …

**Summary**, from NCBI Gene [2810](https://www.ncbi.nlm.nih.gov/gene/2810):

> This gene encodes a cell cycle checkpoint protein. The encoded protein binds to translation and initiation factors and functions as a regulator of mitotic translation. In response to DNA damage this protein plays a role in preventing DNA errors during mitosis. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:10773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10773) · Entrez [2810](https://www.ncbi.nlm.nih.gov/gene/2810) · UniProt [P31947](https://www.uniprot.org/uniprotkb/P31947) · Ensembl [ENSG00000175793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175793)

## Data

Gene col 10651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10651); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10651]; `tensor/DDL_lfc|DDL_z.npy` [10651]; `embed/gene_vectors.npy` [10651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10651 or target_col == 10651). Every well: [[SFN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
