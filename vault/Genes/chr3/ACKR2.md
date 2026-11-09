---
symbol: "ACKR2"
type: "gene"
col: 6909
ensembl_id: "ENSG00000144648"
name: "atypical chemokine receptor 2"
location: "3p22.1"
module: 35
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ACKR2

*atypical chemokine receptor 2* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.95× (z +18.5, q 0e+00, up in 28 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.385× (z -7.8, q 3e-12, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAFA2]] (+0.63, fdr 3e-05), [[UPK2]] (+0.63, fdr 1e-05), [[ITGB2]] (+0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.95×** | +18.5 | 0e+00 | 28/29 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.33×** | +9.8 | 2e-20 | 31/43 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.33×** | +9.8 | 3e-20 | 18/42 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +9.0 | 4e-17 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +8.2 | 2e-14 | 14/29 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +8.2 | 2e-14 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +7.7 | 1e-12 | 15/24 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +7.2 | 3e-11 | 23/41 (HT-29, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +6.4 | 8e-09 | 18/40 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +6.0 | 1e-07 | 23/39 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +5.5 | 2e-06 | 3/12 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +4.8 | 7e-05 | 13/42 (Hs 766T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +4.8 | 7e-05 | 11/30 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +4.6 | 2e-04 | 10/35 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +4.5 | 2e-04 | 6/37 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.5 | 2e-04 | 11/35 (SK-MEL-2, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.76×** | +4.4 | 3e-04 | 13/38 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +4.3 | 5e-04 | 14/44 (NCI-H23, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.016 | 6/38 (NCI-H1573, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -7.8 | 3e-12 | 28/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -5.9 | 8e-07 | 19/38 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -5.6 | 5e-06 | 13/18 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.530×** | -5.2 | 3e-05 | 16/37 (SW 900, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -4.2 | 0.002 | 16/42 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.603×** | -4.1 | 0.003 | 9/45 (C32, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -3.8 | 0.012 | 16/39 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.618×** | -3.7 | 0.014 | 13/33 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.640×** | -3.6 | 0.017 | 9/35 (MIA PaCa-2, C-33 A, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.672×** | -3.2 | 0.060 | 17/38 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.060 | 7/38 (SW 900, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.673×** | -3.2 | 0.066 | 10/43 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -3.2 | 0.066 | 11/27 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.693× | -3.0 | 0.11 | 6/40 (NCI-H2030, BT-474, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.81 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0510× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 2 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0581× (z -9.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -8.9) |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.05 µM 0.0414× (z -8.8) |
| [[SW480 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.927 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAFA2]] | +0.63 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[UPK2]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ITGB2]] | +0.62 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[FAM174B]] | +0.62 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[PACRG]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CHKB-DT]] | +0.61 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[LRIG2-DT]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RELN]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BTC]] | +0.60 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[TMEM72-AS1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[IL1RAPL2]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACKR2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ID2-AS1]] | B | ID2-AS1 activity raises ACKR2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without ID2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[LINC02175]] | B | LINC02175 activity raises ACKR2's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without LINC02175 | 0.053 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.8, 27.4); signed map (35.4, -6.3). **Vector** length 54.8, 8.06% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | atypical chemokine receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,804,752-42,887,974 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCR10, D6, CCR9; previously CMKBR9, CCBP2 |
| Gene groups (HGNC) | Atypical chemokine receptors |
| Reactome | 5 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00590](https://www.uniprot.org/uniprotkb/O00590) (Atypical chemokine receptor 2):

> Atypical chemokine receptor that controls chemokine levels and localization via high-affinity chemokine binding that is uncoupled from classic ligand-driven signal transduction cascades, resulting instead in chemokine sequestration, degradation, or transcytosis. Also known as interceptor (internalizing receptor) or chemokine-scavenging receptor or chemokine decoy receptor. Acts as a receptor for chemokines including CCL2, CCL3, CCL3L1, CCL4, CCL5, CCL7, CCL8, CCL11, CCL13, CCL17, CCL22, CCL23, …

**Summary**, from NCBI Gene [1238](https://www.ncbi.nlm.nih.gov/gene/1238):

> This gene encodes a beta chemokine receptor, which is predicted to be a seven transmembrane protein similar to G protein-coupled receptors. Chemokines and their receptor-mediated signal transduction are critical for the recruitment of effector immune cells to the inflammation site. This gene is expressed in a range of tissues and hemopoietic cells. The expression of this receptor in lymphatic endothelial cells and overexpression in vascular tumors suggested its function in chemokine-driven …

**Accessions** — [HGNC:1565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1565) · Entrez [1238](https://www.ncbi.nlm.nih.gov/gene/1238) · UniProt [O00590](https://www.uniprot.org/uniprotkb/O00590) · Ensembl [ENSG00000144648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144648)

## Data

Gene col 6909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6909); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6909]; `tensor/DDL_lfc|DDL_z.npy` [6909]; `embed/gene_vectors.npy` [6909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6909 or target_col == 6909). Every well: [[ACKR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACKR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
