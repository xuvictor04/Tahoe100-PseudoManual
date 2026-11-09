---
symbol: "FLAD1"
type: "gene"
col: 8367
ensembl_id: "ENSG00000160688"
name: "flavin adenine dinucleotide synthetase 1"
location: "1q21.3"
module: 1
arm: "+"
pooled_cpm: 9.38
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FLAD1

*flavin adenine dinucleotide synthetase 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.05× (z +14.0, q 5e-42, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +12.6, q 4e-34, up in 33 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.292×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (C-33 A 0.0937×); [[DT-061 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0701×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT12]] (+0.72, fdr 7e-06), [[TWNK]] (+0.72, fdr 7e-06), [[NIP7]] (+0.69, fdr 7e-06); moves opposite to [[TXNDC16]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.05×** | +14.0 | 5e-42 | 44/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.85×** | +13.2 | 2e-37 | 45/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +12.6 | 4e-34 | 33/43 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.56×** | +11.9 | 3e-30 | 42/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +8.8 | 1e-16 | 29/37 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.09×** | +8.6 | 7e-16 | 18/26 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.83×** | +7.3 | 2e-11 | 6/15 (NCI-H2030, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +7.0 | 2e-10 | 27/45 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +7.0 | 2e-10 | 25/46 (LoVo, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +6.8 | 7e-10 | 26/44 (KATO III, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 1e-09 | 27/42 (CFPAC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.66×** | +6.1 | 4e-08 | 22/44 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.60×** | +5.9 | 2e-07 | 17/33 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.7 | 4e-07 | 24/47 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +5.6 | 7e-07 | 25/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 4e-06 | 22/46 (A-427, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.1 | 1e-05 | 17/48 (A-172, HEC-1-A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.9 | 3e-05 | 16/44 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 3e-05 | 19/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.006 | 4/37 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.007 | 12/45 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.030 | 3/35 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.043 | 5/36 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.292×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (C-33 A 0.0937×); [[DT-061 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0701×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.783× | -3.1 | 0.68 | 13/45 (HEC-1-A, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.292× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0937× (z -9.9) |
| [[Hs 766T (line)]] | wt | 5.59 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0701× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 5.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0918× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT12]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[TWNK]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[NIP7]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[BYSL]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[COMMD5]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CCDC86]] | +0.67 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[EIF6]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[ZNF142]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[DPH2]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TIMM22]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SCO1]] | +0.66 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[PHF5A]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.62 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FLAD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.2, 1.7); signed map (-6.5, -26.2). **Vector** length 57.0, 8.43% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | flavin adenine dinucleotide synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,983,338-154,993,111 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP591, FAD1 |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 3 pathways, smallest: Vitamin B2 (riboflavin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFF5](https://www.uniprot.org/uniprotkb/Q8NFF5) (Bifunctional FAD diphosphatase/FAD synthase):

> This enzyme has two activities: FAD diphosphatase activity and FAD synthase activity. FAD diphosphatase acts on FAD and NADH to produce FMN and NMNH(2-), respectively. FAD synthase catalyzes the adenylation of flavin mononucleotide (FMN) to form flavin adenine dinucleotide (FAD) coenzyme. In addition to its catalytic activities, the protein also facilitates the delivery of FAD to client apo-flavoproteins. The balance between FAD synthesis and hydrolysis may be regulated by redox-sensing …

**Summary**, from NCBI Gene [80308](https://www.ncbi.nlm.nih.gov/gene/80308):

> This gene encodes the enzyme that catalyzes adenylation of flavin mononucleotide (FMN) to form flavin adenine dinucleotide (FAD) coenzyme. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24671) · Entrez [80308](https://www.ncbi.nlm.nih.gov/gene/80308) · UniProt [Q8NFF5](https://www.uniprot.org/uniprotkb/Q8NFF5) · Ensembl [ENSG00000160688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160688)

## Data

Gene col 8367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8367); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8367]; `tensor/DDL_lfc|DDL_z.npy` [8367]; `embed/gene_vectors.npy` [8367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8367 or target_col == 8367). Every well: [[FLAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
