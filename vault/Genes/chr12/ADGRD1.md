---
symbol: "ADGRD1"
type: "gene"
col: 3235
ensembl_id: "ENSG00000111452"
name: "adhesion G protein-coupled receptor D1"
location: "12q24.33"
module: 19
arm: "+"
pooled_cpm: 30.59
n_lines_expressing: 13
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 17
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ADGRD1

*adhesion G protein-coupled receptor D1* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +10.0, q 6e-21, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.02× (z +4.0, q 0.009, up in 0 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.510× (z -5.4, q 3e-05, down in 5 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03000]] (+0.89, fdr 7e-06), [[LINC01035]] (+0.89, fdr 7e-06), [[CHL1]] (+0.84, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 11 go from it, the strongest it → [[KCNMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.53×** | +10.0 | 6e-21 | 2/7 (HEC-1-A, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +5.7 | 3e-06 | 2/5 (NCI-H2347, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +4.9 | 2e-04 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.02×** | +4.0 | 0.009 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.027 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.078 | 0/10 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.087 | 1/8 (SW 900) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.087 | 3/11 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.087 | 0/9 | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.46× | +3.0 | 0.14 | 3/9 (NCI-H2347, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -5.4 | 3e-05 | 5/10 (SHP-77, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.514×** | -5.3 | 3e-05 | 4/10 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -4.5 | 0.001 | 4/10 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.582×** | -4.3 | 0.002 | 5/10 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.578×** | -4.2 | 0.003 | 6/9 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -3.6 | 0.033 | 4/8 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -3.5 | 0.039 | 4/9 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.652×** | -3.4 | 0.042 | 3/10 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.668×** | -3.2 | 0.076 | 4/11 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -3.2 | 0.080 | 2/10 (NCI-H460, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 519 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -18.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 57.9 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03000]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.89 | +0.82 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.84 | +0.73 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.83 | +0.72 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.83 | +0.75 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A5]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[LIN7A]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ADGRD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GSG1L2]] | C | GSG1L2 activity raises ADGRD1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 6.93× lower at baseline in the lines without GSG1L2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises ADGRD1's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.47× lower at baseline in the lines without LINC01508 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises ADGRD1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.21× lower at baseline in the lines without MARCOL, SPINK13 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[SLC15A5]] | C | SLC15A5 activity raises ADGRD1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.69× lower at baseline in the lines without SLC15A5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises ADGRD1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 5.65× lower at baseline in the lines without LINC03000 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises ADGRD1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.67× lower at baseline in the lines without DPP10 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises ADGRD1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.52× lower at baseline in the lines without SCARA5 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[LINC01257]] | C | LINC01257 activity raises ADGRD1's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without LINC01257 | 0.052 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises ADGRD1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.31× lower at baseline in the lines without CHL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises ADGRD1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 15.89× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[CTNND2]] | C | CTNND2 activity raises ADGRD1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.61× lower at baseline in the lines without CTNND2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | ADGRD1 activity raises KCNMB2's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without ADGRD1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| cells under [[Docetaxel (drug)]] 5 µM | B | ADGRD1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express ADGRD1 (37) vs lines expressing it (11) | the lines without ADGRD1: 0.86× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | ADGRD1 activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express ADGRD1 (37) vs lines expressing it (11) | the lines without ADGRD1: 0.87× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| [[CLDN10-AS1]] | C | ADGRD1 activity raises CLDN10-AS1's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 3.65× lower at baseline in the lines without ADGRD1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[SLC7A2]] | C | ADGRD1 activity raises SLC7A2's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 4.36× lower at baseline in the lines without ADGRD1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[SOX6]] | C | ADGRD1 activity raises SOX6's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 3.82× lower at baseline in the lines without ADGRD1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[DPP10]] | C | ADGRD1 activity raises DPP10's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.67× lower at baseline in the lines without ADGRD1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[LINC01508]] | C | ADGRD1 activity raises LINC01508's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without ADGRD1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[ST8SIA4]] | C | ADGRD1 activity raises ST8SIA4's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without ADGRD1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[SMOC1]] | C | ADGRD1 activity raises SMOC1's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without ADGRD1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |
| [[LINC01257]] | C | ADGRD1 activity raises LINC01257's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.28× lower at baseline in the lines without ADGRD1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 36.3); signed map (43.1, 44.0). **Vector** length 43.0, 17.5% of its response variance represented; |z| ≥ 3 in 216 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.52 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | -0.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -4.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:130,953,907-131,141,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434B1272, PGR25; previously GPR133 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily D |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6QNK2](https://www.uniprot.org/uniprotkb/Q6QNK2) (Adhesion G protein-coupled receptor D1):

> Adhesion G protein-coupled receptor (aGPCR) for androgen hormone 5alpha-dihydrotestosterone (5alpha-DHT), also named 17beta-hydroxy-5alpha-androstan-3-one, the most potent hormone among androgens. Also activated by methenolone drug. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. ADGRD1 is coupled to G(s) G proteins and mediates activation of …

**Summary**, from NCBI Gene [283383](https://www.ncbi.nlm.nih.gov/gene/283383):

> The adhesion G-protein-coupled receptors (GPCRs), including GPR133, are membrane-bound proteins with long N termini containing multiple domains. GPCRs, or GPRs, contain 7 transmembrane domains and transduce extracellular signals through heterotrimeric G proteins (summary by Bjarnadottir et al., 2004 [PubMed 15203201]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:19893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19893) · Entrez [283383](https://www.ncbi.nlm.nih.gov/gene/283383) · UniProt [Q6QNK2](https://www.uniprot.org/uniprotkb/Q6QNK2) · Ensembl [ENSG00000111452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111452)

## Data

Gene col 3235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3235); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3235]; `tensor/DDL_lfc|DDL_z.npy` [3235]; `embed/gene_vectors.npy` [3235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3235 or target_col == 3235). Every well: [[ADGRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
