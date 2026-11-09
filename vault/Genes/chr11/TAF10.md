---
symbol: "TAF10"
type: "gene"
col: 9286
ensembl_id: "ENSG00000166337"
name: "TATA-box binding protein associated factor 10"
location: "11p15.4"
module: 109
arm: "+"
pooled_cpm: 12.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# TAF10

*TATA-box binding protein associated factor 10* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.64× (z +17.1, q 0e+00, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +13.1, q 3e-37, up in 37 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0687×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.118×; ⚠ cell-cycle shift, explains ~79% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX32]] (+0.61, fdr 1e-05), [[STX10]] (+0.52, fdr 2e-05), [[FAAP20]] (+0.50, fdr 5e-05); moves opposite to [[ZNF639]] (-0.54, fdr 3e-05), [[CCDC43]] (-0.48, fdr 2e-04), [[CDC5L]] (-0.48, fdr 5e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.64×** | +17.1 | 0e+00 | 34/35 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.94×** | +13.8 | 1e-40 | 23/24 (PANC-1, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +13.7 | 4e-40 | 25/27 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +13.1 | 3e-37 | 37/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.07×** | +9.6 | 7e-20 | 39/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +8.3 | 1e-14 | 27/40 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.85×** | +8.1 | 3e-14 | 36/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.73×** | +7.3 | 2e-11 | 34/47 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.2 | 3e-08 | 25/46 (A-172, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +5.9 | 2e-07 | 28/46 (NCI-H2347, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +4.8 | 9e-05 | 15/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.28×** | +4.6 | 2e-04 | 20/45 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +4.1 | 0.002 | 17/44 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 16/48 (A498, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.35×** | +3.9 | 0.003 | 17/45 (RKO, AsPC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.010 | 12/44 (J82, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.015 | 8/44 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.032 | 5/44 (BT-474, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.060 | 8/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.070 | 8/44 (SW 900, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +2.9 | 0.084 | 7/44 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0687×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.118×; ⚠ cell-cycle shift, explains ~79% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 12.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.92× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 9.40 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 8.75 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +19.0) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[PANC-1 (line)]] | alt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 14.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -8.7) ⚠ cell-cycle shift, explains ~79% of this change |
| [[J82 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 7.22 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +10.6) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[Panc 03.27 (line)]] | alt | 7.80 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0687× (z -11.1) |
| [[SNU-423 (line)]] | alt | 9.75 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.0) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[A-172 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX32]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[STX10]] | +0.52 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[FAAP20]] | +0.50 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ADGRE3]] | +0.50 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[BCL2L12]] | +0.49 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SYN1]] | +0.49 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | +0.49 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[NOP14-AS1]] | +0.48 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SURF1]] | +0.48 | +0.30 / +0.57 | both halves | 2e-04 | pathway: HALLMARK_DNA_REPAIR |
| [[MLF2]] | +0.48 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[SEPTIN10]] | +0.48 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[MXRA7]] | +0.48 | +0.21 / +0.46 | both halves | 7e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF639]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[CCDC43]] | -0.48 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[CDC5L]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ZBTB24]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MTARC2]] | -0.46 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[KBTBD6]] | -0.46 | -0.21 / -0.56 | both halves | 6e-04 |  |
| [[KAT14]] | -0.46 | -0.28 / -0.48 | both halves | 3e-04 | pathway: Chromatin modifying enzymes; STRING 773 |
| [[THUMPD1]] | -0.45 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[COIL]] | -0.45 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[MRPS9]] | -0.44 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[FAM217B]] | -0.44 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[SETD2]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 | pathway: Chromatin modifying enzymes |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAF10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.384). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, -28.6); signed map (3.9, 29.4). **Vector** length 52.2, 7.49% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.5 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | -1.0 |
|  | [[Bimatoprost (drug)]] 0.5 µM |  | +0.9 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,606,294-6,612,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII30; previously TAF2H, TAF2A |
| Gene groups (HGNC) | SAGA complex; General transcription factor IID complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 24 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12962](https://www.uniprot.org/uniprotkb/Q12962) (Transcription initiation factor TFIID subunit 10):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF10 is also component of …

**Summary**, from NCBI Gene [6881](https://www.ncbi.nlm.nih.gov/gene/6881):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11543) · Entrez [6881](https://www.ncbi.nlm.nih.gov/gene/6881) · UniProt [Q12962](https://www.uniprot.org/uniprotkb/Q12962) · Ensembl [ENSG00000166337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166337)

## Data

Gene col 9286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9286); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9286]; `tensor/DDL_lfc|DDL_z.npy` [9286]; `embed/gene_vectors.npy` [9286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9286 or target_col == 9286). Every well: [[TAF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
