---
symbol: "PRADC1"
type: "gene"
col: 5730
ensembl_id: "ENSG00000135617"
name: "protease associated domain containing 1"
location: "2p13.2"
module: 3
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PRADC1

*protease associated domain containing 1* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.03× (z +17.5, q 0e+00, up in 27 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.0645×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (53 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 48 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA3]] (+0.66, fdr 3e-05), [[GPN3]] (+0.61, fdr 2e-05), [[SIVA1]] (+0.61, fdr 0.002, ⚠ one half only (not replicated)), [[CMC2]] (+0.60, fdr 2e-04); moves opposite to [[EWSR1]] (-0.55, fdr 2e-04), [[HDDC2]] (-0.55, fdr 2e-04), [[RABGGTB]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.03×** | +17.5 | 0e+00 | 27/27 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.60×** | +14.5 | 6e-45 | 39/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **5.81×** | +13.5 | 3e-39 | 37/38 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **5.50×** | +13.1 | 6e-37 | 44/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.27×** | +12.8 | 1e-35 | 22/32 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.14×** | +10.5 | 1e-23 | 3/4 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.49×** | +9.6 | 8e-20 | 9/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.79×** | +7.9 | 3e-13 | 25/28 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +7.4 | 9e-12 | 33/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.49×** | +6.4 | 7e-09 | 1/4 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +6.0 | 9e-08 | 7/10 (HEC-1-A, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.17×** | +5.9 | 2e-07 | 4/10 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.9 | 2e-07 | 10/43 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.01×** | +5.1 | 1e-05 | 18/31 (SW480, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.91×** | +4.8 | 7e-05 | 11/25 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +4.7 | 9e-05 | 8/29 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.81×** | +4.1 | 0.001 | 5/35 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.0645×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.631× | -3.6 | 0.20 | 14/44 (HT-29, A498, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.650× | -3.3 | 0.24 | 9/40 (NCI-H1573, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.77 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 118× (z +19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 66.5× (z +12.0) | — |
| [[C32 (line)]] | wt | 2.03 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 55.6× (z +14.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 2.46 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 1.13 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 147× (z +14.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 3.88 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 2.66 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0645× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 2.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 101× (z +15.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 2.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +10.6) | — |
| [[A-172 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.940 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 39 of them with an alert (⚠; 38 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA3]] | +0.66 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[GPN3]] | +0.61 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[SIVA1]] | +0.61 | +0.11 / +0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[PLA2G15]] | +0.60 | +0.17 / +0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[CMC2]] | +0.60 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[MAP3K3]] | +0.59 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[PMM1]] | +0.58 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[NDUFA2]] | +0.58 | +0.26 / +0.60 | both halves | 4e-04 |  |
| [[CDKN2D]] | +0.57 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ING1]] | +0.56 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[CDK2AP2]] | +0.56 | +0.22 / +0.61 | both halves | 6e-04 |  |
| [[NUDT8]] | +0.56 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[NUDT16L1]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[RNASE4]] | +0.55 | +0.25 / +0.51 | both halves | 4e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.55 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[HDDC2]] | -0.55 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[RABGGTB]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZNF195]] | -0.54 | -0.14 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[RBM41]] | -0.51 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SPIN3]] | -0.50 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[MRRF]] | -0.50 | -0.07 / -0.54 | ⚠ one half (not replicated) | 0.004 |  |
| [[ZNF300]] | -0.49 | -0.03 / -0.52 | ⚠ one half (not replicated) | 0.007 |  |
| [[AMMECR1]] | -0.49 | -0.10 / -0.38 | ⚠ not reproduced | 0.003 |  |
| [[GNL3L]] | -0.49 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[GPATCH4]] | -0.49 | -0.13 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[SHLD1]] | -0.48 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[METAP1D]] | -0.48 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[TRMT11]] | -0.47 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[EIF4B]] | -0.47 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[FECH]] | -0.46 | -0.21 / -0.34 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRADC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.8, -53.5); signed map (-33.9, 15.1). **Vector** length 47.0, 6.48% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +17.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +12.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.5 | +13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +14.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.4 | +13.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.4 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +0.9 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | protease associated domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:73,228,010-73,233,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13004, PAP21, hPAP21; previously C2orf7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSG0](https://www.uniprot.org/uniprotkb/Q9BSG0) (Protease-associated domain-containing protein 1):

> Plays a role in the modulation of physical activity and adiposity.

**Summary**, from NCBI Gene [84279](https://www.ncbi.nlm.nih.gov/gene/84279):

> Located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16047) · Entrez [84279](https://www.ncbi.nlm.nih.gov/gene/84279) · UniProt [Q9BSG0](https://www.uniprot.org/uniprotkb/Q9BSG0) · Ensembl [ENSG00000135617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135617)

## Data

Gene col 5730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5730); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5730]; `tensor/DDL_lfc|DDL_z.npy` [5730]; `embed/gene_vectors.npy` [5730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5730 or target_col == 5730). Every well: [[PRADC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRADC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
