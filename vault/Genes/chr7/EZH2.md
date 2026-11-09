---
symbol: "EZH2"
type: "gene"
col: 2763
ensembl_id: "ENSG00000106462"
name: "enhancer of zeste 2 polycomb repressive complex 2 subunit"
location: "7q36.1"
module: 6
arm: "+"
pooled_cpm: 118.81
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# EZH2

*enhancer of zeste 2 polycomb repressive complex 2 subunit* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +20.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.725× (z -4.9, q 7e-04, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Belzutifan (drug)]] 5 µM: 0.600× (z -3.8, q 0.029, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCLAF]] (+0.79, fdr 7e-06), [[HELLS]] (+0.78, fdr 7e-06), [[RAD51AP1]] (+0.77, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +20.9 | 0e+00 | 44/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +15.4 | 0e+00 | 45/49 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.31×** | +12.6 | 5e-34 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +10.7 | 2e-24 | 42/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.98×** | +10.3 | 1e-22 | 45/48 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.93×** | +9.5 | 2e-19 | 39/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.83×** | +9.1 | 8e-18 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.74×** | +8.4 | 5e-15 | 41/48 (C32, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.74×** | +8.3 | 8e-15 | 40/48 (C32, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.67×** | +7.7 | 1e-12 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.69×** | +7.6 | 1e-12 | 40/48 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +7.1 | 6e-11 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 9e-07 | 31/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +5.2 | 8e-06 | 31/48 (RPMI-7951, RKO, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.41×** | +5.0 | 2e-05 | 34/50 (C32, NCI-H23, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.024 | 21/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.029 | 14/48 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.031 | 21/49 (A549, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.063 | 16/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.0 | 0.067 | 14/48 (RPMI-7951, SW 900, …) | top dose only |  |
| [[venetoclax (drug)]] 0.5 µM |  | **1.31×** | +2.8 | 0.094 | 11/49 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.725×** | -4.9 | 7e-04 | 33/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.824×** | -4.2 | 0.009 | 23/48 (A-427, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **0.600×** | -3.8 | 0.029 | 27/47 (COLO 205, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.709×** | -3.6 | 0.039 | 23/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.089 | 22/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.805×** | -3.3 | 0.097 | 24/48 (HCT15, SNU-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.098 | 20/48 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.098 | 22/47 (SW48, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.098 | 16/48 (RKO, C32, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.864× | -3.1 | 0.098 | 17/48 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.866× | -3.1 | 0.098 | 17/49 (NCI-H2122, Panc 03.27, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.098 | 22/48 (PANC-1, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 100 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +21.2) | — |
| [[C32 (line)]] | wt | 152 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +23.6) | — |
| [[PANC-1 (line)]] | alt | 111 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.5) | — |
| [[LoVo (line)]] | wt | 114 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +18.5) | — |
| [[A498 (line)]] | wt | 116 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +21.1) | [[Selinexor (drug)]] 5 µM 0.448× (z -10.5) ⚠ cell-cycle shift, explains ~70% of this change |
| [[J82 (line)]] | alt | 150 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +17.3) | — |
| [[NCI-H23 (line)]] | alt | 120 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 198 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +8.6) | — |
| [[H4 (line)]] | wt | 112 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.328× (z -11.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 105 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.7) | — |
| [[HOP62 (line)]] | alt | 77.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.7) | — |
| [[hTERT-HPNE (line)]] | wt | 43.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +23.7) | — |
| [[RPMI-7951 (line)]] | alt | 70.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +20.2) | — |
| [[SNU-423 (line)]] | alt | 77.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +21.0) | — |
| [[A-172 (line)]] | wt | 58.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.452× (z -9.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[Hs 766T (line)]] | wt | 73.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 88.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 105 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.4) | [[Lonafarnib (drug)]] 5 µM 0.173× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 182 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.398× (z -13.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A549 (line)]] | wt | 79.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 71.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 80.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +23.7) | — |
| [[HT-29 (line)]] | alt | 158 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 97.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +19.3) | — |
| [[NCI-H2347 (line)]] | alt | 125 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.6) | — |
| [[RKO (line)]] | wt | 177 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 255 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.22× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 136 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 58.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 57.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.3) | — |
| [[KATO III (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 76.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.7) | — |
| [[SW48 (line)]] | wt | 191 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 280 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCLAF]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 | STRING 525 |
| [[HELLS]] | +0.78 | +0.78 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 581 |
| [[RAD51AP1]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 404 |
| [[MYBL2]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 568 |
| [[TMPO]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPH]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[MELK]] | +0.75 | +0.68 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 738 |
| [[E2F8]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 438 |
| [[BARD1]] | +0.74 | +0.68 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SPC25]] | +0.74 | +0.67 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RAD54L]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 469 |
| [[NCAPG2]] | +0.73 | +0.70 / +0.79 | both halves | 7e-06 | STRING 451 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises EZH2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without E2F2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TEKT4P2-1]] | B | TEKT4P2-1 activity raises EZH2's level | lines that do not express TEKT4P2-1 (20) vs lines expressing it (30) | 1.13× lower at baseline in the lines without TEKT4P2-1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000291032, ENSG00000291065, IL1RAPL1 |
| [[E2F8]] | B | E2F8 activity raises EZH2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without E2F8 | 0.047 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises EZH2's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without PBK | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises EZH2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[DSCC1]] | C | DSCC1 activity raises EZH2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without DSCC1 | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.3, -45.1); signed map (-39.2, -47.0). **Vector** length 115, 44.4% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.54 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40); *E2F G1/S* (control, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.1 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +4.7 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +15.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.2 | +5.0 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +3.1 | +2.8 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Relugolix (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -8.3 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.5 | -0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.8 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of zeste 2 polycomb repressive complex 2 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:148,807,257-148,884,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EZH1, ENX-1, KMT6, KMT6A |
| Gene groups (HGNC) | Histone lysine methyltransferases; Myb/SANT domain containing; Polycomb repressive complex 2; SET domain containing |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 35 pathways, smallest: Defective pyroptosis; PRC2 methylates histones and DNA; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15910](https://www.uniprot.org/uniprotkb/Q15910) (Histone-lysine N-methyltransferase EZH2):

> Catalytic subunit of the PRC2/EED-EZH2 complex, a Polycomb group (PcG) complex that methylates 'Lys-9' (H3K9me) and 'Lys-27' (H3K27me) of histone H3, leading to transcriptional repression of the affected target gene. Able to mono-, di- and trimethylate 'Lys-27' of histone H3 to form H3K27me1, H3K27me2 and H3K27me3, respectively. Displays a preference for substrates with less methylation, loses activity when progressively more methyl groups are incorporated into H3K27, H3K27me0 > H3K27me1 > …

**Summary**, from NCBI Gene [2146](https://www.ncbi.nlm.nih.gov/gene/2146):

> This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein associates with the embryonic ectoderm development protein, the VAV1 oncoprotein, and the X-linked nuclear protein. This protein may play a role in the hematopoietic and central nervous systems. Multiple alternatively splcied transcript variants encoding …

**Accessions** — [HGNC:3527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3527) · Entrez [2146](https://www.ncbi.nlm.nih.gov/gene/2146) · UniProt [Q15910](https://www.uniprot.org/uniprotkb/Q15910) · Ensembl [ENSG00000106462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106462)

## Data

Gene col 2763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2763); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2763]; `tensor/DDL_lfc|DDL_z.npy` [2763]; `embed/gene_vectors.npy` [2763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2763 or target_col == 2763). Every well: [[EZH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EZH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
