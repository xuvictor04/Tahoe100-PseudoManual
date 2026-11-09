---
symbol: "AGO3"
type: "gene"
col: 4713
ensembl_id: "ENSG00000126070"
name: "argonaute RISC catalytic component 3"
location: "1p34.3"
module: 38
arm: "+"
pooled_cpm: 209.2
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# AGO3

*argonaute RISC catalytic component 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.35× (z +7.7, q 9e-12, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.512× (z -16.7, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.813× (z -7.6, q 5e-12, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02804]] (+0.63, fdr 3e-05), [[ORAI2]] (+0.62, fdr 7e-06), [[TFAP2E]] (+0.61, fdr 1e-05); moves opposite to [[COPS6]] (-0.46, fdr 1e-04), [[SPTBN1]] (-0.45, fdr 7e-05), [[PFKM]] (-0.44, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.7 | 9e-12 | 29/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.5 | 2e-08 | 25/48 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +6.1 | 2e-07 | 34/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 7e-04 | 23/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.5 | 7e-04 | 21/48 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 0.003 | 21/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.004 | 22/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.010 | 21/48 (SW480, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.035 | 22/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.067 | 3/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -16.7 | 0e+00 | 36/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -14.2 | 2e-43 | 44/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -9.1 | 1e-17 | 34/45 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -8.3 | 2e-14 | 34/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -7.6 | 5e-12 | 25/49 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -5.6 | 2e-06 | 19/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.827×** | -4.7 | 2e-04 | 24/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.854× | -4.1 | 0.003 | 20/48 (SW480, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.896× | -4.0 | 0.004 | 8/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.859× | -3.9 | 0.005 | 19/48 (SW480, HS-578T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 0.855× | -3.9 | 0.005 | 22/47 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.753×** | -3.8 | 0.006 | 27/49 (SNU-423, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.865× | -3.7 | 0.008 | 18/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.077 | 11/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 253 | 8 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.635× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 245 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.474× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 188 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 297 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 176 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.490× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 236 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.507× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 223 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.402× (z -13.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 252 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 253 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.545× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 190 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 239 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 236 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 286 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -15.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 225 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.567× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.562× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 204 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 158 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.87× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 292 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -14.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 179 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.544× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 312 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -24.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 286 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.438× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 179 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 239 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -13.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 147 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[AN3 CA (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.456× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.475× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -9.3) |
| [[H4 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.566× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 226 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -15.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.511× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.596× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 216 | 1 | 0 | [[Fulvestrant (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -14.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -28.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.5) |
| [[A-172 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02804]] | +0.63 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ORAI2]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TFAP2E]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TINCR]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GON4L]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CDK13]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HM13]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[USE1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[VWCE]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SELENOS]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MON2]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FLACC1]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS6]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SPTBN1]] | -0.45 | -0.38 / -0.44 | both halves | 7e-05 | pathway: Cell-Cell communication |
| [[PFKM]] | -0.44 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, -20.3); signed map (11.9, 12.4). **Vector** length 110, 34.0% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +4.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | -0.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.4 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | argonaute RISC catalytic component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,930,718-36,072,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hAGO3, FLJ12765; previously EIF2C3 |
| Gene groups (HGNC) | RISC loading complex subunits; Argonaute RISC component family |
| Reactome | 69 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9G7](https://www.uniprot.org/uniprotkb/Q9H9G7) (Protein argonaute-3):

> Required for RNA-mediated gene silencing (RNAi). Binds to short RNAs such as microRNAs (miRNAs) and represses the translation of mRNAs which are complementary to them. Proposed to be involved in stabilization of small RNA derivates (siRNA) derived from processed RNA polymerase III-transcribed Alu repeats containing a DR2 retinoic acid response element (RARE) in stem cells and in the subsequent siRNA-dependent degradation of a subset of RNA polymerase II-transcribed coding mRNAs by recruiting a …

**Summary**, from NCBI Gene [192669](https://www.ncbi.nlm.nih.gov/gene/192669):

> This gene encodes a member of the Argonaute family of proteins which play a role in RNA interference. The encoded protein is highly basic, contains a PAZ domain and a PIWI domain, and may play a role in short-interfering-RNA-mediated gene silencing. This gene is located on chromosome 1 in a tandem cluster of closely related family members including argonaute 4 and eukaryotic translation initiation factor 2C, 1. Two transcript variants encoding distinct isoforms have been identified for this …

**Accessions** — [HGNC:18421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18421) · Entrez [192669](https://www.ncbi.nlm.nih.gov/gene/192669) · UniProt [Q9H9G7](https://www.uniprot.org/uniprotkb/Q9H9G7) · Ensembl [ENSG00000126070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126070)

## Data

Gene col 4713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4713); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4713]; `tensor/DDL_lfc|DDL_z.npy` [4713]; `embed/gene_vectors.npy` [4713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4713 or target_col == 4713). Every well: [[AGO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
