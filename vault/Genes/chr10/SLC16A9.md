---
symbol: "SLC16A9"
type: "gene"
col: 9122
ensembl_id: "ENSG00000165449"
name: "solute carrier family 16 member 9"
location: "10q21.2"
module: 68
arm: "+"
pooled_cpm: 9.05
n_lines_expressing: 32
n_dd_up: 32
n_dd_down: 22
n_dd_up_clean: 24
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SLC16A9

*solute carrier family 16 member 9* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.47× (z +25.3, q 0e+00, up in 25 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.538× (z -8.9, q 4e-16, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM169A]] (+0.77, fdr 7e-06), [[MCCC2]] (+0.69, fdr 3e-05), [[ZNF462]] (+0.68, fdr 1e-05); moves opposite to [[ADIPOR1]] (-0.67, fdr 2e-05), [[PCMT1]] (-0.67, fdr 1e-04), [[GNB2]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BCL2]] → it (grade B ⚠); 8 go from it, the strongest it → [[BAIAP2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.47×** | +25.3 | 0e+00 | 25/27 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.50×** | +18.7 | 0e+00 | 27/29 (A-172, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.87×** | +15.2 | 0e+00 | 23/26 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.89×** | +14.7 | 0e+00 | 24/29 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +14.2 | 8e-44 | 19/29 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.49×** | +13.1 | 2e-37 | 25/29 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.38×** | +12.5 | 1e-33 | 25/29 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.8 | 1e-16 | 16/29 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.77×** | +8.2 | 1e-14 | 21/29 (LS 180, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.1 | 3e-14 | 16/28 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.8 | 4e-13 | 13/25 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.5 | 2e-12 | 5/13 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-10 | 14/28 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +6.7 | 1e-09 | 14/29 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.1 | 4e-08 | 16/29 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 6e-04 | 7/29 (A-172, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.2 | 8e-04 | 7/29 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.001 | 14/29 (NCI-H1573, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -8.9 | 4e-16 | 19/29 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -8.4 | 1e-14 | 20/29 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.562×** | -8.2 | 3e-14 | 20/29 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -7.9 | 4e-13 | 15/29 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -7.4 | 1e-11 | 15/29 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -7.1 | 1e-10 | 18/29 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -6.3 | 2e-08 | 16/29 (LoVo, RKO, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -6.0 | 1e-07 | 18/29 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -5.8 | 3e-07 | 18/28 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -5.8 | 5e-07 | 16/29 (SW48, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.681×** | -5.5 | 2e-06 | 11/29 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.7 | 1e-04 | 17/29 (LoVo, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.734×** | -4.2 | 1e-03 | 6/29 (SNU-423, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.750×** | -4.1 | 0.002 | 10/29 (RKO, SW48, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -4.0 | 0.002 | 14/25 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.758×** | -4.0 | 0.003 | 14/29 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.592×** | -3.9 | 0.003 | 8/28 (A498, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.5 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +31.8) | [[Panobinostat (drug)]] 5 µM 0.167× (z -17.0) |
| [[RKO (line)]] | wt | 35.4 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0716× (z -18.0) |
| [[LoVo (line)]] | wt | 29.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -14.7) |
| [[SW480 (line)]] | alt | 10.2 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0570× (z -10.2) |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0148× (z -17.5) |
| [[SW1417 (line)]] | alt | 6.30 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.54× (z +11.0) | — |
| [[A-172 (line)]] | wt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0837× (z -9.1) |
| [[H4 (line)]] | wt | 11.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 17.3× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 8.68 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -9.9) |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0795× (z -10.4) |
| [[A-427 (line)]] | wt | 15.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.2) |
| [[BT-474 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 6.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +10.7) | — |
| [[J82 (line)]] | alt | 9.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.39 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0960× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.7) | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0717× (z -9.8) ⚠ toxic |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM169A]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.69 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[ZNF462]] | +0.68 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SDSL]] | +0.68 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[KICS2]] | +0.67 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[PLD6]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[RWDD2B]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ARL14EP]] | +0.65 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[GCFC2]] | +0.65 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[POGLUT1]] | +0.65 | +0.73 / +0.36 | both halves | 1e-04 |  |
| [[ZNF827]] | +0.64 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[LATS1]] | +0.64 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADIPOR1]] | -0.67 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[PCMT1]] | -0.67 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[GNB2]] | -0.64 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[GNAI2]] | -0.64 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[PSMD9]] | -0.62 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[TPST2]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[VRK3]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[F11R]] | -0.61 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[PHF1]] | -0.60 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TMEM41B]] | -0.60 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[GSDMB]] | -0.60 | -0.49 / -0.55 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.60 | -0.59 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2]] | B | BCL2 activity raises SLC16A9's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without BCL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CD226 |
| [[IKZF3]] | B | IKZF3 activity raises SLC16A9's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without IKZF3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAIAP2-DT]] | B | SLC16A9 activity lowers BAIAP2-DT's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.37× higher at baseline in the lines without SLC16A9 | 0.020 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[PPP1R9A]] | B | SLC16A9 activity raises PPP1R9A's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without SLC16A9 | 0.032 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[TRAF3]] | B | SLC16A9 activity raises TRAF3's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without SLC16A9 | 0.041 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[RPAP2]] | B | SLC16A9 activity raises RPAP2's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without SLC16A9 | 0.079 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[SMAD1]] | B | SLC16A9 activity raises SMAD1's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without SLC16A9 | 0.080 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[GCFC2]] | B | SLC16A9 activity raises GCFC2's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without SLC16A9 | 0.096 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[FAIM]] | B | SLC16A9 activity raises FAIM's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without SLC16A9 | 0.098 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[PCSK6]] | B | SLC16A9 activity raises PCSK6's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without SLC16A9 | 0.099 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.6, 6.5); signed map (21.2, -31.9). **Vector** length 83.6, 19.5% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +18.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +25.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +15.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.1 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -8.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -6.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:59,650,764-59,736,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43803, MCT9; previously C10orf36 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTY1](https://www.uniprot.org/uniprotkb/Q7RTY1) (Monocarboxylate transporter 9):

> Extracellular pH-and Na(+)-sensitive low-affinity creatine transporter. Also functions as a pH-independent carnitine efflux transporter.

**Summary**, from NCBI Gene [220963](https://www.ncbi.nlm.nih.gov/gene/220963):

> Enables carnitine transmembrane transporter activity and creatine transmembrane transporter activity. Involved in carnitine transmembrane transport; creatine transmembrane transport; and urate metabolic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23520) · Entrez [220963](https://www.ncbi.nlm.nih.gov/gene/220963) · UniProt [Q7RTY1](https://www.uniprot.org/uniprotkb/Q7RTY1) · Ensembl [ENSG00000165449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165449)

## Data

Gene col 9122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9122); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9122]; `tensor/DDL_lfc|DDL_z.npy` [9122]; `embed/gene_vectors.npy` [9122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9122 or target_col == 9122). Every well: [[SLC16A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
