---
symbol: "ARHGEF16"
type: "gene"
col: 5119
ensembl_id: "ENSG00000130762"
name: "Rho guanine nucleotide exchange factor 16"
location: "1p36.32"
module: 31
arm: "+"
pooled_cpm: 5.63
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 82
direction_downstream: 16
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ARHGEF16

*Rho guanine nucleotide exchange factor 16* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.85× (z +5.4, q 4e-05, up in 8 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.524× (z -11.1, q 6e-26, down in 21 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMO3]] (+0.70, fdr 1e-05), [[MUC3A]] (+0.68, fdr 7e-06), [[LAMA5]] (+0.66, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[BSPRY]] → it (grade B ⚠); 16 go from it, the strongest it → [[SPIRE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +5.4 | 4e-05 | 8/28 (LS 180, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.5 | 0.002 | 4/11 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 9/28 (HepG2/C3A, SW480, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.7 | 0.027 | 2/12 (NCI-H2347, LoVo) | top dose only | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.088 | 4/28 (Hs 766T, SW480, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.16 | 7/29 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.28× | +3.1 | 0.16 | 2/22 (NCI-H2030, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.524×** | -11.1 | 6e-26 | 21/27 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.611×** | -8.5 | 8e-15 | 21/28 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.509×** | -8.2 | 4e-14 | 20/31 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.529×** | -7.7 | 2e-12 | 21/31 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -7.3 | 4e-11 | 18/31 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.1 | 8e-11 | 18/28 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -6.6 | 4e-09 | 16/32 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -5.5 | 3e-06 | 16/27 (Hs 766T, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -4.9 | 5e-05 | 17/29 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.710×** | -4.1 | 0.002 | 10/30 (LS 180, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -4.0 | 0.003 | 4/31 (SW1417, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.028 | 12/31 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.754×** | -3.4 | 0.028 | 12/31 (A549, BT-474, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -3.4 | 0.028 | 9/27 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.753×** | -3.3 | 0.036 | 11/28 (HT-29, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -3.1 | 0.057 | 9/31 (HT-29, Panc 03.27, …) | top dose only | position effect removed |
| [[Nevirapine (drug)]] 0.05 µM |  | **0.767×** | -3.0 | 0.091 | 7/30 (SHP-77, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.2) |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.0) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0688× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0933× (z -15.1) |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.1) |
| [[Hs 766T (line)]] | wt | 4.89 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0352× (z -11.3) |
| [[KATO III (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -13.6) |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.7) |
| [[SW480 (line)]] | alt | 11.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 2.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0704× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0613× (z -11.1) |
| [[A-172 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMO3]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[MUC3A]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[LAMA5]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 | same gene group |
| [[PIK3C2B]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GPR35]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SEMA4D]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TJP2]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 | same gene group |
| [[IL22RA1]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TC2N]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 65, C 17. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSPRY]] | B | BSPRY activity raises ARHGEF16's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.79× lower at baseline in the lines without BSPRY | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[ATP2C2]] | B | ATP2C2 activity raises ARHGEF16's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without ATP2C2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[RAB25]] | B | RAB25 activity raises ARHGEF16's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 3.96× lower at baseline in the lines without RAB25 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[CBLC]] | B | CBLC activity raises ARHGEF16's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.47× lower at baseline in the lines without CBLC | 5e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[ESRP1]] | B | ESRP1 activity raises ARHGEF16's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.65× lower at baseline in the lines without ESRP1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ARHGEF16's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without TMPRSS4 | 7e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TJP3]] | B | TJP3 activity raises ARHGEF16's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without TJP3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[ST14]] | B | ST14 activity raises ARHGEF16's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.62× lower at baseline in the lines without ST14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[MAL2]] | B | MAL2 activity raises ARHGEF16's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.66× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[MPZL2]] | B | MPZL2 activity raises ARHGEF16's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.55× lower at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[TMEM125]] | B | TMEM125 activity raises ARHGEF16's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.83× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises ARHGEF16's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.46× lower at baseline in the lines without PLEKHG6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 11, C 5. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPIRE2]] | B | ARHGEF16 activity raises SPIRE2's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without ARHGEF16 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[TMC6]] | B | ARHGEF16 activity raises TMC6's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.93× lower at baseline in the lines without ARHGEF16 | 0.044 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[KIAA1522]] | B | ARHGEF16 activity raises KIAA1522's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 2.84× lower at baseline in the lines without ARHGEF16 | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[CALML4]] | B | ARHGEF16 activity raises CALML4's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without ARHGEF16 | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[SYTL1]] | B | ARHGEF16 activity raises SYTL1's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without ARHGEF16 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[SLC37A4]] | B | ARHGEF16 activity raises SLC37A4's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without ARHGEF16 | 0.066 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[CCDC120]] | B | ARHGEF16 activity raises CCDC120's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without ARHGEF16 | 0.068 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[PRXL2B]] | B | ARHGEF16 activity raises PRXL2B's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without ARHGEF16 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[TJP3]] | B | ARHGEF16 activity raises TJP3's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.49× lower at baseline in the lines without ARHGEF16 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[PCDH1]] | B | ARHGEF16 activity raises PCDH1's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without ARHGEF16 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[CRYBG2]] | B | ARHGEF16 activity raises CRYBG2's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.08× lower at baseline in the lines without ARHGEF16 | 0.098 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[SLC29A2]] | C | ARHGEF16 activity raises SLC29A2's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.11× lower at baseline in the lines without ARHGEF16 | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.6, 53.4); signed map (59.9, 9.3). **Vector** length 57.5, 11.4% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,454,665-3,481,113 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBR, GEF16 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VV41](https://www.uniprot.org/uniprotkb/Q5VV41) (Rho guanine nucleotide exchange factor 16):

> Guanyl-nucleotide exchange factor of the RHOG GTPase stimulating the exchange of RHOG-associated GDP for GTP. May play a role in chemotactic cell migration by mediating the activation of RAC1 by EPHA2. May also activate CDC42 and mediate activation of CDC42 by the viral protein HPV16 E6.

**Summary**, from NCBI Gene [27237](https://www.ncbi.nlm.nih.gov/gene/27237):

> Although the specific function of this protein is not known yet, it is thought to be involved in protein-protein and protein-lipid interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15515) · Entrez [27237](https://www.ncbi.nlm.nih.gov/gene/27237) · UniProt [Q5VV41](https://www.uniprot.org/uniprotkb/Q5VV41) · Ensembl [ENSG00000130762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130762)

## Data

Gene col 5119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5119); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5119]; `tensor/DDL_lfc|DDL_z.npy` [5119]; `embed/gene_vectors.npy` [5119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5119 or target_col == 5119). Every well: [[ARHGEF16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
