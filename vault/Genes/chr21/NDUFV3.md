---
symbol: "NDUFV3"
type: "gene"
col: 8314
ensembl_id: "ENSG00000160194"
name: "NADH:ubiquinone oxidoreductase subunit V3"
location: "21q22.3"
module: 12
arm: "+"
pooled_cpm: 29.41
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NDUFV3

*NADH:ubiquinone oxidoreductase subunit V3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.09× (z +11.2, q 2e-26, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.350× (z -8.4, q 3e-14, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBY1]] (+0.70, fdr 7e-06), [[MRPL2]] (+0.63, fdr 7e-06), [[AARSD1]] (+0.62, fdr 1e-05); moves opposite to [[YWHAQ]] (-0.52, fdr 1e-05), [[EPB41L2]] (-0.51, fdr 4e-05), [[GGH]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GGH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +11.2 | 2e-26 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +10.2 | 9e-22 | 44/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +8.9 | 2e-16 | 42/48 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.3 | 4e-08 | 35/46 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.7 | 1e-06 | 2/48 (Hs 766T, NCI-H1792) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.2 | 2e-05 | 24/47 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.40×** | +5.1 | 3e-05 | 23/44 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 26/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.22×** | +4.2 | 0.001 | 23/48 (A-427, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.009 | 21/48 (NCI-H2030, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.030 | 20/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.25×** | +3.2 | 0.055 | 18/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +3.2 | 0.064 | 7/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.088 | 17/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.088 | 9/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.093 | 13/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -8.4 | 3e-14 | 40/48 (SK-MEL-2, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -7.2 | 2e-10 | 37/47 (HS-578T, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.698×** | -5.5 | 6e-06 | 25/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -5.5 | 6e-06 | 30/48 (LoVo, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -4.9 | 1e-04 | 24/46 (HOP62, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -4.4 | 9e-04 | 19/48 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 28.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0592× (z -10.2) |
| [[SW480 (line)]] | alt | 43.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +9.3) | — |
| [[A-427 (line)]] | wt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 30.4 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0823× (z -9.6) |
| [[COLO 205 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[RKO (line)]] | wt | 35.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.131× (z -13.9) |
| [[A-172 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBY1]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MRPL2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[AARSD1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[YIF1A]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[KLHL12]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZCCHC9]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NEMF]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DCAF10]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[UFL1]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MTRES1]] | +0.57 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TMEM260]] | +0.57 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAQ]] | -0.52 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[GGH]] | -0.50 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[RBBP7]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[FOXM1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGH]] | B | GGH activity raises NDUFV3's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without GGH | 0.098 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.1, -10.5); signed map (-12.9, -6.2). **Vector** length 74.3, 14.7% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +3.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit V3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,879,644-42,913,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-10k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P56181](https://www.uniprot.org/uniprotkb/P56181) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. May be the terminally assembled subunit of Complex I.

**Summary**, from NCBI Gene [4731](https://www.ncbi.nlm.nih.gov/gene/4731):

> The protein encoded by this gene is one of at least forty-one subunits that make up the NADH-ubiquinone oxidoreductase complex. This complex is part of the mitochondrial respiratory chain and serves to catalyze the rotenone-sensitive oxidation of NADH and the reduction of ubiquinone. The encoded protein is one of three proteins found in the flavoprotein fraction of the complex. The specific function of the encoded protein is unknown. Two transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:7719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7719) · Entrez [4731](https://www.ncbi.nlm.nih.gov/gene/4731) · UniProt [P56181](https://www.uniprot.org/uniprotkb/P56181) · Ensembl [ENSG00000160194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160194)

## Data

Gene col 8314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8314); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8314]; `tensor/DDL_lfc|DDL_z.npy` [8314]; `embed/gene_vectors.npy` [8314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8314 or target_col == 8314). Every well: [[NDUFV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
