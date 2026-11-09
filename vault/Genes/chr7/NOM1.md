---
symbol: "NOM1"
type: "gene"
col: 7132
ensembl_id: "ENSG00000146909"
name: "nucleolar protein with MIF4G domain 1"
location: "7q36.3"
module: 5
arm: "+"
pooled_cpm: 51.96
n_lines_expressing: 50
n_dd_up: 49
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOM1

*nucleolar protein with MIF4G domain 1* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (26 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.05× (z +14.6, q 1e-45, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.94× (z +14.6, q 1e-45, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.777× (z -3.9, q 0.020, down in 18 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Binimetinib (drug)]] 0.5 µM: 0.851× (z -3.8, q 0.020, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.710×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.599×; ⚠ cell-cycle shift, explains ~41% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.194×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.77, fdr 7e-06), [[POLR1A]] (+0.76, fdr 7e-06), [[URB2]] (+0.76, fdr 7e-06); moves opposite to [[LINC01273]] (-0.63, fdr 1e-05), [[MYLIP]] (-0.61, fdr 1e-05), [[CCNG2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 29 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.05×** | +14.6 | 1e-45 | 47/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.94×** | +14.6 | 1e-45 | 47/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +14.1 | 5e-43 | 38/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.94×** | +13.5 | 3e-39 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.86×** | +12.6 | 1e-34 | 45/48 (SW480, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.96×** | +11.6 | 7e-29 | 42/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +11.4 | 3e-28 | 45/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.73×** | +10.7 | 5e-25 | 41/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +10.1 | 4e-22 | 39/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.80×** | +9.9 | 2e-21 | 32/45 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.60×** | +9.5 | 8e-20 | 33/46 (SNU-423, LS 180, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.39×** | +9.5 | 1e-19 | 28/48 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.3 | 8e-19 | 41/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +9.0 | 8e-18 | 35/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.54×** | +8.8 | 5e-17 | 33/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +8.5 | 5e-16 | 35/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.5 | 2e-12 | 33/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.76×** | +6.0 | 4e-08 | 34/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 3e-06 | 26/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +5.2 | 5e-06 | 25/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 7e-06 | 22/48 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +4.6 | 8e-05 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 1e-04 | 19/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 2e-04 | 21/47 (MIA PaCa-2, SW 900, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +4.2 | 3e-04 | 17/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.710×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.599×; ⚠ cell-cycle shift, explains ~41% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.194×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.777×** | -3.9 | 0.020 | 18/48 (A498, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.020 | 18/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.829×** | -3.8 | 0.020 | 19/49 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.875× | -3.8 | 0.020 | 17/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.884× | -3.6 | 0.039 | 5/48 (RPMI-7951, A-427, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 0.886× | -3.5 | 0.039 | 20/48 (AsPC-1, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.852× | -3.5 | 0.039 | 13/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -3.5 | 0.039 | 15/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.847× | -3.3 | 0.066 | 18/47 (AsPC-1, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.895× | -3.2 | 0.073 | 6/48 (NCI-H23, NCI-H1573, …) | top dose only | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.082 | 10/48 (A-427, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.833× | -3.1 | 0.096 | 14/47 (LOX-IMVI, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.097 | 15/47 (A-172, A-427, …) | two highest doses | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.862× | -3.0 | 0.097 | 10/48 (SW 1271, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 75.8 | 12 (9 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +14.1) | — |
| [[LoVo (line)]] | wt | 64.3 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +10.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.25× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 32.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.73× (z +9.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 38.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.17× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 81.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 131 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.40× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 79.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.9) | — |
| [[KATO III (line)]] | alt | 48.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.80× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 32.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 40.5 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.98× (z +11.2) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 60.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.31× (z +11.1) | — |
| [[A549 (line)]] | wt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.53× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.194× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 69.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.2) | — |
| [[SW48 (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.96× (z +9.1) | — |
| [[A-172 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 | STRING 677 |
| [[URB2]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.75 | +0.79 / +0.75 | both halves | 7e-06 | STRING 433 |
| [[TCOF1]] | +0.74 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 | STRING 523 |
| [[TWNK]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[LSG1]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | STRING 419 |
| [[TOMM40]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[LTV1]] | +0.73 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; STRING 717 |
| [[GRWD1]] | +0.72 | +0.72 / +0.74 | both halves | 7e-06 | STRING 635 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01273]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MYLIP]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CCNG2]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.3, -35.8); signed map (-3.6, -47.1). **Vector** length 95.0, 27.9% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *rRNA processing* (reactome, mean cos +0.56 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.57 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -4.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.9 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | +8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein with MIF4G domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:156,949,712-156,973,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SGD1, PPP1R113; previously C7orf3 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; SSU processome; MIF4G domain containing proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5C9Z4](https://www.uniprot.org/uniprotkb/Q5C9Z4) (Nucleolar MIF4G domain-containing protein 1):

> Plays a role in targeting PPP1CA to the nucleolus.

**Summary**, from NCBI Gene [64434](https://www.ncbi.nlm.nih.gov/gene/64434):

> Proteins that contain MIF4G (middle of eIF4G (MIM 600495)) and/or MA3 domains, such as NOM1, function in protein translation. These domains include binding sites for members of the EIF4A family of ATP-dependent DEAD box RNA helicases (see EIF4A1; MIM 602641) (Simmons et al., 2005 [PubMed 15715967]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13244) · Entrez [64434](https://www.ncbi.nlm.nih.gov/gene/64434) · UniProt [Q5C9Z4](https://www.uniprot.org/uniprotkb/Q5C9Z4) · Ensembl [ENSG00000146909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146909)

## Data

Gene col 7132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7132); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7132]; `tensor/DDL_lfc|DDL_z.npy` [7132]; `embed/gene_vectors.npy` [7132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7132 or target_col == 7132). Every well: [[NOM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
