---
symbol: "PSKH1"
type: "gene"
col: 8277
ensembl_id: "ENSG00000159792"
name: "protein serine kinase H1"
location: "16q22.1"
module: 83
arm: "+"
pooled_cpm: 10.64
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PSKH1

*protein serine kinase H1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +8.9, q 2e-16, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.480× (z -8.7, q 2e-15, down in 27 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.641× (z -5.5, q 6e-06, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213-AS1]] (+0.68, fdr 9e-06), [[MAEA]] (+0.66, fdr 1e-05), [[SPRYD4]] (+0.66, fdr 1e-05); moves opposite to [[SH3PXD2B]] (-0.58, fdr 1e-04), [[TPST1]] (-0.56, fdr 3e-05), [[ARHGAP32]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.9 | 2e-16 | 33/44 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.8 | 2e-06 | 20/39 (LOX-IMVI, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.6 | 4e-06 | 21/46 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.7 | 3e-04 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.024 | 12/48 (A498, RKO, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.30× | +3.2 | 0.11 | 4/48 (HT-29, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -8.7 | 2e-15 | 27/40 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.533×** | -7.7 | 3e-12 | 31/45 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.617×** | -5.7 | 2e-06 | 25/46 (Panc 03.27, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -5.5 | 6e-06 | 21/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.654×** | -5.2 | 2e-05 | 22/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -5.2 | 2e-05 | 23/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -5.1 | 3e-05 | 20/48 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.694×** | -4.5 | 5e-04 | 19/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.514×** | -4.3 | 0.001 | 15/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -3.8 | 0.007 | 12/46 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.763×** | -3.3 | 0.044 | 15/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 3 | — | [[TAK-901 (drug)]] 0.05 µM 0.0603× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 7.25 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.118× (z -9.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 9.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 9.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 7.35 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -8.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 6.65 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0823× (z -8.8) |
| [[SW 900 (line)]] | alt | 8.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | +0.68 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[MAEA]] | +0.66 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.66 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.65 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.62 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LINC01134]] | +0.62 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[MAPKAPK5]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[DDX59]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TECPR2]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PDCD6P1]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PPP1R3F]] | +0.61 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[TPST1]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ARHGAP32]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RADX]] | -0.56 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[RBM11]] | -0.55 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CCDC112]] | -0.55 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[USP2]] | -0.54 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[MAPRE2]] | -0.54 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[RAB39A]] | -0.54 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[SOGA3]] | -0.53 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[MLF1]] | -0.53 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[CDC14B]] | -0.53 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSKH1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PSKH1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RAB3IP]] | B | RAB3IP activity lowers PSKH1's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.20× higher at baseline in the lines without RAB3IP | 0.067 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers PSKH1's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.7, 18.6); signed map (28.5, -19.6). **Vector** length 58.4, 8.23% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | protein serine kinase H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,893,254-67,929,676 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein serine kinase H family |
| Matched by | ensembl_id |

**Function**, from UniProt [P11801](https://www.uniprot.org/uniprotkb/P11801) (Serine/threonine-protein kinase H1):

> Serine/threonine protein kinase that may be involved in the regulation of pre-mRNA processing. It may phosphorylate components of nuclear splice factor compartments (SFC), such as non-snRNP splicing factors containing a serine/arginine-rich domain (SR proteins). Reversible phosphorylation of SR proteins may cause their release into the nucleoplasm and change their local concentration, thereby influencing alternative splicing.

**Summary**, from NCBI Gene [5681](https://www.ncbi.nlm.nih.gov/gene/5681):

> Enables protein serine/threonine kinase activity. Predicted to act upstream of or within determination of left/right symmetry; heart development; and protein phosphorylation. Located in cytosol; nuclear speck; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9529) · Entrez [5681](https://www.ncbi.nlm.nih.gov/gene/5681) · UniProt [P11801](https://www.uniprot.org/uniprotkb/P11801) · Ensembl [ENSG00000159792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159792)

## Data

Gene col 8277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8277); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8277]; `tensor/DDL_lfc|DDL_z.npy` [8277]; `embed/gene_vectors.npy` [8277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8277 or target_col == 8277). Every well: [[PSKH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSKH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
