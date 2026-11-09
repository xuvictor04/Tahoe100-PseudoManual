---
symbol: "NMT1"
type: "gene"
col: 5864
ensembl_id: "ENSG00000136448"
name: "N-myristoyltransferase 1"
location: "17q21.31"
module: 156
arm: "+"
pooled_cpm: 109.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# NMT1

*N-myristoyltransferase 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.91× (z +11.6, q 2e-28, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.632× (z -11.7, q 1e-28, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBSN]] (+0.69, fdr 7e-06), [[ECSIT]] (+0.69, fdr 9e-06), [[SFSWAP]] (+0.68, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.60, fdr 1e-05), [[PTPN18]] (-0.57, fdr 1e-05), [[TFRC]] (-0.57, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +11.6 | 2e-28 | 48/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +11.5 | 4e-28 | 48/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.64×** | +8.9 | 8e-17 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +8.5 | 3e-15 | 46/48 (NCI-H2347, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.57×** | +8.1 | 8e-14 | 43/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +6.8 | 8e-10 | 43/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +6.7 | 1e-09 | 42/48 (C32, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.47×** | +6.7 | 2e-09 | 35/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +6.7 | 2e-09 | 39/49 (SW480, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +6.4 | 7e-09 | 28/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.7 | 7e-07 | 32/45 (CFPAC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.27×** | +4.3 | 1e-03 | 31/48 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.26×** | +4.2 | 0.001 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.6 | 0.013 | 25/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.013 | 25/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.027 | 25/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.084 | 20/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -11.7 | 1e-28 | 42/49 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -8.1 | 1e-13 | 40/48 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -4.7 | 3e-04 | 31/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.7 | 3e-04 | 28/50 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 0.836× | -4.6 | 6e-04 | 20/48 (A498, J82, …) | rises with dose | low cells (technical?) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.824× | -3.2 | 0.12 | 25/48 (A498, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 110 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 107 | 4 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.12× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.1) |
| [[SW480 (line)]] | alt | 126 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.22× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 114 | 2 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.66× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.7) |
| [[KATO III (line)]] | alt | 138 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 87.2 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 131 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -9.0) |
| [[LoVo (line)]] | wt | 99.3 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.2) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.7) |
| [[RKO (line)]] | wt | 129 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.6) |
| [[A-172 (line)]] | wt | 140 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +10.0) | — |
| [[A-427 (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 93.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[H4 (line)]] | wt | 136 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 124 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 97.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.67× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 95.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 130 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 89.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.10× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 126 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.8) |
| [[PANC-1 (line)]] | alt | 84.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 114 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +9.2) | — |
| [[A549 (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 131 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.6) |
| [[HT-29 (line)]] | alt | 87.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 124 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.60× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 96.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.3) |
| [[A498 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBSN]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ECSIT]] | +0.69 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[SFSWAP]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.68 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Apoptosis |
| [[PSMD3]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Apoptosis |
| [[PSMB1]] | +0.67 | +0.58 / +0.71 | both halves | 8e-06 | pathway: Apoptosis |
| [[FAF2]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DCTN6]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[BRF2]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MAU2]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PSMA4]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[UBE2J2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PTPN18]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TFRC]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[FKBP1A]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RASSF3]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[EDEM1]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[H3-3A]] | -0.51 | -0.57 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NMT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EPB41L2]] | B | EPB41L2 activity raises NMT1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without EPB41L2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.5, -2.9); signed map (-5.6, -15.3). **Vector** length 112, 36.3% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.7 | +5.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | -0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | -0.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -2.9 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | N-myristoyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,957,992-45,109,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NMT |
| Gene groups (HGNC) | N-myristoyltransferase family |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 17 pathways, smallest: Activation, myristolyation of BID and translocation to mitochondria; eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P30419](https://www.uniprot.org/uniprotkb/P30419) (Glycylpeptide N-tetradecanoyltransferase 1):

> Adds a myristoyl group to the N-terminal glycine residue of certain cellular and viral proteins. Also able to mediate N-terminal lysine myristoylation of proteins: catalyzes myristoylation of ARF6 on both 'Gly-2' and 'Lys-3'. Lysine myristoylation is required to maintain ARF6 on membranes during the GTPase cycle.

**Summary**, from NCBI Gene [4836](https://www.ncbi.nlm.nih.gov/gene/4836):

> Myristate, a rare 14-carbon saturated fatty acid, is cotranslationally attached by an amide linkage to the N-terminal glycine residue of cellular and viral proteins with diverse functions. N-myristoyltransferase (NMT; EC 2.3.1.97) catalyzes the transfer of myristate from CoA to proteins. N-myristoylation appears to be irreversible and is required for full expression of the biologic activities of several N-myristoylated proteins, including the alpha subunit of the signal-transducing guanine …

**Accessions** — [HGNC:7857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7857) · Entrez [4836](https://www.ncbi.nlm.nih.gov/gene/4836) · UniProt [P30419](https://www.uniprot.org/uniprotkb/P30419) · Ensembl [ENSG00000136448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136448)

## Data

Gene col 5864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5864); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5864]; `tensor/DDL_lfc|DDL_z.npy` [5864]; `embed/gene_vectors.npy` [5864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5864 or target_col == 5864). Every well: [[NMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
