---
symbol: "ELMO3"
type: "gene"
col: 2283
ensembl_id: "ENSG00000102890"
name: "engulfment and cell motility 3"
location: "16q22.1"
module: 31
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 54
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ELMO3

*engulfment and cell motility 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.22× (z +7.1, q 7e-10, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.74× (z +3.7, q 0.026, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.413× (z -7.9, q 2e-12, down in 17 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB25]] (+0.70, fdr 1e-05), [[PROM2]] (+0.70, fdr 1e-05), [[ARHGEF16]] (+0.70, fdr 1e-05); moves opposite to [[MCPH1-AS1]] (-0.50, fdr 1e-04), [[CHROMR]] (-0.50, fdr 1e-04), [[C2orf74-DT]] (-0.46, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.1 | 7e-10 | 1/6 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.1 | 8e-05 | 3/8 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.6 | 8e-04 | 8/18 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 0.001 | 4/13 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.026 | 7/26 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.96× | +3.3 | 0.11 | 0/7 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.413×** | -7.9 | 2e-12 | 17/31 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -6.7 | 6e-09 | 21/25 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -6.0 | 4e-07 | 20/26 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -4.2 | 0.004 | 16/38 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.530× | -3.1 | 0.24 | 14/30 (KATO III, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.45 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0200× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -14.0) |
| [[LoVo (line)]] | wt | 5.60 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.2) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 7.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.4) |
| [[COLO 205 (line)]] | alt | 7.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -9.1) |
| [[HCT15 (line)]] | alt | 8.61 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -8.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HT-29 (line)]] | alt | 9.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0843× (z -15.8) |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -10.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H2347 (line)]] | alt | 5.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -14.6) |
| [[SW1417 (line)]] | alt | 9.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.0) |
| [[SW48 (line)]] | wt | 9.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.2) |
| [[A-172 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB25]] | +0.70 | +0.74 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PROM2]] | +0.70 | +0.69 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[ARHGEF16]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[IQANK1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MUC5B]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.62 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[P2RY2]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FAM83E]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[AMN]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PRSS8]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1-AS1]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CHROMR]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[C2orf74-DT]] | -0.46 | -0.51 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises ELMO3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without TMPRSS4 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[P2RY2]] | B | P2RY2 activity raises ELMO3's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without P2RY2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[CLDN3]] | B | CLDN3 activity raises ELMO3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without CLDN3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[RAB25]] | B | RAB25 activity raises ELMO3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without RAB25 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[PRSS8]] | B | PRSS8 activity raises ELMO3's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 2.65× lower at baseline in the lines without PRSS8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[ESRP1]] | B | ESRP1 activity raises ELMO3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without ESRP1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[CYP4F3]] | B | CYP4F3 activity raises ELMO3's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without CYP4F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[ITGB6]] | B | ITGB6 activity raises ELMO3's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.73× lower at baseline in the lines without ITGB6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[MAL2]] | B | MAL2 activity raises ELMO3's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[TMC4]] | B | TMC4 activity raises ELMO3's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.43× lower at baseline in the lines without TMC4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ST14]] | B | ST14 activity raises ELMO3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.87× lower at baseline in the lines without ST14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TMEM125]] | B | TMEM125 activity raises ELMO3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 54.2); signed map (59.3, 9.0). **Vector** length 55.8, 9.15% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.5 | -6.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | engulfment and cell motility 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,199,111-67,204,029 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13824, CED12, ELMO-3, CED-12 |
| Gene groups (HGNC) | Engulfment and cell motility proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BJ8](https://www.uniprot.org/uniprotkb/Q96BJ8) (Engulfment and cell motility protein 3):

> Involved in cytoskeletal rearrangements required for phagocytosis of apoptotic cells and cell motility. Acts in association with DOCK1 and CRK. Was initially proposed to be required in complex with DOCK1 to activate Rac Rho small GTPases. May enhance the guanine nucleotide exchange factor (GEF) activity of DOCK1 (By similarity).

**Summary**, from NCBI Gene [79767](https://www.ncbi.nlm.nih.gov/gene/79767):

> The protein encoded by this gene is similar to a C. elegans protein that functions in phagocytosis of apoptotic cells and in cell migration. Other members of this small family of engulfment and cell motility (ELMO) proteins have been shown to interact with the dedicator of cyto-kinesis 1 protein to promote phagocytosis and effect cell shape changes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17289) · Entrez [79767](https://www.ncbi.nlm.nih.gov/gene/79767) · UniProt [Q96BJ8](https://www.uniprot.org/uniprotkb/Q96BJ8) · Ensembl [ENSG00000102890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102890)

## Data

Gene col 2283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2283); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2283]; `tensor/DDL_lfc|DDL_z.npy` [2283]; `embed/gene_vectors.npy` [2283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2283 or target_col == 2283). Every well: [[ELMO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELMO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
