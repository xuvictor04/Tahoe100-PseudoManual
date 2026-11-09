---
symbol: "FILIP1"
type: "gene"
col: 3986
ensembl_id: "ENSG00000118407"
name: "filamin A interacting protein 1"
location: "6q14.1"
module: 140
arm: "+"
pooled_cpm: 6.88
n_lines_expressing: 38
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# FILIP1

*filamin A interacting protein 1* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.39× (z +22.5, q 0e+00, up in 24 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A549 0.0562×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A549 0.0746×; ⚠ cell-cycle shift, explains ~34% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0828×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01579]] (+0.73, fdr 7e-06), [[DPYD-AS1]] (+0.71, fdr 7e-06), [[CTDSPL2-DT]] (+0.68, fdr 1e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.39×** | +22.5 | 0e+00 | 24/28 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +11.0 | 1e-25 | 8/12 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +9.7 | 5e-20 | 17/29 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.32×** | +9.1 | 1e-17 | 14/22 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +9.1 | 1e-17 | 1/5 (A498) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +8.3 | 1e-14 | 2/7 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +7.3 | 3e-11 | 20/31 (SW480, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +6.3 | 2e-08 | 15/28 (LOX-IMVI, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.17×** | +6.1 | 5e-08 | 17/32 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.0 | 9e-08 | 11/34 (A-172, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +4.9 | 5e-05 | 11/34 (KATO III, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.77×** | +4.2 | 0.001 | 2/6 (KATO III, SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.68×** | +4.1 | 0.002 | 7/23 (C32, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.0 | 0.002 | 5/17 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.002 | 9/27 (SK-MEL-2, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.015 | 15/34 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.079 | 7/31 (LoVo, NCI-H23, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +2.9 | 0.095 | 3/14 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A549 0.0562×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A549 0.0746×; ⚠ cell-cycle shift, explains ~34% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0828×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.640× | -3.6 | 0.13 | 3/34 (AN3 CA, A498, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.879× | -3.5 | 0.13 | 18/35 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.637× | -3.2 | 0.22 | 3/34 (J82, HT-29, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.675× | -3.2 | 0.22 | 4/34 (NCI-H2030, AN3 CA, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 46.5 | 0 | 5 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0562× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 202 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.12× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.79× (z +11.9) | — |
| [[KATO III (line)]] | alt | 10.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.50× (z +9.7) | — |
| [[A498 (line)]] | wt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.2) | — |
| [[LoVo (line)]] | wt | 1.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 99.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0828× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 2.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01579]] | +0.73 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[DPYD-AS1]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.68 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EAF1-AS1]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.66 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[A2ML1-AS1]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SCHLAP1]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.64 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[RBFOX3]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.64 | +0.52 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FILIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.3, 27.6); signed map (33.2, 8.8). **Vector** length 49.0, 7.62% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +22.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | filamin A interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:75,291,859-75,493,800 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FILIP, KIAA1275 |
| Reactome | 4 pathways, smallest: RHOD GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7B0](https://www.uniprot.org/uniprotkb/Q7Z7B0) (Filamin-A-interacting protein 1):

> By acting through a filamin-A/F-actin axis, it controls the start of neocortical cell migration from the ventricular zone. May be able to induce the degradation of filamin-A.

**Summary**, from NCBI Gene [27145](https://www.ncbi.nlm.nih.gov/gene/27145):

> This gene encodes a filamin A binding protein. The encoded protein promotes the degradation of filamin A and may regulate cortical neuron migration and dendritic spine morphology. Mice lacking a functional copy of this gene exhibit reduced dendritic spine length and altered excitatory signaling. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:21015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21015) · Entrez [27145](https://www.ncbi.nlm.nih.gov/gene/27145) · UniProt [Q7Z7B0](https://www.uniprot.org/uniprotkb/Q7Z7B0) · Ensembl [ENSG00000118407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118407)

## Data

Gene col 3986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3986); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3986]; `tensor/DDL_lfc|DDL_z.npy` [3986]; `embed/gene_vectors.npy` [3986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3986 or target_col == 3986). Every well: [[FILIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FILIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
