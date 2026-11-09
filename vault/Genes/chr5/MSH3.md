---
symbol: "MSH3"
type: "gene"
col: 3448
ensembl_id: "ENSG00000113318"
name: "mutS homolog 3"
location: "5q14.1"
module: 4
arm: "+"
pooled_cpm: 96.85
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MSH3

*mutS homolog 3* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.20× (z +6.5, q 4e-08, up in 21 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.15× (z +4.9, q 3e-04, up in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 2.89×, J82 1.82×; ⚠ cell-cycle shift, explains ~19% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.20×; ⚠ cell-cycle shift, explains ~23% of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.20×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.556× (z -29.6, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPIDR]] (+0.62, fdr 1e-05), [[WDR70]] (+0.57, fdr 4e-05), [[POLR3B]] (+0.57, fdr 2e-05); moves opposite to [[SIX4]] (-0.49, fdr 5e-05), [[C14orf28]] (-0.48, fdr 1e-04), [[PPP1R18]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 2.89×, J82 1.82×; ⚠ cell-cycle shift, explains ~19% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.20×; ⚠ cell-cycle shift, explains ~23% of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 2.20×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +6.5 | 4e-08 | 21/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +4.9 | 3e-04 | 14/48 (RKO, C-33 A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +4.8 | 3e-04 | 17/48 (C-33 A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +4.1 | 0.006 | 8/49 (NCI-H460, H4, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.052 | 10/48 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.086 | 4/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -29.6 | 0e+00 | 47/49 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -15.2 | 0e+00 | 38/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -15.2 | 0e+00 | 36/45 (SNU-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -14.1 | 7e-43 | 38/50 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -13.2 | 1e-37 | 32/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.773×** | -13.0 | 2e-36 | 26/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.707×** | -12.4 | 3e-33 | 36/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -11.5 | 6e-29 | 27/49 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.736×** | -10.9 | 5e-26 | 30/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -10.6 | 2e-24 | 34/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -10.5 | 6e-24 | 25/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -8.3 | 6e-15 | 27/48 (CHP-212, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.798×** | -8.1 | 4e-14 | 27/48 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.800×** | -7.9 | 8e-14 | 25/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.811×** | -7.5 | 3e-12 | 25/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -7.3 | 1e-11 | 24/48 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -5.8 | 2e-07 | 9/49 (NCI-H1573, Panc 03.27, …) | two highest doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.905× | -5.0 | 1e-05 | 3/49 (A498, HS-578T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.001 | 12/49 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.895× | -3.9 | 0.001 | 10/47 (NCI-H2030, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.908× | -3.4 | 0.010 | 7/48 (SHP-77, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 115 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -23.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -22.3) |
| [[NCI-H460 (line)]] | wt | 97.4 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -21.0) |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -15.4) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -12.3) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.6) |
| [[C-33 A (line)]] | alt | 109 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.9) |
| [[LS 180 (line)]] | wt | 114 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.432× (z -11.7) |
| [[SW480 (line)]] | alt | 148 | 1 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +12.1) ⚠ cell-cycle shift, explains ~23% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -18.7) |
| [[C32 (line)]] | wt | 122 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.20× (z +10.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -16.3) |
| [[HT-29 (line)]] | alt | 88.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.1) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 88.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -16.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.415× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 76.5 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.382× (z -12.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.497× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -32.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -21.5) |
| [[SW 900 (line)]] | alt | 96.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -18.3) |
| [[H4 (line)]] | wt | 76.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.566× (z -10.2) |
| [[HOP62 (line)]] | alt | 98.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -16.4) |
| [[HS-578T (line)]] | alt | 62.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 64.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.5) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 95.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.6) |
| [[A-427 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -16.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.202× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 96.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.2) |
| [[RKO (line)]] | wt | 73.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -14.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 85.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -14.6) |
| [[SW48 (line)]] | wt | 149 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0549× (z -30.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.9) |
| [[A498 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.485× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 75.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.5) |
| [[HCT15 (line)]] | alt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.6) |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -13.2) |
| [[J82 (line)]] | alt | 70.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.3) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[KATO III (line)]] | alt | 64.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -10.9) |
| [[LoVo (line)]] | wt | 144 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -14.4) |
| [[SHP-77 (line)]] | alt | 91.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 79.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.2) |
| [[A-172 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[WDR70]] | +0.57 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[POLR3B]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CDIN1]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[INTS7]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[FAM133B]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[VWA8]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[C2CD5]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CRTC1]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[GMNN]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[FAM98B]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.53 | +0.40 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX4]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[C14orf28]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[PPP1R18]] | -0.47 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[SLC35F5]] | -0.47 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[CTTN]] | -0.47 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[KDM6B]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ERO1B]] | -0.46 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[HLA-L-1]] | -0.45 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[UPK2]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MSH3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ERO1B]] | C | ERO1B activity raises MSH3's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 1.64× lower at baseline in the lines without ERO1B | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.8, -5.3); signed map (-13.0, -49.7). **Vector** length 99.5, 23.8% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | -5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.3 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -29.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -15.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -13.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -7.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mutS homolog 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,654,652-80,876,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DUP, MRP1 |
| Gene groups (HGNC) | MutS homologs |
| Reactome | 6 pathways, smallest: Defective Mismatch Repair Associated With MSH2; Diseases of Mismatch Repair (MMR); Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta) |
| Matched by | ensembl_id |

**Function**, from UniProt [P20585](https://www.uniprot.org/uniprotkb/P20585) (DNA mismatch repair protein Msh3):

> Component of the post-replicative DNA mismatch repair system (MMR). Heterodimerizes with MSH2 to form MutS beta which binds to DNA mismatches thereby initiating DNA repair. When bound, the MutS beta heterodimer bends the DNA helix and shields approximately 20 base pairs. MutS beta recognizes large insertion-deletion loops (IDL) up to 13 nucleotides long. After mismatch binding, forms a ternary complex with the MutL alpha heterodimer, which is thought to be responsible for directing the …

**Summary**, from NCBI Gene [4437](https://www.ncbi.nlm.nih.gov/gene/4437):

> The protein encoded by this gene forms a heterodimer with MSH2 to form MutS beta, part of the post-replicative DNA mismatch repair system. MutS beta initiates mismatch repair by binding to a mismatch and then forming a complex with MutL alpha heterodimer. This gene contains a polymorphic 9 bp tandem repeat sequence in the first exon. The repeat is present 6 times in the reference genome sequence and 3-7 repeats have been reported. Defects in this gene are a cause of susceptibility to …

**Accessions** — [HGNC:7326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7326) · Entrez [4437](https://www.ncbi.nlm.nih.gov/gene/4437) · UniProt [P20585](https://www.uniprot.org/uniprotkb/P20585) · Ensembl [ENSG00000113318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113318)

## Data

Gene col 3448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3448); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3448]; `tensor/DDL_lfc|DDL_z.npy` [3448]; `embed/gene_vectors.npy` [3448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3448 or target_col == 3448). Every well: [[MSH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
