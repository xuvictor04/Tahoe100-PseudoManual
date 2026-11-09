---
symbol: "PPFIBP2"
type: "gene"
col: 9294
ensembl_id: "ENSG00000166387"
name: "PPFIB scaffold protein 2"
location: "11p15.4"
module: 44
arm: "+"
pooled_cpm: 13.82
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PPFIBP2

*PPFIB scaffold protein 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +15.6, q 0e+00, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.644× (z -6.8, q 6e-09, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC11A2]] (+0.64, fdr 8e-06), [[ANO9]] (+0.63, fdr 1e-05), [[PPM1H]] (+0.62, fdr 1e-05); moves opposite to [[PDK1-AS1]] (-0.55, fdr 1e-05), [[KANSL1L-AS1]] (-0.52, fdr 4e-05), [[ARPC5L]] (-0.52, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KSR2]] → it (grade B ⚠); 3 go from it, the strongest it → [[CGNL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +15.6 | 0e+00 | 29/40 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +10.8 | 2e-24 | 29/42 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +8.3 | 2e-14 | 25/40 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +7.7 | 2e-12 | 20/41 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +7.5 | 7e-12 | 21/41 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +7.3 | 3e-11 | 23/42 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +7.3 | 3e-11 | 21/42 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +5.5 | 2e-06 | 17/41 (HT-29, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.2 | 1e-05 | 17/42 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.1 | 2e-05 | 15/40 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.4 | 5e-04 | 13/41 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 8/41 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.008 | 9/41 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 5/41 (BT-474, A549, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.013 | 11/34 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -6.8 | 6e-09 | 21/41 (SNU-423, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -6.3 | 8e-08 | 20/41 (PANC-1, HT-29, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.667×** | -4.5 | 0.002 | 14/39 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.750×** | -4.3 | 0.003 | 10/41 (HT-29, RPMI-7951, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.619×** | -3.9 | 0.012 | 17/40 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.783×** | -3.8 | 0.014 | 12/42 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.648×** | -3.5 | 0.037 | 8/20 (HT-29, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 5 µM |  | 0.862× | -3.3 | 0.072 | 10/42 (H4, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.811×** | -3.3 | 0.072 | 9/42 (SW480, BT-474, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.815× | -3.0 | 0.15 | 6/41 (SHP-77, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.377× (z -8.7) |
| [[C32 (line)]] | wt | 9.84 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.113× (z -8.8) |
| [[Hs 766T (line)]] | wt | 8.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.246× (z -9.5) |
| [[J82 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +14.3) | — |
| [[LoVo (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 3.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.194× (z -10.0) |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0487× (z -10.1) |
| [[A-172 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC11A2]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[ANO9]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PPM1H]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MPP7]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PKDCC]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[AMOT]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ATP8B1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CGNL1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PER3]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SORL1]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TJP3]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK1-AS1]] | -0.55 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | -0.52 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[ARPC5L]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[GRPEL1]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[OSMR]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ARL16]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[OGFOD1]] | -0.48 | -0.39 / -0.36 | both halves | 1e-04 | STRING 415 |
| [[ERVK13-1]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PSMD14]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PSMD12]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[SFN]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF731P]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KSR2]] | B | KSR2 activity raises PPFIBP2's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without KSR2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PPFIBP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGNL1]] | B | PPFIBP2 activity lowers CGNL1's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 3.75× higher at baseline in the lines without PPFIBP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LRRC8D |
| [[CLCN5]] | B | PPFIBP2 activity raises CLCN5's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without PPFIBP2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC8D |
| [[NEO1]] | B | PPFIBP2 activity raises NEO1's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without PPFIBP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC8D |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, 46.6); signed map (51.4, 3.1). **Vector** length 72.0, 12.9% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +15.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +5.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.8 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PPFIB scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:7,513,298-7,657,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cclp1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PPFI scaffold protein family |
| Reactome | 3 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND30](https://www.uniprot.org/uniprotkb/Q8ND30) (Liprin-beta-2):

> May regulate the disassembly of focal adhesions. Did not bind receptor-like tyrosine phosphatases type 2A.

**Summary**, from NCBI Gene [8495](https://www.ncbi.nlm.nih.gov/gene/8495):

> This gene encodes a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. The encoded protein is a beta liprin and plays a role in axon guidance and neuronal synapse development by recruiting LAR protein-tyrosine phosphatases to the plasma membrane. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:9250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9250) · Entrez [8495](https://www.ncbi.nlm.nih.gov/gene/8495) · UniProt [Q8ND30](https://www.uniprot.org/uniprotkb/Q8ND30) · Ensembl [ENSG00000166387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166387)

## Data

Gene col 9294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9294); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9294]; `tensor/DDL_lfc|DDL_z.npy` [9294]; `embed/gene_vectors.npy` [9294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9294 or target_col == 9294). Every well: [[PPFIBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
