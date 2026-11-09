---
symbol: "CD2BP2"
type: "gene"
col: 9773
ensembl_id: "ENSG00000169217"
name: "CD2 cytoplasmic tail binding protein 2"
location: "16p11.2"
module: 7
arm: "+"
pooled_cpm: 16.4
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CD2BP2

*CD2 cytoplasmic tail binding protein 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.6, q 5e-15, up in 34 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.59× (z +6.8, q 3e-09, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.752× (z -4.2, q 0.015, down in 17 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.758× (z -3.9, q 0.025, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACTIN]] (+0.71, fdr 7e-06), [[SCAF1]] (+0.66, fdr 7e-06), [[MEPCE]] (+0.64, fdr 1e-05); moves opposite to [[ARL3]] (-0.56, fdr 4e-05), [[SKIC3]] (-0.56, fdr 3e-05), [[HSDL2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +8.6 | 5e-15 | 34/43 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.8 | 3e-09 | 32/47 (RKO, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +6.3 | 6e-08 | 28/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +6.1 | 2e-07 | 26/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 2e-07 | 27/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 2e-07 | 26/48 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +5.3 | 7e-06 | 22/47 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 7e-06 | 23/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.7 | 2e-04 | 22/43 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +4.7 | 2e-04 | 23/48 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.6 | 2e-04 | 18/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.5 | 3e-04 | 18/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.36×** | +4.5 | 3e-04 | 18/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.4 | 5e-04 | 16/35 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.002 | 17/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.012 | 13/48 (HS-578T, SNU-423, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.031 | 5/47 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.752×** | -4.2 | 0.015 | 17/47 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.758×** | -3.9 | 0.025 | 22/47 (SNU-423, A-172, …) | top dose only | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.841× | -3.6 | 0.051 | 8/48 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.051 | 5/48 (NCI-H460, NCI-H2030, …) | two highest doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.051 | 6/47 (SW480, HT-29, …) | top dose only | plate-row cell shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -3.4 | 0.053 | 6/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.814× | -3.0 | 0.20 | 10/48 (COLO 205, SW480, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.2 | 10 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.75× (z +14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.85× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.09× (z +10.6) | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -13.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0937× (z -10.8) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.47× (z +10.0) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACTIN]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[EGLN2]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZNF468]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZNF513]] | +0.62 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[TSSC4]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | same gene group; STRING 882 |
| [[SLC66A1]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[EIF2B5]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[FBRS]] | +0.61 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[GRWD1]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SKIC3]] | -0.56 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[HSDL2]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[USP48]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ANAPC5]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R2]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 | same gene group |
| [[LYRM7]] | -0.53 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[ORC4]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[PAPSS1]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DSTN]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.51 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NIPSNAP1]] | -0.50 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.2, -2.4); signed map (1.4, -9.8). **Vector** length 71.1, 12.9% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +8.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | CD2 cytoplasmic tail binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,350,773-30,355,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIN1, Snu40, PPP1R59, U5-52K |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; U5 small nuclear ribonucleoprotein |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [O95400](https://www.uniprot.org/uniprotkb/O95400) (CD2 antigen cytoplasmic tail-binding protein 2):

> Involved in pre-mRNA splicing as component of the U5 snRNP complex that is involved in spliceosome assembly.

**Summary**, from NCBI Gene [10421](https://www.ncbi.nlm.nih.gov/gene/10421):

> This gene encodes a bi-functional protein. In the cytoplasm, the encoded protein binds the cytoplasmic tail of human surface antigen CD2 via its C-terminal GYF domain, and regulate CD2-triggered T lymphocyte activation. In the nucleus, this protein is a component of the U5 small nuclear ribonucleoprotein complex and is involved in RNA splicing. A pseudogene has been identified on chromosome 7. Alternative splicing results in multiple transcript variants but their biological validity has not …

**Accessions** — [HGNC:1656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1656) · Entrez [10421](https://www.ncbi.nlm.nih.gov/gene/10421) · UniProt [O95400](https://www.uniprot.org/uniprotkb/O95400) · Ensembl [ENSG00000169217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169217)

## Data

Gene col 9773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9773); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9773]; `tensor/DDL_lfc|DDL_z.npy` [9773]; `embed/gene_vectors.npy` [9773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9773 or target_col == 9773). Every well: [[CD2BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CD2BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
