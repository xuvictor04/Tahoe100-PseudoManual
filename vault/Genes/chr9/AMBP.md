---
symbol: "AMBP"
type: "gene"
col: 2814
ensembl_id: "ENSG00000106927"
name: "alpha-1-microglobulin/bikunin precursor"
location: "9q32"
module: 8
arm: "+"
pooled_cpm: 5.22
n_lines_expressing: 9
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# AMBP

*alpha-1-microglobulin/bikunin precursor* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.33× (z +10.3, q 4e-22, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +9.1, q 1e-17, up in 4 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.160×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.133×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.172×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSG]] (+0.67, fdr 7e-06), [[ALB]] (+0.67, fdr 7e-06), [[AGT]] (+0.60, fdr 1e-05); moves opposite to [[POGK]] (-0.52, fdr 1e-04), [[RAD51D]] (-0.51, fdr 2e-04), [[UBL4A]] (-0.47, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIGR]] → it (grade C ⚠); 13 go from it, the strongest it → [[NDUFA4L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.33×** | +10.3 | 4e-22 | 2/2 (HepG2/C3A, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.66×** | +10.2 | 6e-22 | 3/3 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +9.1 | 1e-17 | 4/4 (HEC-1-A, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.54×** | +8.5 | 3e-15 | 2/2 (A498, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +6.5 | 7e-09 | 2/4 (HepG2/C3A, HT-29) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.49×** | +6.5 | 1e-08 | 2/4 (HepG2/C3A, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.009 | 1/5 (HEC-1-A) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.53×** | +3.5 | 0.028 | 1/2 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.87×** | +3.3 | 0.053 | 2/4 (A498, HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.84×** | +3.3 | 0.061 | 0/5 | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.93×** | +3.2 | 0.061 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.77× | +3.0 | 0.11 | 0/5 | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.160×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.133×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.172×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.484× | -3.7 | 0.12 | 1/5 (HT-29) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.552× | -3.2 | 0.36 | 3/5 (HepG2/C3A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 378 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +10.8) | — |
| [[A-172 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.991 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.651 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSG]] | +0.67 | +0.76 / +0.60 | both halves | 7e-06 | STRING 932 |
| [[ALB]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 970 |
| [[AGT]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 | STRING 612 |
| [[APOA1]] | +0.59 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 891 |
| [[AFP]] | +0.54 | +0.64 / +0.55 | both halves | 1e-05 | STRING 823 |
| [[SVBP]] | +0.51 | +0.34 / +0.36 | both halves | 1e-04 |  |
| [[SOD3]] | +0.51 | +0.41 / +0.20 | ⚠ not reproduced | 7e-04 |  |
| [[PIGR]] | +0.50 | +0.39 / +0.36 | both halves | 9e-05 |  |
| [[OXR1-AS1]] | +0.50 | +0.27 / +0.39 | both halves | 3e-04 |  |
| [[SLC23A1]] | +0.49 | +0.32 / +0.48 | both halves | 1e-04 |  |
| [[C12orf40]] | +0.48 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[MTCP1]] | +0.48 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ZBTB20-AS5]] | +0.47 | +0.38 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.52 | -0.44 / -0.32 | both halves | 1e-04 |  |
| [[RAD51D]] | -0.51 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[UBL4A]] | -0.47 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[BAZ1B]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[COA7]] | -0.45 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[IFRD2]] | -0.45 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[CFAP298]] | -0.44 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[RBM28]] | -0.44 | -0.43 / -0.26 | both halves | 3e-04 |  |
| [[DCLRE1A]] | -0.44 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[PTCD2]] | -0.44 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[PSMG1]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[RIOX2]] | -0.44 | -0.40 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIGR]] | C | PIGR activity raises AMBP's level | lines that do not express PIGR (45) vs lines expressing it (5) | 1.94× lower at baseline in the lines without PIGR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises AMBP's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without SERPINF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[SOD3]] | C | SOD3 activity raises AMBP's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 1.12× lower at baseline in the lines without SOD3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |
| [[AGT]] | C | AGT activity raises AMBP's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.98× lower at baseline in the lines without AGT | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFA4L2]] | B | AMBP activity raises NDUFA4L2's level | lines that do not express AMBP (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without AMBP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[SLC3A1]] | B | AMBP activity raises SLC3A1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.18× lower at baseline in the lines without AMBP | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[CYP2U1-AS1]] | B | AMBP activity raises CYP2U1-AS1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.19× lower at baseline in the lines without AMBP | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[ZBTB20-AS5]] | B | AMBP activity raises ZBTB20-AS5's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without AMBP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[PMEL]] | B | AMBP activity raises PMEL's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.20× lower at baseline in the lines without AMBP | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[CHMP3-AS1]] | B | AMBP activity raises CHMP3-AS1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.10× lower at baseline in the lines without AMBP | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[TICAM2-AS1]] | B | AMBP activity raises TICAM2-AS1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.09× lower at baseline in the lines without AMBP | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[SLC23A1]] | B | AMBP activity raises SLC23A1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.12× lower at baseline in the lines without AMBP | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[CNTNAP2]] | B | AMBP activity raises CNTNAP2's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.97× lower at baseline in the lines without AMBP | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[MTCP1]] | B | AMBP activity raises MTCP1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.48× lower at baseline in the lines without AMBP | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[AGT]] | C | AMBP activity raises AGT's level | lines that do not express AMBP (41) vs lines expressing it (9) | 4.23× lower at baseline in the lines without AMBP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2; co-absent with the target |
| [[APOH]] | C | AMBP activity raises APOH's level | lines that do not express AMBP (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without AMBP | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.223). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, 55.0); signed map (66.8, 20.0). **Vector** length 10.7, 2.32% of its response variance represented; |z| ≥ 3 in 98 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.4 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.3 | -2.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.3 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1-microglobulin/bikunin precursor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,060,127-114,078,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UTI, HCP, EDC1, HI30, IATIL, ITILC; previously ITI, ITIL |
| Gene groups (HGNC) | Lipocalins; Oxidoreductases |
| Reactome | 3 pathways, smallest: Scavenging of heme from plasma; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P02760](https://www.uniprot.org/uniprotkb/P02760) (Protein AMBP):

> [Alpha-1-microglobulin]: Antioxidant and tissue repair protein with reductase, heme-binding and radical-scavenging activities. Removes and protects against harmful oxidants and repairs macromolecules in intravascular and extravascular spaces and in intracellular compartments. Intravascularly, plays a regulatory role in red cell homeostasis by preventing heme- and reactive oxygen species-induced cell damage. Binds and degrades free heme to protect fetal and adult red blood cells from hemolysis. …

**Summary**, from NCBI Gene [259](https://www.ncbi.nlm.nih.gov/gene/259):

> This gene encodes a complex glycoprotein secreted in plasma. The precursor is proteolytically processed into distinct functioning proteins: alpha-1-microglobulin, which belongs to the superfamily of lipocalin transport proteins and may play a role in the regulation of inflammatory processes, and bikunin, which is a urinary trypsin inhibitor belonging to the superfamily of Kunitz-type protease inhibitors and plays an important role in many physiological and pathological processes. This gene is …

**Accessions** — [HGNC:453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:453) · Entrez [259](https://www.ncbi.nlm.nih.gov/gene/259) · UniProt [P02760](https://www.uniprot.org/uniprotkb/P02760) · Ensembl [ENSG00000106927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106927)

## Data

Gene col 2814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2814); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2814]; `tensor/DDL_lfc|DDL_z.npy` [2814]; `embed/gene_vectors.npy` [2814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2814 or target_col == 2814). Every well: [[AMBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
