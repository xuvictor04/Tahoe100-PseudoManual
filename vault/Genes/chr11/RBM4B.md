---
symbol: "RBM4B"
type: "gene"
col: 10442
ensembl_id: "ENSG00000173914"
name: "RNA binding motif protein 4B"
location: "11q13.2"
module: 12
arm: "+"
pooled_cpm: 21.91
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RBM4B

*RNA binding motif protein 4B* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.43× (z +7.8, q 3e-12, up in 24 of 43 measured lines) ⚠ toxic.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.639× (z -14.4, q 6e-44, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTC1]] (+0.63, fdr 7e-06), [[DRG1]] (+0.63, fdr 1e-05), [[TEN1]] (+0.61, fdr 7e-06); moves opposite to [[WWC3]] (-0.60, fdr 7e-06), [[DGKH]] (-0.52, fdr 1e-05), [[IGF2BP3]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +7.8 | 3e-12 | 24/43 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.30 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -14.4 | 6e-44 | 33/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.602×** | -11.5 | 4e-28 | 39/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -11.2 | 8e-27 | 34/48 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -11.0 | 4e-26 | 32/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -10.6 | 3e-24 | 29/47 (C-33 A, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -9.8 | 1e-20 | 29/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -9.7 | 2e-20 | 38/48 (NCI-H1792, BT-474, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.670×** | -9.1 | 6e-18 | 31/48 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -8.4 | 2e-15 | 32/47 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -7.9 | 2e-13 | 22/48 (A498, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -6.8 | 6e-10 | 25/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.745×** | -6.7 | 1e-09 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.754×** | -6.4 | 7e-09 | 27/48 (H4, NCI-H661, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.751×** | -6.3 | 2e-08 | 22/47 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.764×** | -6.1 | 4e-08 | 13/41 (CFPAC-1, NCI-H1792, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -6.1 | 4e-08 | 21/47 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.652×** | -5.1 | 1e-05 | 19/47 (SNU-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -4.9 | 2e-05 | 16/48 (KATO III, SHP-77, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -4.9 | 2e-05 | 14/48 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.814×** | -4.5 | 2e-04 | 17/48 (SNU-1, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 22.2 | 0 | 4 (3 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0914× (z -13.2) |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.2) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 36.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.0) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.4) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.351× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[KATO III (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[PANC-1 (line)]] | alt | 29.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -11.0) |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.6) |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -8.6) |
| [[SW48 (line)]] | wt | 20.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0803× (z -11.9) |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTC1]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[DRG1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TEN1]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RINT1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BCAS2]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZNF10]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SUGP1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[VIRMA]] | +0.55 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[CEP76]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SUGT1P3-1]] | +0.54 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[PIGB]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF594-DT]] | +0.54 | +0.31 / +0.69 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WWC3]] | -0.60 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[DGKH]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[IGF2BP3]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 | same gene group |
| [[MYCBP2]] | -0.48 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TEAD1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PRR5L]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SATB2]] | -0.48 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[CHD7]] | -0.47 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[TULP4]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ASXL2]] | -0.46 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[DIAPH1]] | -0.46 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[PKP4]] | -0.46 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBM4B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.6, -12.1); signed map (-12.7, -12.3). **Vector** length 76.1, 13.3% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +2.3 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -11.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -4.6 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -4.5 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,664,998-66,677,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10871, ZCCHC15, RBM4L, ZCRB3B, ZCCHC21B; previously RBM30 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ04](https://www.uniprot.org/uniprotkb/Q9BQ04) (RNA-binding protein 4B):

> Required for the translational activation of PER1 mRNA in response to circadian clock. Binds directly to the 3'-UTR of the PER1 mRNA (By similarity).

**Summary**, from NCBI Gene [83759](https://www.ncbi.nlm.nih.gov/gene/83759):

> Enables RNA binding activity. Predicted to be involved in entrainment of circadian clock by photoperiod and regulation of gene expression. Predicted to act upstream of or within positive regulation of gene expression. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28842) · Entrez [83759](https://www.ncbi.nlm.nih.gov/gene/83759) · UniProt [Q9BQ04](https://www.uniprot.org/uniprotkb/Q9BQ04) · Ensembl [ENSG00000173914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173914)

## Data

Gene col 10442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10442); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10442]; `tensor/DDL_lfc|DDL_z.npy` [10442]; `embed/gene_vectors.npy` [10442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10442 or target_col == 10442). Every well: [[RBM4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
