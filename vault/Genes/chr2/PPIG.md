---
symbol: "PPIG"
type: "gene"
col: 6169
ensembl_id: "ENSG00000138398"
name: "peptidylprolyl isomerase G"
location: "2q31.1"
module: 12
arm: "+"
pooled_cpm: 216.69
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PPIG

*peptidylprolyl isomerase G* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +14.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.20× (z +11.5, q 6e-28, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.722× (z -4.8, q 0.001, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.80, fdr 7e-06), [[ZC3H13]] (+0.80, fdr 7e-06), [[SEC62]] (+0.78, fdr 7e-06); moves opposite to [[NUTF2]] (-0.72, fdr 7e-06), [[MDH2]] (-0.69, fdr 7e-06), [[FKBP1A]] (-0.67, fdr 8e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.06×** | +14.9 | 0e+00 | 48/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +11.5 | 6e-28 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.06×** | +10.1 | 7e-22 | 48/48 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.54×** | +6.3 | 4e-08 | 44/48 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +6.0 | 2e-07 | 39/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.0 | 2e-07 | 42/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +6.0 | 2e-07 | 44/49 (COLO 205, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.49×** | +5.8 | 5e-07 | 42/48 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.37×** | +4.4 | 6e-04 | 35/47 (LoVo, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.024 | 31/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.032 | 30/48 (LoVo, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.25×** | +3.3 | 0.050 | 29/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 5/49 (LoVo, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.722×** | -4.8 | 0.001 | 43/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.3 | 0.005 | 31/48 (HS-578T, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.078 | 29/48 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -3.4 | 0.094 | 34/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.094 | 27/48 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.802× | -3.2 | 0.12 | 28/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.812× | -3.0 | 0.19 | 26/49 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 194 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +13.7) | — |
| [[LoVo (line)]] | wt | 187 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 259 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +10.6) | — |
| [[SW480 (line)]] | alt | 241 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.58× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.6) | — |
| [[C32 (line)]] | wt | 179 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +12.0) | — |
| [[H4 (line)]] | wt | 186 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 199 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 209 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +21.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +16.1) | — |
| [[A-172 (line)]] | wt | 214 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +11.7) | — |
| [[A498 (line)]] | wt | 338 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 201 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +17.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 277 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 163 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.24× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 231 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +13.6) | — |
| [[KATO III (line)]] | alt | 187 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 201 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +16.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 217 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 217 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 163 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 263 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 201 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 256 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HS-578T (line)]] | alt | 162 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 139 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 340 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 209 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 164 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 257 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[CHP-212 (line)]] | wt | 208 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HepG2_C3A (line)]] | wt | 247 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.29× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 152 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HT-29 (line)]] | alt | 201 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 218 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.3) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Panc 03.27 (line)]] | alt | 219 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[RKO (line)]] | wt | 236 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 227 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 201 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 241 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.80 | +0.81 / +0.76 | both halves | 7e-06 | STRING 542 |
| [[SEC62]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[SNW1]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 890 |
| [[SRSF11]] ⚠ | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 611; ⚠ in the vector space only through flagged drug-doses |
| [[SCAF11]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[FRG1]] | +0.75 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[RSF1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 542 |
| [[C1orf131]] | +0.73 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.73 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTF2]] | -0.72 | -0.74 / -0.63 | both halves | 7e-06 |  |
| [[MDH2]] | -0.69 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.67 | -0.66 / -0.58 | both halves | 8e-06 | pathway: SARS-CoV-1 Infection |
| [[SLC25A39]] | -0.66 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[NAGA]] | -0.66 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[COLGALT1]] | -0.66 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[USB1]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[BSG]] | -0.63 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[AKT1]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 | STRING 471 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PPIG's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PPIG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.7, 2.0); signed map (2.0, -15.7). **Vector** length 118, 49.2% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +8.7 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +11.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +6.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +0.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.1 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +2.1 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,584,342-169,641,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CARS-Cyp, SRCyp, SCAF10 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 9 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; SARS-CoV-1-host interactions; SARS-CoV-1 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13427](https://www.uniprot.org/uniprotkb/Q13427) (Peptidyl-prolyl cis-trans isomerase G):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. May be implicated in the folding, transport, and assembly of proteins. May play an important role in the regulation of pre-mRNA splicing.

**Summary**, from NCBI Gene [9360](https://www.ncbi.nlm.nih.gov/gene/9360):

> Enables peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein folding. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14650) · Entrez [9360](https://www.ncbi.nlm.nih.gov/gene/9360) · UniProt [Q13427](https://www.uniprot.org/uniprotkb/Q13427) · Ensembl [ENSG00000138398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138398)

## Data

Gene col 6169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6169); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6169]; `tensor/DDL_lfc|DDL_z.npy` [6169]; `embed/gene_vectors.npy` [6169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6169 or target_col == 6169). Every well: [[PPIG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
