---
symbol: "VPS28"
type: "gene"
col: 8396
ensembl_id: "ENSG00000160948"
name: "VPS28 subunit of ESCRT-I"
location: "8q24.3"
module: 12
arm: "+"
pooled_cpm: 11.37
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# VPS28

*VPS28 subunit of ESCRT-I* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +7.1, q 8e-10, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.04× (z +4.3, q 0.003, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.568× (z -8.7, q 1e-15, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW5]] (+0.59, fdr 3e-05), [[RNF166]] (+0.57, fdr 4e-04), [[RCE1]] (+0.57, fdr 1e-05); moves opposite to [[HELLS]] (-0.58, fdr 1e-05), [[EPB41L2]] (-0.56, fdr 2e-05), [[HMGB1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.1 | 8e-10 | 17/21 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.0 | 4e-07 | 24/33 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 5e-04 | 3/48 (RKO, SW 900, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +4.3 | 0.003 | 18/40 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.94×** | +4.0 | 0.008 | 13/43 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.83×** | +3.6 | 0.029 | 17/44 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.79×** | +3.5 | 0.041 | 10/44 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.058 | 15/43 (C32, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.33×** | +3.2 | 0.091 | 8/44 (C-33 A, HepG2/C3A, …) | top dose only | position effect removed |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.091 | 9/45 (A498, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -8.7 | 1e-15 | 34/45 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.618×** | -5.3 | 3e-05 | 29/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.712×** | -5.2 | 3e-05 | 22/44 (LOX-IMVI, SW48, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.626×** | -5.1 | 5e-05 | 27/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.644×** | -4.8 | 2e-04 | 22/47 (PANC-1, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -4.7 | 3e-04 | 24/46 (LOX-IMVI, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -4.3 | 0.002 | 20/46 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.008 | 18/48 (HS-578T, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.702×** | -3.7 | 0.013 | 22/44 (PANC-1, A498, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -3.6 | 0.020 | 20/43 (PANC-1, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.722×** | -3.3 | 0.049 | 15/46 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -3.3 | 0.049 | 18/47 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.742×** | -3.2 | 0.049 | 14/46 (SK-MEL-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.743×** | -3.2 | 0.049 | 4/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.087 | 17/48 (NCI-H2030, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.94 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 5 µM 0.215× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.8) |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0939× (z -10.1) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW5]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RNF166]] | +0.57 | +0.25 / +0.59 | both halves | 4e-04 |  |
| [[RCE1]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PLEKHJ1]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RFNG]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[GFER]] | +0.55 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[NKIRAS2]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[YIF1A]] | +0.54 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[PCGF1]] ⚠ | +0.53 | +0.44 / +0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TMEM167B]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MYG1]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CIAO3]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELLS]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[HMGB1]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[FAM81A]] | -0.54 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[UHRF1]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.53 | -0.32 / -0.64 | both halves | 2e-04 | pathway: HCMV Infection |
| [[RRM2]] | -0.52 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[LMNB1]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MCM3]] | -0.51 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[CLSPN]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[RANBP1]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 | pathway: HIV Infection |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.3, -14.5); signed map (-17.3, -2.2). **Vector** length 50.8, 7.84% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | VPS28 subunit of ESCRT-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,423,601-144,428,563 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CIIA |
| Gene groups (HGNC) | ESCRT-I |
| Hallmark sets | DNA_REPAIR |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK41](https://www.uniprot.org/uniprotkb/Q9UK41) (Vacuolar protein sorting-associated protein 28 homolog):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process.

**Summary**, from NCBI Gene [51160](https://www.ncbi.nlm.nih.gov/gene/51160):

> This gene encodes a protein subunit of the ESCRT-I complex (endosomal complexes required for transport), which functions in the transport and sorting of proteins into subcellular vesicles. This complex can also be hijacked to facilitate the budding of enveloped viruses from the cell membrane. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:18178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18178) · Entrez [51160](https://www.ncbi.nlm.nih.gov/gene/51160) · UniProt [Q9UK41](https://www.uniprot.org/uniprotkb/Q9UK41) · Ensembl [ENSG00000160948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160948)

## Data

Gene col 8396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8396); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8396]; `tensor/DDL_lfc|DDL_z.npy` [8396]; `embed/gene_vectors.npy` [8396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8396 or target_col == 8396). Every well: [[VPS28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
