---
symbol: "ECM1"
type: "gene"
col: 6725
ensembl_id: "ENSG00000143369"
name: "extracellular matrix protein 1"
location: "1q21.2"
module: 50
arm: "+"
pooled_cpm: 14.33
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ECM1

*extracellular matrix protein 1* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +12.9, q 2e-35, up in 20 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +12.0, q 4e-31, up in 20 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.322× (z -12.0, q 3e-30, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPARC]] (+0.71, fdr 7e-06), [[MMP2]] (+0.65, fdr 7e-06), [[RTL8C]] (+0.64, fdr 7e-06); moves opposite to [[MRPL58]] (-0.59, fdr 1e-05), [[TRMT10B]] (-0.58, fdr 1e-05), [[RSL1D1]] (-0.56, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[HTRA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +12.9 | 2e-35 | 20/21 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +12.6 | 4e-34 | 16/17 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +12.0 | 4e-31 | 20/27 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +10.6 | 3e-24 | 15/20 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.9 | 8e-05 | 11/23 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.9 | 8e-05 | 13/24 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.4 | 9e-04 | 13/27 (LOX-IMVI, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.2 | 0.002 | 6/27 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.004 | 14/27 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.011 | 10/27 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.081 | 3/25 (RPMI-7951, A498, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.1 | 0.095 | 6/20 (HOP62, A-172, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.66× | +3.0 | 0.11 | 4/26 (A-172, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6725.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -12.0 | 3e-30 | 25/27 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -11.8 | 6e-30 | 26/27 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -8.5 | 4e-15 | 23/27 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -6.7 | 3e-09 | 21/27 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.644×** | -4.8 | 2e-04 | 14/27 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.655×** | -4.3 | 0.002 | 7/27 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.706×** | -3.7 | 0.019 | 18/26 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.047 | 8/27 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.751×** | -3.1 | 0.097 | 8/26 (A498, SW 1271, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.752×** | -3.1 | 0.097 | 7/26 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 146 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -24.2) |
| [[hTERT-HPNE (line)]] | wt | 59.9 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.4) |
| [[C32 (line)]] | wt | 48.9 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.6) |
| [[J82 (line)]] | alt | 34.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -30.3) |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.5) |
| [[H4 (line)]] | wt | 21.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -14.8) |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -18.8) |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.4) |
| [[HOP62 (line)]] | alt | 10.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +9.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.142× (z -10.6) |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.9) |
| [[KATO III (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.5) |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.9) |
| [[RKO (line)]] | wt | 18.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -11.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 7.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0788× (z -9.5) |
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -8.6) |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -9.0) |
| [[SW 900 (line)]] | alt | 6.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0481× (z -10.1) |
| [[A-427 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPARC]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MMP2]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RTL8C]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMED4]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ITM2C]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[CD81]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[BSG]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LRPAP1]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[GM2A]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RPN2]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NID2]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[P3H3]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RSL1D1]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[C15orf40]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZNF480]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PEX1]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ZNF23]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NOL8]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[THAP5]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ECM1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PTN]] | C | PTN activity raises ECM1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without PTN | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[MMP14]] | C | MMP14 activity raises ECM1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without MMP14 | 0.036 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTRA1]] | B | ECM1 activity raises HTRA1's level | lines that do not express ECM1 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without ECM1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SEMA5A, NLRP1, MMP14; maybe low, not absent |
| [[PTN]] | C | ECM1 activity raises PTN's level | lines that do not express ECM1 (21) vs lines expressing it (29) | 2.61× lower at baseline in the lines without ECM1 | 0.093 | ⚠ within organs, on part of the lines; also absent: SEMA5A, NLRP1, MMP14; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.1, -20.9); signed map (-53.5, -12.0). **Vector** length 64.0, 15.9% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +12.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -11.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | extracellular matrix protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,508,062-150,513,789 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16610](https://www.uniprot.org/uniprotkb/Q16610) (Extracellular matrix protein 1):

> Involved in endochondral bone formation as negative regulator of bone mineralization. Stimulates the proliferation of endothelial cells and promotes angiogenesis. Inhibits MMP9 proteolytic activity.

**Summary**, from NCBI Gene [1893](https://www.ncbi.nlm.nih.gov/gene/1893):

> This gene encodes a soluble protein that is involved in endochondral bone formation, angiogenesis, and tumor biology. It also interacts with a variety of extracellular and structural proteins, contributing to the maintenance of skin integrity and homeostasis. Mutations in this gene are associated with lipoid proteinosis disorder (also known as hyalinosis cutis et mucosae or Urbach-Wiethe disease) that is characterized by generalized thickening of skin, mucosae and certain viscera. Alternatively …

**Accessions** — [HGNC:3153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3153) · Entrez [1893](https://www.ncbi.nlm.nih.gov/gene/1893) · UniProt [Q16610](https://www.uniprot.org/uniprotkb/Q16610) · Ensembl [ENSG00000143369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143369)

## Data

Gene col 6725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6725); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6725]; `tensor/DDL_lfc|DDL_z.npy` [6725]; `embed/gene_vectors.npy` [6725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6725 or target_col == 6725). Every well: [[ECM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
