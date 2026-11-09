---
symbol: "PARG"
type: "gene"
col: 13583
ensembl_id: "ENSG00000227345"
name: "poly(ADP-ribose) glycohydrolase"
location: "10q11.23"
module: 5
arm: "+"
pooled_cpm: 47.81
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PARG

*poly(ADP-ribose) glycohydrolase* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +15.0, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.748× (z -7.9, q 2e-12, down in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.830× (z -7.1, q 2e-10, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (hTERT-HPNE 0.0814×, RKO 0.253×, SK-MEL-2 0.275×, SW48 0.174×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.462×, LS 180 0.385×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.562×, HT-29 0.428×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARS2]] (+0.67, fdr 7e-06), [[CPSF3]] (+0.66, fdr 1e-05), [[MAPKAP1]] (+0.64, fdr 1e-05); moves opposite to [[HDAC5]] (-0.61, fdr 1e-05), [[SHF]] (-0.55, fdr 2e-05), [[SH3GL2]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +15.0 | 0e+00 | 38/48 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.71×** | +14.5 | 1e-45 | 44/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +13.6 | 9e-40 | 39/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +12.9 | 7e-36 | 41/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.58×** | +12.3 | 8e-33 | 40/48 (A498, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +12.2 | 2e-32 | 38/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +10.4 | 2e-23 | 29/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +10.2 | 2e-22 | 33/49 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +9.4 | 5e-19 | 33/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +9.2 | 2e-18 | 31/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +8.5 | 1e-15 | 34/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.2 | 1e-14 | 35/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +8.2 | 1e-14 | 26/48 (NCI-H460, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +8.0 | 3e-14 | 21/48 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +7.6 | 1e-12 | 28/48 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.3 | 8e-12 | 26/48 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 1e-05 | 22/48 (LoVo, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.8 | 5e-05 | 16/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +4.4 | 2e-04 | 14/48 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.7 | 0.004 | 14/47 (LoVo, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (hTERT-HPNE 0.0814×, RKO 0.253×, SK-MEL-2 0.275×, SW48 0.174×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 0.462×, LS 180 0.385×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.562×, HT-29 0.428×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -7.9 | 2e-12 | 27/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -7.3 | 9e-11 | 0/49 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -7.1 | 2e-10 | 25/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.818×** | -5.4 | 7e-06 | 18/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.819×** | -5.4 | 7e-06 | 23/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.3 | 0.001 | 20/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.851× | -4.2 | 0.002 | 20/47 (COLO 205, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.16 | 7/48 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.808× | -3.0 | 0.16 | 12/48 (SW1417, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 76.6 | 6 (1 ⚠) | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.557× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.562× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 55.7 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.462× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 32.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 43.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.133× (z -10.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.428× (z -8.5) |
| [[LS 180 (line)]] | wt | 50.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.385× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 57.1 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 50.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 48.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.5) | — |
| [[RKO (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARS2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CPSF3]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MAPKAP1]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[TIMM21]] | +0.62 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[TACO1]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[NUP205]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RPTOR]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.58 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[UCHL5]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[UTP15]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NSD1]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SHF]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[SH3GL2]] | -0.53 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[SYP]] | -0.53 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[OAZ1]] | -0.52 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ASMTL]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SNN]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TP53INP2]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PLPPR2]] | -0.51 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PHF1]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CDKN1C]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ITGA7]] | -0.49 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PARG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.9, -33.5); signed map (-5.9, -39.7). **Vector** length 87.6, 19.1% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +10.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +8.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -7.4 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.6 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) glycohydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:49,818,279-49,970,203 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: POLB-Dependent Long Patch Base Excision Repair; Resolution of AP sites via the multiple-nucleotide patch replacement pathway; Resolution of Abasic Sites (AP sites) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W56](https://www.uniprot.org/uniprotkb/Q86W56) (Poly(ADP-ribose) glycohydrolase):

> Poly(ADP-ribose) glycohydrolase that degrades poly(ADP-ribose) by hydrolyzing the ribose-ribose bonds present in poly(ADP-ribose). Mainly acts as an exo-glycohydrolase but can act as an endo-glycohydrolase at low efficiency, releasing poly(ADP-ribose) of different length as well as ADP-ribose monomers. It is however unable to cleave the ester bond between the terminal ADP-ribose and ADP-ribosylated residues, leaving proteins that are mono-ADP-ribosylated. Poly(ADP-ribose) synthesized after DNA …

**Summary**, from NCBI Gene [8505](https://www.ncbi.nlm.nih.gov/gene/8505):

> Poly(ADP-ribose) glycohydrolase (PARG) is the major enzyme responsible for the catabolism of poly(ADP-ribose), a reversible covalent-modifier of chromosomal proteins. The protein is found in many tissues and may be subject to proteolysis generating smaller, active products. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:8605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8605) · Entrez [8505](https://www.ncbi.nlm.nih.gov/gene/8505) · UniProt [Q86W56](https://www.uniprot.org/uniprotkb/Q86W56) · Ensembl [ENSG00000227345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227345)

## Data

Gene col 13583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13583); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13583]; `tensor/DDL_lfc|DDL_z.npy` [13583]; `embed/gene_vectors.npy` [13583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13583 or target_col == 13583). Every well: [[PARG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
