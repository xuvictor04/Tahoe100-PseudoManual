---
symbol: "CPLX2"
type: "gene"
col: 7044
ensembl_id: "ENSG00000145920"
name: "complexin 2"
location: "5q35.2"
module: 27
arm: "+"
pooled_cpm: 8.86
n_lines_expressing: 9
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CPLX2

*complexin 2* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.28× (z +15.4, q 0e+00, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +10.4, q 4e-23, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.601× (z -3.9, q 0.045, down in 0 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (SW1417 0.209×, SW480 0.191×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR0B1]] (+0.56, fdr 2e-05), [[CSMD3]] (+0.54, fdr 5e-05), [[KLK6]] (+0.52, fdr 3e-05); moves opposite to [[NR2E3]] (-0.50, fdr 5e-05), [[GLTP]] (-0.47, fdr 5e-05), [[ZMAT5]] (-0.45, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PCSK1]] → it (grade C ⚠); 9 go from it, the strongest it → [[PLXNB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.28×** | +15.4 | 0e+00 | 5/6 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.90×** | +14.4 | 1e-44 | 4/5 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.35×** | +12.0 | 5e-31 | 5/5 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +10.4 | 4e-23 | 2/7 (A549, NCI-H460) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +6.8 | 9e-10 | 4/7 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +5.6 | 2e-06 | 1/7 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.1 | 3e-05 | 5/7 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.001 | 0/7 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.77×** | +4.1 | 0.002 | 2/6 (A549, SW1417) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.013 | 0/7 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.55×** | +3.4 | 0.037 | 2/7 (NCI-H1573, NCI-H460) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.040 | 0/7 | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.52×** | +3.2 | 0.049 | 1/7 (SW480) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +3.2 | 0.049 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7044.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (SW1417 0.209×, SW480 0.191×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.601×** | -3.9 | 0.045 | 0/7 | two highest doses | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.641× | -3.2 | 0.27 | 0/7 | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.671× | -3.1 | 0.27 | 0/7 | two highest doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.652× | -3.1 | 0.27 | 0/7 | inconsistent across doses | position effect removed |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.654× | -3.0 | 0.27 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 26.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 27.9× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.21× (z +9.5) | — |
| [[SW480 (line)]] | alt | 24.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.93× (z +12.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.191× (z -8.7) |
| [[SW1417 (line)]] | alt | 157 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.97× (z +8.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.209× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 2.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.8× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR0B1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CSMD3]] | +0.54 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[KLK6]] | +0.52 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[APCDD1]] | +0.51 | +0.53 / +0.37 | both halves | 9e-05 |  |
| [[IGFL4]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[MIR4500HG]] | +0.50 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[COLGALT2]] | +0.50 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[RMST]] | +0.50 | +0.47 / +0.26 | both halves | 4e-04 |  |
| [[VWA2]] | +0.49 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[PCSK1]] | +0.49 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[SLC30A10]] | +0.48 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[FGF19]] | +0.48 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2E3]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[GLTP]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ZMAT5]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[CREG2]] | -0.43 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[DUSP18]] | -0.42 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[CRLF2]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ULBP2]] | -0.42 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[FEZ2]] | -0.42 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[CCDC126]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[P4HA3]] | -0.41 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[C9orf72]] | -0.39 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[NQO2]] | -0.39 | -0.29 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1]] | C | PCSK1 activity raises CPLX2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.72× lower at baseline in the lines without PCSK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises CPLX2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without JAKMIP2-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[FGL1]] | C | FGL1 activity raises CPLX2's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without FGL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises CPLX2's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without FKBP9P1-1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises CPLX2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.16× lower at baseline in the lines without CSMD3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises CPLX2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without ANO4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNB1]] | B | CPLX2 activity raises PLXNB1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 1.55× lower at baseline in the lines without CPLX2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5 |
| [[APCDD1]] | C | CPLX2 activity raises APCDD1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 3.01× lower at baseline in the lines without CPLX2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[LINC01622]] | C | CPLX2 activity raises LINC01622's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 2.08× lower at baseline in the lines without CPLX2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[PCSK1]] | C | CPLX2 activity raises PCSK1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 4.02× lower at baseline in the lines without CPLX2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[PROX1]] | C | CPLX2 activity raises PROX1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 4.41× lower at baseline in the lines without CPLX2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[RIMBP2]] | C | CPLX2 activity raises RIMBP2's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 3.17× lower at baseline in the lines without CPLX2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[JAKMIP2-AS1]] | C | CPLX2 activity raises JAKMIP2-AS1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 2.48× lower at baseline in the lines without CPLX2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[NKD1]] | C | CPLX2 activity raises NKD1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 3.86× lower at baseline in the lines without CPLX2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[PKHD1]] | C | CPLX2 activity raises PKHD1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 2.19× lower at baseline in the lines without CPLX2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 41.6); signed map (65.2, 15.5). **Vector** length 32.4, 12.6% of its response variance represented; |z| ≥ 3 in 195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +14.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.7 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.7 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.6 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.6 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -0.9 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | complexin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:175,796,310-175,884,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPX-2, DKFZp547D155 |
| Gene groups (HGNC) | Complexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PUV4](https://www.uniprot.org/uniprotkb/Q6PUV4) (Complexin-2):

> Negatively regulates the formation of synaptic vesicle clustering at active zone to the presynaptic membrane in postmitotic neurons. Positively regulates a late step in exocytosis of various cytoplasmic vesicles, such as synaptic vesicles and other secretory vesicles. Also involved in mast cell exocytosis (By similarity).

**Summary**, from NCBI Gene [10814](https://www.ncbi.nlm.nih.gov/gene/10814):

> Proteins encoded by the complexin/synaphin gene family are cytosolic proteins that function in synaptic vesicle exocytosis. These proteins bind syntaxin, part of the SNAP receptor. The protein product of this gene binds to the SNAP receptor complex and disrupts it, allowing transmitter release. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2310) · Entrez [10814](https://www.ncbi.nlm.nih.gov/gene/10814) · UniProt [Q6PUV4](https://www.uniprot.org/uniprotkb/Q6PUV4) · Ensembl [ENSG00000145920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145920)

## Data

Gene col 7044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7044); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7044]; `tensor/DDL_lfc|DDL_z.npy` [7044]; `embed/gene_vectors.npy` [7044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7044 or target_col == 7044). Every well: [[CPLX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPLX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
