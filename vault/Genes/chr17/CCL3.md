---
symbol: "CCL3"
type: "gene"
col: 15896
ensembl_id: "ENSG00000277632"
name: "C-C motif chemokine ligand 3"
location: "17q12"
module: 125
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 18
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# CCL3

*C-C motif chemokine ligand 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 11.6× (z +8.2, q 1e-13, up in 5 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.0996×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNLIPRP3]] (+0.70, fdr 7e-06), [[LINC02154]] (+0.60, fdr 1e-05), [[CXCL8]] (+0.59, fdr 2e-05); moves opposite to [[ZDHHC7]] (-0.49, fdr 2e-05), [[SLC15A5]] (-0.48, fdr 9e-04, ⚠ one half only (not replicated)), [[SLITRK5]] (-0.47, fdr 1e-04), [[LRRC63]] (-0.46, fdr 2e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAGEA1]] → it (grade C ⚠); 18 go from it, the strongest it → [[ACVR1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.6×** | +8.2 | 1e-13 | 5/5 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.69×** | +7.3 | 6e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.91×** | +6.5 | 2e-08 | 4/5 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.52×** | +6.3 | 4e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.52×** | +5.7 | 1e-06 | 2/2 (NCI-H460, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.35×** | +5.6 | 2e-06 | 9/9 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.59×** | +4.7 | 2e-04 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.80×** | +4.3 | 0.001 | 5/6 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.75×** | +4.3 | 0.001 | 1/2 (NCI-H460) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.49×** | +4.2 | 0.002 | 7/9 (NCI-H460, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.32×** | +4.0 | 0.003 | 3/6 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.34×** | +3.9 | 0.005 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.80×** | +3.4 | 0.025 | 4/6 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.76×** | +3.4 | 0.028 | 5/10 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **2.62×** | +3.2 | 0.047 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.52×** | +3.1 | 0.069 | 4/7 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +3.0 | 0.083 | 0/8 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.0996×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.530× | -3.1 | 0.84 | 0/10 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.79 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0996× (z -9.5) |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.135 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.167 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.157 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.598 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.155 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNLIPRP3]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC02154]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 977 |
| [[C12orf50]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ACTN2]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LINC01828]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[BMP2]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[INHBA]] | +0.53 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[C11orf96]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[TRIML2]] | +0.53 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[IL6]] | +0.53 | +0.40 / +0.65 | both halves | 4e-05 | pathway: Interleukin-10 signaling; STRING 962 |
| [[TRAF1]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC7]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SLC15A5]] | -0.48 | -0.58 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SLITRK5]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LRRC63]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[FAM120A]] | -0.43 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[SMARCD2]] | -0.42 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ABCB10]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[SCARA5]] | -0.42 | -0.50 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[PLOD3]] | -0.41 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[NUP133]] | -0.41 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[ZNF595]] | -0.41 | -0.30 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA1]] | C | MAGEA1 activity raises CCL3's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without MAGEA1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises CCL3's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 1.88× lower at baseline in the lines without LINC01592 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises CCL3's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without INHBA | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[LINC02154]] | C | LINC02154 activity raises CCL3's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without LINC02154 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises CCL3's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.08× lower at baseline in the lines without SCARA5 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises CCL3's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without SCN3A | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 9, C 9. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACVR1C]] | B | CCL3 activity raises ACVR1C's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 1.97× lower at baseline in the lines without CCL3 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under Omeprazole 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.79× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[KBTBD8]] | B | CCL3 activity raises KBTBD8's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 1.82× lower at baseline in the lines without CCL3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[C12orf50]] | B | CCL3 activity raises C12orf50's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 1.62× lower at baseline in the lines without CCL3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.79× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[Hesperidin (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.83× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[Methylthiouracil (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.80× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.82× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | B | CCL3 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[IL6]] | C | CCL3 activity raises IL6's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 11.58× lower at baseline in the lines without CCL3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[INHBA]] | C | CCL3 activity raises INHBA's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 6.76× lower at baseline in the lines without CCL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[CCL5]] | C | CCL3 activity raises CCL5's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 5.27× lower at baseline in the lines without CCL3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.3, 21.4); signed map (37.6, 22.2). **Vector** length 24.0, 8.18% of its response variance represented; |z| ≥ 3 in 127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +1.5 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.5 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.5 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.4 | +0.5 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine ligand 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,088,256-36,090,169 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G0S19-1, LD78ALPHA, MIP-1-alpha, LD78, SCI; previously SCYA3 |
| Gene groups (HGNC) | Chemokine ligands |
| Reactome | 10 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells); Chemokine receptors bind chemokines; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P10147](https://www.uniprot.org/uniprotkb/P10147) (C-C motif chemokine 3):

> Monokine with inflammatory and chemokinetic properties. Binds to CCR1, CCR4 and CCR5. One of the major HIV-suppressive factors produced by CD8+ T-cells. Recombinant MIP-1-alpha induces a dose-dependent inhibition of different strains of HIV-1, HIV-2, and simian immunodeficiency virus (SIV).

**Summary**, from NCBI Gene [6348](https://www.ncbi.nlm.nih.gov/gene/6348):

> This locus represents a small inducible cytokine. The encoded protein, also known as macrophage inflammatory protein 1 alpha, plays a role in inflammatory responses through binding to the receptors CCR1, CCR4 and CCR5. Polymorphisms at this locus may be associated with both resistance and susceptibility to infection by human immunodeficiency virus type 1.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:10627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10627) · Entrez [6348](https://www.ncbi.nlm.nih.gov/gene/6348) · UniProt [P10147](https://www.uniprot.org/uniprotkb/P10147) · Ensembl [ENSG00000277632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277632)

## Data

Gene col 15896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15896); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15896]; `tensor/DDL_lfc|DDL_z.npy` [15896]; `embed/gene_vectors.npy` [15896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15896 or target_col == 15896). Every well: [[CCL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
