---
symbol: "PLCD1"
type: "gene"
col: 11883
ensembl_id: "ENSG00000187091"
name: "phospholipase C delta 1"
location: "3p22.2"
module: 85
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PLCD1

*phospholipase C delta 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.89× (z +11.9, q 6e-30, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.267× (z -14.7, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSBPL7]] (+0.69, fdr 1e-05), [[MOSPD3]] (+0.69, fdr 1e-05), [[ANKMY2]] (+0.69, fdr 1e-05); moves opposite to [[CPSF2]] (-0.71, fdr 7e-06), [[ST7L]] (-0.68, fdr 1e-05), [[ANAPC7]] (-0.67, fdr 8e-06).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FKBP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +11.9 | 6e-30 | 40/45 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +11.0 | 1e-25 | 37/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +10.6 | 9e-24 | 39/46 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +10.2 | 2e-22 | 29/40 (HOP62, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +8.0 | 1e-13 | 22/46 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.72×** | +6.1 | 1e-07 | 17/42 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.7 | 9e-07 | 12/37 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 1e-05 | 19/37 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.9 | 5e-05 | 17/46 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.7 | 2e-04 | 7/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +4.5 | 3e-04 | 5/44 (SW1417, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 4e-04 | 10/47 (LS 180, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 1e-03 | 11/42 (AsPC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.003 | 13/47 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.2 | 0.057 | 1/17 (A549) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.267×** | -14.7 | 0e+00 | 39/46 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.279×** | -14.3 | 1e-43 | 36/42 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -11.0 | 6e-26 | 27/38 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.393×** | -10.4 | 3e-23 | 33/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -10.4 | 3e-23 | 30/36 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.586×** | -8.4 | 3e-15 | 28/40 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.507×** | -7.6 | 3e-12 | 23/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.509×** | -7.5 | 4e-12 | 26/46 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.527×** | -6.9 | 4e-10 | 22/44 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -6.4 | 6e-09 | 20/30 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.588×** | -5.9 | 2e-07 | 19/44 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -5.7 | 6e-07 | 17/44 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -5.6 | 1e-06 | 19/35 (Hs 766T, J82, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -5.5 | 1e-06 | 19/38 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -5.5 | 1e-06 | 21/44 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -5.5 | 1e-06 | 13/35 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -4.4 | 4e-04 | 18/45 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.688×** | -4.0 | 0.002 | 12/43 (NCI-H23, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0908× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 4.89 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.8) |
| [[A549 (line)]] | wt | 5.73 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0559× (z -11.6) |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -10.1) |
| [[LoVo (line)]] | wt | 8.47 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.6) |
| [[LS 180 (line)]] | wt | 6.15 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -10.0) |
| [[PANC-1 (line)]] | alt | 2.97 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0959× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0423× (z -9.8) |
| [[C32 (line)]] | wt | 5.01 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0757× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 5.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 5.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 6.71 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0345× (z -10.1) |
| [[HOP62 (line)]] | alt | 4.86 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.5× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 6.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -10.4) |
| [[KATO III (line)]] | alt | 6.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0695× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0558× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 7.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0876× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 5.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0587× (z -10.8) |
| [[SNU-423 (line)]] | alt | 5.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL7]] | +0.69 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.69 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MAST3]] | +0.69 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.68 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LMBR1L]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RGS14]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MGST3]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[YIF1B]] | +0.66 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SNAPC3]] | +0.66 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.71 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ST7L]] | -0.68 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.67 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[ENOX2]] | -0.67 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.65 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SNX5]] | -0.64 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[PSPC1]] | -0.63 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.63 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.63 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SDCBP2-AS1]] | -0.63 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.62 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP1B]] | B | FKBP1B activity raises PLCD1's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without FKBP1B | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.6, -6.1); signed map (-31.1, 19.9). **Vector** length 75.1, 13.6% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +10.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -14.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -14.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,007,496-38,029,642 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases; EF-hand domain containing |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P51178](https://www.uniprot.org/uniprotkb/P51178) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase delta-1):

> The production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) is mediated by activated phosphatidylinositol-specific phospholipase C enzymes. Essential for trophoblast and placental development (By similarity). Binds phosphatidylinositol 4,5-bisphosphate.

**Summary**, from NCBI Gene [5333](https://www.ncbi.nlm.nih.gov/gene/5333):

> This gene encodes a member of the phospholipase C family. Phospholipase C isozymes play critical roles in intracellular signal transduction by catalyzing the hydrolysis of phosphatidylinositol 4,5-bisphosphate (PIP2) into the second messengers diacylglycerol (DAG) and inositol triphosphate (IP3). The encoded protein functions as a tumor suppressor in several types of cancer, and mutations in this gene are a cause of hereditary leukonychia. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:9060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9060) · Entrez [5333](https://www.ncbi.nlm.nih.gov/gene/5333) · UniProt [P51178](https://www.uniprot.org/uniprotkb/P51178) · Ensembl [ENSG00000187091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187091)

## Data

Gene col 11883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11883); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11883]; `tensor/DDL_lfc|DDL_z.npy` [11883]; `embed/gene_vectors.npy` [11883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11883 or target_col == 11883). Every well: [[PLCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
