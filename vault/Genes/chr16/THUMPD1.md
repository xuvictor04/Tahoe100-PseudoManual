---
symbol: "THUMPD1"
type: "gene"
col: 835
ensembl_id: "ENSG00000066654"
name: "THUMP domain 1 NAT10 acetyltransferase adaptor"
location: "16p12.3"
module: 11
arm: "+"
pooled_cpm: 45.66
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# THUMPD1

*THUMP domain 1 NAT10 acetyltransferase adaptor* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.69× (z +9.7, q 3e-19, up in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.48× (z +7.5, q 8e-12, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.779× (z -6.7, q 1e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB6]] (+0.74, fdr 7e-06), [[MRFAP1L1]] (+0.72, fdr 7e-06), [[ZNF24]] (+0.70, fdr 7e-06); moves opposite to [[NPTN]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +9.7 | 3e-19 | 39/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +9.2 | 1e-17 | 39/47 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.38×** | +8.6 | 1e-15 | 28/47 (A549, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.54×** | +8.0 | 1e-13 | 32/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.5 | 8e-12 | 40/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +7.2 | 5e-11 | 34/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 2e-08 | 32/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.7 | 9e-07 | 29/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.27×** | +4.5 | 4e-04 | 26/48 (HEC-1-A, SHP-77, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.4 | 6e-04 | 22/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +4.2 | 0.001 | 25/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.008 | 21/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.20× | +3.5 | 0.023 | 16/48 (SHP-77, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.030 | 18/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.040 | 19/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -6.7 | 1e-08 | 28/48 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -6.6 | 1e-08 | 30/48 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.011 | 23/48 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.039 | 21/48 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.4 | 0.075 | 18/48 (A498, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.855× | -3.0 | 0.23 | 18/48 (HS-578T, HCT15, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 85.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.503× (z -8.8) |
| [[HT-29 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.55× (z +9.2) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.7) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A549 (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.0) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[BT-474 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.4) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.633× (z -8.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SHP-77 (line)]] | alt | 46.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.1) |
| [[SNU-1 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 47.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -10.0) |
| [[SW480 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.17× (z +10.1) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB6]] | +0.74 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[ZNF24]] | +0.70 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[ZNF426]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[PHAX]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[RBAK]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[NME6]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.58 | -0.62 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises THUMPD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.2, 7.2); signed map (0.2, -22.0). **Vector** length 101, 24.7% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.7 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Thymol (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.7 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.4 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.3 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | THUMP domain 1 NAT10 acetyltransferase adaptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,702,816-20,742,084 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20274, Tan1 |
| Reactome | 4 pathways, smallest: rRNA modification in the nucleus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXG2](https://www.uniprot.org/uniprotkb/Q9NXG2) (THUMP domain-containing protein 1):

> Functions as a tRNA-binding adapter to mediate NAT10-dependent tRNA acetylation modifying cytidine to N4-acetylcytidine (ac4C).

**Summary**, from NCBI Gene [55623](https://www.ncbi.nlm.nih.gov/gene/55623):

> Enables RNA binding activity. Predicted to be involved in tRNA modification. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23807) · Entrez [55623](https://www.ncbi.nlm.nih.gov/gene/55623) · UniProt [Q9NXG2](https://www.uniprot.org/uniprotkb/Q9NXG2) · Ensembl [ENSG00000066654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066654)

## Data

Gene col 835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 835); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 835]; `tensor/DDL_lfc|DDL_z.npy` [835]; `embed/gene_vectors.npy` [835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 835 or target_col == 835). Every well: [[THUMPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THUMPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
