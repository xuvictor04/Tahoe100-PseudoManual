---
symbol: "DCAF4"
type: "gene"
col: 4083
ensembl_id: "ENSG00000119599"
name: "DDB1 and CUL4 associated factor 4"
location: "14q24.2"
module: 33
arm: "+"
pooled_cpm: 11.88
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DCAF4

*DDB1 and CUL4 associated factor 4* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.49× (z +16.4, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.669× (z -10.2, q 1e-21, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLE1]] (+0.74, fdr 7e-06), [[GARNL3]] (+0.70, fdr 7e-06), [[TSNARE1]] (+0.68, fdr 1e-05); moves opposite to [[FKBP3]] (-0.58, fdr 3e-05), [[SNHG31]] (-0.56, fdr 6e-05), [[PRKAR1A]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NUFIP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +16.4 | 0e+00 | 40/47 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +15.6 | 0e+00 | 40/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +14.7 | 0e+00 | 37/47 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +9.0 | 3e-17 | 23/45 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +8.9 | 6e-17 | 27/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +8.9 | 7e-17 | 26/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +7.7 | 1e-12 | 22/44 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 5e-12 | 20/45 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.7 | 1e-09 | 21/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +6.3 | 2e-08 | 20/44 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.1 | 5e-08 | 19/46 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 1e-07 | 19/44 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.8 | 9e-05 | 6/19 (NCI-H2030, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 7e-04 | 10/35 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 7e-04 | 16/47 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 11/47 (PANC-1, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 9/48 (MIA PaCa-2, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -10.2 | 1e-21 | 31/45 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -8.3 | 4e-14 | 25/46 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -8.1 | 8e-14 | 24/45 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.654×** | -7.6 | 4e-12 | 20/36 (MIA PaCa-2, NCI-H2347, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.8 | 1e-06 | 19/47 (MIA PaCa-2, SNU-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.013 | 10/46 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.4 | 0.049 | 3/48 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.049 | 11/46 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Futibatinib (drug)]] 5 µM 0.0628× (z -9.4) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0771× (z -14.0) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 9.17 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.131× (z -9.5) |
| [[LS 180 (line)]] | wt | 9.78 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0874× (z -8.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0732× (z -9.6) |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -9.5) |
| [[SW 900 (line)]] | alt | 6.41 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0669× (z -8.9) |
| [[A498 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLE1]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 | same gene group |
| [[GARNL3]] | +0.70 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TSNARE1]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[POLR3H]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RCL1]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EMSLR]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CAMKK1]] | +0.64 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CTU1]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[SNHG17]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.63 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[DDX31]] | +0.63 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MPP3]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP3]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SNHG31]] | -0.56 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[PRKAR1A]] | -0.53 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[DLEU2]] | -0.53 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[TYMSOS]] | -0.52 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[DECR1]] | -0.52 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[RO60]] | -0.52 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[SYNJ1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DCAF4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABCA3]] | B | ABCA3 activity raises DCAF4's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without ABCA3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUFIP1]] | C | DCAF4's natural level weakens NUFIP1's drug response | DCAF4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.03; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.0, -43.5); signed map (-10.1, -54.5). **Vector** length 90.3, 18.1% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +16.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +15.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +14.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:72,926,377-72,959,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K114; previously WDR21, WDR21A |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV16](https://www.uniprot.org/uniprotkb/Q8WV16) (DDB1- and CUL4-associated factor 4):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [26094](https://www.ncbi.nlm.nih.gov/gene/26094):

> This gene encodes a WD repeat-containing protein that interacts with the Cul4-Ddb1 E3 ligase macromolecular complex. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:20229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20229) · Entrez [26094](https://www.ncbi.nlm.nih.gov/gene/26094) · UniProt [Q8WV16](https://www.uniprot.org/uniprotkb/Q8WV16) · Ensembl [ENSG00000119599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119599)

## Data

Gene col 4083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4083); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4083]; `tensor/DDL_lfc|DDL_z.npy` [4083]; `embed/gene_vectors.npy` [4083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4083 or target_col == 4083). Every well: [[DCAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
