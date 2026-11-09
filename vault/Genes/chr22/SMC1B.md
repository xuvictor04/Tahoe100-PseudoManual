---
symbol: "SMC1B"
type: "gene"
col: 1199
ensembl_id: "ENSG00000077935"
name: "structural maintenance of chromosomes 1B"
location: "22q13.31"
module: 91
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# SMC1B

*structural maintenance of chromosomes 1B* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.04× (z +12.4, q 1e-32, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +8.2, q 3e-14, up in 7 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0640×, PANC-1 0.0822×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.0904×; ⚠ toxic; cell-cycle shift, explains ~58% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (J82 0.127×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMC1]] (+0.65, fdr 7e-06), [[GPR19]] (+0.63, fdr 7e-06), [[C5]] (+0.62, fdr 1e-05); moves opposite to [[ORMDL3]] (-0.45, fdr 4e-04), [[VAT1]] (-0.45, fdr 1e-04).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.04×** | +12.4 | 1e-32 | 2/2 (NCI-H2347, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.92×** | +10.9 | 3e-25 | 6/8 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.71×** | +9.7 | 8e-20 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +8.2 | 3e-14 | 7/22 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.6 | 2e-06 | 9/34 (SW480, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.3 | 0.002 | 1/9 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.71×** | +4.1 | 0.003 | 7/17 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.57×** | +3.9 | 0.006 | 1/4 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 5/25 (NCI-H2347, J82, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.007 | 5/11 (BT-474, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.008 | 7/26 (C-33 A, NCI-H23, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.011 | 6/37 (NCI-H23, NCI-H2030, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +3.5 | 0.019 | 7/30 (SW480, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.031 | 10/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.036 | 4/29 (LoVo, SW480, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.057 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.057 | 7/14 (C32, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.078 | 4/41 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.078 | 1/37 (C32) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.090 | 2/20 (HEC-1-A, NCI-H2347) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1199.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0640×, PANC-1 0.0822×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.0904×; ⚠ toxic; cell-cycle shift, explains ~58% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (J82 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | 0.742× | -3.4 | 0.17 | 9/32 (J82, A549, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.664× | -3.3 | 0.17 | 16/37 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.664× | -3.3 | 0.17 | 9/34 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.672× | -3.2 | 0.17 | 11/38 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.574× | -3.2 | 0.17 | 8/37 (HepG2/C3A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 10.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0640× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.127× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 2.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0822× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.678 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.738 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.648 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.791 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.616 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.809 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.772 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMC1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Meiosis; STRING 496 |
| [[GPR19]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[C5]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[BRCA2]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 | pathway: Meiosis |
| [[DHRS4L2]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HENMT1]] | +0.59 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[HIRIP3]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF724]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[C10orf88B]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[BRME1]] | +0.56 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RAD9B]] | +0.55 | +0.62 / +0.36 | both halves | 1e-04 | STRING 451 |
| [[STOX1]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORMDL3]] | -0.45 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[VAT1]] | -0.45 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMC1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.3, -45.8); signed map (30.8, -30.3). **Vector** length 38.9, 5.17% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +1.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +5.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.7 | -2.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,344,063-45,413,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bK268H5; previously SMC1L2 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; Cohesin complex |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDV3](https://www.uniprot.org/uniprotkb/Q8NDV3) (Structural maintenance of chromosomes protein 1B):

> Meiosis-specific component of cohesin complex. Required for the maintenance of meiotic cohesion, but not, or only to a minor extent, for its establishment. Contributes to axial element (AE) formation and the organization of chromatin loops along the AE. Plays a key role in synapsis, recombination and chromosome movements. The cohesin complex is required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which …

**Summary**, from NCBI Gene [27127](https://www.ncbi.nlm.nih.gov/gene/27127):

> SMC1L2 belongs to a family of proteins required for chromatid cohesion and DNA recombination during meiosis and mitosis (3:Revenkova et al., 2001 [PubMed 11564881]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:11112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11112) · Entrez [27127](https://www.ncbi.nlm.nih.gov/gene/27127) · UniProt [Q8NDV3](https://www.uniprot.org/uniprotkb/Q8NDV3) · Ensembl [ENSG00000077935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077935)

## Data

Gene col 1199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1199); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1199]; `tensor/DDL_lfc|DDL_z.npy` [1199]; `embed/gene_vectors.npy` [1199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1199 or target_col == 1199). Every well: [[SMC1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
