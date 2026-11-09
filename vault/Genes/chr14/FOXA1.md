---
symbol: "FOXA1"
type: "gene"
col: 4981
ensembl_id: "ENSG00000129514"
name: "forkhead box A1"
location: "14q21.1"
module: 68
arm: "+"
pooled_cpm: 6.21
n_lines_expressing: 28
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# FOXA1

*forkhead box A1* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.53× (z +13.0, q 6e-36, up in 15 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.400× (z -9.0, q 8e-17, down in 22 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC6]] (+0.74, fdr 7e-06, ⚠ same locus), [[RASGRP3]] (+0.57, fdr 1e-05), [[TFAP2A]] (+0.57, fdr 1e-05), [[HOXA10-AS]] (+0.56, fdr 3e-05); moves opposite to [[BCL7C]] (-0.55, fdr 6e-05), [[PIGF]] (-0.54, fdr 6e-05), [[ZDHHC9]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 11 go from it, the strongest it → [[PLEKHG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +13.0 | 6e-36 | 15/22 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +8.8 | 4e-16 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.6 | 7e-09 | 3/18 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.5 | 1e-08 | 11/22 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +5.3 | 1e-05 | 14/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +4.8 | 2e-04 | 3/11 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.2 | 0.002 | 6/18 (Panc 03.27, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.006 | 9/20 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.020 | 5/25 (LoVo, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.43×** | +3.5 | 0.025 | 7/22 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.088 | 6/25 (LoVo, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.097 | 4/25 (NCI-H1573, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -9.0 | 8e-17 | 22/25 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.421×** | -8.5 | 4e-15 | 20/26 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -7.3 | 4e-11 | 21/26 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.692×** | -3.6 | 0.040 | 10/26 (NCI-H2347, NCI-H1792, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.3 | 0.11 | 4/26 (C-33 A, AN3 CA, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.730× | -3.1 | 0.17 | 7/26 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.731× | -3.1 | 0.17 | 8/26 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0684× (z -19.5) |
| [[LS 180 (line)]] | wt | 14.5 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.144× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 10.8 | 3 | 2 | [[Harringtonine (drug)]] 5 µM 12.8× (z +13.2) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.152× (z -10.1) |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0998× (z -13.9) |
| [[LoVo (line)]] | wt | 11.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.201× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 8.64 | 0 | 3 | — | [[Aprepitant (drug)]] 0.5 µM 0.0728× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 8.04 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.25× (z +11.6) | — |
| [[KATO III (line)]] | alt | 8.24 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0232× (z -16.8) |
| [[SW48 (line)]] | wt | 14.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 11.6× (z +8.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 53.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0518× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 6.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 1.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 6.88 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.116× (z -8.5) |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -8.6) |
| [[A-172 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.878 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC6]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RASGRP3]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TFAP2A]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 | pathway: Gastrulation; STRING 716 |
| [[HOXA10-AS]] | +0.56 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[GATA3]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 | pathway: ESR-mediated signaling; STRING 997 |
| [[STAP2]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[GULP1]] | +0.53 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[MARVELD2]] | +0.53 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[REPIN1]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[MAP3K2-DT]] | +0.52 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[ZNF747]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[TFAP2A-AS1]] | +0.51 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[METTL18]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7C]] | -0.55 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[PIGF]] | -0.54 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ZDHHC9]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ATP1A1]] | -0.54 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ERGIC1]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ABLIM2]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ITGB1BP1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ENTPD2]] | -0.50 | -0.54 / -0.22 | both halves | 6e-04 |  |
| [[TBC1D2B]] | -0.50 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CDC42BPB]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[WDR5]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 | STRING 589 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FOXA1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RBPMS]] | B | RBPMS activity raises FOXA1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.66× lower at baseline in the lines without RBPMS | 0.089 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[DAPP1]] | C | DAPP1 activity raises FOXA1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.55× lower at baseline in the lines without DAPP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[MTUS1-DT]] | C | MTUS1-DT activity raises FOXA1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without MTUS1-DT | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3; co-absent with the target |
| [[TTC6]] | C | TTC6 activity raises FOXA1's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without TTC6 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent; co-absent with the target |
| [[SMIM31]] | C | SMIM31 activity raises FOXA1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 3.14× lower at baseline in the lines without SMIM31 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises FOXA1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.87× lower at baseline in the lines without ATP2C2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[CRB3]] | C | CRB3 activity raises FOXA1's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 2.96× lower at baseline in the lines without CRB3 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG3]] | B | FOXA1 activity raises PLEKHG3's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without FOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[RECQL]] | B | FOXA1 activity lowers RECQL's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.63× higher at baseline in the lines without FOXA1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[RASGRP3]] | B | FOXA1 activity raises RASGRP3's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without FOXA1 | 0.061 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[STX2]] | B | FOXA1 activity lowers STX2's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.55× higher at baseline in the lines without FOXA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| cells under [[Torkinib (drug)]] 5 µM | B | FOXA1 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express FOXA1 (22) vs lines expressing it (26) | the lines without FOXA1: 0.78× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| cells under [[Penfluridol (drug)]] 5 µM | B | FOXA1 activity raises the cells' numbers under Penfluridol 5 µM (protects the cells) | lines that do not express FOXA1 (22) vs lines expressing it (26) | the lines without FOXA1: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[ZNF827]] | B | FOXA1 activity lowers ZNF827's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.05× higher at baseline in the lines without FOXA1 | 0.083 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| cells under [[Vortioxetine (drug)]] 5 µM | B | FOXA1 activity raises the cells' numbers under Vortioxetine 5 µM (protects the cells) | lines that do not express FOXA1 (22) vs lines expressing it (26) | the lines without FOXA1: 0.84× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[TTC6]] | C | FOXA1 activity raises TTC6's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 4.20× lower at baseline in the lines without FOXA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL; co-absent with the target |
| [[MTUS1-DT]] | C | FOXA1 activity raises MTUS1-DT's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 2.76× lower at baseline in the lines without FOXA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL; co-absent with the target |
| [[DAPP1]] | C | FOXA1 activity raises DAPP1's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 2.99× lower at baseline in the lines without FOXA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL; co-absent with the target |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.7, 12.2); signed map (18.7, -10.7). **Vector** length 66.0, 15.3% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +1.6 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -9.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | -7.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:37,589,552-37,596,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNF3A |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 5 pathways, smallest: Formation of axial mesoderm; Gastrulation; Estrogen-dependent gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P55317](https://www.uniprot.org/uniprotkb/P55317) (Hepatocyte nuclear factor 3-alpha):

> Transcription factor that is involved in embryonic development, establishment of tissue-specific gene expression and regulation of gene expression in differentiated tissues. Is thought to act as a 'pioneer' factor opening the compacted chromatin for other proteins through interactions with nucleosomal core histones and thereby replacing linker histones at target enhancer and/or promoter sites. Binds DNA with the consensus sequence 5'-[AC]A[AT]T[AG]TT[GT][AG][CT]T[CT]-3' (By similarity). …

**Summary**, from NCBI Gene [3169](https://www.ncbi.nlm.nih.gov/gene/3169):

> This gene encodes a member of the forkhead class of DNA-binding proteins. These hepatocyte nuclear factors are transcriptional activators for liver-specific transcripts such as albumin and transthyretin, and they also interact with chromatin. Similar family members in mice have roles in the regulation of metabolism and in the differentiation of the pancreas and liver. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5021) · Entrez [3169](https://www.ncbi.nlm.nih.gov/gene/3169) · UniProt [P55317](https://www.uniprot.org/uniprotkb/P55317) · Ensembl [ENSG00000129514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129514)

## Data

Gene col 4981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4981); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4981]; `tensor/DDL_lfc|DDL_z.npy` [4981]; `embed/gene_vectors.npy` [4981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4981 or target_col == 4981). Every well: [[FOXA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
