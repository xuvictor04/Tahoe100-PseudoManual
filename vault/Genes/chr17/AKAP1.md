---
symbol: "AKAP1"
type: "gene"
col: 4247
ensembl_id: "ENSG00000121057"
name: "A-kinase anchoring protein 1"
location: "17q22"
module: 33
arm: "+"
pooled_cpm: 31.1
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# AKAP1

*A-kinase anchoring protein 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 1.49× (z +8.2, q 2e-13, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.570× (z -16.7, q 0e+00, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88C]] (+0.65, fdr 7e-06), [[UCK2]] (+0.63, fdr 7e-06), [[PPARGC1B]] (+0.62, fdr 7e-06); moves opposite to [[NFU1]] (-0.53, fdr 2e-05), [[BBIP1]] (-0.52, fdr 3e-05), [[SPAG5-AS1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MEST]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +8.2 | 2e-13 | 28/47 (NCI-H1792, NCI-H2347, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +7.8 | 2e-12 | 27/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.6 | 6e-12 | 27/45 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +7.2 | 1e-10 | 27/46 (NCI-H23, RKO, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +7.1 | 1e-10 | 22/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +6.2 | 5e-08 | 22/47 (COLO 205, J82, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.9 | 3e-07 | 21/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.32×** | +5.6 | 1e-06 | 17/46 (C32, HOP62, …) | two highest doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 5e-06 | 21/46 (BT-474, A498, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 20/48 (A549, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +5.1 | 2e-05 | 16/47 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.1 | 2e-05 | 22/48 (A-427, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +4.8 | 6e-05 | 15/48 (A549, J82, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +4.5 | 3e-04 | 13/42 (A-172, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 7e-04 | 10/45 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 12/48 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 6/48 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.024 | 6/42 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.035 | 9/47 (A498, HOP62, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.083 | 3/47 (A-172, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -16.7 | 0e+00 | 34/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.457×** | -16.0 | 0e+00 | 35/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -10.1 | 1e-21 | 32/46 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -9.9 | 7e-21 | 34/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -8.8 | 2e-16 | 29/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -8.6 | 8e-16 | 30/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.705×** | -7.5 | 6e-12 | 24/47 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -7.5 | 6e-12 | 27/47 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -6.3 | 2e-08 | 25/48 (LS 180, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -5.0 | 4e-05 | 20/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.833× | -3.9 | 0.005 | 21/47 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.8 | 0.006 | 17/41 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.4 | 0.028 | 17/47 (HepG2/C3A, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 44.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.3) |
| [[SW480 (line)]] | alt | 50.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -21.2) |
| [[LS 180 (line)]] | wt | 68.3 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.307× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -14.4) |
| [[PANC-1 (line)]] | alt | 37.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.1) |
| [[A549 (line)]] | wt | 27.6 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.0) |
| [[KATO III (line)]] | alt | 101 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.318× (z -11.5) |
| [[LoVo (line)]] | wt | 79.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.8) |
| [[A-427 (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -10.1) |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0651× (z -10.2) |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0842× (z -18.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -21.9) |
| [[RKO (line)]] | wt | 27.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.226× (z -9.5) |
| [[A-172 (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -12.2) |
| [[H4 (line)]] | wt | 14.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0829× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.139× (z -8.9) ⚠ transcription drop; unreliable plate only |
| [[SHP-77 (line)]] | alt | 32.3 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0838× (z -9.1) |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.0) |
| [[A498 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88C]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[UCK2]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PPARGC1B]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[AHCTF1]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[TBC1D14]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DKC1]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[EXOSC5]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MDN1]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ASB13]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[WDR43]] | +0.59 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFU1]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[BBIP1]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SPAG5-AS1]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SELENOK]] | -0.51 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[CREM]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[WDR26]] | -0.48 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CALCRL-AS1]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ENSA]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEST]] | B | MEST activity raises AKAP1's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without MEST | 0.032 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[HSD11B2]] | B | HSD11B2 activity raises AKAP1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without HSD11B2 | 0.052 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[CCDC88C]] | B | CCDC88C activity raises AKAP1's level | lines that do not express CCDC88C (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without CCDC88C | 0.086 | ⚠ within organs, on part of the lines; also absent: SPTBN2, NUP210, NOXA1 |
| [[GPD1L]] | C | GPD1L activity raises AKAP1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without GPD1L | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.3, -39.1); signed map (-6.2, -52.7). **Vector** length 109, 27.2% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.3 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.2 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | +1.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:57,085,092-57,121,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKAP121, AKAP149, SAKAP84, S-AKAP84, AKAP84, D-AKAP1, PPP1R43, TDRD17; previously PRKA1 |
| Gene groups (HGNC) | A-kinase anchoring proteins; Protein phosphatase 1 regulatory subunits; Tudor domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Mitochondrial calcium ion transport; Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92667](https://www.uniprot.org/uniprotkb/Q92667) (A-kinase anchor protein 1, mitochondrial):

> Binds to type I and II regulatory subunits of protein kinase A and anchors them to the cytoplasmic face of the mitochondrial outer membrane (By similarity). Involved in mitochondrial-mediated antiviral innate immunity. Promotes translocation of NDUFS1 into mitochondria to regulate mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) activity (By similarity).

**Summary**, from NCBI Gene [8165](https://www.ncbi.nlm.nih.gov/gene/8165):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein binds to type I and type II regulatory subunits of PKA and anchors them to the mitochondrion. This protein is speculated to be involved in the cAMP-dependent signal transduction pathway …

**Accessions** — [HGNC:367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:367) · Entrez [8165](https://www.ncbi.nlm.nih.gov/gene/8165) · UniProt [Q92667](https://www.uniprot.org/uniprotkb/Q92667) · Ensembl [ENSG00000121057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121057)

## Data

Gene col 4247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4247); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4247]; `tensor/DDL_lfc|DDL_z.npy` [4247]; `embed/gene_vectors.npy` [4247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4247 or target_col == 4247). Every well: [[AKAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
