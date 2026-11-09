---
symbol: "KCMF1"
type: "gene"
col: 10715
ensembl_id: "ENSG00000176407"
name: "potassium channel modulatory factor 1"
location: "2p11.2"
module: 60
arm: "+"
pooled_cpm: 222.38
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# KCMF1

*potassium channel modulatory factor 1* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.24× (z +13.6, q 4e-39, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.285× (z -22.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSR]] (+0.57, fdr 1e-05), [[TALDO1]] (+0.56, fdr 7e-06), [[PTGES3]] (+0.55, fdr 1e-05); moves opposite to [[AHI1]] (-0.47, fdr 5e-05), [[NEU1]] (-0.46, fdr 5e-05), [[HLA-A]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.24×** | +13.6 | 4e-39 | 48/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +11.9 | 3e-30 | 47/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.96×** | +10.2 | 4e-22 | 43/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +10.1 | 5e-22 | 48/48 (NCI-H460, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +8.1 | 5e-14 | 44/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.7 | 1e-09 | 39/48 (A-427, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 7e-05 | 32/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.8 | 0.009 | 28/45 (KATO III, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.014 | 26/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.014 | 30/49 (COLO 205, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.6 | 0.016 | 25/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.3 | 0.052 | 20/38 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.052 | 13/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.1 | 0.068 | 22/49 (LS 180, NCI-H1792, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -22.5 | 0e+00 | 48/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.305×** | -21.3 | 0e+00 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -13.5 | 5e-39 | 44/48 (AsPC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.546×** | -10.4 | 2e-23 | 39/44 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.606×** | -9.0 | 2e-17 | 39/49 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -8.7 | 3e-16 | 41/49 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.661×** | -6.9 | 5e-10 | 31/45 (C32, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.674×** | -6.8 | 7e-10 | 40/47 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -6.0 | 1e-07 | 41/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.724×** | -5.6 | 1e-06 | 35/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.739×** | -5.2 | 9e-06 | 36/50 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -5.1 | 1e-05 | 25/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.799×** | -4.0 | 0.003 | 30/48 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.806×** | -3.9 | 0.004 | 29/48 (A549, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.822×** | -3.5 | 0.016 | 24/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.022 | 22/48 (NCI-H23, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 215 | 1 | 11 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 251 | 2 | 9 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 4.43× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.180× (z -21.5) |
| [[PANC-1 (line)]] | alt | 239 | 7 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 10.8× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.256× (z -20.4) |
| [[HT-29 (line)]] | alt | 241 | 3 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.41× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.195× (z -20.3) |
| [[KATO III (line)]] | alt | 179 | 4 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.255× (z -16.9) |
| [[NCI-H2347 (line)]] | alt | 188 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 200 | 5 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.232× (z -21.1) |
| [[SW480 (line)]] | alt | 204 | 5 | 3 | [[TAK-901 (drug)]] 5 µM 6.57× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.193× (z -25.7) |
| [[A-427 (line)]] | wt | 333 | 2 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.09× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.222× (z -21.5) |
| [[AsPC-1 (line)]] | alt | 422 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.0838× (z -30.7) |
| [[LoVo (line)]] | wt | 229 | 4 | 3 | [[TAK-901 (drug)]] 5 µM 8.50× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.194× (z -23.0) |
| [[NCI-H2030 (line)]] | alt | 324 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.287× (z -15.0) |
| [[A498 (line)]] | wt | 208 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.339× (z -13.2) |
| [[A549 (line)]] | wt | 305 | 2 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 7.16× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -24.0) |
| [[H4 (line)]] | wt | 201 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.264× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 170 | 4 | 2 | [[TAK-901 (drug)]] 5 µM 4.99× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.408× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 328 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.180× (z -25.8) |
| [[RKO (line)]] | wt | 145 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.00× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -15.2) |
| [[SW1417 (line)]] | alt | 248 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.62× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -19.3) |
| [[C32 (line)]] | wt | 136 | 2 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.400× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 233 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -13.9) |
| [[Hs 766T (line)]] | wt | 199 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -16.0) |
| [[LS 180 (line)]] | wt | 201 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 6.61× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 289 | 3 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.313× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 194 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 4.93× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.237× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -15.9) |
| [[C-33 A (line)]] | alt | 214 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -10.8) |
| [[COLO 205 (line)]] | alt | 112 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.18× (z +14.7) | — |
| [[HepG2_C3A (line)]] | wt | 312 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -17.8) |
| [[HOP62 (line)]] | alt | 208 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.29× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.189× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 310 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.05× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.241× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 489 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.62× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.244× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 116 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.04× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 143 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 3.87× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -15.5) |
| [[SW 900 (line)]] | alt | 177 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.78× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.267× (z -14.5) |
| [[HS-578T (line)]] | alt | 162 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 7.40× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -13.1) |
| [[J82 (line)]] | alt | 111 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -14.3) |
| [[SNU-1 (line)]] | wt | 137 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +10.1) | — |
| [[SW48 (line)]] | wt | 254 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -18.5) |
| [[BT-474 (line)]] | alt | 131 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -10.6) |
| [[AN3 CA (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 167 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -9.2) |
| [[SW 1088 (line)]] | alt | 172 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.144× (z -9.4) |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSR]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TALDO1]] | +0.56 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PTGES3]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[TMEM161A]] | +0.52 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[CACYBP]] | +0.52 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ABCC5]] | +0.52 | +0.48 / +0.27 | both halves | 3e-04 |  |
| [[NXPE3]] | +0.51 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[CHORDC1]] | +0.51 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[OTULIN]] | +0.51 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[MRPL18]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PLAA]] | +0.50 | +0.64 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1]] | -0.47 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[NEU1]] | -0.46 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[HLA-A]] | -0.45 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CCP110]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[REL]] | -0.43 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[NFKB2]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PER2]] | -0.43 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[WASHC4]] | -0.42 | -0.49 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KCMF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.8, -12.7); signed map (-27.2, -27.5). **Vector** length 90.2, 32.7% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.3 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.6 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +10.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.3 | +0.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.1 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel modulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:84,971,093-85,059,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEBT91, PCMF, DKFZP434L1021, ZZZ1 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; UBR4 complex |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0J7](https://www.uniprot.org/uniprotkb/Q9P0J7) (E3 ubiquitin-protein ligase KCMF1):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme and then transfers it to targeted substrates, promoting their degradation by the proteasome. Together with UBR4, component of the N-end rule pathway: ubiquitinates proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their degradation. Does not ubiquitinate proteins that are acetylated at the N-terminus. Together with UBR4, part of a protein quality …

**Summary**, from NCBI Gene [56888](https://www.ncbi.nlm.nih.gov/gene/56888):

> Enables ubiquitin protein ligase activity. Involved in several processes, including HRI-mediated signaling; negative regulation of HRI-mediated signaling; and protein polyubiquitination. Located in cytosol. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20589) · Entrez [56888](https://www.ncbi.nlm.nih.gov/gene/56888) · UniProt [Q9P0J7](https://www.uniprot.org/uniprotkb/Q9P0J7) · Ensembl [ENSG00000176407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176407)

## Data

Gene col 10715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10715); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10715]; `tensor/DDL_lfc|DDL_z.npy` [10715]; `embed/gene_vectors.npy` [10715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10715 or target_col == 10715). Every well: [[KCMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
