---
symbol: "SLC35A3"
type: "gene"
col: 3934
ensembl_id: "ENSG00000117620"
name: "solute carrier family 35 member A3"
location: "1p21.2"
module: 57
arm: "+"
pooled_cpm: 95.64
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SLC35A3

*solute carrier family 35 member A3* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.45× (z +4.0, q 0.043, up in 22 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -19.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP1]] (+0.70, fdr 2e-05), [[LONP2]] (+0.63, fdr 1e-05), [[ERP44]] (+0.63, fdr 2e-05); moves opposite to [[KDM6B]] (-0.63, fdr 4e-05), [[ERCC6L2]] (-0.62, fdr 2e-04), [[PLA2G4C]] (-0.62, fdr 8e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.043 | 22/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.14× | +3.7 | 0.054 | 7/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.14 | 3/48 (RKO, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -19.6 | 0e+00 | 42/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -16.1 | 0e+00 | 43/49 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -14.9 | 0e+00 | 42/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.542×** | -12.6 | 2e-34 | 47/48 (HT-29, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -8.8 | 1e-16 | 36/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -8.7 | 3e-16 | 35/50 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -8.7 | 4e-16 | 33/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.747×** | -8.5 | 1e-15 | 40/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -8.3 | 9e-15 | 34/48 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -8.1 | 4e-14 | 39/47 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -7.6 | 1e-12 | 32/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.727×** | -6.6 | 2e-09 | 33/48 (SNU-1, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.734×** | -6.4 | 7e-09 | 28/49 (SNU-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.739×** | -6.3 | 2e-08 | 32/48 (HOP62, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.750×** | -5.9 | 1e-07 | 30/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -4.1 | 0.001 | 24/49 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 278 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -17.5) |
| [[LoVo (line)]] | wt | 230 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -29.3) |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.3) |
| [[A-172 (line)]] | wt | 79.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -20.7) |
| [[HT-29 (line)]] | alt | 162 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -14.2) |
| [[Hs 766T (line)]] | wt | 164 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -20.7) |
| [[KATO III (line)]] | alt | 127 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.408× (z -10.2) |
| [[SNU-1 (line)]] | wt | 119 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -13.1) |
| [[A498 (line)]] | wt | 76.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.3) |
| [[HOP62 (line)]] | alt | 46.6 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -13.8) |
| [[HS-578T (line)]] | alt | 107 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 82.6 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.1) |
| [[J82 (line)]] | alt | 76.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -15.5) |
| [[SNU-423 (line)]] | alt | 61.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.5) |
| [[A-427 (line)]] | wt | 47.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 71.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 81.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.305× (z -11.3) |
| [[A549 (line)]] | wt | 56.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -10.6) |
| [[C32 (line)]] | wt | 42.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.2) |
| [[PANC-1 (line)]] | alt | 56.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -14.0) |
| [[BT-474 (line)]] | alt | 91.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.390× (z -9.6) |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.102× (z -8.5) |
| [[COLO 205 (line)]] | alt | 61.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 98.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.437× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 85.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[NCI-H23 (line)]] | alt | 51.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.322× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.4) |
| [[RKO (line)]] | wt | 90.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -9.3) |
| [[SHP-77 (line)]] | alt | 70.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -8.7) |
| [[SW48 (line)]] | wt | 92.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 78.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.484× (z -10.8) |
| [[AN3 CA (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | +0.70 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[LONP2]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ERP44]] | +0.63 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TAF5L]] | +0.63 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[MED23]] | +0.62 | +0.72 / +0.41 | both halves | 4e-05 |  |
| [[NUDT21]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[FAR1]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.61 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[AKTIP]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[EFCAB14]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.59 | +0.72 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM6B]] | -0.63 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.62 | -0.69 / -0.31 | both halves | 2e-04 |  |
| [[PLA2G4C]] | -0.62 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[SATB2]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[ZBED5]] | -0.61 | -0.64 / -0.39 | both halves | 6e-05 |  |
| [[PPP1R1C]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ST7L]] | -0.59 | -0.69 / -0.33 | both halves | 1e-04 |  |
| [[SON]] | -0.57 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[IGF2BP3]] | -0.57 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.56 | -0.64 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[LINC01762]] | -0.56 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[CREM]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ARHGAP15]] | -0.56 | -0.62 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC35A3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.4, -5.2); signed map (-38.1, -13.0). **Vector** length 107, 31.2% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +5.9 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -14.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:99,969,351-100,035,634 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 35 |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 6 pathways, smallest: Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D2](https://www.uniprot.org/uniprotkb/Q9Y2D2) (UDP-N-acetylglucosamine transporter):

> Transports diphosphate-N-acetylglucosamine (UDP-GlcNAc) from the cytosol into the lumen of the Golgi apparatus, functioning as an antiporter that exchanges UDP-N-acetyl-alpha-D-glucosamine for UMP. May supply UDP-GlcNAc as substrate for Golgi-resident glycosyltransferases that generate highly branched, multiantennary complex N-glycans and keratan sulfate. However, the exact role of SLC35A3 still needs to be elucidated, it could be a member of a catalytically more efficient multiprotein complex …

**Summary**, from NCBI Gene [23443](https://www.ncbi.nlm.nih.gov/gene/23443):

> This gene encodes a UDP-N-acetylglucosamine transporter found in the golgi apparatus membrane. In cattle, a missense mutation in this gene causes complex vertebral malformation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:11023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11023) · Entrez [23443](https://www.ncbi.nlm.nih.gov/gene/23443) · UniProt [Q9Y2D2](https://www.uniprot.org/uniprotkb/Q9Y2D2) · Ensembl [ENSG00000117620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117620)

## Data

Gene col 3934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3934); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3934]; `tensor/DDL_lfc|DDL_z.npy` [3934]; `embed/gene_vectors.npy` [3934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3934 or target_col == 3934). Every well: [[SLC35A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
