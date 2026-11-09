---
symbol: "PARP4"
type: "gene"
col: 2262
ensembl_id: "ENSG00000102699"
name: "poly(ADP-ribose) polymerase family member 4"
location: "13q12.12"
module: 3
arm: "-"
pooled_cpm: 202.46
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 44
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PARP4

*poly(ADP-ribose) polymerase family member 4* — 13q12.12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.10×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.239× (z -24.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK4]] (+0.51, fdr 3e-05), [[IL6ST]] (+0.51, fdr 1e-04), [[PTER]] (+0.51, fdr 1e-04); moves opposite to [[SLC29A4]] (-0.49, fdr 1e-04), [[GFOD2]] (-0.49, fdr 1e-04), [[SDHAP4-1]] (-0.48, fdr 4e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.10×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.21× | +3.3 | 0.39 | 25/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | 1.41× | +3.1 | 0.39 | 21/48 (PANC-1, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.39 | 21/47 (LS 180, HEC-1-A, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.239×** | -24.3 | 0e+00 | 48/48 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.261×** | -22.8 | 0e+00 | 47/48 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.264×** | -22.6 | 0e+00 | 47/48 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.443×** | -19.5 | 0e+00 | 47/49 (RKO, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.440×** | -13.9 | 8e-42 | 47/48 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.444×** | -13.7 | 5e-41 | 48/48 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.457×** | -13.3 | 2e-38 | 47/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.627×** | -11.2 | 4e-27 | 35/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -10.3 | 5e-23 | 42/47 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -9.3 | 6e-19 | 48/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.579×** | -9.3 | 1e-18 | 44/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.641×** | -7.5 | 3e-12 | 41/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.654×** | -7.2 | 3e-11 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.636×** | -7.1 | 6e-11 | 32/45 (HT-29, KATO III, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.462×** | -6.8 | 3e-10 | 42/49 (HepG2/C3A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -6.5 | 4e-09 | 33/48 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -6.0 | 5e-08 | 28/48 (SNU-423, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -6.0 | 7e-08 | 35/48 (Hs 766T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.526×** | -5.7 | 4e-07 | 38/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.539×** | -5.5 | 1e-06 | 40/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.8 | 3e-05 | 26/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 199 | 0 | 17 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -21.0) |
| [[SW480 (line)]] | alt | 239 | 0 | 17 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.205× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 343 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -17.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 320 | 0 | 12 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.173× (z -18.4) |
| [[COLO 205 (line)]] | alt | 706 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -27.8) |
| [[Hs 766T (line)]] | wt | 332 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 282 | 0 | 11 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.222× (z -16.9) |
| [[PANC-1 (line)]] | alt | 151 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -16.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.5) |
| [[SNU-423 (line)]] | alt | 165 | 0 | 11 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.127× (z -22.5) |
| [[RKO (line)]] | wt | 283 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -21.2) |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -18.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -16.8) |
| [[A549 (line)]] | wt | 246 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 9 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.103× (z -25.7) |
| [[HT-29 (line)]] | alt | 521 | 0 | 9 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.220× (z -19.8) |
| [[KATO III (line)]] | alt | 396 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -28.1) |
| [[LoVo (line)]] | wt | 210 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -25.6) |
| [[BT-474 (line)]] | alt | 131 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.170× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.185× (z -18.0) |
| [[HOP62 (line)]] | alt | 136 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.175× (z -18.8) |
| [[HS-578T (line)]] | alt | 88.3 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.180× (z -18.5) |
| [[LS 180 (line)]] | wt | 322 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -26.7) |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -23.1) |
| [[A-172 (line)]] | wt | 209 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -19.7) |
| [[C32 (line)]] | wt | 195 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -14.3) |
| [[HCT15 (line)]] | alt | 369 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -22.5) |
| [[SW 900 (line)]] | alt | 178 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.212× (z -16.7) |
| [[SW1417 (line)]] | alt | 144 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.318× (z -13.5) |
| [[A498 (line)]] | wt | 171 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.297× (z -12.6) |
| [[H4 (line)]] | wt | 151 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.233× (z -13.3) |
| [[J82 (line)]] | alt | 169 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.272× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 185 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 98.4 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -14.0) |
| [[SNU-1 (line)]] | wt | 222 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.8) |
| [[SW48 (line)]] | wt | 242 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -18.8) |
| [[AsPC-1 (line)]] | alt | 164 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.197× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.315× (z -12.7) |
| [[A-427 (line)]] | wt | 76.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 127 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -9.1) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 69.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -10.3) |
| [[SHP-77 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.389× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 235 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.163× (z -10.5) |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[IL6ST]] | +0.51 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[PTER]] | +0.51 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[SPG11]] | +0.50 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[TRMT13]] | +0.49 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[ZNF252P]] | +0.48 | +0.23 / +0.54 | both halves | 5e-04 |  |
| [[SLF2]] | +0.47 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[SLK]] | +0.46 | +0.25 / +0.52 | both halves | 4e-04 |  |
| [[STX17]] | +0.45 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[DTX3L]] | +0.45 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[EIF2B5]] | +0.45 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[ZBTB38]] | +0.45 | +0.36 / +0.43 | both halves | 9e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 13 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC29A4]] | -0.49 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[GFOD2]] | -0.49 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[SDHAP4-1]] | -0.48 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[TBC1D22A-DT]] | -0.48 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[SBK1]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[PTMAP2]] ⚠ | -0.47 | -0.34 / -0.42 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[UBTD1]] | -0.47 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[RGS10]] | -0.47 | -0.24 / -0.52 | both halves | 4e-04 |  |
| [[MIR4458HG]] | -0.47 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[MARK4]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SNHG18]] | -0.46 | -0.20 / -0.53 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MED26]] | -0.46 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CHST12]] | -0.46 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[FAM168A]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.1, 0.9); signed map (15.3, -32.7). **Vector** length 96.8, 37.1% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.9 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | -0.2 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:24,420,931-24,512,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VAULT3, p193, VPARP, VWA5C, ARTD4; previously ADPRTL1 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKK3](https://www.uniprot.org/uniprotkb/Q9UKK3) (Protein mono-ADP-ribosyltransferase PARP4):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins. Component of the vault particle, which is a massive ribonucleoprotein complex that may play a role in cargo transport and signal transduction.

**Summary**, from NCBI Gene [143](https://www.ncbi.nlm.nih.gov/gene/143):

> This gene encodes poly(ADP-ribosyl)transferase-like 1 protein, which is capable of catalyzing a poly(ADP-ribosyl)ation reaction. This protein has a catalytic domain which is homologous to that of poly (ADP-ribosyl) transferase, but lacks an N-terminal DNA binding domain which activates the C-terminal catalytic domain of poly (ADP-ribosyl) transferase. Since this protein is not capable of binding DNA directly, its transferase activity may be activated by other factors such as protein-protein …

**Accessions** — [HGNC:271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:271) · Entrez [143](https://www.ncbi.nlm.nih.gov/gene/143) · UniProt [Q9UKK3](https://www.uniprot.org/uniprotkb/Q9UKK3) · Ensembl [ENSG00000102699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102699)

## Data

Gene col 2262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2262); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2262]; `tensor/DDL_lfc|DDL_z.npy` [2262]; `embed/gene_vectors.npy` [2262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2262 or target_col == 2262). Every well: [[PARP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
