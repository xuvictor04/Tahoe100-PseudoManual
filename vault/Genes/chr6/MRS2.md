---
symbol: "MRS2"
type: "gene"
col: 4537
ensembl_id: "ENSG00000124532"
name: "magnesium transporter MRS2"
location: "6p22.3"
module: 65
arm: "+"
pooled_cpm: 22.54
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MRS2

*magnesium transporter MRS2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.01× (z +11.3, q 1e-26, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.721× (z -5.3, q 7e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1C]] (+0.75, fdr 7e-06), [[MINDY3]] (+0.73, fdr 7e-06), [[ADH5]] (+0.72, fdr 7e-06); moves opposite to [[DPH1-AS1]] (-0.63, fdr 7e-06), [[TUT7]] (-0.62, fdr 8e-06), [[RBBP6]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC44A2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +11.3 | 1e-26 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +9.5 | 4e-19 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +9.4 | 9e-19 | 37/48 (C32, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +7.9 | 3e-13 | 35/47 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 6e-07 | 26/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 9e-05 | 21/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +4.5 | 6e-04 | 15/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 8e-04 | 18/47 (SNU-423, A-172, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.4 | 8e-04 | 17/48 (NCI-H2030, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.002 | 14/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.0 | 0.003 | 8/48 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.30×** | +4.0 | 0.003 | 14/44 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.0 | 0.003 | 19/44 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 11/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.014 | 9/28 (HS-578T, A549, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.029 | 12/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.038 | 14/48 (C32, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.040 | 18/48 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.090 | 12/47 (SNU-423, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -5.3 | 7e-05 | 25/47 (CFPAC-1, SW 900, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.8 | 4e-04 | 25/48 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.747×** | -4.7 | 5e-04 | 20/47 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 0.002 | 19/47 (RKO, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.816× | -3.3 | 0.12 | 13/47 (AsPC-1, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.869× | -3.2 | 0.13 | 21/47 (RPMI-7951, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.825× | -3.1 | 0.15 | 19/48 (SW 900, HT-29, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0907× (z -9.3) |
| [[J82 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) ⚠ cell-cycle shift, explains ~85% of this change |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -10.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.139× (z -9.1) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1C]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ADH5]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RPP30]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.70 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[EXD2]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.69 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[NDFIP1]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[SACM1L]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH1-AS1]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TUT7]] | -0.62 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[RBBP6]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[NFATC1]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[IER5]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.59 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[INTS6]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.58 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A2]] | C | SLC44A2 activity raises MRS2's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without SLC44A2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.8, -10.9); signed map (-31.6, -14.6). **Vector** length 101, 23.7% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.5 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -4.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.9 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | magnesium transporter MRS2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,402,908-24,426,194 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MRS2L |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD23](https://www.uniprot.org/uniprotkb/Q9HD23) (Magnesium transporter MRS2 homolog, mitochondrial):

> Magnesium transporter that mediates the influx of magnesium into the mitochondrial matrix and regulates magnesium metabolism. Also permeable to calcium, sodium and potassium ions. Required for normal expression of the mitochondrial respiratory complex I subunits. May play a role in maintaining the inner mitochondrial membrane potential.

**Summary**, from NCBI Gene [57380](https://www.ncbi.nlm.nih.gov/gene/57380):

> Enables magnesium ion transmembrane transporter activity. Involved in mitochondrial magnesium ion transmembrane transport. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13785) · Entrez [57380](https://www.ncbi.nlm.nih.gov/gene/57380) · UniProt [Q9HD23](https://www.uniprot.org/uniprotkb/Q9HD23) · Ensembl [ENSG00000124532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124532)

## Data

Gene col 4537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4537); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4537]; `tensor/DDL_lfc|DDL_z.npy` [4537]; `embed/gene_vectors.npy` [4537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4537 or target_col == 4537). Every well: [[MRS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
