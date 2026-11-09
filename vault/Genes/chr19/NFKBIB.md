---
symbol: "NFKBIB"
type: "gene"
col: 2503
ensembl_id: "ENSG00000104825"
name: "NFKB inhibitor beta"
location: "19q13.2"
module: 20
arm: "-"
pooled_cpm: 36.87
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NFKBIB

*NFKB inhibitor beta* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.04× (z +28.0, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPF3B]] (+0.71, fdr 7e-06), [[CHMP4A]] (+0.71, fdr 7e-06), [[ITSN2]] (+0.70, fdr 7e-06); moves opposite to [[PHB1]] (-0.64, fdr 2e-05), [[GRB2]] (-0.62, fdr 1e-05), [[SKP2]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.04×** | +28.0 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.99×** | +16.3 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.28×** | +15.8 | 0e+00 | 47/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **5.28×** | +15.8 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.26×** | +15.7 | 0e+00 | 47/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.34×** | +10.8 | 4e-25 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.98×** | +10.4 | 3e-23 | 45/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.43×** | +8.4 | 3e-15 | 41/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +8.3 | 9e-15 | 37/39 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.42×** | +7.9 | 2e-13 | 39/43 (NCI-H460, A-427, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +7.9 | 2e-13 | 43/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +7.0 | 2e-10 | 40/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.12×** | +6.9 | 3e-10 | 30/36 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.9 | 1e-07 | 36/45 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.7 | 4e-07 | 31/47 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +5.2 | 7e-06 | 36/47 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 3e-04 | 30/47 (NCI-H2030, SW48, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.030 | 25/47 (SW480, A-427, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.094 | 16/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.795× | -3.1 | 0.94 | 24/48 (HS-578T, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.3 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +25.7) | — |
| [[LoVo (line)]] | wt | 20.8 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +22.6) | — |
| [[PANC-1 (line)]] | alt | 168 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +32.3) | — |
| [[A-427 (line)]] | wt | 29.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 26.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +20.9) | — |
| [[BT-474 (line)]] | alt | 23.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +19.1) | — |
| [[H4 (line)]] | wt | 34.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +18.2) | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +25.3) | — |
| [[HOP62 (line)]] | alt | 23.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +25.1) | — |
| [[AsPC-1 (line)]] | alt | 39.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +24.0) | — |
| [[HS-578T (line)]] | alt | 44.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +21.4) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +18.6) | — |
| [[NCI-H1792 (line)]] | alt | 27.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +14.5) | — |
| [[A549 (line)]] | wt | 63.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +23.5) | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +19.2) | — |
| [[J82 (line)]] | alt | 35.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +20.0) | — |
| [[KATO III (line)]] | alt | 32.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 18.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +16.3) | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 23.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +23.9) | — |
| [[SW480 (line)]] | alt | 26.2 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.11× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.69× (z +12.8) | — |
| [[A-172 (line)]] | wt | 28.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +23.7) | — |
| [[A498 (line)]] | wt | 32.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +21.4) | — |
| [[COLO 205 (line)]] | alt | 46.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 27.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 53.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +22.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.5) | — |
| [[RKO (line)]] | wt | 34.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +15.2) | — |
| [[SW48 (line)]] | wt | 26.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +13.3) | — |
| [[C32 (line)]] | wt | 15.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +17.9) | — |
| [[HepG2_C3A (line)]] | wt | 28.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +19.2) | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +18.4) | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +18.1) | — |
| [[SHP-77 (line)]] | alt | 40.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +17.7) | — |
| [[SNU-1 (line)]] | wt | 23.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 27.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +14.8) | — |
| [[C-33 A (line)]] | alt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +11.4) | — |
| [[SW 1088 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF3B]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ITSN2]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PLA2G4C]] | +0.69 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[GATAD1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[XIAP]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.63 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PPP1R15A]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[STAP2]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZDHHC1]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ZC3H6]] | +0.60 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[WBP4]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[GRB2]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[SKP2]] | -0.62 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[PAFAH1B2]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[RNF4]] | -0.60 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.60 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ATP5F1B]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CDC123]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[STARD7]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PARP1]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PODXL2]] | -0.57 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.8, -27.4); signed map (4.0, -12.3). **Vector** length 76.3, 23.6% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +16.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +28.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | -1.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.3 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +3.3 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,899,700-38,908,893 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKBB, TRIP9 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NFKB inhibitor family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 35 pathways, smallest: RIP-mediated NFkB activation via ZBP1; Dengue virus modulates apoptosis; ZBP1(DAI) mediated induction of type I IFNs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15653](https://www.uniprot.org/uniprotkb/Q15653) (NF-kappa-B inhibitor beta):

> Inhibits NF-kappa-B by complexing with and trapping it in the cytoplasm. However, the unphosphorylated form resynthesized after cell stimulation is able to bind NF-kappa-B allowing its transport to the nucleus and protecting it to further NFKBIA-dependent inactivation. Association with inhibitor kappa B-interacting NKIRAS1 and NKIRAS2 prevent its phosphorylation rendering it more resistant to degradation, explaining its slower degradation.

**Summary**, from NCBI Gene [4793](https://www.ncbi.nlm.nih.gov/gene/4793):

> The protein encoded by this gene belongs to the NF-kappa-B inhibitor family, which inhibit NF-kappa-B by complexing with, and trapping it in the cytoplasm. Phosphorylation of serine residues on these proteins by kinases marks them for destruction via the ubiquitination pathway, thereby allowing activation of the NF-kappa-B, which translocates to the nucleus to function as a transcription factor. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Jul …

**Accessions** — [HGNC:7798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7798) · Entrez [4793](https://www.ncbi.nlm.nih.gov/gene/4793) · UniProt [Q15653](https://www.uniprot.org/uniprotkb/Q15653) · Ensembl [ENSG00000104825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104825)

## Data

Gene col 2503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2503); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2503]; `tensor/DDL_lfc|DDL_z.npy` [2503]; `embed/gene_vectors.npy` [2503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2503 or target_col == 2503). Every well: [[NFKBIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
