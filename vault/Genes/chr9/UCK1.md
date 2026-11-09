---
symbol: "UCK1"
type: "gene"
col: 5105
ensembl_id: "ENSG00000130717"
name: "uridine-cytidine kinase 1"
location: "9q34.13"
module: 107
arm: "+"
pooled_cpm: 5.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# UCK1

*uridine-cytidine kinase 1* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.99× (z +8.5, q 1e-14, up in 21 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.52× (z +5.5, q 9e-06, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.528× (z -8.4, q 3e-14, down in 24 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.546× (z -7.9, q 6e-13, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF3]] (+0.67, fdr 1e-05), [[DMAP1]] (+0.65, fdr 8e-06), [[HARS2]] (+0.64, fdr 7e-06); moves opposite to [[ATP1B3]] (-0.53, fdr 3e-05), [[PFN1]] (-0.50, fdr 8e-05), [[CLDN11]] (-0.49, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +8.5 | 1e-14 | 21/29 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.2 | 5e-14 | 8/12 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 9e-06 | 18/46 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 4e-04 | 9/41 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.43×** | +4.6 | 4e-04 | 13/27 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.4 | 0.001 | 14/36 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 0.001 | 7/46 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.001 | 9/46 (A498, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.006 | 6/32 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +3.8 | 0.009 | 8/47 (SW480, HEC-1-A, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +3.4 | 0.032 | 6/47 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.3 | 0.038 | 2/43 (Panc 03.27, A498) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.20× | +3.3 | 0.038 | 4/47 (SW 1088, CFPAC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.038 | 0/17 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.095 | 7/46 (HOP62, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -8.4 | 3e-14 | 24/42 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -7.9 | 6e-13 | 32/45 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.605×** | -6.6 | 8e-09 | 21/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -5.5 | 4e-06 | 18/45 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -4.6 | 6e-04 | 10/46 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.016 | 21/45 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 8.69 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -9.0) |
| [[BT-474 (line)]] | alt | 9.76 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0799× (z -8.7) |
| [[HT-29 (line)]] | alt | 5.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0807× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.195× (z -8.6) |
| [[A-172 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF3]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.65 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[HARS2]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[BRMS1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SF3A2]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ASB6]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MYG1]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TSR3]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GFER]] | +0.60 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[NKIRAS2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ESS2]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1B3]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[PFN1]] | -0.50 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[CLDN11]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[FAM81A]] | -0.49 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CALM2]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[IGF2BP3]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[METTL21A]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MYL12A]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises UCK1's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.12× lower at baseline in the lines without ZNF613 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -3.2); signed map (-10.6, -25.7). **Vector** length 50.3, 6.42% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | uridine-cytidine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:131,523,801-131,531,264 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URK1, FLJ12255 |
| Gene groups (HGNC) | Uridine-cytidine kinase family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA47](https://www.uniprot.org/uniprotkb/Q9HA47) (Uridine-cytidine kinase 1):

> Phosphorylates uridine and cytidine to uridine monophosphate and cytidine monophosphate. Does not phosphorylate deoxyribonucleosides or purine ribonucleosides. Can use ATP or GTP as a phosphate donor. Can also phosphorylate cytidine and uridine nucleoside analogs such as 6-azauridine, 5-fluorouridine, 4-thiouridine, 5-bromouridine, N(4)-acetylcytidine, N(4)-benzoylcytidine, 5-fluorocytidine, 2-thiocytidine, 5-methylcytidine, and N(4)-anisoylcytidine.

**Summary**, from NCBI Gene [83549](https://www.ncbi.nlm.nih.gov/gene/83549):

> This gene encodes a uridine-cytidine kinase that catalyzes the phosphorylation of uridine and cytidine to uridine monophosphate (UMP) and cytidine monophosphate (CMP) but not the phosphorylation of deoxyribonucleosides or purine ribonucleosides. This enzyme can also phosphorylate uridine and cytidine analogs and uses both ATP and GTP as a phosphate donor. Alternative splicing results in multiple splice variants encoding distinct isoforms. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:14859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14859) · Entrez [83549](https://www.ncbi.nlm.nih.gov/gene/83549) · UniProt [Q9HA47](https://www.uniprot.org/uniprotkb/Q9HA47) · Ensembl [ENSG00000130717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130717)

## Data

Gene col 5105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5105); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5105]; `tensor/DDL_lfc|DDL_z.npy` [5105]; `embed/gene_vectors.npy` [5105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5105 or target_col == 5105). Every well: [[UCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
