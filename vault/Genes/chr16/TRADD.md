---
symbol: "TRADD"
type: "gene"
col: 2279
ensembl_id: "ENSG00000102871"
name: "TNFRSF1A associated via death domain"
location: "16q22.1"
module: 3
arm: "+"
pooled_cpm: 14.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRADD

*TNFRSF1A associated via death domain* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.44× (z +4.0, q 0.031, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.285× (z -19.9, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRT7]] (+0.68, fdr 1e-05), [[TM2D2]] (+0.64, fdr 8e-05), [[BSDC1]] (+0.64, fdr 7e-06); moves opposite to [[BTBD1]] (-0.60, fdr 4e-05), [[ATIC]] (-0.60, fdr 1e-05), [[GNG12]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.031 | 23/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.031 | 21/47 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.033 | 14/40 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.072 | 17/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.12 | 12/48 (HOP62, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.24 | 13/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.285×** | -19.9 | 0e+00 | 43/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.372×** | -11.1 | 4e-26 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -10.9 | 2e-25 | 40/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -9.2 | 4e-18 | 36/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -9.1 | 7e-18 | 37/44 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -9.0 | 1e-17 | 35/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.228×** | -8.7 | 3e-16 | 36/48 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.478×** | -8.3 | 9e-15 | 34/48 (SNU-423, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.277×** | -7.5 | 3e-12 | 33/44 (SW 900, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.515×** | -7.4 | 6e-12 | 34/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -7.3 | 1e-11 | 38/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -7.0 | 1e-10 | 31/43 (RPMI-7951, NCI-H23, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.545×** | -6.8 | 4e-10 | 32/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.570×** | -6.3 | 1e-08 | 23/34 (A-172, NCI-H1792, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.735×** | -4.9 | 4e-05 | 23/44 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.652×** | -4.8 | 6e-05 | 22/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -4.5 | 2e-04 | 23/48 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -4.2 | 6e-04 | 19/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.030 | 18/48 (NCI-H2347, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.031 | 19/48 (A-172, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.8 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -23.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0666× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.2) |
| [[A-172 (line)]] | wt | 29.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -16.6) |
| [[A549 (line)]] | wt | 17.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0354× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0735× (z -19.7) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.5) |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 8.50 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0753× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.64 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.0) |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.7) |
| [[A498 (line)]] | wt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.9) |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0638× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.0) |
| [[H4 (line)]] | wt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -9.0) |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -24.1) |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.3) |
| [[J82 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.5) |
| [[LoVo (line)]] | wt | 8.92 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -8.6) |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 9.66 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.222× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.9) |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.7) |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT7]] | +0.68 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.64 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[BSDC1]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DUSP18]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[NOL3]] | +0.63 | +0.53 / +0.71 | both halves | 1e-05 | STRING 406; ⚠ same locus (10.2 kb: neighbours can correlate without regulation) |
| [[PEX16]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[RNF181]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[JOSD2]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[BAHD1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD1]] | -0.60 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ATIC]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[GNG12]] | -0.58 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[IPO5]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SEPTIN11]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[MTHFD1]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[DHFR]] | -0.56 | -0.24 / -0.62 | both halves | 4e-04 |  |
| [[TFDP1]] | -0.55 | -0.43 / -0.59 | both halves | 4e-05 | pathway: Apoptosis |
| [[SNX5]] | -0.55 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[AKAP11]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[NUP210]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PRPS2]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRADD's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRADD's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[LINC00847]] | C | LINC00847 activity raises TRADD's level | lines that do not express LINC00847 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without LINC00847 | 0.056 | ⚠ few lines (4 vs 46); across organs; also absent: DDR1, FTH1, HEIH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.3, -16.2); signed map (-24.0, 8.0). **Vector** length 71.5, 14.9% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -6.0 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.7 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -5.6 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TNFRSF1A associated via death domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,154,185-67,159,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hs.89862 |
| Reactome | 17 pathways, smallest: Defective RIPK1-mediated regulated necrosis; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15628](https://www.uniprot.org/uniprotkb/Q15628) (Tumor necrosis factor receptor type 1-associated DEATH domain protein):

> Adapter molecule for TNFRSF1A/TNFR1 in the tumor necrosis factor-mediated (TNF) signaling pathway. Specifically associates with the cytoplasmic domain of activated TNFRSF1A/TNFR1 mediating its interaction with FADD, initiating formation of the complex I (TNF-R1 signaling complex also known as TNF-RSC), a multiprotein complex that acts as a decision maker to initiate pro-survival or programmed cell death. Overexpression of TRADD leads to two major TNF-induced responses, apoptosis and activation …

**Summary**, from NCBI Gene [8717](https://www.ncbi.nlm.nih.gov/gene/8717):

> The protein encoded by this gene is a death domain containing adaptor molecule that interacts with TNFRSF1A/TNFR1 and mediates programmed cell death signaling and NF-kappaB activation. This protein binds adaptor protein TRAF2, reduces the recruitment of inhibitor-of-apoptosis proteins (IAPs) by TRAF2, and thus suppresses TRAF2 mediated apoptosis. This protein can also interact with receptor TNFRSF6/FAS and adaptor protein FADD/MORT1, and is involved in the Fas-induced cell death pathway. …

**Accessions** — [HGNC:12030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12030) · Entrez [8717](https://www.ncbi.nlm.nih.gov/gene/8717) · UniProt [Q15628](https://www.uniprot.org/uniprotkb/Q15628) · Ensembl [ENSG00000102871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102871)

## Data

Gene col 2279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2279); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2279]; `tensor/DDL_lfc|DDL_z.npy` [2279]; `embed/gene_vectors.npy` [2279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2279 or target_col == 2279). Every well: [[TRADD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRADD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
