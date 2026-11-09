---
symbol: "LOXL1"
type: "gene"
col: 4943
ensembl_id: "ENSG00000129038"
name: "lysyl oxidase like 1"
location: "15q24.1"
module: 13
arm: "+"
pooled_cpm: 4.63
n_lines_expressing: 32
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 11
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LOXL1

*lysyl oxidase like 1* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.46× (z +11.0, q 2e-25, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +7.9, q 1e-12, up in 11 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.461× (z -9.9, q 3e-20, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL1-AS1]] (+0.60, fdr 1e-05, ⚠ same locus), [[SCUBE3]] (+0.59, fdr 1e-05), [[B4GALNT1]] (+0.51, fdr 1e-04), [[CNPY4]] (+0.50, fdr 2e-05); moves opposite to [[FNIP1]] (-0.53, fdr 2e-05), [[RABGAP1]] (-0.50, fdr 3e-05), [[BABAM2]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PDGFRB]] → it (grade B ⚠); 11 go from it, the strongest it → [[CERCAM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +11.0 | 2e-25 | 3/8 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.9 | 1e-12 | 11/23 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +7.5 | 1e-11 | 4/17 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +7.3 | 3e-11 | 12/28 (SW48, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.4 | 2e-08 | 3/9 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.0 | 2e-07 | 9/26 (RPMI-7951, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.4 | 5e-06 | 5/14 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +4.4 | 8e-04 | 10/21 (NCI-H460, SW48, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.063 | 2/26 (LOX-IMVI, J82) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.077 | 4/8 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.10 | 3/26 (HOP62, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.10 | 6/28 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.10 | 1/25 (NCI-H23) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.461×** | -9.9 | 3e-20 | 16/26 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.477×** | -9.4 | 1e-18 | 15/26 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.508×** | -8.6 | 1e-15 | 15/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -5.9 | 7e-07 | 14/23 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.661×** | -5.3 | 2e-05 | 9/27 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -4.9 | 8e-05 | 14/21 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.002 | 9/27 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -3.8 | 0.009 | 6/28 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.747×** | -3.7 | 0.012 | 9/29 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.760×** | -3.5 | 0.026 | 11/28 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -3.4 | 0.030 | 6/22 (SW48, NCI-H23, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.077 | 4/30 (H4, HOP62, …) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 0.5 µM |  | 0.789× | -3.0 | 0.11 | 8/25 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.2) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 2.12 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0576× (z -9.4) |
| [[H4 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.177× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[LOX-IMVI (line)]] | wt | 8.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 6.56 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.115× (z -9.7) |
| [[PANC-1 (line)]] | alt | 6.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.8) |
| [[SNU-423 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL1-AS1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SCUBE3]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[B4GALNT1]] | +0.51 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[CNPY4]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CHST14]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[FIBCD1]] | +0.50 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[SSC5D]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[ACLY]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CAPN2]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[CERCAM]] | +0.47 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[KIAA1549L]] | +0.47 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[UBP1]] | +0.47 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[COL6A1]] | +0.46 | +0.43 / +0.43 | both halves | 3e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 488 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNIP1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RABGAP1]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BABAM2]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ALPK1]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[IRF2BP2]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[LINC01473]] | -0.43 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[CLN3]] | -0.42 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[NEU1]] | -0.41 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[MAP2K7]] | -0.41 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[TMEM161B-DT]] | -0.41 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[DHRSX]] | -0.40 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[GOLGA4]] | -0.40 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRB]] | B | PDGFRB activity raises LOXL1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.34× lower at baseline in the lines without PDGFRB | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[APCDD1L]] | B | APCDD1L activity raises LOXL1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without APCDD1L | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[SARDH]] | B | SARDH activity raises LOXL1's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.40× lower at baseline in the lines without SARDH | 0.045 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[PLEKHG4B]] | B | PLEKHG4B activity raises LOXL1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without PLEKHG4B | 0.050 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[BVES]] | B | BVES activity raises LOXL1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without BVES | 0.060 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[ITGA4]] | B | ITGA4 activity raises LOXL1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without ITGA4 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[DOCK2]] | B | DOCK2 activity raises LOXL1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without DOCK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[TSHZ3-AS1]] | B | TSHZ3-AS1 activity raises LOXL1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 2.79× lower at baseline in the lines without TSHZ3-AS1 | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[COL5A1]] | B | COL5A1 activity raises LOXL1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without COL5A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[BVES-AS1]] | B | BVES-AS1 activity raises LOXL1's level | lines that do not express BVES-AS1 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without BVES-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: BVES, MPDZ, MAP9; maybe low, not absent |
| [[LOXL1-AS1]] | C | LOXL1-AS1 activity raises LOXL1's level | lines that do not express LOXL1-AS1 (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without LOXL1-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BEX4, ENSG00000255330, LOXL1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | LOXL1 activity raises CERCAM's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.93× lower at baseline in the lines without LOXL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[BVES]] | B | LOXL1 activity raises BVES's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without LOXL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[PLEKHG4B]] | B | LOXL1 activity raises PLEKHG4B's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without LOXL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[CHST14]] | B | LOXL1 activity raises CHST14's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without LOXL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[BVES-AS1]] | B | LOXL1 activity raises BVES-AS1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without LOXL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[ANXA6]] | B | LOXL1 activity raises ANXA6's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without LOXL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[COL6A1]] | B | LOXL1 activity raises COL6A1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.80× lower at baseline in the lines without LOXL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[VPS41]] | B | LOXL1 activity raises VPS41's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.09× lower at baseline in the lines without LOXL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[PSMD2]] | B | LOXL1 activity raises PSMD2's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without LOXL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[SSC5D]] | B | LOXL1 activity raises SSC5D's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without LOXL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[LOXL1-AS1]] | C | LOXL1 activity raises LOXL1-AS1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without LOXL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.0, 18.0); signed map (23.1, 44.2). **Vector** length 48.2, 8.17% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +1.9 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | lysyl oxidase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:73,925,989-73,952,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOXL, LOL |
| Gene groups (HGNC) | Lysyl oxidase family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Elastic fibre formation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08397](https://www.uniprot.org/uniprotkb/Q08397) (Lysyl oxidase homolog 1):

> Catalyzes the oxidative deamination of lysine and hydroxylysine residues in collagen and elastin, resulting in the formation of covalent cross-linkages, and the stabilization of collagen and elastin fibers (By similarity). Essential for the elastic fiber homeostasis and for their maintenance at adult age (By similarity).

**Summary**, from NCBI Gene [4016](https://www.ncbi.nlm.nih.gov/gene/4016):

> This gene encodes a member of the lysyl oxidase family of proteins. The prototypic member of the family is essential to the biogenesis of connective tissue, encoding an extracellular copper-dependent amine oxidase that catalyzes the first step in the formation of crosslinks in collagen and elastin. The encoded preproprotein is proteolytically processed to generate the mature enzyme. A highly conserved amino acid sequence at the C-terminus end appears to be sufficient for amine oxidase activity, …

**Accessions** — [HGNC:6665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6665) · Entrez [4016](https://www.ncbi.nlm.nih.gov/gene/4016) · UniProt [Q08397](https://www.uniprot.org/uniprotkb/Q08397) · Ensembl [ENSG00000129038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129038)

## Data

Gene col 4943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4943); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4943]; `tensor/DDL_lfc|DDL_z.npy` [4943]; `embed/gene_vectors.npy` [4943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4943 or target_col == 4943). Every well: [[LOXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
