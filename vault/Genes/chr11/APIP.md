---
symbol: "APIP"
type: "gene"
col: 7338
ensembl_id: "ENSG00000149089"
name: "APAF1 interacting protein"
location: "11p13"
module: 18
arm: "+"
pooled_cpm: 24.61
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# APIP

*APAF1 interacting protein* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.26× (z +4.2, q 0.017, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -12.3, q 8e-32, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC2]] (+0.60, fdr 7e-06), [[TSEN15]] (+0.59, fdr 1e-05), [[PTAR1]] (+0.57, fdr 1e-05); moves opposite to [[AVIL]] (-0.60, fdr 1e-05), [[USP11]] (-0.54, fdr 1e-05), [[C19orf38]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.017 | 17/46 (A-172, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.021 | 15/46 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.21× | +3.4 | 0.11 | 17/46 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.19× | +3.1 | 0.28 | 9/46 (J82, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -12.3 | 8e-32 | 32/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -9.8 | 3e-20 | 32/46 (MIA PaCa-2, AN3 CA, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.630×** | -8.1 | 1e-13 | 26/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -7.8 | 9e-13 | 30/47 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -5.6 | 3e-06 | 22/46 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.768×** | -4.8 | 2e-04 | 19/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -4.4 | 7e-04 | 16/47 (SNU-1, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.818×** | -3.6 | 0.019 | 14/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.813×** | -3.6 | 0.019 | 18/47 (SW480, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.828×** | -3.4 | 0.035 | 23/47 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.076 | 6/47 (SW1417, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.2 | 0.076 | 11/46 (RPMI-7951, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | 0.835× | -3.0 | 0.11 | 12/36 (SHP-77, NCI-H1573, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 51.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 66.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -18.7) |
| [[A549 (line)]] | wt | 34.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.8) |
| [[H4 (line)]] | wt | 35.4 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0886× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.6) |
| [[PANC-1 (line)]] | alt | 39.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.0) |
| [[RKO (line)]] | wt | 23.9 | 0 | 2 | — | [[PF-06260933 (drug)]] 5 µM 0.0400× (z -10.9) |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 38.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.7) |
| [[A498 (line)]] | wt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.7) |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.2) |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.2) |
| [[Hs 766T (line)]] | wt | 36.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.442× (z -8.5) |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.5) |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0613× (z -8.6) |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 1 | — | [[Sinomenine (drug)]] 0.5 µM 0.0618× (z -9.3) |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC2]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TSEN15]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PTAR1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.56 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[DTD2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[XPO5]] | +0.55 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[VPS36]] | +0.55 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[RFT1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PPA2]] | +0.54 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ME2]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[POFUT1]] | +0.53 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[TMEM209]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVIL]] | -0.60 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[USP11]] | -0.54 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[C19orf38]] | -0.54 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[C5AR1]] | -0.54 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[ROPN1L]] | -0.54 | -0.62 / -0.32 | both halves | 1e-04 |  |
| [[HEXIM1]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SAP18]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MED29]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[GPANK1]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[LSR]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RBM8A]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[GARIN1A]] | -0.50 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises APIP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.1, -32.2); signed map (-11.1, -40.9). **Vector** length 77.4, 13.8% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.0 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | APAF1 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,853,094-34,916,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-29, Mmrp19, APIP2 |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Reactome | 10 pathways, smallest: Methionine salvage pathway; Formation of apoptosome; Regulation of the apoptosome activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GX9](https://www.uniprot.org/uniprotkb/Q96GX9) (Methylthioribulose-1-phosphate dehydratase):

> Catalyzes the dehydration of methylthioribulose-1-phosphate (MTRu-1-P) into 2,3-diketo-5-methylthiopentyl-1-phosphate (DK-MTP-1-P). Functions in the methionine salvage pathway, which plays a key role in cancer, apoptosis, microbial proliferation and inflammation. May inhibit the CASP1-related inflammatory response (pyroptosis), the CASP9-dependent apoptotic pathway and the cytochrome c-dependent and APAF1-mediated cell death.

**Summary**, from NCBI Gene [51074](https://www.ncbi.nlm.nih.gov/gene/51074):

> Enables identical protein binding activity; methylthioribulose 1-phosphate dehydratase activity; and zinc ion binding activity. Involved in several processes, including obsolete L-methionine salvage from methylthioadenosine; protein homotetramerization; and pyroptotic inflammatory response. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17581) · Entrez [51074](https://www.ncbi.nlm.nih.gov/gene/51074) · UniProt [Q96GX9](https://www.uniprot.org/uniprotkb/Q96GX9) · Ensembl [ENSG00000149089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149089)

## Data

Gene col 7338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7338); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7338]; `tensor/DDL_lfc|DDL_z.npy` [7338]; `embed/gene_vectors.npy` [7338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7338 or target_col == 7338). Every well: [[APIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
