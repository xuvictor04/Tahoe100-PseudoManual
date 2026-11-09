---
symbol: "PFDN1"
type: "gene"
col: 3428
ensembl_id: "ENSG00000113068"
name: "prefoldin subunit 1"
location: "5q31.3"
module: 7
arm: "+"
pooled_cpm: 73.65
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PFDN1

*prefoldin subunit 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.56× (z +11.3, q 7e-27, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.705× (z -8.0, q 6e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLPH]] (+0.70, fdr 7e-06), [[FBXO38]] (+0.68, fdr 7e-06), [[FRS2]] (+0.67, fdr 8e-06); moves opposite to [[SLC25A40]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.56×** | +11.3 | 7e-27 | 44/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.6 | 1e-08 | 29/48 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.4 | 4e-08 | 36/47 (A498, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 1e-05 | 26/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.2 | 2e-05 | 28/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.8 | 2e-04 | 29/48 (A498, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 22/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.003 | 12/48 (SW1417, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.9 | 0.007 | 13/48 (AsPC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.18× | +3.6 | 0.016 | 17/48 (A498, A549, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.4 | 0.029 | 0/49 | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.051 | 15/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.059 | 20/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.097 | 11/48 (MIA PaCa-2, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -8.0 | 6e-13 | 32/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.709×** | -7.9 | 8e-13 | 36/48 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -7.4 | 3e-11 | 35/48 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.756×** | -6.4 | 2e-08 | 32/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -4.7 | 2e-04 | 15/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.874× | -4.4 | 0.001 | 17/48 (MIA PaCa-2, AsPC-1, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.698×** | -4.3 | 0.001 | 24/49 (LoVo, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.876× | -4.3 | 0.001 | 20/49 (AsPC-1, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.870× | -3.1 | 0.13 | 14/47 (NCI-H460, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.778× | -3.0 | 0.14 | 16/49 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 71.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LS 180 (line)]] | wt | 97.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.456× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 88.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.20× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -8.9) |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 2 (1 ⚠) | — | [[Apalutamide (drug)]] 5 µM 0.101× (z -9.1) |
| [[A498 (line)]] | wt | 51.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 79.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.447× (z -8.6) |
| [[J82 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.8) ⚠ cell-cycle shift, explains ~8% of this change |
| [[KATO III (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 97.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.537× (z -8.8) |
| [[SW480 (line)]] | alt | 79.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.31× (z +11.3) | — |
| [[A-172 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLPH]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[FBXO38]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[FRS2]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[ALKBH1]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[POP4]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[TIMM22]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TACO1]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[C12orf43]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KTI12]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TRMT10C]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DDX28]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A40]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PFDN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.4, 5.3); signed map (-2.7, -24.4). **Vector** length 94.4, 21.9% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +11.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +6.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +3.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | prefoldin subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,245,035-140,303,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PFD1 |
| Gene groups (HGNC) | Prefoldin subunits |
| Reactome | 4 pathways, smallest: Prefoldin mediated transfer of substrate  to CCT/TriC; Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [O60925](https://www.uniprot.org/uniprotkb/O60925) (Prefoldin subunit 1):

> Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins.

**Summary**, from NCBI Gene [5201](https://www.ncbi.nlm.nih.gov/gene/5201):

> This gene encodes a member of the prefoldin beta subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8866) · Entrez [5201](https://www.ncbi.nlm.nih.gov/gene/5201) · UniProt [O60925](https://www.uniprot.org/uniprotkb/O60925) · Ensembl [ENSG00000113068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113068)

## Data

Gene col 3428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3428); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3428]; `tensor/DDL_lfc|DDL_z.npy` [3428]; `embed/gene_vectors.npy` [3428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3428 or target_col == 3428). Every well: [[PFDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
