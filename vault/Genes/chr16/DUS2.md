---
symbol: "DUS2"
type: "gene"
col: 9443
ensembl_id: "ENSG00000167264"
name: "dihydrouridine synthase 2"
location: "16q22.1"
module: 5
arm: "+"
pooled_cpm: 12.8
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DUS2

*dihydrouridine synthase 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.68× (z +39.0, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.645× (z -6.9, q 2e-09, down in 24 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.829× (z -4.2, q 0.004, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.113×, NCI-H2030 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.314×, NCI-H460 0.381×; ⚠ cell-cycle shift, explains ~24% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (C32 0.0851×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW48 0.0889×); [[Simotinib (drug)]] 0.05 µM in 1 line (SW48 0.0974×); [[Bimiralisib (drug)]] 0.05 µM in 1 line (CHP-212 0.0829×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF10]] (+0.68, fdr 1e-05), [[PIGW]] (+0.68, fdr 1e-05), [[MRM1]] (+0.68, fdr 1e-05); moves opposite to [[HDAC5]] (-0.64, fdr 1e-05), [[USP2]] (-0.63, fdr 2e-05), [[SVIP]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CAMK2N1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.68×** | +39.0 | 0e+00 | 44/44 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +11.1 | 3e-26 | 34/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.6 | 1e-15 | 30/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +7.5 | 7e-12 | 27/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.8 | 1e-09 | 29/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.9 | 1e-04 | 19/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.77×** | +4.7 | 2e-04 | 9/44 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.7 | 2e-04 | 20/46 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.23×** | +4.6 | 2e-04 | 18/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.73×** | +4.6 | 3e-04 | 7/45 (SW480, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.008 | 5/45 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.014 | 6/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.063 | 6/43 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.065 | 2/45 (SHP-77, SNU-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.21×** | +3.0 | 0.093 | 7/44 (HT-29, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.113×, NCI-H2030 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.314×, NCI-H460 0.381×; ⚠ cell-cycle shift, explains ~24% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (C32 0.0851×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (SW48 0.0889×); [[Simotinib (drug)]] 0.05 µM in 1 line (SW48 0.0974×); [[Bimiralisib (drug)]] 0.05 µM in 1 line (CHP-212 0.0829×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.9 | 2e-09 | 24/46 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.720×** | -4.8 | 4e-04 | 12/28 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -4.6 | 7e-04 | 20/48 (SW480, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -4.2 | 0.004 | 19/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -4.0 | 0.007 | 14/42 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.788×** | -3.6 | 0.028 | 11/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.068 | 3/48 (Hs 766T, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 13.6 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +25.4) | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 15.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +11.1) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0889× (z -9.8) |
| [[C32 (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +16.1) | [[Docetaxel (drug)]] 0.05 µM 0.0851× (z -11.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0948× (z -8.6) ⚠ toxic · without an alert: [[Bimiralisib (drug)]] 0.05 µM 0.0829× (z -8.6) |
| [[HOP62 (line)]] | alt | 12.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +16.8) | — |
| [[KATO III (line)]] | alt | 13.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 8.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +18.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -8.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 9.21 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +18.7) | — |
| [[SW480 (line)]] | alt | 28.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +17.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 6.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +11.2) | — |
| [[A498 (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +16.7) | — |
| [[A549 (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.62× (z +15.6) | — |
| [[AsPC-1 (line)]] | alt | 5.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +20.5) | — |
| [[C-33 A (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +14.4) | — |
| [[H4 (line)]] | wt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 6.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 6.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.9) | — |
| [[J82 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +19.3) | — |
| [[LS 180 (line)]] | wt | 9.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 9.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 5.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 8.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +9.1) | — |
| [[RKO (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 9.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 5.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.2) | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PIGW]] | +0.68 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MRM1]] | +0.68 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PRR3]] | +0.67 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ALG8]] | +0.67 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 | same gene group |
| [[MRTO4]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[DHX37]] | +0.64 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PRORP]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 | pathway: tRNA processing |
| [[METTL13]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TLCD3A]] | +0.63 | +0.19 / +0.64 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TRMT1]] | +0.62 | +0.43 / +0.63 | both halves | 3e-05 | pathway: tRNA modification in the nucleus and cytosol; STRING 758 |
| [[FBXW9]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[USP2]] | -0.63 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[SVIP]] | -0.61 | -0.26 / -0.58 | both halves | 3e-04 |  |
| [[YPEL2]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CYRIA]] | -0.58 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[MGAT4A]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ALAD]] | -0.57 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[GDE1]] | -0.57 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[SNX15]] | -0.57 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.56 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[STARD5]] | -0.55 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[TUFT1]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[TMOD2]] | -0.55 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK2N1]] | B | CAMK2N1 activity lowers DUS2's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.66× higher at baseline in the lines without CAMK2N1 | 0.007 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DUS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TPST1]] | B | TPST1 activity raises DUS2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without TPST1 | 0.087 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.9, 10.4); signed map (24.7, -29.7). **Vector** length 82.9, 15.6% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +39.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dihydrouridine synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,987,746-68,079,320 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20399, SMM1; previously DUS2L |
| Gene groups (HGNC) | Flavoproteins; Dihydrouridine synthase family |
| Reactome | 7 pathways, smallest: tRNA modification in the nucleus and cytosol; PKR-mediated signaling; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX74](https://www.uniprot.org/uniprotkb/Q9NX74) (tRNA-dihydrouridine(20) synthase):

> Catalyzes the NADPH-dependent synthesis of dihydrouridine, a modified base found in the D-loop of most tRNAs. Specifically modifies U20 in cytoplasmic tRNAs. Activity depends on the presence of guanosine at position 19 in the tRNA substrate. Negatively regulates the activation of EIF2AK2/PKR.

**Summary**, from NCBI Gene [54920](https://www.ncbi.nlm.nih.gov/gene/54920):

> This gene encodes a cytoplasmic protein that catalyzes the conversion of uridine residues to dihydrouridine in the D-loop of tRNA. The resulting modified bases confer enhanced regional flexibility to tRNA. The encoded protein may increase the rate of translation by inhibiting an interferon-induced protein kinase. This gene has been implicated in pulmonary carcinogenesis. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:26014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26014) · Entrez [54920](https://www.ncbi.nlm.nih.gov/gene/54920) · UniProt [Q9NX74](https://www.uniprot.org/uniprotkb/Q9NX74) · Ensembl [ENSG00000167264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167264)

## Data

Gene col 9443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9443); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9443]; `tensor/DDL_lfc|DDL_z.npy` [9443]; `embed/gene_vectors.npy` [9443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9443 or target_col == 9443). Every well: [[DUS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
