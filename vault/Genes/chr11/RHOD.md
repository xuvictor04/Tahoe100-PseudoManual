---
symbol: "RHOD"
type: "gene"
col: 10347
ensembl_id: "ENSG00000173156"
name: "ras homolog family member D"
location: "11q13.2"
module: 20
arm: "-"
pooled_cpm: 7.98
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RHOD

*ras homolog family member D* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.48× (z +9.2, q 2e-17, up in 19 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.64× (z +5.0, q 5e-05, up in 14 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Brivudine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0561×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8E]] (+0.50, fdr 2e-05), [[CAMK2N1]] (+0.50, fdr 4e-04), [[IL6R]] (+0.50, fdr 3e-05); moves opposite to [[XRCC6]] (-0.47, fdr 4e-05), [[NUP205]] (-0.47, fdr 4e-05), [[PAICS]] (-0.46, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[S100A2]] → it (grade B ⚠); 6 go from it, the strongest it → [[ACHE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +9.2 | 2e-17 | 19/23 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.3 | 2e-14 | 12/14 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +8.0 | 3e-13 | 21/25 (NCI-H2030, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.68×** | +7.4 | 2e-11 | 17/30 (HOP62, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +6.5 | 9e-09 | 13/17 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +5.0 | 5e-05 | 14/29 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.67×** | +5.0 | 6e-05 | 17/32 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.58×** | +4.6 | 3e-04 | 15/31 (BT-474, HCT15, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.022 | 13/32 (KATO III, SW480, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.045 | 7/32 (A549, LS 180, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.090 | 3/32 (A-427, HEC-1-A, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.093 | 6/32 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Brivudine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.519× | -3.5 | 0.28 | 14/31 (Hs 766T, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.557× | -3.1 | 0.53 | 9/30 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +10.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 1 | — | [[Brivudine (drug)]] 0.05 µM 0.0561× (z -10.9) |
| [[SW480 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8E]] | +0.50 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CAMK2N1]] | +0.50 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[IL6R]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ACHE]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CDKN1C]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ADIRF]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DNAJC21]] | +0.48 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[ITSN2]] | +0.48 | +0.51 / +0.35 | both halves | 1e-04 | STRING 568 |
| [[RILP]] | +0.48 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[S100A2]] | +0.48 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[MUC12]] | +0.47 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[RNF223]] | +0.46 | +0.46 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC6]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NUP205]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PAICS]] | -0.46 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RANBP1]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[RAD54B]] | -0.44 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[RBBP7]] | -0.44 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RNPS1]] | -0.44 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ILF2]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[HAUS6]] | -0.43 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[XRCC5]] | -0.43 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[STT3B]] | -0.43 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[TRIP13]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A2]] | B | S100A2 activity raises RHOD's level | lines that do not express S100A2 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without S100A2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT81, LINC00408, FGFBP1; maybe low, not absent |
| [[RNF223]] | B | RNF223 activity raises RHOD's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without RNF223 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[AP1M2]] | C | AP1M2 activity raises RHOD's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 3.38× lower at baseline in the lines without AP1M2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7; co-absent with the target |
| [[C19orf33]] | C | C19orf33 activity raises RHOD's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 3.21× lower at baseline in the lines without C19orf33 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG; co-absent with the target |
| [[VAMP8]] | C | VAMP8 activity raises RHOD's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 3.34× lower at baseline in the lines without VAMP8 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACHE]] | B | RHOD activity raises ACHE's level | lines that do not express RHOD (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without RHOD | 0.032 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1 |
| [[HNRNPA3]] | B | RHOD activity raises HNRNPA3's level | lines that do not express RHOD (15) vs lines expressing it (35) | 1.19× lower at baseline in the lines without RHOD | 0.068 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1 |
| [[NTN1]] | B | RHOD activity raises NTN1's level | lines that do not express RHOD (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without RHOD | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1 |
| [[VAMP8]] | C | RHOD activity raises VAMP8's level | lines that do not express RHOD (15) vs lines expressing it (35) | 3.09× lower at baseline in the lines without RHOD | 0.040 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1; co-absent with the target |
| [[C19orf33]] | C | RHOD activity raises C19orf33's level | lines that do not express RHOD (15) vs lines expressing it (35) | 4.60× lower at baseline in the lines without RHOD | 0.041 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1; co-absent with the target |
| [[AP1M2]] | C | RHOD activity raises AP1M2's level | lines that do not express RHOD (15) vs lines expressing it (35) | 4.15× lower at baseline in the lines without RHOD | 0.054 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-21.7, 38.5); signed map (47.6, -3.3). **Vector** length 54.0, 11.1% of its response variance represented; |z| ≥ 3 in 502 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.5 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,056,847-67,072,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RhoHP1, Rho; previously ARHD |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: RHOD GTPase cycle; RHO GTPases Activate Formins; RHO GTPase Effectors |
| Matched by | ensembl_id |

**Function**, from UniProt [O00212](https://www.uniprot.org/uniprotkb/O00212) (Rho-related GTP-binding protein RhoD):

> Involved in endosome dynamics. May coordinate membrane transport with the function of the cytoskeleton. Involved in the internalization and trafficking of activated tyrosine kinase receptors such as PDGFRB. Participates in the reorganization of actin cytoskeleton; the function seems to involve WHAMM and includes regulation of filopodia formation and actin filament bundling. Can modulate the effect of DAPK3 in reorganization of actin cytoskeleton and focal adhesion dissolution.

**Summary**, from NCBI Gene [29984](https://www.ncbi.nlm.nih.gov/gene/29984):

> Ras homolog, or Rho, proteins interact with protein kinases and may serve as targets for activated GTPase. They play a critical role in muscle differentiation. The protein encoded by this gene binds GTP and is a member of the small GTPase superfamily. It is involved in endosome dynamics and reorganization of the actin cytoskeleton, and it may coordinate membrane transport with the function of the cytoskeleton. Two transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:670) · Entrez [29984](https://www.ncbi.nlm.nih.gov/gene/29984) · UniProt [O00212](https://www.uniprot.org/uniprotkb/O00212) · Ensembl [ENSG00000173156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173156)

## Data

Gene col 10347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10347); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10347]; `tensor/DDL_lfc|DDL_z.npy` [10347]; `embed/gene_vectors.npy` [10347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10347 or target_col == 10347). Every well: [[RHOD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
