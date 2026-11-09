---
symbol: "EPS8L1"
type: "gene"
col: 5161
ensembl_id: "ENSG00000131037"
name: "EPS8 signaling adaptor L1"
location: "19q13.42"
module: 31
arm: "+"
pooled_cpm: 14.49
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 124
direction_downstream: 73
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EPS8L1

*EPS8 signaling adaptor L1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +7.2, q 3e-10, up in 15 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.454× (z -9.8, q 9e-20, down in 22 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDCBP2]] (+0.78, fdr 7e-06), [[TMPRSS4]] (+0.75, fdr 7e-06), [[EPS8L3]] (+0.74, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 124 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); 73 go from it, the strongest it → [[MYH14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.2 | 3e-10 | 15/32 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.5 | 9e-06 | 4/15 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 0.002 | 8/22 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +4.3 | 0.003 | 5/27 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.038 | 6/33 (NCI-H2030, CFPAC-1, …) | two highest doses | low cells (technical?); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.038 | 3/33 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.61× | +3.1 | 0.16 | 2/20 (NCI-H1573, LS 180) | top dose only | noisy plate (z scaled) |
| [[Simotinib (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.16 | 8/33 (KATO III, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -9.8 | 9e-20 | 22/33 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.559×** | -7.2 | 2e-10 | 20/33 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.564×** | -7.1 | 3e-10 | 21/31 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.606×** | -6.2 | 8e-08 | 18/33 (KATO III, HT-29, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.611×** | -6.1 | 1e-07 | 21/33 (KATO III, HT-29, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -6.1 | 1e-07 | 16/32 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -5.7 | 8e-07 | 15/33 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.428×** | -5.5 | 3e-06 | 18/34 (KATO III, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.9 | 5e-05 | 19/30 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.755×** | -4.9 | 5e-05 | 18/29 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.700×** | -4.4 | 5e-04 | 14/33 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.2 | 0.001 | 15/33 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.712×** | -4.2 | 0.001 | 9/33 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.794×** | -4.0 | 0.002 | 9/34 (LoVo, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -3.4 | 0.023 | 11/33 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.619×** | -3.1 | 0.061 | 7/32 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 10 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.104× (z -12.0) |
| [[SW48 (line)]] | wt | 54.2 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0712× (z -11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0715× (z -11.8) |
| [[HT-29 (line)]] | alt | 181 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0550× (z -21.0) |
| [[KATO III (line)]] | alt | 52.1 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -16.0) |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0664× (z -11.7) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.8) |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.254× (z -9.7) |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -8.9) |
| [[A-172 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.74 | +0.76 / +0.65 | both halves | 7e-06 | same gene group |
| [[INAVA]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[DSG3]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[C1orf116]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CYP3A5]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RDH13]] | +0.71 | +0.78 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.7 kb: neighbours can correlate without regulation) |
| [[CRYBG2]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 | same gene group |
| [[GCNT3]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.70 | +0.68 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*124 arrows, 124 of them with an alert ⚠; grade A 0, B 119, C 5. Shown: the 12 strongest; 112 more arrows (112 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises EPS8L1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.63× lower at baseline in the lines without TMPRSS4 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[LAD1]] | B | LAD1 activity raises EPS8L1's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 5.01× lower at baseline in the lines without LAD1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ST14]] | B | ST14 activity raises EPS8L1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 5.47× lower at baseline in the lines without ST14 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[CDH1]] | B | CDH1 activity raises EPS8L1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.07× lower at baseline in the lines without CDH1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CLDN7]] | B | CLDN7 activity raises EPS8L1's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.92× lower at baseline in the lines without CLDN7 | 6e-05 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises EPS8L1's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.97× lower at baseline in the lines without INAVA, MROH3P | 8e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[C1orf116]] | B | C1orf116 activity raises EPS8L1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.85× lower at baseline in the lines without C1orf116 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TMEM30B]] | B | TMEM30B activity raises EPS8L1's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 5.34× lower at baseline in the lines without TMEM30B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[FAM83B]] | B | FAM83B activity raises EPS8L1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.21× lower at baseline in the lines without FAM83B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[MPZL2]] | B | MPZL2 activity raises EPS8L1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.28× lower at baseline in the lines without MPZL2 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[SULT2B1]] | B | SULT2B1 activity raises EPS8L1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 4.36× lower at baseline in the lines without SULT2B1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises EPS8L1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.73× lower at baseline in the lines without TMPRSS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |

### Downstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 70, C 3. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYH14]] | B | EPS8L1 activity raises MYH14's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without EPS8L1 | 0.005 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SH2D3A]] | B | EPS8L1 activity raises SH2D3A's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.53× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TMC4]] | B | EPS8L1 activity raises TMC4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MYO5B]] | B | EPS8L1 activity raises MYO5B's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 5.16× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CEP170P1]] | B | EPS8L1 activity lowers CEP170P1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.37× higher at baseline in the lines without EPS8L1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SPINT1]] | B | EPS8L1 activity raises SPINT1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 4.18× lower at baseline in the lines without EPS8L1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[INAVA]] | B | EPS8L1 activity raises INAVA's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without EPS8L1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CDH1]] | B | EPS8L1 activity raises CDH1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 5.17× lower at baseline in the lines without EPS8L1 | 0.010 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[HSH2D]] | B | EPS8L1 activity raises HSH2D's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without EPS8L1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MISP]] | B | EPS8L1 activity raises MISP's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.23× lower at baseline in the lines without EPS8L1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[ELMO3]] | B | EPS8L1 activity raises ELMO3's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without EPS8L1 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MROH3P]] | B | EPS8L1 activity raises MROH3P's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.91× lower at baseline in the lines without EPS8L1 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.826). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 55.5); signed map (57.3, 8.4). **Vector** length 81.7, 20.4% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | EPS8 signaling adaptor L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,072,020-55,087,923 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20258, DRC3, MGC23164, MGC4642 |
| Gene groups (HGNC) | EPS8 signaling adaptor family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE68](https://www.uniprot.org/uniprotkb/Q8TE68) (Epidermal growth factor receptor kinase substrate 8-like protein 1):

> Stimulates guanine exchange activity of SOS1. May play a role in membrane ruffling and remodeling of the actin cytoskeleton.

**Summary**, from NCBI Gene [54869](https://www.ncbi.nlm.nih.gov/gene/54869):

> This gene encodes a protein that is related to epidermal growth factor receptor pathway substrate 8 (EPS8), a substrate for the epidermal growth factor receptor. The function of this protein is unknown. At least two alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21295) · Entrez [54869](https://www.ncbi.nlm.nih.gov/gene/54869) · UniProt [Q8TE68](https://www.uniprot.org/uniprotkb/Q8TE68) · Ensembl [ENSG00000131037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131037)

## Data

Gene col 5161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5161); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5161]; `tensor/DDL_lfc|DDL_z.npy` [5161]; `embed/gene_vectors.npy` [5161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5161 or target_col == 5161). Every well: [[EPS8L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS8L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
