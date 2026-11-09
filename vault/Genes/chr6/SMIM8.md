---
symbol: "SMIM8"
type: "gene"
col: 3293
ensembl_id: "ENSG00000111850"
name: "small integral membrane protein 8"
location: "6q15"
module: 129
arm: "+"
pooled_cpm: 26.95
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# SMIM8

*small integral membrane protein 8* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +11.6, q 3e-28, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.319× (z -14.6, q 1e-45, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VTA1]] (+0.71, fdr 1e-05), [[ZNF559]] (+0.67, fdr 3e-05), [[DHX57]] (+0.65, fdr 1e-05); moves opposite to [[CLOCK]] (-0.55, fdr 7e-05), [[ATP11C]] (-0.55, fdr 7e-05), [[METTL21A]] (-0.54, fdr 5e-05).
> It is in [[Module 129]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +11.6 | 3e-28 | 46/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +10.6 | 6e-24 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +9.4 | 1e-18 | 43/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +7.6 | 3e-12 | 40/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.2 | 5e-08 | 37/47 (KATO III, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +4.6 | 3e-04 | 28/47 (SW480, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.6 | 3e-04 | 28/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +4.2 | 0.002 | 25/47 (HCT15, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.013 | 20/47 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 18/47 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 22/47 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 16/47 (C32, LS 180, …) | two highest doses | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.319×** | -14.6 | 1e-45 | 45/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -13.7 | 4e-40 | 46/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.373×** | -12.6 | 3e-34 | 45/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.400×** | -11.3 | 2e-27 | 38/47 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.420×** | -11.1 | 1e-26 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -10.9 | 1e-25 | 42/47 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.459×** | -9.6 | 7e-20 | 34/47 (A-427, RPMI-7951, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.638×** | -8.1 | 3e-14 | 30/47 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.547×** | -7.7 | 7e-13 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.3 | 2e-08 | 33/47 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.643×** | -5.7 | 8e-07 | 25/46 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -5.5 | 2e-06 | 25/47 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.643×** | -5.4 | 2e-06 | 21/35 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -5.4 | 2e-06 | 27/47 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.692×** | -4.7 | 9e-05 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.010 | 23/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.771×** | -3.2 | 0.039 | 18/47 (A549, C32, …) | top dose only |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.793×** | -3.0 | 0.079 | 14/47 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.0 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 37.5 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0874× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -14.0) |
| [[HOP62 (line)]] | alt | 31.1 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.9) |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -14.7) |
| [[SW480 (line)]] | alt | 29.6 | 2 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.186× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 41.1 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -12.3) |
| [[A549 (line)]] | wt | 28.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -11.8) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.6) |
| [[A-172 (line)]] | wt | 18.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.3) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.172× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0729× (z -13.4) |
| [[J82 (line)]] | alt | 27.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 41.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -10.7) |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -12.1) |
| [[COLO 205 (line)]] | alt | 36.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +21.2) ⚠ cell-cycle shift, explains ~67% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -14.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 25.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 37.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -12.2) |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -10.8) |
| [[A498 (line)]] | wt | 12.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -12.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 58.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -9.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0863× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -8.7) |
| [[H4 (line)]] | wt | 27.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0260× (z -19.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.5) ⚠ cell-cycle shift, explains ~67% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -11.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 26.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.18× (z +9.2) | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 35.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0539× (z -18.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +8.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.260× (z -9.2) |
| [[SW1417 (line)]] | alt | 9.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -8.5) |
| [[SW48 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -9.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTA1]] | +0.71 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZNF559]] | +0.67 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[DHX57]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.65 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[COG2]] | +0.64 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[ZNF329]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF212]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF322]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[TBC1D25]] | +0.62 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[BTBD2]] | +0.62 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ZNF567]] | +0.62 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[ZNF790-AS1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLOCK]] | -0.55 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ATP11C]] | -0.55 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[METTL21A]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN8]] | -0.54 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[B3GALNT2]] | -0.54 | -0.45 / -0.26 | both halves | 3e-04 |  |
| [[SIX4]] | -0.54 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[NFKBID]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[DGKH]] | -0.52 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[RCC2]] | -0.52 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[SLC5A3]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.8, -4.3); signed map (-17.5, -17.1). **Vector** length 89.3, 23.9% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.9 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +11.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:87,322,583-87,399,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586E1923, dJ102H19.2; previously C6orf162 |
| Matched by | ensembl_id |

UniProt [Q96KF7](https://www.uniprot.org/uniprotkb/Q96KF7) carries no function annotation.

**Summary**, from NCBI Gene [57150](https://www.ncbi.nlm.nih.gov/gene/57150):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21401) · Entrez [57150](https://www.ncbi.nlm.nih.gov/gene/57150) · UniProt [Q96KF7](https://www.uniprot.org/uniprotkb/Q96KF7) · Ensembl [ENSG00000111850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111850)

## Data

Gene col 3293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3293); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3293]; `tensor/DDL_lfc|DDL_z.npy` [3293]; `embed/gene_vectors.npy` [3293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3293 or target_col == 3293). Every well: [[SMIM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
