---
symbol: "ZSCAN23"
type: "gene"
col: 11963
ensembl_id: "ENSG00000187987"
name: "zinc finger and SCAN domain containing 23"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 27
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN23

*zinc finger and SCAN domain containing 23* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.24× (z +10.3, q 5e-22, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.315× (z -10.1, q 4e-21, down in 18 of 23 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNYL2-1]] (+0.65, fdr 3e-05), [[CCNYL2]] (+0.63, fdr 4e-05), [[ZNF334]] (+0.59, fdr 1e-04); moves opposite to [[CTBP2]] (-0.49, fdr 3e-05), [[GNAQ]] (-0.44, fdr 1e-04), [[BCL2L14]] (-0.42, fdr 0.001, ⚠ not reproduced), [[MBOAT7]] (-0.41, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZSCAN12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.24×** | +10.3 | 5e-22 | 22/24 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +9.1 | 4e-17 | 19/22 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +7.2 | 1e-10 | 18/22 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +5.0 | 7e-05 | 13/23 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.002 | 10/24 (LS 180, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.007 | 3/21 (Panc 03.27, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.007 | 4/20 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.014 | 4/23 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.5 | 0.029 | 3/25 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.31×** | +3.3 | 0.053 | 3/23 (CFPAC-1, SW 900, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.074 | 6/20 (HS-578T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.11 | 4/21 (J82, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -10.1 | 4e-21 | 18/23 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.419×** | -7.3 | 9e-11 | 13/18 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -6.2 | 1e-07 | 16/22 (PANC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.495×** | -6.1 | 1e-07 | 11/22 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -4.6 | 5e-04 | 11/22 (J82, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.616×** | -4.2 | 0.002 | 9/13 (RPMI-7951, SNU-423, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.660×** | -3.6 | 0.025 | 11/20 (PANC-1, SNU-423, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.689× | -3.1 | 0.13 | 6/20 (SW 900, H4, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.608× | -3.1 | 0.13 | 5/19 (NCI-H1792, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.92 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0369× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0446× (z -13.6) |
| [[SNU-423 (line)]] | alt | 6.23 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0512× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 4.17 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0886× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -9.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0602× (z -14.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.659 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.417 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL2-1]] | +0.65 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[CCNYL2]] | +0.63 | +0.62 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[ZNF334]] | +0.59 | +0.35 / +0.57 | both halves | 1e-04 | same gene group |
| [[ZNF354C]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 | same gene group |
| [[ZNF571]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 | same gene group |
| [[ZNF284]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 | same gene group |
| [[C2orf74]] | +0.56 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[ZNF229]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF439]] | +0.54 | +0.57 / +0.39 | both halves | 5e-05 | same gene group |
| [[ZNF607]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 | same gene group |
| [[FRG1JP]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZNF793]] | +0.53 | +0.58 / +0.58 | both halves | 8e-06 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP2]] | -0.49 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[GNAQ]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[BCL2L14]] | -0.42 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[OVOL2]] | -0.42 | -0.08 / -0.29 | ⚠ not reproduced | 0.004 | same gene group |
| [[MBOAT7]] | -0.41 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SNTB2]] | -0.41 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ZNF704]] | -0.41 | -0.31 / -0.34 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ZSCAN23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ZSCAN23's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KCTD16]] | C | KCTD16 activity raises ZSCAN23's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without KCTD16 | 0.031 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[ZNF626]] | C | ZNF626 activity raises ZSCAN23's level | lines that do not express ZNF626 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without ZNF626 | 0.041 | ⚠ within organs, on part of the lines; also absent: ROS1, GDNF, HTRA3; co-absent with the target |
| [[ZNF229]] | C | ZNF229 activity raises ZSCAN23's level | lines that do not express ZNF229 (25) vs lines expressing it (25) | 2.52× lower at baseline in the lines without ZNF229 | 0.067 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, STAC, C15orf48; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN23 activity raises ZSCAN12's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without ZSCAN23 | 0.018 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[STRA6LP]] | B | ZSCAN23 activity raises STRA6LP's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ZSCAN23 | 0.050 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[SUGT1P4-STRA6LP]] | B | ZSCAN23 activity raises SUGT1P4-STRA6LP's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without ZSCAN23 | 0.051 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[SUGT1P4-STRA6LP-CCDC180]] | B | ZSCAN23 activity raises SUGT1P4-STRA6LP-CCDC180's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without ZSCAN23 | 0.067 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[TMEM30A-DT]] | B | ZSCAN23 activity raises TMEM30A-DT's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 1.24× lower at baseline in the lines without ZSCAN23 | 0.082 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3 |
| [[ZNF229]] | C | ZSCAN23 activity raises ZNF229's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 3.59× lower at baseline in the lines without ZSCAN23 | 0.015 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |
| [[ZNF626]] | C | ZSCAN23 activity raises ZNF626's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 2.83× lower at baseline in the lines without ZSCAN23 | 0.026 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |
| [[ZNF439]] | C | ZSCAN23 activity raises ZNF439's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 3.02× lower at baseline in the lines without ZSCAN23 | 0.037 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |
| [[KCTD16]] | C | ZSCAN23 activity raises KCTD16's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 3.68× lower at baseline in the lines without ZSCAN23 | 0.043 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |
| [[CCNYL2]] | C | ZSCAN23 activity raises CCNYL2's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without ZSCAN23 | 0.090 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.9, 22.6); signed map (-5.4, -32.3). **Vector** length 30.9, 4.29% of its response variance represented; |z| ≥ 3 in 580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +1.0 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.7 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +0.5 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | +1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,431,930-28,443,502 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ29K1.3.1; previously ZNF453, ZNF390 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MJ62](https://www.uniprot.org/uniprotkb/Q3MJ62) (Zinc finger and SCAN domain-containing protein 23):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [222696](https://www.ncbi.nlm.nih.gov/gene/222696):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21193) · Entrez [222696](https://www.ncbi.nlm.nih.gov/gene/222696) · UniProt [Q3MJ62](https://www.uniprot.org/uniprotkb/Q3MJ62) · Ensembl [ENSG00000187987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187987)

## Data

Gene col 11963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11963); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11963]; `tensor/DDL_lfc|DDL_z.npy` [11963]; `embed/gene_vectors.npy` [11963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11963 or target_col == 11963). Every well: [[ZSCAN23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
