---
symbol: "ZNF92"
type: "gene"
col: 7119
ensembl_id: "ENSG00000146757"
name: "zinc finger protein 92"
location: "7q11.21"
module: 91
arm: "+"
pooled_cpm: 28.01
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF92

*zinc finger protein 92* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +26.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.463× (z -14.9, q 0e+00, down in 27 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.738× (z -4.4, q 0.002, down in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SW480 0.124×, HEC-1-A 0.172×, BT-474 0.0861×, A-172 0.138×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.265×, NCI-H2347 0.252×, RKO 0.246×, SW1417 0.333×, …; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.103×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.247×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.205×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF430]] (+0.59, fdr 2e-05), [[FAAP24]] (+0.56, fdr 2e-05), [[ZNF273]] (+0.55, fdr 1e-05); moves opposite to [[SMAD2]] (-0.49, fdr 3e-05), [[EFR3A]] (-0.45, fdr 1e-04), [[ARHGAP17]] (-0.45, fdr 7e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +26.8 | 0e+00 | 45/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +15.2 | 0e+00 | 34/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.99×** | +13.7 | 2e-40 | 40/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.90×** | +12.8 | 3e-35 | 43/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +12.2 | 6e-32 | 39/48 (LoVo, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +11.9 | 8e-31 | 37/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.81×** | +11.9 | 2e-30 | 36/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +11.8 | 3e-30 | 32/45 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +11.5 | 6e-29 | 34/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +9.4 | 3e-19 | 34/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +8.4 | 2e-15 | 38/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.5 | 2e-12 | 30/43 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +7.0 | 1e-10 | 27/48 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.37×** | +6.2 | 2e-08 | 24/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.34×** | +5.8 | 3e-07 | 23/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.6 | 7e-07 | 22/48 (SW480, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.6 | 7e-07 | 19/48 (J82, HOP62, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.59×** | +4.8 | 5e-05 | 13/45 (RPMI-7951, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 8e-05 | 17/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.003 | 8/48 (RKO, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.007 | 12/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.4 | 0.017 | 4/48 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7119.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SW480 0.124×, HEC-1-A 0.172×, BT-474 0.0861×, A-172 0.138×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.265×, NCI-H2347 0.252×, RKO 0.246×, SW1417 0.333×, …; ⚠ toxic; transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.103×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.247×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.205×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -14.9 | 0e+00 | 27/37 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -14.2 | 4e-43 | 34/42 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.791×** | -4.7 | 4e-04 | 15/48 (BT-474, HOP62, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.738×** | -4.4 | 0.002 | 19/44 (H4, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.812×** | -4.2 | 0.003 | 20/46 (SHP-77, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.6 | 0.036 | 18/48 (NCI-H1792, LS 180, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.898× | -3.0 | 0.19 | 6/48 (A549, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 47.7 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 25.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -13.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.7 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -24.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 35.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 41.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 27.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0861× (z -16.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +17.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.43× (z +9.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 27.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 45.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 33.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 74.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.205× (z -8.5) |
| [[HOP62 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 24.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.103× (z -10.3) |
| [[Hs 766T (line)]] | wt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.8) | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF430]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 | same gene group |
| [[FAAP24]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF273]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF714]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF93]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF724]] | +0.51 | +0.54 / +0.49 | both halves | 1e-05 | same gene group |
| [[TTF1]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF431]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 | same gene group |
| [[E2F7]] | +0.50 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[ZNF486]] | +0.50 | +0.40 / +0.51 | both halves | 4e-05 | same gene group |
| [[CCDC97]] | +0.50 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ZNF100]] | +0.49 | +0.53 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.45 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[ARHGAP17]] | -0.45 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[FDX1]] | -0.44 | -0.48 / -0.26 | both halves | 3e-04 |  |
| [[ENAH]] | -0.44 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[NCOR2]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[B4GALT1]] | -0.43 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[SNX12]] | -0.43 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[STOM]] | -0.43 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CTC1]] | -0.42 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[EPS15]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[CD99L2]] | -0.42 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.461). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-45.2, -47.7); signed map (-39.1, -35.0). **Vector** length 81.2, 17.3% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.9 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.2 | +9.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 92 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:65,373,799-65,401,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPF12, TF12 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03936](https://www.uniprot.org/uniprotkb/Q03936) (Zinc finger protein 92):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [168374](https://www.ncbi.nlm.nih.gov/gene/168374):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13168) · Entrez [168374](https://www.ncbi.nlm.nih.gov/gene/168374) · UniProt [Q03936](https://www.uniprot.org/uniprotkb/Q03936) · Ensembl [ENSG00000146757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146757)

## Data

Gene col 7119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7119); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7119]; `tensor/DDL_lfc|DDL_z.npy` [7119]; `embed/gene_vectors.npy` [7119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7119 or target_col == 7119). Every well: [[ZNF92 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF92.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
