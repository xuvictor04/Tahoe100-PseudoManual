---
symbol: "ZIC1"
type: "gene"
col: 7676
ensembl_id: "ENSG00000152977"
name: "Zic family zinc finger 1"
location: "3q24"
module: 10
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 16
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZIC1

*Zic family zinc finger 1* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.75× (z +18.2, q 0e+00, up in 9 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.629× (z -3.8, q 0.040, down in 10 of 12 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Lucanthone (drug)]] 0.05 µM: 0.631× (z -3.5, q 0.058, down in 0 of 13 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR548XHG]] (+0.68, fdr 2e-05), [[MAGI2-AS3]] (+0.66, fdr 3e-05), [[CACNA2D1]] (+0.66, fdr 1e-04); moves opposite to [[WASF3]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[HOXB-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.75×** | +18.2 | 0e+00 | 9/12 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +12.5 | 4e-33 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.6 | 1e-15 | 2/10 (SHP-77, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +8.5 | 2e-15 | 3/8 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +6.5 | 1e-08 | 5/11 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.001 | 2/13 (A-172, C32) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.002 | 5/12 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +3.9 | 0.007 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.8 | 0.008 | 2/12 (RPMI-7951, A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.8 | 0.008 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.8 | 0.008 | 4/12 (H4, RPMI-7951, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.90×** | +3.8 | 0.008 | 1/10 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.018 | 4/12 (NCI-H1573, C32, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.4 | 0.026 | 1/9 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.046 | 3/12 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.73×** | +3.2 | 0.046 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.049 | 3/12 (A-427, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.050 | 0/12 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.082 | 6/12 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.093 | 1/12 (H4) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.629×** | -3.8 | 0.040 | 10/12 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -3.8 | 0.040 | 2/12 (NCI-H23, HS-578T) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.640×** | -3.7 | 0.040 | 10/13 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.631×** | -3.5 | 0.058 | 0/13 | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | **0.662×** | -3.4 | 0.070 | 0/12 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.666×** | -3.4 | 0.070 | 7/12 (H4, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.678× | -3.2 | 0.10 | 1/12 (SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -14.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 17.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0587× (z -14.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 16.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0486× (z -13.7) ⚠ cell-cycle shift, explains ~91% of this change |
| [[C32 (line)]] | wt | 15.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 49.8 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 4.96 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0323× (z -11.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0722× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.460 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR548XHG]] | +0.68 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MAGI2-AS3]] | +0.66 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CACNA2D1]] | +0.66 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[STPG2]] | +0.66 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[LINC01905]] | +0.64 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[FBXO38-DT]] | +0.63 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[LINC01687]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HOXD10]] | +0.63 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[NPAS3]] | +0.62 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TENM3-AS1]] | +0.62 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CDH8]] | +0.62 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[MGAT4C]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.57 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZIC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ZIC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises ZIC1's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[LINC02438]] | C | LINC02438 activity raises ZIC1's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 4.17× lower at baseline in the lines without LINC02438 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises ZIC1's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 4.89× lower at baseline in the lines without LINC00648 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[CDH8]] | C | CDH8 activity raises ZIC1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 4.10× lower at baseline in the lines without CDH8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises ZIC1's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.57× lower at baseline in the lines without TWIST1 | 0.046 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises ZIC1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 3.68× lower at baseline in the lines without LINC01687 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[LINC01139]] | C | LINC01139 activity raises ZIC1's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 2.87× lower at baseline in the lines without LINC01139 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises ZIC1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 4.04× lower at baseline in the lines without GABRG2 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB-AS1]] | B | ZIC1 activity raises HOXB-AS1's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 1.77× lower at baseline in the lines without ZIC1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN |
| [[CCDC30]] | B | ZIC1 activity raises CCDC30's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 1.36× lower at baseline in the lines without ZIC1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN |
| [[LINC02438]] | C | ZIC1 activity raises LINC02438's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 6.51× lower at baseline in the lines without ZIC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[CDH8]] | C | ZIC1 activity raises CDH8's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without ZIC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[TWIST1]] | C | ZIC1 activity raises TWIST1's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 5.94× lower at baseline in the lines without ZIC1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[PI15]] | C | ZIC1 activity raises PI15's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without ZIC1 | 0.071 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[OR3A2]] | C | ZIC1 activity raises OR3A2's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without ZIC1 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (35.5, 25.1); signed map (44.1, 28.5). **Vector** length 36.9, 10.2% of its response variance represented; |z| ≥ 3 in 266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.6 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -1.5 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -1.3 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Zic family zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:147,393,422-147,510,293 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZIC, ZNF201 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZIC family zinc fingers |
| Reactome | 4 pathways, smallest: Specification of the neural plate border; Transcriptional and post-translational regulation of MITF-M expression and activity; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15915](https://www.uniprot.org/uniprotkb/Q15915) (Zinc finger protein ZIC 1):

> Acts as a transcriptional activator. Involved in neurogenesis. Plays important roles in the early stage of organogenesis of the CNS, as well as during dorsal spinal cord development and maturation of the cerebellum. Involved in the spatial distribution of mossy fiber (MF) neurons within the pontine gray nucleus (PGN). Plays a role in the regulation of MF axon pathway choice. Promotes MF migration towards ipsilaterally-located cerebellar territories. May have a role in shear flow …

**Summary**, from NCBI Gene [7545](https://www.ncbi.nlm.nih.gov/gene/7545):

> This gene encodes a member of the ZIC family of C2H2-type zinc finger proteins. Members of this family are important during development. Aberrant expression of this gene is seen in medulloblastoma, a childhood brain tumor. This gene is closely linked to the gene encoding zinc finger protein of the cerebellum 4, a related family member on chromosome 3. This gene encodes a transcription factor that can bind and transactivate the apolipoprotein E gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12872) · Entrez [7545](https://www.ncbi.nlm.nih.gov/gene/7545) · UniProt [Q15915](https://www.uniprot.org/uniprotkb/Q15915) · Ensembl [ENSG00000152977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152977)

## Data

Gene col 7676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7676); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7676]; `tensor/DDL_lfc|DDL_z.npy` [7676]; `embed/gene_vectors.npy` [7676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7676 or target_col == 7676). Every well: [[ZIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
