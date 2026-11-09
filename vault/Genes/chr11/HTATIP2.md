---
symbol: "HTATIP2"
type: "gene"
col: 3088
ensembl_id: "ENSG00000109854"
name: "HIV-1 Tat interactive protein 2"
location: "11p15.1"
module: 135
arm: "+"
pooled_cpm: 18.33
n_lines_expressing: 43
n_dd_up: 30
n_dd_down: 12
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# HTATIP2

*HIV-1 Tat interactive protein 2* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +13.6, q 2e-39, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.41× (z +10.8, q 9e-25, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.455× (z -9.6, q 3e-19, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.70, fdr 1e-05), [[NQO1-DT]] (+0.70, fdr 8e-06), [[RNF6]] (+0.70, fdr 1e-05); moves opposite to [[BRAT1]] (-0.58, fdr 3e-05), [[TXNDC17]] (-0.58, fdr 2e-04), [[ETHE1]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZFR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +13.6 | 2e-39 | 33/35 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.3 | 3e-27 | 24/25 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.41×** | +10.8 | 9e-25 | 34/40 (HT-29, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +9.7 | 3e-20 | 28/29 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +8.4 | 7e-15 | 35/40 (NCI-H2347, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.97×** | +8.3 | 7e-15 | 33/40 (COLO 205, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +7.5 | 4e-12 | 29/40 (COLO 205, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.2 | 6e-11 | 27/41 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.5 | 5e-09 | 28/41 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.6 | 3e-04 | 22/40 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +4.5 | 3e-04 | 19/41 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.4 | 6e-04 | 20/40 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.2 | 0.001 | 19/38 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 14/40 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.008 | 15/41 (PANC-1, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.011 | 13/41 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.012 | 14/40 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.013 | 13/40 (PANC-1, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.021 | 14/40 (NCI-H460, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -9.6 | 3e-19 | 34/40 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -7.7 | 5e-12 | 34/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.539×** | -7.6 | 8e-12 | 29/40 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.435×** | -5.3 | 1e-05 | 20/40 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.763×** | -4.7 | 4e-04 | 19/41 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -4.6 | 4e-04 | 20/40 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.006 | 16/40 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -3.5 | 0.032 | 18/40 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.067 | 15/40 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.095 | 15/40 (LoVo, HOP62, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.615×** | -3.1 | 0.097 | 13/40 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.097 | 12/40 (CFPAC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +9.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.83× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 28.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.5) |
| [[A498 (line)]] | wt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 23.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.62× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 8.84 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0833× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~19% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.135× (z -8.6) |
| [[HT-29 (line)]] | alt | 34.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.44× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.327× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0732× (z -11.0) |
| [[J82 (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.8) |
| [[A-427 (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 6.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -10.3) |
| [[A-172 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.70 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[RNF6]] | +0.70 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.68 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[DNAJB4]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.67 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MRPL45]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[AP5M1]] | +0.66 | +0.67 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.58 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.58 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[ETHE1]] | -0.57 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[FANCE]] | -0.57 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[TXNL4A]] | -0.56 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[PIBF1]] | -0.55 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[VPS37C]] | -0.55 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[CKLF]] | -0.55 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[MINK1]] | -0.54 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[NPHP4]] | -0.54 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[SOX13]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HTATIP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFR]] | B | HTATIP2 activity lowers ZFR's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 1.11× higher at baseline in the lines without HTATIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3; its own permutation p |
| [[ME1]] | B | HTATIP2 activity raises ME1's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without HTATIP2 | 0.077 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3 |
| [[DEPDC7]] | B | HTATIP2 activity lowers DEPDC7's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without HTATIP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3 |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-16.6, 10.5); signed map (21.2, -24.9). **Vector** length 92.6, 23.9% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.0 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.0 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -9.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -5.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | +0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Baicalin (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | HIV-1 Tat interactive protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:20,363,685-20,383,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIP30, CC3, FLJ26963, SDR44U1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUP3](https://www.uniprot.org/uniprotkb/Q9BUP3) (Protein HTATIP2):

> Represses translation by preventing reactivation of elongation factor eEF1A (By similarity). May also inhibit nuclear import by competing with nuclear import substrates for binding to a subset of nuclear transport receptors. Has additionally been proposed to act as a redox sensor involved in cellular oxidative stress surveillance.

**Summary**, from NCBI Gene [10553](https://www.ncbi.nlm.nih.gov/gene/10553):

> Enables protein serine/threonine kinase activity. Acts upstream of or within positive regulation of programmed cell death; positive regulation of transcription by RNA polymerase II; and protein autophosphorylation. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16637) · Entrez [10553](https://www.ncbi.nlm.nih.gov/gene/10553) · UniProt [Q9BUP3](https://www.uniprot.org/uniprotkb/Q9BUP3) · Ensembl [ENSG00000109854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109854)

## Data

Gene col 3088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3088); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3088]; `tensor/DDL_lfc|DDL_z.npy` [3088]; `embed/gene_vectors.npy` [3088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3088 or target_col == 3088). Every well: [[HTATIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTATIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
