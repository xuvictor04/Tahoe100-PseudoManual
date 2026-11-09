---
symbol: "PDLIM4"
type: "gene"
col: 5207
ensembl_id: "ENSG00000131435"
name: "PDZ and LIM domain 4"
location: "5q31.1"
module: 13
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 18
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PDLIM4

*PDZ and LIM domain 4* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.00× (z +11.3, q 1e-26, up in 0 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +3.5, q 0.033, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.601× (z -4.3, q 0.009, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBB2A]] (+0.59, fdr 2e-05), [[SLC9A3R2]] (+0.58, fdr 1e-05), [[RUNX3]] (+0.53, fdr 1e-04); moves opposite to [[RBBP4]] (-0.48, fdr 2e-04), [[POLR2B]] (-0.47, fdr 2e-04), [[RCN2]] (-0.46, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FMNL1]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZNF697]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +11.3 | 1e-26 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +8.6 | 2e-15 | 1/14 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +6.8 | 1e-09 | 3/14 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.24×** | +4.4 | 0.001 | 2/13 (PANC-1, CHP-212) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.6 | 0.032 | 1/13 (MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.5 | 0.033 | 2/14 (NCI-H1792, SW 900) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +3.5 | 0.033 | 3/14 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.033 | 6/14 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.052 | 1/14 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.052 | 7/14 (HOP62, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.46× | +3.1 | 0.10 | 9/14 (HOP62, PANC-1, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -4.3 | 0.009 | 12/14 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.0 | 0.013 | 5/14 (CFPAC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.624×** | -4.0 | 0.013 | 12/14 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -3.9 | 0.016 | 12/14 (NCI-H1792, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.441×** | -3.6 | 0.033 | 8/14 (HOP62, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **0.451×** | -3.5 | 0.041 | 3/14 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.646×** | -3.4 | 0.052 | 4/15 (SW480, NCI-H661, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.677× | -3.1 | 0.16 | 1/14 (HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 76.0 | 1 (1 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.72× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -19.3) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.144× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 52.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.5) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -11.4) |
| [[SW480 (line)]] | alt | 16.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.6) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.196× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.9) ⚠ cell-cycle shift, explains ~77% of this change |
| [[CHP-212 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic |
| [[H4 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0612× (z -11.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[PANC-1 (line)]] | alt | 2.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.98× (z +8.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.977 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB2A]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC9A3R2]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 | same gene group |
| [[RUNX3]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[STRA6]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TNIP2]] | +0.52 | +0.29 / +0.56 | both halves | 2e-04 |  |
| [[FMNL1-DT]] | +0.51 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TNS1]] | +0.51 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[HEYL]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[NAA30]] | +0.50 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[GLRX2]] | +0.50 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[TP53RK]] | +0.49 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[MAP1S]] | +0.49 | +0.36 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | -0.48 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[POLR2B]] | -0.47 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[RCN2]] | -0.46 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[PMS2]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[VSIG10]] | -0.44 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[PAXBP1]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ASAH1]] | -0.43 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[SNRPG]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[CA5BP1-1]] | -0.43 | -0.20 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[SEPHS1]] | -0.42 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[TM9SF3]] | -0.42 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[PLBD1]] | -0.42 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[LAMTOR5-AS1]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMNL1]] | B | FMNL1 activity raises PDLIM4's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without FMNL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3 |
| [[RFX8]] | C | RFX8 activity raises PDLIM4's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without RFX8 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises PDLIM4's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without NAV1 | 0.061 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[AGTR1]] | C | AGTR1 activity raises PDLIM4's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without AGTR1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF697]] | B | PDLIM4 activity raises ZNF697's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.49× lower at baseline in the lines without PDLIM4 | 0.027 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[PELO]] | B | PDLIM4 activity raises PELO's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without PDLIM4 | 0.052 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[NFKBIE]] | B | PDLIM4 activity raises NFKBIE's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without PDLIM4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[LIMD2]] | B | PDLIM4 activity raises LIMD2's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.71× lower at baseline in the lines without PDLIM4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[STRA6]] | C | PDLIM4 activity raises STRA6's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without PDLIM4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3; co-absent with the target |
| [[PWWP3B]] | C | PDLIM4 activity raises PWWP3B's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without PDLIM4 | 0.064 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.9, 1.2); signed map (-21.5, 25.5). **Vector** length 41.9, 12.2% of its response variance represented; |z| ≥ 3 in 314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.9 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -3.6 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -3.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,257,696-132,273,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIL |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P50479](https://www.uniprot.org/uniprotkb/P50479) (PDZ and LIM domain protein 4):

> [Isoform 1]: Suppresses SRC activation by recognizing and binding to active SRC and facilitating PTPN13-mediated dephosphorylation of SRC 'Tyr-419' leading to its inactivation. Inactivated SRC dissociates from this protein allowing the initiation of a new SRC inactivation cycle. Involved in reorganization of the actin cytoskeleton. In nonmuscle cells, binds to ACTN1 (alpha-actinin-1), increases the affinity of ACTN1 to F-actin (filamentous actin), and promotes formation of actin stress fibers. …

**Summary**, from NCBI Gene [8572](https://www.ncbi.nlm.nih.gov/gene/8572):

> Enables alpha-actinin binding activity; protein homodimerization activity; and protein phosphatase binding activity. Involved in actin cytoskeleton organization. Located in several cellular components, including lamellipodium; perinuclear region of cytoplasm; and stress fiber. Part of filamentous actin. Implicated in osteoporosis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16501) · Entrez [8572](https://www.ncbi.nlm.nih.gov/gene/8572) · UniProt [P50479](https://www.uniprot.org/uniprotkb/P50479) · Ensembl [ENSG00000131435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131435)

## Data

Gene col 5207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5207); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5207]; `tensor/DDL_lfc|DDL_z.npy` [5207]; `embed/gene_vectors.npy` [5207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5207 or target_col == 5207). Every well: [[PDLIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
