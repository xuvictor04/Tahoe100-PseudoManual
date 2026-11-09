---
symbol: "ARHGEF26-AS1"
type: "gene"
col: 14339
ensembl_id: "ENSG00000243069"
name: "ARHGEF26 antisense RNA 1"
location: "3q25.2"
module: 150
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 43
n_dd_up: 45
n_dd_down: 13
n_dd_up_clean: 35
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# ARHGEF26-AS1

*ARHGEF26 antisense RNA 1* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.95× (z +22.1, q 0e+00, up in 25 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.672× (z -4.9, q 4e-04, down in 14 of 35 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL2]] (+0.62, fdr 1e-05), [[BRINP3]] (+0.61, fdr 2e-05), [[LINC01122]] (+0.59, fdr 1e-05); moves opposite to [[RNF34]] (-0.48, fdr 8e-04, ⚠ not reproduced).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.95×** | +22.1 | 0e+00 | 25/29 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.77×** | +15.3 | 0e+00 | 36/40 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.51×** | +13.2 | 2e-37 | 35/37 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +11.6 | 4e-29 | 20/31 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.43×** | +10.8 | 4e-25 | 32/40 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +10.8 | 5e-25 | 19/25 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.40×** | +10.7 | 8e-25 | 33/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.29×** | +10.4 | 1e-23 | 19/33 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.09×** | +9.1 | 5e-18 | 27/38 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.0 | 5e-14 | 20/31 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.38×** | +7.6 | 2e-12 | 22/38 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.60×** | +7.0 | 1e-10 | 22/33 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +6.9 | 3e-10 | 3/6 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +6.5 | 3e-09 | 18/33 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +6.3 | 8e-09 | 13/29 (NCI-H1792, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 8e-06 | 16/32 (NCI-H2347, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.672×** | -4.9 | 4e-04 | 14/35 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.584×** | -4.7 | 7e-04 | 15/33 (C-33 A, PANC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.592×** | -4.4 | 0.002 | 12/34 (PANC-1, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -3.9 | 0.014 | 8/32 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -3.8 | 0.014 | 14/25 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.652×** | -3.8 | 0.016 | 12/39 (NCI-H23, A-427, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -3.6 | 0.027 | 15/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.668×** | -3.5 | 0.027 | 12/39 (LOX-IMVI, PANC-1, …) | all doses, flat | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.670×** | -3.4 | 0.044 | 6/38 (SW480, NCI-H661, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.689×** | -3.3 | 0.060 | 6/40 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -3.2 | 0.069 | 13/33 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.697×** | -3.2 | 0.069 | 7/40 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.692×** | -3.1 | 0.081 | 4/38 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 6.79 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 2.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 7.78 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.73× (z +8.5) | [[Bendamustine (drug)]] 5 µM 0.0664× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 3.86 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +9.4) | [[Digitoxin (drug)]] 0.5 µM 0.0599× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.60× (z +8.6) | — |
| [[J82 (line)]] | alt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 1.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.16 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.99× (z +8.5) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0403× (z -11.6) |
| [[SW 900 (line)]] | alt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.894 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL2]] | +0.62 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[BRINP3]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LINC01122]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[EFHD1]] | +0.58 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[LINC02006]] | +0.56 | +0.65 / +0.54 | both halves | 1e-05 | ⚠ same locus (44.2 kb, same strand: neighbours can correlate without regulation) |
| [[MAPK10]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[PCDHA6]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[PCDH11X]] | +0.55 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[LINC02208]] | +0.54 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PRKCH]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[PDE8B]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[BEND6]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MYO16]] | +0.53 | +0.65 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF34]] | -0.48 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARHGEF26-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH2]] | B | ALDH2 activity strengthens ARHGEF26-AS1's drug response | lines that do not express ALDH2 (8) vs lines expressing it (32) | the lines without ALDH2 respond 0.90× as strongly (z diff +0.74); strongest at Idarubicin (hydrochloride) 5 µM: 2.47x vs 6.67x (z diff +4.2) | 0.086 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.5, 33.4); signed map (38.5, 17.0). **Vector** length 49.2, 7.48% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +22.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +5.2 |
| fall | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -4.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ARHGEF26 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.2 — chr3:154,024,401-154,121,347 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41048) · Entrez [100507524](https://www.ncbi.nlm.nih.gov/gene/100507524) · Ensembl [ENSG00000243069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243069)

## Data

Gene col 14339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14339); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14339]; `tensor/DDL_lfc|DDL_z.npy` [14339]; `embed/gene_vectors.npy` [14339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14339 or target_col == 14339). Every well: [[ARHGEF26-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF26-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
