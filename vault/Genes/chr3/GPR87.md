---
symbol: "GPR87"
type: "gene"
col: 6146
ensembl_id: "ENSG00000138271"
name: "G protein-coupled receptor 87"
location: "3q25.1"
module: 8
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 14
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 35
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GPR87

*G protein-coupled receptor 87* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.22× (z +11.8, q 4e-29, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +7.4, q 2e-11, up in 1 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clopidogrel (drug)]] 0.05 µM: 0.490× (z -4.4, q 0.005, down in 5 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (Panc 03.27 0.139×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACSTD2]] (+0.60, fdr 7e-06), [[ST6GALNAC5]] (+0.58, fdr 1e-05), [[ADGRF4]] (+0.58, fdr 1e-05); moves opposite to [[SYCP2L]] (-0.42, fdr 3e-04), [[KIZ]] (-0.41, fdr 1e-04), [[CCDC146]] (-0.40, fdr 5e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[DAPP1]] → it (grade C ⚠); 35 go from it, the strongest it → [[GRHL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.22×** | +11.8 | 4e-29 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.10×** | +8.7 | 8e-16 | 1/5 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +7.4 | 2e-11 | 1/7 (LS 180) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.15×** | +7.4 | 2e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +5.9 | 5e-07 | 1/5 (NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.60×** | +5.6 | 2e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +5.6 | 2e-06 | 0/5 | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +5.3 | 1e-05 | 2/6 (NCI-H1573, NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +5.1 | 2e-05 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.0 | 3e-05 | 0/11 | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +4.5 | 3e-04 | 1/10 (NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.81×** | +4.5 | 3e-04 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.66×** | +4.2 | 0.001 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.001 | 1/11 (NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.98×** | +3.6 | 0.011 | 1/6 (NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.78×** | +3.5 | 0.014 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.94×** | +3.4 | 0.018 | 1/6 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.14×** | +3.3 | 0.025 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.062 | 1/6 (CFPAC-1) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.63×** | +3.0 | 0.068 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6146.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (Panc 03.27 0.139×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.490×** | -4.4 | 0.005 | 5/11 (LS 180, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Lopinavir (drug)]] 0.5 µM |  | 0.521× | -3.5 | 0.13 | 0/11 | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.602× | -3.2 | 0.26 | 2/8 (NCI-H2347, Panc 03.27) | inconsistent across doses |  |
| [[ML264 (drug)]] 5 µM |  | 0.384× | -3.1 | 0.26 | 0/6 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -3.1 | 0.26 | 2/12 (NCI-H23, LS 180) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.714 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.732 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.614 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.226 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACSTD2]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ST6GALNAC5]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ADGRF4]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | STRING 414 |
| [[VGLL3]] | +0.52 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[SH3RF2]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[INPP4B]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PRSS51]] | +0.50 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[FAM83B]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[DAPP1]] | +0.49 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[BARX2]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[TTC9]] | +0.48 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SLC15A1]] | +0.47 | +0.60 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCP2L]] | -0.42 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[KIZ]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[CCDC146]] | -0.40 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[RBM44]] | -0.39 | -0.24 / -0.30 | both halves | 5e-04 |  |
| [[LINC01118]] | -0.39 | -0.26 / -0.24 | both halves | 4e-04 |  |
| [[EPIC1]] | -0.39 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[BNIP3L]] | -0.38 | -0.20 / -0.36 | both halves | 7e-04 |  |
| [[PPP1R32]] | -0.38 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[EFCAB3P1]] | -0.37 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[C9orf153]] | -0.37 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[TESK2]] | -0.37 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[SLC6A6]] | -0.37 | -0.20 / -0.34 | ⚠ not reproduced | 8e-04 |  |
| [[ECT2L]] | -0.37 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPP1]] | C | DAPP1 activity raises GPR87's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.46× lower at baseline in the lines without DAPP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises GPR87's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without MAL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises GPR87's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without FUT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises GPR87's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without ITGB6 | 0.012 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[ST14]] | C | ST14 activity raises GPR87's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without ST14 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises GPR87's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without MACC1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises GPR87's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without ADGRF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[KDF1]] | C | KDF1 activity raises GPR87's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without KDF1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises GPR87's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without CDH1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises GPR87's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.91× lower at baseline in the lines without FAM83B | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises GPR87's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.13× lower at baseline in the lines without GABRP | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[BARX2]] | C | BARX2 activity raises GPR87's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.10× lower at baseline in the lines without BARX2 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 10, C 25. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL3]] | B | GPR87 activity raises GRHL3's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without GPR87 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[OCLN]] | B | GPR87 activity raises OCLN's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 4.10× lower at baseline in the lines without GPR87 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[PCAT1]] | B | GPR87 activity raises PCAT1's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.34× lower at baseline in the lines without GPR87 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[GNRH1]] | B | GPR87 activity lowers GNRH1's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 1.39× higher at baseline in the lines without GPR87 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[LINC00857]] | B | GPR87 activity raises LINC00857's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without GPR87 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[KRT80]] | B | GPR87 activity raises KRT80's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.62× lower at baseline in the lines without GPR87 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[ARHGEF34P]] | B | GPR87 activity raises ARHGEF34P's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without GPR87 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[OCLN]] | B | GPR87 activity strengthens OCLN's drug response | lines that do not express GPR87 (18) vs lines expressing it (12) | the lines without GPR87 respond 0.49× as strongly (z diff +2.99); strongest at Dinaciclib 0.5 µM: 0.56x vs 0.24x (z diff +4.8) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1; target measured in part of the lines; artifact flags |
| [[FGD4]] | B | GPR87 activity raises FGD4's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without GPR87 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[ZDHHC13]] | B | GPR87 activity raises ZDHHC13's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 1.53× lower at baseline in the lines without GPR87 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[DAPP1]] | C | GPR87 activity raises DAPP1's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 5.35× lower at baseline in the lines without GPR87 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1; co-absent with the target |
| [[MYO5B]] | C | GPR87 activity raises MYO5B's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 5.10× lower at baseline in the lines without GPR87 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.411). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.3, 58.7); signed map (55.5, 6.5). **Vector** length 24.3, 7.10% of its response variance represented; |z| ≥ 3 in 174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.7 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.6 | +2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.6 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -0.6 | +0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.5 | -3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -0.4 | -0.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -0.4 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.4 | -1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 87 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:151,294,086-151,316,820 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPR95 |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Hallmark sets | GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY21](https://www.uniprot.org/uniprotkb/Q9BY21) (G protein-coupled receptor 87):

> Receptor for lysophosphatidic acid (LPA). Necessary for p53/TP53-dependent survival in response to DNA damage. Promotes the Hippo-YAP signaling pathway and thereby modulates glycolysis and oxidative stress production by the regulation of hexokinase-2/HK2.

**Summary**, from NCBI Gene [53836](https://www.ncbi.nlm.nih.gov/gene/53836):

> This gene encodes a G protein-coupled receptor and is located in a cluster of G protein-couple receptor genes on chromosome 3. The encoded protein has been shown to be overexpressed in lung squamous cell carcinoma (PMID:18057535) and regulated by p53 (PMID:19602589). [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:4538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4538) · Entrez [53836](https://www.ncbi.nlm.nih.gov/gene/53836) · UniProt [Q9BY21](https://www.uniprot.org/uniprotkb/Q9BY21) · Ensembl [ENSG00000138271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138271)

## Data

Gene col 6146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6146); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6146]; `tensor/DDL_lfc|DDL_z.npy` [6146]; `embed/gene_vectors.npy` [6146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6146 or target_col == 6146). Every well: [[GPR87 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR87.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
