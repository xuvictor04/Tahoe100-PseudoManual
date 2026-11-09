---
symbol: "NCOR2"
type: "gene"
col: 12220
ensembl_id: "ENSG00000196498"
name: "nuclear receptor corepressor 2"
location: "12q24.31"
module: 2
arm: "+"
pooled_cpm: 264.65
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NCOR2

*nuclear receptor corepressor 2* — 12q24.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 2.00×, NCI-H1573 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.479× (z -21.8, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGFRL1]] (+0.66, fdr 1e-05), [[BCAM]] (+0.65, fdr 3e-05), [[PLXND1]] (+0.64, fdr 1e-05); moves opposite to [[FAAP24]] (-0.58, fdr 3e-05), [[DNAJC30]] (-0.58, fdr 2e-05), [[CPT2]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12220.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 2.00×, NCI-H1573 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.1 | 2e-04 | 23/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.7 | 0.059 | 21/49 (KATO III, BT-474, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.085 | 19/47 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -21.8 | 0e+00 | 46/49 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.576×** | -16.4 | 0e+00 | 37/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.524×** | -13.5 | 2e-39 | 42/48 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.684×** | -11.2 | 4e-27 | 39/48 (RKO, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.580×** | -11.0 | 6e-26 | 43/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -10.7 | 1e-24 | 40/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.684×** | -7.9 | 2e-13 | 38/48 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.771×** | -7.7 | 1e-12 | 36/48 (HOP62, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.694×** | -7.7 | 1e-12 | 36/48 (A-172, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.688×** | -7.5 | 3e-12 | 29/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.700×** | -7.5 | 4e-12 | 42/48 (J82, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.703×** | -7.1 | 6e-11 | 40/50 (SW480, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -6.9 | 2e-10 | 37/49 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.723×** | -6.8 | 5e-10 | 35/48 (A-172, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -6.6 | 1e-09 | 32/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -6.3 | 8e-09 | 30/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.782×** | -5.1 | 9e-06 | 36/48 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.774×** | -5.1 | 1e-05 | 30/48 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -4.6 | 1e-04 | 27/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.823×** | -4.1 | 0.001 | 23/48 (SNU-1, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -4.1 | 0.001 | 24/48 (HT-29, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 356 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -29.1) |
| [[HOP62 (line)]] | alt | 322 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -23.1) |
| [[A-172 (line)]] | wt | 438 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.9) |
| [[Hs 766T (line)]] | wt | 495 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -20.4) |
| [[PANC-1 (line)]] | alt | 333 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -17.3) |
| [[SW480 (line)]] | alt | 201 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -26.9) |
| [[J82 (line)]] | alt | 353 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 387 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -21.7) |
| [[CFPAC-1 (line)]] | alt | 316 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -21.5) |
| [[HS-578T (line)]] | alt | 254 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -17.3) |
| [[KATO III (line)]] | alt | 363 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -21.1) |
| [[LOX-IMVI (line)]] | wt | 356 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 153 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 219 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 207 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -18.0) |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -17.0) |
| [[AN3 CA (line)]] | alt | 424 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.8) |
| [[COLO 205 (line)]] | alt | 281 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -19.5) |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -12.0) |
| [[RKO (line)]] | wt | 142 | 0 | 5 | — | [[Selinexor (drug)]] 5 µM 0.430× (z -14.9) |
| [[HT-29 (line)]] | alt | 305 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 387 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -15.7) |
| [[SW1417 (line)]] | alt | 240 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -17.9) |
| [[BT-474 (line)]] | alt | 252 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -12.5) |
| [[LS 180 (line)]] | wt | 315 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 274 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -22.8) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -14.0) |
| [[SW 900 (line)]] | alt | 204 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.0) |
| [[SW48 (line)]] | wt | 251 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.0) |
| [[A-427 (line)]] | wt | 171 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -16.8) |
| [[A549 (line)]] | wt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -11.2) |
| [[C32 (line)]] | wt | 184 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 199 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.2) |
| [[SNU-423 (line)]] | alt | 231 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.491× (z -12.7) |
| [[H4 (line)]] | wt | 262 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.9) |
| [[HCT15 (line)]] | alt | 222 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.6) |
| [[SNU-1 (line)]] | wt | 169 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.370× (z -14.5) |
| [[SW 1088 (line)]] | alt | 392 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -13.4) |
| [[A498 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 207 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 214 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGFRL1]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[BCAM]] | +0.65 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[PLXND1]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Signaling by NOTCH |
| [[COL18A1]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LAMA5]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[INF2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.60 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[HIP1R]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PITPNM1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CYB5R3]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAP24]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[DNAJC30]] | -0.58 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CPT2]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 | pathway: PPARA activates gene expression |
| [[CNPY2]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PCF11-AS1]] | -0.56 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[COA6]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[SMIM10L1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[YARS2]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PIGP]] | -0.54 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ATP6V0D1-DT]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PAAF1]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[HSCB]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NCOR2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARHGAP23]] | B | ARHGAP23 activity raises NCOR2's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without ARHGAP23 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[MYRF]] | B | MYRF activity lowers NCOR2's level | lines that do not express MYRF (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without MYRF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPB41L4B, IL23A; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.8, -5.1); signed map (-11.2, 30.1). **Vector** length 115, 37.5% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.9 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.5 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.1 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.5 | -7.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.3 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -13.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -7.7 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor corepressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:124,324,415-124,567,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMRT, SMRTE, TRAC-1, CTG26, TNRC14 |
| Gene groups (HGNC) | Myb/SANT domain containing; NCoR/SMRT transcriptional repression complex subunits |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, TGF_BETA_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 53 pathways, smallest: Loss of MECP2 binding ability to the NCoR/SMRT complex; NR1H2 & NR1H3 regulate gene expression to control bile acid homeostasis; Disorders of Nervous System Development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y618](https://www.uniprot.org/uniprotkb/Q9Y618) (Nuclear receptor corepressor 2):

> Transcriptional corepressor that mediates the transcriptional repression activity of some nuclear receptors by promoting chromatin condensation, thus preventing access of the basal transcription. Acts by recruiting chromatin modifiers, such as histone deacetylases HDAC1, HDAC2 and HDAC3. Required to activate the histone deacetylase activity of HDAC3. Involved in the regulation BCL6-dependent of the germinal center (GC) reactions, mainly through the control of the GC B-cells proliferation and …

**Summary**, from NCBI Gene [9612](https://www.ncbi.nlm.nih.gov/gene/9612):

> This gene encodes a nuclear receptor co-repressor that mediates transcriptional silencing of certain target genes. The encoded protein is a member of a family of thyroid hormone- and retinoic acid receptor-associated co-repressors. This protein acts as part of a multisubunit complex which includes histone deacetylases to modify chromatin structure that prevents basal transcriptional activity of target genes. Aberrant expression of this gene is associated with certain cancers. Alternate splicing …

**Accessions** — [HGNC:7673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7673) · Entrez [9612](https://www.ncbi.nlm.nih.gov/gene/9612) · UniProt [Q9Y618](https://www.uniprot.org/uniprotkb/Q9Y618) · Ensembl [ENSG00000196498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196498)

## Data

Gene col 12220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12220); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12220]; `tensor/DDL_lfc|DDL_z.npy` [12220]; `embed/gene_vectors.npy` [12220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12220 or target_col == 12220). Every well: [[NCOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
