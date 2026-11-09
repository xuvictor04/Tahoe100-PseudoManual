---
symbol: "RIN1"
type: "gene"
col: 10526
ensembl_id: "ENSG00000174791"
name: "Ras and Rab interactor 1"
location: "11q13.2"
module: 84
arm: "+"
pooled_cpm: 6.71
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# RIN1

*Ras and Rab interactor 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.56× (z +4.2, q 0.012, up in 13 of 30 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~25% of this change.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.313× (z -10.9, q 6e-25, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNN4]] (+0.71, fdr 7e-06), [[CYTH4]] (+0.66, fdr 1e-05), [[GALE]] (+0.66, fdr 1e-05); moves opposite to [[CMPK1]] (-0.57, fdr 3e-05), [[MGST1]] (-0.53, fdr 8e-05), [[RUFY3]] (-0.52, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.56×** | +4.2 | 0.012 | 13/30 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 1.42× | +3.3 | 0.19 | 5/37 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.68× | +3.3 | 0.19 | 7/36 (NCI-H460, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.313×** | -10.9 | 6e-25 | 40/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.387×** | -8.9 | 1e-16 | 34/42 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -7.5 | 2e-11 | 32/43 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -6.6 | 5e-09 | 27/40 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.507×** | -6.0 | 2e-07 | 25/41 (Hs 766T, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -5.8 | 5e-07 | 25/43 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.500×** | -5.8 | 5e-07 | 25/45 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.568×** | -5.3 | 8e-06 | 23/43 (H4, Panc 03.27, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.567×** | -5.1 | 2e-05 | 19/41 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.675×** | -5.1 | 2e-05 | 23/44 (A549, SW 900, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.0 | 4e-05 | 22/39 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -4.9 | 4e-05 | 22/45 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.671×** | -4.6 | 2e-04 | 21/43 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.641×** | -4.2 | 0.001 | 18/44 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.707×** | -4.0 | 0.002 | 15/44 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.002 | 23/44 (NCI-H23, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0906× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 5.22 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0822× (z -8.6) |
| [[SW480 (line)]] | alt | 3.72 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -9.9) |
| [[H4 (line)]] | wt | 8.45 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0613× (z -8.8) |
| [[HOP62 (line)]] | alt | 8.60 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 4.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0447× (z -11.5) |
| [[RKO (line)]] | wt | 8.47 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0553× (z -11.0) |
| [[SW 900 (line)]] | alt | 5.92 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0664× (z -8.6) |
| [[A-172 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNN4]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[CYTH4]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GALE]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PLK3]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RAC2]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EHD1]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[STX1A]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RASA3]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[NTSR1]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.57 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MGST1]] | -0.53 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[RUFY3]] | -0.52 | -0.53 / -0.32 | both halves | 1e-04 |  |
| [[ENAH]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[RCN1]] | -0.52 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[AKR1C1]] | -0.52 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[FUCA2]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[MED28]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SETD7]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RIN1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, -1.4); signed map (-0.2, 43.6). **Vector** length 81.8, 17.0% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -10.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | Ras and Rab interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,330,241-66,336,840 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | VPS9 domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13671](https://www.uniprot.org/uniprotkb/Q13671) (Ras and Rab interactor 1):

> Ras effector protein, which may serve as an inhibitory modulator of neuronal plasticity in aversive memory formation. Can affect Ras signaling at different levels. First, by competing with RAF1 protein for binding to activated Ras. Second, by enhancing signaling from ABL1 and ABL2, which regulate cytoskeletal remodeling. Third, by activating RAB5A, possibly by functioning as a guanine nucleotide exchange factor (GEF) for RAB5A, by exchanging bound GDP for free GTP, and facilitating …

**Summary**, from NCBI Gene [9610](https://www.ncbi.nlm.nih.gov/gene/9610):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in intracellular signal transduction. Predicted to act upstream of or within associative learning; memory; and negative regulation of synaptic plasticity. Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18749) · Entrez [9610](https://www.ncbi.nlm.nih.gov/gene/9610) · UniProt [Q13671](https://www.uniprot.org/uniprotkb/Q13671) · Ensembl [ENSG00000174791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174791)

## Data

Gene col 10526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10526); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10526]; `tensor/DDL_lfc|DDL_z.npy` [10526]; `embed/gene_vectors.npy` [10526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10526 or target_col == 10526). Every well: [[RIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
