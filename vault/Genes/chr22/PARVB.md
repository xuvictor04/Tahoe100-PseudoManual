---
symbol: "PARVB"
type: "gene"
col: 12038
ensembl_id: "ENSG00000188677"
name: "parvin beta"
location: "22q13.31"
module: 110
arm: "+"
pooled_cpm: 55.67
n_lines_expressing: 37
n_dd_up: 3
n_dd_down: 34
n_dd_up_clean: 2
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 8
direction_downstream: 18
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# PARVB

*parvin beta* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.28× (z +5.6, q 2e-05, up in 19 of 35 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.17× (z +5.0, q 1e-04, up in 13 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.307× (z -38.0, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARVG]] (+0.73, fdr 7e-06, ⚠ read-through risk), [[ARHGAP22]] (+0.62, fdr 1e-05), [[PYGL]] (+0.61, fdr 7e-06), [[XPO6]] (+0.59, fdr 1e-05); moves opposite to [[ADD3]] (-0.57, fdr 1e-05), [[DLEU1]] (-0.54, fdr 3e-05), [[MTUS1]] (-0.51, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LEF1-AS1]] → it (grade B ⚠); 18 go from it, the strongest it → [[NBPF15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +5.6 | 2e-05 | 19/35 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +5.0 | 1e-04 | 13/36 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.038 | 8/33 (NCI-H460, J82, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.038 | 6/34 (BT-474, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.038 | 9/35 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.043 | 7/35 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.4 | 0.058 | 10/35 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.11 | 7/34 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.11 | 3/35 (A-427, SW 900, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.13 | 1/35 (HOP62) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.307×** | -38.0 | 0e+00 | 32/34 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -18.3 | 0e+00 | 28/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.463×** | -17.5 | 0e+00 | 28/35 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.476×** | -16.9 | 0e+00 | 29/35 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.479×** | -16.8 | 0e+00 | 28/35 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -15.5 | 0e+00 | 27/34 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -13.8 | 3e-41 | 26/34 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.541×** | -13.5 | 2e-39 | 29/35 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.299×** | -13.2 | 1e-37 | 31/36 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.603×** | -11.5 | 7e-29 | 26/33 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -10.0 | 7e-22 | 25/35 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -9.4 | 4e-19 | 28/35 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -9.3 | 5e-19 | 21/35 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -9.1 | 4e-18 | 26/35 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.674×** | -9.0 | 1e-17 | 20/35 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -8.1 | 2e-14 | 23/34 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.0 | 6e-11 | 19/33 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -7.0 | 8e-11 | 20/35 (C32, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 541 | 0 | 35 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -52.6) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.3) |
| [[LOX-IMVI (line)]] | wt | 90.6 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -22.3) |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -28.8) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -26.7) |
| [[PANC-1 (line)]] | alt | 76.3 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -25.8) |
| [[SW480 (line)]] | alt | 133 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -34.7) |
| [[HOP62 (line)]] | alt | 53.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 74.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.9) |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 7 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.210× (z -12.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.4) |
| [[J82 (line)]] | alt | 34.3 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 78.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -20.2) |
| [[RKO (line)]] | wt | 71.8 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -12.0) |
| [[SHP-77 (line)]] | alt | 89.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.6) |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.4) |
| [[H4 (line)]] | wt | 86.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.8) |
| [[LoVo (line)]] | wt | 38.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.2) |
| [[A-427 (line)]] | wt | 37.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.3) |
| [[Hs 766T (line)]] | wt | 80.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 46.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.3) |
| [[HS-578T (line)]] | alt | 55.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.0) |
| [[A549 (line)]] | wt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.1) |
| [[NCI-H460 (line)]] | wt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.8) |
| [[A498 (line)]] | wt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.9) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.0) |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.3) |
| [[A-172 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVG]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; STRING 914; ⚠ **readthrough risk**: PARVG lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ARHGAP22]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PYGL]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[XPO6]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LINC01812]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[KIAA1549L]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.57 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[NBPF8]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NHSL1-AS1]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RHBDF2]] | +0.56 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[AKAP12]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MSRB3-AS1]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADD3]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DLEU1]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MTUS1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MBNL2]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RBM47]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HNMT]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ATP1B1]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[FAAH2]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[DNAH7]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[BMF]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CDKN1B]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1-AS1]] | B | LEF1-AS1 activity raises PARVB's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without LEF1-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[ERBB3]] | B | ERBB3 activity lowers PARVB's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.08× higher at baseline in the lines without ERBB3 | 0.038 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[FAAH2]] | B | FAAH2 activity lowers PARVB's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.11× higher at baseline in the lines without FAAH2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises PARVB's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without HS3ST3A1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[ZEB1]] | B | ZEB1 activity raises PARVB's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 3.21× lower at baseline in the lines without ZEB1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[OCLN]] | B | OCLN activity lowers PARVB's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.27× higher at baseline in the lines without OCLN | 0.079 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[RASA3]] | B | RASA3 activity raises PARVB's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without RASA3 | 0.083 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PARVG]] | C | PARVG activity raises PARVB's level | lines that do not express PARVG (15) vs lines expressing it (35) | 5.62× lower at baseline in the lines without PARVG | 2e-04 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBPF15]] | B | PARVB activity raises NBPF15's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PARVB | 0.009 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[OCLN]] | B | PARVB activity lowers OCLN's level | lines that do not express PARVB (13) vs lines expressing it (37) | 4.10× higher at baseline in the lines without PARVB | 0.015 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[NBPF8]] | B | PARVB activity raises NBPF8's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without PARVB | 0.015 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[ST3GAL3]] | B | PARVB activity raises ST3GAL3's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without PARVB | 0.021 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[NBPF20]] | B | PARVB activity raises NBPF20's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without PARVB | 0.037 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[FAAH2]] | B | PARVB activity lowers FAAH2's level | lines that do not express PARVB (13) vs lines expressing it (37) | 4.65× higher at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[ZNG1F]] | B | PARVB activity raises ZNG1F's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.13× lower at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[TANGO6]] | B | PARVB activity raises TANGO6's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[POLR3G]] | B | PARVB activity raises POLR3G's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without PARVB | 0.047 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[PLGRKT]] | B | PARVB activity raises PLGRKT's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without PARVB | 0.049 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[NBPF9]] | B | PARVB activity raises NBPF9's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without PARVB | 0.049 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[OCLN]] | B | PARVB activity weakens OCLN's drug response | lines that do not express PARVB (11) vs lines expressing it (19) | the lines without PARVB respond 3.09× as strongly (z diff -4.11); strongest at Homoharringtonine 5 µM: 0.41x vs 0.92x (z diff -6.6) | 0.052 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.7, 4.6); signed map (14.4, 49.1). **Vector** length 106, 29.6% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | +3.8 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -13.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -5.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | parvin beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:43,999,211-44,172,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-56 |
| Gene groups (HGNC) | Parvins; ILK-PINCH-Parvin complex subunits |
| Reactome | 4 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Cell-extracellular matrix interactions; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBI1](https://www.uniprot.org/uniprotkb/Q9HBI1) (Beta-parvin):

> Adapter protein that plays a role in integrin signaling via ILK and in activation of the GTPases CDC42 and RAC1 by guanine exchange factors, such as ARHGEF6. Is involved in the reorganization of the actin cytoskeleton and formation of lamellipodia. Plays a role in cell adhesion, cell spreading, establishment or maintenance of cell polarity, and cell migration.

**Summary**, from NCBI Gene [29780](https://www.ncbi.nlm.nih.gov/gene/29780):

> This gene encodes a member of the parvin family of actin-binding proteins, which play a role in cytoskeleton organization and cell adhesion. These proteins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. This family member binds to alphaPIX and alpha-actinin, and it can inhibit the activity of integrin-linked kinase. This protein also functions in tumor suppression. Alternative splicing of this gene results in multiple transcript variants. …

**Accessions** — [HGNC:14653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14653) · Entrez [29780](https://www.ncbi.nlm.nih.gov/gene/29780) · UniProt [Q9HBI1](https://www.uniprot.org/uniprotkb/Q9HBI1) · Ensembl [ENSG00000188677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188677)

## Data

Gene col 12038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12038); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12038]; `tensor/DDL_lfc|DDL_z.npy` [12038]; `embed/gene_vectors.npy` [12038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12038 or target_col == 12038). Every well: [[PARVB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARVB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
