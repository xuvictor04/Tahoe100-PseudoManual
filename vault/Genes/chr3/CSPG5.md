---
symbol: "CSPG5"
type: "gene"
col: 3570
ensembl_id: "ENSG00000114646"
name: "chondroitin sulfate proteoglycan 5"
location: "3p21.31"
module: 47
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CSPG5

*chondroitin sulfate proteoglycan 5* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +11.5, q 7e-28, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.447× (z -7.9, q 1e-12, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.75, fdr 7e-06), [[CHADL]] (+0.75, fdr 7e-06), [[LINC02236]] (+0.75, fdr 7e-06); moves opposite to [[PEX2]] (-0.62, fdr 8e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC16A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +11.5 | 7e-28 | 22/32 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.1 | 2e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.2 | 9e-08 | 3/13 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +4.8 | 3e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 0.002 | 11/42 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.005 | 11/44 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.07×** | +3.7 | 0.016 | 2/19 (NCI-H2030, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.063 | 3/43 (C32, RPMI-7951, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.2 | 0.075 | 3/44 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.089 | 8/39 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.39× | +3.1 | 0.11 | 5/30 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.447×** | -7.9 | 1e-12 | 22/44 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -7.7 | 3e-12 | 25/42 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -6.3 | 5e-08 | 19/28 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -5.9 | 7e-07 | 17/41 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -5.7 | 2e-06 | 18/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -5.3 | 1e-05 | 19/42 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.587×** | -5.2 | 1e-05 | 19/43 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.424×** | -4.4 | 7e-04 | 11/25 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.657×** | -4.1 | 0.002 | 12/40 (A-427, SNU-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.747×** | -4.1 | 0.003 | 13/40 (BT-474, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -3.6 | 0.017 | 13/39 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -3.3 | 0.053 | 3/44 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -10.3) |
| [[A-172 (line)]] | wt | 5.82 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0937× (z -10.3) |
| [[A549 (line)]] | wt | 2.36 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0390× (z -8.6) |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.129× (z -8.5) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 6.67 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0641× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 1.64 | 0 | 1 | — | [[Folic acid (drug)]] 0.05 µM 0.0533× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -8.7) |
| [[A498 (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.910 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[CHADL]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[AZU1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[KIF17]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PYGM]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[TMEM25]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TTC36]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.62 | -0.63 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises CSPG5's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.40× lower at baseline in the lines without CHD5 | 0.055 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[CHD5]] | B | CHD5 activity strengthens CSPG5's drug response | lines that do not express CHD5 (26) vs lines expressing it (18) | the lines without CHD5 respond 0.64× as strongly (z diff +0.84); strongest at Harringtonine 5 µM: 0.75x vs 0.35x (z diff +2.9) | 0.076 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A1]] | C | CSPG5 activity raises SLC16A1's level | lines that do not express CSPG5 (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without CSPG5 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[MYLK2]] | C | CSPG5 activity raises MYLK2's level | lines that do not express CSPG5 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without CSPG5 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.4, -15.7); signed map (16.8, 13.0). **Vector** length 64.5, 9.65% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate proteoglycan 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,562,238-47,580,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NGC |
| Reactome | 16 pathways, smallest: Defective CHST14 causes EDS, musculocontractural type; Defective CHST3 causes SEDCJD; Defective CHSY1 causes TPBS |
| Matched by | ensembl_id |

**Function**, from UniProt [O95196](https://www.uniprot.org/uniprotkb/O95196) (Chondroitin sulfate proteoglycan 5):

> May function as a growth and differentiation factor involved in neuritogenesis. May induce ERBB3 activation.

**Summary**, from NCBI Gene [10675](https://www.ncbi.nlm.nih.gov/gene/10675):

> The protein encoded by this gene is a proteoglycan that may function as a neural growth and differentiation factor. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:2467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2467) · Entrez [10675](https://www.ncbi.nlm.nih.gov/gene/10675) · UniProt [O95196](https://www.uniprot.org/uniprotkb/O95196) · Ensembl [ENSG00000114646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114646)

## Data

Gene col 3570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3570); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3570]; `tensor/DDL_lfc|DDL_z.npy` [3570]; `embed/gene_vectors.npy` [3570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3570 or target_col == 3570). Every well: [[CSPG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSPG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
