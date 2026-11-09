---
symbol: "EIF2B3"
type: "gene"
col: 967
ensembl_id: "ENSG00000070785"
name: "eukaryotic translation initiation factor 2B subunit gamma"
location: "1p34.1"
module: 1
arm: "+"
pooled_cpm: 35.47
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 6
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EIF2B3

*eukaryotic translation initiation factor 2B subunit gamma* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.71× (z +32.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.654× (z -7.6, q 2e-11, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGK]] (+0.78, fdr 7e-06), [[RIOK1]] (+0.77, fdr 7e-06), [[TSEN2]] (+0.74, fdr 7e-06); moves opposite to [[YPEL5]] (-0.72, fdr 7e-06), [[FAM117A]] (-0.68, fdr 3e-05), [[CCNG2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SATB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.71×** | +32.1 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.68×** | +28.4 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.38×** | +27.2 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.90×** | +11.4 | 9e-28 | 42/46 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +10.7 | 2e-24 | 41/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.79×** | +10.3 | 5e-23 | 29/40 (SW 900, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +9.5 | 2e-19 | 36/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.8 | 9e-17 | 30/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.7 | 7e-13 | 32/48 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.51×** | +7.5 | 3e-12 | 38/48 (PANC-1, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +7.5 | 3e-12 | 33/48 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +7.1 | 7e-11 | 35/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.1 | 8e-11 | 26/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.44×** | +6.7 | 6e-10 | 28/46 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +6.3 | 1e-08 | 26/48 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.85×** | +5.9 | 1e-07 | 30/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +5.2 | 6e-06 | 17/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +5.2 | 7e-06 | 23/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.6 | 1e-04 | 17/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 1e-04 | 19/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -7.6 | 2e-11 | 26/48 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.6 | 1e-08 | 26/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.801×** | -4.0 | 0.014 | 15/48 (hTERT-HPNE, PANC-1, …) | rises with dose | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.817×** | -3.7 | 0.025 | 16/47 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.025 | 20/48 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.076 | 21/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.838× | -3.3 | 0.085 | 16/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.891× | -3.0 | 0.18 | 14/48 (LS 180, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 64.7 | 3 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +17.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -19.7) |
| [[HT-29 (line)]] | alt | 21.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +12.8) | — |
| [[RKO (line)]] | wt | 49.4 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -10.9) |
| [[SW480 (line)]] | alt | 39.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +20.8) | — |
| [[A-427 (line)]] | wt | 51.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.68× (z +12.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -15.8) |
| [[C-33 A (line)]] | alt | 50.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[C32 (line)]] | wt | 44.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.15× (z +11.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 24.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.00× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.63× (z +17.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 32.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.25× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.358× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.86× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 22.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 51.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.85× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.0) |
| [[SNU-423 (line)]] | alt | 18.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.09× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 18.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 25.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.306× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 39.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.94× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[A-172 (line)]] | wt | 25.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.02× (z +15.0) | — |
| [[A498 (line)]] | wt | 38.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +13.3) | — |
| [[A549 (line)]] | wt | 20.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.83× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.8× (z +13.7) | — |
| [[H4 (line)]] | wt | 24.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.60× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 33.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.27× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 45.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +15.8) | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.5× (z +11.8) | — |
| [[J82 (line)]] | alt | 31.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.86× (z +13.6) | — |
| [[KATO III (line)]] | alt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +12.2) | — |
| [[LoVo (line)]] | wt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.63× (z +17.5) | — |
| [[LS 180 (line)]] | wt | 20.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 31.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.57× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.49× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.05× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 29.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.36× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 12.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 30.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.93× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.05× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.72× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 66.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 46.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.70× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0550× (z -14.1) |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGK]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[NOL10]] | +0.72 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[FARSB]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | STRING 547 |
| [[NAA15]] | +0.71 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[RBM28]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[MPHOSPH6]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[POLR3B]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[EEFSEC]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 | STRING 416 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.72 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[FAM117A]] | -0.68 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CCNG2]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[GNAS]] | -0.67 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[TSC22D4]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[CDK19]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[STX17-DT]] | -0.65 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[UPK2]] | -0.64 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[OSER1-DT]] | -0.64 | -0.29 / -0.63 | both halves | 2e-04 |  |
| [[TMEM59]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[CD27-AS1]] | -0.62 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[HBP1]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1 activity lowers EIF2B3's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without SATB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[TOP2A]] | B | TOP2A activity raises EIF2B3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity lowers EIF2B3's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without ATXN1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[FAM78B]] | B | FAM78B activity raises EIF2B3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without FAM78B | 0.094 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.1, -42.0); signed map (-7.1, -48.7). **Vector** length 107, 29.6% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +9.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +27.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -14.2 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.0 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2B subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,850,522-44,986,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2Bgamma, EIF-2B |
| Reactome | 4 pathways, smallest: Recycling of eIF2:GDP; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR50](https://www.uniprot.org/uniprotkb/Q9NR50) (Translation initiation factor eIF2B subunit gamma):

> Acts as a component of the translation initiation factor 2B (eIF2B) complex, which catalyzes the exchange of GDP for GTP on the eukaryotic initiation factor 2 (eIF2) complex gamma subunit. Its guanine nucleotide exchange factor activity is repressed when bound to eIF2 complex phosphorylated on the alpha subunit, thereby limiting the amount of methionyl-initiator methionine tRNA available to the ribosome and consequently global translation is repressed.

**Summary**, from NCBI Gene [8891](https://www.ncbi.nlm.nih.gov/gene/8891):

> The protein encoded by this gene is one of the subunits of initiation factor eIF2B, which catalyzes the exchange of eukaryotic initiation factor 2-bound GDP for GTP. It has also been found to function as a cofactor of hepatitis C virus internal ribosome entry site-mediated translation. Mutations in this gene have been associated with leukodystrophy with vanishing white matter. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:3259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3259) · Entrez [8891](https://www.ncbi.nlm.nih.gov/gene/8891) · UniProt [Q9NR50](https://www.uniprot.org/uniprotkb/Q9NR50) · Ensembl [ENSG00000070785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070785)

## Data

Gene col 967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 967); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 967]; `tensor/DDL_lfc|DDL_z.npy` [967]; `embed/gene_vectors.npy` [967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 967 or target_col == 967). Every well: [[EIF2B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
