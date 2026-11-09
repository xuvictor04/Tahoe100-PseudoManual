---
symbol: "SBNO2"
type: "gene"
col: 762
ensembl_id: "ENSG00000064932"
name: "strawberry notch homolog 2"
location: "19p13.3"
module: 14
arm: "+"
pooled_cpm: 53.91
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SBNO2

*strawberry notch homolog 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +14.1, q 1e-42, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.644× (z -9.3, q 6e-18, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOCS3]] (+0.73, fdr 7e-06), [[ZC3H12A]] (+0.65, fdr 7e-06), [[TNKS1BP1]] (+0.64, fdr 7e-06); moves opposite to [[PPHLN1]] (-0.48, fdr 4e-05), [[VDAC3]] (-0.48, fdr 4e-05), [[TMED4]] (-0.47, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZC3H12A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +14.1 | 1e-42 | 37/47 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +7.5 | 1e-11 | 31/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +6.2 | 9e-08 | 33/49 (A-172, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 3e-06 | 27/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.005 | 25/47 (A-172, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.026 | 22/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.039 | 23/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.0 | 0.18 | 20/48 (SW480, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -9.3 | 6e-18 | 37/49 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.579×** | -7.9 | 1e-12 | 28/38 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -6.9 | 1e-09 | 33/47 (MIA PaCa-2, SW 1271, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.652×** | -6.4 | 2e-08 | 37/48 (PANC-1, SW1417, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.658×** | -6.3 | 4e-08 | 33/48 (NCI-H23, SW480, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.674×** | -5.7 | 1e-06 | 30/49 (MIA PaCa-2, SW 1271, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -5.7 | 1e-06 | 2/49 (SW 1271, SW 1088) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.706×** | -5.2 | 1e-05 | 29/48 (HT-29, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.703×** | -5.1 | 2e-05 | 27/47 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -4.6 | 2e-04 | 23/48 (J82, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.735×** | -4.6 | 2e-04 | 31/49 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.758×** | -4.1 | 0.002 | 28/48 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.594×** | -4.1 | 0.002 | 25/47 (CFPAC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -3.8 | 0.007 | 21/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.839× | -3.7 | 0.008 | 19/49 (COLO 205, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.843× | -3.6 | 0.011 | 21/49 (HT-29, NCI-H1792, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.052 | 17/48 (LoVo, SW1417, …) | rises with dose | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **0.669×** | -3.1 | 0.052 | 22/48 (NCI-H1573, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.811×** | -3.0 | 0.094 | 13/47 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.822×** | -2.9 | 0.099 | 17/48 (J82, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.7 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +18.3) | — |
| [[A-172 (line)]] | wt | 83.8 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 79.0 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.4) |
| [[A498 (line)]] | wt | 67.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 89.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.1) |
| [[HS-578T (line)]] | alt | 54.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +20.9) | — |
| [[Panc 03.27 (line)]] | alt | 137 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.1) |
| [[BT-474 (line)]] | alt | 54.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 45.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 39.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 64.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.6) |
| [[PANC-1 (line)]] | alt | 57.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.404× (z -9.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 42.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +15.7) | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.0) |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.0) |
| [[SW480 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 56.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 83.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.3) |
| [[H4 (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0808× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 67.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 62.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.9) | — |
| [[J82 (line)]] | alt | 62.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.24× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 62.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS3]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 | STRING 469 |
| [[ZC3H12A]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TNKS1BP1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TICAM1]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BCL3]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 | STRING 660 |
| [[BCL9L]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[COQ8B]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[IL4R]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MOB3C]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SYNPO]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CSRNP1]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPHLN1]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[VDAC3]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TMED4]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MFN1]] | -0.47 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[LNPK]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[HMBOX1]] | -0.46 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[NBAS]] | -0.45 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[MIGA1]] | -0.45 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[GOLT1B]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12A]] | B | ZC3H12A activity raises SBNO2's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CSRNP1]] | C | CSRNP1's natural level strengthens SBNO2's drug response | CSRNP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.21; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 7.3); signed map (8.2, 32.9). **Vector** length 103, 27.1% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.8 | -5.7 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | strawberry notch homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,107,637-1,174,268 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00173, Stno, Sno; previously KIAA0963 |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G9](https://www.uniprot.org/uniprotkb/Q9Y2G9) (Protein strawberry notch homolog 2):

> Acts as a transcriptional coregulator, that can have both coactivator and corepressor functions. Inhibits the DCSTAMP-repressive activity of TAL1, hence enhancing the access of the transcription factor MITF to the DC-STAMP promoter in osteoclast. Plays a role in bone homeostasis; required as a positive regulator in TNFSF11//RANKL-mediated osteoclast fusion via a DCSTAMP-dependent pathway. May also be required in the regulation of osteoblast differentiation (By similarity). Involved in the …

**Summary**, from NCBI Gene [22904](https://www.ncbi.nlm.nih.gov/gene/22904):

> Predicted to enable chromatin DNA binding activity and histone binding activity. Involved in several processes, including cellular response to interleukin-6; macrophage activation involved in immune response; and negative regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29158) · Entrez [22904](https://www.ncbi.nlm.nih.gov/gene/22904) · UniProt [Q9Y2G9](https://www.uniprot.org/uniprotkb/Q9Y2G9) · Ensembl [ENSG00000064932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064932)

## Data

Gene col 762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 762); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 762]; `tensor/DDL_lfc|DDL_z.npy` [762]; `embed/gene_vectors.npy` [762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 762 or target_col == 762). Every well: [[SBNO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBNO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
