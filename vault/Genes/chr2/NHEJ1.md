---
symbol: "NHEJ1"
type: "gene"
col: 11941
ensembl_id: "ENSG00000187736"
name: "non-homologous end joining factor 1"
location: "2q35"
module: 38
arm: "+"
pooled_cpm: 28.02
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# NHEJ1

*non-homologous end joining factor 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +16.2, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.450× (z -15.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC23A3]] (+0.65, fdr 1e-05, ⚠ same locus), [[ISY1-RAB43]] (+0.63, fdr 1e-05), [[LINC01588]] (+0.62, fdr 7e-06), [[SMG1P7]] (+0.60, fdr 1e-05); moves opposite to [[PEX2]] (-0.54, fdr 3e-05), [[HMSD]] (-0.52, fdr 4e-05), [[NHLRC2]] (-0.52, fdr 8e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +16.2 | 0e+00 | 41/47 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +7.6 | 6e-12 | 29/48 (A-172, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 7e-06 | 24/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.002 | 15/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.052 | 15/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.052 | 19/48 (SW480, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.4 | 0.052 | 0/48 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.052 | 9/47 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.11 | 14/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.13 | 17/48 (SHP-77, KATO III, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.13 | 12/47 (HS-578T, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -15.0 | 0e+00 | 43/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -11.4 | 1e-27 | 38/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.621×** | -9.3 | 3e-18 | 35/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -6.9 | 6e-10 | 27/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.739×** | -5.4 | 6e-06 | 19/42 (NCI-H2030, SK-MEL-2, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -5.1 | 3e-05 | 23/48 (HT-29, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.8 | 1e-04 | 18/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.847× | -4.6 | 3e-04 | 21/47 (A-427, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.808×** | -4.1 | 0.002 | 20/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.698×** | -3.7 | 0.015 | 11/44 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.830×** | -3.6 | 0.015 | 18/47 (PANC-1, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | 0.835× | -3.4 | 0.036 | 14/37 (C32, Hs 766T, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.734×** | -3.1 | 0.071 | 10/47 (C-33 A, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.314× (z -12.7) |
| [[SW480 (line)]] | alt | 29.4 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.365× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.422× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 32.0 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +12.2) | [[Harringtonine (drug)]] 0.5 µM 0.393× (z -9.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.387× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.205× (z -11.1) |
| [[C32 (line)]] | wt | 54.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 49.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 24.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.74× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 16.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 37.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.285× (z -9.1) |
| [[LS 180 (line)]] | wt | 21.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -19.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0727× (z -10.3) |
| [[BT-474 (line)]] | alt | 9.51 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0731× (z -9.6) |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 1 | — | [[Capivasertib (drug)]] 5 µM 0.0431× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.5) | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -9.6) |
| [[RKO (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC23A3]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 | STRING 730; ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[ISY1-RAB43]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SMG1P7]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TRPV1]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EFCAB8]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PHYHD1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PYGM]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SPOCK2]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[VWCE]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC22A20P]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[QRICH2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[HMSD]] | -0.52 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[NHLRC2]] | -0.52 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[TMEM254]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CEP295]] | -0.51 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ARMCX5]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[THOC1]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MRPL16]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCNC]] | -0.48 | -0.26 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.9, -16.4); signed map (13.2, 10.2). **Vector** length 86.9, 17.3% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +16.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -15.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -6.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.0 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | non-homologous end joining factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,069,355-219,160,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cernunnos, XLF, FLJ12610 |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9Q4](https://www.uniprot.org/uniprotkb/Q9H9Q4) (Non-homologous end-joining factor 1):

> DNA repair protein involved in DNA non-homologous end joining (NHEJ); it is required for double-strand break (DSB) repair and V(D)J recombination and is also involved in telomere maintenance. Plays a key role in NHEJ by promoting the ligation of various mismatched and non-cohesive ends. Together with PAXX, collaborates with DNA polymerase lambda (POLL) to promote joining of non-cohesive DNA ends. May act in concert with XRCC5-XRCC6 (Ku) to stimulate XRCC4-mediated joining of blunt ends and …

**Summary**, from NCBI Gene [79840](https://www.ncbi.nlm.nih.gov/gene/79840):

> Double-strand breaks in DNA result from genotoxic stresses and are among the most damaging of DNA lesions. This gene encodes a DNA repair factor essential for the nonhomologous end-joining pathway, which preferentially mediates repair of double-stranded breaks. Mutations in this gene cause different kinds of severe combined immunodeficiency disorders. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25737) · Entrez [79840](https://www.ncbi.nlm.nih.gov/gene/79840) · UniProt [Q9H9Q4](https://www.uniprot.org/uniprotkb/Q9H9Q4) · Ensembl [ENSG00000187736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187736)

## Data

Gene col 11941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11941); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11941]; `tensor/DDL_lfc|DDL_z.npy` [11941]; `embed/gene_vectors.npy` [11941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11941 or target_col == 11941). Every well: [[NHEJ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHEJ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
