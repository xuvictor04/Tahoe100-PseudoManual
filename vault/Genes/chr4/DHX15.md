---
symbol: "DHX15"
type: "gene"
col: 3064
ensembl_id: "ENSG00000109606"
name: "DEAH-box helicase 15"
location: "4p15.2"
module: 20
arm: "+"
pooled_cpm: 197.33
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DHX15

*DEAH-box helicase 15* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.82× (z +12.0, q 1e-30, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.541× (z -11.3, q 4e-27, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX9]] (+0.77, fdr 7e-06), [[HNRNPA3]] (+0.72, fdr 7e-06), [[RPSA]] (+0.69, fdr 7e-06); moves opposite to [[SELENOK]] (-0.68, fdr 1e-05), [[NKAP]] (-0.65, fdr 7e-06), [[INAFM1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.82×** | +12.0 | 1e-30 | 48/49 (NCI-H1573, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +11.8 | 7e-30 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.15×** | +11.2 | 8e-27 | 47/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +10.1 | 8e-22 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.11×** | +9.8 | 2e-20 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +7.1 | 1e-10 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.1 | 8e-08 | 43/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +5.9 | 3e-07 | 34/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.6 | 3e-04 | 38/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 4e-04 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.44×** | +4.0 | 0.003 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.19× | +3.2 | 0.067 | 21/48 (SK-MEL-2, H4, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.067 | 25/48 (Hs 766T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.079 | 28/48 (PANC-1, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -11.3 | 4e-27 | 45/49 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -8.1 | 2e-13 | 46/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.563×** | -7.5 | 1e-11 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.607×** | -6.5 | 1e-08 | 43/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.0 | 0.006 | 32/47 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.025 | 32/48 (A498, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -3.5 | 0.031 | 32/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.031 | 32/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.050 | 27/48 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.704×** | -3.3 | 0.061 | 31/48 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.783× | -3.1 | 0.11 | 27/47 (HOP62, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.794× | -3.0 | 0.12 | 26/48 (NCI-H23, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 226 | 7 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -15.7) |
| [[SW480 (line)]] | alt | 198 | 7 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 201 | 7 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 6.46× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 152 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.9) |
| [[PANC-1 (line)]] | alt | 156 | 6 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.8) |
| [[KATO III (line)]] | alt | 188 | 5 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 220 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 199 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -10.0) |
| [[LS 180 (line)]] | wt | 267 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.9) |
| [[COLO 205 (line)]] | alt | 217 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 10.2× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.8) |
| [[Hs 766T (line)]] | wt | 99.7 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.7) | — |
| [[H4 (line)]] | wt | 241 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.1) |
| [[HT-29 (line)]] | alt | 186 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 8.55× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.1) |
| [[J82 (line)]] | alt | 229 | 2 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 180 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.26× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 140 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.6) |
| [[A-172 (line)]] | wt | 122 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 5.88× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.6) |
| [[BT-474 (line)]] | alt | 220 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 230 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 6.73× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 131 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.2) | — |
| [[RKO (line)]] | wt | 290 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 7.26× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 167 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +11.8) | [[Docetaxel (drug)]] 0.05 µM 0.344× (z -10.3) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 194 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 300 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +9.6) | — |
| [[SW48 (line)]] | wt | 261 | 2 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.08× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -8.6) |
| [[A-427 (line)]] | wt | 174 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.78× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 160 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 236 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.42× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 160 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.39× (z +11.3) | — |
| [[A549 (line)]] | wt | 170 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.7) |
| [[C-33 A (line)]] | alt | 260 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -8.5) |
| [[C32 (line)]] | wt | 188 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 9.05× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -8.6) |
| [[HS-578T (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.94× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 193 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.82× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 223 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +8.6) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 242 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.32× (z +9.0) | — |
| [[A498 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 199 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 715 |
| [[HNRNPA3]] | +0.72 | +0.70 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RPSA]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[MEST]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MAT2A]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RANBP1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SRSF1]] | +0.66 | +0.41 / +0.78 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 763 |
| [[FAM98B]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.65 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[NUP210]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MTHFD1]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.68 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[NKAP]] | -0.65 | -0.63 / -0.73 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 515 |
| [[INAFM1]] | -0.64 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.64 | -0.64 / -0.72 | both halves | 7e-06 |  |
| [[RNF181]] | -0.63 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[ING2]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.61 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.61 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[AK6]] | -0.59 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | -0.59 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[ZNF791]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.1, -28.5); signed map (-20.6, -43.5). **Vector** length 88.3, 38.0% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.1 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.0 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.6 | -1.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +6.1 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | +11.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:24,517,441-24,584,554 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRH2, DBP1, Prp43, PrPp43p, PRPF43; previously DDX15 |
| Gene groups (HGNC) | DEAH-box helicases; SSU processome; Spliceosomal A complex; Spliceosomal B complex; U11/U12 di-snRNP |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43143](https://www.uniprot.org/uniprotkb/O43143) (ATP-dependent RNA helicase DHX15):

> RNA helicase involved in mRNA processing and antiviral innate immunity. Pre-mRNA processing factor involved in disassembly of spliceosomes after the release of mature mRNA. In cooperation with TFIP11 seem to be involved in the transition of the U2, U5 and U6 snRNP-containing IL complex to the snRNP-free IS complex leading to efficient debranching and turnover of excised introns. Plays a key role in antiviral innate immunity by promoting both MAVS-dependent signaling and NLRP6 inflammasome. Acts …

**Summary**, from NCBI Gene [1665](https://www.ncbi.nlm.nih.gov/gene/1665):

> The protein encoded by this gene is a putative ATP-dependent RNA helicase implicated in pre-mRNA splicing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2738) · Entrez [1665](https://www.ncbi.nlm.nih.gov/gene/1665) · UniProt [O43143](https://www.uniprot.org/uniprotkb/O43143) · Ensembl [ENSG00000109606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109606)

## Data

Gene col 3064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3064); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3064]; `tensor/DDL_lfc|DDL_z.npy` [3064]; `embed/gene_vectors.npy` [3064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3064 or target_col == 3064). Every well: [[DHX15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
