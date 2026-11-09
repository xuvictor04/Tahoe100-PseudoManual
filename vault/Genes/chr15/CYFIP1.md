---
symbol: "CYFIP1"
type: "gene"
col: 15797
ensembl_id: "ENSG00000273749"
name: "cytoplasmic FMR1 interacting protein 1"
location: "15q11.2"
module: 101
arm: "+"
pooled_cpm: 136.06
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# CYFIP1

*cytoplasmic FMR1 interacting protein 1* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +18.2, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.735× (z -8.9, q 2e-16, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA4]] (+0.65, fdr 1e-05), [[MYO1C]] (+0.64, fdr 7e-06), [[EGFR]] (+0.63, fdr 7e-06); moves opposite to [[ASB7]] (-0.59, fdr 5e-05), [[NDUFAF7]] (-0.57, fdr 5e-05), [[MRPL34]] (-0.56, fdr 5e-05).
> It is in [[Module 101]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +18.2 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.7 | 4e-09 | 35/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.5 | 2e-08 | 40/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 0.002 | 25/47 (HOP62, LS 180, …) | two highest doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.008 | 24/48 (BT-474, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.017 | 23/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.026 | 22/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.032 | 26/48 (BT-474, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.10 | 20/44 (SK-MEL-2, LoVo, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +3.0 | 0.15 | 21/47 (H4, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.735×** | -8.9 | 2e-16 | 42/48 (RKO, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -8.5 | 5e-15 | 37/48 (HOP62, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.685×** | -7.7 | 2e-12 | 34/48 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -7.0 | 4e-10 | 33/48 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -6.8 | 2e-09 | 34/48 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.805×** | -6.3 | 3e-08 | 26/49 (A549, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -6.0 | 1e-07 | 35/47 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.795×** | -4.7 | 2e-04 | 31/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -4.3 | 0.001 | 28/48 (BT-474, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.819×** | -4.1 | 0.002 | 25/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.878× | -3.7 | 0.013 | 13/49 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.844× | -3.5 | 0.023 | 22/48 (A498, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.848× | -3.4 | 0.030 | 20/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.856× | -3.2 | 0.057 | 20/49 (Hs 766T, H4, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.858× | -3.2 | 0.061 | 18/48 (BT-474, CFPAC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.078 | 18/47 (SHP-77, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 188 | 8 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.9) ⚠ cell-cycle shift, explains ~16% of this change |
| [[RKO (line)]] | wt | 208 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.428× (z -15.8) |
| [[BT-474 (line)]] | alt | 348 | 5 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 92.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +31.0) | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.4) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HOP62 (line)]] | alt | 171 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.400× (z -12.5) |
| [[LoVo (line)]] | wt | 162 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.2) | [[Auranofin (drug)]] 5 µM 0.518× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.4) | [[Auranofin (drug)]] 5 µM 0.528× (z -8.6) |
| [[A549 (line)]] | wt | 229 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.3) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H1573 (line)]] | alt | 293 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 165 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +29.4) | — |
| [[SW48 (line)]] | wt | 168 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +17.1) | [[Auranofin (drug)]] 5 µM 0.438× (z -8.5) |
| [[A-172 (line)]] | wt | 130 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.500× (z -9.5) |
| [[COLO 205 (line)]] | alt | 91.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 173 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.546× (z -8.8) |
| [[HS-578T (line)]] | alt | 83.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.461× (z -8.7) |
| [[J82 (line)]] | alt | 92.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.518× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 192 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +17.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.9) | — |
| [[A498 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.1) | — |
| [[H4 (line)]] | wt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 89.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 149 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.2) | — |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.414× (z -8.7) |
| [[KATO III (line)]] | alt | 119 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.515× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.617× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 171 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 90.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.9) | — |
| [[SW 1088 (line)]] | alt | 86.4 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0907× (z -9.0) |
| [[SW 900 (line)]] | alt | 73.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.1) | — |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 165 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[MYO1C]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[EGFR]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ABR]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[BMAL2]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[THOC6]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ARHGDIA]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 | pathway: RAC1 GTPase cycle; STRING 443 |
| [[CAPN2]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[STK10]] | +0.57 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[WDR1]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[NOP14-AS1]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ETS1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | -0.59 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[NDUFAF7]] | -0.57 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[MRPL34]] | -0.56 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[ZNF738]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RNF145]] | -0.56 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CNOT8]] | -0.55 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[TRIT1]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SPCS2]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[VPS37D]] | -0.55 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[ALG9]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[KIAA2013]] | -0.53 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[EID2B]] | -0.53 | -0.36 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, 8.7); signed map (-3.4, 34.5). **Vector** length 120, 37.5% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.1 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.4 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.7 | -8.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic FMR1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:22,867,052-22,981,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0068, P140SRA-1, SHYC |
| Gene groups (HGNC) | SCAR/WAVE complex |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 21 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L576](https://www.uniprot.org/uniprotkb/Q7L576) (Cytoplasmic FMR1-interacting protein 1):

> Component of the CYFIP1-EIF4E-FMR1 complex which binds to the mRNA cap and mediates translational repression. In the CYFIP1-EIF4E-FMR1 complex this subunit is an adapter between EIF4E and FMR1. Promotes the translation repression activity of FMR1 in brain probably by mediating its association with EIF4E and mRNA (By similarity). Regulates formation of membrane ruffles and lamellipodia. Plays a role in axon outgrowth. Binds to F-actin but not to RNA. Part of the WAVE complex that regulates actin …

**Summary**, from NCBI Gene [23191](https://www.ncbi.nlm.nih.gov/gene/23191):

> This gene encodes a protein that regulates cytoskeletal dynamics and protein translation. The encoded protein is a component of the WAVE regulatory complex (WRC), which promotes actin polymerization. This protein also interacts with the synaptic functional regulator FMR1 protein and translation initiation factor 4E to inhibit protein translation. A large chromosomal deletion including this gene is associated with increased risk of schizophrenia and epilepsy in human patients. Reduced expression …

**Accessions** — [HGNC:13759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13759) · Entrez [23191](https://www.ncbi.nlm.nih.gov/gene/23191) · UniProt [Q7L576](https://www.uniprot.org/uniprotkb/Q7L576) · Ensembl [ENSG00000273749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273749)

## Data

Gene col 15797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15797); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15797]; `tensor/DDL_lfc|DDL_z.npy` [15797]; `embed/gene_vectors.npy` [15797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15797 or target_col == 15797). Every well: [[CYFIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYFIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
