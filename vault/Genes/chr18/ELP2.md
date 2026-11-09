---
symbol: "ELP2"
type: "gene"
col: 5600
ensembl_id: "ENSG00000134759"
name: "elongator acetyltransferase complex subunit 2"
location: "18q12.2"
module: 40
arm: "+"
pooled_cpm: 128.57
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ELP2

*elongator acetyltransferase complex subunit 2* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.54× (z +5.9, q 2e-06, up in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +5.6, q 5e-06, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.347× (z -14.0, q 1e-41, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM: 0.721× (z -4.5, q 8e-04, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAX]] (+0.82, fdr 7e-06), [[SRP54-AS1]] (+0.78, fdr 7e-06), [[MALSU1]] (+0.74, fdr 7e-06); moves opposite to [[ZNF655]] (-0.69, fdr 7e-06), [[TRIP12]] (-0.69, fdr 7e-06), [[MAPRE1]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00857]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.9 | 2e-06 | 36/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +5.6 | 5e-06 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +4.3 | 0.003 | 34/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.9 | 0.016 | 30/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.028 | 28/48 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.24 | 27/48 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -14.0 | 1e-41 | 43/44 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.455×** | -10.2 | 6e-22 | 47/49 (RPMI-7951, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -7.0 | 6e-10 | 37/45 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.721×** | -4.5 | 8e-04 | 36/49 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.724×** | -4.4 | 8e-04 | 35/49 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.724×** | -4.4 | 8e-04 | 35/48 (H4, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.739×** | -4.2 | 0.002 | 32/49 (A498, HOP62, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.740×** | -4.1 | 0.002 | 32/48 (A-172, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.741×** | -4.1 | 0.002 | 37/49 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.752×** | -3.9 | 0.005 | 36/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.776×** | -3.5 | 0.026 | 31/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.831×** | -3.4 | 0.027 | 20/49 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.4 | 0.028 | 28/48 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.039 | 22/48 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.053 | 22/48 (SW48, LS 180, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.053 | 25/48 (SHP-77, SW 1088, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.053 | 23/48 (Hs 766T, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.054 | 26/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.060 | 26/48 (NCI-H460, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 118 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 131 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.52× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 160 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -18.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -12.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -14.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.62× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.0615× (z -24.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -20.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -16.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 99.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 91.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0640× (z -13.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAX]] | +0.82 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.74 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[DUXAP10]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[AFMID]] | +0.74 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MMS19]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MHENCR]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.71 | +0.78 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.69 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.68 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[TUG1]] | -0.67 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PURB]] | -0.66 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[SOCS4]] | -0.65 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[LIG4]] | -0.65 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RBM12]] | -0.65 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ZC3H4]] | -0.65 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[WDR1]] | -0.64 | -0.50 / -0.65 | both halves | 1e-05 | same gene group |
| [[TASOR]] | -0.64 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00857]] | B | LINC00857 activity lowers ELP2's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.36× higher at baseline in the lines without LINC00857 | 0.032 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (1.5, -18.9); signed map (-41.9, 12.0). **Vector** length 129, 49.5% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.7 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +3.1 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.8 | -4.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.4 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:36,129,444-36,180,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10879, StIP; previously STATIP1 |
| Gene groups (HGNC) | WD repeat domain containing; Elongator acetyltransferase complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IA86](https://www.uniprot.org/uniprotkb/Q6IA86) (Elongator complex protein 2):

> Component of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). The elongator complex catalyzes the formation of carboxymethyluridine in the wobble base at position 34 in tRNAs.

**Summary**, from NCBI Gene [55250](https://www.ncbi.nlm.nih.gov/gene/55250):

> The protein encoded by this gene is a core subunit of the elongator complex, a histone acetyltransferase complex that associates with RNA polymerase II. In addition to histone acetylation, the encoded protein effects transcriptional elongation and may help remodel chromatin. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:18248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18248) · Entrez [55250](https://www.ncbi.nlm.nih.gov/gene/55250) · UniProt [Q6IA86](https://www.uniprot.org/uniprotkb/Q6IA86) · Ensembl [ENSG00000134759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134759)

## Data

Gene col 5600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5600); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5600]; `tensor/DDL_lfc|DDL_z.npy` [5600]; `embed/gene_vectors.npy` [5600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5600 or target_col == 5600). Every well: [[ELP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
