---
symbol: "GGT1"
type: "gene"
col: 1849
ensembl_id: "ENSG00000100031"
name: "gamma-glutamyltransferase 1"
location: "22q11.23"
module: 53
arm: "+"
pooled_cpm: 7.61
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# GGT1

*gamma-glutamyltransferase 1* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +16.6, q 0e+00, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.499× (z -8.6, q 6e-15, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHDH]] (+0.70, fdr 7e-06), [[CPT1C]] (+0.68, fdr 7e-06), [[SELPLG]] (+0.66, fdr 7e-06); moves opposite to [[IDH3A]] (-0.56, fdr 4e-05), [[DCAF16]] (-0.51, fdr 2e-04), [[ABHD13]] (-0.50, fdr 4e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +16.6 | 0e+00 | 26/35 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.51×** | +11.3 | 5e-27 | 30/40 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +9.8 | 2e-20 | 21/35 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +9.0 | 4e-17 | 22/43 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +7.2 | 7e-11 | 18/40 (LS 180, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.4 | 1e-08 | 19/42 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +6.0 | 2e-07 | 18/39 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.4 | 4e-06 | 1/13 (HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.4 | 4e-06 | 11/42 (A498, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 3e-04 | 11/36 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 12/35 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.006 | 6/43 (A498, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.018 | 9/33 (A498, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.019 | 9/40 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.32×** | +3.1 | 0.074 | 3/17 (HepG2/C3A, BT-474, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -8.6 | 6e-15 | 26/43 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -8.0 | 4e-13 | 23/35 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -7.8 | 8e-13 | 27/41 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -7.0 | 3e-10 | 24/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.741×** | -3.7 | 0.023 | 14/41 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.049 | 7/41 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.764×** | -3.3 | 0.067 | 10/28 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.755×** | -3.2 | 0.091 | 7/41 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.760× | -3.1 | 0.10 | 6/42 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.770× | -3.1 | 0.12 | 11/39 (SNU-423, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.783× | -3.0 | 0.12 | 11/43 (CHP-212, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -8.6) |
| [[KATO III (line)]] | alt | 4.79 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0816× (z -10.0) |
| [[A549 (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0916× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 4.41 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0842× (z -8.5) |
| [[LoVo (line)]] | wt | 4.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 5.38 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0638× (z -8.8) |
| [[SW480 (line)]] | alt | 4.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.109× (z -10.3) |
| [[A-427 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDH]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.68 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |
| [[KBTBD11-OT1-1]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[IRAG1-AS1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC4A10]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[C9orf24]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LINC00672]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FAM209A]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[L3MBTL2-AS1]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3A]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DCAF16]] | -0.51 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[ABHD13]] | -0.50 | -0.41 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GGT1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.2, -19.0); signed map (13.2, 15.2). **Vector** length 74.5, 12.7% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,594,811-24,629,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D22S672, D22S732, CD224; previously GGT |
| Gene groups (HGNC) | CD molecules; Gamma-glutamyltransferases; Acyltransferases |
| Reactome | 17 pathways, smallest: Aflatoxin activation and detoxification; Synthesis of Leukotrienes (LT) and Eoxins (EX); Glutathione synthesis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [P19440](https://www.uniprot.org/uniprotkb/P19440) (Glutathione hydrolase 1 proenzyme):

> Cleaves the gamma-glutamyl bond of extracellular glutathione (gamma-Glu-Cys-Gly), glutathione conjugates (such as maresin conjugate (13R)-S-glutathionyl-(14S)-hydroxy-(4Z,7Z,9E,11E,16Z,19Z)-docosahexaenoate, MCTR1) and other gamma-glutamyl compounds (such as leukotriene C4, LTC4). The metabolism of glutathione by GGT1 releases free glutamate and the dipeptide cysteinyl-glycine, which is hydrolyzed to cysteine and glycine by dipeptidases. In the presence of high concentrations of dipeptides and …

**Summary**, from NCBI Gene [2678](https://www.ncbi.nlm.nih.gov/gene/2678):

> The enzyme encoded by this gene is a type I gamma-glutamyltransferase that catalyzes the transfer of the glutamyl moiety of glutathione to a variety of amino acids and dipeptide acceptors. The enzyme is composed of a heavy chain and a light chain, which are derived from a single precursor protein. It is expressed in tissues involved in absorption and secretion and may contribute to the etiology of diabetes and other metabolic disorders. Multiple alternatively spliced variants have been …

**Accessions** — [HGNC:4250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4250) · Entrez [2678](https://www.ncbi.nlm.nih.gov/gene/2678) · UniProt [P19440](https://www.uniprot.org/uniprotkb/P19440) · Ensembl [ENSG00000100031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100031)

## Data

Gene col 1849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1849); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1849]; `tensor/DDL_lfc|DDL_z.npy` [1849]; `embed/gene_vectors.npy` [1849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1849 or target_col == 1849). Every well: [[GGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
