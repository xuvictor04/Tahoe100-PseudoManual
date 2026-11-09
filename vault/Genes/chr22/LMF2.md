---
symbol: "LMF2"
type: "gene"
col: 1905
ensembl_id: "ENSG00000100258"
name: "lipase maturation factor 2"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 6.52
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LMF2

*lipase maturation factor 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.05× (z +14.5, q 7e-45, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.67× (z +4.9, q 6e-05, up in 10 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.658× (z -8.0, q 7e-13, down in 25 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGA]] (+0.69, fdr 1e-05), [[MAN2B2]] (+0.67, fdr 1e-05), [[HECTD3]] (+0.66, fdr 1e-05); moves opposite to [[PRPF38B]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +14.5 | 7e-45 | 10/10 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.54×** | +12.6 | 8e-34 | 27/31 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +11.3 | 3e-27 | 12/17 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.84×** | +8.3 | 2e-14 | 28/47 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.76×** | +7.7 | 2e-12 | 25/46 (KATO III, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.47×** | +5.2 | 2e-05 | 17/47 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +4.9 | 6e-05 | 10/34 (HOP62, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.42×** | +4.5 | 5e-04 | 11/32 (Panc 03.27, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.25×** | +4.3 | 0.001 | 16/42 (LS 180, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +4.0 | 0.004 | 12/37 (LS 180, SNU-423, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.8 | 0.006 | 13/38 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.029 | 4/42 (HS-578T, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.29×** | +3.3 | 0.043 | 8/39 (LS 180, A498, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.2 | 0.057 | 3/17 (A-172, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.061 | 6/42 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.069 | 2/43 (HS-578T, RPMI-7951) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.092 | 4/43 (CFPAC-1, SHP-77, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -8.0 | 7e-13 | 25/40 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.632×** | -6.0 | 7e-07 | 23/43 (J82, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -5.5 | 7e-06 | 20/47 (Hs 766T, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.759×** | -3.7 | 0.026 | 14/45 (HCT15, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.026 | 17/45 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.769×** | -3.6 | 0.035 | 14/40 (HS-578T, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.787×** | -3.2 | 0.090 | 10/45 (SW1417, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.090 | 9/46 (HCT15, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clotrimazole (drug)]] 0.05 µM |  | **0.791×** | -3.2 | 0.090 | 4/44 (Hs 766T, BT-474, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -3.2 | 0.090 | 7/46 (LoVo, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 7.90 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0791× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[Hs 766T (line)]] | wt | 9.20 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.136× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0714× (z -11.0) |
| [[J82 (line)]] | alt | 8.85 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.124× (z -10.4) |
| [[KATO III (line)]] | alt | 7.29 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.97× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SHP-77 (line)]] | alt | 6.92 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0914× (z -9.1) |
| [[A-172 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGA]] | +0.69 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RUSC1]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CRAT]] | +0.63 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[MED25]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZDHHC16]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NCAPH2]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 | STRING 698; ⚠ same locus (0.5 kb: neighbours can correlate without regulation) |
| [[ACD]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |
| [[GUCD1]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TESK1]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF38B]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.9, -21.2); signed map (-47.5, -11.3). **Vector** length 58.2, 8.31% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.9 | +8.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +4.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.1 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lipase maturation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,502,949-50,507,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM153, TMEM112B |
| Reactome | 4 pathways, smallest: Assembly of active LPL and LIPC lipase complexes; Plasma lipoprotein remodeling; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU23](https://www.uniprot.org/uniprotkb/Q9BU23) (Lipase maturation factor 2):

> Involved in the maturation of specific proteins in the endoplasmic reticulum. May be required for maturation and transport of active lipoprotein lipase (LPL) through the secretory pathway (By similarity).

**Summary**, from NCBI Gene [91289](https://www.ncbi.nlm.nih.gov/gene/91289):

> Predicted to be involved in protein maturation. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25096) · Entrez [91289](https://www.ncbi.nlm.nih.gov/gene/91289) · UniProt [Q9BU23](https://www.uniprot.org/uniprotkb/Q9BU23) · Ensembl [ENSG00000100258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100258)

## Data

Gene col 1905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1905); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1905]; `tensor/DDL_lfc|DDL_z.npy` [1905]; `embed/gene_vectors.npy` [1905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1905 or target_col == 1905). Every well: [[LMF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
