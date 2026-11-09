---
symbol: "SERPINB8"
type: "gene"
col: 9298
ensembl_id: "ENSG00000166401"
name: "serpin family B member 8"
location: "18q22.1"
module: 101
arm: "+"
pooled_cpm: 21.83
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 33
n_dd_up_clean: 7
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# SERPINB8

*serpin family B member 8* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.71× (z +6.1, q 8e-07, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.366× (z -11.7, q 7e-29, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP14-AS1]] (+0.73, fdr 7e-06), [[KRT8P12]] (+0.66, fdr 1e-05), [[LINC01204]] (+0.66, fdr 7e-06); moves opposite to [[PPP1R12B]] (-0.67, fdr 7e-06), [[KIAA2013]] (-0.61, fdr 1e-05), [[ZFP14]] (-0.60, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NIPAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +6.1 | 8e-07 | 27/45 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +5.3 | 4e-05 | 32/45 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 5e-05 | 27/45 (HS-578T, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.6 | 6e-04 | 22/46 (LOX-IMVI, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.017 | 20/45 (hTERT-HPNE, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.033 | 17/45 (HEC-1-A, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.065 | 21/46 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +3.2 | 0.090 | 14/46 (SHP-77, SNU-1, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.21× | +3.1 | 0.11 | 16/46 (HEC-1-A, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.65× | +3.1 | 0.11 | 13/44 (A-427, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.30× | +3.1 | 0.11 | 16/41 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 2 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -11.7 | 7e-29 | 45/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.371×** | -11.6 | 2e-28 | 44/46 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.405×** | -10.5 | 1e-23 | 41/46 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.469×** | -8.8 | 2e-16 | 39/45 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.484×** | -8.4 | 4e-15 | 36/46 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.552×** | -6.9 | 5e-10 | 36/46 (MIA PaCa-2, NCI-H23, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.632×** | -6.4 | 2e-08 | 30/46 (MIA PaCa-2, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.572×** | -6.3 | 3e-08 | 29/45 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.369×** | -6.1 | 8e-08 | 37/46 (SK-MEL-2, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.641×** | -5.9 | 3e-07 | 31/46 (SK-MEL-2, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.694×** | -5.8 | 3e-07 | 31/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.595×** | -5.8 | 3e-07 | 31/45 (HCT15, RKO, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.658×** | -5.7 | 4e-07 | 28/46 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.600×** | -5.5 | 2e-06 | 29/46 (NCI-H23, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.667×** | -5.5 | 2e-06 | 32/46 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 48.5 | 0 | 7 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.430× (z -20.0) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.145× (z -13.4) |
| [[BT-474 (line)]] | alt | 44.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0549× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.0916× (z -11.6) |
| [[LS 180 (line)]] | wt | 35.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 70.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.216× (z -10.5) |
| [[A549 (line)]] | wt | 22.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -9.5) |
| [[C32 (line)]] | wt | 13.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +9.2) | [[Radotinib (drug)]] 5 µM 0.171× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -13.2) |
| [[HS-578T (line)]] | alt | 20.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.7) | — |
| [[A498 (line)]] | wt | 8.77 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -8.8) |
| [[H4 (line)]] | wt | 47.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +12.6) | — |
| [[J82 (line)]] | alt | 45.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 39.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 38.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.192× (z -10.2) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.201× (z -8.6) |
| [[HOP62 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.583× (z -10.8) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.155× (z -9.2) |
| [[SW48 (line)]] | wt | 20.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0465× (z -12.6) |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP14-AS1]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[KRT8P12]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SOWAHC]] | +0.65 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[KHNYN]] | +0.65 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[BCAN-AS2]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BACH1]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[NIPAL1]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[EIF5]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[KIAA2013]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZFP14]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[STK38]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[NPEPPS]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.59 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[KLHDC10]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[DPM3]] | -0.58 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[MZT2B]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PHAF1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.58 | -0.67 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPAL1]] | B | NIPAL1 activity raises SERPINB8's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without NIPAL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises SERPINB8's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without SPRY4-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, -2.5); signed map (4.8, 33.3). **Vector** length 128, 37.5% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +7.1 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.9 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.4 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -8.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.0 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:63,970,029-64,019,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP2; previously PI8 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Dissolution of Fibrin Clot; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P50452](https://www.uniprot.org/uniprotkb/P50452) (Serpin B8):

> Has an important role in epithelial desmosome-mediated cell-cell adhesion.

**Summary**, from NCBI Gene [5271](https://www.ncbi.nlm.nih.gov/gene/5271):

> The protein encoded by this gene is a member of the ov-serpin family of serine protease inhibitors. The encoded protein is produced by platelets and can bind to and inhibit the function of furin, a serine protease involved in platelet functions. In addition, this protein has been found to enhance the mechanical stability of cell-cell adhesion in the skin, and defects in this gene have been associated with an autosomal-recessive form of exfoliative ichthyosis. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:8952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8952) · Entrez [5271](https://www.ncbi.nlm.nih.gov/gene/5271) · UniProt [P50452](https://www.uniprot.org/uniprotkb/P50452) · Ensembl [ENSG00000166401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166401)

## Data

Gene col 9298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9298); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9298]; `tensor/DDL_lfc|DDL_z.npy` [9298]; `embed/gene_vectors.npy` [9298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9298 or target_col == 9298). Every well: [[SERPINB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
