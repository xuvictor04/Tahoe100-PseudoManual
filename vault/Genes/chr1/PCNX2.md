---
symbol: "PCNX2"
type: "gene"
col: 5751
ensembl_id: "ENSG00000135749"
name: "pecanex 2"
location: "1q42.2"
module: 207
arm: "-"
pooled_cpm: 83.43
n_lines_expressing: 42
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# PCNX2

*pecanex 2* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.22× (z +15.3, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.604× (z -9.6, q 3e-19, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BICD1]] (+0.62, fdr 7e-06), [[MPDZ]] (+0.61, fdr 1e-05), [[TMEM185B]] (+0.60, fdr 1e-05); moves opposite to [[PMS2P4-1]] (-0.64, fdr 1e-05), [[GLE1]] (-0.63, fdr 3e-05), [[APTR]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STK32B]] → it (grade B ⚠); 5 go from it, the strongest it → [[JAZF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +15.3 | 0e+00 | 40/40 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +12.0 | 2e-30 | 38/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +11.0 | 9e-26 | 39/41 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.66×** | +10.8 | 8e-25 | 39/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +10.2 | 2e-22 | 37/40 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +10.1 | 6e-22 | 36/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +9.5 | 2e-19 | 31/40 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.78×** | +7.2 | 3e-11 | 36/41 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 3e-09 | 34/40 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 20/40 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.001 | 26/40 (NCI-H1573, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 21/40 (A-172, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.029 | 18/40 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 22/40 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.036 | 19/41 (NCI-H460, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -9.6 | 3e-19 | 31/41 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -8.4 | 2e-14 | 29/40 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -7.4 | 2e-11 | 31/40 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -7.3 | 4e-11 | 29/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -6.6 | 6e-09 | 30/40 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.626×** | -5.2 | 2e-05 | 26/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -4.2 | 0.003 | 22/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.8 | 0.010 | 20/41 (A549, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.010 | 26/40 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -3.7 | 0.014 | 21/40 (LS 180, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.4 | 6 | 11 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.10× (z +13.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -14.8) |
| [[LoVo (line)]] | wt | 56.6 | 7 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.57× (z +19.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 101 | 1 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.3) |
| [[HT-29 (line)]] | alt | 72.3 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 100 | 8 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.31× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -11.3) |
| [[COLO 205 (line)]] | alt | 79.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 76.3 | 4 | 3 | [[Tucidinostat (drug)]] 5 µM 2.46× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.1) |
| [[A-172 (line)]] | wt | 95.6 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 2.96× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 41.8 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 4.48× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 56.6 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.14× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 167 | 3 | 3 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +14.1) | [[Digitoxin (drug)]] 0.05 µM 0.323× (z -9.1) |
| [[A-427 (line)]] | wt | 83.1 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.381× (z -10.2) |
| [[J82 (line)]] | alt | 31.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 3.73× (z +12.2) | — |
| [[RKO (line)]] | wt | 125 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 125 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.4) |
| [[SNU-423 (line)]] | alt | 38.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.18× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 67.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.5) | — |
| [[KATO III (line)]] | alt | 28.5 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 82.2 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.1) |
| [[SW480 (line)]] | alt | 139 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.17× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -12.6) |
| [[C32 (line)]] | wt | 85.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.77× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.0) |
| [[HS-578T (line)]] | alt | 103 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 111 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.50× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -8.7) |
| [[SW 900 (line)]] | alt | 131 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.49× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 60.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.37× (z +10.8) | [[Digitoxin (drug)]] 0.5 µM 0.389× (z -8.5) |
| [[SW48 (line)]] | wt | 86.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.4) | — |
| [[A498 (line)]] | wt | 98.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.45× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 108 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.96× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 135 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.23× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 75.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.57× (z +10.0) | — |
| [[A549 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICD1]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MPDZ]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GALNT10]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[IQCH]] | +0.60 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[AIG1]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[WDR7]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FGGY]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[LINC00460]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TAF1B]] | +0.56 | +0.40 / +0.59 | both halves | 5e-05 | STRING 540 |
| [[RNF180]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[GLE1]] | -0.63 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[APTR]] | -0.63 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[GUCD1]] | -0.60 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SOS1]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[RAB5B]] | -0.59 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[FBXO34]] | -0.59 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[STX5-DT]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MFSD8]] | -0.57 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[GPBP1L1]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE27]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK32B]] | B | STK32B activity raises PCNX2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without STK32B | 0.042 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[CDC42EP3]] | B | CDC42EP3 activity raises PCNX2's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without CDC42EP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises PCNX2's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without ANAPC1P4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAZF1]] | B | PCNX2 activity raises JAZF1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without PCNX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[IQCH]] | B | PCNX2 activity raises IQCH's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without PCNX2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[SRP54-AS1]] | B | PCNX2 activity lowers SRP54-AS1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.56× higher at baseline in the lines without PCNX2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[NCK1-DT]] | B | PCNX2 activity raises NCK1-DT's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without PCNX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[AIG1]] | B | PCNX2 activity raises AIG1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without PCNX2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-2.3, -31.6); signed map (8.0, -48.9). **Vector** length 117, 39.2% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.0 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.2 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.7 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | pecanex 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:232,983,435-233,295,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0435, FLJ11383; previously PCNXL2 |
| Gene groups (HGNC) | Pecanex family |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NKB5](https://www.uniprot.org/uniprotkb/A6NKB5) (Pecanex-like protein 2):

> May play a role in tumorigenesis of colorectal carcinomas with high microsatellite instability (MSI-H).

**Summary**, from NCBI Gene [80003](https://www.ncbi.nlm.nih.gov/gene/80003):

> This gene contains coding mononucleotide repeats that are associated with tumors of high mcrosatellite instability (MSI-H). Defects in this gene are involved in the tumorigenesis of MSI-H colorectal carcinomas. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:8736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8736) · Entrez [80003](https://www.ncbi.nlm.nih.gov/gene/80003) · UniProt [A6NKB5](https://www.uniprot.org/uniprotkb/A6NKB5) · Ensembl [ENSG00000135749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135749)

## Data

Gene col 5751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5751); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5751]; `tensor/DDL_lfc|DDL_z.npy` [5751]; `embed/gene_vectors.npy` [5751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5751 or target_col == 5751). Every well: [[PCNX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
