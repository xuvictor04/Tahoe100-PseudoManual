---
symbol: "ATOSB"
type: "gene"
col: 75
ensembl_id: "ENSG00000005238"
name: "atos homolog B"
location: "9p13.3"
module: 161
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 14
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# ATOSB

*atos homolog B* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.67× (z +8.9, q 2e-16, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.380× (z -11.8, q 1e-29, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D10A]] (+0.65, fdr 3e-05), [[PLCD1]] (+0.64, fdr 1e-05), [[CARD19]] (+0.63, fdr 3e-05); moves opposite to [[ENOSF1]] (-0.64, fdr 4e-05), [[SLC12A2-DT]] (-0.59, fdr 3e-05), [[PSPC1]] (-0.58, fdr 1e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DAB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 75.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +8.9 | 2e-16 | 23/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 2e-05 | 14/38 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +5.1 | 6e-05 | 15/45 (A-172, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 2e-04 | 13/43 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 4e-04 | 14/42 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +4.4 | 8e-04 | 14/41 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 8e-04 | 11/46 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 17/45 (KATO III, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.0 | 0.004 | 10/32 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.008 | 14/46 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.035 | 8/46 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.065 | 5/31 (HEC-1-A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.074 | 6/35 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.077 | 12/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.089 | 3/39 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 75.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.380×** | -11.8 | 1e-29 | 30/46 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.457×** | -9.6 | 2e-19 | 29/44 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -6.9 | 1e-09 | 26/45 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -6.2 | 6e-08 | 28/38 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -5.9 | 3e-07 | 20/39 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.7 | 9e-07 | 19/35 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -5.6 | 1e-06 | 21/45 (hTERT-HPNE, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -5.6 | 2e-06 | 16/31 (Hs 766T, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.634×** | -5.6 | 2e-06 | 19/28 (AsPC-1, PANC-1, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -4.9 | 5e-05 | 19/44 (Hs 766T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -4.4 | 5e-04 | 11/41 (H4, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.679×** | -4.4 | 6e-04 | 13/36 (A-172, A549, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.2 | 1e-03 | 19/42 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.008 | 16/42 (NCI-H1792, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.745×** | -3.6 | 0.012 | 8/45 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -3.3 | 0.029 | 12/37 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.031 | 10/43 (HCT15, NCI-H460, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.829×** | -3.1 | 0.057 | 8/46 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 75. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.8 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.112× (z -13.3) |
| [[H4 (line)]] | wt | 14.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0449× (z -12.3) |
| [[HS-578T (line)]] | alt | 9.88 | 0 | 4 (2 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0792× (z -11.4) |
| [[A498 (line)]] | wt | 14.2 | 0 | 2 (1 ⚠) | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.208× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.8) |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -14.4) |
| [[BT-474 (line)]] | alt | 3.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0368× (z -9.2) ⚠ cell-cycle shift, explains ~6% of this change |
| [[HOP62 (line)]] | alt | 5.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -9.0) |
| [[J82 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[LOX-IMVI (line)]] | wt | 7.20 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.78 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.131× (z -9.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 3.94 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[Panc 03.27 (line)]] | alt | 4.60 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0890× (z -8.9) |
| [[PANC-1 (line)]] | alt | 5.08 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 7.70 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0780× (z -9.0) |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 75), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D10A]] | +0.65 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[PLCD1]] | +0.64 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CARD19]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TMEM120A]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SIRT7]] | +0.62 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[GIPR]] | +0.62 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TWF2]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CASTOR1]] | +0.61 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[RRAS]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NAGK]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[KCTD10]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DOK4]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOSF1]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.59 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[PSPC1]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.56 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[GTF2I]] | -0.56 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[RNASEH2B]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SNX5]] | -0.55 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CPSF2]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PAXBP1]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ANXA2R-AS1]] | -0.54 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[ATE1]] | -0.54 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[DPY19L1P1]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAB2]] | B | DAB2 activity raises ATOSB's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without DAB2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.8, 3.3); signed map (-28.3, 17.8). **Vector** length 82.3, 15.3% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.3 | +8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -9.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | atos homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,104,112-35,116,341 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11560, bA182N22.6; previously KIAA1539, FAM214B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5A3](https://www.uniprot.org/uniprotkb/Q7L5A3) (Atos homolog protein B):

> Transcription regulator that may syncronize transcriptional and translational programs.

**Summary**, from NCBI Gene [80256](https://www.ncbi.nlm.nih.gov/gene/80256):

> Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25666) · Entrez [80256](https://www.ncbi.nlm.nih.gov/gene/80256) · UniProt [Q7L5A3](https://www.uniprot.org/uniprotkb/Q7L5A3) · Ensembl [ENSG00000005238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005238)

## Data

Gene col 75: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 75); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 75, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 75]; `tensor/DDL_lfc|DDL_z.npy` [75]; `embed/gene_vectors.npy` [75]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 75 or target_col == 75). Every well: [[ATOSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATOSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
