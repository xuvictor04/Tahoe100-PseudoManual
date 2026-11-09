---
symbol: "DPY19L3-DT"
type: "gene"
col: 15534
ensembl_id: "ENSG00000267213"
name: "DPY19L3 divergent transcript"
location: "19q13.11"
module: 15
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DPY19L3-DT

*DPY19L3 divergent transcript* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +8.5, q 1e-14, up in 20 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.394× (z -7.3, q 1e-10, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.500× (z -5.5, q 7e-06, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALY-AS1]] (+0.68, fdr 7e-06), [[GTF3C2-AS2]] (+0.66, fdr 1e-05), [[SMIM15-AS1]] (+0.65, fdr 1e-05); moves opposite to [[TTBK2]] (-0.63, fdr 3e-05), [[CAPN7]] (-0.55, fdr 1e-04), [[LIFR]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +8.5 | 1e-14 | 20/27 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.05×** | +8.0 | 4e-13 | 15/42 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +6.9 | 1e-09 | 1/4 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.6 | 4e-09 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +5.0 | 6e-05 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +4.8 | 2e-04 | 10/22 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.027 | 4/43 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.54×** | +3.4 | 0.044 | 5/40 (H4, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.54×** | +3.4 | 0.044 | 8/35 (HOP62, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.394×** | -7.3 | 1e-10 | 29/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.439×** | -6.5 | 3e-08 | 23/40 (KATO III, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.472×** | -5.9 | 7e-07 | 12/17 (A549, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -5.5 | 7e-06 | 18/40 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.515×** | -5.2 | 2e-05 | 19/39 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.540×** | -4.7 | 3e-04 | 14/38 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.555×** | -4.6 | 3e-04 | 18/39 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.624×** | -3.7 | 0.015 | 15/44 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.620×** | -3.6 | 0.019 | 10/40 (J82, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.650×** | -3.4 | 0.041 | 9/43 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.78 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.73 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0618× (z -10.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Flumatinib (mesylate) (drug)]] 5 µM 0.0637× (z -9.9) |
| [[PANC-1 (line)]] | alt | 5.19 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 1 | — | [[Anastrozole (drug)]] 0.5 µM 0.160× (z -12.3) |
| [[A-172 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.525 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.634 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALY-AS1]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C2-AS2]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.65 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ASB1]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[LENG8-AS1]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.62 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ZNF514]] | +0.62 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CCT6B]] | +0.61 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[NIPBL-DT]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 | same gene group |
| [[CTBP1-DT]] | +0.60 | +0.57 / +0.36 | both halves | 1e-04 | same gene group |
| [[MYADM-AS1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[LINC01134]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTBK2]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CAPN7]] | -0.55 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[LIFR]] | -0.53 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R12B]] | -0.53 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[TAOK3]] | -0.53 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[TENT4B]] | -0.52 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[KMT2C]] | -0.51 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[NR6A1]] | -0.51 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[TTLL7]] | -0.51 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[RALGAPA2]] | -0.50 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[PAFAH1B3]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[KIF13A]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPY19L3-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers DPY19L3-DT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CHST14]] | C | CHST14 activity raises DPY19L3-DT's level | lines that do not express CHST14 (3) vs lines expressing it (47) | 1.26× lower at baseline in the lines without CHST14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DLG4, NECAB2, DMXL2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.0, 20.8); signed map (29.3, -17.4). **Vector** length 47.1, 5.74% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.4 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.11 — chr19:32,390,050-32,405,560 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55307) · Entrez [400684](https://www.ncbi.nlm.nih.gov/gene/400684) · Ensembl [ENSG00000267213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267213)

## Data

Gene col 15534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15534); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15534]; `tensor/DDL_lfc|DDL_z.npy` [15534]; `embed/gene_vectors.npy` [15534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15534 or target_col == 15534). Every well: [[DPY19L3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
