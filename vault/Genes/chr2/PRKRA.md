---
symbol: "PRKRA"
type: "gene"
col: 11089
ensembl_id: "ENSG00000180228"
name: "protein activator of interferon induced protein kinase EIF2AK2"
location: "2q31.2"
module: 40
arm: "+"
pooled_cpm: 54.22
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PRKRA

*protein activator of interferon induced protein kinase EIF2AK2* — 2q31.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 1.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.685× (z -11.5, q 9e-28, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TULP3]] (+0.68, fdr 7e-06), [[MALSU1]] (+0.67, fdr 7e-06), [[ELP2]] (+0.67, fdr 1e-05); moves opposite to [[PPP1R10]] (-0.68, fdr 7e-06), [[PURB]] (-0.66, fdr 1e-05), [[ZC3H4]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 1.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | 1.18× | +3.6 | 0.18 | 21/48 (SW480, PANC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.2 | 0.38 | 10/48 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.38 | 5/48 (LS 180, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -11.5 | 9e-28 | 33/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -9.1 | 2e-17 | 39/49 (RPMI-7951, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -9.1 | 2e-17 | 37/45 (SHP-77, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -8.8 | 1e-16 | 32/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.701×** | -7.2 | 8e-11 | 37/47 (RKO, AN3 CA, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.742×** | -6.4 | 2e-08 | 38/48 (LS 180, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -6.0 | 1e-07 | 33/48 (LS 180, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -5.9 | 3e-07 | 28/48 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -4.9 | 6e-05 | 23/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.810×** | -4.5 | 4e-04 | 23/48 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.811×** | -4.3 | 8e-04 | 23/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.806×** | -4.3 | 8e-04 | 24/48 (CHP-212, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **0.815×** | -4.2 | 0.001 | 20/42 (AsPC-1, HS-578T, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.833×** | -3.9 | 0.004 | 22/48 (H4, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.839× | -3.8 | 0.006 | 19/48 (MIA PaCa-2, SNU-423, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.886× | -3.6 | 0.009 | 20/48 (A-172, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.850× | -3.5 | 0.018 | 16/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.028 | 9/49 (C32, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.897× | -3.3 | 0.033 | 5/48 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.047 | 7/48 (LOX-IMVI, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 72.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -17.4) |
| [[A-172 (line)]] | wt | 58.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.154× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.5) |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.144× (z -8.7) |
| [[H4 (line)]] | wt | 70.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HS-578T (line)]] | alt | 61.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.7) |
| [[A-427 (line)]] | wt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[HOP62 (line)]] | alt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -15.7) |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.1) |
| [[J82 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.5) |
| [[LoVo (line)]] | wt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -9.7) |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.5) |
| [[SW 1271 (line)]] | alt | 78.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[SW 900 (line)]] | alt | 59.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.0) |
| [[SW480 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.86× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | — |
| [[A549 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP3]] | +0.68 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ELP2]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ABHD18]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NKTR]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[HSPB11]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ARSK]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[GMCL1]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[FLYWCH2]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.68 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[PURB]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.66 | -0.73 / -0.57 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[DDX5]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[FSCN2]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SLC2A9]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.2, -13.3); signed map (-40.9, 10.4). **Vector** length 112, 27.8% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | +2.9 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.8 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.0 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | protein activator of interferon induced protein kinase EIF2AK2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,431,292-178,451,512 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PACT, RAX, HSD14, DYT16 |
| Gene groups (HGNC) | RISC loading complex subunits |
| Reactome | 7 pathways, smallest: Small interfering RNA (siRNA) biogenesis; MicroRNA (miRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O75569](https://www.uniprot.org/uniprotkb/O75569) (Interferon-inducible double-stranded RNA-dependent protein kinase activator A):

> Activates EIF2AK2/PKR in the absence of double-stranded RNA (dsRNA), leading to phosphorylation of EIF2S1/EFI2-alpha and inhibition of translation and induction of apoptosis. Required for siRNA production by DICER1 and for subsequent siRNA-mediated post-transcriptional gene silencing. Does not seem to be required for processing of pre-miRNA to miRNA by DICER1. Promotes UBC9-p53/TP53 association and sumoylation and phosphorylation of p53/TP53 at 'Lys-386' at 'Ser-392' respectively and enhances …

**Summary**, from NCBI Gene [8575](https://www.ncbi.nlm.nih.gov/gene/8575):

> This gene encodes a protein kinase activated by double-stranded RNA which mediates the effects of interferon in response to viral infection. Mutations in this gene have been associated with dystonia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:9438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9438) · Entrez [8575](https://www.ncbi.nlm.nih.gov/gene/8575) · UniProt [O75569](https://www.uniprot.org/uniprotkb/O75569) · Ensembl [ENSG00000180228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180228)

## Data

Gene col 11089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11089); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11089]; `tensor/DDL_lfc|DDL_z.npy` [11089]; `embed/gene_vectors.npy` [11089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11089 or target_col == 11089). Every well: [[PRKRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
