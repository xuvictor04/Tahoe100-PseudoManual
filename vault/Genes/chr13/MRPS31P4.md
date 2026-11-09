---
symbol: "MRPS31P4"
type: "gene"
col: 14679
ensembl_id: "ENSG00000250299"
name: "mitochondrial ribosomal protein S31 pseudogene 4"
location: "13q14.3"
module: 17
arm: "+"
pooled_cpm: 12.35
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MRPS31P4

*mitochondrial ribosomal protein S31 pseudogene 4* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.14× (z +12.3, q 4e-32, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -12.9, q 2e-35, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGT1P4-STRA6LP]] (+0.80, fdr 7e-06), [[MRPS31P5-1]] (+0.78, fdr 7e-06), [[STRA6LP]] (+0.78, fdr 7e-06); moves opposite to [[MCF2]] (-0.67, fdr 1e-05), [[PRDM10]] (-0.66, fdr 1e-05), [[RNF217-AS1]] (-0.65, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF569]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +12.3 | 4e-32 | 41/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +11.5 | 3e-28 | 43/47 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +11.4 | 6e-28 | 41/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.1 | 1e-07 | 19/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +5.7 | 2e-06 | 18/48 (HT-29, HOP62, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.8 | 1e-04 | 15/48 (HT-29, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 1e-04 | 15/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.0 | 0.004 | 13/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +3.9 | 0.006 | 10/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 7/47 (KATO III, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.6 | 0.014 | 14/40 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.021 | 9/48 (HT-29, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.038 | 11/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.084 | 9/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.097 | 11/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.097 | 5/47 (Panc 03.27, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -12.9 | 2e-35 | 36/45 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.553×** | -9.5 | 4e-19 | 29/47 (NCI-H23, COLO 205, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -9.5 | 4e-19 | 31/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -8.5 | 2e-15 | 28/47 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -8.1 | 7e-14 | 29/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -6.4 | 1e-08 | 24/45 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.703×** | -5.7 | 1e-06 | 23/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.714×** | -5.4 | 5e-06 | 21/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.799×** | -5.1 | 2e-05 | 19/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.1 | 0.002 | 14/48 (SW1417, A498, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.775×** | -4.1 | 0.002 | 7/47 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.794×** | -3.7 | 0.010 | 9/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.783×** | -3.7 | 0.010 | 9/46 (HEC-1-A, NCI-H1792, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.650×** | -3.6 | 0.012 | 11/33 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.794×** | -3.6 | 0.014 | 17/41 (SNU-423, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.026 | 16/48 (KATO III, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.033 | 11/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.033 | 14/47 (KATO III, SNU-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.051 | 12/42 (A549, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.2) |
| [[C32 (line)]] | wt | 8.90 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0873× (z -9.4) |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.1) |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.1) |
| [[A498 (line)]] | wt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.2) |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0744× (z -11.0) |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.6) |
| [[KATO III (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 8.30 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0772× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0984× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP]] | +0.80 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[MRPS31P5-1]] | +0.78 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[STRA6LP]] | +0.78 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[BBS5]] | +0.75 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.75 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.75 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[COG2]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[THOC1]] | +0.74 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.72 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCF2]] | -0.67 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.66 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RNF217-AS1]] | -0.65 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[SAXO1]] | -0.65 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LINC00393]] | -0.64 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CCNT2-AS1]] | -0.64 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SIAH2-AS1]] | -0.64 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | -0.64 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.64 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[C2orf88]] | -0.63 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[FBXL19-AS1]] | -0.63 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[BANP]] | -0.63 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF569]] | B | ZNF569 activity raises MRPS31P4's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.07× lower at baseline in the lines without ZNF569 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[MBP]] | B | MBP activity lowers MRPS31P4's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without MBP | 0.060 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[ZNF420]] | B | ZNF420 activity raises MRPS31P4's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without ZNF420 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.902). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.9, -2.4); signed map (-22.3, -14.8). **Vector** length 83.0, 15.5% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of the 9+0 primary cilium* (reactome, mean cos +0.51 to 11); *Intraflagellar transport* (reactome, mean cos +0.56 to 6); *Cilium Assembly* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.8 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +12.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.3 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S31 pseudogene 4 |
| Locus type | pseudogene |
| Location | 13q14.3 — chr13:52,617,558-52,637,446 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42649) · Entrez [100885866](https://www.ncbi.nlm.nih.gov/gene/100885866) · Ensembl [ENSG00000250299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250299)

## Data

Gene col 14679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14679); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14679]; `tensor/DDL_lfc|DDL_z.npy` [14679]; `embed/gene_vectors.npy` [14679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14679 or target_col == 14679). Every well: [[MRPS31P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS31P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
