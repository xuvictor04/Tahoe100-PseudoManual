---
symbol: "CTPS2"
type: "gene"
col: 510
ensembl_id: "ENSG00000047230"
name: "CTP synthase 2"
location: "Xp22.2"
module: 46
arm: "+"
pooled_cpm: 40.75
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 5
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CTPS2

*CTP synthase 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.32× (z +5.5, q 3e-05, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.266× (z -37.8, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARS2]] (+0.62, fdr 3e-05), [[NCOA2]] (+0.59, fdr 1e-05), [[NNT]] (+0.58, fdr 1e-05); moves opposite to [[SYP]] (-0.61, fdr 3e-05), [[AMN1]] (-0.60, fdr 2e-05), [[AREG]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +5.5 | 3e-05 | 23/46 (NCI-H2347, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.0 | 2e-04 | 20/47 (HOP62, KATO III, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.054 | 11/48 (C-33 A, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.076 | 9/45 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.093 | 11/46 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.093 | 13/46 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.12 | 11/46 (A549, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.266×** | -37.8 | 0e+00 | 45/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.177×** | -34.8 | 0e+00 | 46/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.238×** | -28.9 | 0e+00 | 47/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.245×** | -28.4 | 0e+00 | 46/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.303×** | -24.1 | 0e+00 | 47/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.318×** | -23.1 | 0e+00 | 44/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.353×** | -21.0 | 0e+00 | 46/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.403×** | -17.6 | 0e+00 | 38/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.427×** | -17.1 | 0e+00 | 41/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -17.0 | 0e+00 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.478×** | -14.9 | 0e+00 | 42/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.640×** | -12.7 | 3e-35 | 41/47 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -12.3 | 3e-33 | 40/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.549×** | -12.1 | 4e-32 | 42/46 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -10.7 | 3e-25 | 39/48 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.544×** | -10.4 | 6e-24 | 40/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -10.1 | 3e-22 | 32/47 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.2 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -30.3) |
| [[MIA PaCa-2 (line)]] | alt | 81.5 | 0 | 18 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -20.3) |
| [[SNU-423 (line)]] | alt | 61.2 | 0 | 17 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -26.1) |
| [[SW480 (line)]] | alt | 76.2 | 0 | 16 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -30.4) |
| [[A-172 (line)]] | wt | 61.0 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0365× (z -28.0) |
| [[HOP62 (line)]] | alt | 66.8 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -25.6) |
| [[Hs 766T (line)]] | wt | 61.6 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.0) |
| [[LoVo (line)]] | wt | 43.8 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -24.2) |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.2) |
| [[J82 (line)]] | alt | 42.0 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.0) |
| [[LS 180 (line)]] | wt | 43.5 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -24.2) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -20.7) |
| [[SW1417 (line)]] | alt | 50.2 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -21.1) |
| [[COLO 205 (line)]] | alt | 36.0 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -24.9) |
| [[HEC-1-A (line)]] | alt | 89.7 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -26.5) |
| [[NCI-H1792 (line)]] | alt | 58.8 | 0 | 9 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -20.8) |
| [[KATO III (line)]] | alt | 43.8 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.128× (z -20.1) |
| [[A549 (line)]] | wt | 36.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.0) |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.104× (z -12.8) |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0389× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.3) |
| [[BT-474 (line)]] | alt | 90.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.0) |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.7) |
| [[A498 (line)]] | wt | 18.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.5) |
| [[C32 (line)]] | wt | 18.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 5 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -10.8) |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0509× (z -18.0) |
| [[SW48 (line)]] | wt | 41.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -12.8) |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.164× (z -10.8) |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.0) |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0903× (z -10.1) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -14.5) |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.205× (z -11.1) |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -8.8) |
| [[H4 (line)]] | wt | 17.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0570× (z -12.2) |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARS2]] | +0.62 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NCOA2]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NNT]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MAP2K5]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TLK2]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[USP24]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[IPO11]] | +0.54 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[ARID1B]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[GANC]] | +0.54 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[PARG]] | +0.53 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[DYRK1A]] | +0.53 | +0.51 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYP]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[AMN1]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[AREG]] | -0.57 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ASMTL]] | -0.52 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[IER2]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[WDR26]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 | same gene group |
| [[MIDN]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[CCNYL1]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 | same gene group |
| [[SEPTIN10]] | -0.50 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[MYL12A]] | -0.50 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[FRMD8]] | -0.49 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[EGLN3]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.2, 15.4); signed map (28.0, -23.9). **Vector** length 65.9, 15.8% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +3.3 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.4 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -34.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -14.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | CTP synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:16,587,999-16,712,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GATD5B |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; MicroRNA protein coding host genes; CTP synthase family |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRF8](https://www.uniprot.org/uniprotkb/Q9NRF8) (CTP synthase 2):

> Cytidine triphosphate synthase involved in the de novo synthesis of CTP, a precursor of DNA, RNA and phospholipids. Catalyzes the ATP-dependent amination of UTP to CTP with either L-glutamine or ammonia as a source of nitrogen. Constitutes the rate-limiting enzyme in the synthesis of cytosine nucleotides.

**Summary**, from NCBI Gene [56474](https://www.ncbi.nlm.nih.gov/gene/56474):

> The protein encoded by this gene catalyzes the formation of CTP from UTP with the concomitant deamination of glutamine to glutamate. This protein is the rate-limiting enzyme in the synthesis of cytosine nucleotides, which play an important role in various metabolic processes and provide the precursors necessary for the synthesis of RNA and DNA. Cancer cells that exhibit increased cell proliferation also exhibit an increased activity of this encoded protein. Thus, this protein is an attractive …

**Accessions** — [HGNC:2520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2520) · Entrez [56474](https://www.ncbi.nlm.nih.gov/gene/56474) · UniProt [Q9NRF8](https://www.uniprot.org/uniprotkb/Q9NRF8) · Ensembl [ENSG00000047230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047230)

## Data

Gene col 510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 510); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 510]; `tensor/DDL_lfc|DDL_z.npy` [510]; `embed/gene_vectors.npy` [510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 510 or target_col == 510). Every well: [[CTPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
