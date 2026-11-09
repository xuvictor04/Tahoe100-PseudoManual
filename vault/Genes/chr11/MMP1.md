---
symbol: "MMP1"
type: "gene"
col: 12249
ensembl_id: "ENSG00000196611"
name: "matrix metallopeptidase 1"
location: "11q22.2"
module: 81
arm: "+"
pooled_cpm: 34.7
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# MMP1

*matrix metallopeptidase 1* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.48× (z +9.8, q 5e-20, up in 10 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.21× (z +7.3, q 1e-10, up in 14 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -11.9, q 1e-29, down in 21 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2]] (+0.74, fdr 7e-06), [[ABTB3]] (+0.71, fdr 7e-06), [[STC1]] (+0.71, fdr 7e-06); moves opposite to [[NNMT]] (-0.59, fdr 1e-05), [[ZNF608]] (-0.57, fdr 1e-05), [[CEBPD]] (-0.57, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 16 go from it, the strongest it → [[ACVR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.48×** | +9.8 | 5e-20 | 10/21 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +7.3 | 1e-10 | 14/22 (C32, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +6.6 | 7e-09 | 8/16 (C32, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +5.8 | 7e-07 | 7/21 (KATO III, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +5.2 | 2e-05 | 3/16 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +4.5 | 7e-04 | 8/22 (KATO III, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.95×** | +4.2 | 0.002 | 11/22 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +4.1 | 0.003 | 7/21 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +3.7 | 0.012 | 5/21 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.013 | 7/21 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.049 | 4/24 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.061 | 6/22 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.61×** | +3.1 | 0.079 | 4/21 (AN3 CA, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.60×** | +3.1 | 0.081 | 6/23 (NCI-H460, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 1 with an alert ⚠; shown: the 15 strongest. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -11.9 | 1e-29 | 21/21 (KATO III, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -7.4 | 5e-11 | 20/21 (hTERT-HPNE, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.392×** | -6.1 | 2e-07 | 17/21 (hTERT-HPNE, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.438×** | -5.2 | 3e-05 | 15/21 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.568×** | -5.2 | 3e-05 | 13/22 (AsPC-1, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.444×** | -4.9 | 8e-05 | 13/21 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.475×** | -4.9 | 8e-05 | 13/21 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.597×** | -4.7 | 2e-04 | 12/22 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.489×** | -4.7 | 2e-04 | 13/21 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.543×** | -4.7 | 2e-04 | 13/22 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.436×** | -4.3 | 7e-04 | 15/24 (A549, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.493×** | -4.2 | 0.001 | 16/23 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.530×** | -4.2 | 0.001 | 15/22 (SNU-423, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.524×** | -4.1 | 0.002 | 10/21 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.544×** | -4.0 | 0.002 | 12/21 (A549, AsPC-1, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 30.1 | 7 (2 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 20.0× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.0116× (z -22.9) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -13.6) |
| [[A549 (line)]] | wt | 19.5 | 0 | 6 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0204× (z -14.4) |
| [[BT-474 (line)]] | alt | 10.6 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 55.9× (z +10.5) | — |
| [[C32 (line)]] | wt | 10.1 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 34.5× (z +13.6) | — |
| [[NCI-H596 (line)]] | alt | 98.1 | 2 | 1 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 32.3× (z +22.0) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.268× (z -8.7) |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 1,881 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0771× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0978× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -9.5) |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -10.0) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 813 |
| [[ABTB3]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[STC1]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TIMP1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 999 |
| [[AADAC]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CALB2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[S100A16]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNMT]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ZNF608]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CEBPD]] | -0.57 | -0.68 / -0.46 | both halves | 3e-05 | pathway: Interleukin-4 and Interleukin-13 signaling |
| [[STOM]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[EDN2]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TNS3]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers MMP1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[CPA6]] | B | CPA6 activity raises MMP1's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without CPA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises MMP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SPOCK1]] | C | SPOCK1 activity raises MMP1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without SPOCK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACVR1]] | B | MMP1 activity raises ACVR1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without MMP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[TDRKH]] | B | MMP1 activity lowers TDRKH's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.43× higher at baseline in the lines without MMP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[TMEM158]] | B | MMP1 activity raises TMEM158's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 4.16× lower at baseline in the lines without MMP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[ARMC8]] | B | MMP1 activity lowers ARMC8's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.22× higher at baseline in the lines without MMP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[PPFIBP1]] | B | MMP1 activity raises PPFIBP1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without MMP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[SH3BGRL3]] | B | MMP1 activity raises SH3BGRL3's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without MMP1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[CD44]] | B | MMP1 activity raises CD44's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without MMP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| cells under [[Dexamethasone (drug)]] 0.5 µM | B | MMP1 activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express MMP1 (26) vs lines expressing it (22) | the lines without MMP1: 1.17× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[MMP14]] | B | MMP1 activity raises MMP14's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without MMP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[FXYD5]] | B | MMP1 activity raises FXYD5's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without MMP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| cells under [[Vemurafenib (drug)]] 5 µM | B | MMP1 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express MMP1 (26) vs lines expressing it (22) | the lines without MMP1: 0.86× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[MDGA1]] | B | MMP1 activity raises MDGA1's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without MMP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.7, 3.3); signed map (3.1, 47.9). **Vector** length 75.0, 21.0% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.5 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -11.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -7.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.6 | -6.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,789,401-102,798,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CLG |
| Gene groups (HGNC) | Receptor ligands; M10 matrix metallopeptidases |
| Hallmark sets | COAGULATION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: Activation of Matrix Metalloproteinases; Basigin interactions; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P03956](https://www.uniprot.org/uniprotkb/P03956) (Interstitial collagenase):

> Cleaves collagens of types I, II, and III at one site in the helical domain. Also cleaves collagens of types VII and X. In case of HIV infection, interacts and cleaves the secreted viral Tat protein, leading to a decrease in neuronal Tat's mediated neurotoxicity.

**Summary**, from NCBI Gene [4312](https://www.ncbi.nlm.nih.gov/gene/4312):

> This gene encodes a member of the peptidase M10 family of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. The encoded preproprotein is proteolytically processed to generate the mature protease. This secreted protease breaks down the interstitial collagens, …

**Accessions** — [HGNC:7155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7155) · Entrez [4312](https://www.ncbi.nlm.nih.gov/gene/4312) · UniProt [P03956](https://www.uniprot.org/uniprotkb/P03956) · Ensembl [ENSG00000196611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196611)

## Data

Gene col 12249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12249); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12249]; `tensor/DDL_lfc|DDL_z.npy` [12249]; `embed/gene_vectors.npy` [12249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12249 or target_col == 12249). Every well: [[MMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
