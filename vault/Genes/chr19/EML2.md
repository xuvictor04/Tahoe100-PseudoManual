---
symbol: "EML2"
type: "gene"
col: 4657
ensembl_id: "ENSG00000125746"
name: "EMAP like 2"
location: "19q13.32"
module: 3
arm: "+"
pooled_cpm: 41.9
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# EML2

*EMAP like 2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +6.4, q 1e-07, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.497× (z -11.7, q 1e-28, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3A]] (+0.70, fdr 7e-06), [[DOCK6]] (+0.69, fdr 7e-06), [[ETHE1]] (+0.65, fdr 1e-05); moves opposite to [[MOB1A]] (-0.70, fdr 7e-06), [[EIF4G2]] (-0.68, fdr 1e-05), [[RCN1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CACNG7]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Fluvoxamine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.4 | 1e-07 | 29/47 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 1e-06 | 35/47 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 6e-06 | 36/45 (A549, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.002 | 23/47 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.5 | 0.053 | 18/46 (A-427, NCI-H1573, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.087 | 14/47 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.11 | 8/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.11 | 11/47 (CFPAC-1, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.497×** | -11.7 | 1e-28 | 42/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -9.4 | 1e-18 | 42/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -9.4 | 1e-18 | 35/46 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.604×** | -8.4 | 7e-15 | 34/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.9 | 4e-13 | 33/46 (MIA PaCa-2, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -7.5 | 5e-12 | 30/44 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -7.0 | 3e-10 | 29/46 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -6.5 | 5e-09 | 28/46 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -5.8 | 3e-07 | 28/45 (HS-578T, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -5.4 | 5e-06 | 27/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.8 | 7e-05 | 22/47 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.821×** | -4.6 | 2e-04 | 22/46 (MIA PaCa-2, LoVo, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -4.6 | 2e-04 | 27/48 (HS-578T, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.783×** | -4.0 | 0.002 | 19/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.786×** | -4.0 | 0.002 | 24/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.792×** | -3.7 | 0.007 | 21/46 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -3.7 | 0.008 | 19/47 (SK-MEL-2, LoVo, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.6 | 0.011 | 19/47 (BT-474, J82, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.012 | 20/46 (HT-29, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 55.9 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -14.8) |
| [[HOP62 (line)]] | alt | 99.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.6) |
| [[PANC-1 (line)]] | alt | 40.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -12.6) |
| [[A-427 (line)]] | wt | 35.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.1) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.5) |
| [[Hs 766T (line)]] | wt | 43.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.315× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 47.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 30.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.6) |
| [[A498 (line)]] | wt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.5) |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[HS-578T (line)]] | alt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.0) |
| [[HT-29 (line)]] | alt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -10.8) |
| [[LS 180 (line)]] | wt | 52.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -8.7) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0667× (z -16.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3A]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[DOCK6]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ETHE1]] | +0.65 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CAMKK1]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MAST1]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[GIPR]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 | same gene group; ⚠ same locus (22.6 kb: neighbours can correlate without regulation) |
| [[TECPR1]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PHLDB3]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SMIM29]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BCAS4]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DENND6B]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[CCDC85B]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.70 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.68 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[RCN1]] | -0.63 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SPAG16]] | -0.62 | -0.52 / -0.54 | both halves | 1e-05 | same gene group |
| [[TRIP12]] | -0.62 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CNOT1]] | -0.61 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[DDX3X]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CHRAC1]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TUG1]] | -0.60 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CRPPA]] | -0.60 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.60 | -0.48 / -0.57 | both halves | 2e-05 | same gene group |
| [[TARDBP]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG7]] | B | CACNG7 activity raises EML2's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.28× lower at baseline in the lines without CACNG7 | 0.038 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EML2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | EML2's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | EML2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.317 over the table, 0.044 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | EML2's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | EML2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.499 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.3, 1.4); signed map (-24.7, 22.1). **Vector** length 103, 26.1% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,606,994-45,645,602 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EMAP2, ELP70, EMAP-2 |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95834](https://www.uniprot.org/uniprotkb/O95834) (Echinoderm microtubule-associated protein-like 2):

> Tubulin binding protein that inhibits microtubule nucleation and growth, resulting in shorter microtubules.

**Summary**, from NCBI Gene [24139](https://www.ncbi.nlm.nih.gov/gene/24139):

> Enables microtubule binding activity. Involved in negative regulation of microtubule polymerization and regulation of microtubule nucleation. Located in mitotic spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18035) · Entrez [24139](https://www.ncbi.nlm.nih.gov/gene/24139) · UniProt [O95834](https://www.uniprot.org/uniprotkb/O95834) · Ensembl [ENSG00000125746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125746)

## Data

Gene col 4657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4657); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4657]; `tensor/DDL_lfc|DDL_z.npy` [4657]; `embed/gene_vectors.npy` [4657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4657 or target_col == 4657). Every well: [[EML2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
