---
symbol: "MYLK2"
type: "gene"
col: 2112
ensembl_id: "ENSG00000101306"
name: "myosin light chain kinase 2"
location: "20q11.21"
module: 47
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MYLK2

*myosin light chain kinase 2* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +6.8, q 5e-09, up in 18 of 29 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.85× (z +3.6, q 0.034, up in 5 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.396× (z -5.4, q 2e-05, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02236]] (+0.75, fdr 7e-06), [[MYH15]] (+0.74, fdr 7e-06), [[CHADL]] (+0.73, fdr 7e-06); moves opposite to [[RNPC3]] (-0.57, fdr 1e-05), [[ZDHHC24]] (-0.56, fdr 1e-05), [[TRAF6]] (-0.55, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KIF17]] → it (grade C ⚠); 6 go from it, the strongest it → [[KIF2C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.28×** | +6.8 | 5e-09 | 18/29 (HS-578T, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.94×** | +6.1 | 4e-07 | 2/3 (A498, J82) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.37×** | +4.7 | 5e-04 | 1/5 (A498) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +4.0 | 0.008 | 9/45 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.034 | 5/44 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.79×** | +3.4 | 0.061 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.67× | +3.0 | 0.21 | 7/41 (HOP62, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.396×** | -5.4 | 2e-05 | 22/39 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.520×** | -5.4 | 2e-05 | 16/42 (LoVo, LOX-IMVI, …) | rises with dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.415×** | -5.1 | 6e-05 | 22/36 (A498, HS-578T, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.487×** | -4.0 | 0.008 | 16/36 (HOP62, SW 900, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.013 | 18/40 (SW 900, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.523×** | -3.8 | 0.013 | 20/43 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.506×** | -3.7 | 0.013 | 13/35 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.526×** | -3.7 | 0.013 | 13/43 (A-427, HT-29, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.540×** | -3.6 | 0.021 | 16/38 (A549, A-427, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.534×** | -3.4 | 0.041 | 17/44 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -3.2 | 0.062 | 15/41 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.681×** | -3.2 | 0.076 | 9/44 (LoVo, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 7.41 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0245× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 4.60 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0379× (z -10.0) |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0578× (z -8.6) |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.758 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.693 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02236]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MYH15]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CHADL]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.70 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PILRA]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SPATA32]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MTFR2]] | +0.67 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[PYGM]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.66 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPC3]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZDHHC24]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TRAF6]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.54 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MORN4]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TP53TG1]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[BBS7]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF17]] | C | KIF17 activity raises MYLK2's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without KIF17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |
| [[CSPG5]] | C | CSPG5 activity raises MYLK2's level | lines that do not express CSPG5 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without CSPG5 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF2C]] | C | MYLK2 activity raises KIF2C's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without MYLK2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[GTSE1]] | C | MYLK2 activity raises GTSE1's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.17× lower at baseline in the lines without MYLK2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent; its own permutation p |
| [[ASPM]] | C | MYLK2 activity raises ASPM's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.29× lower at baseline in the lines without MYLK2 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[PRC1]] | C | MYLK2 activity raises PRC1's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without MYLK2 | 0.075 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[KIF23]] | C | MYLK2 activity raises KIF23's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.91× lower at baseline in the lines without MYLK2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[NCAPG]] | C | MYLK2 activity raises NCAPG's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.89× lower at baseline in the lines without MYLK2 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, -14.5); signed map (17.9, 12.5). **Vector** length 80.4, 16.1% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.9 | +6.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.0 | +6.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +4.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.7 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.7 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,819,308-31,834,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | skMLCK, KMLC, MLCK2 |
| Gene groups (HGNC) | Myosin light chain kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1R3](https://www.uniprot.org/uniprotkb/Q9H1R3) (Myosin light chain kinase 2, skeletal/cardiac muscle):

> Ca(2+)/calmodulin-dependent kinase that phosphorylates the regulatory light chain (RLC) of sarcomeric myosin in skeletal and cardiac muscle. Phosphorylation of RLC promotes displacement of myosin cross-bridges from the thick filament backbone toward actin-containing thin filaments, increasing the probability of cross-bridge entry into force-generating states and thereby potentiating contractile force at submaximal Ca(2+) concentrations.

**Summary**, from NCBI Gene [85366](https://www.ncbi.nlm.nih.gov/gene/85366):

> This gene encodes a myosin light chain kinase, a calcium/calmodulin dependent enzyme, that is exclusively expressed in adult skeletal muscle. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16243) · Entrez [85366](https://www.ncbi.nlm.nih.gov/gene/85366) · UniProt [Q9H1R3](https://www.uniprot.org/uniprotkb/Q9H1R3) · Ensembl [ENSG00000101306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101306)

## Data

Gene col 2112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2112); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2112]; `tensor/DDL_lfc|DDL_z.npy` [2112]; `embed/gene_vectors.npy` [2112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2112 or target_col == 2112). Every well: [[MYLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
