---
symbol: "TNKS1BP1"
type: "gene"
col: 7342
ensembl_id: "ENSG00000149115"
name: "CCR4-NOT transcription complex subunit 12"
location: "11q12.1"
module: 14
arm: "+"
pooled_cpm: 49.49
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNKS1BP1

*CCR4-NOT transcription complex subunit 12* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +23.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.513× (z -11.9, q 4e-30, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFE3]] (+0.65, fdr 7e-06), [[SBNO2]] (+0.64, fdr 7e-06), [[C15orf39]] (+0.63, fdr 2e-05); moves opposite to [[FBXW11]] (-0.57, fdr 1e-05), [[PPHLN1]] (-0.56, fdr 1e-05), [[GLUD1P3]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SYNPO]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +23.3 | 0e+00 | 45/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +11.9 | 5e-30 | 41/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.7 | 9e-16 | 36/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +8.6 | 1e-15 | 33/49 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.5 | 5e-06 | 35/48 (Hs 766T, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.5 | 7e-04 | 28/48 (SW1417, LS 180, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.010 | 24/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.077 | 23/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.28× | +3.1 | 0.12 | 20/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.12 | 22/48 (CFPAC-1, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.513×** | -11.9 | 4e-30 | 39/48 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.563×** | -7.3 | 8e-11 | 44/48 (SW480, A-172, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.584×** | -6.8 | 2e-09 | 45/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.582×** | -6.6 | 6e-09 | 25/36 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.591×** | -5.9 | 5e-07 | 32/47 (NCI-H1792, H4, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -4.5 | 6e-04 | 30/48 (RKO, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.704×** | -4.5 | 6e-04 | 32/48 (SNU-1, AsPC-1, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -4.2 | 0.002 | 29/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.002 | 30/49 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.729×** | -4.0 | 0.003 | 29/48 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.706×** | -3.9 | 0.005 | 31/48 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.749×** | -3.7 | 0.010 | 26/48 (H4, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.05 µM |  | **0.745×** | -3.5 | 0.022 | 25/48 (COLO 205, SW1417, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.031 | 18/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.039 | 22/48 (A-172, C32, …) | top dose only | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.767×** | -3.1 | 0.055 | 24/47 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.063 | 17/48 (NCI-H2347, NCI-H1573, …) | rises with dose | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -3.0 | 0.066 | 17/48 (A549, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 51.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +24.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 107 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 27.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +21.5) | — |
| [[A-172 (line)]] | wt | 72.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 44.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +24.1) | — |
| [[J82 (line)]] | alt | 65.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 54.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 66.6 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.7) |
| [[PANC-1 (line)]] | alt | 32.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +25.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.2) |
| [[SNU-423 (line)]] | alt | 65.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -8.8) |
| [[A498 (line)]] | wt | 48.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +22.2) | — |
| [[H4 (line)]] | wt | 68.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -11.0) |
| [[HS-578T (line)]] | alt | 81.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 50.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +18.6) | — |
| [[CFPAC-1 (line)]] | alt | 67.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 24.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 55.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 36.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.0) |
| [[SW 900 (line)]] | alt | 49.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.2) | — |
| [[SW48 (line)]] | wt | 44.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.8) | — |
| [[SW480 (line)]] | alt | 39.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.6) |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0972× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 83.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +15.1) | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.6) |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.5) |
| [[Hs 766T (line)]] | wt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.2) |
| [[LoVo (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +19.0) | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.6) |
| [[SW 1271 (line)]] | alt | 86.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 60.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.1) | — |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SBNO2]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[C15orf39]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RELA]] | +0.63 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PRR14]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MBD6]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SYNPO]] | +0.62 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SOCS3]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZC3H12A]] | +0.61 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[BCL9L]] | +0.61 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DEDD]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW11]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PPHLN1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GLUD1P3]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[COP1]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[HACD3]] | -0.50 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MCM9]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NFATC3]] | -0.49 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[NAP1L4]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ORC2]] | -0.49 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[PIGN]] | -0.48 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO]] | B | SYNPO activity raises TNKS1BP1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without SYNPO | 0.058 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises TNKS1BP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.56× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TNKS1BP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[BSN]] | B | BSN activity lowers TNKS1BP1's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.46× higher at baseline in the lines without BSN | 0.095 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[POTEE]] | B | POTEE activity lowers TNKS1BP1's level | lines that do not express POTEE (29) vs lines expressing it (21) | 1.43× higher at baseline in the lines without POTEE | 0.098 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 7.5); signed map (-3.9, 22.7). **Vector** length 118, 33.4% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.3 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +23.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +8.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Dihydroartemisinin (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.2 | -11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.7 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.6 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,299,638-57,324,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAB182, KIAA1741, FLJ45975; previously TNKS1BP1 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0C2](https://www.uniprot.org/uniprotkb/Q9C0C2) (CCR4-NOT transcription complex subunit 12):

> Component of the CCR4-NOT complex, a large multiprotein complex with several proteins assembled around the scaffolding protein CNOT1. This complex is one of the major cellular mRNA deadenylase and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. CNOT12 affects helicase selection into the CCR4-NOT complex. In addition, plays a role in DNA double strand …

**Summary**, from NCBI Gene [85456](https://www.ncbi.nlm.nih.gov/gene/85456):

> Enables ankyrin repeat binding activity; enzyme binding activity; and protein serine/threonine kinase activator activity. Involved in cellular response to ionizing radiation and double-strand break repair. Located in several cellular components, including adherens junction; heterochromatin; and nucleus. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19081) · Entrez [85456](https://www.ncbi.nlm.nih.gov/gene/85456) · UniProt [Q9C0C2](https://www.uniprot.org/uniprotkb/Q9C0C2) · Ensembl [ENSG00000149115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149115)

## Data

Gene col 7342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7342); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7342]; `tensor/DDL_lfc|DDL_z.npy` [7342]; `embed/gene_vectors.npy` [7342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7342 or target_col == 7342). Every well: [[TNKS1BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNKS1BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
