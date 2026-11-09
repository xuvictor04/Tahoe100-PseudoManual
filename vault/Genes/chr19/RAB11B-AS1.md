---
symbol: "RAB11B-AS1"
type: "gene"
col: 15622
ensembl_id: "ENSG00000269386"
name: "RAB11B antisense RNA 1"
location: "19p13.2"
module: 95
arm: "+"
pooled_cpm: 7.43
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# RAB11B-AS1

*RAB11B antisense RNA 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +8.4, q 2e-14, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.461× (z -8.7, q 2e-15, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM39]] (+0.59, fdr 1e-05), [[CYTH2]] (+0.57, fdr 1e-05), [[GPAT4-AS1]] (+0.56, fdr 1e-05); moves opposite to [[PIP4K2A]] (-0.52, fdr 3e-05), [[KIF13A]] (-0.51, fdr 4e-05), [[WDFY1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRRG1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.4 | 2e-14 | 25/42 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.6 | 6e-06 | 5/15 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.3 | 0.003 | 7/22 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.014 | 12/44 (A498, A-172, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.32× | +3.1 | 0.22 | 9/43 (HT-29, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.47× | +3.1 | 0.22 | 7/42 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -8.7 | 2e-15 | 32/46 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -8.6 | 2e-15 | 33/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -8.5 | 5e-15 | 28/45 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -7.8 | 7e-13 | 26/40 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.539×** | -6.9 | 5e-10 | 26/46 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -6.9 | 5e-10 | 25/46 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -6.5 | 6e-09 | 26/45 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -6.2 | 4e-08 | 25/37 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -6.1 | 8e-08 | 26/44 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -5.8 | 5e-07 | 21/43 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -4.9 | 4e-05 | 19/46 (H4, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.638×** | -4.8 | 6e-05 | 19/45 (RKO, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -4.7 | 1e-04 | 18/39 (HS-578T, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.469×** | -4.4 | 4e-04 | 17/44 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.682×** | -4.3 | 7e-04 | 16/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.674×** | -4.3 | 7e-04 | 17/45 (H4, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -4.3 | 7e-04 | 16/45 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.506×** | -4.0 | 0.002 | 12/44 (C32, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.687×** | -4.0 | 0.002 | 13/44 (HS-578T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 8 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -12.1) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.199× (z -11.1) |
| [[C32 (line)]] | wt | 22.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.272× (z -9.0) |
| [[H4 (line)]] | wt | 20.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.8) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0956× (z -10.5) |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.123× (z -9.6) |
| [[HS-578T (line)]] | alt | 9.46 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0426× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0998× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 5.04 | 0 | 2 | — | [[Belumosudil (drug)]] 5 µM 0.112× (z -9.2) |
| [[RKO (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -10.3) |
| [[BT-474 (line)]] | alt | 8.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -9.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.114× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.106× (z -8.6) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -8.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 8.19 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0706× (z -10.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0812× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 6.40 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0814× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0950× (z -8.9) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SNU-423 (line)]] | alt | 9.20 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -8.6) |
| [[A-172 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM39]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CYTH2]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GPAT4-AS1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[SP2]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[LINC01138]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ZNF200]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MCL1]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ARMC5]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 | same gene group |
| [[AP4M1]] | +0.52 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[VPS9D1]] | +0.52 | +0.39 / +0.59 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP4K2A]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[KIF13A]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[WDFY1]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[WWP1]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[RFXAP]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NDRG3]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[STX7]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TKT]] | -0.47 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[TRAK1]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[FYCO1]] | -0.47 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[PRRG1]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MCUR1]] ⚠ | -0.46 | -0.41 / -0.43 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ENPP4]] | -0.46 | -0.38 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG1]] | C | PRRG1 activity raises RAB11B-AS1's level | lines that do not express PRRG1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without PRRG1 | 0.078 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.408). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-12.8, 27.9); signed map (1.8, -7.3). **Vector** length 69.9, 11.8% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB11B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.2 — chr19:8,374,372-8,390,685 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MIR4999HG |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44178) · Entrez [100507567](https://www.ncbi.nlm.nih.gov/gene/100507567) · Ensembl [ENSG00000269386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269386)

## Data

Gene col 15622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15622); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15622]; `tensor/DDL_lfc|DDL_z.npy` [15622]; `embed/gene_vectors.npy` [15622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15622 or target_col == 15622). Every well: [[RAB11B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
