---
symbol: "PDCL3"
type: "gene"
col: 3691
ensembl_id: "ENSG00000115539"
name: "phosducin like 3"
location: "2q11.2"
module: 20
arm: "+"
pooled_cpm: 9.13
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PDCL3

*phosducin like 3* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.54× (z +19.5, q 0e+00, up in 32 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.69× (z +5.7, q 9e-07, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.576× (z -8.9, q 3e-16, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL9]] (+0.64, fdr 9e-06), [[SEPHS1]] (+0.62, fdr 1e-05), [[FECH]] (+0.61, fdr 2e-05); moves opposite to [[PPP1R13L]] (-0.61, fdr 2e-05), [[MIDN]] (-0.55, fdr 3e-05), [[INAFM1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.54×** | +19.5 | 0e+00 | 32/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.48×** | +18.7 | 0e+00 | 18/19 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +13.2 | 2e-37 | 24/24 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +8.0 | 3e-13 | 21/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.1 | 1e-07 | 22/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.69×** | +5.7 | 9e-07 | 24/46 (PANC-1, LoVo, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.3 | 8e-06 | 20/37 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.1 | 3e-05 | 19/39 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 14/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 12/45 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.89×** | +3.8 | 0.008 | 9/41 (PANC-1, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.017 | 11/46 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.046 | 6/47 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.2 | 0.062 | 6/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.066 | 4/42 (RPMI-7951, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.576×** | -8.9 | 3e-16 | 34/46 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.553×** | -6.8 | 4e-09 | 27/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.567×** | -6.5 | 2e-08 | 28/47 (J82, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.627×** | -5.3 | 1e-05 | 23/44 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -4.8 | 2e-04 | 20/47 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -4.8 | 2e-04 | 19/44 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.664×** | -4.7 | 2e-04 | 21/47 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.527×** | -3.8 | 0.009 | 12/48 (NCI-H460, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.048 | 14/46 (SNU-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.087 | 11/45 (SNU-423, A549, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.761× | -3.0 | 0.14 | 12/46 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.65× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 6.70 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.22× (z +9.8) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0573× (z -12.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 12.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.84 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.53× (z +13.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 5.53 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.64× (z +8.6) ⚠ toxic; transcription drop | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0937× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 7.25 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.8× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0842× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.2) |
| [[SNU-423 (line)]] | alt | 7.46 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.35× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 7.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 7.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 6.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.54 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 7.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 6.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL9]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[SEPHS1]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FECH]] | +0.61 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RCN1]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[B3GALNT1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[RPL6]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FAM136A]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[EMB]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[APEX1]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[HNRNPA1L3]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[RPSA]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R13L]] | -0.61 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[MIDN]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.55 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[ATG2A]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MTHFR]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TOM1L2]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[FKBP2]] ⚠ | -0.52 | -0.56 / -0.37 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J4]] | -0.51 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[SRSF9]] ⚠ | -0.51 | -0.49 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPARA]] | -0.51 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[ARID3A]] | -0.51 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ELL]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TRIOBP]] | -0.50 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ZBTB7A]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PDCL3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PDCL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.7, -27.7); signed map (-13.8, -41.9). **Vector** length 64.6, 10.5% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +19.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +13.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.5 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -8.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.2 | +0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phosducin like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:100,562,993-100,576,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VIAF1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2J4](https://www.uniprot.org/uniprotkb/Q9H2J4) (Phosducin-like protein 3):

> Acts as a chaperone for the angiogenic VEGF receptor KDR/VEGFR2, increasing its abundance by inhibiting its ubiquitination and degradation. Inhibits the folding activity of the chaperonin-containing T-complex (CCT) which leads to inhibition of cytoskeletal actin folding. Acts as a chaperone during heat shock alongside HSP90 and HSP40/70 chaperone complexes (By similarity). Modulates the activation of caspases during apoptosis.

**Summary**, from NCBI Gene [79031](https://www.ncbi.nlm.nih.gov/gene/79031):

> This gene encodes a member of the phosducin-like protein family and is a putative modulator of heterotrimeric G proteins. The protein shares extensive amino acid sequence homology with phosducin. Members of the phosducin-like protein family have been shown to bind to the beta-gamma subunits of G proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28860) · Entrez [79031](https://www.ncbi.nlm.nih.gov/gene/79031) · UniProt [Q9H2J4](https://www.uniprot.org/uniprotkb/Q9H2J4) · Ensembl [ENSG00000115539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115539)

## Data

Gene col 3691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3691); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3691]; `tensor/DDL_lfc|DDL_z.npy` [3691]; `embed/gene_vectors.npy` [3691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3691 or target_col == 3691). Every well: [[PDCL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
