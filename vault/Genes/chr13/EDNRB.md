---
symbol: "EDNRB"
type: "gene"
col: 5828
ensembl_id: "ENSG00000136160"
name: "endothelin receptor type B"
location: "13q22.3"
module: 87
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 16
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 24
direction_downstream: 38
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# EDNRB

*endothelin receptor type B* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.00× (z +10.1, q 2e-21, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +6.7, q 3e-09, up in 0 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.498× (z -4.0, q 0.029, down in 1 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.0647×, SK-MEL-2 0.183×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.162×; ⚠ cell-cycle shift, explains ~35% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYR]] (+0.69, fdr 7e-06), [[A2M]] (+0.67, fdr 7e-06), [[LHFPL3-AS1]] (+0.66, fdr 7e-06); moves opposite to [[C11orf80]] (-0.42, fdr 1e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[IHO1]] → it (grade C ⚠); 38 go from it, the strongest it → [[C11orf80]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.00×** | +10.1 | 2e-21 | 1/3 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.95×** | +10.0 | 5e-21 | 3/7 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.42×** | +8.6 | 2e-15 | 2/4 (J82, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +6.7 | 3e-09 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.70×** | +5.8 | 7e-07 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.7 | 2e-04 | 3/7 (J82, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +4.5 | 6e-04 | 2/9 (LS 180, J82) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.4 | 7e-04 | 0/7 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.0 | 0.005 | 2/7 (J82, hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.010 | 0/12 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +3.7 | 0.013 | 1/5 (J82) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.013 | 0/8 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +3.4 | 0.025 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.034 | 0/8 | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.045 | 1/9 (J82) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Pimozide (drug)]] 0.05 µM |  | **1.66×** | +3.1 | 0.060 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.070 | 2/12 (NCI-H460, LOX-IMVI) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.0647×, SK-MEL-2 0.183×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.162×; ⚠ cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.498×** | -4.0 | 0.029 | 1/12 (NCI-H460) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.618× | -3.0 | 0.70 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.9) |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -12.0) |
| [[A-172 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.689 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.590 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.316 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYR]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 | pathway: MITF-M-regulated melanocyte development; STRING 691 |
| [[A2M]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LHFPL3-AS1]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GAS7]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[TRPM8]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PI15]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MMP16]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SDC2]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf80]] | -0.42 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IHO1]] | C | IHO1 activity raises EDNRB's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.27× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises EDNRB's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without TTTY10 | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises EDNRB's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without BCHE | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[ARHGAP6]] | C | ARHGAP6 activity raises EDNRB's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without ARHGAP6 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises EDNRB's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without LINC02941 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises EDNRB's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without LOXL3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises EDNRB's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without COL19A1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[TXLNGY]], [[TXLNGY-1]] | C | TXLNGY, TXLNGY-1 activity raises EDNRB's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.39× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[AEBP1]] | C | AEBP1 activity raises EDNRB's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.68× lower at baseline in the lines without AEBP1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises EDNRB's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without LINC01687 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises EDNRB's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.92× lower at baseline in the lines without FCRLA | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises EDNRB's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 1.91× lower at baseline in the lines without LINC01242 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 1, C 37. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf80]] | B | EDNRB activity lowers C11orf80's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 1.50× higher at baseline in the lines without EDNRB | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2 |
| [[PDE3A]] | C | EDNRB activity raises PDE3A's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.61× lower at baseline in the lines without EDNRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[COL19A1]] | C | EDNRB activity raises COL19A1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without EDNRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[AEBP1]] | C | EDNRB activity raises AEBP1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.65× lower at baseline in the lines without EDNRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[KCNE4]] | C | EDNRB activity raises KCNE4's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.92× lower at baseline in the lines without EDNRB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[DAAM2]] | C | EDNRB activity raises DAAM2's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without EDNRB | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LINC01098]] | C | EDNRB activity raises LINC01098's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without EDNRB | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LOXL3]] | C | EDNRB activity raises LOXL3's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.77× lower at baseline in the lines without EDNRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[C10orf90]] | C | EDNRB activity raises C10orf90's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.32× lower at baseline in the lines without EDNRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[MIR3681HG]] | C | EDNRB activity raises MIR3681HG's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 5.64× lower at baseline in the lines without EDNRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LHFPL3-AS1]] | C | EDNRB activity raises LHFPL3-AS1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without EDNRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[COL11A1]] | C | EDNRB activity raises COL11A1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.67× lower at baseline in the lines without EDNRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.9, 29.0); signed map (29.8, 39.6). **Vector** length 26.0, 6.31% of its response variance represented; |z| ≥ 3 in 246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.6 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | -0.2 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -0.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | endothelin receptor type B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:77,895,481-77,975,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ETB; previously HSCR2, HSCR |
| Gene groups (HGNC) | Endothelin receptors |
| Reactome | 8 pathways, smallest: Transcriptional and post-translational regulation of MITF-M expression and activity; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P24530](https://www.uniprot.org/uniprotkb/P24530) (Endothelin receptor type B):

> Non-specific receptor for endothelin 1, 2, and 3. Mediates its action by association with G proteins that activate a phosphatidylinositol-calcium second messenger system.

**Summary**, from NCBI Gene [1910](https://www.ncbi.nlm.nih.gov/gene/1910):

> The protein encoded by this gene is a G protein-coupled receptor which activates a phosphatidylinositol-calcium second messenger system. Its ligand, endothelin, consists of a family of three potent vasoactive peptides: ET1, ET2, and ET3. Studies suggest that the multigenic disorder, Hirschsprung disease type 2, is due to mutations in the endothelin receptor type B gene. Alternative splicing and the use of alternative promoters results in multiple transcript variants. [provided by RefSeq, Oct …

**Accessions** — [HGNC:3180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3180) · Entrez [1910](https://www.ncbi.nlm.nih.gov/gene/1910) · UniProt [P24530](https://www.uniprot.org/uniprotkb/P24530) · Ensembl [ENSG00000136160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136160)

## Data

Gene col 5828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5828); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5828]; `tensor/DDL_lfc|DDL_z.npy` [5828]; `embed/gene_vectors.npy` [5828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5828 or target_col == 5828). Every well: [[EDNRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDNRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
