---
symbol: "INTS1"
type: "gene"
col: 9019
ensembl_id: "ENSG00000164880"
name: "integrator complex subunit 1"
location: "7p22.3"
module: 2
arm: "+"
pooled_cpm: 53.59
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# INTS1

*integrator complex subunit 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.00× (z +11.6, q 1e-28, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.681× (z -6.2, q 4e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.74, fdr 7e-06), [[SBF1]] (+0.73, fdr 7e-06), [[CHID1]] (+0.72, fdr 7e-06); moves opposite to [[RPP25L]] (-0.64, fdr 1e-05), [[MPLKIP]] (-0.63, fdr 7e-06), [[PLEKHF2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +11.6 | 1e-28 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +11.6 | 1e-28 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +9.0 | 3e-17 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.5 | 8e-09 | 29/48 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.5 | 1e-08 | 27/42 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.32×** | +4.3 | 0.001 | 22/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.29×** | +4.3 | 0.002 | 24/48 (PANC-1, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.020 | 20/48 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.681×** | -6.2 | 4e-07 | 29/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 3e-04 | 24/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -3.7 | 0.035 | 24/47 (COLO 205, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.6 | 0.035 | 20/49 (NCI-H23, A498, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.6 | 0.035 | 19/48 (NCI-H2347, H4, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.861× | -3.5 | 0.035 | 20/48 (NCI-H2030, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.035 | 18/46 (RKO, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.048 | 19/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.821×** | -3.2 | 0.083 | 22/48 (NCI-H2030, RPMI-7951, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.9 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +15.0) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 2.77× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 42.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 1 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.50× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.292× (z -11.2) |
| [[LoVo (line)]] | wt | 40.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 76.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.325× (z -9.7) |
| [[SW480 (line)]] | alt | 46.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +11.8) | — |
| [[KATO III (line)]] | alt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 51.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +8.6) | — |
| [[H4 (line)]] | wt | 78.2 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.111× (z -8.9) |
| [[HOP62 (line)]] | alt | 34.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +9.6) | — |
| [[RKO (line)]] | wt | 47.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -10.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0632× (z -9.0) |
| [[A-172 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 | STRING 793 |
| [[SBF1]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CHID1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[EPN1]] | +0.69 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.68 | +0.62 / +0.58 | both halves | 7e-06 | STRING 697 |
| [[INTS11]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 | same gene group; pathway: RNA polymerase II transcribes snRNA genes; STRING 999 |
| [[NOMO1]] | +0.67 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[AKT1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MPLKIP]] | -0.63 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[PLEKHF2]] | -0.62 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PBDC1]] | -0.61 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[FDX2]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ZNF330]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[KIAA1586]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PIGP]] | -0.58 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[NNT-AS1]] | -0.57 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ARL14EP]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[HOXA10-AS]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers INTS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.3, -23.2); signed map (-45.5, -11.1). **Vector** length 113, 28.0% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +9.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Pentoxifylline (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -0.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.3 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -0.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,470,277-1,504,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586J0619, KIAA1440, INT1, NET28 |
| Gene groups (HGNC) | Integrator complex; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N201](https://www.uniprot.org/uniprotkb/Q8N201) (Integrator complex subunit 1):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [26173](https://www.ncbi.nlm.nih.gov/gene/26173):

> INTS1 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24555) · Entrez [26173](https://www.ncbi.nlm.nih.gov/gene/26173) · UniProt [Q8N201](https://www.uniprot.org/uniprotkb/Q8N201) · Ensembl [ENSG00000164880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164880)

## Data

Gene col 9019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9019); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9019]; `tensor/DDL_lfc|DDL_z.npy` [9019]; `embed/gene_vectors.npy` [9019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9019 or target_col == 9019). Every well: [[INTS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
