---
symbol: "SH2D4A"
type: "gene"
col: 2474
ensembl_id: "ENSG00000104611"
name: "SH2 domain containing 4A"
location: "8p21.3"
module: 8
arm: "+"
pooled_cpm: 35.57
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SH2D4A

*SH2 domain containing 4A* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.42× (z +6.5, q 6e-08, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.189× (z -30.5, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND2D]] (+0.66, fdr 1e-05), [[HTR1D]] (+0.62, fdr 3e-05), [[ANKRD18B]] (+0.61, fdr 2e-05); moves opposite to [[DNAAF9]] (-0.63, fdr 1e-05), [[RRAS]] (-0.62, fdr 5e-05), [[CD81]] (-0.58, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); 5 go from it, the strongest it → [[PLEKHA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.5 | 6e-08 | 23/37 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 7e-06 | 20/37 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 5e-04 | 17/37 (A549, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.6 | 5e-04 | 13/31 (Panc 03.27, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +3.7 | 0.029 | 15/37 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.036 | 12/37 (BT-474, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.036 | 11/36 (NCI-H1573, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.036 | 10/37 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.063 | 10/36 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.075 | 6/37 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.075 | 7/37 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.075 | 5/37 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.075 | 6/37 (A-427, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.084 | 7/37 (KATO III, AsPC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.091 | 8/36 (A549, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.189×** | -30.5 | 0e+00 | 37/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.191×** | -30.3 | 0e+00 | 36/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.207×** | -28.9 | 0e+00 | 37/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.483×** | -13.3 | 3e-38 | 35/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -11.6 | 3e-29 | 23/37 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.563×** | -10.5 | 7e-24 | 29/36 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -10.3 | 4e-23 | 26/36 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.653×** | -7.8 | 4e-13 | 21/36 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.491×** | -6.8 | 6e-10 | 26/37 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -5.3 | 6e-06 | 21/37 (LoVo, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -4.8 | 8e-05 | 15/37 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.6 | 2e-04 | 20/37 (HEC-1-A, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.3 | 7e-04 | 19/37 (AsPC-1, NCI-H460, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.004 | 16/37 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.834× | -3.3 | 0.035 | 16/37 (BT-474, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.840× | -3.1 | 0.073 | 11/36 (BT-474, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 81.6 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0690× (z -32.2) |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0797× (z -23.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.112× (z -20.9) |
| [[LS 180 (line)]] | wt | 73.6 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0774× (z -25.0) |
| [[A-427 (line)]] | wt | 37.8 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.2) |
| [[HT-29 (line)]] | alt | 41.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0759× (z -20.5) |
| [[SNU-1 (line)]] | wt | 55.7 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0782× (z -17.3) |
| [[SW480 (line)]] | alt | 34.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -22.4) |
| [[HEC-1-A (line)]] | alt | 93.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0904× (z -28.3) |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0884× (z -21.8) |
| [[RKO (line)]] | wt | 27.5 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0740× (z -15.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.190× (z -10.4) |
| [[SW48 (line)]] | wt | 54.2 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0902× (z -16.8) |
| [[A498 (line)]] | wt | 42.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -16.5) |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -12.7) |
| [[Hs 766T (line)]] | wt | 57.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0815× (z -20.7) |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.163× (z -15.3) |
| [[KATO III (line)]] | alt | 83.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0825× (z -24.6) |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -13.6) ⚠ toxic; cell-cycle shift, explains ~4% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.127× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 46.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -21.0) |
| [[A-172 (line)]] | wt | 37.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -13.5) |
| [[A549 (line)]] | wt | 38.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.134× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -9.9) |
| [[J82 (line)]] | alt | 19.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.218× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -15.1) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -11.4) |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -9.2) |
| [[H4 (line)]] | wt | 21.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -10.3) |
| [[HOP62 (line)]] | alt | 9.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -11.3) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -8.9) |
| [[AN3 CA (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2D]] | +0.66 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[HTR1D]] | +0.62 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ANKRD18B]] | +0.61 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[IQCH-AS1]] | +0.59 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[HNF4G]] | +0.59 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SLFN12]] | +0.58 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[PARD3B]] | +0.58 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[JADE2]] | +0.58 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[PLEKHA6]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TNFSF15]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[AMIGO2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.55 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.63 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[RRAS]] | -0.62 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CD81]] | -0.58 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[DNASE1L1]] | -0.57 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[GUK1]] | -0.56 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[PLD3]] | -0.55 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[GNAI2]] | -0.54 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[F11R]] | -0.54 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[OGG1]] | -0.54 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[TNNT1]] | -0.53 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[GDI1]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[EPOR]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity raises SH2D4A's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without PLEKHA6 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SLC22A3]] | B | SLC22A3 activity raises SH2D4A's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without SLC22A3 | 0.018 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[SERTAD4]] | B | SERTAD4 activity raises SH2D4A's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without SERTAD4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[ESRP2]] | B | ESRP2 activity raises SH2D4A's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without ESRP2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[SPON1]] | B | SPON1 activity raises SH2D4A's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.26× lower at baseline in the lines without SPON1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[ACSL5]] | B | ACSL5 activity raises SH2D4A's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without ACSL5 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[ANKRD18B]] | B | ANKRD18B activity lowers SH2D4A's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 2.06× higher at baseline in the lines without ANKRD18B | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[ZNF177]] | B | ZNF177 activity lowers SH2D4A's level | lines that do not express ZNF177 (8) vs lines expressing it (42) | 2.91× higher at baseline in the lines without ZNF177 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF559-ZNF177, ZNF559, HYDIN |
| [[GPR39]] | C | GPR39 activity raises SH2D4A's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.83× lower at baseline in the lines without GPR39 | 0.004 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3; co-absent with the target |
| [[SEPTIN9-DT]] | C | SEPTIN9-DT activity raises SH2D4A's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 3.23× lower at baseline in the lines without SEPTIN9-DT | 0.097 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | SH2D4A activity raises PLEKHA6's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.54× lower at baseline in the lines without SH2D4A | 0.025 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA |
| [[ESRP2]] | B | SH2D4A activity raises ESRP2's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.15× lower at baseline in the lines without SH2D4A | 0.066 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA |
| [[F11R]] | B | SH2D4A activity raises F11R's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without SH2D4A | 0.070 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA |
| [[SEPTIN9-DT]] | C | SH2D4A activity raises SEPTIN9-DT's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without SH2D4A | 0.020 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA; co-absent with the target |
| [[GPR39]] | C | SH2D4A activity raises GPR39's level | lines that do not express SH2D4A (11) vs lines expressing it (39) | 3.94× lower at baseline in the lines without SH2D4A | 0.026 | ⚠ within organs, on part of the lines; also absent: IL22RA1, ABCC3, CDA; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.377). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 46.5); signed map (52.4, 5.9). **Vector** length 107, 28.0% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +6.8 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | +4.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -30.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -28.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -30.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -13.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | +0.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SH2 domain containing 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:19,313,693-19,396,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20967, SH2A, PPP1R38 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; SH2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H788](https://www.uniprot.org/uniprotkb/Q9H788) (SH2 domain-containing protein 4A):

> Inhibits estrogen-induced cell proliferation by competing with PLCG for binding to ESR1, blocking the effect of estrogen on PLCG and repressing estrogen-induced proliferation. May play a role in T-cell development and function.

**Summary**, from NCBI Gene [63898](https://www.ncbi.nlm.nih.gov/gene/63898):

> Enables phosphatase binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26102) · Entrez [63898](https://www.ncbi.nlm.nih.gov/gene/63898) · UniProt [Q9H788](https://www.uniprot.org/uniprotkb/Q9H788) · Ensembl [ENSG00000104611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104611)

## Data

Gene col 2474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2474); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2474]; `tensor/DDL_lfc|DDL_z.npy` [2474]; `embed/gene_vectors.npy` [2474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2474 or target_col == 2474). Every well: [[SH2D4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2D4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
