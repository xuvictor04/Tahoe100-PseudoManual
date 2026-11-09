---
symbol: "IPO8"
type: "gene"
col: 5467
ensembl_id: "ENSG00000133704"
name: "importin 8"
location: "12p11.21"
module: 25
arm: "+"
pooled_cpm: 58.86
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# IPO8

*importin 8* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.57× (z +11.0, q 1e-25, up in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.16× (z +3.6, q 0.070, up in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 2.19×, SNU-423 2.63×, KATO III 2.40×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 3.30×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.563× (z -19.8, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC21]] (+0.71, fdr 7e-06), [[FAM98B]] (+0.71, fdr 7e-06), [[DLAT]] (+0.70, fdr 7e-06); moves opposite to [[HIC2]] (-0.65, fdr 7e-06), [[INAFM1]] (-0.64, fdr 7e-06), [[FAU]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5467.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 2.19×, SNU-423 2.63×, KATO III 2.40×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 3.30×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +11.0 | 1e-25 | 33/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.8 | 2e-20 | 28/43 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.070 | 10/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.072 | 19/45 (A-172, RPMI-7951, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.4 | 0.072 | 0/49 | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.072 | 12/47 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.15× | +3.2 | 0.100 | 7/48 (NCI-H2347, LoVo, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.18 | 12/47 (NCI-H2030, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -19.8 | 0e+00 | 39/48 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -13.4 | 1e-38 | 31/48 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.606×** | -12.2 | 4e-32 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -12.1 | 1e-31 | 39/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -12.1 | 2e-31 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.617×** | -11.8 | 4e-30 | 38/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -11.2 | 3e-27 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -9.0 | 2e-17 | 32/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -8.7 | 2e-16 | 34/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -8.7 | 3e-16 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.779×** | -6.1 | 5e-08 | 27/48 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -6.0 | 7e-08 | 27/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -6.0 | 8e-08 | 23/49 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.653×** | -5.4 | 2e-06 | 25/48 (SW480, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -5.2 | 8e-06 | 22/47 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.9 | 0.004 | 9/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.012 | 12/47 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 85.4 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 44.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -15.6) |
| [[SHP-77 (line)]] | alt | 195 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -19.7) |
| [[LS 180 (line)]] | wt | 80.1 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -17.0) |
| [[J82 (line)]] | alt | 44.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.3) |
| [[LoVo (line)]] | wt | 96.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -22.1) |
| [[SW 900 (line)]] | alt | 115 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.1) |
| [[PANC-1 (line)]] | alt | 67.6 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 80.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.409× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.420× (z -10.4) |
| [[KATO III (line)]] | alt | 50.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -13.1) |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.1) |
| [[HOP62 (line)]] | alt | 80.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -8.9) |
| [[RKO (line)]] | wt | 86.3 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -15.6) |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -11.3) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.4) |
| [[A-427 (line)]] | wt | 76.0 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.427× (z -11.0) |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.9) |
| [[HT-29 (line)]] | alt | 55.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.6) |
| [[SNU-423 (line)]] | alt | 47.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.2) |
| [[A-172 (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.8) |
| [[A549 (line)]] | wt | 54.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.8) |
| [[C32 (line)]] | wt | 56.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0829× (z -14.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 56.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -15.5) |
| [[SW1417 (line)]] | alt | 40.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC21]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[DLAT]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[API5]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[DLD]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[OCRL]] | +0.68 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[PFKM]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MRPL19]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 | STRING 578 |
| [[ATIC]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[AIFM1]] | +0.65 | +0.43 / +0.71 | both halves | 4e-05 |  |
| [[CCT2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIC2]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[FAU]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 | STRING 931 |
| [[SNHG9]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CATSPERG]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[LINC00685]] | -0.62 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[FKBP2]] ⚠ | -0.62 | -0.51 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[STX5]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FBXL12]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[BRI3]] | -0.61 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[SERF2]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[RBM38]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[RABAC1]] | -0.59 | -0.40 / -0.63 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IPO8's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SMBD1P]] | C | SMBD1P activity lowers IPO8's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.01× higher at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.1, -34.9); signed map (-16.4, -43.9). **Vector** length 102, 25.4% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.7 |
|  | [[NG25 (drug)]] 5 µM |  | +4.0 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -19.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | -11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -12.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | importin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:30,628,988-30,695,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP8; previously RANBP8 |
| Gene groups (HGNC) | Importins |
| Reactome | 2 pathways, smallest: Transcriptional regulation by small RNAs; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O15397](https://www.uniprot.org/uniprotkb/O15397) (Importin-8):

> Involved in nuclear protein import, either by acting as autonomous nuclear transport receptor or as an adapter-like protein in association with the importin-beta subunit KPNB1. Acting autonomously, may serve as receptor for nuclear localization signals (NLS) and promote translocation of import substrates through the nuclear pore complex (NPC) by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin, the importin/substrate complex dissociates …

**Summary**, from NCBI Gene [10526](https://www.ncbi.nlm.nih.gov/gene/10526):

> The importin-alpha/beta complex and the GTPase Ran mediate nuclear import of proteins with a classical nuclear localization signal. The protein encoded by this gene is a member of a class of approximately 20 potential Ran targets that share a sequence motif related to the Ran-binding site of importin-beta. This protein binds to the nuclear pore complex and, along with RanGTP and RANBP1, inhibits the GAP stimulation of the Ran GTPase. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:9853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9853) · Entrez [10526](https://www.ncbi.nlm.nih.gov/gene/10526) · UniProt [O15397](https://www.uniprot.org/uniprotkb/O15397) · Ensembl [ENSG00000133704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133704)

## Data

Gene col 5467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5467); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5467]; `tensor/DDL_lfc|DDL_z.npy` [5467]; `embed/gene_vectors.npy` [5467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5467 or target_col == 5467). Every well: [[IPO8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
