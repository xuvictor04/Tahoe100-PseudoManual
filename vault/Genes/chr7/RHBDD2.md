---
symbol: "RHBDD2"
type: "gene"
col: 85
ensembl_id: "ENSG00000005486"
name: "rhomboid domain containing 2"
location: "7q11.23"
module: 33
arm: "-"
pooled_cpm: 12.9
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 4
n_dd_up_clean: 29
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RHBDD2

*rhomboid domain containing 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (15 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.55× (z +19.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.714× (z -5.0, q 4e-04, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALS8]] (+0.53, fdr 3e-05), [[PITHD1]] (+0.53, fdr 1e-05), [[PSMD8]] (+0.53, fdr 1e-04); moves opposite to [[NARS2]] (-0.51, fdr 7e-05), [[TMCO6]] (-0.50, fdr 2e-04), [[PA2G4]] (-0.46, fdr 6e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 85.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.55×** | +19.7 | 0e+00 | 46/48 (SW480, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.45×** | +19.2 | 0e+00 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.41×** | +19.0 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +18.7 | 0e+00 | 41/44 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +17.6 | 0e+00 | 38/46 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.54×** | +14.5 | 3e-45 | 43/48 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +13.9 | 4e-42 | 42/45 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +13.8 | 3e-41 | 40/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +13.4 | 2e-39 | 36/40 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.43×** | +13.3 | 2e-38 | 24/25 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.22×** | +12.4 | 1e-33 | 31/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.6 | 3e-20 | 37/48 (A-427, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.4 | 2e-19 | 40/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +8.7 | 2e-16 | 31/45 (NCI-H460, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +8.6 | 3e-16 | 34/46 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.9 | 1e-13 | 29/48 (SW480, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +7.9 | 1e-13 | 29/47 (H4, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +7.6 | 6e-13 | 27/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +6.7 | 4e-10 | 21/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.8 | 1e-07 | 22/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 85.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.714×** | -5.0 | 4e-04 | 19/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.619×** | -3.9 | 0.027 | 11/44 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.027 | 12/47 (SW 1271, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.803×** | -3.4 | 0.089 | 8/48 (A498, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 85. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.8 | 10 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.36× (z +14.9) | — |
| [[KATO III (line)]] | alt | 16.4 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.22× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 12.1 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 9.00 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 13.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.95× (z +10.2) | — |
| [[A498 (line)]] | wt | 18.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.1) | — |
| [[A549 (line)]] | wt | 10.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 17.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.90× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 9.81 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.33× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.48× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.07× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 16.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.82× (z +10.2) | — |
| [[A-172 (line)]] | wt | 26.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.24× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 8.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +13.1) | — |
| [[HCT15 (line)]] | alt | 9.01 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0815× (z -8.5) |
| [[HS-578T (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.5) | — |
| [[J82 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +8.7) | — |
| [[LoVo (line)]] | wt | 9.21 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.03× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 7.26 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.128× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 9.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 8.63 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.09× (z +9.5) | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 85), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS8]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[PITHD1]] | +0.53 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PSMD8]] | +0.53 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[UBE2A]] | +0.50 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[CREM]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ACOX1]] | +0.48 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[MICALL2]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RELL2]] | +0.46 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[BBIP1]] | +0.46 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[DMAC2]] | +0.46 | +0.43 / +0.29 | both halves | 3e-04 |  |
| [[PITRM1]] | +0.45 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[WNT9A]] | +0.44 | +0.31 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARS2]] | -0.51 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[TMCO6]] | -0.50 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[PA2G4]] | -0.46 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[WDR43]] | -0.45 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[IPO11]] | -0.45 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DDX11-AS1]] | -0.44 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[NUFIP1]] | -0.44 | -0.10 / -0.48 | ⚠ not reproduced | 0.003 |  |
| [[CUZD1]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[NHLRC3]] | -0.43 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[NUBPL]] | -0.43 | -0.16 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[WDR3]] | -0.43 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[CLYBL]] | -0.43 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[UTP18]] | -0.43 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[SNRPD1]] | -0.43 | -0.37 / -0.38 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RHBDD2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.8% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.0, -51.3); signed map (-9.5, 19.9). **Vector** length 63.6, 11.5% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +19.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.3 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.2 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +5.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,842,602-75,888,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPD007; previously RHBDL7 |
| Gene groups (HGNC) | Rhomboid family |
| Matched by | ensembl_id |

UniProt [Q6NTF9](https://www.uniprot.org/uniprotkb/Q6NTF9) carries no function annotation.

**Summary**, from NCBI Gene [57414](https://www.ncbi.nlm.nih.gov/gene/57414):

> The protein encoded by this gene is a member of the rhomboid family of membrane-bound proteases and is overexpressed in some breast cancers. Members of this family are involved in intramembrane proteolysis. In mouse, the orthologous protein associates with the Golgi body. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:23082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23082) · Entrez [57414](https://www.ncbi.nlm.nih.gov/gene/57414) · UniProt [Q6NTF9](https://www.uniprot.org/uniprotkb/Q6NTF9) · Ensembl [ENSG00000005486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005486)

## Data

Gene col 85: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 85); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 85, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 85]; `tensor/DDL_lfc|DDL_z.npy` [85]; `embed/gene_vectors.npy` [85]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 85 or target_col == 85). Every well: [[RHBDD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
