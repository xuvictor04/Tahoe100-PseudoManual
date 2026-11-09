---
symbol: "EHHADH"
type: "gene"
col: 3503
ensembl_id: "ENSG00000113790"
name: "enoyl-CoA hydratase and 3-hydroxyacyl CoA dehydrogenase"
location: "3q27.2"
module: 64
arm: "+"
pooled_cpm: 11.88
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# EHHADH

*enoyl-CoA hydratase and 3-hydroxyacyl CoA dehydrogenase* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.65× (z +8.4, q 2e-14, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.335× (z -12.9, q 2e-35, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGT1B]] (+0.69, fdr 1e-05), [[ZNF691]] (+0.67, fdr 7e-06), [[RBM45]] (+0.65, fdr 7e-06); moves opposite to [[KIAA1958]] (-0.54, fdr 1e-04), [[P4HB]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF606]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +8.4 | 2e-14 | 32/46 (SW480, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.7 | 6e-09 | 11/17 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +6.2 | 1e-07 | 27/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.9 | 4e-07 | 8/25 (LS 180, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.5 | 4e-06 | 16/35 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +4.5 | 6e-04 | 16/44 (SW480, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.003 | 20/46 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 15/44 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.0 | 0.005 | 16/36 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.007 | 19/45 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.013 | 14/46 (SW480, A-427, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.028 | 14/46 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.029 | 14/46 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.029 | 11/45 (C32, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.029 | 14/46 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.030 | 13/45 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.068 | 9/46 (SW480, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.077 | 9/47 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.335×** | -12.9 | 2e-35 | 38/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.368×** | -11.8 | 8e-30 | 32/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.415×** | -10.2 | 3e-22 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -8.3 | 1e-14 | 35/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.615×** | -5.7 | 1e-06 | 21/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -5.0 | 5e-05 | 17/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -4.9 | 9e-05 | 24/46 (MIA PaCa-2, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.004 | 12/46 (PANC-1, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -3.9 | 0.005 | 17/46 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.024 | 8/46 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.590×** | -3.3 | 0.057 | 16/40 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.763× | -3.1 | 0.10 | 14/43 (A-172, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0931× (z -18.6) |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.6) |
| [[SW480 (line)]] | alt | 20.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -18.2) |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -8.9) |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -12.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.32 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 9.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0757× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 3.64 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0526× (z -8.9) |
| [[J82 (line)]] | alt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -9.0) |
| [[LoVo (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0498× (z -18.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.00 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0404× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0928× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.79 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -8.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGT1B]] | +0.69 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF691]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[RBM45]] | +0.65 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CCNT2]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[TMEM128]] | +0.64 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[ZNF780A]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH3]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF528]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.61 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[MOB4]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[COPS5]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | -0.54 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[P4HB]] | -0.53 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF606]] | B | ZNF606 activity raises EHHADH's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without ZNF606 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[TMTC2]] | B | TMTC2 activity raises EHHADH's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without TMTC2 | 0.090 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.1, 4.3); signed map (2.6, -27.4). **Vector** length 63.4, 10.4% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.4 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -12.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA hydratase and 3-hydroxyacyl CoA dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,190,624-185,281,990 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ECHD |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Enoyl-CoA hydratases; Oxidoreductases |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Beta-oxidation of very long chain fatty acids; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08426](https://www.uniprot.org/uniprotkb/Q08426) (Peroxisomal bifunctional enzyme):

> Peroxisomal trifunctional enzyme possessing 2-enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, and delta 3, delta 2-enoyl-CoA isomerase activities. Catalyzes two of the four reactions of the long chain fatty acids peroxisomal beta-oxidation pathway (By similarity). Can also use branched-chain fatty acids such as 2-methyl-2E-butenoyl-CoA as a substrate, which is hydrated into (2S,3S)-3-hydroxy-2-methylbutanoyl-CoA (By similarity). Optimal isomerase for 2,5 double bonds into 3,5 form …

**Summary**, from NCBI Gene [1962](https://www.ncbi.nlm.nih.gov/gene/1962):

> The protein encoded by this gene is a bifunctional enzyme and is one of the four enzymes of the peroxisomal beta-oxidation pathway. The N-terminal region of the encoded protein contains enoyl-CoA hydratase activity while the C-terminal region contains 3-hydroxyacyl-CoA dehydrogenase activity. Defects in this gene are a cause of peroxisomal disorders such as Zellweger syndrome. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:3247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3247) · Entrez [1962](https://www.ncbi.nlm.nih.gov/gene/1962) · UniProt [Q08426](https://www.uniprot.org/uniprotkb/Q08426) · Ensembl [ENSG00000113790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113790)

## Data

Gene col 3503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3503); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3503]; `tensor/DDL_lfc|DDL_z.npy` [3503]; `embed/gene_vectors.npy` [3503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3503 or target_col == 3503). Every well: [[EHHADH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHHADH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
