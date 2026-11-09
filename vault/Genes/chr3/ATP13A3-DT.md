---
symbol: "ATP13A3-DT"
type: "gene"
col: 13885
ensembl_id: "ENSG00000233058"
name: "ATP13A3 divergent transcript"
location: "3q29"
module: 101
arm: "+"
pooled_cpm: 6.7
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ATP13A3-DT

*ATP13A3 divergent transcript* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.49× (z +27.8, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.378× (z -9.5, q 1e-18, down in 24 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMAL2-AS1]] (+0.66, fdr 1e-05), [[HBEGF]] (+0.60, fdr 2e-05), [[ITGA2-AS1]] (+0.59, fdr 1e-05); moves opposite to [[LSM14B]] (-0.57, fdr 2e-05), [[MED25]] (-0.50, fdr 2e-05), [[IFT122]] (-0.48, fdr 4e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.49×** | +27.8 | 0e+00 | 29/29 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.59×** | +14.9 | 0e+00 | 31/35 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.80×** | +14.2 | 1e-43 | 32/35 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.77×** | +13.0 | 3e-36 | 28/34 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.21×** | +11.4 | 5e-28 | 27/31 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.17×** | +11.3 | 2e-27 | 29/34 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +10.7 | 7e-25 | 13/24 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.0 | 2e-17 | 4/18 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.78×** | +8.6 | 4e-16 | 30/35 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.4 | 2e-15 | 2/9 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +8.3 | 5e-15 | 15/29 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +7.1 | 8e-11 | 4/12 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +6.7 | 7e-10 | 17/32 (AsPC-1, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.6 | 1e-09 | 16/35 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +5.3 | 4e-06 | 13/34 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +4.2 | 0.001 | 10/31 (KATO III, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.003 | 12/29 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.045 | 9/34 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -9.5 | 1e-18 | 24/35 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -8.7 | 1e-15 | 24/33 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.483×** | -7.1 | 2e-10 | 20/32 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -4.9 | 1e-04 | 19/35 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -4.5 | 8e-04 | 20/27 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.666×** | -4.0 | 0.007 | 8/35 (PANC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.632×** | -3.9 | 0.009 | 13/32 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.664×** | -3.5 | 0.038 | 15/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.731× | -3.1 | 0.13 | 10/34 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.733× | -3.0 | 0.13 | 11/35 (J82, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0599× (z -20.6) |
| [[KATO III (line)]] | alt | 15.5 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.12× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.139× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.207× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 41.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -12.1) |
| [[SW480 (line)]] | alt | 3.38 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.62× (z +12.7) | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -9.6) |
| [[A-172 (line)]] | wt | 3.06 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.3× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 4.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +9.8) | [[Digitoxin (drug)]] 0.05 µM 0.0358× (z -11.9) |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0391× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 4.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.36× (z +9.2) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 3.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +9.3) | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +10.0) | — |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMAL2-AS1]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ITGA2-AS1]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HCG20]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ASIC2]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[STARD13-AS]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NABP1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[C11orf91]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[DELEC1]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF385D]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MED25]] | -0.50 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[IFT122]] | -0.48 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP13A3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF385D]] | B | ZNF385D activity raises ATP13A3-DT's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.58× lower at baseline in the lines without ZNF385D | 0.084 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, -4.5); signed map (3.3, 31.3). **Vector** length 64.5, 12.5% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +27.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ATP13A3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q29 — chr3:194,487,140-194,521,156 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00884 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48570) · Entrez [401106](https://www.ncbi.nlm.nih.gov/gene/401106) · Ensembl [ENSG00000233058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233058)

## Data

Gene col 13885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13885); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13885]; `tensor/DDL_lfc|DDL_z.npy` [13885]; `embed/gene_vectors.npy` [13885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13885 or target_col == 13885). Every well: [[ATP13A3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP13A3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
