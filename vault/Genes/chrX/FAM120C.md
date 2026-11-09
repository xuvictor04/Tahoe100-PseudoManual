---
symbol: "FAM120C"
type: "gene"
col: 11490
ensembl_id: "ENSG00000184083"
name: "family with sequence similarity 120 member C"
location: "Xp11.22"
module: 1
arm: "+"
pooled_cpm: 17.55
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FAM120C

*family with sequence similarity 120 member C* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.37× (z +8.7, q 2e-15, up in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.32× (z +8.5, q 4e-15, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -17.2, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSL2]] (+0.65, fdr 1e-05), [[QTRT2]] (+0.63, fdr 1e-05), [[SCO1]] (+0.62, fdr 1e-05); moves opposite to [[SORBS1]] (-0.54, fdr 4e-05), [[SPAG9]] (-0.54, fdr 7e-05), [[ABHD3]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +8.7 | 2e-15 | 28/48 (NCI-H2347, A549, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +8.5 | 4e-15 | 28/45 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.0 | 4e-10 | 22/46 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +6.7 | 4e-09 | 26/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +5.5 | 5e-06 | 18/48 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.25×** | +4.3 | 0.001 | 10/47 (KATO III, HS-578T, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 8/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.2 | 0.002 | 15/45 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.021 | 11/48 (KATO III, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.025 | 8/46 (A498, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | **1.20×** | +3.4 | 0.036 | 11/42 (Panc 03.27, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.088 | 7/46 (A549, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -17.2 | 0e+00 | 37/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -10.4 | 1e-22 | 34/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -9.1 | 1e-17 | 29/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -8.2 | 4e-14 | 26/48 (AN3 CA, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -7.3 | 4e-11 | 24/47 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.679×** | -7.2 | 5e-11 | 25/48 (PANC-1, SK-MEL-2, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -7.0 | 1e-10 | 23/48 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -6.8 | 7e-10 | 22/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -6.7 | 1e-09 | 23/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.727×** | -6.2 | 4e-08 | 20/48 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.794×** | -4.5 | 4e-04 | 15/48 (PANC-1, Hs 766T, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.676×** | -4.0 | 0.003 | 15/45 (SNU-423, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.816×** | -4.0 | 0.003 | 12/47 (COLO 205, H4, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.682×** | -3.9 | 0.004 | 11/39 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.825×** | -3.7 | 0.007 | 19/46 (BT-474, SW1417, …) | two highest doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.040 | 7/46 (SW48, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.078 | 10/48 (C-33 A, H4, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.0) |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.4) |
| [[HOP62 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.1) |
| [[SW480 (line)]] | alt | 36.0 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 4.60× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.400× (z -9.9) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.207× (z -10.3) |
| [[H4 (line)]] | wt | 33.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.171× (z -9.8) |
| [[LoVo (line)]] | wt | 8.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.211× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.0) |
| [[RKO (line)]] | wt | 8.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -8.6) |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 1 | — | [[Everolimus (drug)]] 0.05 µM 0.121× (z -11.6) |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.2) |
| [[A-427 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSL2]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[QTRT2]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SCO1]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PCMTD1-DT]] | +0.62 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[KLHL42]] | +0.61 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ECHDC1]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MTPAP]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[MRM1]] | +0.59 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[TYSND1]] | +0.59 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[COG8]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DHX33]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORBS1]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.54 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ABHD3]] | -0.53 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PTPRH]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[BAIAP2L1]] | -0.52 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[F11R]] | -0.51 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PLEKHO2]] | -0.51 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ABAT]] | -0.51 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[GK]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[PRKCZ]] | -0.51 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[CAST]] | -0.50 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[NBEAL1]] | -0.50 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.3, 16.8); signed map (4.9, -40.9). **Vector** length 75.9, 13.0% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.9 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | +3.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -17.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -7.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 120 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:54,068,324-54,183,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORF34, FLJ20506; previously CXorf17 |
| Gene groups (HGNC) | PIN-like domain superfamily |
| Matched by | ensembl_id |

UniProt [Q9NX05](https://www.uniprot.org/uniprotkb/Q9NX05) carries no function annotation.

**Summary**, from NCBI Gene [54954](https://www.ncbi.nlm.nih.gov/gene/54954):

> This gene encodes a potential transmembrane protein and lies in a region where mutations and deletions have been associated with intellectual disability and autism. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:16949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16949) · Entrez [54954](https://www.ncbi.nlm.nih.gov/gene/54954) · UniProt [Q9NX05](https://www.uniprot.org/uniprotkb/Q9NX05) · Ensembl [ENSG00000184083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184083)

## Data

Gene col 11490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11490); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11490]; `tensor/DDL_lfc|DDL_z.npy` [11490]; `embed/gene_vectors.npy` [11490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11490 or target_col == 11490). Every well: [[FAM120C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM120C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
