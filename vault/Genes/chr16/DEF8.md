---
symbol: "DEF8"
type: "gene"
col: 6477
ensembl_id: "ENSG00000140995"
name: "differentially expressed in FDCP 8 homolog"
location: "16q24.3"
module: 138
arm: "+"
pooled_cpm: 16.12
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# DEF8

*differentially expressed in FDCP 8 homolog* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +16.4, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.06× (z +11.4, q 6e-28, up in 37 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ toxic; cell-cycle shift, explains ~71% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.171×); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.181×; ⚠ transcription drop; cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOMER3]] (+0.64, fdr 7e-06), [[TBKBP1]] (+0.58, fdr 1e-05), [[RIPOR1]] (+0.58, fdr 3e-05); moves opposite to [[LDHB]] (-0.40, fdr 2e-04), [[DDX11-AS1]] (-0.40, fdr 2e-04).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.09×** | +16.4 | 0e+00 | 41/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.14×** | +12.0 | 7e-31 | 30/39 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +11.4 | 6e-28 | 37/47 (SW480, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +10.5 | 2e-23 | 22/29 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.58×** | +7.2 | 5e-11 | 28/45 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +6.8 | 9e-10 | 25/33 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.2 | 4e-08 | 21/47 (LOX-IMVI, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.45×** | +5.9 | 3e-07 | 22/43 (HS-578T, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +5.3 | 9e-06 | 21/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.39×** | +5.2 | 9e-06 | 20/48 (SW480, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.40×** | +5.1 | 2e-05 | 20/47 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 4e-04 | 13/45 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +4.2 | 0.001 | 14/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +3.9 | 0.003 | 15/47 (SW480, KATO III, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.9 | 0.004 | 9/26 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 13/45 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.008 | 15/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.011 | 9/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.016 | 14/47 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.017 | 12/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.018 | 10/47 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.024 | 13/44 (SW480, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.034 | 10/45 (LS 180, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ toxic; cell-cycle shift, explains ~71% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.171×); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.181×; ⚠ transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.802× | -3.5 | 0.23 | 8/48 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.0 | 0.70 | 1/48 (A-172) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.4 | 6 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.44× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 16.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.171× (z -9.7) |
| [[A-172 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 7.51 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.181× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +15.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 43.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 8.66 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~71% of this change |
| [[SNU-423 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 15.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMER3]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TBKBP1]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[RIPOR1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[DUSP3]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SGTA]] | +0.53 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[APBB1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ATG4D]] | +0.51 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CLCN7]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FAM50A]] | +0.51 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[UAP1L1]] | +0.50 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[RHOT2]] | +0.50 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[TEPSIN]] | +0.50 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.40 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[DDX11-AS1]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.4, -27.0); signed map (5.2, -8.5). **Vector** length 55.1, 8.32% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.4 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +0.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.3 |
|  | [[Thymol (drug)]] 5 µM |  | -0.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | differentially expressed in FDCP 8 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,948,697-89,968,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20186 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN54](https://www.uniprot.org/uniprotkb/Q6ZN54) (Differentially expressed in FDCP 8 homolog):

> Positively regulates lysosome peripheral distribution and ruffled border formation in osteoclasts. Involved in bone resorption.

**Summary**, from NCBI Gene [54849](https://www.ncbi.nlm.nih.gov/gene/54849):

> Predicted to enable zinc ion binding activity. Predicted to be involved in lysosome localization; positive regulation of bone resorption; and positive regulation of ruffle assembly. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25969) · Entrez [54849](https://www.ncbi.nlm.nih.gov/gene/54849) · UniProt [Q6ZN54](https://www.uniprot.org/uniprotkb/Q6ZN54) · Ensembl [ENSG00000140995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140995)

## Data

Gene col 6477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6477); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6477]; `tensor/DDL_lfc|DDL_z.npy` [6477]; `embed/gene_vectors.npy` [6477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6477 or target_col == 6477). Every well: [[DEF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
