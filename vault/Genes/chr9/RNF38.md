---
symbol: "RNF38"
type: "gene"
col: 5964
ensembl_id: "ENSG00000137075"
name: "ring finger protein 38"
location: "9p13.2"
module: 163
arm: "+"
pooled_cpm: 142.3
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# RNF38

*ring finger protein 38* — 9p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.426× (z -16.5, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.612× (z -9.5, q 3e-19, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GIT1]] (+0.75, fdr 7e-06), [[STRN]] (+0.74, fdr 7e-06), [[UBE2G1]] (+0.72, fdr 7e-06); moves opposite to [[MYSM1]] (-0.67, fdr 1e-05), [[ARCN1]] (-0.65, fdr 1e-05), [[THUMPD3]] (-0.64, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +3.4 | 0.34 | 21/47 (H4, SW480, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.37× | +3.0 | 0.65 | 19/48 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -16.5 | 0e+00 | 47/49 (HCT15, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.419×** | -16.1 | 0e+00 | 43/44 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -10.7 | 2e-24 | 41/45 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -9.5 | 3e-19 | 41/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.624×** | -9.1 | 1e-17 | 44/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.613×** | -9.1 | 1e-17 | 44/48 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -7.6 | 3e-12 | 39/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.704×** | -6.8 | 9e-10 | 36/48 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.809×** | -5.8 | 5e-07 | 23/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -5.0 | 3e-05 | 31/49 (A-172, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 9e-04 | 29/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.1 | 0.002 | 20/48 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.807×** | -4.0 | 0.003 | 25/47 (C32, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -3.9 | 0.004 | 26/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.867× | -3.9 | 0.004 | 8/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -3.1 | 0.059 | 17/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 149 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 225 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -15.6) |
| [[HOP62 (line)]] | alt | 147 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -12.5) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -10.3) |
| [[J82 (line)]] | alt | 203 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -15.2) |
| [[Hs 766T (line)]] | wt | 172 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -10.6) |
| [[SNU-423 (line)]] | alt | 140 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -11.4) |
| [[HS-578T (line)]] | alt | 121 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 209 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -17.8) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -11.5) |
| [[A549 (line)]] | wt | 149 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.8) |
| [[C32 (line)]] | wt | 94.8 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -10.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -17.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 197 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -8.8) |
| [[SW480 (line)]] | alt | 166 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.516× (z -11.0) |
| [[A498 (line)]] | wt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -15.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -20.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 85.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 64.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.381× (z -10.4) |
| [[PANC-1 (line)]] | alt | 241 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -14.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -9.9) |
| [[CHP-212 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0738× (z -16.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.397× (z -13.1) |
| [[KATO III (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -16.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -15.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 174 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -16.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -21.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 86.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -11.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -12.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 117 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.276× (z -11.0) |
| [[BT-474 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIT1]] | +0.75 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[STRN]] | +0.74 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[SMG1P5]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[CYTH3]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[TSPAN17]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[RAP1A]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ABHD12]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYSM1]] | -0.67 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.65 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[THUMPD3]] | -0.64 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.63 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[USP40]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[CWC22]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[LINC00460]] | -0.60 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.59 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[RAD50]] | -0.59 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[TRMT13]] | -0.58 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[USP16]] | -0.58 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[KICS2]] | -0.58 | -0.68 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.2, -6.4); signed map (-41.3, -1.1). **Vector** length 110, 35.8% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.7 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -6.5 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:36,336,396-36,487,548 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0F5](https://www.uniprot.org/uniprotkb/Q9H0F5) (E3 ubiquitin-protein ligase RNF38):

> Acts as an E3 ubiquitin-protein ligase able to ubiquitinate p53/TP53 which promotes its relocalization to discrete foci associated with PML nuclear bodies. Exhibits preference for UBE2D2 as a E2 enzyme.

**Summary**, from NCBI Gene [152006](https://www.ncbi.nlm.nih.gov/gene/152006):

> This gene encodes a protein with a coiled-coil motif and a RING-H2 motif (C3H2C2) at its carboxy-terminus. The RING motif is a zinc-binding domain found in a large set of proteins playing roles in diverse cellular processes including oncogenesis, development, signal transduction, and apoptosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:18052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18052) · Entrez [152006](https://www.ncbi.nlm.nih.gov/gene/152006) · UniProt [Q9H0F5](https://www.uniprot.org/uniprotkb/Q9H0F5) · Ensembl [ENSG00000137075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137075)

## Data

Gene col 5964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5964); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5964]; `tensor/DDL_lfc|DDL_z.npy` [5964]; `embed/gene_vectors.npy` [5964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5964 or target_col == 5964). Every well: [[RNF38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
