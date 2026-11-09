---
symbol: "VAMP3"
type: "gene"
col: 547
ensembl_id: "ENSG00000049245"
name: "vesicle associated membrane protein 3"
location: "1p36.23"
module: 25
arm: "+"
pooled_cpm: 41.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# VAMP3

*vesicle associated membrane protein 3* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.47× (z +17.8, q 0e+00, up in 35 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.60× (z +9.6, q 8e-20, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.711× (z -9.9, q 2e-20, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2M1]] (+0.76, fdr 7e-06), [[MMGT1]] (+0.73, fdr 7e-06), [[PEX19]] (+0.69, fdr 7e-06); moves opposite to [[FOXA2]] (-0.69, fdr 1e-05), [[ZNF503]] (-0.63, fdr 1e-05), [[SNHG8]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +17.8 | 0e+00 | 35/40 (A549, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +17.4 | 0e+00 | 40/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +11.9 | 2e-30 | 34/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +9.6 | 8e-20 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +9.0 | 2e-17 | 38/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +6.7 | 2e-09 | 33/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +6.3 | 3e-08 | 27/48 (SW480, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +6.1 | 6e-08 | 30/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +5.9 | 2e-07 | 22/47 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.31×** | +5.5 | 2e-06 | 28/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 1e-05 | 23/45 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.0 | 3e-05 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.3 | 6e-04 | 0/48 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.003 | 16/34 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 17/47 (COLO 205, A-172, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.005 | 12/48 (A-172, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.032 | 17/48 (HS-578T, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.053 | 10/47 (SK-MEL-2, HOP62, …) | two highest doses | low cells (technical?); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.087 | 8/46 (A549, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.092 | 12/48 (PANC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -9.9 | 2e-20 | 32/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -9.7 | 7e-20 | 40/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.673×** | -7.3 | 6e-11 | 39/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.824×** | -4.0 | 0.009 | 14/48 (SW480, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.015 | 22/48 (NCI-H23, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.022 | 21/47 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pralsetinib (drug)]] 0.05 µM |  | 0.846× | -3.3 | 0.089 | 12/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.854× | -3.2 | 0.12 | 15/48 (J82, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 37.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 51.8 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.8) ⚠ cell-cycle shift, explains ~13% of this change | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -8.6) |
| [[SNU-423 (line)]] | alt | 49.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 29.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +12.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 51.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.4) |
| [[Hs 766T (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 36.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -8.7) |
| [[LS 180 (line)]] | wt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 50.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.48× (z +11.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.291× (z -11.5) |
| [[SW480 (line)]] | alt | 31.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.24× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.93× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 59.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2M1]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 608 |
| [[MMGT1]] | +0.73 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[PEX19]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TGOLN2]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 841 |
| [[MOB1A]] | +0.67 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DLST]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NAGA]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[AIDA]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[NRAS]] | +0.64 | +0.56 / +0.76 | both halves | 1e-05 | STRING 445 |
| [[ZDHHC16]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXA2]] | -0.69 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[PIM3]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IWS1]] | -0.57 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[PPIG]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[COX5A]] ⚠ | -0.55 | -0.53 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.55 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.54 | -0.37 / -0.56 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SUMO4]] | -0.54 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[SMIM26]] ⚠ | -0.54 | -0.49 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.2, -21.7); signed map (-18.2, -36.8). **Vector** length 102, 24.0% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +11.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +9.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.6 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.4 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | vesicle associated membrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:7,771,296-7,781,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEB |
| Gene groups (HGNC) | Vesicle associated membrane proteins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 26 pathways, smallest: RHOH GTPase cycle; RHOF GTPase cycle; Retrograde transport at the Trans-Golgi-Network |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15836](https://www.uniprot.org/uniprotkb/Q15836) (Vesicle-associated membrane protein 3):

> SNARE involved in vesicular transport from the late endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [9341](https://www.ncbi.nlm.nih.gov/gene/9341):

> Synaptobrevins/VAMPs, syntaxins, and the 25-kD synaptosomal-associated protein are the main components of a protein complex involved in the docking and/or fusion of synaptic vesicles with the presynaptic membrane. This gene is a member of the vesicle-associated membrane protein (VAMP)/synaptobrevin family. Because of its high homology to other known VAMPs, its broad tissue distribution, and its subcellular localization, the protein encoded by this gene was shown to be the human equivalent of …

**Accessions** — [HGNC:12644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12644) · Entrez [9341](https://www.ncbi.nlm.nih.gov/gene/9341) · UniProt [Q15836](https://www.uniprot.org/uniprotkb/Q15836) · Ensembl [ENSG00000049245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049245)

## Data

Gene col 547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 547); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 547]; `tensor/DDL_lfc|DDL_z.npy` [547]; `embed/gene_vectors.npy` [547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 547 or target_col == 547). Every well: [[VAMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
