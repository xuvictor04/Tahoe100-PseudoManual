---
symbol: "ADHFE1"
type: "gene"
col: 7200
ensembl_id: "ENSG00000147576"
name: "alcohol dehydrogenase iron containing 1"
location: "8q13.1"
module: 26
arm: "+"
pooled_cpm: 4.6
n_lines_expressing: 43
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ADHFE1

*alcohol dehydrogenase iron containing 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.67× (z +12.4, q 8e-33, up in 22 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0579×, PANC-1 0.199×; ⚠ cell-cycle shift, explains ~71% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.146×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.199×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0718×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01725]] (+0.53, fdr 1e-04), [[HOXA-AS2]] (+0.52, fdr 1e-04), [[LINC02889]] (+0.52, fdr 3e-04); moves opposite to [[SLC25A11]] (-0.54, fdr 6e-05), [[MEA1]] (-0.50, fdr 2e-05), [[CALM1]] (-0.44, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +12.4 | 8e-33 | 22/30 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.7 | 7e-16 | 1/9 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +8.2 | 4e-14 | 12/31 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +7.6 | 6e-12 | 4/12 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.4 | 2e-08 | 2/17 (HS-578T, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.00×** | +6.2 | 5e-08 | 22/38 (CFPAC-1, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 4e-06 | 10/31 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.0 | 4e-05 | 6/22 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.001 | 14/39 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.0 | 0.004 | 5/33 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.006 | 5/40 (SW48, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.036 | 12/36 (SW480, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.038 | 10/35 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.044 | 7/37 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.00×** | +3.2 | 0.045 | 5/29 (LoVo, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.047 | 10/35 (C32, HEC-1-A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.2 | 0.053 | 6/35 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.060 | 4/35 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +2.9 | 0.092 | 6/38 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.43×** | +2.9 | 0.092 | 5/30 (SK-MEL-2, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7200.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0579×, PANC-1 0.199×; ⚠ cell-cycle shift, explains ~71% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.146×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.199×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0718×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.694× | -3.3 | 0.51 | 17/40 (NCI-H1573, PANC-1, …) | top dose only | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.701× | -3.1 | 0.53 | 8/38 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.36 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0718× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 7.36 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0579× (z -11.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0702× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 4.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +9.4) | — |
| [[A-172 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01725]] | +0.53 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[HOXA-AS2]] | +0.52 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[LINC02889]] | +0.52 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[LINC01208]] | +0.51 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[CP]] | +0.51 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[GRK7]] | +0.50 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[CDH26]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TIMD4]] | +0.50 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[CNTN6]] | +0.49 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[AMY2B]] | +0.49 | +0.55 / +0.32 | both halves | 1e-04 |  |
| [[MAMDC2-AS1]] | +0.49 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[C19orf18]] | +0.49 | +0.52 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A11]] | -0.54 | -0.48 / -0.39 | both halves | 6e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MEA1]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[CALM1]] | -0.44 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[TFB1M]] | -0.44 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[APBB2]] | -0.43 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[WDFY2]] | -0.43 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[DHTKD1]] | -0.42 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[NEDD1]] | -0.42 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[TMEM158]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (16.0, 17.6); signed map (25.8, 1.6). **Vector** length 54.7, 8.62% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +6.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.4 | +2.9 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | alcohol dehydrogenase iron containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,432,492-66,468,907 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32430 |
| Gene groups (HGNC) | Alcohol dehydrogenases |
| Reactome | 2 pathways, smallest: Interconversion of 2-oxoglutarate and 2-hydroxyglutarate; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWW8](https://www.uniprot.org/uniprotkb/Q8IWW8) (Hydroxyacid-oxoacid transhydrogenase, mitochondrial):

> Catalyzes the cofactor-independent reversible oxidation of gamma-hydroxybutyrate (GHB) to succinic semialdehyde (SSA) coupled to reduction of 2-ketoglutarate (2-KG) to D-2-hydroxyglutarate (D-2-HG). D,L-3-hydroxyisobutyrate and L-3-hydroxybutyrate (L-3-OHB) are also substrates for HOT with 10-fold lower activities.

**Summary**, from NCBI Gene [137872](https://www.ncbi.nlm.nih.gov/gene/137872):

> The ADHFE1 gene encodes hydroxyacid-oxoacid transhydrogenase (EC 1.1.99.24), which is responsible for the oxidation of 4-hydroxybutyrate in mammalian tissues (Kardon et al., 2006 [PubMed 16616524]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16354) · Entrez [137872](https://www.ncbi.nlm.nih.gov/gene/137872) · UniProt [Q8IWW8](https://www.uniprot.org/uniprotkb/Q8IWW8) · Ensembl [ENSG00000147576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147576)

## Data

Gene col 7200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7200); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7200]; `tensor/DDL_lfc|DDL_z.npy` [7200]; `embed/gene_vectors.npy` [7200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7200 or target_col == 7200). Every well: [[ADHFE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADHFE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
