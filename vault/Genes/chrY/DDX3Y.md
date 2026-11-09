---
symbol: "DDX3Y"
type: "gene"
col: 845
ensembl_id: "ENSG00000067048"
name: "DEAD-box helicase 3 Y-linked"
location: "Yq11.221"
module: 62
arm: "+"
pooled_cpm: 52.88
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DDX3Y

*DEAD-box helicase 3 Y-linked* — Yq11.221

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.33× (z +12.8, q 1e-34, up in 18 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.51× (z +9.8, q 3e-20, up in 18 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.527× (z -6.8, q 8e-09, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCHD4]] (+0.55, fdr 1e-04), [[TYMSOS]] (+0.53, fdr 1e-04), [[REV3L]] (+0.51, fdr 1e-04); moves opposite to [[BCR]] (-0.47, fdr 2e-04), [[UBE2F]] (-0.43, fdr 2e-04), [[YWHAB]] (-0.41, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GRIN2C]] → it (grade B ⚠); 10 go from it, the strongest it → [[BORCS7-ASMT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +12.8 | 1e-34 | 18/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +12.0 | 7e-31 | 1/19 (A-427) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.51×** | +9.8 | 3e-20 | 18/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +9.4 | 7e-19 | 2/16 (LoVo, A-172) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.04×** | +7.6 | 3e-12 | 16/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +6.9 | 5e-10 | 1/16 (LoVo) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +6.4 | 1e-08 | 18/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 5/18 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.69×** | +5.6 | 1e-06 | 13/18 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.3 | 6e-06 | 1/20 (NCI-H460) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.39×** | +5.0 | 3e-05 | 12/18 (COLO 205, A549, …) | top dose only | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 5e-04 | 0/18 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.004 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +3.8 | 0.005 | 16/19 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 0/18 | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.015 | 15/19 (A-172, J82, …) | rises with dose | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.015 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.055 | 0/18 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -6.8 | 8e-09 | 16/18 (SK-MEL-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -5.6 | 6e-06 | 16/18 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.660×** | -4.4 | 0.002 | 18/18 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.640×** | -4.3 | 0.002 | 0/18 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -4.0 | 0.007 | 14/18 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.5 | 0.040 | 0/20 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.789×** | -3.4 | 0.050 | 1/18 (A549) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.553×** | -3.3 | 0.076 | 15/19 (SK-MEL-2, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.809× | -3.1 | 0.11 | 18/18 (LoVo, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 282 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.73× (z +16.7) | — |
| [[LoVo (line)]] | wt | 116 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.92× (z +15.5) | — |
| [[C32 (line)]] | wt | 164 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 9.75× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -8.6) |
| [[COLO 205 (line)]] | alt | 109 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.57× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.4) ⚠ cell-cycle shift, explains ~97% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -8.7) |
| [[SNU-1 (line)]] | wt | 197 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +10.2) | — |
| [[A-427 (line)]] | wt | 116 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -8.6) |
| [[A549 (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.5) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[H4 (line)]] | wt | 223 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 175 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -9.0) |
| [[J82 (line)]] | alt | 96.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[A-172 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCHD4]] | +0.55 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[TYMSOS]] | +0.53 | +0.33 / +0.38 | both halves | 1e-04 |  |
| [[REV3L]] | +0.51 | +0.32 / +0.47 | both halves | 1e-04 |  |
| [[GRIN2C]] | +0.51 | +0.32 / +0.42 | both halves | 2e-04 |  |
| [[ACTA2]] | +0.51 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[DDB2]] | +0.50 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[EDA2R]] | +0.49 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[C12orf50]] | +0.49 | +0.41 / +0.28 | both halves | 3e-04 |  |
| [[MAP7D2]] | +0.49 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[CABYR]] | +0.48 | +0.24 / +0.39 | both halves | 4e-04 |  |
| [[GLS2]] | +0.48 | +0.45 / +0.32 | both halves | 1e-04 |  |
| [[TRIML2]] | +0.48 | +0.43 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | -0.47 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[UBE2F]] | -0.43 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[YWHAB]] | -0.41 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[GTF2E2]] | -0.41 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[FAM118B]] | -0.41 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[MBOAT2]] | -0.40 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[STIMATE]] | -0.40 | -0.19 / -0.35 | ⚠ not reproduced | 8e-04 |  |
| [[HERC2P9]] | -0.40 | -0.15 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[COMMD2]] | -0.40 | -0.38 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIN2C]] | B | GRIN2C activity raises DDX3Y's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 3.31× lower at baseline in the lines without GRIN2C | 0.027 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises DDX3Y's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UTY]] | C | UTY activity raises DDX3Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 19.46× lower at baseline in the lines without UTY | 6e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[RPS4Y1]] | C | RPS4Y1 activity raises DDX3Y's level | lines that do not express RPS4Y1 (30) vs lines expressing it (20) | 12.57× lower at baseline in the lines without RPS4Y1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, LINC00278; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BORCS7-ASMT]] | B | DDX3Y activity raises BORCS7-ASMT's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without DDX3Y | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[FDXR]] | B | DDX3Y activity raises FDXR's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without DDX3Y | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[HAND2-AS1]] | B | DDX3Y activity raises HAND2-AS1's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without DDX3Y | 0.059 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[CAB39]] | B | DDX3Y activity lowers CAB39's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.35× higher at baseline in the lines without DDX3Y | 0.071 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[FAP]] | B | DDX3Y activity raises FAP's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without DDX3Y | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[ANKRA2]] | B | DDX3Y activity raises ANKRA2's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.27× lower at baseline in the lines without DDX3Y | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[C12orf50]] | B | DDX3Y activity raises C12orf50's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without DDX3Y | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[UTY]] | C | DDX3Y, [[KDM5D]] activity raises UTY's level | lines that do not express DDX3Y, KDM5D (30) vs lines expressing them (20) | 24.64× lower at baseline in the lines without DDX3Y, KDM5D | 5e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[RPS4Y1]] | C | DDX3Y activity raises RPS4Y1's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 10.78× lower at baseline in the lines without DDX3Y | 5e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[EDA2R]] | C | DDX3Y activity raises EDA2R's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 2.79× lower at baseline in the lines without DDX3Y | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, 35.4); signed map (40.9, -22.4). **Vector** length 53.3, 14.8% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +0.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.7 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | +2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 3 Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.221 — chrY:12,904,108-12,920,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DBY |
| Gene groups (HGNC) | DEAD-box helicases; Minor histocompatibility antigens |
| Matched by | ensembl_id |

**Function**, from UniProt [O15523](https://www.uniprot.org/uniprotkb/O15523) (ATP-dependent RNA helicase DDX3Y):

> Probable ATP-dependent RNA helicase. During immune response, may enhance IFNB1 expression via IRF3/IRF7 pathway (By similarity).

**Summary**, from NCBI Gene [8653](https://www.ncbi.nlm.nih.gov/gene/8653):

> The protein encoded by this gene is a member of the DEAD-box RNA helicase family, characterized by nine conserved motifs, included the conserved Asp-Glu-Ala-Asp (DEAD) motif. These motifs are thought to be involved in ATP binding, hydrolysis, RNA binding, and in the formation of intramolecular interactions. This protein shares high similarity to DDX3X, on the X chromosome, but a deletion of this gene is not complemented by DDX3X. Mutations in this gene result in male infertility, a reduction in …

**Accessions** — [HGNC:2699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2699) · Entrez [8653](https://www.ncbi.nlm.nih.gov/gene/8653) · UniProt [O15523](https://www.uniprot.org/uniprotkb/O15523) · Ensembl [ENSG00000067048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067048)

## Data

Gene col 845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 845); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 845]; `tensor/DDL_lfc|DDL_z.npy` [845]; `embed/gene_vectors.npy` [845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 845 or target_col == 845). Every well: [[DDX3Y — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX3Y.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
