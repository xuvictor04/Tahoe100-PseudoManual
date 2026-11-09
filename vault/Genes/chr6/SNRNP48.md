---
symbol: "SNRNP48"
type: "gene"
col: 9670
ensembl_id: "ENSG00000168566"
name: "small nuclear ribonucleoprotein U11/U12 subunit 48"
location: "6p24.3"
module: 30
arm: "+"
pooled_cpm: 36.47
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SNRNP48

*small nuclear ribonucleoprotein U11/U12 subunit 48* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.12× (z +24.2, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.0969×, SW48 0.156×, AN3 CA 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.109×, SNU-1 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[8-Hydroxyquinoline (drug)]] 5 µM in 1 line (CHP-212 0.197×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (H4 0.354×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF20]] (+0.70, fdr 7e-06), [[CDC40]] (+0.64, fdr 7e-06), [[STX7]] (+0.63, fdr 4e-05); moves opposite to [[MORN1]] (-0.58, fdr 4e-05), [[MBD3]] (-0.57, fdr 5e-05), [[TRNT1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.12×** | +24.2 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +23.2 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +20.2 | 0e+00 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +11.3 | 2e-27 | 31/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +9.8 | 1e-20 | 37/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.8 | 1e-20 | 32/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.7 | 3e-20 | 39/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +8.9 | 4e-17 | 38/48 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +8.9 | 4e-17 | 38/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +8.8 | 6e-17 | 34/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +8.8 | 9e-17 | 37/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.81×** | +6.6 | 3e-09 | 30/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +6.5 | 5e-09 | 32/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.4 | 2e-06 | 23/43 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 4e-06 | 24/47 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 7e-06 | 24/48 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9670.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.0969×, SW48 0.156×, AN3 CA 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW48 0.109×, SNU-1 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[8-Hydroxyquinoline (drug)]] 5 µM in 1 line (CHP-212 0.197×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (H4 0.354×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.9 | 0.039 | 16/48 (HCT15, CFPAC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -3.8 | 0.039 | 17/48 (H4, HS-578T, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.847× | -3.6 | 0.057 | 12/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.891× | -3.5 | 0.057 | 9/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.854× | -3.4 | 0.077 | 10/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.902× | -3.1 | 0.15 | 4/48 (NCI-H1573, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.17 | 13/47 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 45.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.5) | — |
| [[KATO III (line)]] | alt | 47.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +14.6) | — |
| [[PANC-1 (line)]] | alt | 30.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +13.8) | — |
| [[A549 (line)]] | wt | 25.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 41.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.81× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 44.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 41.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +13.3) | — |
| [[J82 (line)]] | alt | 39.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[LoVo (line)]] | wt | 40.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 76.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 45.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +12.5) | — |
| [[RKO (line)]] | wt | 35.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 49.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 41.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +13.1) | — |
| [[SW480 (line)]] | alt | 54.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +18.3) | — |
| [[A498 (line)]] | wt | 21.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 43.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.37× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 37.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 40.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.00× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 58.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A-427 (line)]] | wt | 24.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 5 µM 0.197× (z -9.0) |
| [[H4 (line)]] | wt | 30.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.354× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF20]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CDC40]] | +0.64 | +0.69 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 715 |
| [[STX7]] | +0.63 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[SUGT1]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[UBR2]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CCDC112]] | +0.59 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[ABCD4]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.59 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MFSD9]] | +0.58 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NFRKB]] | +0.58 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[CALCOCO2]] | +0.58 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN1]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MBD3]] | -0.57 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[TRNT1]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SNRPB]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 930 |
| [[E2F3]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[HNRNPAB]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SATB2]] | -0.55 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[C10orf88B]] | -0.54 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[SLFNL1-AS1]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DDX5]] | -0.54 | -0.36 / -0.51 | both halves | 9e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[HIVEP1]] | -0.52 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[NFKB1]] | -0.52 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-18.6, -6.3); signed map (-27.2, -19.5). **Vector** length 91.6, 21.4% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +8.8 |
|  | [[NG25 (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U11/U12 subunit 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,590,198-7,611,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32234, dJ512B11.2, dJ336K20B.1; previously C6orf151 |
| Gene groups (HGNC) | U11/U12 di-snRNP; U11 small nuclear ribonucleoprotein; Zinc fingers U11-48K-like CHHC-type |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IEG0](https://www.uniprot.org/uniprotkb/Q6IEG0) (U11/U12 small nuclear ribonucleoprotein 48 kDa protein):

> Likely involved in U12-type 5' splice site recognition.

**Summary**, from NCBI Gene [154007](https://www.ncbi.nlm.nih.gov/gene/154007):

> Predicted to enable zinc ion binding activity. Predicted to be involved in spliceosome conformational change to release U4 (or U4atac) and U1 (or U11). Located in nucleoplasm. Part of U12-type spliceosomal complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21368) · Entrez [154007](https://www.ncbi.nlm.nih.gov/gene/154007) · UniProt [Q6IEG0](https://www.uniprot.org/uniprotkb/Q6IEG0) · Ensembl [ENSG00000168566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168566)

## Data

Gene col 9670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9670); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9670]; `tensor/DDL_lfc|DDL_z.npy` [9670]; `embed/gene_vectors.npy` [9670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9670 or target_col == 9670). Every well: [[SNRNP48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
