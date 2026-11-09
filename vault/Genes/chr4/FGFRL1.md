---
symbol: "FGFRL1"
type: "gene"
col: 4807
ensembl_id: "ENSG00000127418"
name: "fibroblast growth factor receptor like 1"
location: "4p16.3"
module: 2
arm: "+"
pooled_cpm: 13.25
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FGFRL1

*fibroblast growth factor receptor like 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +13.2, q 5e-37, up in 32 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.72× (z +10.7, q 2e-24, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.813× (z -7.9, q 2e-12, down in 29 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Hydroxyurea (drug)]] 0.5 µM: 0.533× (z -6.8, q 3e-09, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOR2]] (+0.66, fdr 1e-05), [[SUN1]] (+0.66, fdr 2e-05), [[FGFR3]] (+0.63, fdr 3e-05); moves opposite to [[PPCS]] (-0.54, fdr 5e-05), [[SLC16A14]] (-0.53, fdr 6e-05), [[RNF135]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEC]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.43×** | +13.2 | 5e-37 | 32/35 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +12.4 | 1e-32 | 21/23 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +10.7 | 2e-24 | 44/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +10.6 | 6e-24 | 41/46 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +8.5 | 1e-15 | 23/27 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +6.5 | 7e-09 | 31/46 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.61×** | +5.1 | 3e-05 | 24/46 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.0 | 3e-05 | 26/45 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.013 | 16/46 (C32, KATO III, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.015 | 9/46 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.017 | 17/40 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.047 | 10/45 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.36×** | +3.3 | 0.049 | 6/46 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.049 | 8/43 (HCT15, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.049 | 3/39 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.053 | 10/43 (SNU-423, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.085 | 4/43 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.088 | 5/45 (H4, KATO III, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.088 | 6/43 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.813×** | -7.9 | 2e-12 | 29/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.533×** | -6.8 | 3e-09 | 36/46 (HT-29, A498, …) | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.612×** | -5.1 | 6e-05 | 23/44 (NCI-H2030, HS-578T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -5.0 | 7e-05 | 16/45 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Captopril (drug)]] 5 µM |  | **0.629×** | -5.0 | 7e-05 | 28/46 (RKO, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.630×** | -4.8 | 2e-04 | 18/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.644×** | -4.5 | 6e-04 | 16/44 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.650×** | -4.5 | 6e-04 | 18/45 (A498, SW 900, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.752×** | -4.2 | 0.001 | 20/46 (SNU-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -3.8 | 0.007 | 19/41 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.7 | 0.013 | 16/40 (HT-29, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -3.5 | 0.023 | 15/44 (Hs 766T, PANC-1, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.023 | 15/46 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Thymol (drug)]] 0.05 µM |  | **0.731×** | -3.4 | 0.030 | 9/44 (AN3 CA, A498, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.031 | 11/46 (SNU-1, H4, …) | rises with dose | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.059 | 4/47 (A498, A-172, …) | two highest doses | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **0.810×** | -3.0 | 0.097 | 7/47 (A-172, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 21.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.30× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.479× (z -9.6) ⚠ position not correctable · without an alert: [[Ligustrazine (drug)]] 5 µM 0.0753× (z -9.3) |
| [[SW480 (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 5.67 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0737× (z -9.5) |
| [[BT-474 (line)]] | alt | 6.67 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0720× (z -8.7) |
| [[H4 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0718× (z -9.5) |
| [[KATO III (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.144× (z -9.9) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0733× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOR2]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SUN1]] | +0.66 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FGFR3]] | +0.63 | +0.58 / +0.46 | both halves | 3e-05 | same gene group; pathway: Signaling by FGFR |
| [[SBF1]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ACTN4]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[L1CAM]] | +0.61 | +0.40 / +0.61 | both halves | 5e-05 | same gene group |
| [[CYB5R3]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[GALNS]] | +0.60 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[INTS1]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[PLXNA3]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPCS]] | -0.54 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SLC16A14]] | -0.53 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[RNF135]] | -0.52 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ANKRD13C]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[COA6]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[C1orf131]] | -0.51 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[RPP38]] | -0.50 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SNW1]] | -0.50 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[SMAD1]] | -0.50 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEC]] | C | PLEC activity raises FGFRL1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.3, -4.7); signed map (-13.4, 34.7). **Vector** length 86.4, 17.5% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +10.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -4.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,009,936-1,026,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FGFR5 |
| Gene groups (HGNC) | I-set domain containing; Ig-like cell adhesion molecule family; Fibroblast growth factor receptor family |
| Reactome | 4 pathways, smallest: FGFRL1 modulation of FGFR1 signaling; Signaling by FGFR1; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N441](https://www.uniprot.org/uniprotkb/Q8N441) (Fibroblast growth factor receptor-like 1):

> Has a negative effect on cell proliferation.

**Summary**, from NCBI Gene [53834](https://www.ncbi.nlm.nih.gov/gene/53834):

> The protein encoded by this gene is a member of the fibroblast growth factor receptor (FGFR) family, where amino acid sequence is highly conserved between members and throughout evolution. FGFR family members differ from one another in their ligand affinities and tissue distribution. A full-length representative protein would consist of an extracellular region, composed of three immunoglobulin-like domains, a single hydrophobic membrane-spanning segment and a cytoplasmic tyrosine kinase domain. …

**Accessions** — [HGNC:3693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3693) · Entrez [53834](https://www.ncbi.nlm.nih.gov/gene/53834) · UniProt [Q8N441](https://www.uniprot.org/uniprotkb/Q8N441) · Ensembl [ENSG00000127418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127418)

## Data

Gene col 4807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4807); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4807]; `tensor/DDL_lfc|DDL_z.npy` [4807]; `embed/gene_vectors.npy` [4807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4807 or target_col == 4807). Every well: [[FGFRL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFRL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
