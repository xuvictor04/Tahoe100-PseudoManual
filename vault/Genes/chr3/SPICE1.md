---
symbol: "SPICE1"
type: "gene"
col: 8730
ensembl_id: "ENSG00000163611"
name: "spindle and centriole associated protein 1"
location: "3q13.2"
module: 40
arm: "+"
pooled_cpm: 64.11
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SPICE1

*spindle and centriole associated protein 1* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +15.9, q 0e+00, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (NCI-H1573 2.42×, MIA PaCa-2 2.64×, SW480 1.80×, Panc 03.27 2.24×, …); [[Panobinostat (drug)]] 5 µM in 3 lines (PANC-1 3.89×, A-427 2.82×, A549 2.85×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 3.56×, A-427 2.58×, LOX-IMVI 2.88×; ⚠ cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.544× (z -22.2, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP37]] (+0.78, fdr 7e-06), [[SMAP2]] (+0.73, fdr 7e-06), [[GMCL1]] (+0.72, fdr 7e-06); moves opposite to [[PTPN21]] (-0.66, fdr 7e-06), [[CPLANE1]] (-0.61, fdr 1e-05), [[NUTM2B-AS1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF331]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (NCI-H1573 2.42×, MIA PaCa-2 2.64×, SW480 1.80×, Panc 03.27 2.24×, …); [[Panobinostat (drug)]] 5 µM in 3 lines (PANC-1 3.89×, A-427 2.82×, A549 2.85×; ⚠ cell-cycle shift, explains ~34% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 3.56×, A-427 2.58×, LOX-IMVI 2.88×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +15.9 | 0e+00 | 36/49 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.67×** | +13.2 | 3e-37 | 40/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.62×** | +12.5 | 1e-33 | 34/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.62×** | +12.4 | 3e-33 | 38/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.26×** | +5.7 | 1e-06 | 24/50 (PANC-1, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.6 | 2e-06 | 24/49 (PANC-1, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.23×** | +5.3 | 9e-06 | 22/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +5.3 | 9e-06 | 21/48 (PANC-1, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.17× | +4.0 | 0.004 | 17/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.058 | 8/48 (A-172, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.544×** | -22.2 | 0e+00 | 38/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -18.5 | 0e+00 | 42/48 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -11.8 | 7e-30 | 33/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.614×** | -11.6 | 3e-29 | 35/45 (KATO III, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -11.3 | 9e-28 | 33/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -11.1 | 7e-27 | 35/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -9.9 | 3e-21 | 36/48 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -9.2 | 2e-18 | 35/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.714×** | -8.7 | 2e-16 | 31/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -8.7 | 2e-16 | 34/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -8.1 | 4e-14 | 31/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.742×** | -7.7 | 8e-13 | 29/49 (RPMI-7951, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -7.3 | 2e-11 | 31/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -7.1 | 7e-11 | 27/48 (C32, SNU-423, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -6.8 | 5e-10 | 29/47 (Panc 03.27, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -6.0 | 6e-08 | 26/48 (Panc 03.27, HT-29, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.794×** | -5.7 | 3e-07 | 23/48 (C32, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -5.2 | 5e-06 | 25/48 (HT-29, C32, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.818×** | -5.2 | 6e-06 | 18/48 (A-172, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 93.2 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 51.3 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -13.0) |
| [[SW480 (line)]] | alt | 80.0 | 4 (3 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.424× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.448× (z -11.8) |
| [[LoVo (line)]] | wt | 84.2 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -10.0) |
| [[A498 (line)]] | wt | 52.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 48.6 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 69.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -21.1) |
| [[PANC-1 (line)]] | alt | 33.6 | 4 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.89× (z +17.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.2) |
| [[SNU-423 (line)]] | alt | 64.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.6) |
| [[A-172 (line)]] | wt | 50.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.1) |
| [[A-427 (line)]] | wt | 62.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.141× (z -21.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 89.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -20.5) |
| [[SW 900 (line)]] | alt | 67.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -20.1) |
| [[SW1417 (line)]] | alt | 58.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.0) | — |
| [[A549 (line)]] | wt | 44.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 69.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 55.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.0) |
| [[H4 (line)]] | wt | 72.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.5) |
| [[J82 (line)]] | alt | 81.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.1) |
| [[KATO III (line)]] | alt | 84.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.444× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 36.9 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.88× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 79.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.8) |
| [[HCT15 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 94.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.3) |
| [[HOP62 (line)]] | alt | 75.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.0) |
| [[Hs 766T (line)]] | wt | 53.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.5) |
| [[HT-29 (line)]] | alt | 110 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -8.9) |
| [[LS 180 (line)]] | wt | 79.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.448× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 79.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.160× (z -20.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 72.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.8) |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.125× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -11.2) |
| [[C-33 A (line)]] | alt | 56.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 55.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +8.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 65.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 77.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -11.4) |
| [[SW48 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP37]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[SMAP2]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[APAF1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PEX3]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MLEC]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[COG6]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[P3H1]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN21]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[CPLANE1]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SYT14]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[COA7]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[FKRP]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CDV3]] | -0.60 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[BMPR1B]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.58 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.57 | -0.57 / -0.58 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF331]] | B | ZNF331 activity raises SPICE1's level | lines that do not express ZNF331 (15) vs lines expressing it (35) | 1.07× lower at baseline in the lines without ZNF331 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF256, SNRPN, ZNF625 |
| [[PLEKHG4]] | B | PLEKHG4 activity raises SPICE1's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without PLEKHG4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[RAB20]] | B | RAB20 activity strengthens SPICE1's drug response | lines that do not express RAB20 (8) vs lines expressing it (41) | the lines without RAB20 respond 0.82× as strongly (z diff +0.56); strongest at Homoharringtonine 5 µM: 0.87x vs 0.46x (z diff +4.4) | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[NRN1]] | B | NRN1 activity raises SPICE1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.35× lower at baseline in the lines without NRN1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[HDAC6]] | B | HDAC6 activity lowers SPICE1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NRN1]] | B | NRN1 activity weakens SPICE1's drug response | lines that do not express NRN1 (27) vs lines expressing it (22) | the lines without NRN1 respond 1.02× as strongly (z diff -0.17); strongest at Panobinostat 5 µM: 2.02x vs 1.41x (z diff -2.8) | 0.089 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137; target measured in part of the lines; both ways; artifact flags |
| [[MYH10]] | B | MYH10 activity raises SPICE1's level | lines that do not express MYH10 (10) vs lines expressing it (40) | 1.14× lower at baseline in the lines without MYH10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAPT, MOCS1, GAMT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.9, -18.8); signed map (-37.9, 21.0). **Vector** length 122, 37.1% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.1 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.0 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.0 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +15.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.1 | +0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Pimitespib (drug)]] 0.05 µM |  | +2.1 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.2 | -22.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -18.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | spindle and centriole associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:113,442,718-113,515,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPICE; previously CCDC52 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0Z3](https://www.uniprot.org/uniprotkb/Q8N0Z3) (Spindle and centriole-associated protein 1):

> Regulator required for centriole duplication, for proper bipolar spindle formation and chromosome congression in mitosis.

**Summary**, from NCBI Gene [152185](https://www.ncbi.nlm.nih.gov/gene/152185):

> Involved in metaphase chromosome alignment; mitotic spindle assembly; and regulation of centriole replication. Located in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25083) · Entrez [152185](https://www.ncbi.nlm.nih.gov/gene/152185) · UniProt [Q8N0Z3](https://www.uniprot.org/uniprotkb/Q8N0Z3) · Ensembl [ENSG00000163611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163611)

## Data

Gene col 8730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8730); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8730]; `tensor/DDL_lfc|DDL_z.npy` [8730]; `embed/gene_vectors.npy` [8730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8730 or target_col == 8730). Every well: [[SPICE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPICE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
