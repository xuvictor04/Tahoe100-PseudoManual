---
symbol: "IER5"
type: "gene"
col: 8580
ensembl_id: "ENSG00000162783"
name: "immediate early response 5"
location: "1q25.3"
module: 20
arm: "-"
pooled_cpm: 39.68
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IER5

*immediate early response 5* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.59× (z +13.4, q 5e-38, up in 39 of 45 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.71× (z +12.2, q 9e-32, up in 44 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD11]] (+0.72, fdr 7e-06), [[SERTAD1]] (+0.71, fdr 7e-06), [[ZSWIM4]] (+0.70, fdr 7e-06); moves opposite to [[ENOPH1]] (-0.68, fdr 7e-06), [[TSN]] (-0.64, fdr 7e-06), [[ERLIN1]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSORS1C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.59×** | +13.4 | 5e-38 | 39/45 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.71×** | +12.2 | 9e-32 | 44/46 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.69×** | +9.9 | 1e-20 | 40/45 (A549, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.20×** | +9.2 | 8e-18 | 42/44 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +7.9 | 2e-13 | 39/43 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +7.7 | 1e-12 | 38/45 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.22×** | +6.3 | 3e-08 | 40/46 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +5.8 | 4e-07 | 37/46 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.09×** | +5.8 | 5e-07 | 25/40 (SK-MEL-2, HS-578T, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.93×** | +5.2 | 1e-05 | 36/45 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.86×** | +4.5 | 3e-04 | 20/38 (PANC-1, HS-578T, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.72×** | +4.3 | 9e-04 | 30/46 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.71×** | +4.2 | 0.001 | 25/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.71×** | +4.2 | 0.001 | 32/46 (A-427, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 29/46 (A-427, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.23×** | +3.7 | 0.007 | 35/44 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.011 | 29/47 (LOX-IMVI, NCI-H2347, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.054 | 22/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.076 | 16/46 (LS 180, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.089 | 25/47 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.86×** | +2.9 | 0.089 | 22/45 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8580.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.697× | -3.7 | 0.11 | 30/46 (A-427, LoVo, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.729× | -3.5 | 0.15 | 28/46 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.662× | -3.3 | 0.21 | 21/46 (HOP62, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.673× | -3.1 | 0.21 | 27/46 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.638× | -3.1 | 0.21 | 22/47 (Hs 766T, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.1 | 9 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.35× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.95× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 17.2 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +13.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 17.4× (z +13.3) | — |
| [[A498 (line)]] | wt | 58.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.04× (z +9.5) | — |
| [[A549 (line)]] | wt | 46.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +14.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.64× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 56.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 38.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.13× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.4× (z +13.9) | — |
| [[C32 (line)]] | wt | 30.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +15.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 18.0× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 62.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +15.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 49.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 10.1× (z +14.7) | — |
| [[Hs 766T (line)]] | wt | 65.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.08× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 37.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +15.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.49× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.99 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 32.0× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.1× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 24.6 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.83× (z +9.7) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Auranofin (drug)]] 5 µM 6.76× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 47.3 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +12.8) | — |
| [[A-172 (line)]] | wt | 54.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +13.1) | — |
| [[J82 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 13.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.31× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +13.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 29.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.8× (z +13.5) | — |
| [[A-427 (line)]] | wt | 16.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 24.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.1× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 42.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.54× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.33× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.39× (z +8.5) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.3× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 63.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 35.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.40× (z +8.7) | — |
| [[SW480 (line)]] | alt | 45.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD11]] | +0.72 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[SERTAD1]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 | STRING 430 |
| [[ZSWIM4]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF503]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MIDN]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CDKN1A]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CLCF1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZBTB7A]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CATSPERG]] | +0.58 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[GOLT1A]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MAFF]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOPH1]] | -0.68 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[TSN]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[ERLIN1]] | -0.64 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[PAICS]] | -0.64 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[KDM1A]] | -0.63 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[IARS2]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SKP2]] | -0.61 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[PMS2]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[ABCB10]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[IPO5]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[RPE]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.59 | -0.64 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSORS1C1]] | B | PSORS1C1 activity raises IER5's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without PSORS1C1 | 0.053 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[RNF223]] | B | RNF223 activity raises IER5's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without RNF223 | 0.066 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[BACH2]] | B | BACH2 activity raises IER5's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without BACH2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.8, -22.5); signed map (4.4, 24.8). **Vector** length 104, 33.8% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -4.9 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | -4.1 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | immediate early response 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:181,088,700-181,092,900 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VY09](https://www.uniprot.org/uniprotkb/Q5VY09) (Immediate early response gene 5 protein):

> Plays a role as a transcription factor. Mediates positive transcriptional regulation of several chaperone genes during the heat shock response in a HSF1-dependent manner. Mediates negative transcriptional regulation of CDC25B expression. Plays a role in the dephosphorylation of the heat shock factor HSF1 and ribosomal protein S6 kinase (S6K) by the protein phosphatase PP2A. Involved in the regulation of cell proliferation and resistance to thermal stress. Involved in the cell cycle checkpoint …

**Summary**, from NCBI Gene [51278](https://www.ncbi.nlm.nih.gov/gene/51278):

> This gene encodes a protein that is similar to other immediate early response proteins. In the mouse, a similar gene may play an important role in mediating the cellular response to mitogenic signals. Studies in rats found the expression of a similar gene to be increased after waking and sleep deprivation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5393) · Entrez [51278](https://www.ncbi.nlm.nih.gov/gene/51278) · UniProt [Q5VY09](https://www.uniprot.org/uniprotkb/Q5VY09) · Ensembl [ENSG00000162783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162783)

## Data

Gene col 8580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8580); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8580]; `tensor/DDL_lfc|DDL_z.npy` [8580]; `embed/gene_vectors.npy` [8580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8580 or target_col == 8580). Every well: [[IER5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IER5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
