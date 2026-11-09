---
symbol: "POLM"
type: "gene"
col: 4363
ensembl_id: "ENSG00000122678"
name: "DNA polymerase mu"
location: "7p13"
module: 12
arm: "+"
pooled_cpm: 8.41
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# POLM

*DNA polymerase mu* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.03× (z +10.7, q 4e-24, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.448× (z -17.2, q 0e+00, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAP29]] (+0.65, fdr 2e-05), [[INIP]] (+0.64, fdr 3e-05), [[TTC38]] (+0.62, fdr 5e-05); moves opposite to [[ATP11C]] (-0.65, fdr 1e-05), [[CDK2AP1]] (-0.63, fdr 5e-05), [[PRDM10]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +10.7 | 4e-24 | 38/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +9.7 | 1e-19 | 34/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +9.2 | 5e-18 | 28/46 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +8.9 | 1e-16 | 35/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +7.8 | 6e-13 | 21/44 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.6 | 0.034 | 9/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.037 | 6/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.045 | 6/47 (H4, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Resveratrol (drug)]] 5 µM |  | 1.16× | +3.3 | 0.070 | 5/48 (SW 900, AsPC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.100 | 9/43 (PANC-1, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.448×** | -17.2 | 0e+00 | 39/44 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -8.2 | 9e-14 | 26/39 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -5.3 | 2e-05 | 19/44 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.722×** | -4.9 | 1e-04 | 18/47 (SW480, HOP62, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -4.9 | 1e-04 | 17/46 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.728×** | -4.8 | 1e-04 | 16/31 (SW480, NCI-H460, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -4.8 | 1e-04 | 19/45 (A-427, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -4.7 | 2e-04 | 18/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.739×** | -4.6 | 3e-04 | 15/47 (J82, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -4.1 | 0.002 | 16/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -3.5 | 0.020 | 16/44 (Hs 766T, H4, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.3 | 0.048 | 16/46 (SK-MEL-2, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0733× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.8) |
| [[PANC-1 (line)]] | alt | 11.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -9.0) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.1) |
| [[A498 (line)]] | wt | 9.13 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 7.50 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0583× (z -9.8) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 7.14 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.124× (z -9.8) |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 1 | — | [[Aliskiren (drug)]] 0.5 µM 0.147× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -9.2) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0863× (z -13.8) |
| [[A-427 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP29]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[INIP]] | +0.64 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TTC38]] | +0.62 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[MTRES1]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[KRI1]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ZBTB48]] | +0.60 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[MAP1S]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SRRD]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GGA1]] | +0.60 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[RING1]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[COG2]] | +0.59 | +0.33 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 | same gene group |
| [[CDK2AP1]] | -0.63 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[PRDM10]] | -0.61 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[METTL4]] | -0.60 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.60 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[C2orf88]] | -0.59 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[SAXO1]] | -0.58 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[LAMTOR5-AS1]] | -0.57 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[STARD4-AS1]] | -0.57 | -0.16 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANP32A]] | -0.57 | -0.43 / -0.54 | both halves | 4e-05 | same gene group |
| [[PXDNL]] | -0.57 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[CCNO-DT]] | -0.57 | -0.16 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[ALG1L9P]] | -0.56 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[SAP30L-AS1]] | -0.55 | -0.29 / -0.34 | both halves | 3e-04 |  |
| [[PRDM6]] | -0.53 | -0.23 / -0.37 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers POLM's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises POLM's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-29.0, -2.2); signed map (-19.5, -9.5). **Vector** length 69.5, 10.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +8.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | -0.0 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -17.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.6 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase mu |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,072,062-44,082,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tdt-N |
| Gene groups (HGNC) | DNA polymerases; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP87](https://www.uniprot.org/uniprotkb/Q9NP87) (DNA-directed DNA/RNA polymerase mu):

> Catalyzes template-directed nucleotide addition during gap filling at DNA double-strand breaks. Functions as a gap-filling polymerase involved in repair of DNA double-strand breaks by non-homologous end joining (NHEJ). Displays reduced sugar discrimination, incorporating deoxyribonucleotides and ribonucleotides with similar efficiency on DNA primer strands, and is able to polymerize nucleotides on RNA-terminated primer strands in vitro. Participates in immunoglobulin (Ig) light chain gene …

**Summary**, from NCBI Gene [27434](https://www.ncbi.nlm.nih.gov/gene/27434):

> Predicted to enable DNA-directed DNA polymerase activity. Predicted to be involved in double-strand break repair via nonhomologous end joining. Predicted to act upstream of or within B cell differentiation and somatic hypermutation of immunoglobulin genes. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9185) · Entrez [27434](https://www.ncbi.nlm.nih.gov/gene/27434) · UniProt [Q9NP87](https://www.uniprot.org/uniprotkb/Q9NP87) · Ensembl [ENSG00000122678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122678)

## Data

Gene col 4363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4363); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4363]; `tensor/DDL_lfc|DDL_z.npy` [4363]; `embed/gene_vectors.npy` [4363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4363 or target_col == 4363). Every well: [[POLM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
