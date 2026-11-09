---
symbol: "BLOC1S5"
type: "gene"
col: 12012
ensembl_id: "ENSG00000188428"
name: "biogenesis of lysosomal organelles complex 1 subunit 5"
location: "6p24.3"
module: 17
arm: "+"
pooled_cpm: 24.38
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# BLOC1S5

*biogenesis of lysosomal organelles complex 1 subunit 5* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.28× (z +5.8, q 5e-06, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -20.1, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZYG11B]] (+0.61, fdr 3e-05), [[ABITRAM]] (+0.59, fdr 1e-05), [[ZBTB41]] (+0.59, fdr 1e-05); moves opposite to [[SLC6A16]] (-0.53, fdr 3e-05), [[PSPC1]] (-0.53, fdr 3e-05), [[TP53I11]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 5e-06 | 19/47 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +5.4 | 2e-05 | 18/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 0.001 | 16/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +4.2 | 0.005 | 14/48 (LS 180, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.1 | 0.005 | 14/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.008 | 9/48 (KATO III, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -20.1 | 0e+00 | 36/47 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.501×** | -16.9 | 0e+00 | 38/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -15.5 | 0e+00 | 36/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.321×** | -14.5 | 1e-45 | 41/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -12.0 | 4e-31 | 35/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -10.7 | 1e-24 | 28/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -10.4 | 2e-23 | 30/47 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.793×** | -5.4 | 4e-06 | 20/48 (LS 180, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.655×** | -5.4 | 4e-06 | 17/48 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.802×** | -5.4 | 5e-06 | 22/47 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.801×** | -5.2 | 1e-05 | 19/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.811×** | -5.1 | 2e-05 | 17/47 (SW 1271, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.823×** | -4.7 | 1e-04 | 15/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.819×** | -4.7 | 1e-04 | 18/47 (BT-474, HepG2/C3A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.831×** | -4.5 | 3e-04 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -4.1 | 0.002 | 15/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.003 | 5/46 (RPMI-7951, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -3.7 | 0.007 | 11/48 (KATO III, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.015 | 8/48 (J82, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.911× | -3.1 | 0.037 | 4/48 (HT-29, J82, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.037 | 11/47 (HCT15, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 32.5 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -11.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -11.7) |
| [[A-172 (line)]] | wt | 22.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.0) |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[KATO III (line)]] | alt | 31.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.8) |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -13.9) |
| [[A-427 (line)]] | wt | 22.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -15.2) |
| [[H4 (line)]] | wt | 24.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.6) |
| [[J82 (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -14.2) |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.154× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.2) |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -15.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.3) |
| [[A549 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -8.8) |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 17.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.191× (z -9.5) |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~70% of this change |
| [[HS-578T (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.9) |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[RKO (line)]] | wt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.3) |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.6) |
| [[SW 1271 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0808× (z -8.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.499× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZYG11B]] | +0.61 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[ABITRAM]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB41]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZCCHC9]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[BLOC1S5-TXNDC5]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAD17]] | +0.56 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PWP1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CMAS]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.55 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[ARMC1]] | +0.55 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[MRPL2]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DBT]] | +0.55 | +0.33 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A16]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PSPC1]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TP53I11]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[B4GAT1-DT]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SMAD6]] | -0.47 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD10]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[ARGLU1]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[STARD4-AS1]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SRSF5]] | -0.45 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.7, -1.2); signed map (-19.6, -13.2). **Vector** length 67.6, 10.9% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.3 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.5 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +5.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | -4.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -20.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -15.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of lysosomal organelles complex 1 subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:8,013,567-8,064,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MU, dJ303A1.3; previously MUTED |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDH9](https://www.uniprot.org/uniprotkb/Q8TDH9) (Biogenesis of lysosome-related organelles complex 1 subunit 5):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. Plays a role in intracellular …

**Summary**, from NCBI Gene [63915](https://www.ncbi.nlm.nih.gov/gene/63915):

> This gene encodes a component of BLOC-1 (biogenesis of lysosome-related organelles complex 1). Components of this complex are involved in the biogenesis of organelles such as melanosomes and platelet-dense granules. A mouse model for Hermansky-Pudlak Syndrome is mutated in the murine version of this gene. Alternative splicing results in multiple transcript variants. Read-through transcription exists between this gene and the upstream EEF1E1 (eukaryotic translation elongation factor 1 epsilon 1) …

**Accessions** — [HGNC:18561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18561) · Entrez [63915](https://www.ncbi.nlm.nih.gov/gene/63915) · UniProt [Q8TDH9](https://www.uniprot.org/uniprotkb/Q8TDH9) · Ensembl [ENSG00000188428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188428)

## Data

Gene col 12012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12012); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12012]; `tensor/DDL_lfc|DDL_z.npy` [12012]; `embed/gene_vectors.npy` [12012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12012 or target_col == 12012). Every well: [[BLOC1S5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
