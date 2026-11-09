---
symbol: "BCAP31"
type: "gene"
col: 11737
ensembl_id: "ENSG00000185825"
name: "B cell receptor associated protein 31"
location: "Xq28"
module: 12
arm: "-"
pooled_cpm: 38.61
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# BCAP31

*B cell receptor associated protein 31* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.19× (z +16.1, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.83× (z +8.4, q 9e-15, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.471× (z -11.3, q 1e-26, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM3]] (+0.76, fdr 7e-06), [[ZNF731P]] (+0.73, fdr 7e-06), [[MAPK9]] (+0.68, fdr 8e-06); moves opposite to [[RPP25L]] (-0.70, fdr 7e-06), [[SNHG11]] (-0.70, fdr 7e-06), [[TMEM265]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NSDHL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.19×** | +16.1 | 0e+00 | 43/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.10×** | +15.1 | 0e+00 | 38/38 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.46×** | +11.6 | 1e-28 | 39/41 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +8.4 | 9e-15 | 43/48 (HT-29, COLO 205, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +7.3 | 3e-11 | 39/48 (HT-29, Panc 03.27, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +7.0 | 2e-10 | 40/48 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +7.0 | 3e-10 | 36/48 (HT-29, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +6.4 | 8e-09 | 33/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +6.2 | 4e-08 | 34/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.52×** | +5.8 | 3e-07 | 33/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.49×** | +5.5 | 2e-06 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +5.0 | 2e-05 | 27/48 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +4.9 | 4e-05 | 28/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.36×** | +4.3 | 9e-04 | 27/47 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.32×** | +3.9 | 0.004 | 20/48 (KATO III, AsPC-1, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.471×** | -11.3 | 1e-26 | 43/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -10.0 | 3e-21 | 44/47 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.623×** | -6.6 | 8e-09 | 41/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -6.6 | 8e-09 | 35/48 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.747×** | -4.1 | 0.005 | 21/48 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.814×** | -4.0 | 0.006 | 22/48 (NCI-H1573, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -3.6 | 0.030 | 23/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.5 | 0.036 | 21/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.041 | 20/48 (HT-29, SW480, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.783×** | -3.3 | 0.063 | 18/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.074 | 14/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.080 | 18/47 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.792×** | -3.1 | 0.087 | 20/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.088 | 19/48 (CHP-212, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.091 | 8/48 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.793×** | -3.0 | 0.093 | 19/47 (RPMI-7951, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 43.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.5) |
| [[A498 (line)]] | wt | 50.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -8.6) |
| [[PANC-1 (line)]] | alt | 55.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -9.3) |
| [[HT-29 (line)]] | alt | 52.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.9) |
| [[J82 (line)]] | alt | 43.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.2) |
| [[SW 900 (line)]] | alt | 39.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -11.8) |
| [[SW480 (line)]] | alt | 28.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -9.4) |
| [[A549 (line)]] | wt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 49.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.6) |
| [[Hs 766T (line)]] | wt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 54.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 45.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 60.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 37.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.7) |
| [[HCT15 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.5) |
| [[LoVo (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0465× (z -16.6) |
| [[SHP-77 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 80.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.8) |
| [[SW1417 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM3]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ZNF731P]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[MAPK9]] | +0.68 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[CHID1]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[THOC5]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[HSPA8]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 | pathway: Respiratory Syncytial Virus Infection Pathway; STRING 511 |
| [[ABHD17A]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[UFD1]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MSN]] | +0.65 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 | pathway: RHOA GTPase cycle |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[SNHG11]] | -0.70 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[TMEM265]] | -0.69 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[PEX12]] | -0.68 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[COIL]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[CLK4]] | -0.67 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[PPP4R2]] | -0.67 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[EPC1]] | -0.67 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PIM3]] | -0.66 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[COMMD3]] | -0.65 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[RAB9A]] | -0.65 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[TMEM42]] | -0.63 | -0.60 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises BCAP31's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BTG3]] | C | BTG3 activity raises BCAP31's level | lines that do not express BTG3 (4) vs lines expressing it (46) | 1.36× lower at baseline in the lines without BTG3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WTIP; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSDHL]] | C | BCAP31's natural level strengthens NSDHL's drug response | BCAP31's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.52; direction not clear | 0.067 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.7, 3.0); signed map (-28.5, -31.8). **Vector** length 115, 31.1% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.3 | +15.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.0 | +16.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Decitabine (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.3 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.7 | -10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.1 | -1.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | B cell receptor associated protein 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,700,492-153,724,565 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS1357E, BAP31, 6C6-Ag, CDM |
| Hallmark sets | APOPTOSIS, DNA_REPAIR |
| Reactome | 14 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Apoptotic cleavage of cellular proteins; Apoptotic execution phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P51572](https://www.uniprot.org/uniprotkb/P51572) (B-cell receptor-associated protein 31):

> Functions as a chaperone protein. Is one of the most abundant endoplasmic reticulum (ER) proteins. Plays a role in the export of secreted proteins in the ER, the recognition of abnormally folded protein and their targeting to the ER associated-degradation (ERAD). Also serves as a cargo receptor for the export of transmembrane proteins (By similarity). Plays a role in the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) by stimulating the translocation of …

**Summary**, from NCBI Gene [10134](https://www.ncbi.nlm.nih.gov/gene/10134):

> This gene encodes a member of the B-cell receptor associated protein 31 superfamily. The encoded protein is a multi-pass transmembrane protein of the endoplasmic reticulum that is involved in the anterograde transport of membrane proteins from the endoplasmic reticulum to the Golgi and in caspase 8-mediated apoptosis. Microdeletions in this gene are associated with contiguous ABCD1/DXS1375E deletion syndrome (CADDS), a neonatal disorder. Alternative splicing of this gene results in multiple …

**Accessions** — [HGNC:16695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16695) · Entrez [10134](https://www.ncbi.nlm.nih.gov/gene/10134) · UniProt [P51572](https://www.uniprot.org/uniprotkb/P51572) · Ensembl [ENSG00000185825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185825)

## Data

Gene col 11737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11737); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11737]; `tensor/DDL_lfc|DDL_z.npy` [11737]; `embed/gene_vectors.npy` [11737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11737 or target_col == 11737). Every well: [[BCAP31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAP31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
