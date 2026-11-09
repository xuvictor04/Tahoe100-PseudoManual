---
symbol: "AK5"
type: "gene"
col: 7762
ensembl_id: "ENSG00000154027"
name: "adenylate kinase 5"
location: "1p31.1"
module: 13
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 25
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 19
direction_downstream: 32
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# AK5

*adenylate kinase 5* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.09× (z +14.9, q 0e+00, up in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +13.4, q 1e-38, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.660× (z -4.4, q 0.006, down in 12 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.178×, HOP62 0.178×, Hs 766T 0.143×, A498 0.274×; ⚠ cell-cycle shift, explains ~47% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0302×, hTERT-HPNE 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (J82 0.132×); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.0661×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA4]] (+0.70, fdr 7e-06), [[ADAMTS12]] (+0.67, fdr 7e-06), [[INSYN2B]] (+0.65, fdr 7e-06); moves opposite to [[TNFAIP6]] (-0.55, fdr 3e-05), [[KIF13B]] (-0.47, fdr 4e-05), [[MUC1]] (-0.47, fdr 9e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ITGA4]] → it (grade C ⚠); 32 go from it, the strongest it → [[FBLN7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +14.9 | 0e+00 | 10/12 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.24×** | +14.6 | 0e+00 | 11/12 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +13.4 | 1e-38 | 5/18 (A549, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +10.7 | 1e-24 | 7/12 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.90×** | +6.7 | 2e-09 | 3/20 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.9 | 1e-04 | 2/20 (LOX-IMVI, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.1 | 0.004 | 2/14 (A-172, NCI-H1792) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.014 | 0/21 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.27×** | +3.5 | 0.026 | 0/19 | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.045 | 2/19 (MIA PaCa-2, LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.062 | 2/15 (MIA PaCa-2, A-172) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7762.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.178×, HOP62 0.178×, Hs 766T 0.143×, A498 0.274×; ⚠ cell-cycle shift, explains ~47% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0302×, hTERT-HPNE 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (J82 0.132×); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.0661×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -4.4 | 0.006 | 12/20 (hTERT-HPNE, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.680×** | -3.9 | 0.025 | 7/20 (HOP62, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.783× | -3.2 | 0.24 | 6/21 (J82, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.735× | -3.1 | 0.24 | 1/20 (J82) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0302× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.132× (z -9.2) |
| [[A-172 (line)]] | wt | 3.76 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0661× (z -8.5) |
| [[A498 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA4]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS12]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ITGA11]] | +0.64 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[APCDD1L]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.63 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[WNT5B]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[EVC]] | +0.61 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[HHIP]] | +0.60 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[VEPH1]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SCUBE3]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP6]] | -0.55 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[KIF13B]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MUC1]] | -0.47 | -0.46 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA4]] | C | ITGA4 activity raises AK5's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.81× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[COL6A3]] | C | COL6A3 activity raises AK5's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.35× lower at baseline in the lines without COL6A3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises AK5's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 3.70× lower at baseline in the lines without CCDC190 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises AK5's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without PRRX1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises AK5's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without SPOCD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises AK5's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without INSYN2B | 0.026 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises AK5's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without WNT5A | 0.026 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises AK5's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without ITGA11 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises AK5's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without RGS4 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises AK5's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 2.94× lower at baseline in the lines without ADAM12 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises AK5's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without VEPH1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises AK5's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.71× lower at baseline in the lines without NAV1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 2, C 30. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBLN7]] | B | AK5 activity raises FBLN7's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without AK5 | 0.079 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent |
| [[BOC]] | B | AK5 activity raises BOC's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without AK5 | 0.097 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent |
| [[RGS4]] | C | AK5 activity raises RGS4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 3.20× lower at baseline in the lines without AK5 | 0.013 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[NAV1]] | C | AK5 activity raises NAV1's level | lines that do not express AK5 (25) vs lines expressing it (25) | 5.38× lower at baseline in the lines without AK5 | 0.018 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[ITGA11]] | C | AK5 activity raises ITGA11's level | lines that do not express AK5 (25) vs lines expressing it (25) | 5.11× lower at baseline in the lines without AK5 | 0.022 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[ITGA4]] | C | AK5 activity raises ITGA4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 6.09× lower at baseline in the lines without AK5 | 0.026 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[TNFAIP6]] | C | AK5 activity raises TNFAIP6's level | lines that do not express AK5 (25) vs lines expressing it (25) | 3.32× lower at baseline in the lines without AK5 | 0.029 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[COL6A3]] | C | AK5 activity raises COL6A3's level | lines that do not express AK5 (25) vs lines expressing it (25) | 5.66× lower at baseline in the lines without AK5 | 0.036 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[LAMA4]] | C | AK5 activity raises LAMA4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 4.19× lower at baseline in the lines without AK5 | 0.038 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[COL1A2]] | C | AK5 activity raises COL1A2's level | lines that do not express AK5 (25) vs lines expressing it (25) | 7.28× lower at baseline in the lines without AK5 | 0.038 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[SYNDIG1]] | C | AK5 activity raises SYNDIG1's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without AK5 | 0.039 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[HHIP]] | C | AK5 activity raises HHIP's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without AK5 | 0.042 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.2, 16.7); signed map (21.6, 46.9). **Vector** length 53.4, 13.7% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,282,019-77,559,966 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adenylate kinases |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6K8](https://www.uniprot.org/uniprotkb/Q9Y6K8) (Adenylate kinase isoenzyme 5):

> Nucleoside monophosphate (NMP) kinase that catalyzes the reversible transfer of the terminal phosphate group between nucleoside triphosphates and monophosphates. Active on AMP and dAMP with ATP as a donor. When GTP is used as phosphate donor, the enzyme phosphorylates AMP, CMP, and to a small extent dCMP. Also displays broad nucleoside diphosphate kinase activity.

**Summary**, from NCBI Gene [26289](https://www.ncbi.nlm.nih.gov/gene/26289):

> This gene encodes a member of the adenylate kinase family, which is involved in regulating the adenine nucleotide composition within a cell by catalyzing the reversible transfer of phosphate groups among adenine nucleotides. This member is related to the UMP/CMP kinase of several species. It is located in the cytosol and expressed exclusively in brain. Alternatively spliced transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:365) · Entrez [26289](https://www.ncbi.nlm.nih.gov/gene/26289) · UniProt [Q9Y6K8](https://www.uniprot.org/uniprotkb/Q9Y6K8) · Ensembl [ENSG00000154027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154027)

## Data

Gene col 7762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7762); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7762]; `tensor/DDL_lfc|DDL_z.npy` [7762]; `embed/gene_vectors.npy` [7762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7762 or target_col == 7762). Every well: [[AK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
