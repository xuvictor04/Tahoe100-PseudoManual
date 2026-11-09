---
symbol: "CIB2"
type: "gene"
col: 5861
ensembl_id: "ENSG00000136425"
name: "calcium and integrin binding family member 2"
location: "15q25.1"
module: 100
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 35
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# CIB2

*calcium and integrin binding family member 2* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +9.7, q 1e-19, up in 13 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +6.5, q 1e-08, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -7.5, q 5e-11, down in 19 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC29A4]] (+0.70, fdr 1e-05), [[PDZD7]] (+0.68, fdr 1e-05), [[RGS10]] (+0.65, fdr 1e-05); moves opposite to [[SRCAP]] (-0.56, fdr 1e-04), [[EIF2B5]] (-0.54, fdr 4e-05), [[ZXDB]] (-0.54, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 2 go from it, the strongest it → [[SBK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +9.7 | 1e-19 | 13/16 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +7.9 | 6e-13 | 4/6 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.5 | 1e-08 | 15/23 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +6.3 | 5e-08 | 9/10 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.003 | 8/19 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.003 | 7/31 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.003 | 9/28 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.0 | 0.004 | 10/25 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.55×** | +3.6 | 0.019 | 8/20 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.039 | 7/24 (C-33 A, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -7.5 | 5e-11 | 19/25 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -5.9 | 1e-06 | 16/23 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -5.6 | 5e-06 | 17/31 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -4.6 | 7e-04 | 15/31 (HEC-1-A, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.654×** | -3.5 | 0.059 | 11/32 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.692× | -3.0 | 0.24 | 9/31 (A-172, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.95 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0590× (z -10.9) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -10.0) |
| [[A549 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.5) |
| [[HOP62 (line)]] | alt | 6.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 5.93 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0818× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.3) |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.3) |
| [[A498 (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC29A4]] | +0.70 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PDZD7]] | +0.68 | +0.50 / +0.61 | both halves | 1e-05 | STRING 777 |
| [[RGS10]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[NENF]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SBK1]] | +0.63 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[METRN]] | +0.63 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[NFATC2IP-AS1]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[TSPAN33]] | +0.63 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PCSK1N]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[MAPT]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D22A-DT]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[HDAC3]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRCAP]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[EIF2B5]] | -0.54 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZXDB]] | -0.54 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[SLC35A4]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[KICS2]] | -0.54 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[UTP20]] | -0.53 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[LIG4]] | -0.53 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.53 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[USP40]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises CIB2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without PDZD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SBK1]] | B | SBK1 activity raises CIB2's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without SBK1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[BARX1]] | B | BARX1 activity raises CIB2's level | lines that do not express BARX1 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without BARX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: INA, LIN28B, NEXMIF |
| [[ANKRD6]] | B | ANKRD6 activity raises CIB2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without ANKRD6 | 0.068 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[CECR2]] | B | CECR2 activity raises CIB2's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CECR2 | 0.077 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[CYS1]] | B | CYS1 activity raises CIB2's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without CYS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[CACNG7]] | B | CACNG7 activity raises CIB2's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without CACNG7 | 0.097 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SBK1]] | B | CIB2 activity raises SBK1's level | lines that do not express CIB2 (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without CIB2 | 0.067 | ⚠ within organs, on part of the lines; also absent: HID1, ENSG00000266869, FAM169A; maybe low, not absent |
| [[CERK]] | B | CIB2 activity lowers CERK's level | lines that do not express CIB2 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without CIB2 | 0.070 | ⚠ within organs, on part of the lines; also absent: HID1, ENSG00000266869, FAM169A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.3, -2.0); signed map (-28.9, 22.2). **Vector** length 36.1, 5.34% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +0.8 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -7.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium and integrin binding family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,104,606-78,131,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIP2; previously DFNB48, USH1J |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [O75838](https://www.uniprot.org/uniprotkb/O75838) (Calcium and integrin-binding family member 2):

> Calcium- and integrin-binding protein that plays a role in intracellular calcium homeostasis (By similarity). Acts as an auxiliary subunit of the sensory mechanoelectrical transduction (MET) channel in hair cells (By similarity). Essential for mechanoelectrical transduction (MET) currents in auditory hair cells and thereby required for hearing (By similarity). Regulates the function of hair cell mechanotransduction by controlling the distribution of transmembrane channel-like proteins TMC1 and …

**Summary**, from NCBI Gene [10518](https://www.ncbi.nlm.nih.gov/gene/10518):

> The protein encoded by this gene is similar to that of KIP/CIB, calcineurin B, and calmodulin. The encoded protein is a calcium-binding regulatory protein that interacts with DNA-dependent protein kinase catalytic subunits (DNA-PKcs), and it is involved in photoreceptor cell maintenance. Mutations in this gene cause deafness, autosomal recessive, 48 (DFNB48), and also Usher syndrome 1J (USH1J). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:24579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24579) · Entrez [10518](https://www.ncbi.nlm.nih.gov/gene/10518) · UniProt [O75838](https://www.uniprot.org/uniprotkb/O75838) · Ensembl [ENSG00000136425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136425)

## Data

Gene col 5861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5861); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5861]; `tensor/DDL_lfc|DDL_z.npy` [5861]; `embed/gene_vectors.npy` [5861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5861 or target_col == 5861). Every well: [[CIB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
