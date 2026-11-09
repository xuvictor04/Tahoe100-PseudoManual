---
symbol: "ACIN1"
type: "gene"
col: 2026
ensembl_id: "ENSG00000100813"
name: "apoptotic chromatin condensation inducer 1"
location: "14q11.2"
module: 51
arm: "+"
pooled_cpm: 156.45
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ACIN1

*apoptotic chromatin condensation inducer 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +23.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.742× (z -10.9, q 6e-25, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP7]] (+0.74, fdr 7e-06), [[ATRX]] (+0.72, fdr 7e-06), [[USP16]] (+0.71, fdr 7e-06); moves opposite to [[PRELID1]] (-0.64, fdr 1e-05), [[PIGF]] (-0.62, fdr 1e-05), [[RASA2]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +23.7 | 0e+00 | 46/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +16.3 | 0e+00 | 48/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +15.1 | 0e+00 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +12.2 | 3e-32 | 44/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +12.0 | 4e-31 | 43/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +10.4 | 3e-23 | 41/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +9.7 | 2e-20 | 45/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +9.4 | 5e-19 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.5 | 3e-12 | 39/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +7.5 | 5e-12 | 31/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +7.3 | 1e-11 | 36/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 4e-11 | 37/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +6.9 | 3e-10 | 27/48 (NCI-H23, SW480, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +6.4 | 9e-09 | 25/47 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +6.1 | 5e-08 | 37/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.2 | 7e-04 | 21/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -10.9 | 6e-25 | 37/49 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.683×** | -9.9 | 1e-20 | 43/48 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.713×** | -8.8 | 4e-16 | 41/48 (NCI-H23, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.729×** | -8.2 | 4e-14 | 42/48 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.744×** | -7.7 | 2e-12 | 37/48 (NCI-H2030, NCI-H23, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.755×** | -7.0 | 3e-10 | 36/48 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.777×** | -6.5 | 5e-09 | 35/48 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.801×** | -5.5 | 2e-06 | 30/50 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -5.1 | 2e-05 | 11/48 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.723×** | -4.4 | 6e-04 | 33/49 (NCI-H23, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.016 | 23/47 (CHP-212, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.788×** | -3.2 | 0.059 | 22/45 (SK-MEL-2, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.1 | 0.073 | 16/49 (SK-MEL-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +23.1) | — |
| [[SW480 (line)]] | alt | 180 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 237 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +19.3) | — |
| [[PANC-1 (line)]] | alt | 131 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +19.1) | — |
| [[LoVo (line)]] | wt | 153 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 190 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 220 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.534× (z -10.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A549 (line)]] | wt | 141 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +26.6) | — |
| [[LOX-IMVI (line)]] | wt | 138 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 229 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.5) | [[Panobinostat (drug)]] 5 µM 0.582× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[LS 180 (line)]] | wt | 165 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -9.1) |
| [[SHP-77 (line)]] | alt | 191 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.4) | — |
| [[A-172 (line)]] | wt | 95.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.3) | — |
| [[A498 (line)]] | wt | 138 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +22.8) | — |
| [[AsPC-1 (line)]] | alt | 147 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.562× (z -8.5) ⚠ cell-cycle shift, explains ~24% of this change |
| [[COLO 205 (line)]] | alt | 186 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 143 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 150 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.2) | — |
| [[RKO (line)]] | wt | 173 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 156 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.3) | — |
| [[A-427 (line)]] | wt | 141 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.4) | — |
| [[C32 (line)]] | wt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 222 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -12.4) |
| [[J82 (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 161 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 183 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +17.8) | — |
| [[Panc 03.27 (line)]] | alt | 176 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.6) | [[Lonafarnib (drug)]] 5 µM 0.111× (z -18.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.2) | — |
| [[SNU-423 (line)]] | alt | 137 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.8) |
| [[H4 (line)]] | wt | 161 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.0) |
| [[HOP62 (line)]] | alt | 143 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 106 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.2) |
| [[KATO III (line)]] | alt | 137 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 172 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 219 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 242 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.3) |
| [[SW1417 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ATRX]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[USP16]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HNRNPH2]] | +0.66 | +0.57 / +0.62 | both halves | 9e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PAF1]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 942 |
| [[DNAJC7]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SREK1]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RBM23]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TSR2]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID1]] | -0.64 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PIGF]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[RASA2]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[WDFY2]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[STK32C]] | -0.55 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[UBTD1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MAP2K1]] | -0.54 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[COG5]] | -0.54 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[CHCHD2]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MPZL1]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ACIN1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.3, 9.6); signed map (11.8, -27.8). **Vector** length 108, 35.3% of its response variance represented; |z| ≥ 3 in 1,389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +23.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.3 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.8 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | apoptotic chromatin condensation inducer 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,058,564-23,095,614 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0670, fSAP152; previously ACINUS |
| Gene groups (HGNC) | ASAP complex subunits |
| Reactome | 8 pathways, smallest: Apoptotic cleavage of cellular proteins; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKV3](https://www.uniprot.org/uniprotkb/Q9UKV3) (Apoptotic chromatin condensation inducer in the nucleus):

> Auxiliary component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junction on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. Component of the ASAP complexes which bind RNA in a sequence-independent manner and are proposed to be recruited to the EJC prior to or during …

**Summary**, from NCBI Gene [22985](https://www.ncbi.nlm.nih.gov/gene/22985):

> Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposited at splice junctions on mRNAs, as a consequence of pre-mRNA splicing. It may thus be involved in …

**Accessions** — [HGNC:17066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17066) · Entrez [22985](https://www.ncbi.nlm.nih.gov/gene/22985) · UniProt [Q9UKV3](https://www.uniprot.org/uniprotkb/Q9UKV3) · Ensembl [ENSG00000100813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100813)

## Data

Gene col 2026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2026); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2026]; `tensor/DDL_lfc|DDL_z.npy` [2026]; `embed/gene_vectors.npy` [2026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2026 or target_col == 2026). Every well: [[ACIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
