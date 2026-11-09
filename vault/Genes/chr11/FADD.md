---
symbol: "FADD"
type: "gene"
col: 9587
ensembl_id: "ENSG00000168040"
name: "Fas associated via death domain"
location: "11q13.3"
module: 7
arm: "+"
pooled_cpm: 11.07
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FADD

*Fas associated via death domain* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.09× (z +7.2, q 3e-10, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.444× (z -7.9, q 1e-12, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTI12]] (+0.73, fdr 7e-06), [[DNTTIP2]] (+0.72, fdr 7e-06), [[EIF6]] (+0.70, fdr 7e-06); moves opposite to [[RCN2]] (-0.61, fdr 1e-05), [[SEPTIN2]] (-0.60, fdr 1e-05), [[CTC1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PWP2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Fluvoxamine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +7.2 | 3e-10 | 33/46 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.1 | 0.011 | 19/44 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.51×** | +4.0 | 0.011 | 20/47 (A549, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.011 | 16/42 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.49×** | +3.9 | 0.011 | 15/41 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.016 | 12/47 (A549, CFPAC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.12 | 18/45 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 1.84× | +3.1 | 0.13 | 10/36 (SK-MEL-2, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.13 | 13/42 (A549, HT-29, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -7.9 | 1e-12 | 33/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -7.4 | 4e-11 | 26/42 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -5.9 | 5e-07 | 21/31 (NCI-H1573, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -5.8 | 1e-06 | 31/46 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -5.1 | 3e-05 | 24/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -4.9 | 7e-05 | 24/39 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -4.4 | 8e-04 | 24/46 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -3.3 | 0.059 | 17/28 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.083 | 17/47 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 21.1 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -12.1) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -10.3) |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -8.5) |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.26 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0762× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -19.1) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0653× (z -8.7) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.43 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0807× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.106× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 9.71 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTI12]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[EIF6]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[THAP7]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[HPS6]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 | pathway: Apoptosis |
| [[CCDC137]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[VPS25]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[BLOC1S4]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[UTP3]] | +0.67 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[MRM2]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.60 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[CTC1]] | -0.59 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[GNAS]] | -0.55 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PWP2]] | B | PWP2 activity raises FADD's level | lines that do not express PWP2 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without PWP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: KRT80, ENSG00000224621, ANO1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | FADD's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | FADD's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.470 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.0, 0.3); signed map (-3.9, -24.1). **Vector** length 90.5, 20.2% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Fas associated via death domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:70,203,296-70,207,390 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MORT1, GIG3 |
| Gene groups (HGNC) | Death effector domain containing; Ripoptosome; Death inducing signaling complex |
| Reactome | 28 pathways, smallest: FasL/ CD95L signaling; TLR3-mediated TICAM1-dependent programmed cell death; Defective RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13158](https://www.uniprot.org/uniprotkb/Q13158) (FAS-associated death domain protein):

> Apoptotic adapter molecule that recruits caspases CASP8 or CASP10 to the activated FAS/CD95 or TNFRSF1A/TNFR-1 receptors. The resulting aggregates, named death-inducing signaling complexes (DISCs), perform CASP8 proteolytic activation. Active CASP8 initiates the subsequent cascade of caspases mediating apoptosis. Involved in interferon-mediated antiviral immune response, playing a role in the positive regulation of interferon signaling.

**Summary**, from NCBI Gene [8772](https://www.ncbi.nlm.nih.gov/gene/8772):

> The protein encoded by this gene is an adaptor molecule that interacts with various cell surface receptors and mediates cell apoptotic signals. Through its C-terminal death domain, this protein can be recruited by TNFRSF6/Fas-receptor, tumor necrosis factor receptor, TNFRSF25, and TNFSF10/TRAIL-receptor, and thus it participates in the death signaling initiated by these receptors. Interaction of this protein with the receptors unmasks the N-terminal effector domain of this protein, which allows …

**Accessions** — [HGNC:3573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3573) · Entrez [8772](https://www.ncbi.nlm.nih.gov/gene/8772) · UniProt [Q13158](https://www.uniprot.org/uniprotkb/Q13158) · Ensembl [ENSG00000168040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168040)

## Data

Gene col 9587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9587); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9587]; `tensor/DDL_lfc|DDL_z.npy` [9587]; `embed/gene_vectors.npy` [9587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9587 or target_col == 9587). Every well: [[FADD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FADD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
