---
symbol: "STXBP5"
type: "gene"
col: 8956
ensembl_id: "ENSG00000164506"
name: "syntaxin binding protein 5"
location: "6q24.3"
module: 98
arm: "+"
pooled_cpm: 139.26
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# STXBP5

*syntaxin binding protein 5* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.59× (z +5.7, q 5e-06, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.375× (z -12.1, q 8e-31, down in 40 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.433× (z -10.3, q 2e-22, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HECTD1]] (+0.67, fdr 7e-06), [[HIPK2]] (+0.66, fdr 7e-06), [[PCNX1]] (+0.62, fdr 1e-05); moves opposite to [[TNFRSF11A]] (-0.57, fdr 1e-05), [[RAB3A]] (-0.55, fdr 2e-05), [[C7orf57]] (-0.55, fdr 5e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HECW2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +5.7 | 5e-06 | 36/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 4e-05 | 32/47 (HS-578T, A-172, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.056 | 25/46 (HS-578T, A-172, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.056 | 25/46 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.081 | 24/47 (HS-578T, A-172, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.084 | 28/47 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.375×** | -12.1 | 8e-31 | 40/47 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.431×** | -10.3 | 1e-22 | 45/47 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.433×** | -10.3 | 2e-22 | 47/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.436×** | -10.2 | 2e-22 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.487×** | -8.8 | 1e-16 | 43/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.616×** | -8.4 | 4e-15 | 37/47 (NCI-H23, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.565×** | -7.0 | 2e-10 | 34/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.562×** | -6.8 | 7e-10 | 34/47 (NCI-H2030, A549, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.568×** | -6.7 | 2e-09 | 30/43 (Panc 03.27, C-33 A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.363×** | -6.5 | 4e-09 | 42/48 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.604×** | -5.7 | 5e-07 | 30/44 (A-427, HT-29, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.666×** | -5.0 | 3e-05 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.679×** | -4.6 | 2e-04 | 28/46 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **0.656×** | -4.4 | 4e-04 | 32/48 (NCI-H23, SNU-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.697×** | -4.4 | 4e-04 | 32/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -3.7 | 0.008 | 28/47 (hTERT-HPNE, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.784×** | -3.0 | 0.075 | 25/47 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.845× | -2.9 | 0.087 | 15/48 (HT-29, A-172, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.758×** | -2.9 | 0.087 | 21/47 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -2.9 | 0.092 | 18/47 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.785×** | -2.9 | 0.094 | 21/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 122 | 14 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 3.81× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.321× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 252 | 15 | 0 | [[Triamcinolone (drug)]] 5 µM 3.29× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 259 | 6 | 8 (8 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 3.42× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.225× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 143 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 6.67× (z +12.7) | — |
| [[A-172 (line)]] | wt | 152 | 9 | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 3.78× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 184 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -16.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.351× (z -10.1) |
| [[KATO III (line)]] | alt | 114 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -16.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.327× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 174 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.298× (z -10.6) |
| [[SHP-77 (line)]] | alt | 507 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.240× (z -13.5) |
| [[SW480 (line)]] | alt | 145 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -18.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.2) |
| [[PANC-1 (line)]] | alt | 217 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -19.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.394× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 223 | 2 (1 ⚠) | 6 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +13.7) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.05 µM 2.31× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 97.3 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -15.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 95.3 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -19.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 134 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 149 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[LOX-IMVI (line)]] | wt | 177 | 1 | 5 (3 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.51× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.0) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -10.5) |
| [[SNU-1 (line)]] | wt | 120 | 0 | 6 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0578× (z -11.9) |
| [[HT-29 (line)]] | alt | 219 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -10.7) |
| [[BT-474 (line)]] | alt | 68.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[J82 (line)]] | alt | 140 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -11.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 130 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.382× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 163 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW 900 (line)]] | alt | 110 | 1 | 3 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.86× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.3) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -8.6) |
| [[AN3 CA (line)]] | alt | 242 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.244× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 53.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 291 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -10.1) |
| [[Hs 766T (line)]] | wt | 86.9 | 2 | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 3.17× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -13.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW1417 (line)]] | alt | 79.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 47.8 | 2 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.30× (z +9.1) | — |
| [[RKO (line)]] | wt | 87.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW 1271 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0797× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.8) ⚠ cell-cycle shift, explains ~73% of this change |
| [[RPMI-7951 (line)]] | alt | 98.9 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.14× (z +8.8) | — |
| [[A498 (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD1]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[HIPK2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PCNX1]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PID1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MGST1]] | +0.59 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[NUTM2B-AS1]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[STXBP5-AS1]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TMTC1]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ARMC8]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF11A]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 | STRING 769 |
| [[C7orf57]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[TBC1D10A]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[IGFBP3]] | -0.54 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[SLC9A7]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[UBA6]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LRP1]] | -0.52 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[GPR160]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[LRIG1]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CDK18]] | -0.51 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[DBP]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HECW2]] | B | HECW2 activity raises STXBP5's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without HECW2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[DNER]] | B | DNER activity raises STXBP5's level | lines that do not express DNER (32) vs lines expressing it (18) | 1.41× lower at baseline in the lines without DNER | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC |
| [[C7orf57]] | B | C7orf57 activity lowers STXBP5's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 1.36× higher at baseline in the lines without C7orf57 | 0.059 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN |
| [[MTHFD1L]] | C | MTHFD1L activity raises STXBP5's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.88× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 16.3); signed map (19.1, 32.7). **Vector** length 116, 45.4% of its response variance represented; |z| ≥ 3 in 1,555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.6 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +6.2 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.1 | +5.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +5.6 | +3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.3 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -10.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.1 | -10.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -8.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | -3.9 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:147,204,180-147,391,010 (+) |
| Ensembl biotype | protein_coding |
| Also known as | tomosyn, LLGL3, tomosyn-1 |
| Gene groups (HGNC) | WD repeat domain containing; Syntaxin binding protein 5 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T5C0](https://www.uniprot.org/uniprotkb/Q5T5C0) (Syntaxin-binding protein 5):

> Plays a regulatory role in calcium-dependent exocytosis and neurotransmitter release. Inhibits membrane fusion between transport vesicles and the plasma membrane. May modulate the assembly of trans-SNARE complexes between transport vesicles and the plasma membrane. Inhibits translocation of GLUT4 from intracellular vesicles to the plasma membrane. Competes with STXBP1 for STX1 binding (By similarity).

**Summary**, from NCBI Gene [134957](https://www.ncbi.nlm.nih.gov/gene/134957):

> Syntaxin 1 is a component of the 7S and 20S SNARE complexes which are involved in docking and fusion of synaptic vesicles with the presynaptic plasma membrane. This gene encodes a syntaxin 1 binding protein. In rat, a similar protein dissociates syntaxin 1 from the Munc18/n-Sec1/rbSec1 complex to form a 10S complex, an intermediate which can be converted to the 7S SNARE complex. Thus this protein is thought to be involved in neurotransmitter release by stimulating SNARE complex formation. …

**Accessions** — [HGNC:19665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19665) · Entrez [134957](https://www.ncbi.nlm.nih.gov/gene/134957) · UniProt [Q5T5C0](https://www.uniprot.org/uniprotkb/Q5T5C0) · Ensembl [ENSG00000164506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164506)

## Data

Gene col 8956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8956); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8956]; `tensor/DDL_lfc|DDL_z.npy` [8956]; `embed/gene_vectors.npy` [8956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8956 or target_col == 8956). Every well: [[STXBP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
