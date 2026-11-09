---
symbol: "VPS39"
type: "gene"
col: 9378
ensembl_id: "ENSG00000166887"
name: "VPS39 subunit of HOPS complex"
location: "15q15.1"
module: 89
arm: "+"
pooled_cpm: 44.15
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# VPS39

*VPS39 subunit of HOPS complex* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.32× (z +8.1, q 3e-13, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.22× (z +3.8, q 0.019, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.477× (z -15.4, q 0e+00, down in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.796× (z -6.7, q 1e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIPAS39]] (+0.70, fdr 7e-06), [[BRAP]] (+0.59, fdr 1e-05), [[ALKBH6]] (+0.58, fdr 2e-05); moves opposite to [[EML4]] (-0.60, fdr 1e-05), [[ADGRL1]] (-0.55, fdr 1e-05), [[UXS1]] (-0.52, fdr 7e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.32×** | +8.1 | 3e-13 | 33/48 (HT-29, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.27×** | +4.6 | 9e-04 | 21/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.019 | 16/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.019 | 13/48 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.056 | 15/48 (HEC-1-A, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.056 | 10/47 (NCI-H23, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.056 | 13/47 (C32, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.065 | 9/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.3 | 0.065 | 16/48 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.076 | 11/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.16× | +3.2 | 0.076 | 10/48 (BT-474, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.16× | +3.2 | 0.076 | 10/49 (SW480, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.1 | 0.089 | 7/48 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.092 | 4/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -15.4 | 0e+00 | 45/47 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.587×** | -11.1 | 3e-26 | 36/48 (NCI-H23, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.616×** | -10.1 | 1e-21 | 40/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -10.1 | 1e-21 | 41/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -9.5 | 2e-19 | 37/47 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.619×** | -9.2 | 3e-18 | 29/43 (A549, HT-29, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.667×** | -8.5 | 2e-15 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -6.7 | 1e-09 | 31/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -6.1 | 9e-08 | 29/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.689×** | -5.9 | 3e-07 | 24/40 (SW480, NCI-H460, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.787×** | -5.0 | 3e-05 | 24/48 (PANC-1, SW 1088, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.656×** | -4.6 | 2e-04 | 24/49 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -4.5 | 4e-04 | 23/48 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.777×** | -4.0 | 0.003 | 20/48 (PANC-1, COLO 205, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.829×** | -3.9 | 0.004 | 20/48 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.788×** | -3.5 | 0.013 | 12/48 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.024 | 11/48 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.033 | 10/48 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.1 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.250× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 51.9 | 0 | 6 (6 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.103× (z -12.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 46.7 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -14.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[hTERT-HPNE (line)]] | wt | 52.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.321× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.385× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 64.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LOX-IMVI (line)]] | wt | 37.8 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0976× (z -10.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 57.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -9.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -9.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0871× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -9.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0747× (z -12.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPAS39]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 | STRING 755 |
| [[BRAP]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ALKBH6]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[IREB2]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 | same gene group; pathway: SARS-CoV-2 Infection; STRING 999 |
| [[RECQL5]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SLC30A6]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GPATCH2]] | +0.56 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[ALKBH3]] | +0.56 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[POLR3F]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 | same gene group |
| [[PSMC2]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZNF419]] | +0.55 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML4]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ADGRL1]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[UXS1]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[H2AZ2]] | -0.51 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ADGRE5]] | -0.51 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[SLAIN1]] | -0.51 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[GAS2L3]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[STIM2]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[STRBP]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[PPAT]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PRKAR2B]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, 17.8); signed map (-8.3, -17.4). **Vector** length 86.4, 19.4% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +6.8 | +8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.5 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.0 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -15.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -1.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | VPS39 subunit of HOPS complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:42,158,701-42,208,307 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0770, VAM6 |
| Gene groups (HGNC) | HOPS complex; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JC1](https://www.uniprot.org/uniprotkb/Q96JC1) (Vam6/Vps39-like protein):

> Regulator of TGF-beta/activin signaling, inhibiting SMAD3- and activating SMAD2-dependent transcription. Acts by interfering with SMAD3/SMAD4 complex formation, this would lead to inhibition of SMAD3-dependent transcription and relieve SMAD3 inhibition of SMAD2-dependent promoters, thus increasing SMAD2-dependent transcription. Does not affect TGF-beta-induced SMAD2 or SMAD3 phosphorylation, nor SMAD2/SMAD4 complex formation.; Plays a role in vesicle-mediated protein trafficking to lysosomal …

**Summary**, from NCBI Gene [23339](https://www.ncbi.nlm.nih.gov/gene/23339):

> This gene encodes a protein that may promote clustering and fusion of late endosomes and lysosomes. The protein may also act as an adaptor protein that modulates the transforming growth factor-beta response by coupling the transforming growth factor-beta receptor complex to the Smad pathway. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:20593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20593) · Entrez [23339](https://www.ncbi.nlm.nih.gov/gene/23339) · UniProt [Q96JC1](https://www.uniprot.org/uniprotkb/Q96JC1) · Ensembl [ENSG00000166887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166887)

## Data

Gene col 9378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9378); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9378]; `tensor/DDL_lfc|DDL_z.npy` [9378]; `embed/gene_vectors.npy` [9378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9378 or target_col == 9378). Every well: [[VPS39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
