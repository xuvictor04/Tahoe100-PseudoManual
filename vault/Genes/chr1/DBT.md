---
symbol: "DBT"
type: "gene"
col: 6104
ensembl_id: "ENSG00000137992"
name: "dihydrolipoamide branched chain transacylase E2"
location: "1p21.2"
module: 28
arm: "+"
pooled_cpm: 28.99
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DBT

*dihydrolipoamide branched chain transacylase E2* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +12.0, q 3e-30, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.439× (z -15.3, q 0e+00, down in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.454× (z -14.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT12]] (+0.69, fdr 7e-06), [[ABITRAM]] (+0.68, fdr 7e-06), [[ZSCAN26]] (+0.68, fdr 9e-06); moves opposite to [[SLC6A16]] (-0.56, fdr 2e-05), [[TAF4]] (-0.55, fdr 3e-05), [[ATP1B3]] (-0.53, fdr 6e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +12.0 | 3e-30 | 43/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +11.1 | 3e-26 | 44/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +8.1 | 9e-14 | 36/48 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +7.8 | 8e-13 | 30/48 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.0 | 2e-10 | 29/45 (LoVo, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.6 | 2e-06 | 28/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.3 | 1e-05 | 21/38 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.7 | 2e-04 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 0.001 | 18/48 (H4, C-33 A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 18/48 (NCI-H2347, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.004 | 16/47 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.013 | 16/48 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.016 | 12/48 (A-172, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.041 | 12/47 (hTERT-HPNE, C32, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.042 | 9/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.042 | 9/48 (HT-29, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.048 | 10/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.082 | 8/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -15.3 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -14.7 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -11.5 | 2e-28 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -11.3 | 2e-27 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -11.3 | 2e-27 | 38/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.469×** | -7.4 | 2e-11 | 31/48 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.694×** | -6.8 | 8e-10 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.735×** | -5.7 | 7e-07 | 29/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.703×** | -4.7 | 2e-04 | 18/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.779×** | -4.6 | 2e-04 | 20/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[EX229 (drug)]] 5 µM |  | **0.653×** | -4.1 | 0.002 | 16/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.826×** | -3.4 | 0.035 | 12/48 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.039 | 15/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -3.3 | 0.039 | 13/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.048 | 14/47 (HCT15, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.3 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.158× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -19.4) |
| [[SW480 (line)]] | alt | 44.1 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.160× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 31.4 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.370× (z -10.5) |
| [[HT-29 (line)]] | alt | 30.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +8.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -12.1) |
| [[SNU-423 (line)]] | alt | 33.2 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -12.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -10.9) ⚠ toxic |
| [[H4 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -11.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0903× (z -11.3) |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -8.7) |
| [[J82 (line)]] | alt | 31.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.250× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -9.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0794× (z -13.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT12]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZSCAN26]] | +0.68 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[DDX1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[COPS5]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.66 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[RBM18]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SLC25A46]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MKS1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A16]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TAF4]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ATP1B3]] | -0.53 | -0.60 / -0.22 | both halves | 6e-04 | pathway: HALLMARK_ADIPOGENESIS |
| [[AGAP3]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.3, 2.3); signed map (6.9, -25.8). **Vector** length 76.0, 15.8% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -15.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | dihydrolipoamide branched chain transacylase E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,186,919-100,249,834 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCOADC-E2, BCKAD-E2, BCKDH-E2 |
| Gene groups (HGNC) | Branched chain alpha-keto acid dehydrogenase complex subunits; Acyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 17 pathways, smallest: Loss-of-function mutations in BCKDHA or BCKDHB cause MSUD; BCKDH synthesizes BCAA-CoA from KIC, KMVA, KIV; Loss-of-function mutations in DBT cause MSUD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P11182](https://www.uniprot.org/uniprotkb/P11182) (Lipoamide acyltransferase component of branched-chain alpha-keto acid dehydrogenase complex, mitochondrial):

> The branched-chain alpha-keto dehydrogenase complex catalyzes the overall conversion of alpha-keto acids to acyl-CoA and CO(2). It contains multiple copies of three enzymatic components: branched-chain alpha-keto acid decarboxylase (E1), lipoamide acyltransferase (E2) and lipoamide dehydrogenase (E3). Within this complex, the catalytic function of this enzyme is to accept, and to transfer to coenzyme A, acyl groups that are generated by the branched-chain alpha-keto acid decarboxylase component.

**Summary**, from NCBI Gene [1629](https://www.ncbi.nlm.nih.gov/gene/1629):

> The branched-chain alpha-keto acid dehydrogenase complex (BCKD) is an inner-mitochondrial enzyme complex involved in the breakdown of the branched-chain amino acids isoleucine, leucine, and valine. The BCKD complex is thought to be composed of a core of 24 transacylase (E2) subunits, and associated decarboxylase (E1), dehydrogenase (E3), and regulatory subunits. This gene encodes the transacylase (E2) subunit. Mutations in this gene result in maple syrup urine disease, type 2. Alternatively …

**Accessions** — [HGNC:2698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2698) · Entrez [1629](https://www.ncbi.nlm.nih.gov/gene/1629) · UniProt [P11182](https://www.uniprot.org/uniprotkb/P11182) · Ensembl [ENSG00000137992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137992)

## Data

Gene col 6104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6104); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6104]; `tensor/DDL_lfc|DDL_z.npy` [6104]; `embed/gene_vectors.npy` [6104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6104 or target_col == 6104). Every well: [[DBT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
