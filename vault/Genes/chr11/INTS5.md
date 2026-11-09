---
symbol: "INTS5"
type: "gene"
col: 11621
ensembl_id: "ENSG00000185085"
name: "integrator complex subunit 5"
location: "11q12.3"
module: 7
arm: "+"
pooled_cpm: 4.02
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# INTS5

*integrator complex subunit 5* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.08× (z +10.6, q 3e-23, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -6.6, q 3e-08, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf47]] (+0.72, fdr 7e-06), [[ZBTB9]] (+0.67, fdr 7e-06), [[BLOC1S4]] (+0.67, fdr 7e-06); moves opposite to [[RCAN3]] (-0.54, fdr 2e-05), [[SNX3]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.08×** | +10.6 | 3e-23 | 40/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +9.6 | 2e-19 | 38/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.61×** | +9.0 | 4e-17 | 37/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +8.8 | 2e-16 | 19/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.9 | 4e-07 | 19/38 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.83×** | +5.5 | 4e-06 | 2/9 (J82, HOP62) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.4 | 4e-06 | 17/45 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.4 | 6e-04 | 8/22 (KATO III, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.4 | 7e-04 | 8/45 (LOX-IMVI, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.001 | 13/37 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.013 | 9/44 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +3.6 | 0.013 | 9/45 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.043 | 7/42 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.047 | 7/47 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.073 | 7/38 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.087 | 7/45 (NCI-H23, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.087 | 1/40 (SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.087 | 1/45 (NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -6.6 | 3e-08 | 24/44 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -6.4 | 4e-08 | 25/36 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -5.0 | 1e-04 | 20/47 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.9 | 2e-04 | 18/45 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -4.6 | 5e-04 | 15/43 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.615×** | -4.6 | 5e-04 | 13/47 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.618×** | -4.3 | 0.002 | 13/42 (NCI-H23, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.076 | 10/44 (RKO, C-33 A, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.709× | -3.1 | 0.12 | 11/44 (SK-MEL-2, C-33 A, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.722× | -3.1 | 0.13 | 11/46 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.46 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0997× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 7.76 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.143× (z -8.6) |
| [[A498 (line)]] | wt | 2.01 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0592× (z -8.7) |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0792× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0587× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.24 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0602× (z -8.8) |
| [[A-172 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf47]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ZBTB9]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[BLOC1S4]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[RPP14]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | STRING 536 |
| [[PRPF4]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[HPS6]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 | STRING 577 |
| [[KTI12]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ABT1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DDX28]] | +0.64 | +0.71 / +0.60 | both halves | 7e-06 | STRING 436 |
| [[ZSWIM1]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CTDSP1]] | +0.63 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCAN3]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SNX3]] | -0.52 | -0.64 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises INTS5's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.7, -0.2); signed map (-3.3, -21.9). **Vector** length 51.0, 6.60% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,646,848-62,653,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INT5; previously KIAA1698 |
| Gene groups (HGNC) | Integrator complex; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9B9](https://www.uniprot.org/uniprotkb/Q6P9B9) (Integrator complex subunit 5):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [80789](https://www.ncbi.nlm.nih.gov/gene/80789):

> The Integrator complex is a complex that associates with the C-terminal domain of RNA polymerase II large subunit. This complex is brought to U1 and U2 small nuclear RNA genes, where it is involved in the transcription and processing of their transcripts. The protein encoded by this gene represents a subunit of the Integrator complex. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:29352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29352) · Entrez [80789](https://www.ncbi.nlm.nih.gov/gene/80789) · UniProt [Q6P9B9](https://www.uniprot.org/uniprotkb/Q6P9B9) · Ensembl [ENSG00000185085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185085)

## Data

Gene col 11621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11621); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11621]; `tensor/DDL_lfc|DDL_z.npy` [11621]; `embed/gene_vectors.npy` [11621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11621 or target_col == 11621). Every well: [[INTS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
