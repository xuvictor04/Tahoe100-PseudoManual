---
symbol: "CHTOP"
type: "gene"
col: 8365
ensembl_id: "ENSG00000160679"
name: "chromatin target of PRMT1"
location: "1q21.3"
module: 16
arm: "+"
pooled_cpm: 32.61
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CHTOP

*chromatin target of PRMT1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +22.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.739× (z -9.1, q 7e-17, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRCAP]] (+0.79, fdr 7e-06), [[ZNF776]] (+0.76, fdr 7e-06), [[PIGO]] (+0.72, fdr 7e-06); moves opposite to [[RAB6A]] (-0.73, fdr 7e-06), [[SRP54-AS1]] (-0.68, fdr 7e-06), [[PIK3C2A]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +22.1 | 0e+00 | 43/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +19.3 | 0e+00 | 47/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +18.3 | 0e+00 | 44/47 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.41×** | +17.8 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.43×** | +16.4 | 0e+00 | 44/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +14.8 | 0e+00 | 42/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +14.2 | 8e-44 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +12.6 | 3e-34 | 41/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.99×** | +12.1 | 1e-31 | 37/47 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.5 | 2e-19 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.5 | 4e-09 | 0/48 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +5.6 | 1e-06 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.0 | 3e-05 | 18/46 (RKO, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.9 | 4e-05 | 21/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.7 | 1e-04 | 21/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 2e-04 | 15/47 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.4 | 0.022 | 13/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.046 | 8/47 (RKO, NCI-H2030, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.056 | 6/48 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -9.1 | 7e-17 | 31/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -7.9 | 7e-13 | 33/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -6.2 | 1e-07 | 26/47 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.762×** | -5.8 | 1e-06 | 25/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.782×** | -5.2 | 2e-05 | 26/47 (SW48, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -5.1 | 4e-05 | 23/48 (LS 180, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.796×** | -4.8 | 1e-04 | 20/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.007 | 15/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.834× | -3.9 | 0.007 | 19/48 (A498, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.882× | -3.8 | 0.008 | 11/48 (RKO, A549, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | 0.840× | -3.6 | 0.018 | 11/48 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.890× | -3.5 | 0.019 | 13/48 (A498, HCT15, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.891× | -3.5 | 0.020 | 6/48 (A-427, HEC-1-A, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.857× | -3.3 | 0.039 | 15/46 (HT-29, RKO, …) | two highest doses | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 0.857× | -3.2 | 0.057 | 11/47 (BT-474, HEC-1-A, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.095 | 12/48 (A-427, SW 1271, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.5 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +17.8) | — |
| [[NCI-H1573 (line)]] | alt | 37.9 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +12.9) | — |
| [[RKO (line)]] | wt | 44.4 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.4) |
| [[LS 180 (line)]] | wt | 33.6 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 34.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +18.7) | — |
| [[A-427 (line)]] | wt | 38.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A498 (line)]] | wt | 25.0 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.6) |
| [[A-172 (line)]] | wt | 30.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +14.5) | — |
| [[A549 (line)]] | wt | 28.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[LOX-IMVI (line)]] | wt | 26.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 26.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[HS-578T (line)]] | alt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 34.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[NCI-H23 (line)]] | alt | 76.9 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.55× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.3) |
| [[SW480 (line)]] | alt | 37.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.33× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[HEC-1-A (line)]] | alt | 31.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.1) |
| [[HOP62 (line)]] | alt | 25.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[KATO III (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 38.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.420× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 27.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.22× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 35.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.2) | — |
| [[SW48 (line)]] | wt | 41.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -10.5) |
| [[BT-474 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0907× (z -9.5) |
| [[COLO 205 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.00× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 47.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 40.5 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.91× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRCAP]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PIGO]] | +0.72 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[PUF60]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CSTF2T]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF268]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SRRM2]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RTL6]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EIF2B5]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SRSF6]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 544 |
| [[PRRC2A]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ZNF502]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.68 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ECI2]] | -0.66 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[DPM1]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.66 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[SGTB]] | -0.66 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.65 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[APAF1]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[GRB2]] | -0.65 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CHTOP's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CHTOP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.6, -2.3); signed map (1.5, -32.2). **Vector** length 88.1, 20.3% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +22.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +12.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | +0.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chromatin target of PRMT1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,633,982-153,646,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP547E1010, SRAG, FOP; previously C1orf77 |
| Gene groups (HGNC) | Transcription and export complex 1 subunits |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3Y2](https://www.uniprot.org/uniprotkb/Q9Y3Y2) (Chromatin target of PRMT1 protein):

> Plays an important role in the ligand-dependent activation of estrogen receptor target genes. May play a role in the silencing of fetal globin genes. Recruits the 5FMC complex to ZNF148, leading to desumoylation of ZNF148 and subsequent transactivation of ZNF148 target genes (By similarity). Plays an important role in the tumorigenicity of glioblastoma cells. Binds to 5-hydroxymethylcytosine (5hmC) and associates with the methylosome complex containing PRMT1, PRMT5, MEP50 and ERH. The …

**Summary**, from NCBI Gene [26097](https://www.ncbi.nlm.nih.gov/gene/26097):

> This gene encodes a small nuclear protein that is characterized by an arginine and glycine rich region. This protein may have an important role in the regulation of fetal globin gene expression and in the activation of estrogen-responsive genes. A recent study reported that this protein binds 5-hydroxymethylcytosine (5hmC) and associates with an arginine methyltransferase complex (methylosome), which promotes methylation of arginine 3 of histone H4 (H4R3) and activation of genes involved in …

**Accessions** — [HGNC:24511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24511) · Entrez [26097](https://www.ncbi.nlm.nih.gov/gene/26097) · UniProt [Q9Y3Y2](https://www.uniprot.org/uniprotkb/Q9Y3Y2) · Ensembl [ENSG00000160679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160679)

## Data

Gene col 8365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8365); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8365]; `tensor/DDL_lfc|DDL_z.npy` [8365]; `embed/gene_vectors.npy` [8365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8365 or target_col == 8365). Every well: [[CHTOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHTOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
