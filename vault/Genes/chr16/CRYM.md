---
symbol: "CRYM"
type: "gene"
col: 2351
ensembl_id: "ENSG00000103316"
name: "crystallin mu"
location: "16p12.2"
module: 125
arm: "+"
pooled_cpm: 14.87
n_lines_expressing: 38
n_dd_up: 61
n_dd_down: 0
n_dd_up_clean: 53
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 11
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# CRYM

*crystallin mu* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 61 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.5× (z +35.1, q 0e+00, up in 35 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0573×, RPMI-7951 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.110×, RKO 0.164×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 2 lines (J82 0.107×, A-172 0.250×; ⚠ cell-cycle shift, explains ~6% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.159×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0914×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02154]] (+0.70, fdr 7e-06), [[HDAC9]] (+0.68, fdr 7e-06), [[ENTHD1]] (+0.68, fdr 7e-06); moves opposite to [[RANBP9]] (-0.60, fdr 1e-05), [[SETD3]] (-0.57, fdr 1e-05), [[NCAPD3]] (-0.57, fdr 1e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ENTHD1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PPP1R15A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 61 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.5×** | +35.1 | 0e+00 | 35/35 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.57×** | +22.2 | 0e+00 | 34/34 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.37×** | +19.6 | 0e+00 | 34/35 (LoVo, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.44×** | +14.1 | 9e-43 | 34/36 (COLO 205, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.10×** | +13.8 | 2e-41 | 33/36 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +11.9 | 1e-30 | 30/34 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.44×** | +11.7 | 2e-29 | 24/30 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.87×** | +10.3 | 4e-23 | 28/34 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.34×** | +8.3 | 5e-15 | 28/35 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.30×** | +8.2 | 2e-14 | 29/36 (A498, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.18×** | +7.6 | 1e-12 | 21/36 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +7.5 | 4e-12 | 17/36 (HepG2/C3A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.11×** | +7.3 | 1e-11 | 26/36 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.06×** | +7.1 | 5e-11 | 23/36 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +6.9 | 3e-10 | 26/35 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +6.4 | 7e-09 | 17/35 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +6.2 | 2e-08 | 17/36 (AsPC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **3.32×** | +6.2 | 2e-08 | 27/35 (A498, COLO 205, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2351.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.0573×, RPMI-7951 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.110×, RKO 0.164×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 2 lines (J82 0.107×, A-172 0.250×; ⚠ cell-cycle shift, explains ~6% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.159×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0914×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.692× | -3.6 | 0.13 | 13/36 (H4, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.704× | -3.5 | 0.13 | 14/36 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.699× | -3.4 | 0.13 | 11/34 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.698× | -3.3 | 0.14 | 10/34 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.2 | 0.14 | 7/36 (SNU-423, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.3 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.2× (z +22.1) | — |
| [[A-172 (line)]] | wt | 78.3 | 8 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +24.8) | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 21.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +23.1) | — |
| [[COLO 205 (line)]] | alt | 12.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 182× (z +23.3) | — |
| [[HS-578T (line)]] | alt | 24.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +20.0) | — |
| [[RKO (line)]] | wt | 76.9 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -15.7) |
| [[A498 (line)]] | wt | 17.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +20.2) | — |
| [[hTERT-HPNE (line)]] | wt | 52.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +23.0) | — |
| [[Hs 766T (line)]] | wt | 28.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +18.9) | — |
| [[SW48 (line)]] | wt | 48.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.5× (z +22.9) | — |
| [[HEC-1-A (line)]] | alt | 5.29 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +17.2) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0914× (z -9.0) |
| [[KATO III (line)]] | alt | 6.29 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 26.4× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 11.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +13.8) | — |
| [[LoVo (line)]] | wt | 11.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +22.7) | — |
| [[LS 180 (line)]] | wt | 6.42 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 9.79 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 26.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +17.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0506× (z -14.2) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 6.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 5.12 | 2 | 0 | [[Auranofin (drug)]] 5 µM 46.6× (z +12.8) | — |
| [[J82 (line)]] | alt | 15.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.3) | [[Belinostat (drug)]] 0.5 µM 0.107× (z -10.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[LOX-IMVI (line)]] | wt | 8.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.9× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +18.5) | — |
| [[A549 (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 3.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +9.7) | — |
| [[A-427 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02154]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[HDAC9]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ENTHD1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RRAGC-DT]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | +0.63 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[ABCA15P]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 | ⚠ same locus (12.8 kb: neighbours can correlate without regulation) |
| [[LINC00520]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LINC00944]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GEM]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.60 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[GNPDA1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP9]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SETD3]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZDHHC3]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ACTL6A]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CNOT6L]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MTRR]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 | same gene group; pathway: Metabolism of amino acids and derivatives |
| [[LRRC1]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PIGS]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SPAST]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RPA1]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTHD1]] | B | ENTHD1 activity raises CRYM's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without ENTHD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[NGF]] | B | NGF activity raises CRYM's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without NGF | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[LINC02154]] | B | LINC02154 activity raises CRYM's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 2.38× lower at baseline in the lines without LINC02154 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |
| [[LINC00504]] | B | LINC00504 activity raises CRYM's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.03× lower at baseline in the lines without LINC00504 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[IGFN1]] | B | IGFN1 activity raises CRYM's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without IGFN1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[LINC00520]] | B | LINC00520 activity raises CRYM's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without LINC00520 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[C12orf50]] | B | C12orf50 activity raises CRYM's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 2.37× lower at baseline in the lines without C12orf50 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises CRYM's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without ROR1-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[LINC01705]] | B | LINC01705 activity raises CRYM's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without LINC01705 | 0.055 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[GEM]] | B | GEM activity raises CRYM's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.45× lower at baseline in the lines without GEM | 0.060 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[LINC01828]] | B | LINC01828 activity raises CRYM's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without LINC01828 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |
| [[PNLIPRP3]] | B | PNLIPRP3 activity raises CRYM's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without PNLIPRP3 | 0.063 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R15A]] | B | CRYM activity raises PPP1R15A's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.60× lower at baseline in the lines without CRYM | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[IL6R]] | B | CRYM activity raises IL6R's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without CRYM | 0.018 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[MTRR]] | B | CRYM activity lowers MTRR's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without CRYM | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[OSGIN1]] | B | CRYM activity raises OSGIN1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without CRYM | 0.053 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[ENTHD1]] | B | CRYM activity raises ENTHD1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without CRYM | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[SPINK1]] | B | CRYM activity raises SPINK1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without CRYM | 0.073 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[NCAPD3]] | B | CRYM activity lowers NCAPD3's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without CRYM | 0.074 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[TM4SF19]] | B | CRYM activity raises TM4SF19's level | lines that do not express CRYM (12) vs lines expressing it (38) | 3.61× lower at baseline in the lines without CRYM | 0.077 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[ATP6V0D2]] | B | CRYM activity raises ATP6V0D2's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without CRYM | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[ZBTB43]] | B | CRYM activity raises ZBTB43's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without CRYM | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[MAPK6]] | B | CRYM activity raises MAPK6's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without CRYM | 0.093 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 21.4); signed map (37.8, 21.8). **Vector** length 114, 32.0% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +19.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +22.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +7.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -3.4 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +5.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | crystallin mu |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:21,238,874-21,303,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DFNA40 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 2 pathways, smallest: Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14894](https://www.uniprot.org/uniprotkb/Q14894) (Ketimine reductase mu-crystallin):

> Catalyzes the NAD(P)H-dependent reduction of imine double bonds of a number of cyclic ketimine substrates, including sulfur-containing cyclic ketimines. Under physiological conditions, it efficiently catalyzes delta(1)-piperideine-2-carboxylate (P2C) and delta(1)-pyrroline-2-carboxylate (Pyr2C) reduction, suggesting a central role in lysine and glutamate metabolism. Additional substrates are delta(2)-thiazoline-2-carboxylate (T2C), 3,4-dehydrothiomorpholine-3-carboxylate (AECK), and …

**Summary**, from NCBI Gene [1428](https://www.ncbi.nlm.nih.gov/gene/1428):

> Crystallins are separated into two classes: taxon-specific and ubiquitous. The former class is also called phylogenetically-restricted crystallins. The latter class constitutes the major proteins of vertebrate eye lens and maintains the transparency and refractive index of the lens. This gene encodes a taxon-specific crystallin protein that binds NADPH and has sequence similarity to bacterial ornithine cyclodeaminases. The encoded protein does not perform a structural role in lens tissue, and …

**Accessions** — [HGNC:2418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2418) · Entrez [1428](https://www.ncbi.nlm.nih.gov/gene/1428) · UniProt [Q14894](https://www.uniprot.org/uniprotkb/Q14894) · Ensembl [ENSG00000103316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103316)

## Data

Gene col 2351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2351); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2351]; `tensor/DDL_lfc|DDL_z.npy` [2351]; `embed/gene_vectors.npy` [2351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2351 or target_col == 2351). Every well: [[CRYM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
