---
symbol: "TM9SF2"
type: "gene"
col: 4600
ensembl_id: "ENSG00000125304"
name: "transmembrane 9 superfamily member 2"
location: "13q32.3"
module: 42
arm: "+"
pooled_cpm: 148.89
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TM9SF2

*transmembrane 9 superfamily member 2* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +8.5, q 7e-15, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.82× (z +6.9, q 1e-09, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 2.94×, SK-MEL-2 3.12×, A-172 2.03×, HS-578T 2.65×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 2.69×, SW480 2.01×; ⚠ cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.63×, SW480 1.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.24×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.479× (z -23.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER3IP1]] (+0.77, fdr 7e-06), [[LAPTM4A]] (+0.77, fdr 7e-06), [[SEC23A]] (+0.75, fdr 7e-06); moves opposite to [[RPL7L1]] (-0.69, fdr 7e-06), [[THG1L]] (-0.69, fdr 7e-06), [[CMTR2]] (-0.69, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 2.94×, SK-MEL-2 3.12×, A-172 2.03×, HS-578T 2.65×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 2.69×, SW480 2.01×; ⚠ cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.63×, SW480 1.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 3.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.5 | 7e-15 | 38/49 (SNU-423, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +6.9 | 1e-09 | 37/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +5.4 | 1e-05 | 27/45 (SNU-423, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.0 | 9e-05 | 23/44 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.9 | 9e-05 | 30/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.7 | 3e-04 | 28/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +3.2 | 0.11 | 15/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.12 | 10/48 (SW480, Hs 766T, …) | rises with dose | plate-row cell shift |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.12 | 12/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4600.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.479×** | -23.0 | 0e+00 | 47/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.459×** | -16.6 | 0e+00 | 46/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -15.0 | 0e+00 | 43/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -12.0 | 9e-31 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -7.7 | 1e-12 | 42/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -7.1 | 2e-10 | 37/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.741×** | -6.4 | 1e-08 | 31/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.777×** | -5.6 | 1e-06 | 33/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.788×** | -5.3 | 8e-06 | 23/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.856× | -4.9 | 5e-05 | 23/49 (A549, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.6 | 2e-04 | 26/47 (C32, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.6 | 3e-04 | 18/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.845× | -3.7 | 0.008 | 18/49 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.847× | -3.7 | 0.009 | 22/48 (AsPC-1, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.858× | -3.4 | 0.024 | 14/48 (LoVo, J82, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.871× | -3.1 | 0.070 | 12/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.911× | -3.0 | 0.093 | 5/48 (Hs 766T, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 163 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -35.0) |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -19.7) |
| [[A498 (line)]] | wt | 245 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -17.7) |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -24.3) |
| [[PANC-1 (line)]] | alt | 96.4 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 140 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -13.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.383× (z -11.0) |
| [[HOP62 (line)]] | alt | 106 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -23.6) |
| [[LoVo (line)]] | wt | 144 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 269 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 95.1 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 194 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.87× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -16.4) |
| [[SNU-423 (line)]] | alt | 98.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.8) |
| [[SW480 (line)]] | alt | 218 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.24× (z +10.0) | — |
| [[C32 (line)]] | wt | 134 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -19.8) |
| [[HT-29 (line)]] | alt | 188 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -22.5) |
| [[J82 (line)]] | alt | 165 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -25.2) |
| [[KATO III (line)]] | alt | 178 | 2 (2 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 1.90× (z +8.8) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -21.0) |
| [[SW 900 (line)]] | alt | 153 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.356× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -20.1) |
| [[Hs 766T (line)]] | wt | 223 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.9) |
| [[LS 180 (line)]] | wt | 210 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.6) |
| [[BT-474 (line)]] | alt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.8) |
| [[COLO 205 (line)]] | alt | 450 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +9.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -15.7) |
| [[H4 (line)]] | wt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.7) |
| [[HS-578T (line)]] | alt | 87.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -13.1) |
| [[SW1417 (line)]] | alt | 151 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -12.5) |
| [[A-427 (line)]] | wt | 94.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.522× (z -8.6) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.9) |
| [[CHP-212 (line)]] | wt | 139 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.194× (z -11.1) |
| [[HCT15 (line)]] | alt | 223 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 69.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 98.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -14.7) |
| [[RKO (line)]] | wt | 72.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -11.4) |
| [[SW 1088 (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.0) |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER3IP1]] | +0.77 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.77 | +0.81 / +0.73 | both halves | 7e-06 | STRING 685 |
| [[SEC23A]] | +0.75 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[STRAP]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[GGCX]] | +0.72 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.72 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[STT3A]] | +0.71 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[EFCAB14]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.71 | +0.81 / +0.57 | both halves | 9e-06 |  |
| [[SAR1A]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[GPR107]] | +0.70 | +0.77 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7L1]] | -0.69 | -0.75 / -0.63 | both halves | 7e-06 |  |
| [[THG1L]] | -0.69 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[CMTR2]] | -0.69 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[RPP25L]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[PBDC1]] | -0.67 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.67 | -0.74 / -0.58 | both halves | 8e-06 |  |
| [[TRIM47]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ZNF525]] | -0.65 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.65 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[NOP56]] | -0.65 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[ESF1]] | -0.65 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[METTL18]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN13]] | B | TSPAN13 activity raises TM9SF2's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without TSPAN13 | 0.074 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[P3H3]] | B | P3H3 activity lowers TM9SF2's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.29× higher at baseline in the lines without P3H3 | 0.099 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[P3H1]] | C | P3H1 activity lowers TM9SF2's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.75× higher at baseline in the lines without P3H1 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -30.6); signed map (-50.2, -5.0). **Vector** length 134, 44.5% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.63 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.59 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.58 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -12.3 | -12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.8 | -16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.2 | -23.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.2 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -15.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 9 superfamily member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:99,446,311-99,564,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P76, Lnc-PCIR |
| Gene groups (HGNC) | Transmembrane 9 superfamily members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99805](https://www.uniprot.org/uniprotkb/Q99805) (Transmembrane 9 superfamily member 2):

> In the intracellular compartments, may function as a channel or small molecule transporter.

**Summary**, from NCBI Gene [9375](https://www.ncbi.nlm.nih.gov/gene/9375):

> This gene encodes a member of the transmembrane 9 superfamily. The encoded 76 kDa protein localizes to early endosomes in human cells. The encoded protein possesses a conserved and highly hydrophobic C-terminal domain which contains nine transmembrane domains. The protein may play a role in small molecule transport or act as an ion channel. A pseudogene associated with this gene is located on the X chromosome. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:11865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11865) · Entrez [9375](https://www.ncbi.nlm.nih.gov/gene/9375) · UniProt [Q99805](https://www.uniprot.org/uniprotkb/Q99805) · Ensembl [ENSG00000125304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125304)

## Data

Gene col 4600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4600); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4600]; `tensor/DDL_lfc|DDL_z.npy` [4600]; `embed/gene_vectors.npy` [4600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4600 or target_col == 4600). Every well: [[TM9SF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM9SF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
