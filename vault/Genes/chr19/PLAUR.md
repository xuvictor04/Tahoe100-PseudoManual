---
symbol: "PLAUR"
type: "gene"
col: 239
ensembl_id: "ENSG00000011422"
name: "plasminogen activator, urokinase receptor"
location: "19q13"
module: 34
arm: "+"
pooled_cpm: 192.1
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 81
n_dd_up_clean: 0
n_dd_down_clean: 59
in_vector_space: true
direction_upstream: 30
direction_downstream: 31
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLAUR

*plasminogen activator, urokinase receptor* — 19q13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 2.22×).
> Pooled over the cell lines (median), lowered significantly by 81 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.363× (z -18.1, q 0e+00, down in 36 of 38 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.287× (z -15.8, q 0e+00, down in 36 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA7A]] (+0.72, fdr 7e-06), [[PPARD]] (+0.72, fdr 7e-06), [[CDCP1]] (+0.71, fdr 7e-06); moves opposite to [[MGST1]] (-0.58, fdr 3e-05), [[RDX]] (-0.56, fdr 2e-05), [[TNS3]] (-0.55, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 31 go from it, the strongest it → [[S100A16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 2.22×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[vincristine (drug)]] 0.5 µM |  | 1.55× | +3.6 | 0.15 | 23/38 (HT-29, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 2.01× | +3.5 | 0.15 | 22/38 (HEC-1-A, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.24 | 18/37 (LOX-IMVI, hTERT-HPNE, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 83 in all, 23 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 81 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.363×** | -18.1 | 0e+00 | 36/38 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.287×** | -15.8 | 0e+00 | 36/38 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.331×** | -14.0 | 3e-42 | 37/38 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -13.7 | 2e-40 | 36/39 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.356×** | -13.1 | 6e-37 | 37/38 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.404×** | -11.0 | 3e-26 | 35/38 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.429×** | -10.7 | 1e-24 | 36/38 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.437×** | -10.1 | 6e-22 | 33/38 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.473×** | -9.5 | 2e-19 | 35/38 (H4, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -7.1 | 6e-11 | 33/40 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.558×** | -7.1 | 9e-11 | 27/37 (SW48, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -6.9 | 2e-10 | 26/38 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.556×** | -6.8 | 4e-10 | 33/38 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.680×** | -6.7 | 7e-10 | 31/38 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.634×** | -6.7 | 8e-10 | 27/38 (SK-MEL-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.593×** | -6.6 | 2e-09 | 30/38 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.535×** | -6.5 | 4e-09 | 28/40 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 304 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -22.9) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -11.6) |
| [[SW48 (line)]] | wt | 582 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -21.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -19.7) |
| [[RKO (line)]] | wt | 189 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -33.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -15.7) |
| [[HT-29 (line)]] | alt | 487 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0972× (z -21.9) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.9) ⚠ position correction uncertain · without an alert: [[Binimetinib (drug)]] 5 µM 0.183× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 522 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -20.7) |
| [[HOP62 (line)]] | alt | 490 | 0 | 11 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.590× (z -15.7) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.256× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 1 | 9 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.5) | [[Adagrasib (drug)]] 0.05 µM 0.413× (z -22.9) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 305 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -25.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.186× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -17.7) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.182× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 188 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -23.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.135× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 366 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -19.0) |
| [[hTERT-HPNE (line)]] | wt | 259 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -14.3) |
| [[LoVo (line)]] | wt | 214 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -16.0) |
| [[LS 180 (line)]] | wt | 246 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -16.5) |
| [[A-172 (line)]] | wt | 324 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -12.4) |
| [[A549 (line)]] | wt | 193 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.4) |
| [[HS-578T (line)]] | alt | 285 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.4) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.316× (z -11.0) |
| [[SW1417 (line)]] | alt | 243 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -17.2) |
| [[COLO 205 (line)]] | alt | 185 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -14.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.0) |
| [[HCT15 (line)]] | alt | 403 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.3) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 79.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.4) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.7) |
| [[J82 (line)]] | alt | 140 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.8) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -8.5) |
| [[SW 900 (line)]] | alt | 198 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.1) ⚠ position correction uncertain · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 426 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.641× (z -11.6) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -9.7) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -11.2) |
| [[A498 (line)]] | wt | 129 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.0) |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.2) ⚠ position correction uncertain |
| [[KATO III (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.3) ⚠ position correction uncertain |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.8) ⚠ position correction uncertain |
| [[RPMI-7951 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.2) ⚠ position correction uncertain |
| [[SW 1088 (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.4) ⚠ position correction uncertain |
| [[A-427 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 45.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 35.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 527 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 38.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA7A]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |
| [[PPARD]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 | same gene group |
| [[BCL2A1]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ARID3B]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[STC1]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[EHD1]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[TMEM158]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[TMCC3]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DUSP5]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RDX]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[TNS3]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | -0.54 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[ZMYND11]] | -0.54 | -0.52 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 26, C 4. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises PLAUR's level | lines that do not express F3 (24) vs lines expressing it (26) | 3.17× lower at baseline in the lines without F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[S100A16]] | B | S100A16 activity raises PLAUR's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 4.39× lower at baseline in the lines without S100A16 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[LAMB3]] | B | LAMB3 activity raises PLAUR's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 3.21× lower at baseline in the lines without LAMB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[SMOX]] | B | SMOX activity raises PLAUR's level | lines that do not express SMOX (6) vs lines expressing it (44) | 4.89× lower at baseline in the lines without SMOX | 0.005 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises PLAUR's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without KCNK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[ADAM8]] | B | ADAM8 activity raises PLAUR's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without ADAM8 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises PLAUR's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without EVA1A-AS | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SERPINB1]] | B | SERPINB1 activity raises PLAUR's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 3.16× lower at baseline in the lines without SERPINB1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[FAM107B]] | B | FAM107B activity raises PLAUR's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without FAM107B | 0.027 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[MGST1]] | B | MGST1 activity raises PLAUR's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without MGST1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[PAQR5]] | B | PAQR5 activity raises PLAUR's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without PAQR5 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[TNS3]] | B | TNS3 activity raises PLAUR's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.81× lower at baseline in the lines without TNS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 29, C 2. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | PLAUR activity raises S100A16's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 3.21× lower at baseline in the lines without PLAUR | 0.009 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[TM4SF19]] | B | PLAUR activity raises TM4SF19's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 4.11× lower at baseline in the lines without PLAUR | 0.009 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[SHB]] | B | PLAUR activity raises SHB's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without PLAUR | 0.012 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[CLIP2]] | B | PLAUR activity raises CLIP2's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without PLAUR | 0.014 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[MEAK7]] | B | PLAUR activity raises MEAK7's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without PLAUR | 0.016 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[LAMB3]] | B | PLAUR activity raises LAMB3's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 6.00× lower at baseline in the lines without PLAUR | 0.019 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[RAC2]] | B | PLAUR activity raises RAC2's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 4.36× lower at baseline in the lines without PLAUR | 0.019 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[STX1A]] | B | PLAUR activity raises STX1A's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without PLAUR | 0.024 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[F3]] | B | PLAUR activity raises F3's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 4.47× lower at baseline in the lines without PLAUR | 0.033 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[MGST1]] | B | PLAUR activity raises MGST1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without PLAUR | 0.042 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[SERPINB1]] | B | PLAUR activity raises SERPINB1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without PLAUR | 0.043 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[LUCAT1]] | B | PLAUR activity raises LUCAT1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without PLAUR | 0.050 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 1.2); signed map (0.3, 46.2). **Vector** length 129, 50.4% of its response variance represented; |z| ≥ 3 in 1,707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.8 | -13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | -14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | -15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.6 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.5 | -6.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.8 | -6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.8 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | plasminogen activator, urokinase receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13 — chr19:43,646,095-43,670,547 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URKR, UPAR, CD87 |
| Gene groups (HGNC) | CD molecules; LY6/PLAUR domain containing |
| Hallmark sets | APICAL_SURFACE, CHOLESTEROL_HOMEOSTASIS, INFLAMMATORY_RESPONSE, COMPLEMENT, KRAS_SIGNALING_UP, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 8 pathways, smallest: Regulation of FXIIa and plasma kallikrein activity; Attachment of GPI anchor to uPAR; Dissolution of Fibrin Clot |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03405](https://www.uniprot.org/uniprotkb/Q03405) (Urokinase plasminogen activator surface receptor):

> GPI-anchored receptor that recruits and activates the urokinase-type plasminogen activator (uPA) at the cell surface. Activated uPA converts plasminogen into plasmin, initiating extracellular matrix degradation and remodeling. Also binds the extracellular matrix protein vitronectin, promoting cell-matrix adhesion and indirectly integrin signaling. This dual interaction coordinates dynamic changes in cell migration, proliferation, and tissue remodeling.

**Summary**, from NCBI Gene [5329](https://www.ncbi.nlm.nih.gov/gene/5329):

> This gene encodes the receptor for urokinase plasminogen activator and, given its role in localizing and promoting plasmin formation, likely influences many normal and pathological processes related to cell-surface plasminogen activation and localized degradation of the extracellular matrix. It binds both the proprotein and mature forms of urokinase plasminogen activator and permits the activation of the receptor-bound pro-enzyme by plasmin. The protein lacks transmembrane or cytoplasmic …

**Accessions** — [HGNC:9053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9053) · Entrez [5329](https://www.ncbi.nlm.nih.gov/gene/5329) · UniProt [Q03405](https://www.uniprot.org/uniprotkb/Q03405) · Ensembl [ENSG00000011422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011422)

## Data

Gene col 239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 239); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 239]; `tensor/DDL_lfc|DDL_z.npy` [239]; `embed/gene_vectors.npy` [239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 239 or target_col == 239). Every well: [[PLAUR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAUR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
