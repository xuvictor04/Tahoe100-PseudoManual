---
symbol: "RBM14"
type: "gene"
col: 14189
ensembl_id: "ENSG00000239306"
name: "RNA binding motif protein 14"
location: "11q13.2"
module: 179
arm: "+"
pooled_cpm: 42.08
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# RBM14

*RNA binding motif protein 14* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.07× (z +9.7, q 2e-19, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.390× (z -12.1, q 6e-31, down in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Estrone sulfate (potassium) (drug)]] 5 µM: 0.736× (z -4.1, q 0.004, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1-1]] (+0.60, fdr 1e-05), [[TRABD]] (+0.56, fdr 1e-05), [[ASB16-AS1]] (+0.56, fdr 1e-05); moves opposite to [[EEA1]] (-0.60, fdr 1e-05), [[KTN1]] (-0.53, fdr 1e-05), [[OSTM1]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +9.7 | 2e-19 | 47/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.9 | 2e-16 | 45/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +8.8 | 3e-16 | 44/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +7.6 | 3e-12 | 40/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +7.3 | 4e-11 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +7.0 | 2e-10 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 2e-07 | 35/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +5.9 | 2e-07 | 36/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 3e-06 | 36/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +5.1 | 2e-05 | 31/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.9 | 5e-05 | 27/47 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.9 | 5e-05 | 27/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 25/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +4.5 | 3e-04 | 31/49 (C32, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 3e-04 | 26/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +4.4 | 4e-04 | 27/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.390×** | -12.1 | 6e-31 | 32/41 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.446×** | -9.6 | 4e-19 | 41/47 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.662×** | -5.1 | 6e-05 | 24/44 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.736×** | -4.1 | 0.004 | 28/48 (CFPAC-1, HOP62, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.718×** | -4.1 | 0.004 | 29/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.009 | 22/48 (NCI-H2347, HS-578T, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.786×** | -3.3 | 0.093 | 15/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Proglumide (drug)]] 0.05 µM |  | 0.800× | -3.0 | 0.18 | 17/47 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.9 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 37.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 39.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.8 | 1 | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.69× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0639× (z -19.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 60.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -13.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 41.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +9.0) | — |
| [[LoVo (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 45.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0702× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 43.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.209× (z -8.9) |
| [[SW1417 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1-1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TRABD]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[NCKIPSD]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ARFGAP1]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[B4GALT3]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[CXXC1]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 | STRING 513 |
| [[TRMT2A]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MGAT1]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PHRF1]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MKRN2]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEA1]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[KTN1]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[OSTM1]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DNAJC8]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[IL6ST]] | -0.50 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[YES1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 | pathway: RUNX2 regulates bone development |
| [[RAD50]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[BMI1]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[DARS1]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NEDD4]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[HADHA]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[VPS13C]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.6, -18.1); signed map (-47.8, -14.7). **Vector** length 81.8, 20.1% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +3.2 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | -0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +4.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,616,626-66,629,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIP, SYTIP1, COAA, DKFZp779J0927 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: RUNX2 regulates bone development; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PK6](https://www.uniprot.org/uniprotkb/Q96PK6) (RNA-binding protein 14):

> Isoform 1 may function as a nuclear receptor coactivator, enhancing transcription through other coactivators such as NCOA6 and CITED1. Isoform 2, functions as a transcriptional repressor, modulating transcriptional activities of coactivators including isoform 1, NCOA6 and CITED1. Regulates centriole biogenesis by suppressing the formation of aberrant centriolar protein complexes in the cytoplasm and thus preserving mitotic spindle integrity. Prevents the formation of the STIL-CPAP complex …

**Summary**, from NCBI Gene [10432](https://www.ncbi.nlm.nih.gov/gene/10432):

> This gene encodes a ribonucleoprotein that functions as a general nuclear coactivator, and an RNA splicing modulator. This protein contains two RNA recognition motifs (RRM) at the N-terminus, and multiple hexapeptide repeat domain at the C-terminus that interacts with thyroid hormone receptor-binding protein (TRBP), and is required for transcription activation. Alternatively spliced transcript variants encoding different isoforms (with opposing effects on transcription) have been described for …

**Accessions** — [HGNC:14219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14219) · Entrez [10432](https://www.ncbi.nlm.nih.gov/gene/10432) · UniProt [Q96PK6](https://www.uniprot.org/uniprotkb/Q96PK6) · Ensembl [ENSG00000239306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239306)

## Data

Gene col 14189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14189); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14189]; `tensor/DDL_lfc|DDL_z.npy` [14189]; `embed/gene_vectors.npy` [14189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14189 or target_col == 14189). Every well: [[RBM14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
