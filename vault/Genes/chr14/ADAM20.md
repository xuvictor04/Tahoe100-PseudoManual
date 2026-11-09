---
symbol: "ADAM20"
type: "gene"
col: 5496
ensembl_id: "ENSG00000134007"
name: "ADAM metallopeptidase domain 20"
location: "14q24.2"
module: 37
arm: "+"
pooled_cpm: 27.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ADAM20

*ADAM metallopeptidase domain 20* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 2.33× (z +9.9, q 3e-20, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.265× (z -15.5, q 0e+00, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.562× (z -6.5, q 1e-08, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM20P1]] (+0.86, fdr 7e-06), [[MED6]] (+0.79, fdr 7e-06, ⚠ same locus), [[ECT2L]] (+0.73, fdr 7e-06), [[LINC02680]] (+0.72, fdr 7e-06); moves opposite to [[RBM12]] (-0.58, fdr 7e-06), [[IDH3A]] (-0.56, fdr 1e-05), [[UBE2E3]] (-0.54, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC28A2-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C12orf73]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +9.9 | 3e-20 | 38/48 (HT-29, SW480, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +7.4 | 4e-11 | 43/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +5.7 | 3e-06 | 34/47 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **2.23×** | +4.9 | 1e-04 | 38/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.011 | 19/48 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.66× | +3.1 | 0.19 | 14/31 (NCI-H1792, NCI-H2030, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 1.65× | +3.0 | 0.19 | 12/49 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.265×** | -15.5 | 0e+00 | 42/48 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.351×** | -11.8 | 2e-29 | 33/37 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -7.7 | 2e-12 | 38/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -6.5 | 1e-08 | 31/48 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.586×** | -6.2 | 5e-08 | 31/45 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.865× | -6.1 | 1e-07 | 17/49 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -5.3 | 1e-05 | 25/46 (HepG2/C3A, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.643×** | -4.8 | 1e-04 | 23/41 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -4.6 | 2e-04 | 24/48 (PANC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.679×** | -4.5 | 3e-04 | 28/48 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.700×** | -4.2 | 0.002 | 22/48 (NCI-H1573, LoVo, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.702×** | -4.1 | 0.002 | 23/48 (NCI-H1573, LoVo, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.718×** | -3.9 | 0.005 | 19/48 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.728×** | -3.7 | 0.008 | 22/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.743×** | -3.5 | 0.020 | 16/49 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.749×** | -3.4 | 0.026 | 18/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.757×** | -3.2 | 0.034 | 15/49 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.757×** | -3.2 | 0.034 | 15/49 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.650×** | -3.2 | 0.034 | 12/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.652×** | -3.2 | 0.035 | 13/48 (HEC-1-A, C32, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.045 | 12/48 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.766×** | -3.1 | 0.045 | 18/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 34.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 33.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0505× (z -19.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 81.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0537× (z -18.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -19.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 3 (2 ⚠) | — | [[Allantoin (drug)]] 0.5 µM 0.0809× (z -14.4) |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0788× (z -14.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0727× (z -14.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 46.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0244× (z -26.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 22.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0512× (z -17.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 68.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0618× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.156× (z -8.8) |
| [[H4 (line)]] | wt | 45.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0917× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0745× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 28.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0768× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0985× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -20.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.58× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 17.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.60× (z +9.7) | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -8.7) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -15.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -13.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0692× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM20P1]] | +0.86 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MED6]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | ⚠ same locus (46.2 kb, same strand: neighbours can correlate without regulation) |
| [[ECT2L]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ZNF814]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[TSNAX-DISC1]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[WDR49]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TTC28-AS1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LINC00159]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[BET1]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SRP54]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[RNMT]] | +0.64 | +0.52 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM12]] | -0.58 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[IDH3A]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[UBE2E3]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A2-AS1]] | B | SLC28A2-AS1 activity raises ADAM20's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without SLC28A2-AS1 | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CYP27A1]] | B | CYP27A1 activity raises ADAM20's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without CYP27A1 | 0.071 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf73]] | C | ADAM20's natural level weakens C12orf73's drug response | ADAM20's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.09; direction not clear | 0.024 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, -19.5); signed map (8.1, 4.6). **Vector** length 112, 31.0% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,522,358-70,535,015 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Reactome | 3 pathways, smallest: Interaction With Cumulus Cells And The Zona Pellucida; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O43506](https://www.uniprot.org/uniprotkb/O43506) (Disintegrin and metalloproteinase domain-containing protein 20):

> May be involved in sperm maturation and/or fertilization.

**Summary**, from NCBI Gene [8748](https://www.ncbi.nlm.nih.gov/gene/8748):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The expression of this gene is testis-specific. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:199) · Entrez [8748](https://www.ncbi.nlm.nih.gov/gene/8748) · UniProt [O43506](https://www.uniprot.org/uniprotkb/O43506) · Ensembl [ENSG00000134007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134007)

## Data

Gene col 5496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5496); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5496]; `tensor/DDL_lfc|DDL_z.npy` [5496]; `embed/gene_vectors.npy` [5496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5496 or target_col == 5496). Every well: [[ADAM20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
