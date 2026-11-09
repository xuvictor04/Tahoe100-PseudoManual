---
symbol: "SF3A1"
type: "gene"
col: 1840
ensembl_id: "ENSG00000099995"
name: "splicing factor 3a subunit 1"
location: "22q12.2"
module: 153
arm: "+"
pooled_cpm: 72.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# SF3A1

*splicing factor 3a subunit 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +13.4, q 4e-38, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 0.787× (z -5.3, q 7e-05, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT3]] (+0.82, fdr 7e-06), [[BAG6]] (+0.75, fdr 7e-06), [[LIN7C]] (+0.71, fdr 7e-06); moves opposite to [[RABGEF1P1]] (-0.60, fdr 5e-05), [[LINC00685]] (-0.56, fdr 1e-04), [[UBE2R2]] (-0.55, fdr 5e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +13.4 | 4e-38 | 45/48 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +11.4 | 1e-27 | 39/49 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +10.3 | 1e-22 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +9.8 | 3e-20 | 44/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.2 | 4e-18 | 34/43 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +9.1 | 7e-18 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +8.2 | 2e-14 | 31/45 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.2 | 2e-14 | 41/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.0 | 1e-10 | 33/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +6.9 | 3e-10 | 40/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.1 | 1e-05 | 34/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.34×** | +5.0 | 2e-05 | 32/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 5e-05 | 29/48 (A-427, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.5 | 2e-04 | 30/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.7 | 0.008 | 23/48 (NCI-H1792, SW480, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.015 | 22/48 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **0.787×** | -5.3 | 7e-05 | 37/48 (Panc 03.27, NCI-H23, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.746×** | -4.3 | 0.005 | 34/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Delamanid (drug)]] 0.05 µM |  | **0.788×** | -4.1 | 0.008 | 31/48 (BT-474, RKO, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.793×** | -4.0 | 0.009 | 23/48 (NCI-H2347, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.9 | 0.009 | 19/49 (LoVo, RKO, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.011 | 22/48 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.831× | -3.2 | 0.12 | 17/48 (NCI-H2030, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 80.2 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 53.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 62.0 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.6) | — |
| [[LoVo (line)]] | wt | 67.9 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 57.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 73.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 59.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 71.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 41.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[A-427 (line)]] | wt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 75.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 83.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 97.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 87.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 48.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 87.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 71.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 80.4 | 0 | 2 | — | [[Ranolazine (drug)]] 0.05 µM 0.0745× (z -9.4) |
| [[A498 (line)]] | wt | 88.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 43.7 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.94× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 63.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 95.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT3]] | +0.82 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[BAG6]] | +0.75 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LIN7C]] | +0.71 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SRP68]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[RAB1B]] | +0.68 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ZBED6]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[EIF4H]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[POLR2J3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[USP19]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ARAF]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 995 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1P1]] | -0.60 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[LINC00685]] | -0.56 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[UBE2R2]] | -0.55 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[FBXO11]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ATOX1]] | -0.52 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.8, -23.6); signed map (-14.7, -33.8). **Vector** length 102, 28.6% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | +5.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +13.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +2.6 | +1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +0.1 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3a subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,331,988-30,356,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SF3a120, SAP114, PRPF21, Prp21 |
| Gene groups (HGNC) | U2 small nuclear ribonucleoprotein; SF3a complex |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15459](https://www.uniprot.org/uniprotkb/Q15459) (Splicing factor 3A subunit 1):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3A1 is part of the SF3A subcomplex that …

**Summary**, from NCBI Gene [10291](https://www.ncbi.nlm.nih.gov/gene/10291):

> This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:10765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10765) · Entrez [10291](https://www.ncbi.nlm.nih.gov/gene/10291) · UniProt [Q15459](https://www.uniprot.org/uniprotkb/Q15459) · Ensembl [ENSG00000099995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099995)

## Data

Gene col 1840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1840); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1840]; `tensor/DDL_lfc|DDL_z.npy` [1840]; `embed/gene_vectors.npy` [1840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1840 or target_col == 1840). Every well: [[SF3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
