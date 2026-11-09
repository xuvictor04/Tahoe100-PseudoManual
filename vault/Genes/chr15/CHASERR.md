---
symbol: "CHASERR"
type: "gene"
col: 15750
ensembl_id: "ENSG00000272888"
name: "CHD2 adjacent suppressive regulatory RNA"
location: "15q26.1"
module: 130
arm: "+"
pooled_cpm: 36.25
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CHASERR

*CHD2 adjacent suppressive regulatory RNA* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.51× (z +10.0, q 1e-20, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.325× (z -11.5, q 1e-27, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK1A]] (+0.73, fdr 7e-06), [[H3-3A]] (+0.72, fdr 7e-06), [[RAB21]] (+0.68, fdr 9e-06); moves opposite to [[DAP3]] (-0.61, fdr 1e-05), [[NBPF20]] (-0.59, fdr 1e-05), [[METTL2B]] (-0.59, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPCAM-DT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MATR3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.51×** | +10.0 | 1e-20 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.94×** | +8.5 | 6e-15 | 45/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +6.4 | 3e-08 | 30/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +6.1 | 1e-07 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.4 | 6e-06 | 13/49 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +5.2 | 2e-05 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.0 | 4e-05 | 29/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.003 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.16×** | +4.1 | 0.003 | 29/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.026 | 23/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.030 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.030 | 22/47 (SNU-423, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.1 | 0.089 | 20/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.325×** | -11.5 | 1e-27 | 46/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.327×** | -11.4 | 1e-27 | 46/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.389×** | -9.6 | 1e-19 | 43/48 (SW 900, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.410×** | -8.7 | 3e-16 | 36/38 (NCI-H2347, SW1417, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.518×** | -6.7 | 2e-09 | 39/48 (NCI-H23, SW 900, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -6.1 | 8e-08 | 36/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.572×** | -5.7 | 1e-06 | 36/46 (NCI-H2347, SHP-77, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -4.5 | 6e-04 | 30/48 (PANC-1, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -3.9 | 0.006 | 26/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.607×** | -3.6 | 0.016 | 25/48 (RKO, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.512×** | -3.6 | 0.019 | 23/47 (NCI-H2347, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.713×** | -3.4 | 0.027 | 24/47 (NCI-H2347, NCI-H23, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.790×** | -3.4 | 0.028 | 27/48 (NCI-H2347, NCI-H661, …) | top dose only | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.734×** | -3.2 | 0.065 | 16/48 (RKO, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.1 | 0.072 | 21/48 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.078 | 19/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.662×** | -3.0 | 0.085 | 22/47 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.746×** | -3.0 | 0.085 | 19/47 (hTERT-HPNE, NCI-H661, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 74.9 | 3 (2 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.73× (z +10.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 26.3 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.77× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 29.2 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.247× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 60.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 5 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.199× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.3) |
| [[SW480 (line)]] | alt | 31.8 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.83× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.301× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -9.2) |
| [[COLO 205 (line)]] | alt | 54.7 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -9.0) |
| [[LoVo (line)]] | wt | 36.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 23.9× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 35.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0678× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.105× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -10.3) |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -10.1) |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.144× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.158× (z -10.3) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A498 (line)]] | wt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.7) | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.170× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -10.5) |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK1A]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[H3-3A]] | +0.72 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[RAB21]] | +0.68 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[PCMTD1]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RBM33]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[KDM6A]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TAPT1]] | +0.65 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAF1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[WTAP]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SIAH1]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PPP1CB]] | +0.61 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[WAC]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP3]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NBPF20]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[METTL2B]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SETX]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[STK4]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CRK]] | -0.56 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[TUBB6]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[MPP3]] | -0.55 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ANKS6]] | -0.55 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[CUTC]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[DDX19A]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM-DT]] | B | EPCAM-DT activity raises CHASERR's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without EPCAM-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[EPCAM-DT]] | B | EPCAM-DT activity strengthens CHASERR's drug response | lines that do not express EPCAM-DT (13) vs lines expressing it (36) | the lines without EPCAM-DT respond 0.81× as strongly (z diff +1.31); strongest at Panobinostat 0.5 µM: 0.40x vs 0.27x (z diff +2.4) | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MATR3]] | C | CHASERR's natural level weakens MATR3's drug response | CHASERR's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.12; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.7, -26.4); signed map (29.7, -23.9). **Vector** length 95.1, 27.0% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.3 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | CHD2 adjacent suppressive regulatory RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.1 — chr15:92,819,540-92,899,701 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TGCB; previously LINC01578 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48626) · Entrez [100507217](https://www.ncbi.nlm.nih.gov/gene/100507217) · Ensembl [ENSG00000272888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272888)

## Data

Gene col 15750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15750); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15750]; `tensor/DDL_lfc|DDL_z.npy` [15750]; `embed/gene_vectors.npy` [15750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15750 or target_col == 15750). Every well: [[CHASERR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHASERR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
