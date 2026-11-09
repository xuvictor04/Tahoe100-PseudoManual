---
symbol: "THOC7"
type: "gene"
col: 8739
ensembl_id: "ENSG00000163634"
name: "THO complex subunit 7"
location: "3p14.1"
module: 88
arm: "+"
pooled_cpm: 42.91
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# THOC7

*THO complex subunit 7* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.36× (z +12.9, q 2e-35, up in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.62× (z +5.1, q 4e-05, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.452× (z -8.4, q 2e-14, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AASDHPPT]] (+0.73, fdr 7e-06), [[KRCC1]] (+0.71, fdr 7e-06), [[CCAR1]] (+0.70, fdr 7e-06); moves opposite to [[IGSF8]] (-0.72, fdr 7e-06), [[ADIPOR1]] (-0.69, fdr 1e-05), [[SDF2]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +12.9 | 2e-35 | 45/46 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +12.0 | 2e-30 | 38/38 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +7.3 | 7e-11 | 36/41 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 4e-05 | 39/48 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.45×** | +4.0 | 0.008 | 33/47 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +3.8 | 0.016 | 29/48 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.43×** | +3.7 | 0.017 | 27/48 (HOP62, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.018 | 31/48 (LoVo, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.096 | 21/47 (NCI-H460, A549, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -8.4 | 2e-14 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -7.1 | 3e-10 | 44/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -7.1 | 3e-10 | 41/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -5.0 | 7e-05 | 35/48 (A-427, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -4.4 | 0.001 | 36/48 (SW 1088, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -4.2 | 0.003 | 30/47 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -3.9 | 0.008 | 26/47 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -3.6 | 0.019 | 28/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.799×** | -3.3 | 0.053 | 21/48 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.554×** | -3.3 | 0.061 | 27/47 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.095 | 24/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.267× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.6) |
| [[A498 (line)]] | wt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +12.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 50.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.5) |
| [[KATO III (line)]] | alt | 45.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.243× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 44.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +12.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.354× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 58.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.8) |
| [[PANC-1 (line)]] | alt | 44.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 48.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 45.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 41.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.8) |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | +0.73 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CCAR1]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TIMMDC1]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[UBE3A]] | +0.68 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[COQ5]] | +0.67 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ATRX]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[RAD50]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[GABPB2]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZFR]] | +0.65 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.65 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R9A]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | -0.72 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[ADIPOR1]] | -0.69 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[SDF2]] | -0.67 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[AP1S1]] | -0.65 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[CABLES2]] | -0.65 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TMEM104]] | -0.65 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.64 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TPST2]] | -0.64 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.63 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CD81]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TPRG1L]] | -0.62 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises THOC7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-21.6, 7.9); signed map (13.1, -26.5). **Vector** length 66.8, 16.9% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | +1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.1 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:63,833,870-63,863,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIF3L1BP1, FLJ23445, fSAP24 |
| Gene groups (HGNC) | THO complex |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6I9Y2](https://www.uniprot.org/uniprotkb/Q6I9Y2) (THO complex subunit 7):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Required for efficient export of polyadenylated RNA. Plays a key structural role in the oligomerization of the THO-DDX39B complex. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream of the exon-junction complex (EJC) and is recruited …

**Summary**, from NCBI Gene [80145](https://www.ncbi.nlm.nih.gov/gene/80145):

> Predicted to enable RNA binding activity. Involved in mRNA export from nucleus. Located in chromosome, telomeric region; cytosol; and nuclear speck. Part of THO complex part of transcription export complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29874) · Entrez [80145](https://www.ncbi.nlm.nih.gov/gene/80145) · UniProt [Q6I9Y2](https://www.uniprot.org/uniprotkb/Q6I9Y2) · Ensembl [ENSG00000163634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163634)

## Data

Gene col 8739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8739); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8739]; `tensor/DDL_lfc|DDL_z.npy` [8739]; `embed/gene_vectors.npy` [8739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8739 or target_col == 8739). Every well: [[THOC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
