---
symbol: "USP8"
type: "gene"
col: 6187
ensembl_id: "ENSG00000138592"
name: "ubiquitin specific peptidase 8"
location: "15q21.2"
module: 12
arm: "+"
pooled_cpm: 181.65
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# USP8

*ubiquitin specific peptidase 8* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +17.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.755× (z -9.0, q 2e-16, down in 30 of 45 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW48 0.231×, NCI-H1573 0.457×, C-33 A 0.357×, A549 0.506×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-1 0.283×, A-427 0.450×, KATO III 0.488×, RPMI-7951 0.577×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.617×; ⚠ cell-cycle shift, explains ~25% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.581×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGB1]] (+0.68, fdr 7e-06), [[GOSR1]] (+0.66, fdr 7e-06), [[SLC4A1AP]] (+0.66, fdr 7e-06); moves opposite to [[TMTC4]] (-0.60, fdr 3e-05), [[NUP93]] (-0.56, fdr 1e-05), [[UCK2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +17.1 | 0e+00 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +12.8 | 8e-35 | 40/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +10.5 | 1e-23 | 35/48 (LoVo, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +7.7 | 2e-12 | 29/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +6.6 | 6e-09 | 28/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +6.4 | 1e-08 | 26/48 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +5.3 | 7e-06 | 18/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 1e-05 | 22/48 (LoVo, A-172, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.17× | +5.1 | 2e-05 | 20/50 (C32, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.16× | +4.9 | 5e-05 | 20/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.10× | +4.5 | 3e-04 | 16/49 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +4.5 | 3e-04 | 7/48 (A-172, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 26/47 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.13× | +4.1 | 0.002 | 20/48 (NCI-H2030, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 21/48 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.007 | 12/49 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.5 | 0.013 | 9/48 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.09× | +3.0 | 0.071 | 5/48 (LoVo, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.18× | +2.9 | 0.078 | 10/48 (Hs 766T, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6187.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW48 0.231×, NCI-H1573 0.457×, C-33 A 0.357×, A549 0.506×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-1 0.283×, A-427 0.450×, KATO III 0.488×, RPMI-7951 0.577×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.617×; ⚠ cell-cycle shift, explains ~25% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SNU-423 0.581×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -9.0 | 2e-16 | 30/45 (SNU-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -6.8 | 2e-09 | 12/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.854× | -5.2 | 3e-05 | 20/44 (SW48, NCI-H1573, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.877× | -4.5 | 8e-04 | 10/49 (A-172, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.921× | -4.0 | 0.007 | 1/48 (SNU-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -3.8 | 0.013 | 10/48 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.897× | -3.8 | 0.013 | 3/48 (SK-MEL-2, SNU-423, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.928× | -3.6 | 0.019 | 0/48 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.904× | -3.5 | 0.031 | 5/48 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.903× | -3.4 | 0.041 | 16/47 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.937× | -3.2 | 0.067 | 1/48 (AsPC-1) | top dose only |  |
| [[Roxadustat (drug)]] 0.05 µM |  | 0.908× | -3.1 | 0.093 | 8/47 (SW48, CHP-212, …) | inconsistent across doses |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.941× | -3.0 | 0.11 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 174 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 205 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 101 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 236 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.2) | — |
| [[LoVo (line)]] | wt | 343 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.99× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 128 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.4) | — |
| [[SW48 (line)]] | wt | 190 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 173 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 88.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 221 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H1792 (line)]] | alt | 201 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 163 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 159 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +16.9) | — |
| [[BT-474 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.285× (z -8.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 256 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +13.0) | — |
| [[KATO III (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.488× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 174 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +12.0) | — |
| [[RKO (line)]] | wt | 198 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.577× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -14.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 128 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.581× (z -8.5) |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 199 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 204 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | +0.68 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SCFD1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KIN]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[YME1L1]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[KDM5A]] | +0.63 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[FCF1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[UFL1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SUPT6H]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC4]] | -0.60 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[NUP93]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[UCK2]] | -0.54 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[XPO5]] | -0.54 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[KPNA1]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[GLB1L2]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD52]] | -0.52 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[PPP4R1]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[GNAZ]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NCS1]] | -0.50 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[NUDT3]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[BTBD3]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity lowers USP8's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without NCS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-5.5, -48.1); signed map (-3.3, -12.6). **Vector** length 123, 35.6% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.8 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +17.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.6 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,424,380-50,514,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HumORF8, KIAA0055, UBPY, SPG59 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | COMPLEMENT |
| Reactome | 11 pathways, smallest: Downregulation of ERBB2:ERBB3 signaling; Regulation of FZD by ubiquitination; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P40818](https://www.uniprot.org/uniprotkb/P40818) (Ubiquitin carboxyl-terminal hydrolase 8):

> Hydrolase that can remove conjugated ubiquitin from proteins and therefore plays an important regulatory role at the level of protein turnover by preventing degradation. Converts both 'Lys-48' an 'Lys-63'-linked ubiquitin chains. Catalytic activity is enhanced in the M phase. Involved in cell proliferation. Required to enter into S phase in response to serum stimulation. May regulate T-cell anergy mediated by RNF128 via the formation of a complex containing RNF128 and OTUB1. Probably regulates …

**Summary**, from NCBI Gene [9101](https://www.ncbi.nlm.nih.gov/gene/9101):

> This gene encodes a protein that belongs to the ubiquitin-specific processing protease family of proteins. The encoded protein is thought to regulate the morphology of the endosome by ubiquitination of proteins on this organelle and is involved in cargo sorting and membrane trafficking at the early endosome stage. This protein is required for the cell to enter the S phase of the cell cycle and also functions as a positive regulator in the Hedgehog signaling pathway in development. Pseudogenes …

**Accessions** — [HGNC:12631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12631) · Entrez [9101](https://www.ncbi.nlm.nih.gov/gene/9101) · UniProt [P40818](https://www.uniprot.org/uniprotkb/P40818) · Ensembl [ENSG00000138592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138592)

## Data

Gene col 6187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6187); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6187]; `tensor/DDL_lfc|DDL_z.npy` [6187]; `embed/gene_vectors.npy` [6187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6187 or target_col == 6187). Every well: [[USP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
