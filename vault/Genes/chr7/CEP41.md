---
symbol: "CEP41"
type: "gene"
col: 2764
ensembl_id: "ENSG00000106477"
name: "centrosomal protein 41"
location: "7q32.2"
module: 16
arm: "+"
pooled_cpm: 7.49
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CEP41

*centrosomal protein 41* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.45× (z +17.4, q 0e+00, up in 13 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.47× (z +4.1, q 0.006, up in 10 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.411× (z -9.5, q 1e-18, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCLRE1A]] (+0.74, fdr 7e-06), [[DHX9]] (+0.72, fdr 7e-06), [[RUVBL1]] (+0.70, fdr 7e-06); moves opposite to [[APTR]] (-0.73, fdr 1e-05), [[MIR4458HG]] (-0.70, fdr 7e-06), [[RPLP1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[EID1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.45×** | +17.4 | 0e+00 | 13/13 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.45×** | +15.9 | 0e+00 | 30/31 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +12.4 | 3e-33 | 17/19 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.006 | 10/44 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.9 | 0.010 | 16/38 (SNU-423, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.012 | 14/41 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.012 | 9/44 (A549, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.013 | 8/44 (SW480, HS-578T, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.023 | 9/44 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.034 | 5/44 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.23× | +3.1 | 0.11 | 7/44 (NCI-H23, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.411×** | -9.5 | 1e-18 | 31/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -8.9 | 1e-16 | 29/43 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -8.8 | 2e-16 | 28/40 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.503×** | -7.4 | 3e-11 | 26/42 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.644×** | -4.7 | 3e-04 | 16/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.697×** | -3.9 | 0.011 | 15/44 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -3.7 | 0.021 | 20/41 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -3.3 | 0.058 | 12/43 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -3.3 | 0.067 | 17/43 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.808×** | -3.2 | 0.067 | 12/44 (SHP-77, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.1 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -11.0) |
| [[LoVo (line)]] | wt | 5.63 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0837× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.157× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 8.97 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[A498 (line)]] | wt | 7.33 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.5× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 5.29 | 0 | 2 (1 ⚠) | — | [[Methotrexate (drug)]] 0.05 µM 0.0704× (z -10.1) |
| [[BT-474 (line)]] | alt | 9.95 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0733× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.100× (z -9.2) |
| [[PANC-1 (line)]] | alt | 5.27 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.24× (z +10.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0371× (z -16.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.78× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.159× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 4.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0657× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 5 µM 0.0334× (z -9.2) |
| [[A-172 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.704 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[DHX9]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SLX4IP]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DARS2]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TASOR]] | +0.68 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ALG10]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RIF1]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[FKTN]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PPIL1]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | -0.73 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[MIR4458HG]] | -0.70 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[RPLP1]] | -0.69 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[RPS19]] | -0.69 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.68 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[UBA52]] | -0.68 | -0.54 / -0.70 | both halves | 1e-05 | pathway: G2/M Transition |
| [[RPL37A]] ⚠ | -0.68 | -0.54 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | -0.68 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[SERF2]] | -0.67 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[RPS27]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[RPLP2]] | -0.66 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[RPS29]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers CEP41's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.95× higher at baseline in the lines without HLA-F-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[ZNF512B]] | B | ZNF512B activity raises CEP41's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without ZNF512B | 0.098 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |
| [[EID1]] | C | EID1 activity raises CEP41's level | lines that do not express EID1 (3) vs lines expressing it (47) | 3.57× lower at baseline in the lines without EID1 | 0.017 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID1]] | C | CEP41 activity raises EID1's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 3.03× lower at baseline in the lines without CEP41 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |
| [[CCDC32]] | C | CEP41 activity raises CCDC32's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without CEP41 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35 |
| [[IQCH]] | C | CEP41 activity raises IQCH's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without CEP41 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |
| [[RANBP6]] | C | CEP41 activity raises RANBP6's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.15× lower at baseline in the lines without CEP41 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |
| [[ALG10B]] | C | CEP41 activity raises ALG10B's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without CEP41 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.4, -36.8); signed map (3.9, -35.8). **Vector** length 64.0, 10.7% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.4 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Daidzin (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,393,771-130,442,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762H1311, FLJ22445, JBTS15; previously TSGA14 |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYV8](https://www.uniprot.org/uniprotkb/Q9BYV8) (Centrosomal protein of 41 kDa):

> Required during ciliogenesis for tubulin glutamylation in cilium. Probably acts by participating in the transport of TTLL6, a tubulin polyglutamylase, between the basal body and the cilium.

**Summary**, from NCBI Gene [95681](https://www.ncbi.nlm.nih.gov/gene/95681):

> This gene encodes a centrosomal and microtubule-binding protein which is predicted to have two coiled-coil domains and a rhodanese domain. In human retinal pigment epithelial cells the protein localized to centrioles and cilia. Mutations in this gene have been associated with Joubert Syndrome 15; an autosomal recessive ciliopathy and neurological disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:12370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12370) · Entrez [95681](https://www.ncbi.nlm.nih.gov/gene/95681) · UniProt [Q9BYV8](https://www.uniprot.org/uniprotkb/Q9BYV8) · Ensembl [ENSG00000106477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106477)

## Data

Gene col 2764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2764); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2764]; `tensor/DDL_lfc|DDL_z.npy` [2764]; `embed/gene_vectors.npy` [2764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2764 or target_col == 2764). Every well: [[CEP41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
