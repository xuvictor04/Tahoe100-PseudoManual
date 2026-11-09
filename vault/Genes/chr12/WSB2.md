---
symbol: "WSB2"
type: "gene"
col: 10758
ensembl_id: "ENSG00000176871"
name: "WD repeat and SOCS box containing 2"
location: "12q24.23"
module: 65
arm: "-"
pooled_cpm: 37.03
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# WSB2

*WD repeat and SOCS box containing 2* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +18.5, q 0e+00, up in 30 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +10.0, q 1e-21, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.253× (z -30.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF655]] (+0.64, fdr 4e-05), [[CHMP3]] (+0.64, fdr 2e-04), [[RRAGC-DT]] (+0.62, fdr 6e-05); moves opposite to [[MRPS34]] (-0.68, fdr 2e-05), [[ATG4C]] (-0.68, fdr 1e-05), [[ARL6]] (-0.65, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +18.5 | 0e+00 | 30/37 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +18.1 | 0e+00 | 40/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +10.4 | 3e-23 | 26/41 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +10.0 | 1e-21 | 33/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.8 | 2e-16 | 30/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 6e-13 | 28/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 1e-10 | 22/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +5.4 | 6e-06 | 20/47 (NCI-H460, A498, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.45×** | +4.6 | 3e-04 | 15/44 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.20× | +4.2 | 0.002 | 20/48 (AsPC-1, NCI-H460, …) | top dose only | composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 1.12× | +3.8 | 0.006 | 10/49 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.12× | +3.8 | 0.007 | 19/47 (AsPC-1, NCI-H460, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 8/48 (KATO III, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.019 | 11/48 (SNU-423, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.066 | 5/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.081 | 4/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.253×** | -30.6 | 0e+00 | 48/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.279×** | -30.4 | 0e+00 | 46/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.296×** | -27.1 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.510×** | -16.0 | 0e+00 | 40/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.707×** | -11.7 | 3e-29 | 41/48 (CHP-212, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.458×** | -9.7 | 4e-20 | 39/48 (AsPC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -8.5 | 1e-15 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -6.3 | 3e-08 | 26/48 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.883× | -3.8 | 0.008 | 11/48 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.852× | -3.8 | 0.008 | 7/48 (PANC-1, AN3 CA, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.008 | 18/48 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.848× | -3.8 | 0.008 | 14/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.7 | 0.011 | 10/48 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.857× | -3.6 | 0.011 | 12/48 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.856× | -3.5 | 0.015 | 15/47 (RPMI-7951, H4, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.4 | 0.023 | 10/48 (SW480, HOP62, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.075 | 7/47 (SNU-1, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.8 | 7 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.9) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 119 | 3 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +17.1) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.274× (z -15.2) |
| [[HOP62 (line)]] | alt | 34.6 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.187× (z -16.2) |
| [[PANC-1 (line)]] | alt | 50.7 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +13.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.223× (z -19.2) |
| [[HS-578T (line)]] | alt | 25.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.203× (z -12.1) |
| [[J82 (line)]] | alt | 34.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.198× (z -14.0) |
| [[SW 900 (line)]] | alt | 37.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.3) |
| [[A-172 (line)]] | wt | 36.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0599× (z -24.4) |
| [[A549 (line)]] | wt | 42.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 35.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 42.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 39.8 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -15.6) |
| [[RKO (line)]] | wt | 38.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -9.8) |
| [[SNU-423 (line)]] | alt | 38.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -15.4) |
| [[SW480 (line)]] | alt | 34.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -21.0) |
| [[A-427 (line)]] | wt | 36.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.98× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.2) |
| [[A498 (line)]] | wt | 27.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -10.5) |
| [[COLO 205 (line)]] | alt | 60.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 66.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.144× (z -14.8) |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -12.9) |
| [[HT-29 (line)]] | alt | 37.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -11.0) |
| [[KATO III (line)]] | alt | 31.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -10.5) |
| [[LoVo (line)]] | wt | 34.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -14.7) |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 42.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.251× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 39.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.334× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -14.8) |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -11.6) |
| [[C32 (line)]] | wt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -12.8) |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.227× (z -10.1) |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -8.6) |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.200× (z -11.2) |
| [[AN3 CA (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | +0.64 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CHMP3]] | +0.64 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[RRAGC-DT]] | +0.62 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[FKRP]] | +0.61 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[TMEM192]] | +0.61 | +0.36 / +0.38 | both halves | 1e-04 |  |
| [[HPS1]] | +0.60 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[OSTM1]] | +0.60 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[AKT1S1]] | +0.60 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[TBCE-1]] | +0.59 | +0.32 / +0.39 | both halves | 1e-04 |  |
| [[LTO1]] | +0.58 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[GCNT4]] | +0.58 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[HACD1]] | +0.58 | +0.44 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS34]] | -0.68 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ATG4C]] | -0.68 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ARL6]] | -0.65 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PRRC1]] | -0.60 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[HACE1]] | -0.60 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ABHD10]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[THYN1]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[MRPS26]] | -0.58 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[KCTD6]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 | pathway: Neddylation |
| [[CABIN1]] | -0.56 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[MRPL17]] | -0.56 | -0.21 / -0.42 | both halves | 7e-04 |  |
| [[SAC3D1]] | -0.56 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WSB2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises WSB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.8, -11.2); signed map (19.0, -26.8). **Vector** length 87.4, 20.3% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +8.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +18.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.3 | +5.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -30.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -27.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -30.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and SOCS box containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,032,687-118,062,430 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SBA2, MGC10210 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYS7](https://www.uniprot.org/uniprotkb/Q9NYS7) (WD repeat and SOCS box-containing protein 2):

> May be a substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [55884](https://www.ncbi.nlm.nih.gov/gene/55884):

> This gene encodes a member of the WD-protein subfamily. The encoded protein contains five WD-repeats spanning most of the protein and an SOCS box in the C-terminus. The SOCS box may act as a bridge between specific substrate-binding domains and E3 ubiquitin protein ligases. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:19222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19222) · Entrez [55884](https://www.ncbi.nlm.nih.gov/gene/55884) · UniProt [Q9NYS7](https://www.uniprot.org/uniprotkb/Q9NYS7) · Ensembl [ENSG00000176871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176871)

## Data

Gene col 10758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10758); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10758]; `tensor/DDL_lfc|DDL_z.npy` [10758]; `embed/gene_vectors.npy` [10758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10758 or target_col == 10758). Every well: [[WSB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WSB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
