---
symbol: "FILIP1L"
type: "gene"
col: 9638
ensembl_id: "ENSG00000168386"
name: "filamin A interacting protein 1 like"
location: "3q12.1"
module: 66
arm: "+"
pooled_cpm: 27.94
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# FILIP1L

*filamin A interacting protein 1 like* — 3q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.86× (z +35.9, q 0e+00, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0881×); [[Silodosin (drug)]] 0.05 µM in 1 line (SW48 0.0691×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMO]] (+0.60, fdr 2e-05), [[RIPK2-DT]] (+0.60, fdr 1e-05), [[DUSP16]] (+0.60, fdr 1e-05); moves opposite to [[ANKRD13D]] (-0.61, fdr 1e-05), [[ATG16L1]] (-0.57, fdr 3e-05), [[SAP130]] (-0.55, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.86×** | +35.9 | 0e+00 | 42/47 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.96×** | +20.4 | 0e+00 | 38/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +16.4 | 0e+00 | 30/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +10.1 | 1e-21 | 28/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.2 | 4e-18 | 24/40 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.2 | 2e-14 | 19/34 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 1e-09 | 21/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.7 | 2e-09 | 24/47 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 21/48 (A-172, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +5.8 | 3e-07 | 20/47 (HOP62, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 3e-06 | 20/48 (HOP62, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 2e-05 | 20/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.0 | 2e-05 | 13/48 (A-172, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +4.9 | 3e-05 | 13/48 (HT-29, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.9 | 4e-05 | 17/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +4.8 | 6e-05 | 19/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.7 | 7e-05 | 17/48 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 8e-05 | 18/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.5 | 2e-04 | 15/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 2e-04 | 14/47 (A-172, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9638.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0881×); [[Silodosin (drug)]] 0.05 µM in 1 line (SW48 0.0691×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -6.9 | 4e-09 | 12/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.7 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +23.4) | — |
| [[HOP62 (line)]] | alt | 27.9 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +29.3) | — |
| [[SW480 (line)]] | alt | 37.0 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +17.0) | — |
| [[A498 (line)]] | wt | 27.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +20.2) | — |
| [[HepG2_C3A (line)]] | wt | 315 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -15.4) |
| [[HT-29 (line)]] | alt | 38.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +24.3) | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +18.0) | [[Harringtonine (drug)]] 0.05 µM 0.149× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 23.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +21.3) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +20.9) | — |
| [[J82 (line)]] | alt | 98.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +19.9) | — |
| [[LS 180 (line)]] | wt | 15.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 52.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 15.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +21.6) | — |
| [[RKO (line)]] | wt | 77.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +17.2) | — |
| [[LoVo (line)]] | wt | 12.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 83.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.77× (z +19.3) | — |
| [[BT-474 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +11.2) | — |
| [[C32 (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.1× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 70.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0881× (z -10.8) |
| [[COLO 205 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.0) | — |
| [[KATO III (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.135× (z -9.5) |
| [[SW1417 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.5) | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0691× (z -10.7) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMO]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.60 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[RAB32]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SAMD4A]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CALD1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MYPN]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GPR176]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ARID5B]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FKRP]] | +0.56 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DSEL]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13D]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ATG16L1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SAP130]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RNF168]] | -0.54 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[RNF4]] | -0.54 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.51 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[LPCAT4]] | -0.51 | -0.65 / -0.32 | both halves | 1e-04 |  |
| [[SHQ1]] | -0.50 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[KATNB1]] | -0.49 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[NFATC3]] | -0.49 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[GDAP2]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 18.1); signed map (44.8, 19.9). **Vector** length 95.6, 20.5% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +35.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +20.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +16.4 |
|  | [[Trametinib (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.4 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +10.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.9 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +3.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | filamin A interacting protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1 — chr3:99,828,811-100,114,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DOC-1, GIP130 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4L180](https://www.uniprot.org/uniprotkb/Q4L180) (Filamin A-interacting protein 1-like):

> Acts as a regulator of the antiangiogenic activity on endothelial cells. When overexpressed in endothelial cells, leads to inhibition of cell proliferation and migration and an increase in apoptosis. Inhibits melanoma growth When expressed in tumor-associated vasculature.

**Summary**, from NCBI Gene [11259](https://www.ncbi.nlm.nih.gov/gene/11259):

> Predicted to be involved in protein localization to actin cytoskeleton. Predicted to act upstream of or within several processes, including hindgut development; proteasomal protein catabolic process; and protein secretion. Predicted to be located in cytoplasm; membrane; and nucleus. Predicted to be active in actin cytoskeleton and centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24589) · Entrez [11259](https://www.ncbi.nlm.nih.gov/gene/11259) · UniProt [Q4L180](https://www.uniprot.org/uniprotkb/Q4L180) · Ensembl [ENSG00000168386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168386)

## Data

Gene col 9638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9638); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9638]; `tensor/DDL_lfc|DDL_z.npy` [9638]; `embed/gene_vectors.npy` [9638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9638 or target_col == 9638). Every well: [[FILIP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FILIP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
