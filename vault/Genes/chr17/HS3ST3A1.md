---
symbol: "HS3ST3A1"
type: "gene"
col: 7757
ensembl_id: "ENSG00000153976"
name: "heparan sulfate-glucosamine 3-sulfotransferase 3A1"
location: "17p12"
module: 13
arm: "+"
pooled_cpm: 31.87
n_lines_expressing: 17
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 30
direction_downstream: 44
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# HS3ST3A1

*heparan sulfate-glucosamine 3-sulfotransferase 3A1* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +10.9, q 5e-25, up in 1 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.6, q 2e-06, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.679× (z -6.6, q 3e-08, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSHZ3]] (+0.70, fdr 7e-06), [[INSYN2B]] (+0.69, fdr 7e-06), [[ARHGAP22]] (+0.66, fdr 7e-06); moves opposite to [[DMTN]] (-0.48, fdr 1e-04), [[PATJ]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[AP1G2]] → it (grade B ⚠); 44 go from it, the strongest it → [[RASA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +10.9 | 5e-25 | 1/12 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.4 | 4e-08 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.7 | 2e-06 | 3/13 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.6 | 2e-06 | 1/15 (NCI-H460) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.036 | 5/14 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.047 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.059 | 7/13 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.083 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 3/15 (SW480, A-427, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.12 | 2/15 (A-172, SW 1271) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.12 | 1/13 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -6.6 | 3e-08 | 12/15 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.663×** | -5.1 | 8e-05 | 10/15 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.664×** | -4.5 | 0.001 | 5/14 (C32, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.029 | 0/15 | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.736×** | -3.7 | 0.029 | 10/15 (SNU-423, C32, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.797× | -3.2 | 0.12 | 8/15 (C32, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | 0.583× | -3.2 | 0.12 | 2/15 (C32, SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 99.3 | 0 | 17 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 55.1 | 2 (1 ⚠) | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.9) |
| [[A-172 (line)]] | wt | 372 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 178 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 199 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.8) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -10.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.9) |
| [[SNU-423 (line)]] | alt | 84.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.6) |
| [[SW480 (line)]] | alt | 9.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.7) |
| [[A498 (line)]] | wt | 6.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ARHGAP22]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[RFX8]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[GDNF]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PRRX1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CDH13]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[NALF1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[SAMD3]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[STK32B]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMTN]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[PATJ]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 1, C 29. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP1G2]] | B | AP1G2 activity lowers HS3ST3A1's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 5.17× higher at baseline in the lines without AP1G2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[WNT5A]] | C | WNT5A activity raises HS3ST3A1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 6.47× lower at baseline in the lines without WNT5A | 0.002 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[THBS2]] | C | THBS2 activity raises HS3ST3A1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 8.38× lower at baseline in the lines without THBS2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises HS3ST3A1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 8.83× lower at baseline in the lines without CDH13 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises HS3ST3A1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 5.27× lower at baseline in the lines without GDNF-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[CAMK4]] | C | CAMK4 activity raises HS3ST3A1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 5.72× lower at baseline in the lines without CAMK4 | 0.015 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises HS3ST3A1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.90× lower at baseline in the lines without VEPH1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[NTM]] | C | NTM activity raises HS3ST3A1's level | lines that do not express NTM (33) vs lines expressing it (17) | 6.63× lower at baseline in the lines without NTM | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises HS3ST3A1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 6.51× lower at baseline in the lines without ADAM12 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises HS3ST3A1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 6.60× lower at baseline in the lines without GYPC | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[MME]] | C | MME activity raises HS3ST3A1's level | lines that do not express MME (30) vs lines expressing it (20) | 6.01× lower at baseline in the lines without MME | 0.037 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises HS3ST3A1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 7.00× lower at baseline in the lines without INSYN2B | 0.040 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 15, C 29. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | HS3ST3A1 activity raises RASA3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without HS3ST3A1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[ITPRIP]] | B | HS3ST3A1 activity raises ITPRIP's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without HS3ST3A1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[PARVG]] | B | HS3ST3A1 activity raises PARVG's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without HS3ST3A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[RASSF8]] | B | HS3ST3A1 activity raises RASSF8's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without HS3ST3A1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[TUBB6]] | B | HS3ST3A1 activity raises TUBB6's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without HS3ST3A1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[REP15]] | B | HS3ST3A1 activity raises REP15's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 1.57× lower at baseline in the lines without HS3ST3A1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[WIPF1]] | B | HS3ST3A1 activity raises WIPF1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 4.61× lower at baseline in the lines without HS3ST3A1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[PARVB]] | B | HS3ST3A1 activity raises PARVB's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without HS3ST3A1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[ABL1]] | B | HS3ST3A1 activity raises ABL1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 1.45× lower at baseline in the lines without HS3ST3A1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[SH2B3]] | B | HS3ST3A1 activity raises SH2B3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without HS3ST3A1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[KIAA1549L]] | B | HS3ST3A1 activity raises KIAA1549L's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without HS3ST3A1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[EVC]] | B | HS3ST3A1 activity raises EVC's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without HS3ST3A1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.7, 14.8); signed map (20.7, 47.5). **Vector** length 71.2, 26.9% of its response variance represented; |z| ≥ 3 in 489 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate-glucosamine 3-sulfotransferase 3A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:13,494,032-13,601,929 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 3OST3A1, 30ST3A1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y663](https://www.uniprot.org/uniprotkb/Q9Y663) (Heparan sulfate glucosamine 3-O-sulfotransferase 3A1):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the transfer of a sulfo group to an N-unsubstituted glucosamine linked to a 2-O-sulfo iduronic acid unit on heparan sulfate. Catalyzes the O-sulfation of glucosamine in IdoUA2S-GlcNS and also in IdoUA2S-GlcNH2. The substrate-specific O-sulfation generates an enzyme-modified heparan sulfate which acts as a binding receptor to Herpes simplex virus-1 (HSV-1) and permits its entry. Unlike HS3ST1/3-OST-1, does not …

**Summary**, from NCBI Gene [9955](https://www.ncbi.nlm.nih.gov/gene/9955):

> Heparan sulfate biosynthetic enzymes are key components in generating a myriad of distinct heparan sulfate fine structures that carry out multiple biologic activities. The enzyme encoded by this gene is a member of the heparan sulfate biosynthetic enzyme family. It is a type II integral membrane protein and possesses heparan sulfate glucosaminyl 3-O-sulfotransferase activity. The sulfotransferase domain of this enzyme is highly similar to the same domain of heparan sulfate D-glucosaminyl …

**Accessions** — [HGNC:5196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5196) · Entrez [9955](https://www.ncbi.nlm.nih.gov/gene/9955) · UniProt [Q9Y663](https://www.uniprot.org/uniprotkb/Q9Y663) · Ensembl [ENSG00000153976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153976)

## Data

Gene col 7757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7757); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7757]; `tensor/DDL_lfc|DDL_z.npy` [7757]; `embed/gene_vectors.npy` [7757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7757 or target_col == 7757). Every well: [[HS3ST3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS3ST3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
