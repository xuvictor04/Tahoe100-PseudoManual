---
symbol: "LYSMD4"
type: "gene"
col: 11364
ensembl_id: "ENSG00000183060"
name: "LysM domain containing 4"
location: "15q26.3"
module: 2
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LYSMD4

*LysM domain containing 4* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.02× (z +15.5, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.326× (z -6.5, q 4e-08, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4F]] (+0.60, fdr 3e-05), [[CORO7]] (+0.60, fdr 3e-05), [[CROCCP3]] (+0.59, fdr 1e-05); moves opposite to [[TBCK]] (-0.59, fdr 1e-05), [[ANKRD17]] (-0.58, fdr 5e-05), [[COX18]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLTCL1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.02×** | +15.5 | 0e+00 | 44/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.96×** | +15.3 | 0e+00 | 43/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.89×** | +11.8 | 5e-30 | 40/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.4 | 2e-11 | 20/39 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +6.2 | 5e-08 | 24/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.46×** | +5.3 | 1e-05 | 10/43 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.4 | 1e-03 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.003 | 6/47 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.003 | 10/39 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.005 | 4/45 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 6/46 (RKO, LS 180, …) | top dose only |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.038 | 4/44 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.054 | 7/41 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.091 | 2/46 (NCI-H460, HS-578T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.326×** | -6.5 | 4e-08 | 22/41 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.647×** | -4.9 | 3e-04 | 17/47 (RPMI-7951, HT-29, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.670×** | -4.3 | 0.003 | 9/29 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.708×** | -3.9 | 0.016 | 12/36 (LoVo, J82, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.073 | 13/40 (COLO 205, SHP-77, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -3.4 | 0.073 | 12/34 (NCI-H2030, SHP-77, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.743× | -3.2 | 0.11 | 13/43 (PANC-1, SK-MEL-2, …) | top dose only | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.08 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0850× (z -10.4) |
| [[SW480 (line)]] | alt | 2.79 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.92× (z +9.0) | — |
| [[A498 (line)]] | wt | 3.39 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0665× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 3.51 | 0 | 1 | — | [[Trifluridine (drug)]] 0.05 µM 0.0498× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 3.99 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0661× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0789× (z -8.7) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 4.48 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0801× (z -8.5) |
| [[SHP-77 (line)]] | alt | 6.06 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0719× (z -9.9) |
| [[SW1417 (line)]] | alt | 3.80 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0437× (z -10.8) |
| [[A-172 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4F]] | +0.60 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CORO7]] | +0.60 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CROCCP3]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.59 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SNTA1]] | +0.57 | +0.38 / +0.41 | both halves | 7e-05 |  |
| [[SPRYD3]] | +0.57 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PSMD9]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[DGKQ]] | +0.56 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SERAC1]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ADCK5]] | +0.55 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[KCTD21]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CAPN10]] | +0.54 | +0.48 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD17]] | -0.58 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[COX18]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ANKRD26]] | -0.53 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[MTREX]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[MEIS2]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ZNF638]] | -0.52 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[IKBKE]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[GPHN]] | -0.52 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[PLCH1]] | -0.52 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[RAMP1]] | -0.52 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[RBM23]] | -0.51 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLTCL1]] | C | CLTCL1 activity lowers LYSMD4's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.83× higher at baseline in the lines without CLTCL1 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (1.2, -0.3); signed map (-44.0, -5.1). **Vector** length 45.8, 4.96% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +15.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +15.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +11.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.6 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | +3.1 |

## What is on record

|  |  |
|---|---|
| Name | LysM domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,715,697-99,733,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33008 |
| Gene groups (HGNC) | LysM domain containing |
| Matched by | ensembl_id |

UniProt [Q5XG99](https://www.uniprot.org/uniprotkb/Q5XG99) carries no function annotation.

**Summary**, from NCBI Gene [145748](https://www.ncbi.nlm.nih.gov/gene/145748):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26571) · Entrez [145748](https://www.ncbi.nlm.nih.gov/gene/145748) · UniProt [Q5XG99](https://www.uniprot.org/uniprotkb/Q5XG99) · Ensembl [ENSG00000183060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183060)

## Data

Gene col 11364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11364); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11364]; `tensor/DDL_lfc|DDL_z.npy` [11364]; `embed/gene_vectors.npy` [11364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11364 or target_col == 11364). Every well: [[LYSMD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYSMD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
