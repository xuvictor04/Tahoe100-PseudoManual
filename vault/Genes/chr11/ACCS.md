---
symbol: "ACCS"
type: "gene"
col: 3143
ensembl_id: "ENSG00000110455"
name: "1-aminocyclopropane-1-carboxylate synthase homolog (inactive)"
location: "11p11.2"
module: 46
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ACCS

*1-aminocyclopropane-1-carboxylate synthase homolog (inactive)* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.86× (z +8.4, q 3e-14, up in 27 of 42 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.81× (z +5.7, q 4e-06, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.339× (z -10.3, q 5e-22, down in 32 of 42 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.516× (z -6.3, q 2e-08, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF391]] (+0.62, fdr 1e-05), [[PPM1M]] (+0.61, fdr 2e-05), [[IDNK]] (+0.61, fdr 1e-04); moves opposite to [[PPFIA1]] (-0.58, fdr 3e-05), [[TXNDC17]] (-0.58, fdr 1e-04), [[TMEM184B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[JHY]] → it (grade B ⚠); 14 go from it, the strongest it → cells under [[PF-06260933 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.86×** | +8.4 | 3e-14 | 27/42 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +5.7 | 4e-06 | 24/41 (J82, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.034 | 7/39 (A-427, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +3.6 | 0.038 | 9/40 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.038 | 12/42 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.048 | 7/42 (SW480, J82, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.11 | 8/39 (SW480, J82, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.42× | +3.1 | 0.12 | 5/43 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.339×** | -10.3 | 5e-22 | 32/42 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.378×** | -9.2 | 8e-18 | 28/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.514×** | -8.9 | 8e-17 | 25/36 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.418×** | -8.3 | 2e-14 | 26/33 (A549, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.429×** | -8.0 | 1e-13 | 28/41 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.450×** | -7.6 | 3e-12 | 28/41 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.455×** | -7.5 | 6e-12 | 30/40 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.513×** | -6.3 | 2e-08 | 22/35 (PANC-1, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.516×** | -6.3 | 2e-08 | 22/39 (HCT15, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.548×** | -5.7 | 7e-07 | 22/39 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.577×** | -5.0 | 3e-05 | 14/33 (PANC-1, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.595×** | -4.7 | 1e-04 | 18/39 (PANC-1, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.386×** | -4.7 | 1e-04 | 18/38 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -4.6 | 2e-04 | 16/40 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.654×** | -4.0 | 0.002 | 18/37 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -3.7 | 0.007 | 14/40 (SW480, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.016 | 12/39 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -3.4 | 0.016 | 14/36 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.4 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.291× (z -8.5) |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -21.8) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -8.6) |
| [[A549 (line)]] | wt | 12.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0467× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 8.77 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0654× (z -8.9) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 6.69 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0779× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 7.77 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0763× (z -8.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 4.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0922× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 5.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -12.8) ⚠ cell-cycle shift, explains ~76% of this change |
| [[NCI-H23 (line)]] | alt | 7.24 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.118× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -8.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0524× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF391]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PPM1M]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[IDNK]] | +0.61 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[FAIM]] | +0.61 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[GAS2]] | +0.60 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[RRAGB]] | +0.59 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[THBS4]] | +0.58 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[RAB21]] | +0.58 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ANKRD18CP]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[NEIL1]] | +0.58 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[C14orf93]] | +0.58 | +0.56 / +0.27 | both halves | 3e-04 |  |
| [[CC2D2A]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIA1]] | -0.58 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.58 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.57 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ZFYVE28]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[EPN2]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[AGAP1]] | -0.56 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[KIAA1958]] | -0.56 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[KIAA1328]] | -0.55 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[SLC35E1]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.54 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SLC2A13]] | -0.53 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[RCOR1]] | -0.52 | -0.35 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JHY]] | B | JHY activity raises ACCS's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without JHY | 0.042 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[THBS4]] | B | THBS4 activity raises ACCS's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without THBS4 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[DPH6-DT]] | C | DPH6-DT activity raises ACCS's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 3.38× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[PF-06260933 (drug)]] 5 µM | C | ACCS activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 1.49× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | ACCS activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 1.33× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | ACCS activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.80× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Tranilast (drug)]] 0.5 µM | C | ACCS activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.77× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | ACCS activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.64× the cells of the other lines | 0.040 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | ACCS activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.74× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Tolcapone (drug)]] 5 µM | C | ACCS activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.82× the cells of the other lines | 0.060 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ACCS activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 1.30× the cells of the other lines | 0.073 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Posaconazole (drug)]] 0.5 µM | C | ACCS activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.80× the cells of the other lines | 0.073 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Raltitrexed (drug)]] 0.5 µM | C | ACCS activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 1.27× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Naproxen (drug)]] 5 µM | C | ACCS activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.80× the cells of the other lines | 0.076 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| cells under [[Piroxicam (drug)]] 0.05 µM | C | ACCS activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.79× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.2, 29.5); signed map (35.8, -14.1). **Vector** length 58.2, 9.19% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.9 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.5 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.8 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.7 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.6 | -7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | 1-aminocyclopropane-1-carboxylate synthase homolog (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:44,065,925-44,084,237 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHACS, ACS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QU6](https://www.uniprot.org/uniprotkb/Q96QU6) (1-aminocyclopropane-1-carboxylate synthase-like protein 1):

> Does not catalyze the synthesis of 1-aminocyclopropane-1-carboxylate but is capable of catalyzing the deamination of L-vinylglycine.

**Summary**, from NCBI Gene [84680](https://www.ncbi.nlm.nih.gov/gene/84680):

> Enables identical protein binding activity. Predicted to be involved in amino acid metabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23989) · Entrez [84680](https://www.ncbi.nlm.nih.gov/gene/84680) · UniProt [Q96QU6](https://www.uniprot.org/uniprotkb/Q96QU6) · Ensembl [ENSG00000110455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110455)

## Data

Gene col 3143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3143); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3143]; `tensor/DDL_lfc|DDL_z.npy` [3143]; `embed/gene_vectors.npy` [3143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3143 or target_col == 3143). Every well: [[ACCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
