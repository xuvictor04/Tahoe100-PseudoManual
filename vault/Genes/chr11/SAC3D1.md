---
symbol: "SAC3D1"
type: "gene"
col: 9589
ensembl_id: "ENSG00000168061"
name: "SAC3 domain containing 1"
location: "11q13.1"
module: 54
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SAC3D1

*SAC3 domain containing 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.01× (z +6.9, q 3e-09, up in 21 of 25 measured lines) ⚠ toxic. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.46× (z +3.5, q 0.050, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -5.7, q 5e-06, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP7]] (+0.76, fdr 1e-05), [[LSM2]] (+0.73, fdr 1e-05), [[NR2F6]] (+0.73, fdr 1e-05); moves opposite to [[TRIP12]] (-0.61, fdr 3e-05), [[CCDC200]] (-0.60, fdr 1e-04), [[ZNF655]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.01×** | +6.9 | 3e-09 | 21/25 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.11×** | +4.9 | 3e-04 | 16/26 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.99×** | +4.5 | 0.001 | 23/47 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.89×** | +4.1 | 0.005 | 19/45 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.79×** | +3.8 | 0.018 | 18/44 (KATO III, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.050 | 14/44 (A-427, H4, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.095 | 12/36 (SW480, SW1417, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.62× | +3.0 | 0.18 | 14/42 (SW480, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -5.7 | 5e-06 | 26/38 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -5.2 | 7e-05 | 29/46 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.322×** | -3.9 | 0.021 | 18/35 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -3.7 | 0.037 | 19/45 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -3.5 | 0.045 | 18/40 (NCI-H2030, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | 0.604× | -3.2 | 0.12 | 12/42 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.599× | -3.2 | 0.12 | 18/42 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.622× | -3.1 | 0.13 | 13/36 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.605× | -3.0 | 0.15 | 5/46 (SW 900, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0990× (z -9.5) |
| [[HS-578T (line)]] | alt | 5.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 7.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.7) |
| [[PANC-1 (line)]] | alt | 7.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.0) |
| [[A-172 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 16 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | +0.76 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[LSM2]] | +0.73 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[NR2F6]] | +0.73 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.72 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | +0.72 | +0.51 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS34]] | +0.71 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.70 | +0.41 / +0.80 | both halves | 4e-05 |  |
| [[PET117]] | +0.70 | +0.57 / +0.68 | both halves | 8e-06 |  |
| [[MRPL41]] ⚠ | +0.68 | +0.26 / +0.73 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT8]] | +0.67 | +0.35 / +0.71 | both halves | 1e-04 |  |
| [[C1orf35]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.66 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[ANAPC11]] | +0.66 | +0.37 / +0.70 | both halves | 8e-05 |  |
| [[WRAP73]] | +0.66 | +0.46 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | -0.61 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CCDC200]] | -0.60 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.59 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[CROCC]] | -0.59 | -0.18 / -0.54 | ⚠ one half (not replicated) | 9e-04 |  |
| [[UBE2V1]] | -0.59 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[PEX19]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[TUG1]] | -0.58 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[ALG13]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ZSCAN30]] | -0.58 | -0.32 / -0.53 | both halves | 1e-04 |  |
| [[LINC00641]] | -0.57 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[PRKAR1A]] | -0.57 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[PAPOLA]] | -0.56 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[WSB2]] | -0.56 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SAC3D1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.8, -13.8); signed map (-33.9, 4.4). **Vector** length 65.3, 13.2% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.58 to 9); *Mitochondrial translation* (reactome, mean cos +0.58 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.3 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.1 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.1 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +0.9 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SAC3 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,040,901-65,044,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSU79266, SHD1 |
| Hallmark sets | DNA_REPAIR, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NKF1](https://www.uniprot.org/uniprotkb/A6NKF1) (SAC3 domain-containing protein 1):

> Involved in centrosome duplication and mitotic progression.

**Summary**, from NCBI Gene [29901](https://www.ncbi.nlm.nih.gov/gene/29901):

> Predicted to be involved in centrosome duplication and spindle assembly. Predicted to act upstream of or within negative regulation of receptor signaling pathway via JAK-STAT and regulation of immune response. Predicted to be located in microtubule cytoskeleton. Predicted to be part of protein-containing complex. Predicted to be active in centrosome; nucleus; and spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30179) · Entrez [29901](https://www.ncbi.nlm.nih.gov/gene/29901) · UniProt [A6NKF1](https://www.uniprot.org/uniprotkb/A6NKF1) · Ensembl [ENSG00000168061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168061)

## Data

Gene col 9589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9589); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9589]; `tensor/DDL_lfc|DDL_z.npy` [9589]; `embed/gene_vectors.npy` [9589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9589 or target_col == 9589). Every well: [[SAC3D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAC3D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
