---
symbol: "ZNF48"
type: "gene"
col: 11077
ensembl_id: "ENSG00000180035"
name: "zinc finger protein 48"
location: "16p11.2"
module: 7
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZNF48

*zinc finger protein 48* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +11.1, q 8e-26, up in 32 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.384× (z -10.3, q 5e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF446]] (+0.57, fdr 1e-05), [[MRPL20-AS1]] (+0.56, fdr 1e-05), [[LRRC14]] (+0.55, fdr 3e-05); moves opposite to [[APPL2]] (-0.45, fdr 3e-05), [[DAP]] (-0.44, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +11.1 | 8e-26 | 32/38 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +9.6 | 3e-19 | 33/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +8.7 | 1e-15 | 30/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.6 | 5e-12 | 19/35 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +5.3 | 1e-05 | 22/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.005 | 9/47 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.007 | 14/47 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.007 | 11/39 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.007 | 9/44 (SK-MEL-2, HCT15, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.016 | 6/47 (NCI-H1573, SW480, …) | top dose only |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.73×** | +3.1 | 0.094 | 0/33 | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.094 | 3/47 (H4, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.384×** | -10.3 | 5e-22 | 38/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -8.4 | 9e-15 | 23/36 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -7.9 | 4e-13 | 26/47 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -6.8 | 1e-09 | 25/45 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -6.3 | 5e-08 | 18/30 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.576×** | -5.9 | 3e-07 | 21/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.693×** | -3.7 | 0.016 | 11/43 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 5.74 | 0 | 2 (1 ⚠) | — | [[Tadalafil (drug)]] 5 µM 0.0684× (z -10.1) |
| [[PANC-1 (line)]] | alt | 4.88 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0658× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -11.3) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 5.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0530× (z -11.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0687× (z -9.2) |
| [[KATO III (line)]] | alt | 4.04 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0684× (z -9.6) |
| [[LoVo (line)]] | wt | 4.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0464× (z -12.8) |
| [[SHP-77 (line)]] | alt | 9.40 | 0 | 1 | — | [[MK-8353 (drug)]] 0.05 µM 0.0941× (z -9.0) |
| [[SW1417 (line)]] | alt | 5.91 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0928× (z -9.8) |
| [[SW480 (line)]] | alt | 4.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +8.5) | — |
| [[A-427 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF446]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 | same gene group |
| [[MRPL20-AS1]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LRRC14]] | +0.55 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ABHD15]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SIRT3]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CHKB-DT]] | +0.54 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.51 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[C6orf47]] | +0.51 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LZTS2]] | +0.51 | +0.23 / +0.45 | both halves | 5e-04 |  |
| [[PLPP6]] | +0.50 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MED11]] | +0.50 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ZBTB45]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APPL2]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DAP]] | -0.44 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF48's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCA17P]] | B | ABCA17P activity raises ZNF48's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without ABCA17P | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[ID2-AS1]] | B | ID2-AS1 activity raises ZNF48's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without ID2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[FBXO15]] | B | FBXO15 activity raises ZNF48's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without FBXO15 | 0.085 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.404). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.8, -0.6); signed map (-5.3, -27.6). **Vector** length 42.3, 4.35% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +11.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.6 | -5.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,378,106-30,400,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762K013, FLJ31751, MGC43952; previously ZNF553 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MX3](https://www.uniprot.org/uniprotkb/Q96MX3) (Zinc finger protein 48):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [197407](https://www.ncbi.nlm.nih.gov/gene/197407):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13114) · Entrez [197407](https://www.ncbi.nlm.nih.gov/gene/197407) · UniProt [Q96MX3](https://www.uniprot.org/uniprotkb/Q96MX3) · Ensembl [ENSG00000180035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180035)

## Data

Gene col 11077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11077); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11077]; `tensor/DDL_lfc|DDL_z.npy` [11077]; `embed/gene_vectors.npy` [11077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11077 or target_col == 11077). Every well: [[ZNF48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
