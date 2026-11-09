---
symbol: "BCL2"
type: "gene"
col: 10160
ensembl_id: "ENSG00000171791"
name: "BCL2 apoptosis regulator"
location: "18q21.33"
module: 5
arm: "+"
pooled_cpm: 18.77
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# BCL2

*BCL2 apoptosis regulator* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.00× (z +21.8, q 0e+00, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.624× (z -6.8, q 8e-09, down in 19 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 0.733× (z -6.2, q 2e-07, down in 16 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEND3]] (+0.64, fdr 1e-05), [[ADGRA3]] (+0.61, fdr 1e-05), [[NCR3LG1]] (+0.58, fdr 1e-05); moves opposite to [[ZFYVE19]] (-0.58, fdr 9e-05), [[WIPF2]] (-0.56, fdr 8e-05), [[PLD3]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PDE3B]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLC16A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +21.8 | 0e+00 | 31/36 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +17.6 | 0e+00 | 25/35 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +9.4 | 2e-18 | 22/35 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +9.3 | 2e-18 | 24/35 (C32, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.2 | 7e-11 | 17/37 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.64×** | +6.5 | 7e-09 | 12/27 (C32, Hs 766T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.5 | 7e-09 | 18/36 (LOX-IMVI, J82, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +5.3 | 1e-05 | 14/35 (H4, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +4.8 | 9e-05 | 10/36 (NCI-H1792, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 15/35 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +4.7 | 2e-04 | 14/35 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 14/35 (RKO, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.40×** | +4.6 | 2e-04 | 6/21 (SW480, BT-474, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 10/35 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 7e-04 | 10/37 (LoVo, SHP-77, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.034 | 10/36 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.1 | 0.057 | 3/37 (SHP-77, SNU-1, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.064 | 5/36 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.093 | 1/35 (SNU-1) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.8 | 8e-09 | 19/35 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.733×** | -6.2 | 2e-07 | 16/37 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.728×** | -4.5 | 0.001 | 16/36 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -4.5 | 0.001 | 12/35 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -4.4 | 0.001 | 16/35 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -4.1 | 0.003 | 17/35 (SNU-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.851× | -3.2 | 0.12 | 5/37 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 0.656× | -3.1 | 0.12 | 6/31 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.659× | -3.1 | 0.12 | 8/35 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 143 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0856× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.208× (z -12.8) |
| [[C32 (line)]] | wt | 14.2 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +19.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.102× (z -8.7) |
| [[SHP-77 (line)]] | alt | 233 | 1 | 6 (4 ⚠) | [[Tofacitinib (drug)]] 5 µM 1.89× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.264× (z -13.3) |
| [[A-172 (line)]] | wt | 8.77 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +16.1) | [[Vismodegib (drug)]] 0.05 µM 0.101× (z -9.0) |
| [[A498 (line)]] | wt | 28.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +24.2) | — |
| [[C-33 A (line)]] | alt | 20.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0898× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 24.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +18.8) | — |
| [[LoVo (line)]] | wt | 40.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -11.0) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 2 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0474× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +12.6) | [[Rifaximin (drug)]] 0.05 µM 0.0612× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0677× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0801× (z -11.4) |
| [[RKO (line)]] | wt | 43.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0705× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 9.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +12.4) | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0397× (z -13.5) |
| [[AN3 CA (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 6.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.418× (z -12.9) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 5.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +14.3) | — |
| [[A549 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ADGRA3]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TMEM117]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[GNAL]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PIGW]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[E2F3]] | +0.55 | +0.51 / +0.43 | both halves | 3e-05 | STRING 530 |
| [[PARD3B]] | +0.55 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[PCSK6]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[HNRNPAB]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HS6ST2]] | +0.53 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[USP13]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE19]] | -0.58 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[WIPF2]] | -0.56 | -0.65 / -0.37 | both halves | 8e-05 |  |
| [[PLD3]] | -0.55 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[CCS]] | -0.55 | -0.40 / -0.44 | both halves | 5e-05 | pathway: Cellular response to chemical stress |
| [[RANBP10]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[VRK3]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[TUBG2]] | -0.53 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[ZYG11B]] | -0.53 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CRYZL1]] | -0.53 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[PLD2]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CLPTM1]] | -0.52 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[RAB2B]] | -0.51 | -0.58 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3B]] | B | PDE3B activity raises BCL2's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 2.10× lower at baseline in the lines without PDE3B | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[KCND3]] | B | KCND3 activity raises BCL2's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without KCND3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[CACHD1]] | B | CACHD1 activity raises BCL2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 3.14× lower at baseline in the lines without CACHD1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[TAFA5]] | B | TAFA5 activity raises BCL2's level | lines that do not express TAFA5 (29) vs lines expressing it (21) | 1.47× lower at baseline in the lines without TAFA5 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000260958, UNC5D, EPGN |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A9]] | B | BCL2 activity raises SLC16A9's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without BCL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CD226 |
| [[AUTS2]] | B | BCL2 activity raises AUTS2's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 3.07× lower at baseline in the lines without BCL2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CD226 |
| [[KCND3]] | B | BCL2 activity raises KCND3's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without BCL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CD226 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.1, 7.2); signed map (24.5, -33.2). **Vector** length 99.0, 24.4% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +17.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +21.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 apoptosis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,123,346-63,320,128 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Bcl-2, PPP1R50 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; BCL2 family |
| Hallmark sets | IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_LATE, HYPOXIA, ESTROGEN_RESPONSE_EARLY |
| Reactome | 27 pathways, smallest: The NLRP1 inflammasome; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members; NFE2L2 regulating tumorigenic genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P10415](https://www.uniprot.org/uniprotkb/P10415) (Apoptosis regulator Bcl-2):

> Suppresses apoptosis in a variety of cell systems including factor-dependent lymphohematopoietic and neural cells. Regulates cell death by controlling the mitochondrial membrane permeability. Appears to function in a feedback loop system with caspases. Inhibits caspase activity either by preventing the release of cytochrome c from the mitochondria and/or by binding to the apoptosis-activating factor (APAF-1). Also acts as an inhibitor of autophagy: interacts with BECN1 and AMBRA1 during …

**Summary**, from NCBI Gene [596](https://www.ncbi.nlm.nih.gov/gene/596):

> This gene encodes an integral outer mitochondrial membrane protein that blocks the apoptotic death of some cells such as lymphocytes. Constitutive expression of BCL2, such as in the case of translocation of BCL2 to Ig heavy chain locus, is thought to be the cause of follicular lymphoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:990) · Entrez [596](https://www.ncbi.nlm.nih.gov/gene/596) · UniProt [P10415](https://www.uniprot.org/uniprotkb/P10415) · Ensembl [ENSG00000171791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171791)

## Data

Gene col 10160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10160); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10160]; `tensor/DDL_lfc|DDL_z.npy` [10160]; `embed/gene_vectors.npy` [10160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10160 or target_col == 10160). Every well: [[BCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
