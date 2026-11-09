---
symbol: "IL2RG"
type: "gene"
col: 7159
ensembl_id: "ENSG00000147168"
name: "interleukin 2 receptor subunit gamma"
location: "Xq13.1"
module: 73
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 25
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 27
direction_downstream: 38
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# IL2RG

*interleukin 2 receptor subunit gamma* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.72× (z +10.2, q 2e-21, up in 10 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.457× (z -5.7, q 5e-06, down in 15 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICAM2]] (+0.70, fdr 1e-05), [[SLC22A3]] (+0.66, fdr 1e-05), [[CFAP46]] (+0.61, fdr 2e-05); moves opposite to [[GLB1]] (-0.52, fdr 4e-05), [[PDS5A]] (-0.51, fdr 6e-05), [[LAPTM4B]] (-0.50, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 38 go from it, the strongest it → [[PLCD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +10.2 | 2e-21 | 10/18 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +9.6 | 2e-19 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +7.4 | 2e-11 | 2/12 (Panc 03.27, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +5.9 | 4e-07 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.18×** | +5.6 | 3e-06 | 3/10 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.86×** | +5.4 | 7e-06 | 2/8 (CFPAC-1, SW1417) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.03×** | +5.1 | 3e-05 | 7/18 (SW1417, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.0 | 3e-05 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.78×** | +4.0 | 0.005 | 10/20 (Panc 03.27, AsPC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +3.9 | 0.005 | 7/22 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +3.7 | 0.012 | 0/15 | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +3.7 | 0.012 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +3.4 | 0.027 | 2/13 (KATO III, CFPAC-1) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +3.2 | 0.053 | 2/6 (Panc 03.27, CFPAC-1) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.066 | 11/20 (Panc 03.27, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.083 | 4/17 (Panc 03.27, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.457×** | -5.7 | 5e-06 | 15/21 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.458×** | -5.6 | 5e-06 | 18/20 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.505×** | -4.9 | 1e-04 | 17/20 (LoVo, AsPC-1, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.367×** | -3.8 | 0.022 | 9/20 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.609×** | -3.6 | 0.038 | 15/20 (LoVo, AsPC-1, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -3.5 | 0.041 | 8/21 (NCI-H1792, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.651× | -3.1 | 0.15 | 12/20 (LS 180, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0229× (z -20.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0691× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 48.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.164× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 5.57 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0486× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0756× (z -9.9) |
| [[Hs 766T (line)]] | wt | 14.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 17.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 7.08 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0774× (z -10.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.104× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0884× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0546× (z -10.0) |
| [[A-172 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.959 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICAM2]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 | same gene group |
| [[SLC22A3]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CFAP46]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[LAMB3]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[COL17A1]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[INPP1]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SFR1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TFF2]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[KLF5]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[KLK10]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[UNC13D]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1]] | -0.52 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[PDS5A]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[LAPTM4B]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[KPNB1]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[KPNA3]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ARMH3]] | -0.47 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[POMT2]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[OGFOD3]] | -0.47 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[UBE2K]] | -0.47 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[HACD3]] | -0.46 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[PTK2]] | -0.46 | -0.37 / -0.34 | both halves | 1e-04 | pathway: MAPK family signaling cascades |
| [[NCK2]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 5, C 22. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises IL2RG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[XYLT1]] | B | XYLT1 activity raises IL2RG's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.30× lower at baseline in the lines without XYLT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[KLF5]] | B | KLF5 activity raises IL2RG's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without KLF5 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[LAMA3]] | B | LAMA3 activity raises IL2RG's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without LAMA3 | 0.062 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[EHF]] | B | EHF activity raises IL2RG's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without EHF | 0.094 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[PRSS3]] | C | PRSS3 activity raises IL2RG's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without PRSS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises IL2RG's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.81× lower at baseline in the lines without KLK10 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[SLC22A3]] | C | SLC22A3 activity raises IL2RG's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.78× lower at baseline in the lines without SLC22A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA; co-absent with the target |
| [[LINC02725]] | C | LINC02725 activity raises IL2RG's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 2.21× lower at baseline in the lines without LINC02725 | 0.012 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises IL2RG's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without TFF2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[LAMB3]] | C | LAMB3 activity raises IL2RG's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without LAMB3 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3; co-absent with the target |
| [[IL1A]] | C | IL1A activity raises IL2RG's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without IL1A | 0.022 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 22, C 16. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCD3]] | B | IL2RG activity raises PLCD3's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without IL2RG | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[NGEF]] | B | IL2RG activity raises NGEF's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.37× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[LPAR5]] | B | IL2RG activity raises LPAR5's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[KLF5]] | B | IL2RG activity raises KLF5's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.85× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[UNC13D]] | B | IL2RG activity raises UNC13D's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without IL2RG | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[ALS2CL]] | B | IL2RG activity raises ALS2CL's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without IL2RG | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[LAMA3]] | B | IL2RG activity raises LAMA3's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.85× lower at baseline in the lines without IL2RG | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[EFNB1]] | B | IL2RG activity raises EFNB1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without IL2RG | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[MTMR10]] | B | IL2RG activity raises MTMR10's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.19× lower at baseline in the lines without IL2RG | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[TNFRSF14-AS1]] | B | IL2RG activity raises TNFRSF14-AS1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without IL2RG | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[UNC13D]] | B | IL2RG activity strengthens UNC13D's drug response | lines that do not express IL2RG (15) vs lines expressing it (18) | the lines without IL2RG respond 0.43× as strongly (z diff +1.82); strongest at Belinostat 5 µM: 0.91x vs 0.29x (z diff +5.8) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850; target measured in part of the lines; artifact flags |
| [[NR1D1]] | B | IL2RG activity raises NR1D1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without IL2RG | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.2, 48.5); signed map (4.6, 35.2). **Vector** length 51.2, 12.5% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.8 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | -1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 2 receptor subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,107,404-71,112,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD132; previously SCIDX1, IMD4, CIDX |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Interleukin receptors |
| Hallmark sets | APICAL_SURFACE, IL6_JAK_STAT3_SIGNALING, PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION, KRAS_SIGNALING_UP |
| Reactome | 17 pathways, smallest: Interleukin-9 signaling; Interleukin-21 signaling; Interleukin-2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P31785](https://www.uniprot.org/uniprotkb/P31785) (Cytokine receptor common subunit gamma):

> Common subunit for the receptors for a variety of interleukins. Probably in association with IL15RA, involved in the stimulation of neutrophil phagocytosis by IL15.

**Summary**, from NCBI Gene [3561](https://www.ncbi.nlm.nih.gov/gene/3561):

> The protein encoded by this gene is an important signaling component of many interleukin receptors, including those of interleukin -2, -4, -7 and -21, and is thus referred to as the common gamma chain. Mutations in this gene cause X-linked severe combined immunodeficiency (XSCID), as well as X-linked combined immunodeficiency (XCID), a less severe immunodeficiency disorder. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:6010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6010) · Entrez [3561](https://www.ncbi.nlm.nih.gov/gene/3561) · UniProt [P31785](https://www.uniprot.org/uniprotkb/P31785) · Ensembl [ENSG00000147168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147168)

## Data

Gene col 7159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7159); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7159]; `tensor/DDL_lfc|DDL_z.npy` [7159]; `embed/gene_vectors.npy` [7159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7159 or target_col == 7159). Every well: [[IL2RG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL2RG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
