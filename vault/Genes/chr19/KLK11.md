---
symbol: "KLK11"
type: "gene"
col: 9533
ensembl_id: "ENSG00000167757"
name: "kallikrein related peptidase 11"
location: "19q13.41"
module: 73
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 10
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 51
direction_downstream: 75
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# KLK11

*kallikrein related peptidase 11* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.07× (z +10.7, q 4e-24, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 2.16× (z +3.9, q 0.005, up in 0 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.118×, CFPAC-1 0.107×, HT-29 0.182×, AsPC-1 0.326×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 0.128×, LS 180 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK10]] (+0.90, fdr 7e-06, ⚠ same locus), [[TFF2]] (+0.84, fdr 7e-06), [[HS3ST1]] (+0.74, fdr 9e-06), [[SERPINB5]] (+0.71, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 75 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.07×** | +10.7 | 4e-24 | 3/5 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.07×** | +9.7 | 1e-19 | 2/5 (HT-29, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.33×** | +8.6 | 2e-15 | 1/5 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.72×** | +5.1 | 4e-05 | 2/7 (Panc 03.27, AsPC-1) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.96×** | +4.9 | 1e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +4.7 | 2e-04 | 1/6 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +4.6 | 4e-04 | 0/8 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +4.5 | 6e-04 | 0/6 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.25×** | +4.2 | 0.002 | 1/6 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.16×** | +3.9 | 0.005 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.99×** | +3.9 | 0.005 | 2/6 (KATO III, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.18×** | +3.8 | 0.006 | 1/2 (AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.7 | 0.008 | 1/8 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.2 | 0.057 | 0/8 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.42×** | +3.1 | 0.063 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.063 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.118×, CFPAC-1 0.107×, HT-29 0.182×, AsPC-1 0.326×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 0.128×, LS 180 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.456× | -3.7 | 0.13 | 1/8 (SW1417) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.499× | -3.3 | 0.21 | 0/8 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.500× | -3.3 | 0.21 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 26.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -8.7) |
| [[A-172 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.172 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.357 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK10]] | +0.90 | +0.88 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 825; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[TFF2]] | +0.84 | +0.83 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.74 | +0.79 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[SERPINB5]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[CEACAM6]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TFF1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[DSG3]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.67 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[EPS8L1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DHRS9]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PADI1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 1, C 50. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises KLK11's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without SEMA3B | 0.084 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MUC17]] | C | MUC17 activity raises KLK11's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 8.93× lower at baseline in the lines without MUC17 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[REG4]] | C | REG4 activity raises KLK11's level | lines that do not express REG4 (43) vs lines expressing it (7) | 6.46× lower at baseline in the lines without REG4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[SLC6A20]] | C | SLC6A20 activity raises KLK11's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.23× lower at baseline in the lines without SLC6A20 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises KLK11's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without S100A14 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises KLK11's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.27× lower at baseline in the lines without TMPRSS4 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[MAOB]] | C | MAOB activity raises KLK11's level | lines that do not express MAOB (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without MAOB | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises KLK11's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.01× lower at baseline in the lines without NPSR1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises KLK11's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without PADI1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises KLK11's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without KLK10 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises KLK11's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.89× lower at baseline in the lines without HS3ST1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises KLK11's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without SERPINB5 | 0.019 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |

### Downstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 18, C 57. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | KLK11 activity raises EPS8L1's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 5.64× lower at baseline in the lines without KLK11 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[FAM83E]] | B | KLK11 activity raises FAM83E's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.49× lower at baseline in the lines without KLK11 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[MYRF]] | B | KLK11 activity raises MYRF's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.26× lower at baseline in the lines without KLK11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[RDH13]] | B | KLK11 activity raises RDH13's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 2.72× lower at baseline in the lines without KLK11 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[JUP]] | B | KLK11 activity raises JUP's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 6.06× lower at baseline in the lines without KLK11 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[GRHL3]] | B | KLK11 activity raises GRHL3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.39× lower at baseline in the lines without KLK11 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[SEMA3B]] | B | KLK11 activity raises SEMA3B's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.94× lower at baseline in the lines without KLK11 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[IL22RA1]] | B | KLK11 activity raises IL22RA1's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.27× lower at baseline in the lines without KLK11 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[KRTCAP3]] | B | KLK11 activity raises KRTCAP3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.14× lower at baseline in the lines without KLK11 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[TMC6]] | B | KLK11 activity raises TMC6's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.33× lower at baseline in the lines without KLK11 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[LYPD3]] | B | KLK11 activity raises LYPD3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 2.42× lower at baseline in the lines without KLK11 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[PRDM1]] | B | KLK11 activity raises PRDM1's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.48× lower at baseline in the lines without KLK11 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.1, 53.9); signed map (68.3, 9.5). **Vector** length 35.5, 15.3% of its response variance represented; |z| ≥ 3 in 199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | kallikrein related peptidase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,022,216-51,028,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TLSP; previously PRSS20 |
| Gene groups (HGNC) | Kallikreins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBX7](https://www.uniprot.org/uniprotkb/Q9UBX7) (Kallikrein-11):

> Possible multifunctional protease. Efficiently cleaves 'bz-Phe-Arg-4-methylcoumaryl-7-amide', a kallikrein substrate, and weakly cleaves other substrates for kallikrein and trypsin. Cleaves synthetic peptides after arginine but not lysine residues.

**Summary**, from NCBI Gene [11012](https://www.ncbi.nlm.nih.gov/gene/11012):

> Kallikreins are a subgroup of serine proteases having diverse physiological functions. Growing evidence suggests that many kallikreins are implicated in carcinogenesis and some have potential as novel cancer and other disease biomarkers. This gene is one of the fifteen kallikrein subfamily members located in a cluster on chromosome 19. Alternate splicing and the use of alternate promoters results in multiple transcript variants encoding distinct isoforms which are differentially expressed. …

**Accessions** — [HGNC:6359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6359) · Entrez [11012](https://www.ncbi.nlm.nih.gov/gene/11012) · UniProt [Q9UBX7](https://www.uniprot.org/uniprotkb/Q9UBX7) · Ensembl [ENSG00000167757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167757)

## Data

Gene col 9533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9533); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9533]; `tensor/DDL_lfc|DDL_z.npy` [9533]; `embed/gene_vectors.npy` [9533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9533 or target_col == 9533). Every well: [[KLK11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLK11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
