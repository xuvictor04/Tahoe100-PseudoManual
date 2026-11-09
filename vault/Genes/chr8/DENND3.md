---
symbol: "DENND3"
type: "gene"
col: 2585
ensembl_id: "ENSG00000105339"
name: "DENN domain containing 3"
location: "8q24.3"
module: 97
arm: "+"
pooled_cpm: 39.15
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# DENND3

*DENN domain containing 3* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +10.5, q 4e-23, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.549× (z -11.0, q 3e-25, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13]] (+0.66, fdr 1e-05), [[ESYT2]] (+0.64, fdr 7e-06), [[ERGIC1]] (+0.62, fdr 2e-05); moves opposite to [[YARS2]] (-0.58, fdr 1e-04), [[ARSB]] (-0.55, fdr 4e-04), [[LYPLAL1-AS1]] (-0.55, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PDLIM1]] → it (grade B ⚠); 10 go from it, the strongest it → [[AKAP13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +10.5 | 4e-23 | 31/41 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +9.5 | 8e-19 | 29/41 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +8.1 | 1e-13 | 28/41 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.007 | 18/41 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.013 | 17/41 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.013 | 14/41 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +3.8 | 0.013 | 15/41 (A549, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.013 | 17/41 (HOP62, BT-474, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.018 | 20/41 (HOP62, HS-578T, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +3.5 | 0.026 | 13/41 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.032 | 17/41 (HOP62, RPMI-7951, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -11.0 | 3e-25 | 31/40 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.520×** | -8.5 | 6e-15 | 32/41 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -7.2 | 1e-10 | 30/40 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -6.8 | 2e-09 | 27/35 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.698×** | -6.6 | 5e-09 | 24/41 (NCI-H460, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.394×** | -6.3 | 3e-08 | 32/39 (RPMI-7951, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.620×** | -6.2 | 5e-08 | 26/41 (LS 180, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.624×** | -6.1 | 7e-08 | 24/37 (HCT15, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.726×** | -5.9 | 3e-07 | 29/41 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.617×** | -5.8 | 4e-07 | 24/35 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -5.7 | 7e-07 | 25/41 (SW48, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **0.735×** | -5.6 | 7e-07 | 28/41 (HCT15, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.435×** | -5.6 | 7e-07 | 28/40 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.470×** | -5.1 | 1e-05 | 26/40 (NCI-H460, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -4.9 | 3e-05 | 20/40 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.494×** | -4.8 | 6e-05 | 25/36 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -4.6 | 1e-04 | 20/40 (SW48, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.532×** | -4.3 | 5e-04 | 18/37 (A-172, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.543×** | -4.1 | 9e-04 | 18/39 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.009 | 21/40 (NCI-H460, LOX-IMVI, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.3 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.1) |
| [[HOP62 (line)]] | alt | 39.8 | 10 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.30× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.224× (z -10.7) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -10.9) |
| [[PANC-1 (line)]] | alt | 31.5 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +25.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 57.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -17.0) |
| [[SW 900 (line)]] | alt | 92.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.3) |
| [[SW48 (line)]] | wt | 54.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -16.2) |
| [[SW480 (line)]] | alt | 19.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.84× (z +13.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 83.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.0) |
| [[A-172 (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 65.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 59.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.7) |
| [[A549 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -8.7) |
| [[Hs 766T (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -9.9) ⚠ cell-cycle shift, explains ~12% of this change |
| [[LOX-IMVI (line)]] | wt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 74.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.46× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.3) |
| [[A-427 (line)]] | wt | 8.65 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.90 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ESYT2]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ERGIC1]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[KIF13B]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[FOXO1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[VSIR]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[FADS3]] | +0.56 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[KIAA0513]] | +0.55 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[TRIP10]] | +0.55 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[MT1X]] | +0.55 | +0.43 / +0.36 | both halves | 9e-05 |  |
| [[AGFG2]] | +0.55 | +0.32 / +0.38 | both halves | 2e-04 |  |
| [[PACSIN2]] | +0.54 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.58 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ARSB]] | -0.55 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[LYPLAL1-AS1]] | -0.55 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[PRDM5]] | -0.54 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ANKAR]] | -0.54 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[HCG18]] | -0.54 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[PRKACB]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.51 | -0.37 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[CCNJ]] | -0.51 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[CSTF3]] | -0.50 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[TOX]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[ZNF804A]] | -0.50 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[LINC01134]] | -0.49 | -0.36 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDLIM1]] | B | PDLIM1 activity raises DENND3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without PDLIM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[VSIR]] | B | VSIR activity raises DENND3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without VSIR | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[ANXA10]] | B | ANXA10 activity raises DENND3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without ANXA10 | 0.014 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[TBC1D8]] | B | TBC1D8 activity raises DENND3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without TBC1D8 | 0.014 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DENND3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TSC22D3]] | B | TSC22D3 activity raises DENND3's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TSC22D3 | 0.049 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers DENND3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers DENND3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DUSP1]] | C | DUSP1 activity raises DENND3's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 3.04× lower at baseline in the lines without DUSP1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP13]] | B | DENND3 activity raises AKAP13's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without DENND3 | 0.011 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[ALG8]] | B | DENND3 activity lowers ALG8's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.74× higher at baseline in the lines without DENND3 | 0.020 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[B4GALT1]] | B | DENND3 activity raises B4GALT1's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without DENND3 | 0.032 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[AKAP13]] | B | DENND3 activity strengthens AKAP13's drug response | lines that do not express DENND3 (7) vs lines expressing it (42) | the lines without DENND3 respond 0.85× as strongly (z diff +1.11); strongest at Dinaciclib 0.5 µM: 0.72x vs 0.42x (z diff +5.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PDLIM1]] | B | DENND3 activity raises PDLIM1's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 3.16× lower at baseline in the lines without DENND3 | 0.043 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[TSC22D3]] | B | DENND3 activity raises TSC22D3's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without DENND3 | 0.058 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[ENTPD6]] | B | DENND3 activity lowers ENTPD6's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.08× higher at baseline in the lines without DENND3 | 0.079 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[TBC1D8]] | B | DENND3 activity raises TBC1D8's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 2.31× lower at baseline in the lines without DENND3 | 0.090 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[YARS2]] | B | DENND3 activity lowers YARS2's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without DENND3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[DUSP1]] | C | DENND3 activity raises DUSP1's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 3.24× lower at baseline in the lines without DENND3 | 0.039 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 11.5); signed map (12.4, 32.7). **Vector** length 117, 32.4% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.4 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +8.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.6 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:141,117,278-141,195,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0870 |
| Gene groups (HGNC) | WD repeat domain containing; DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RUS2](https://www.uniprot.org/uniprotkb/A2RUS2) (DENN domain-containing protein 3):

> Guanine nucleotide exchange factor (GEF) activating RAB12. Promotes the exchange of GDP to GTP, converting inactive GDP-bound RAB12 into its active GTP-bound form. Regulates autophagy in response to starvation through RAB12 activation. Starvation leads to ULK1/2-dependent phosphorylation of Ser-472 and Ser-490, which in turn allows recruitment of 14-3-3 adapter proteins and leads to up-regulation of GEF activity towards RAB12 (By similarity). Also plays a role in protein transport from …

**Summary**, from NCBI Gene [22898](https://www.ncbi.nlm.nih.gov/gene/22898):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in endosome to lysosome transport; protein catabolic process; and regulation of Rab protein signal transduction. Predicted to be located in cytosol. Predicted to be active in cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29134) · Entrez [22898](https://www.ncbi.nlm.nih.gov/gene/22898) · UniProt [A2RUS2](https://www.uniprot.org/uniprotkb/A2RUS2) · Ensembl [ENSG00000105339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105339)

## Data

Gene col 2585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2585); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2585]; `tensor/DDL_lfc|DDL_z.npy` [2585]; `embed/gene_vectors.npy` [2585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2585 or target_col == 2585). Every well: [[DENND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
