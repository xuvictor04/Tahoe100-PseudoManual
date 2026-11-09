---
symbol: "FCF1"
type: "gene"
col: 4084
ensembl_id: "ENSG00000119616"
name: "FCF1 rRNA-processing protein"
location: "14q24.3"
module: 28
arm: "+"
pooled_cpm: 53.02
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# FCF1

*FCF1 rRNA-processing protein* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.95× (z +11.6, q 2e-28, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.42× (z +10.4, q 6e-23, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -3.8, q 0.072, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZIC]] (+0.72, fdr 7e-06), [[LARP7]] (+0.72, fdr 7e-06), [[KRIT1]] (+0.72, fdr 7e-06); moves opposite to [[METAP1]] (-0.66, fdr 1e-05), [[WRNIP1]] (-0.62, fdr 1e-05), [[DPY19L1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.95×** | +11.6 | 2e-28 | 48/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.62×** | +10.9 | 3e-25 | 40/42 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +10.4 | 6e-23 | 48/48 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.26×** | +8.9 | 1e-16 | 38/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.0 | 1e-13 | 46/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.58×** | +7.6 | 3e-12 | 39/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +7.1 | 9e-11 | 43/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.9 | 3e-07 | 43/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.2 | 1e-05 | 37/48 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.7 | 1e-04 | 32/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +4.6 | 2e-04 | 30/48 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.42×** | +4.1 | 0.002 | 30/48 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.39×** | +3.9 | 0.005 | 30/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.7 | 0.008 | 30/47 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.041 | 24/48 (Hs 766T, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.072 | 25/48 (NCI-H1792, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.746× | -3.4 | 0.16 | 23/48 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.584× | -3.3 | 0.18 | 25/48 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 72.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 47.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +17.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.92× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 41.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.49× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 43.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 59.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 50.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 77.7 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +12.0) | — |
| [[A-427 (line)]] | wt | 55.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +9.5) | — |
| [[A498 (line)]] | wt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 46.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 36.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.73× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 32.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +9.5) | — |
| [[LoVo (line)]] | wt | 33.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.53× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 44.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 57.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 41.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.87× (z +9.2) | — |
| [[A-172 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 38.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 78.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 70.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 50.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.74× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 66.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 62.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +12.4) | — |
| [[SNU-1 (line)]] | wt | 44.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZIC]] | +0.72 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[LARP7]] | +0.72 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[KRIT1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.72 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.70 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[CHM]] | +0.69 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[DARS1]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[METTL6]] | +0.68 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.68 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.67 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.67 | +0.81 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.66 | -0.77 / -0.52 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.62 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.61 | -0.75 / -0.44 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[NME2]] | -0.60 | -0.72 / -0.37 | both halves | 8e-05 |  |
| [[PODXL2]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[GPAT4]] | -0.60 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[GPC4]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ARHGEF26]] | -0.59 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PALS2]] | -0.59 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[PDXP]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.0, 8.5); signed map (10.0, -23.6). **Vector** length 81.6, 25.2% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +6.5 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.0 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.7 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | FCF1 rRNA-processing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,713,144-74,738,620 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-35, Bka, UTP24; previously C14orf111 |
| Gene groups (HGNC) | SSU processome; Endoribonucleases; PIN-like domain superfamily |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y324](https://www.uniprot.org/uniprotkb/Q9Y324) (rRNA-processing protein FCF1 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [51077](https://www.ncbi.nlm.nih.gov/gene/51077):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20220) · Entrez [51077](https://www.ncbi.nlm.nih.gov/gene/51077) · UniProt [Q9Y324](https://www.uniprot.org/uniprotkb/Q9Y324) · Ensembl [ENSG00000119616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119616)

## Data

Gene col 4084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4084); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4084]; `tensor/DDL_lfc|DDL_z.npy` [4084]; `embed/gene_vectors.npy` [4084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4084 or target_col == 4084). Every well: [[FCF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
