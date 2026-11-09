---
symbol: "CRYGS"
type: "gene"
col: 13084
ensembl_id: "ENSG00000213139"
name: "crystallin gamma S"
location: "3q27.3"
module: 37
arm: "+"
pooled_cpm: 5.15
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CRYGS

*crystallin gamma S* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +13.8, q 2e-40, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.509× (z -6.1, q 8e-07, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCCD1]] (+0.69, fdr 7e-06, ⚠ same locus), [[DNAJC9]] (+0.59, fdr 1e-05), [[PPP1R3F]] (+0.59, fdr 1e-05), [[UBAP1L]] (+0.59, fdr 1e-05); moves opposite to [[BTN3A2]] (-0.59, fdr 2e-05), [[GCNT2]] (-0.55, fdr 3e-05), [[USP54]] (-0.54, fdr 6e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +13.8 | 2e-40 | 37/38 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +13.2 | 2e-37 | 44/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +9.4 | 1e-18 | 37/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +9.1 | 1e-17 | 28/41 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +9.0 | 3e-17 | 24/33 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +8.6 | 6e-16 | 39/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +7.1 | 1e-10 | 29/40 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.74×** | +4.8 | 1e-04 | 19/30 (NCI-H1573, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.007 | 13/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.066 | 10/47 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.40× | +3.0 | 0.13 | 5/46 (CFPAC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.509×** | -6.1 | 8e-07 | 24/44 (C-33 A, PANC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.315×** | -5.4 | 2e-05 | 21/43 (HOP62, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.581×** | -4.9 | 2e-04 | 20/38 (KATO III, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -4.3 | 0.002 | 18/46 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -4.0 | 0.007 | 15/43 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.642×** | -4.0 | 0.007 | 18/47 (PANC-1, KATO III, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -3.7 | 0.016 | 17/31 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -3.5 | 0.029 | 13/46 (A498, SW48, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.503×** | -3.2 | 0.081 | 11/34 (KATO III, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.527× | -3.0 | 0.15 | 15/37 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.07 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +11.6) | — |
| [[KATO III (line)]] | alt | 10.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.62× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 8.53 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -10.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[RKO (line)]] | wt | 6.33 | 0 | 2 | — | [[LJI308 (drug)]] 0.05 µM 0.0625× (z -8.8) |
| [[A498 (line)]] | wt | 2.58 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0499× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0881× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 6.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 2.43 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 0.05 µM 0.0648× (z -9.2) |
| [[A-172 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCCD1]] | +0.69 | +0.68 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DNAJC9]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.59 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[UBAP1L]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ANKMY1]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PSKH1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[AOC2]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC01772]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZNF800]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GLIPR1-AS1]] | +0.54 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[MAP3K7]] | +0.54 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[MSS51]] | +0.54 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A2]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GCNT2]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 | STRING 473 |
| [[USP54]] | -0.54 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[TTBK2]] | -0.54 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[CSTPP1]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SSH2]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DENND4C]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[COA3]] | -0.52 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[HSPA4L]] | -0.51 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[WDR7]] | -0.50 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[GALM]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[VWA1]] | -0.49 | -0.37 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRYGS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, -13.5); signed map (13.6, 1.9). **Vector** length 56.9, 8.00% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +13.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +3.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +0.9 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +2.5 |

## What is on record

|  |  |
|---|---|
| Name | crystallin gamma S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,538,441-186,546,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CRYG8 |
| Gene groups (HGNC) | Beta-gamma crystallins |
| Matched by | ensembl_id |

**Function**, from UniProt [P22914](https://www.uniprot.org/uniprotkb/P22914) (Gamma-crystallin S):

> Crystallins are the dominant structural components of the vertebrate eye lens.

**Summary**, from NCBI Gene [1427](https://www.ncbi.nlm.nih.gov/gene/1427):

> Crystallins are separated into two classes: taxon-specific, or enzyme, and ubiquitous. The latter class constitutes the major proteins of vertebrate eye lens and maintains the transparency and refractive index of the lens. Since lens central fiber cells lose their nuclei during development, these crystallins are made and then retained throughout life, making them extremely stable proteins. Mammalian lens crystallins are divided into alpha, beta, and gamma families; beta and gamma crystallins …

**Accessions** — [HGNC:2417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2417) · Entrez [1427](https://www.ncbi.nlm.nih.gov/gene/1427) · UniProt [P22914](https://www.uniprot.org/uniprotkb/P22914) · Ensembl [ENSG00000213139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213139)

## Data

Gene col 13084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13084); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13084]; `tensor/DDL_lfc|DDL_z.npy` [13084]; `embed/gene_vectors.npy` [13084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13084 or target_col == 13084). Every well: [[CRYGS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYGS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
