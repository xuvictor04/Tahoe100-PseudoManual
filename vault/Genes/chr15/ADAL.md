---
symbol: "ADAL"
type: "gene"
col: 9703
ensembl_id: "ENSG00000168803"
name: "N6-Methyl-AMP deaminase"
location: "15q15.3"
module: 10
arm: "+"
pooled_cpm: 13.58
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ADAL

*N6-Methyl-AMP deaminase* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +13.0, q 1e-35, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.661× (z -5.5, q 1e-05, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF518A]] (+0.63, fdr 5e-05), [[NNT-AS1]] (+0.63, fdr 6e-05), [[ANKRD26]] (+0.62, fdr 9e-05); moves opposite to [[PLXND1]] (-0.54, fdr 2e-04), [[SPATA13]] (-0.54, fdr 2e-04), [[TPRG1L]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LGALSL-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +13.0 | 1e-35 | 37/44 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.46×** | +12.0 | 9e-31 | 29/36 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.23×** | +10.3 | 1e-22 | 21/24 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.80×** | +7.3 | 6e-11 | 20/30 (NCI-H2030, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.68×** | +6.6 | 4e-09 | 24/43 (SW480, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.6 | 4e-09 | 25/40 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 2e-07 | 26/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.57×** | +5.8 | 6e-07 | 22/45 (SW480, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.8 | 8e-05 | 20/45 (SW480, C-33 A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.5 | 4e-04 | 16/44 (LoVo, NCI-H23, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +4.3 | 1e-03 | 14/45 (A498, LoVo, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.005 | 13/45 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.006 | 14/43 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.32×** | +3.6 | 0.013 | 8/44 (COLO 205, SNU-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.013 | 13/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.013 | 9/39 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.013 | 9/42 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 15/45 (J82, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.024 | 9/44 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.028 | 6/41 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.030 | 5/45 (LS 180, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -5.5 | 1e-05 | 24/44 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.460×** | -5.4 | 1e-05 | 24/41 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -5.4 | 1e-05 | 20/44 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -4.6 | 5e-04 | 16/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -3.9 | 0.009 | 12/45 (Panc 03.27, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.010 | 15/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.783× | -3.1 | 0.16 | 12/45 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.797× | -3.0 | 0.17 | 12/44 (A-172, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.27 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0421× (z -10.8) |
| [[BT-474 (line)]] | alt | 5.59 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0654× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.6) | — |
| [[LoVo (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +12.2) | — |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | +0.63 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[NNT-AS1]] | +0.63 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[ANKRD26]] | +0.62 | +0.81 / +0.37 | both halves | 9e-05 |  |
| [[C17orf75]] | +0.62 | +0.65 / +0.33 | both halves | 1e-04 |  |
| [[SCGB2B2]] | +0.61 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PGBD4]] | +0.61 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | +0.61 | +0.72 / +0.30 | both halves | 2e-04 |  |
| [[SMIM19]] | +0.61 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[OXA1L-DT]] | +0.60 | +0.69 / +0.27 | both halves | 3e-04 |  |
| [[ZNF337-AS1]] | +0.60 | +0.71 / +0.31 | both halves | 2e-04 |  |
| [[MZF1-AS1]] | +0.59 | +0.72 / +0.25 | both halves | 4e-04 |  |
| [[TMEM35B]] | +0.59 | +0.59 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXND1]] | -0.54 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[SPATA13]] | -0.54 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[TPRG1L]] | -0.53 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[SLC25A6]] | -0.52 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[MAST3]] | -0.52 | -0.56 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALSL-DT]] | C | ADAL activity weakens LGALSL-DT's drug response | lines that do not express ADAL (3) vs lines expressing it (40) | the lines without ADAL respond 1.74× as strongly (z diff -2.47); strongest at Panobinostat 0.5 µM: 0.06x vs 0.38x (z diff -6.3) | 0.010 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532; target measured in part of the lines; artifact flags |
| [[LGALSL-DT]] | C | ADAL activity lowers LGALSL-DT's level | lines that do not express ADAL (3) vs lines expressing it (47) | 2.74× higher at baseline in the lines without ADAL | 0.045 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532 |
| [[ANKRD18A]] | C | ADAL activity strengthens ANKRD18A's drug response | lines that do not express ADAL (3) vs lines expressing it (34) | the lines without ADAL respond 0.81× as strongly (z diff +0.91); strongest at Homoharringtonine 5 µM: 0.76x vs 1.71x (z diff +7.9) | 0.086 | ⚠ few lines (3 vs 47); across organs; co-occurs with EP300, RNF43, MSH6; also absent: SPAG4, PDE4A, ZNF532; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, 13.2); signed map (19.0, -19.3). **Vector** length 53.7, 8.26% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.4 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.9 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -2.6 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | N6-Methyl-AMP deaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,330,672-43,354,569 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ADAL |
| Gene groups (HGNC) | Adenosine deaminase family |
| Reactome | 6 pathways, smallest: Abacavir metabolism; Abacavir ADME; Purine salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DHV7](https://www.uniprot.org/uniprotkb/Q6DHV7) (N6-Methyl-AMP deaminase):

> Deaminase involved in the detoxification of modified adenosines containing N(6)-methylated adenine (m6A) post-transcriptional modification. Modified nucleosides are derived from the degradation of RNAs (mRNAs, rRNAs and tRNAs) and possess intrinsic cytotoxicity and must be cleared to prevent metabolic dysfunction. Acts downstream of ADK and catalyzes the hydrolysis of the free cytosolic methylated adenosine nucleotides N(6)-methyl-AMP (m6AMP), N(6),N(6)-dimethyl-AMP (m6,6AMP) and …

**Summary**, from NCBI Gene [161823](https://www.ncbi.nlm.nih.gov/gene/161823):

> Enables N6-methyl-AMP deaminase activity. Involved in toxic metabolite repair. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31853) · Entrez [161823](https://www.ncbi.nlm.nih.gov/gene/161823) · UniProt [Q6DHV7](https://www.uniprot.org/uniprotkb/Q6DHV7) · Ensembl [ENSG00000168803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168803)

## Data

Gene col 9703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9703); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9703]; `tensor/DDL_lfc|DDL_z.npy` [9703]; `embed/gene_vectors.npy` [9703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9703 or target_col == 9703). Every well: [[ADAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
