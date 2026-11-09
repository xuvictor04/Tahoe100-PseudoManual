---
symbol: "GPAT4"
type: "gene"
col: 8179
ensembl_id: "ENSG00000158669"
name: "glycerol-3-phosphate acyltransferase 4"
location: "8p11.21"
module: 2
arm: "+"
pooled_cpm: 35.51
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GPAT4

*glycerol-3-phosphate acyltransferase 4* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.54× (z +4.4, q 0.007, up in 13 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.90×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.630× (z -12.7, q 2e-34, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.601× (z -9.9, q 8e-21, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD17A]] (+0.70, fdr 9e-06), [[USP35]] (+0.65, fdr 1e-05), [[NBEAL2]] (+0.64, fdr 7e-06); moves opposite to [[ANKRD26]] (-0.62, fdr 3e-05), [[TRIP11]] (-0.61, fdr 4e-05), [[FCF1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8179.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.90×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.007 | 13/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.021 | 15/48 (SHP-77, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.5 | 0.078 | 11/48 (NCI-H2347, HepG2/C3A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.098 | 13/48 (SHP-77, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.13× | +3.2 | 0.15 | 11/48 (Panc 03.27, RKO, …) | top dose only | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.630×** | -12.7 | 2e-34 | 37/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -9.9 | 8e-21 | 38/47 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.699×** | -6.2 | 1e-07 | 27/48 (HOP62, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -6.2 | 1e-07 | 28/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -5.9 | 4e-07 | 29/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.763×** | -5.3 | 1e-05 | 24/45 (RKO, SNU-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.782×** | -4.5 | 7e-04 | 21/44 (RKO, A-427, …) | all doses, flat | composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.801×** | -4.3 | 1e-03 | 18/48 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.009 | 17/46 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.8 | 0.009 | 22/48 (KATO III, SK-MEL-2, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.013 | 16/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.848× | -3.2 | 0.058 | 14/48 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.834× | -3.2 | 0.068 | 17/48 (SNU-1, KATO III, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 0.839× | -3.1 | 0.092 | 19/39 (Panc 03.27, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 0.857× | -3.0 | 0.094 | 13/47 (RKO, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 55.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -15.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 40.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -10.5) |
| [[A-172 (line)]] | wt | 53.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.295× (z -11.5) |
| [[SHP-77 (line)]] | alt | 96.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -8.9) |
| [[A-427 (line)]] | wt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[HS-578T (line)]] | alt | 56.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.392× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 64.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 53.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.202× (z -8.5) |
| [[H4 (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -11.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.242× (z -9.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD17A]] | +0.70 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[USP35]] | +0.65 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SLC41A3]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[INTS11]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LRFN3]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TATDN2]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LLGL1]] | +0.61 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SEMA4F]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[KLHL17]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | -0.62 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.61 | -0.74 / -0.41 | both halves | 4e-05 |  |
| [[FCF1]] | -0.60 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[DARS1]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZNF638]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[LINC01473]] | -0.57 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[LZIC]] | -0.57 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[GATAD1]] | -0.56 | -0.71 / -0.35 | both halves | 1e-04 |  |
| [[XRN1]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.56 | -0.69 / -0.38 | both halves | 7e-05 |  |
| [[SGO1-AS1]] | -0.55 | -0.70 / -0.42 | both halves | 4e-05 |  |
| [[BPTF]] | -0.55 | -0.66 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.8, -22.4); signed map (-44.2, -9.9). **Vector** length 78.2, 14.0% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +5.1 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.4 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.2 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.7 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.9 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.6 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -6.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -3.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glycerol-3-phosphate acyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,577,187-41,625,001 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586M1819, LPAAT-zeta, TSARG7; previously AGPAT6 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Glycerol-3-phosphate acyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UL3](https://www.uniprot.org/uniprotkb/Q86UL3) (Glycerol-3-phosphate acyltransferase 4):

> Converts glycerol-3-phosphate to 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) by incorporating an acyl moiety at the sn-1 position of the glycerol backbone. Active against both saturated and unsaturated long-chain fatty acyl-CoAs. Protects cells against lipotoxicity.

**Summary**, from NCBI Gene [137964](https://www.ncbi.nlm.nih.gov/gene/137964):

> Lysophosphatidic acid acyltransferases (EC 2.3.1.51) catalyze the conversion of lysophosphatidic acid (LPA) to phosphatidic acid (PA). LPA and PA are involved in signal transduction and lipid biosynthesis.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:20880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20880) · Entrez [137964](https://www.ncbi.nlm.nih.gov/gene/137964) · UniProt [Q86UL3](https://www.uniprot.org/uniprotkb/Q86UL3) · Ensembl [ENSG00000158669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158669)

## Data

Gene col 8179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8179); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8179]; `tensor/DDL_lfc|DDL_z.npy` [8179]; `embed/gene_vectors.npy` [8179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8179 or target_col == 8179). Every well: [[GPAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
