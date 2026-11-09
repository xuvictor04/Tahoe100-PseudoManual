---
symbol: "EBNA1BP2"
type: "gene"
col: 3901
ensembl_id: "ENSG00000117395"
name: "EBNA1 binding protein 2"
location: "1p34.2"
module: 4
arm: "+"
pooled_cpm: 38.49
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EBNA1BP2

*EBNA1 binding protein 2* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.79× (z +16.7, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.77× (z +9.7, q 5e-20, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.202×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUVBL1]] (+0.76, fdr 7e-06), [[MYBBP1A]] (+0.75, fdr 7e-06), [[WDR77]] (+0.72, fdr 7e-06); moves opposite to [[SIRT2]] (-0.70, fdr 7e-06), [[GABARAP]] (-0.63, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[ZMYM5]] (-0.61, fdr 2e-05), [[TXNDC16]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 18 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **5.79×** | +16.7 | 0e+00 | 43/44 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **4.65×** | +14.1 | 2e-42 | 42/43 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.71×** | +11.5 | 2e-28 | 41/43 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.77×** | +9.7 | 5e-20 | 44/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.71×** | +9.5 | 3e-19 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.44×** | +8.5 | 2e-15 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.84×** | +8.2 | 2e-14 | 36/47 (NCI-H1792, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +8.1 | 6e-14 | 41/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.23×** | +7.6 | 2e-12 | 40/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +6.5 | 4e-09 | 44/48 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **2.02×** | +6.4 | 6e-09 | 36/47 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.0 | 9e-08 | 40/48 (HOP62, CFPAC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.72×** | +5.1 | 1e-05 | 32/45 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +5.0 | 2e-05 | 36/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.67×** | +4.7 | 1e-04 | 33/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 3e-04 | 27/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.88×** | +4.0 | 0.002 | 30/47 (NCI-H460, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +3.9 | 0.002 | 27/46 (NCI-H460, LOX-IMVI, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.003 | 30/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.004 | 26/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.006 | 30/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.011 | 26/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.98×** | +3.4 | 0.014 | 22/45 (NCI-H460, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.95×** | +3.3 | 0.019 | 26/48 (HS-578T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.019 | 22/48 (NCI-H23, C-33 A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.022 | 23/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.027 | 26/47 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.281×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.202×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.662× | -3.6 | 0.20 | 25/48 (NCI-H23, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | 0.698× | -3.3 | 0.23 | 23/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.523× | -3.2 | 0.23 | 23/47 (J82, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.79 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 13.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.9× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 22.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.30× (z +8.7) | — |
| [[A549 (line)]] | wt | 20.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HS-578T (line)]] | alt | 43.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HT-29 (line)]] | alt | 26.5 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.28× (z +12.4) | — |
| [[SW480 (line)]] | alt | 42.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.51× (z +8.5) | — |
| [[A498 (line)]] | wt | 43.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HEC-1-A (line)]] | alt | 36.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.63× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 21.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 50.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.1× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 54.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 33.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.96× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 27.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.34× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.6× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.7× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 56.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.58× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 34.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SNU-1 (line)]] | wt | 193 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.1) |
| [[SNU-423 (line)]] | alt | 18.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 59.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.28× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 41.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[H4 (line)]] | wt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HCT15 (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.113× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.06× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2030 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SHP-77 (line)]] | alt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 64.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUVBL1]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | STRING 417 |
| [[MYBBP1A]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | STRING 562 |
| [[WDR77]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[NOLC1]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 | STRING 776 |
| [[EIPR1]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 | STRING 886 |
| [[RRS1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | STRING 996 |
| [[POLR1A]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | STRING 609 |
| [[MAK16]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 | STRING 999 |
| [[PNO1]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 663 |
| [[WDR4]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.70 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | -0.63 | -0.54 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZMYM5]] | -0.61 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[TXNDC16]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ETFDH]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[CRY2]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MAP3K2]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NPC2]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 | same gene group |
| [[ABCA5]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[LIN7B]] | -0.58 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[AAMDC]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.2, -33.7); signed map (-5.4, -46.1). **Vector** length 71.7, 21.8% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.54 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.5 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | EBNA1 binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,164,175-43,270,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOBP, EBP2, P40 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99848](https://www.uniprot.org/uniprotkb/Q99848) (Probable rRNA-processing protein EBP2):

> Required for the processing of the 27S pre-rRNA.

**Summary**, from NCBI Gene [10969](https://www.ncbi.nlm.nih.gov/gene/10969):

> Enables RNA binding activity. Predicted to be involved in rRNA processing and ribosomal large subunit biogenesis. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15531) · Entrez [10969](https://www.ncbi.nlm.nih.gov/gene/10969) · UniProt [Q99848](https://www.uniprot.org/uniprotkb/Q99848) · Ensembl [ENSG00000117395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117395)

## Data

Gene col 3901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3901); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3901]; `tensor/DDL_lfc|DDL_z.npy` [3901]; `embed/gene_vectors.npy` [3901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3901 or target_col == 3901). Every well: [[EBNA1BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBNA1BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
