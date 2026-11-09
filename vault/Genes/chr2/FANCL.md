---
symbol: "FANCL"
type: "gene"
col: 3669
ensembl_id: "ENSG00000115392"
name: "FA complementation group L"
location: "2p16.1"
module: 6
arm: "+"
pooled_cpm: 90.03
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCL

*FA complementation group L* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +7.6, q 2e-11, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -23.0, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX11]] (+0.70, fdr 7e-06), [[POLE2]] (+0.67, fdr 7e-06), [[CENPM]] (+0.67, fdr 7e-06); moves opposite to [[PDPK1]] (-0.59, fdr 1e-05), [[CEP104]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.6 | 2e-11 | 35/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +6.6 | 1e-08 | 30/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +6.1 | 2e-07 | 33/49 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.009 | 23/48 (LS 180, SHP-77, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.009 | 19/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.014 | 22/48 (SNU-423, SW48, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.7 | 0.019 | 0/50 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.089 | 10/48 (NCI-H1792, CHP-212, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.2 | 0.089 | 17/48 (J82, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.15 | 7/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -23.0 | 0e+00 | 42/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -16.3 | 0e+00 | 43/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -11.9 | 3e-30 | 38/49 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -9.1 | 1e-17 | 42/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -8.0 | 1e-13 | 34/48 (SW48, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -7.8 | 5e-13 | 33/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -7.3 | 2e-11 | 39/48 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.694×** | -7.0 | 2e-10 | 30/48 (COLO 205, SW48, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.5 | 5e-09 | 27/44 (SHP-77, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -6.5 | 6e-09 | 31/48 (SW48, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -5.7 | 6e-07 | 28/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.758×** | -5.5 | 2e-06 | 27/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -5.4 | 3e-06 | 26/49 (A-427, RKO, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.767×** | -5.3 | 6e-06 | 29/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.768×** | -5.2 | 7e-06 | 29/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -4.6 | 1e-04 | 25/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -4.4 | 3e-04 | 24/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.802×** | -4.2 | 8e-04 | 27/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.801×** | -4.1 | 9e-04 | 24/48 (KATO III, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.811×** | -4.1 | 9e-04 | 23/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.001 | 21/48 (NCI-H23, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 151 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.8) |
| [[SW480 (line)]] | alt | 179 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 94.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.3) |
| [[SW48 (line)]] | wt | 89.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.0) |
| [[COLO 205 (line)]] | alt | 94.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.5) |
| [[KATO III (line)]] | alt | 126 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.9) |
| [[LS 180 (line)]] | wt | 127 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.210× (z -14.1) |
| [[A-427 (line)]] | wt | 194 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -18.2) |
| [[A498 (line)]] | wt | 81.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.9) |
| [[A549 (line)]] | wt | 114 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -15.1) |
| [[PANC-1 (line)]] | alt | 84.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 61.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -20.2) |
| [[RKO (line)]] | wt | 91.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.1) |
| [[SHP-77 (line)]] | alt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.0) |
| [[SNU-1 (line)]] | wt | 94.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0518× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 72.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.6) |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.6) |
| [[LoVo (line)]] | wt | 69.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.3) |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -20.7) |
| [[AN3 CA (line)]] | alt | 76.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.186× (z -8.9) |
| [[BT-474 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.339× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.0) |
| [[J82 (line)]] | alt | 57.4 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.73× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.5) |
| [[A-172 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 94.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX11]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[POLE2]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CENPM]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[EXO1]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MCM3]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CDC7]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DTL]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 | STRING 678 |
| [[RBL1]] | +0.65 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MIR924HG]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDPK1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CEP104]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.3, -44.5); signed map (-36.7, -43.5). **Vector** length 124, 40.3% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *E2F G1/S* (control, mean cos +0.50 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.53 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -23.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -16.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.6 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:58,159,243-58,241,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10335, FAAP43, Pog; previously PHF9 |
| Gene groups (HGNC) | PHD finger proteins; FA complementation groups; FA core complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW38](https://www.uniprot.org/uniprotkb/Q9NW38) (E3 ubiquitin-protein ligase FANCL):

> Ubiquitin ligase protein that mediates monoubiquitination of FANCD2 in the presence of UBE2T, a key step in the DNA damage pathway. Also mediates monoubiquitination of FANCI. May stimulate the ubiquitin release from UBE2W. May be required for proper primordial germ cell proliferation in the embryonic stage, whereas it is probably not needed for spermatogonial proliferation after birth.

**Summary**, from NCBI Gene [55120](https://www.ncbi.nlm.nih.gov/gene/55120):

> This gene encodes a ubiquitin ligase that is a member of the Fanconi anemia complementation group (FANC). Members of this group are related by their assembly into a common nuclear protein complex rather than by sequence similarity. This gene encodes the protein for complementation group L that mediates monoubiquitination of FANCD2 as well as FANCI. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking …

**Accessions** — [HGNC:20748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20748) · Entrez [55120](https://www.ncbi.nlm.nih.gov/gene/55120) · UniProt [Q9NW38](https://www.uniprot.org/uniprotkb/Q9NW38) · Ensembl [ENSG00000115392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115392)

## Data

Gene col 3669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3669); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3669]; `tensor/DDL_lfc|DDL_z.npy` [3669]; `embed/gene_vectors.npy` [3669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3669 or target_col == 3669). Every well: [[FANCL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
