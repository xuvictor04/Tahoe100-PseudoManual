---
symbol: "SUN1"
type: "gene"
col: 9012
ensembl_id: "ENSG00000164828"
name: "Sad1 and UNC84 domain containing 1"
location: "7p22.3"
module: 2
arm: "+"
pooled_cpm: 159.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SUN1

*Sad1 and UNC84 domain containing 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.00× (z +18.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.810× (z -5.4, q 3e-05, down in 26 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.819× (z -5.3, q 3e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.223×, SHP-77 0.259×, C-33 A 0.261×, NCI-H1573 0.390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.346×, A-427 0.537×, C-33 A 0.422×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.454×, C-33 A 0.367×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.374×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAI2]] (+0.68, fdr 4e-05), [[DNAAF3]] (+0.68, fdr 3e-05), [[TNK2]] (+0.66, fdr 2e-05); moves opposite to [[KLHL42]] (-0.64, fdr 7e-05), [[TACO1]] (-0.60, fdr 5e-05), [[SHLD1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BAIAP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +18.4 | 0e+00 | 44/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +15.1 | 0e+00 | 46/48 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +12.1 | 2e-31 | 44/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +8.3 | 1e-14 | 33/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.0 | 3e-10 | 27/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +6.2 | 5e-08 | 29/48 (RPMI-7951, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +5.4 | 5e-06 | 26/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 33/49 (NCI-H460, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +4.9 | 7e-05 | 24/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.002 | 20/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.9 | 0.005 | 13/48 (LOX-IMVI, CHP-212, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.15× | +3.7 | 0.010 | 17/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.020 | 10/47 (H4, LoVo, …) | two highest doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.030 | 18/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.12× | +3.1 | 0.072 | 11/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9012.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.223×, SHP-77 0.259×, C-33 A 0.261×, NCI-H1573 0.390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.346×, A-427 0.537×, C-33 A 0.422×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.454×, C-33 A 0.367×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.374×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.810×** | -5.4 | 3e-05 | 26/47 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.819×** | -5.3 | 3e-05 | 25/48 (NCI-H1573, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -5.1 | 7e-05 | 12/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.830×** | -4.8 | 3e-04 | 23/48 (A-427, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | 0.841× | -4.4 | 0.001 | 22/44 (NCI-H23, SHP-77, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.848× | -4.4 | 0.001 | 19/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.895× | -4.2 | 0.003 | 11/48 (Panc 03.27, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.863× | -3.9 | 0.007 | 16/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.861× | -3.8 | 0.009 | 15/48 (NCI-H1573, C-33 A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.010 | 15/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.877× | -3.5 | 0.024 | 13/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.921× | -3.1 | 0.094 | 3/48 (SHP-77, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 135 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +30.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +19.5) | — |
| [[COLO 205 (line)]] | alt | 101 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.346× (z -11.7) |
| [[C-33 A (line)]] | alt | 258 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.367× (z -9.6) |
| [[HT-29 (line)]] | alt | 193 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.06× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 301 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +14.2) | — |
| [[A-427 (line)]] | wt | 137 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.454× (z -12.2) |
| [[J82 (line)]] | alt | 102 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.93× (z +10.0) | — |
| [[KATO III (line)]] | alt | 266 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 93.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 170 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 160 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +10.9) | [[Lonafarnib (drug)]] 5 µM 0.100× (z -16.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 107 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 173 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 210 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +13.9) | — |
| [[A498 (line)]] | wt | 166 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.4) | — |
| [[H4 (line)]] | wt | 238 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.38× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 110 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 114 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 76.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +11.5) | — |
| [[LoVo (line)]] | wt | 162 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 184 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[PANC-1 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +18.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.13× (z +12.7) | — |
| [[RKO (line)]] | wt | 94.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.9) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.508× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 97.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 156 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.91× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 236 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.442× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[HEC-1-A (line)]] | alt | 119 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 186 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +11.6) | — |
| [[SW48 (line)]] | wt | 188 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.1) | — |
| [[A-172 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 169 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 246 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | +0.68 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[DNAAF3]] | +0.68 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TNK2]] | +0.66 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FGFRL1]] | +0.66 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PLCB3]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HMG20B]] | +0.63 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NXPH4]] | +0.62 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[QSOX1]] | +0.61 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[F11R]] | +0.60 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[BAIAP3]] | +0.60 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[PEDS1]] | +0.60 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[SNX25]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL42]] | -0.64 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[TACO1]] | -0.60 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[SHLD1]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SMIM10L1]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TYW3]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[SMAD1]] | -0.57 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[RPP38]] | -0.57 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[NIPAL2]] | -0.57 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[METTL18]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[GABPB1]] | -0.57 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[FUNDC1]] | -0.57 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAIAP3]] | B | BAIAP3 activity raises SUN1's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without BAIAP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent |
| [[SLC16A14]] | B | SLC16A14 activity lowers SUN1's level | lines that do not express SLC16A14 (16) vs lines expressing it (34) | 1.02× higher at baseline in the lines without SLC16A14 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, ARHGEF16, NEBL |
| [[HDAC6]] | B | HDAC6 activity lowers SUN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.1, -4.8); signed map (-29.7, 21.2). **Vector** length 119, 34.3% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +18.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.4 | +15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.3 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -6.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.1 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Sad1 and UNC84 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:816,615-896,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0810, FLJ12407; previously UNC84A |
| Gene groups (HGNC) | SUN family |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O94901](https://www.uniprot.org/uniprotkb/O94901) (SUN domain-containing protein 1):

> As a component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and positioning (By similarity). Required for interkinetic nuclear migration (INM) and essential for nucleokinesis and centrosome-nucleus coupling during radial …

**Summary**, from NCBI Gene [23353](https://www.ncbi.nlm.nih.gov/gene/23353):

> This gene is a member of the unc-84 homolog family and encodes a nuclear envelope protein with an Unc84 (SUN) domain. The protein is involved in nuclear anchorage and migration. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2019]

**Accessions** — [HGNC:18587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18587) · Entrez [23353](https://www.ncbi.nlm.nih.gov/gene/23353) · UniProt [O94901](https://www.uniprot.org/uniprotkb/O94901) · Ensembl [ENSG00000164828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164828)

## Data

Gene col 9012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9012); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9012]; `tensor/DDL_lfc|DDL_z.npy` [9012]; `embed/gene_vectors.npy` [9012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9012 or target_col == 9012). Every well: [[SUN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
