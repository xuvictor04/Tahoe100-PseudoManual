---
symbol: "VAC14"
type: "gene"
col: 2309
ensembl_id: "ENSG00000103043"
name: "VAC14 component of PIKFYVE complex"
location: "16q22.1-q22.2"
module: 5
arm: "+"
pooled_cpm: 47.32
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# VAC14

*VAC14 component of PIKFYVE complex* — 16q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.97× (z +12.6, q 1e-33, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.730× (z -5.7, q 7e-06, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.817× (z -5.4, q 2e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.129×, NCI-H23 0.190×, SNU-423 0.223×, CHP-212 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.201×, SNU-423 0.251×, NCI-H2030 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.446×, SW1417 0.499×, C32 0.405×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0916×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0833×); [[Flutamide (drug)]] 0.5 µM in 1 line (BT-474 0.252×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEPD]] (+0.71, fdr 7e-06), [[RBM19]] (+0.67, fdr 7e-06), [[ZFYVE26]] (+0.67, fdr 7e-06); moves opposite to [[LRRC1]] (-0.56, fdr 1e-05), [[SPOPL]] (-0.53, fdr 3e-05), [[CETN3]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +12.6 | 1e-33 | 43/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +11.8 | 1e-29 | 42/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +11.0 | 1e-25 | 41/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +10.8 | 4e-25 | 45/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +9.4 | 5e-19 | 37/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +9.4 | 5e-19 | 40/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +9.0 | 1e-17 | 37/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +8.4 | 4e-15 | 38/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +7.2 | 5e-11 | 30/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.8 | 8e-10 | 33/47 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.44×** | +5.7 | 5e-07 | 25/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.7 | 7e-07 | 24/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +5.6 | 1e-06 | 27/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 22/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +4.3 | 6e-04 | 20/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.2 | 9e-04 | 24/48 (RKO, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.002 | 17/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.004 | 19/49 (J82, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.004 | 13/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.006 | 19/47 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.15× | +3.6 | 0.007 | 15/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2309.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.129×, NCI-H23 0.190×, SNU-423 0.223×, CHP-212 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.201×, SNU-423 0.251×, NCI-H2030 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.446×, SW1417 0.499×, C32 0.405×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0916×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0833×); [[Flutamide (drug)]] 0.5 µM in 1 line (BT-474 0.252×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.730×** | -5.7 | 7e-06 | 27/48 (A549, A-427, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -5.4 | 2e-05 | 25/48 (RPMI-7951, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -4.8 | 3e-04 | 25/48 (SW 1088, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.790×** | -4.3 | 0.003 | 22/47 (SNU-423, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 40.8 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.27× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 57.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 34.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.18× (z +11.5) | — |
| [[A498 (line)]] | wt | 51.3 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +9.7) | — |
| [[RKO (line)]] | wt | 78.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SNU-423 (line)]] | alt | 183 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 3 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0916× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 23.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 27.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 34.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.84× (z +11.3) | — |
| [[LoVo (line)]] | wt | 37.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.62× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.00× (z +10.9) | — |
| [[SW480 (line)]] | alt | 69.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +10.2) | — |
| [[A-427 (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.252× (z -10.0) |
| [[C32 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[J82 (line)]] | alt | 57.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H23 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 30.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.28× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEPD]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[RBM19]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CTNS]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SLC38A7]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MROH1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LYRM4]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SPNS1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KATNIP]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[SLC36A1]] | +0.55 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[SYMPK]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 | same gene group |
| [[SMCR8]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC1]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SPOPL]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CETN3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PLEKHA1]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 | pathway: PI Metabolism |
| [[ORC4]] | -0.52 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CYB5A]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ABHD10]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[RAB11A]] | -0.48 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.47 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[GEMIN2]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CAND1]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 | same gene group |
| [[KBTBD7]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.2, 12.0); signed map (-8.7, -20.4). **Vector** length 113, 30.2% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +11.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.4 | +10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.0 | +9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +7.2 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.0 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.1 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.2 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.5 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | VAC14 component of PIKFYVE complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1-q22.2 — chr16:70,687,439-70,801,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10305, ArPIKfyve; previously TAX1BP2 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08AM6](https://www.uniprot.org/uniprotkb/Q08AM6) (Protein VAC14 homolog):

> Scaffold protein component of the PI(3,5)P2 regulatory complex which regulates both the synthesis and turnover of phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2). Pentamerizes into a star-shaped structure and nucleates the assembly of the complex. The pentamer binds a single copy each of PIKFYVE and FIG4 and coordinates both PIKfyve kinase activity and FIG4 phosphatase activity, being required to maintain normal levels of phosphatidylinositol 3-phosphate (PtdIns(3)P) and …

**Summary**, from NCBI Gene [55697](https://www.ncbi.nlm.nih.gov/gene/55697):

> This gene encodes a scaffold protein that is a component of the PIKfyve protein kinase complex. This complex is responsible for the synthesis of phosphatidylinositol 3,5-bisphosphate, an important component of cellular membranes, from phosphatidylinositol 3-phosphate. Mice lacking a functional copy of this gene exhibit severe neurodegeneration. Mutations in the human gene have been identified in patients with a childhood onset progressive neurological disorder characterized by impaired …

**Accessions** — [HGNC:25507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25507) · Entrez [55697](https://www.ncbi.nlm.nih.gov/gene/55697) · UniProt [Q08AM6](https://www.uniprot.org/uniprotkb/Q08AM6) · Ensembl [ENSG00000103043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103043)

## Data

Gene col 2309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2309); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2309]; `tensor/DDL_lfc|DDL_z.npy` [2309]; `embed/gene_vectors.npy` [2309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2309 or target_col == 2309). Every well: [[VAC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
