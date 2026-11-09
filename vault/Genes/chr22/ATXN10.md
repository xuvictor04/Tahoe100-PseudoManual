---
symbol: "ATXN10"
type: "gene"
col: 5090
ensembl_id: "ENSG00000130638"
name: "ataxin 10"
location: "22q13.31"
module: 1
arm: "+"
pooled_cpm: 138.42
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ATXN10

*ataxin 10* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.60× (z +9.7, q 1e-19, up in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (SHP-77 2.38×, SW480 2.30×, MIA PaCa-2 3.21×, HOP62 2.31×, …); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 2.41×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-172 2.23×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.290× (z -25.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVEN]] (+0.74, fdr 7e-06), [[DPH5-DT]] (+0.68, fdr 1e-05), [[NUTM2B-AS1]] (+0.67, fdr 1e-05); moves opposite to [[FBXO33]] (-0.65, fdr 1e-05), [[ARL3]] (-0.65, fdr 1e-05), [[ORC4]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[POGLUT2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5090.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (SHP-77 2.38×, SW480 2.30×, MIA PaCa-2 3.21×, HOP62 2.31×, …); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 2.41×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-172 2.23×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +9.7 | 1e-19 | 39/48 (SHP-77, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.17× | +4.7 | 9e-04 | 17/48 (NCI-H1573, HT-29, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.8 | 0.024 | 23/48 (A-172, COLO 205, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.7 | 0.024 | 23/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.024 | 23/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.7 | 0.024 | 5/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.290×** | -25.8 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.305×** | -24.7 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.353×** | -21.7 | 0e+00 | 48/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -13.8 | 2e-41 | 47/49 (NCI-H1573, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.560×** | -12.1 | 1e-31 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -11.4 | 2e-28 | 40/49 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -9.5 | 1e-19 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -9.0 | 2e-17 | 36/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.476×** | -8.1 | 4e-14 | 47/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -7.4 | 6e-12 | 35/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.715×** | -7.0 | 1e-10 | 40/48 (SW48, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.816×** | -6.0 | 1e-07 | 25/48 (C32, NCI-H1792, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.822×** | -3.9 | 0.004 | 24/48 (A549, AsPC-1, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.824×** | -3.9 | 0.004 | 25/47 (SW48, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.7 | 0.009 | 20/49 (Panc 03.27, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 158 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -11.7) |
| [[RKO (line)]] | wt | 117 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -23.9) |
| [[A-172 (line)]] | wt | 97.5 | 4 (3 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.41× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.21× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.356× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 180 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -21.3) |
| [[AsPC-1 (line)]] | alt | 73.4 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.53× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -13.7) |
| [[HOP62 (line)]] | alt | 168 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.4) |
| [[KATO III (line)]] | alt | 143 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -25.5) |
| [[LoVo (line)]] | wt | 122 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -26.6) |
| [[NCI-H1792 (line)]] | alt | 227 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -19.6) |
| [[NCI-H23 (line)]] | alt | 146 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 119 | 1 | 6 | [[Auranofin (drug)]] 5 µM 1.83× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -23.0) |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -18.9) |
| [[SNU-423 (line)]] | alt | 144 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.09× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -20.8) |
| [[SW480 (line)]] | alt | 134 | 1 | 6 | [[Auranofin (drug)]] 5 µM 2.30× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.208× (z -26.4) |
| [[A549 (line)]] | wt | 166 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -21.5) |
| [[H4 (line)]] | wt | 219 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -14.1) |
| [[SW48 (line)]] | wt | 152 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -15.6) |
| [[HS-578T (line)]] | alt | 186 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 89.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -21.1) |
| [[LS 180 (line)]] | wt | 116 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 1 | 4 | [[Auranofin (drug)]] 5 µM 3.21× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.147× (z -21.5) |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 244 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -15.8) |
| [[A498 (line)]] | wt | 260 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -18.4) |
| [[HCT15 (line)]] | alt | 181 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -16.6) |
| [[hTERT-HPNE (line)]] | wt | 178 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -11.6) |
| [[PANC-1 (line)]] | alt | 112 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -13.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -9.2) |
| [[SW 900 (line)]] | alt | 149 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -14.6) |
| [[SW1417 (line)]] | alt | 84.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -17.4) |
| [[A-427 (line)]] | wt | 103 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -12.0) |
| [[BT-474 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -11.6) |
| [[COLO 205 (line)]] | alt | 82.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -12.7) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -19.6) |
| [[HT-29 (line)]] | alt | 51.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -13.5) |
| [[J82 (line)]] | alt | 99.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -11.1) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.6) |
| [[AN3 CA (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[CHP-212 (line)]] | wt | 258 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 89.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.40× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.3) |
| [[SHP-77 (line)]] | alt | 244 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.38× (z +14.5) | [[TAK-901 (drug)]] 5 µM 0.352× (z -9.1) |
| [[C-33 A (line)]] | alt | 186 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.213× (z -8.6) |
| [[SW 1088 (line)]] | alt | 112 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.110× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | +0.74 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.68 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | +0.67 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.66 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[ZBTB40]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ITPA]] | +0.64 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GATC]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[UTP20]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 | same gene group |
| [[ATE1]] | +0.62 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ANAPC7]] | +0.62 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[GPATCH2]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[JPX]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO33]] | -0.65 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ARL3]] | -0.65 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ORC4]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.63 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[ANG]] | -0.62 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[MED26]] | -0.61 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ING1]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[NRTN]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.60 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[AHDC1]] | -0.59 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RNASE4]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT2]] | C | POGLUT2 activity raises ATXN10's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without POGLUT2 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.3, -7.8); signed map (21.8, -28.1). **Vector** length 124, 39.5% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.1 | +9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.3 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.5 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.7 | -13.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.7 | -12.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -21.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,671,798-45,845,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E46L, FLJ37990, ATX10; previously SCA10 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBB4](https://www.uniprot.org/uniprotkb/Q9UBB4) (Ataxin-10):

> May play a role in the regulation of cytokinesis. May play a role in signaling by stimulating protein glycosylation. Induces neuritogenesis by activating the Ras-MAP kinase pathway and is necessary for the survival of cerebellar neurons (By similarity). Does not appear to play a major role in ciliogenesis (By similarity).

**Summary**, from NCBI Gene [25814](https://www.ncbi.nlm.nih.gov/gene/25814):

> This gene encodes a protein that may function in neuron survival, neuron differentiation, and neuritogenesis. These roles may be carried out via activation of the mitogen-activated protein kinase cascade. Expansion of an ATTCT repeat from 9-32 copies to 800-4500 copies in an intronic region of this locus has been associated with spinocerebellar ataxia, type 10. Alternatively spliced transcript variants have been described.[provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:10549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10549) · Entrez [25814](https://www.ncbi.nlm.nih.gov/gene/25814) · UniProt [Q9UBB4](https://www.uniprot.org/uniprotkb/Q9UBB4) · Ensembl [ENSG00000130638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130638)

## Data

Gene col 5090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5090); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5090]; `tensor/DDL_lfc|DDL_z.npy` [5090]; `embed/gene_vectors.npy` [5090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5090 or target_col == 5090). Every well: [[ATXN10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
