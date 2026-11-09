---
symbol: "MROH7"
type: "gene"
col: 11519
ensembl_id: "ENSG00000184313"
name: "maestro heat like repeat family member 7"
location: "1p32.3"
module: 55
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 71
direction_downstream: 19
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MROH7

*maestro heat like repeat family member 7* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.51× (z +8.3, q 9e-14, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +6.5, q 1e-08, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.324× (z -10.5, q 6e-23, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.70, fdr 7e-06), [[ACOT11]] (+0.68, fdr 7e-06, ⚠ same locus), [[C9orf152]] (+0.66, fdr 1e-05), [[LINC00299]] (+0.66, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 71 arrows point to it, the strongest [[GPR35]] → it (grade B ⚠); 19 go from it, the strongest it → [[TMC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.3 | 9e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +7.2 | 1e-10 | 1/11 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.5 | 1e-08 | 17/30 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.2 | 1e-07 | 2/16 (HOP62, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +5.7 | 2e-06 | 12/25 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.42× | +3.2 | 0.15 | 6/25 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.26× | +3.0 | 0.18 | 1/29 (A-427) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.38× | +3.0 | 0.18 | 3/24 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.324×** | -10.5 | 6e-23 | 23/30 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.326×** | -10.4 | 6e-23 | 23/31 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.525×** | -8.5 | 5e-15 | 19/24 (COLO 205, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.410×** | -8.3 | 2e-14 | 22/28 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.440×** | -7.3 | 3e-11 | 19/30 (SW480, COLO 205, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.480×** | -6.8 | 9e-10 | 19/30 (HT-29, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -6.7 | 2e-09 | 17/24 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.521×** | -6.0 | 1e-07 | 18/30 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -6.0 | 2e-07 | 18/30 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.540×** | -5.7 | 6e-07 | 20/21 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -5.3 | 6e-06 | 19/29 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.573×** | -5.2 | 1e-05 | 15/30 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -5.2 | 1e-05 | 18/26 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.351×** | -5.1 | 1e-05 | 14/22 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.415×** | -4.3 | 8e-04 | 12/21 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.004 | 7/30 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.011 | 12/29 (KATO III, HT-29, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.016 | 7/30 (SW480, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.704×** | -3.3 | 0.027 | 7/30 (AsPC-1, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.708×** | -3.2 | 0.030 | 11/30 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.708×** | -3.2 | 0.030 | 4/25 (A498, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 21.7 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0453× (z -20.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0462× (z -14.5) |
| [[SW480 (line)]] | alt | 10.5 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0481× (z -16.1) |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0200× (z -28.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0307× (z -9.4) |
| [[LoVo (line)]] | wt | 8.81 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -8.8) |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0672× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.103× (z -8.8) |
| [[KATO III (line)]] | alt | 5.22 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0620× (z -9.9) |
| [[LS 180 (line)]] | wt | 8.04 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0527× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 5.89 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0285× (z -12.5) |
| [[A-172 (line)]] | wt | 6.32 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0351× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 3.59 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0636× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.245× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.167× (z -8.8) |
| [[H4 (line)]] | wt | 7.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0441× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 1.22 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0486× (z -9.0) |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ACOT11]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 | ⚠ same locus (2.6 kb, same strand: neighbours can correlate without regulation) |
| [[C9orf152]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LINC00299]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[EDAR]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NPSR1-AS1]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ADGRG5]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[USH1C]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[VILL]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 70, C 1. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR35]] | B | GPR35 activity raises MROH7's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.89× lower at baseline in the lines without GPR35 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[ST14]] | B | ST14 activity raises MROH7's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without ST14 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TJP3]] | B | TJP3 activity raises MROH7's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without TJP3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CLDN3]] | B | CLDN3 activity raises MROH7's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises MROH7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.77× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMEM45B]] | B | TMEM45B activity raises MROH7's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.53× lower at baseline in the lines without TMEM45B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[LINC02331]] | B | LINC02331 activity raises MROH7's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without LINC02331 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[EPS8L3]] | B | EPS8L3 activity raises MROH7's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.24× lower at baseline in the lines without EPS8L3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[B3GNT3]] | B | B3GNT3 activity raises MROH7's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without B3GNT3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SLC52A3]] | B | SLC52A3 activity raises MROH7's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without SLC52A3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[BMP4]] | B | BMP4 activity raises MROH7's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without BMP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[TMEM125]] | B | TMEM125 activity raises MROH7's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without TMEM125 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC4]] | B | MROH7 activity raises TMC4's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 3.35× lower at baseline in the lines without MROH7 | 0.007 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[FAAH]] | B | MROH7 activity raises FAAH's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without MROH7 | 0.030 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[CLDN3]] | B | MROH7 activity raises CLDN3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.93× lower at baseline in the lines without MROH7 | 0.032 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[TJP3]] | B | MROH7 activity raises TJP3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.83× lower at baseline in the lines without MROH7 | 0.035 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[ST14]] | B | MROH7 activity raises ST14's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 4.24× lower at baseline in the lines without MROH7 | 0.039 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[BMP4]] | B | MROH7 activity raises BMP4's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without MROH7 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[GPR35]] | B | MROH7 activity raises GPR35's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without MROH7 | 0.049 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[C1QTNF3]] | B | MROH7 activity raises C1QTNF3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.25× lower at baseline in the lines without MROH7 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[ZNF860]] | B | MROH7 activity raises ZNF860's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.59× lower at baseline in the lines without MROH7 | 0.054 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[SORL1]] | B | MROH7 activity raises SORL1's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 2.42× lower at baseline in the lines without MROH7 | 0.057 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[TNNT2]] | B | MROH7 activity raises TNNT2's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without MROH7 | 0.074 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[TSPOAP1]] | B | MROH7 activity raises TSPOAP1's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without MROH7 | 0.078 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 48.1); signed map (61.4, 10.8). **Vector** length 65.4, 14.3% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -10.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | maestro heat like repeat family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,641,754-54,710,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46354; previously C1orf175, HEATR8 |
| Gene groups (HGNC) | Maestro heat like repeat containing |
| Matched by | ensembl_id |

UniProt [Q68CQ1](https://www.uniprot.org/uniprotkb/Q68CQ1) carries no function annotation.

**Summary**, from NCBI Gene [374977](https://www.ncbi.nlm.nih.gov/gene/374977):

> Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24802) · Entrez [374977](https://www.ncbi.nlm.nih.gov/gene/374977) · UniProt [Q68CQ1](https://www.uniprot.org/uniprotkb/Q68CQ1) · Ensembl [ENSG00000184313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184313)

## Data

Gene col 11519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11519); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11519]; `tensor/DDL_lfc|DDL_z.npy` [11519]; `embed/gene_vectors.npy` [11519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11519 or target_col == 11519). Every well: [[MROH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MROH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
