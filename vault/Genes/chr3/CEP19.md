---
symbol: "CEP19"
type: "gene"
col: 10452
ensembl_id: "ENSG00000174007"
name: "centrosomal protein 19"
location: "3q29"
module: 16
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CEP19

*centrosomal protein 19* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +11.8, q 2e-29, up in 24 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.461× (z -5.3, q 5e-05, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO48]] (+0.61, fdr 7e-06), [[TRMT1L]] (+0.60, fdr 7e-06), [[SLC2A6]] (+0.57, fdr 1e-05); moves opposite to [[ZNF749]] (-0.55, fdr 3e-05), [[MTFR1]] (-0.52, fdr 4e-05), [[THOC5]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +11.8 | 2e-29 | 24/27 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **4.88×** | +10.4 | 5e-23 | 1/2 (PANC-1) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.33×** | +10.0 | 2e-21 | 42/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.12×** | +9.7 | 5e-20 | 35/39 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.67×** | +8.9 | 7e-17 | 10/10 (A-172, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.43×** | +8.4 | 3e-15 | 37/40 (PANC-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +7.3 | 2e-11 | 16/30 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.90×** | +6.7 | 1e-09 | 3/4 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +6.6 | 2e-09 | 21/39 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +5.0 | 3e-05 | 15/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +4.7 | 2e-04 | 11/26 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 6/45 (A-172, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +3.9 | 0.004 | 2/12 (A-172, SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.79×** | +3.7 | 0.009 | 5/32 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.013 | 6/44 (SW480, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +3.6 | 0.013 | 12/42 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.022 | 8/44 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.049 | 8/27 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.063 | 2/40 (SW480, C-33 A) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -5.3 | 5e-05 | 21/41 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -5.2 | 5e-05 | 22/46 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -4.1 | 0.008 | 19/36 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.390× | -3.4 | 0.11 | 13/33 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.729× | -3.0 | 0.21 | 9/41 (RKO, C32, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.730× | -3.0 | 0.21 | 7/47 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.429× | -3.0 | 0.21 | 7/24 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0986× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO48]] | +0.61 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.60 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SLC2A6]] | +0.57 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[EID2]] | +0.57 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.56 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DENND3-AS1]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[USP27X]] | +0.55 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.54 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[C7orf25]] | +0.54 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[METTL18]] | +0.53 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF749]] | -0.55 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[MTFR1]] | -0.52 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[THOC5]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.51 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.51 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[LENG8]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RER1]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SPTLC1]] | -0.50 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ZNF587B]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DCAF13]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R32]] | -0.49 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[TIMM10B]] | -0.49 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CEP19's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | CEP19's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.478 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.442). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.9, 19.3); signed map (5.0, -16.5). **Vector** length 42.4, 5.46% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.8 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.5 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.6 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Pentagastrin (drug)]] 5 µM |  | -0.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,706,277-196,712,250 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14126; previously C3orf34 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LK0](https://www.uniprot.org/uniprotkb/Q96LK0) (Centrosomal protein of 19 kDa):

> Required for ciliation. Recruits the RABL2B GTPase to the ciliary base to initiate ciliation. After specifically capturing the activated GTP-bound RABL2B, the CEP19-RABL2B complex binds intraflagellar transport (IFT) complex B from the large pool pre-docked at the base of the cilium and thus triggers its entry into the cilia. Involved in the early steps in cilia formation by recruiting the ciliary vesicles (CVs) to the distal end of the mother centriole where they fuse to initiate cilium …

**Summary**, from NCBI Gene [84984](https://www.ncbi.nlm.nih.gov/gene/84984):

> The protein encoded by this gene localizes to centrosomes and primary cilia and co-localizes with a marker for the mother centriole. This gene resides in a region of human chromosome 3 that is linked to morbid obesity. A homozygous knockout of the orthologous gene in mouse resulted in mice with morbid obesity, hyperphagy, glucose intolerance, and insulin resistance. Mutations in this gene cause morbid obesity and spermatogenic failure (MOSPGF). This gene has a pseudogene on human chromosome 2. …

**Accessions** — [HGNC:28209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28209) · Entrez [84984](https://www.ncbi.nlm.nih.gov/gene/84984) · UniProt [Q96LK0](https://www.uniprot.org/uniprotkb/Q96LK0) · Ensembl [ENSG00000174007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174007)

## Data

Gene col 10452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10452); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10452]; `tensor/DDL_lfc|DDL_z.npy` [10452]; `embed/gene_vectors.npy` [10452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10452 or target_col == 10452). Every well: [[CEP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
