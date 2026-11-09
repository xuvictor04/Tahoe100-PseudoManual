---
symbol: "SNX7"
type: "gene"
col: 8548
ensembl_id: "ENSG00000162627"
name: "sorting nexin 7"
location: "1p21.3"
module: 25
arm: "+"
pooled_cpm: 33.47
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SNX7

*sorting nexin 7* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.22× (z +4.0, q 0.044, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -35.6, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D1]] (+0.61, fdr 1e-05), [[GPC4]] (+0.57, fdr 1e-05), [[ABCB10]] (+0.57, fdr 1e-05); moves opposite to [[ZKSCAN1]] (-0.52, fdr 3e-05), [[ENDOV]] (-0.52, fdr 2e-05), [[USP36]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.044 | 17/47 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.42 | 9/46 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.42 | 13/37 (PANC-1, MIA PaCa-2, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -35.6 | 0e+00 | 45/46 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -18.2 | 0e+00 | 42/47 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.417×** | -17.3 | 0e+00 | 44/46 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -16.2 | 0e+00 | 42/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.459×** | -15.3 | 0e+00 | 41/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -14.6 | 0e+00 | 37/47 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.496×** | -13.8 | 2e-41 | 41/47 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -10.4 | 2e-23 | 35/47 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -10.1 | 3e-22 | 32/47 (A-172, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -9.6 | 3e-20 | 34/47 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -9.6 | 5e-20 | 30/47 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -8.5 | 1e-15 | 30/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -7.9 | 1e-13 | 29/47 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -7.6 | 1e-12 | 30/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -7.5 | 3e-12 | 29/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -7.2 | 3e-11 | 33/46 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 40.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.9) |
| [[SW480 (line)]] | alt | 23.1 | 0 | 9 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -15.4) |
| [[HS-578T (line)]] | alt | 79.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -29.8) |
| [[A-172 (line)]] | wt | 46.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.2) |
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.6) |
| [[SNU-1 (line)]] | wt | 79.8 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.214× (z -11.4) |
| [[A498 (line)]] | wt | 57.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -25.5) |
| [[Hs 766T (line)]] | wt | 96.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -28.7) |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 42.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.2) |
| [[SW 900 (line)]] | alt | 39.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -19.7) |
| [[A549 (line)]] | wt | 33.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.6) |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.5) |
| [[J82 (line)]] | alt | 33.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.3) |
| [[LS 180 (line)]] | wt | 32.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0997× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.8) |
| [[C32 (line)]] | wt | 37.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 49.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.2) |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -22.3) |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.9) |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.7) |
| [[A-427 (line)]] | wt | 42.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.6) |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.0) |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.9) |
| [[H4 (line)]] | wt | 33.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -11.7) |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.7) |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.0) |
| [[LoVo (line)]] | wt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.7) |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 2 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0643× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0595× (z -19.6) |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.7) |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0974× (z -8.5) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.5) |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.0) |
| [[PANC-1 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -8.8) |
| [[RKO (line)]] | wt | 32.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.2) |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0421× (z -9.6) |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GPC4]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DCK]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[KLHL2]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RAB23]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[EXOC5]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.54 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[GMPS]] | +0.53 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[RNPEP]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PRPS1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MAPK9]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN1]] | -0.52 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ENDOV]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[USP36]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[OFD1]] | -0.49 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[C19orf18]] | -0.48 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ACAD10]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PRRT3-AS1]] | -0.46 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ITFG2]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LINC02804]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[NFKBIL1]] | -0.45 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[SURF6]] | -0.44 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.9, -34.3); signed map (-30.3, -41.5). **Vector** length 73.2, 15.6% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -5.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -35.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -10.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.8 | -0.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:98,661,701-98,760,500 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNH6](https://www.uniprot.org/uniprotkb/Q9UNH6) (Sorting nexin-7):

> Involved in the regulation of endocytosis and in several stages of intracellular trafficking. Together with SNX4, involved in autophagosome assembly by regulating trafficking and recycling of phospholipid scramblase ATG9A.

**Summary**, from NCBI Gene [51375](https://www.ncbi.nlm.nih.gov/gene/51375):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region like some family members, and its exact function is unknown. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 11. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:14971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14971) · Entrez [51375](https://www.ncbi.nlm.nih.gov/gene/51375) · UniProt [Q9UNH6](https://www.uniprot.org/uniprotkb/Q9UNH6) · Ensembl [ENSG00000162627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162627)

## Data

Gene col 8548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8548); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8548]; `tensor/DDL_lfc|DDL_z.npy` [8548]; `embed/gene_vectors.npy` [8548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8548 or target_col == 8548). Every well: [[SNX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
