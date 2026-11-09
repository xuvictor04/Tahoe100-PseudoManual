---
symbol: "PRRT3"
type: "gene"
col: 8761
ensembl_id: "ENSG00000163704"
name: "proline rich transmembrane protein 3"
location: "3p25.3"
module: 53
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PRRT3

*proline rich transmembrane protein 3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +16.2, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 0.674× (z -4.4, q 0.005, down in 8 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 5 µM in 1 line (NCI-H2030 0.0641×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW480 0.0715×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0953×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC1P]] (+0.78, fdr 7e-06), [[TMPRSS9]] (+0.73, fdr 7e-06), [[CATSPERD]] (+0.72, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +16.2 | 0e+00 | 29/30 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +12.9 | 1e-35 | 26/36 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +11.1 | 2e-26 | 1/1 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +10.1 | 6e-22 | 22/42 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +9.9 | 4e-21 | 28/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +9.3 | 9e-19 | 28/43 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +8.8 | 1e-16 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.1 | 4e-14 | 9/15 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.8 | 3e-13 | 11/27 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +7.7 | 5e-13 | 19/44 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.4 | 8e-09 | 11/30 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.1 | 6e-08 | 13/44 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.7 | 4e-07 | 6/44 (LoVo, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.6 | 1e-06 | 2/14 (HOP62, A549) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +5.3 | 4e-06 | 14/44 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +5.2 | 6e-06 | 9/39 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.2 | 8e-06 | 9/43 (A-172, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 5e-05 | 11/36 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 10/31 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 5 µM in 1 line (NCI-H2030 0.0641×); [[Decitabine (drug)]] 0.05 µM in 1 line (SW480 0.0715×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0953×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -4.4 | 0.005 | 8/44 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | **0.704×** | -3.9 | 0.023 | 8/44 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.753× | -3.2 | 0.21 | 11/40 (A-172, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 0.758× | -3.1 | 0.21 | 4/43 (SW 900, SHP-77, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.758× | -3.1 | 0.21 | 6/44 (H4, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.47 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0953× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 4.31 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0641× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 5.46 | 0 | 1 | — | [[Erlotinib (drug)]] 0.05 µM 0.0552× (z -8.5) |
| [[SW480 (line)]] | alt | 2.43 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0715× (z -10.0) |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC1P]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.71 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[RELA-DT]] | +0.69 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[FEZ1]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SYT16]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[NEB]] | +0.68 | +0.77 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRRT3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ESRRB]] | B | ESRRB activity raises PRRT3's level | lines that do not express ESRRB (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ESRRB | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02932, DYNLRB2-AS1, ARHGAP15; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises PRRT3's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, -14.5); signed map (21.7, 12.2). **Vector** length 34.4, 2.98% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | proline rich transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,939,450-9,952,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33674 |
| Matched by | ensembl_id |

UniProt [Q5FWE3](https://www.uniprot.org/uniprotkb/Q5FWE3) carries no function annotation.

**Summary**, from NCBI Gene [285368](https://www.ncbi.nlm.nih.gov/gene/285368):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26591) · Entrez [285368](https://www.ncbi.nlm.nih.gov/gene/285368) · UniProt [Q5FWE3](https://www.uniprot.org/uniprotkb/Q5FWE3) · Ensembl [ENSG00000163704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163704)

## Data

Gene col 8761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8761); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8761]; `tensor/DDL_lfc|DDL_z.npy` [8761]; `embed/gene_vectors.npy` [8761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8761 or target_col == 8761). Every well: [[PRRT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
