---
symbol: "IQCE"
type: "gene"
col: 2706
ensembl_id: "ENSG00000106012"
name: "IQ motif containing E"
location: "7p22.3"
module: 50
arm: "+"
pooled_cpm: 25.87
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# IQCE

*IQ motif containing E* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +17.7, q 0e+00, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.666× (z -8.6, q 6e-15, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF3IP1]] (+0.63, fdr 2e-05), [[RABL6]] (+0.54, fdr 4e-05), [[NEK4]] (+0.54, fdr 4e-05); moves opposite to [[KYAT3]] (-0.50, fdr 2e-05), [[DMAC1]] (-0.48, fdr 2e-04), [[DDX50]] (-0.46, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +17.7 | 0e+00 | 34/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +16.7 | 0e+00 | 29/36 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +16.2 | 0e+00 | 35/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +12.7 | 6e-35 | 28/46 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +12.0 | 6e-31 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +11.1 | 9e-27 | 35/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +11.1 | 9e-27 | 31/40 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +10.1 | 3e-22 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.1 | 3e-14 | 30/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +6.8 | 4e-10 | 27/47 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.8 | 3e-07 | 21/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +5.5 | 2e-06 | 17/47 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.30×** | +5.2 | 7e-06 | 17/43 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.5 | 3e-04 | 16/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.2 | 9e-04 | 15/47 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.002 | 16/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.002 | 13/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 12/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.011 | 9/47 (NCI-H23, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -8.6 | 6e-15 | 32/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -6.9 | 1e-09 | 22/47 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -5.2 | 4e-05 | 21/47 (SW 1271, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.6 | 5e-04 | 21/47 (C32, KATO III, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.6 | 5e-04 | 19/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -4.2 | 0.003 | 13/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.826×** | -4.0 | 0.005 | 16/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.4 | 0.043 | 9/47 (Panc 03.27, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.843× | -3.3 | 0.055 | 13/46 (NCI-H661, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.858× | -3.2 | 0.073 | 11/46 (hTERT-HPNE, HT-29, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.084 | 7/47 (PANC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.5 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.04× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.441× (z -8.6) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 33.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +30.3) | — |
| [[SW480 (line)]] | alt | 26.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 50.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +29.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.5) | [[Harringtonine (drug)]] 0.5 µM 0.395× (z -10.3) |
| [[A549 (line)]] | wt | 18.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +14.3) | — |
| [[KATO III (line)]] | alt | 44.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 22.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.5) | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -13.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 42.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0782× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.6) | — |
| [[H4 (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0665× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF3IP1]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[RABL6]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[NEK4]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[AKT2]] | +0.51 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[MOK]] | +0.51 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[SMARCC2]] | +0.51 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[ATP9A]] | +0.50 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[USF2]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[NCOA6]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[PRKACA]] | +0.50 | +0.24 / +0.55 | both halves | 5e-04 | pathway: Signaling by Hedgehog |
| [[ELAVL1]] | +0.49 | +0.24 / +0.57 | both halves | 4e-04 |  |
| [[TRAF7]] | +0.48 | +0.27 / +0.59 | both halves | 3e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYAT3]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DMAC1]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[DDX50]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MRPL2]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ZNF215]] | -0.45 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[USP53]] | -0.44 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF697]] | -0.44 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[MRPL17]] | -0.44 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[ZNF699]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[C14orf119]] | -0.44 | -0.08 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[GNPNAT1]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[AASDH]] | -0.43 | -0.08 / -0.44 | ⚠ not reproduced | 0.004 |  |
| [[RARS1]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ZNF280C]] | -0.43 | -0.23 / -0.47 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.360). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, -50.0); signed map (-32.7, -32.2). **Vector** length 92.0, 19.9% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +17.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,558,972-2,614,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1023 |
| Gene groups (HGNC) | EvC complex subunits |
| Reactome | 3 pathways, smallest: Activation of SMO; Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IPM2](https://www.uniprot.org/uniprotkb/Q6IPM2) (IQ domain-containing protein E):

> Component of the EvC complex that positively regulates ciliary Hedgehog (Hh) signaling (By similarity). Required for proper limb morphogenesis.

**Summary**, from NCBI Gene [23288](https://www.ncbi.nlm.nih.gov/gene/23288):

> Involved in limb morphogenesis. Predicted to be located in cytoplasmic side of plasma membrane. Predicted to be part of plasma membrane protein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29171) · Entrez [23288](https://www.ncbi.nlm.nih.gov/gene/23288) · UniProt [Q6IPM2](https://www.uniprot.org/uniprotkb/Q6IPM2) · Ensembl [ENSG00000106012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106012)

## Data

Gene col 2706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2706); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2706]; `tensor/DDL_lfc|DDL_z.npy` [2706]; `embed/gene_vectors.npy` [2706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2706 or target_col == 2706). Every well: [[IQCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
