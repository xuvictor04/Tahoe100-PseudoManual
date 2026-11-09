---
symbol: "ZGPAT"
type: "gene"
col: 12344
ensembl_id: "ENSG00000197114"
name: "zinc finger CCCH-type and G-patch domain containing"
location: "20q13.33"
module: 129
arm: "+"
pooled_cpm: 24.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# ZGPAT

*zinc finger CCCH-type and G-patch domain containing* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +13.2, q 4e-37, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.645× (z -6.7, q 1e-08, down in 26 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.771× (z -4.0, q 0.013, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 0.121×, NCI-H2030 0.150×, NCI-H460 0.145×, SHP-77 0.223×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.110×, A498 0.267×, NCI-H23 0.239×, SNU-423 0.244×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.258×, NCI-H2347 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0868×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C32 0.0933×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF865]] (+0.72, fdr 7e-06), [[C19orf47]] (+0.61, fdr 1e-05), [[ZNF707]] (+0.58, fdr 1e-05); moves opposite to [[BBX]] (-0.49, fdr 7e-05), [[STRADB]] (-0.48, fdr 1e-04), [[OSR2]] (-0.47, fdr 3e-05).
> It is in [[Module 129]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +13.2 | 4e-37 | 35/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.83×** | +10.8 | 2e-24 | 45/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +9.0 | 6e-17 | 37/45 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.8 | 2e-09 | 33/48 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +6.5 | 1e-08 | 33/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.7 | 1e-06 | 23/46 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 2e-05 | 25/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.1 | 3e-05 | 22/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +4.7 | 2e-04 | 23/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.4 | 7e-04 | 20/47 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.015 | 20/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.017 | 19/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +3.2 | 0.056 | 11/47 (PANC-1, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.23× | +3.0 | 0.10 | 12/48 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 0.121×, NCI-H2030 0.150×, NCI-H460 0.145×, SHP-77 0.223×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.110×, A498 0.267×, NCI-H23 0.239×, SNU-423 0.244×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.258×, NCI-H2347 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0868×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C32 0.0933×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.7 | 1e-08 | 26/42 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -6.2 | 1e-07 | 19/31 (A498, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.013 | 16/47 (HS-578T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.9 | 0.013 | 24/47 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.083 | 11/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.812× | -3.1 | 0.20 | 16/48 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.812× | -3.0 | 0.20 | 12/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.0 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +27.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +18.0) | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -9.2) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 21.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +26.0) | — |
| [[SW 900 (line)]] | alt | 24.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.0) | — |
| [[A549 (line)]] | wt | 20.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 45.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 42.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.421× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.9) | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0933× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +11.3) | — |
| [[J82 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 23.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.57× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0868× (z -14.6) |
| [[SW480 (line)]] | alt | 23.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.71× (z +8.5) | — |
| [[A-427 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF865]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C19orf47]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ZNF707]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FBXO46]] | +0.58 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[NACC1]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SNRNP70]] | +0.56 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ZNF212]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SBNO2]] | +0.55 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF316]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CSK]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBX]] | -0.49 | -0.50 / -0.37 | both halves | 7e-05 | STRING 429 |
| [[STRADB]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[OSR2]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[LSMEM1]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[UQCRC2]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MLF1]] | -0.45 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[DESI2]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[PCGF5]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.6, -4.8); signed map (-13.6, -24.3). **Vector** length 76.1, 14.1% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +10.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +13.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type and G-patch domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,707,465-63,736,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ583P15.3, MGC44880, FLJ14972, ZC3HDC9, ZC3H9, GPATC6, GPATCH6, ZIP; previously KIAA1847 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; G-patch domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5A5](https://www.uniprot.org/uniprotkb/Q8N5A5) (Zinc finger CCCH-type with G patch domain-containing protein):

> Transcription repressor that specifically binds the 5'-GGAG[GA]A[GA]A-3' consensus sequence. Represses transcription by recruiting the chromatin multiprotein complex NuRD to target promoters. Negatively regulates expression of EGFR, a gene involved in cell proliferation, survival and migration. Its ability to repress genes of the EGFR pathway suggest it may act as a tumor suppressor. Able to suppress breast carcinogenesis.; [Isoform 4]: Antagonizes the transcription repression by isoform 1 by …

**Summary**, from NCBI Gene [84619](https://www.ncbi.nlm.nih.gov/gene/84619):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in negative regulation of epidermal growth factor-activated receptor activity and negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15948) · Entrez [84619](https://www.ncbi.nlm.nih.gov/gene/84619) · UniProt [Q8N5A5](https://www.uniprot.org/uniprotkb/Q8N5A5) · Ensembl [ENSG00000197114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197114)

## Data

Gene col 12344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12344); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12344]; `tensor/DDL_lfc|DDL_z.npy` [12344]; `embed/gene_vectors.npy` [12344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12344 or target_col == 12344). Every well: [[ZGPAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZGPAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
