---
symbol: "THBS4"
type: "gene"
col: 3445
ensembl_id: "ENSG00000113296"
name: "thrombospondin 4"
location: "5q14.1"
module: 10
arm: "+"
pooled_cpm: 4.74
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 18
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# THBS4

*thrombospondin 4* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.18× (z +9.4, q 4e-18, up in 34 of 41 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +8.0, q 3e-13, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.283× (z -10.7, q 4e-24, down in 36 of 41 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.539× (z -5.3, q 1e-05, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFF-DT]] (+0.80, fdr 1e-05), [[ATE1OSP]] (+0.77, fdr 1e-05), [[ZNF407-AS1]] (+0.77, fdr 7e-06); moves opposite to [[NPHP4]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NNT-AS1]] → it (grade B ⚠); 18 go from it, the strongest it → [[ZSCAN30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.18×** | +9.4 | 4e-18 | 34/41 (NCI-H2347, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.0 | 3e-13 | 29/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.5 | 9e-06 | 18/41 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +5.4 | 9e-06 | 22/39 (LoVo, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +5.4 | 1e-05 | 22/40 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.5 | 7e-04 | 3/9 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.66×** | +4.3 | 0.001 | 15/39 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.61×** | +4.1 | 0.003 | 13/40 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.003 | 8/41 (SW480, SNU-423, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.019 | 11/41 (CFPAC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.283×** | -10.7 | 4e-24 | 36/41 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.385×** | -8.1 | 1e-13 | 27/35 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.451×** | -6.8 | 2e-09 | 27/40 (SNU-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.490×** | -6.1 | 2e-07 | 25/40 (SW480, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.496×** | -6.0 | 2e-07 | 25/40 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.482×** | -6.0 | 2e-07 | 15/28 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.507×** | -5.8 | 6e-07 | 21/41 (RKO, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.539×** | -5.3 | 1e-05 | 21/39 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.553×** | -5.0 | 3e-05 | 20/39 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.590×** | -4.5 | 4e-04 | 18/41 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.369×** | -4.4 | 5e-04 | 13/29 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.714×** | -4.1 | 0.002 | 15/41 (SHP-77, C32, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.631×** | -3.9 | 0.004 | 15/41 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.634×** | -3.9 | 0.004 | 18/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.640×** | -3.8 | 0.005 | 18/40 (COLO 205, LS 180, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.679×** | -3.3 | 0.029 | 8/40 (J82, HCT15, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.687×** | -3.2 | 0.039 | 13/41 (PANC-1, SW 1088, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.05 µM |  | **0.690×** | -3.2 | 0.043 | 11/39 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.608×** | -3.0 | 0.062 | 6/40 (RKO, H4, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0156× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0824× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0818× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[HI-TOPK-032 (drug)]] 5 µM 0.0367× (z -8.6) |
| [[SNU-423 (line)]] | alt | 5.84 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0801× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 5.22 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 2.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0919× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0825× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 3.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0358× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.925 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | +0.80 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.77 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.77 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.75 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.75 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.75 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | +0.74 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[CCNT2]] | +0.74 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MAD2L1-DT]] | +0.73 | +0.73 / +0.37 | both halves | 8e-05 |  |
| [[ZNF596]] | +0.72 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.72 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[PNISR-AS1]] | +0.71 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.62 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT-AS1]] | B | NNT-AS1 activity lowers THBS4's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.69× higher at baseline in the lines without NNT-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-absent genes |
| [[ZNF610]] | B | ZNF610 activity raises THBS4's level | lines that do not express ZNF610 (14) vs lines expressing it (36) | 2.45× lower at baseline in the lines without ZNF610 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF549, LINC02456, ZNF382 |
| [[ZNF701]], [[ZNF808]] | B | ZNF701, ZNF808 activity raises THBS4's level | lines that do not express ZNF701, ZNF808 (6) vs lines expressing them (44) | 1.49× lower at baseline in the lines without ZNF701, ZNF808 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF468, ZNF28, ZNF888; co-absent genes |
| [[ZNF382]] | B | ZNF382 activity raises THBS4's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without ZNF382 | 0.044 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[LINC00665]] | B | LINC00665 activity raises THBS4's level | lines that do not express LINC00665 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without LINC00665 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ZNF518B |
| [[ZFP30]] | B | ZFP30 activity raises THBS4's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without ZFP30 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF790]] | B | ZNF790 activity raises THBS4's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without ZNF790 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |
| [[GPRASP3]] | C | GPRASP3 activity raises THBS4's level | lines that do not express GPRASP3 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without GPRASP3 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DCP1B, ST8SIA5, DISC1; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN30]] | B | THBS4 activity raises ZSCAN30's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 2.24× lower at baseline in the lines without THBS4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[ZSCAN30]] | B | THBS4 activity strengthens ZSCAN30's drug response | lines that do not express THBS4 (6) vs lines expressing it (42) | the lines without THBS4 respond 0.53× as strongly (z diff +2.15); strongest at Digitoxin 5 µM: 0.63x vs 0.26x (z diff +5.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DCP1B]] | B | THBS4 activity raises DCP1B's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without THBS4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[FAM174A-DT]] | B | THBS4 activity raises FAM174A-DT's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without THBS4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[GIN1]] | B | THBS4 activity raises GIN1's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without THBS4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[FAM200A]] | B | THBS4 activity raises FAM200A's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without THBS4 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[LINC00412]] | B | THBS4 activity raises LINC00412's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without THBS4 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[DNAJC30]] | B | THBS4 activity lowers DNAJC30's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without THBS4 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[ZNF234]] | B | THBS4 activity raises ZNF234's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without THBS4 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[TMEM69]] | B | THBS4 activity raises TMEM69's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.22× lower at baseline in the lines without THBS4 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[GPRASP3]] | B | THBS4 activity raises GPRASP3's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without THBS4 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[ZNF808]] | B | THBS4 activity raises ZNF808's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without THBS4 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.0, 15.7); signed map (27.2, -13.7). **Vector** length 63.9, 11.0% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.2 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.8 | -6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.3 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,991,311-80,083,287 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thrombospondin family |
| Reactome | 2 pathways, smallest: Signaling by PDGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P35443](https://www.uniprot.org/uniprotkb/P35443) (Thrombospondin-4):

> Adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions and is involved in various processes including cellular proliferation, migration, adhesion and attachment, inflammatory response to CNS injury, regulation of vascular inflammation and adaptive responses of the heart to pressure overload and in myocardial function and remodeling. Binds to structural extracellular matrix (ECM) proteins and modulates the ECM in response to tissue damage, contributing to …

**Summary**, from NCBI Gene [7060](https://www.ncbi.nlm.nih.gov/gene/7060):

> The protein encoded by this gene belongs to the thrombospondin protein family. Thrombospondin family members are adhesive glycoproteins that mediate cell-to-cell and cell-to-matrix interactions. This protein forms a pentamer and can bind to heparin and calcium. It is involved in local signaling in the developing and adult nervous system, and it contributes to spinal sensitization and neuropathic pain states. This gene is activated during the stromal response to invasive breast cancer. It may …

**Accessions** — [HGNC:11788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11788) · Entrez [7060](https://www.ncbi.nlm.nih.gov/gene/7060) · UniProt [P35443](https://www.uniprot.org/uniprotkb/P35443) · Ensembl [ENSG00000113296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113296)

## Data

Gene col 3445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3445); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3445]; `tensor/DDL_lfc|DDL_z.npy` [3445]; `embed/gene_vectors.npy` [3445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3445 or target_col == 3445). Every well: [[THBS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
