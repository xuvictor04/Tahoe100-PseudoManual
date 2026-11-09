---
symbol: "LNP1"
type: "gene"
col: 13047
ensembl_id: "ENSG00000206535"
name: "leukemia NUP98 fusion partner 1"
location: "3q12.2"
module: 38
arm: "+"
pooled_cpm: 5.97
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# LNP1

*leukemia NUP98 fusion partner 1* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.39× (z +28.1, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.601× (z -6.3, q 1e-07, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP2BP]] (+0.75, fdr 7e-06), [[PELO-AS1]] (+0.71, fdr 7e-06), [[SLC9A5]] (+0.70, fdr 1e-05); moves opposite to [[COMMD2]] (-0.63, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPHA1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.39×** | +28.1 | 0e+00 | 40/40 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +13.9 | 2e-41 | 31/38 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +11.3 | 4e-27 | 27/35 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +10.5 | 1e-23 | 27/40 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +10.3 | 6e-23 | 25/41 (HOP62, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +9.3 | 9e-19 | 22/38 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +7.5 | 5e-12 | 22/46 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +7.1 | 1e-10 | 24/46 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.2 | 4e-08 | 14/46 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 2e-07 | 17/46 (HOP62, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.7 | 6e-07 | 10/15 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.2 | 1e-05 | 16/45 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.0 | 2e-05 | 17/44 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 6e-04 | 12/41 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.41×** | +4.2 | 9e-04 | 5/24 (LoVo, CFPAC-1, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 2/46 (SW480, A-172) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.011 | 11/39 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -6.3 | 1e-07 | 21/44 (A-427, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -5.0 | 2e-04 | 18/44 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.8 | 3e-04 | 8/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -4.3 | 0.002 | 13/42 (Hs 766T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.751×** | -3.6 | 0.041 | 11/40 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.072 | 14/42 (A549, SK-MEL-2, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.601×** | -3.3 | 0.077 | 7/27 (SK-MEL-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | 0.774× | -3.2 | 0.10 | 9/40 (C32, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +11.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.293× (z -8.5) |
| [[HS-578T (line)]] | alt | 6.91 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 7.83 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.4) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0770× (z -10.1) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.150× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 2 | — | [[Monocrotaline (drug)]] 5 µM 0.0696× (z -9.8) |
| [[HOP62 (line)]] | alt | 8.01 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.00× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.12 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +8.8) | [[Aprepitant (drug)]] 0.5 µM 0.0509× (z -9.4) |
| [[RKO (line)]] | wt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0897× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 11.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.3) | — |
| [[A498 (line)]] | wt | 6.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 3.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.3) | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP2BP]] | +0.75 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PELO-AS1]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.70 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[ARL9]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[C17orf100]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.63 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity lowers LNP1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without EPHA1-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LNP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises LNP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, -17.8); signed map (14.1, 6.5). **Vector** length 69.4, 11.1% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +28.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.5 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | leukemia NUP98 fusion partner 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,401,532-100,456,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NP3 |
| Matched by | ensembl_id |

UniProt [A1A4G5](https://www.uniprot.org/uniprotkb/A1A4G5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28014) · Entrez [348801](https://www.ncbi.nlm.nih.gov/gene/348801) · UniProt [A1A4G5](https://www.uniprot.org/uniprotkb/A1A4G5) · Ensembl [ENSG00000206535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206535)

## Data

Gene col 13047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13047); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13047]; `tensor/DDL_lfc|DDL_z.npy` [13047]; `embed/gene_vectors.npy` [13047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13047 or target_col == 13047). Every well: [[LNP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
