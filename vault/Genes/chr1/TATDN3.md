---
symbol: "TATDN3"
type: "gene"
col: 12778
ensembl_id: "ENSG00000203705"
name: "TatD DNase domain containing 3"
location: "1q32.3"
module: 94
arm: "+"
pooled_cpm: 13.51
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# TATDN3

*TatD DNase domain containing 3* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.93× (z +11.9, q 1e-29, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.634× (z -5.6, q 1e-05, down in 19 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.673× (z -5.1, q 1e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD3]] (+0.73, fdr 7e-06), [[MORN4]] (+0.71, fdr 7e-06), [[DUSP15]] (+0.69, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.57, fdr 1e-05), [[G6PD]] (-0.57, fdr 2e-05), [[ZDHHC11]] (-0.56, fdr 4e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FRG1FP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +11.9 | 1e-29 | 38/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.84×** | +7.8 | 2e-12 | 39/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.76×** | +7.2 | 1e-10 | 33/47 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.66×** | +6.5 | 1e-08 | 31/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.0 | 2e-07 | 27/43 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.0 | 5e-05 | 17/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.0 | 5e-05 | 23/46 (RKO, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.004 | 14/47 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.007 | 17/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +3.5 | 0.025 | 10/47 (PANC-1, A549, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.025 | 11/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.20× | +3.2 | 0.068 | 16/46 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.092 | 10/48 (HepG2/C3A, A-172, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.092 | 8/47 (LoVo, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -5.6 | 1e-05 | 19/42 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -5.1 | 1e-04 | 20/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -4.6 | 7e-04 | 22/48 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.506×** | -4.6 | 7e-04 | 20/45 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.3 | 0.002 | 20/47 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.785× | -3.1 | 0.15 | 14/47 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.786× | -3.1 | 0.15 | 14/47 (SK-MEL-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.43× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.344× (z -9.0) ⚠ toxic |
| [[RKO (line)]] | wt | 13.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -11.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.223× (z -8.7) |
| [[KATO III (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 9.31 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MORN4]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[DUSP15]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SLC16A14]] | +0.66 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[KLHL12]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ZNF44]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[KCTD18]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[ZNF433]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[ZNF627]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[G6PD]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ZDHHC11]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[DNAH1]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[SCART1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC25A10]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[MYLK2]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SNRPA]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1FP]] | B | FRG1FP activity raises TATDN3's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without FRG1FP | 0.025 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[ZNF571]] | B | ZNF571 activity raises TATDN3's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without ZNF571 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[CLSTN3]] | C | CLSTN3 activity strengthens TATDN3's drug response | lines that do not express CLSTN3 (3) vs lines expressing it (45) | the lines without CLSTN3 respond 0.40× as strongly (z diff +1.56); strongest at Homoharringtonine 5 µM: 0.63x vs 1.35x (z diff +5.9) | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782; target measured in part of the lines; artifact flags |
| [[DCP1B]] | C | DCP1B activity raises TATDN3's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.0, 22.3); signed map (-15.3, -13.9). **Vector** length 94.8, 21.1% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.1 | +11.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.2 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.0 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.0 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.9 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.8 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TatD DNase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,791,828-212,816,830 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17R31](https://www.uniprot.org/uniprotkb/Q17R31) (Deoxyribonuclease TATDN3):

> Exhibits 3'-exonuclease and apurinic/apyrimidinic (AP) endonuclease activities (in vitro). Show preferential AP endonuclease activity on double-stranded DNA substrates and 3'- exonuclease activity on single-stranded DNA.

**Summary**, from NCBI Gene [128387](https://www.ncbi.nlm.nih.gov/gene/128387):

> Enables DNA-(apurinic or apyrimidinic site) endonuclease activity and single-stranded DNA 3'-5' DNA exonuclease activity. Predicted to be involved in DNA metabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27010) · Entrez [128387](https://www.ncbi.nlm.nih.gov/gene/128387) · UniProt [Q17R31](https://www.uniprot.org/uniprotkb/Q17R31) · Ensembl [ENSG00000203705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203705)

## Data

Gene col 12778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12778); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12778]; `tensor/DDL_lfc|DDL_z.npy` [12778]; `embed/gene_vectors.npy` [12778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12778 or target_col == 12778). Every well: [[TATDN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TATDN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
