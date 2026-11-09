---
symbol: "TEKTIP1"
type: "gene"
col: 11398
ensembl_id: "ENSG00000183397"
name: "tektin bundle interacting protein 1"
location: "19p13.3"
module: 35
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TEKTIP1

*tektin bundle interacting protein 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +9.6, q 4e-19, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +4.7, q 3e-04, up in 10 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.652× (z -4.7, q 0.001, down in 8 of 44 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Larotrectinib (drug)]] 5 µM: 0.789× (z -3.7, q 0.041, down in 9 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0829×, HEC-1-A 0.0871×); [[Decitabine (drug)]] 0.5 µM in 1 line (A-172 0.0872×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC23A3]] (+0.64, fdr 1e-05), [[LINC02951]] (+0.62, fdr 1e-05), [[TOMM20L-DT]] (+0.61, fdr 1e-05); moves opposite to [[THEM6]] (-0.61, fdr 4e-05), [[SDHAF3]] (-0.52, fdr 3e-05), [[CBR1]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +9.6 | 4e-19 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +7.5 | 1e-11 | 2/12 (HOP62, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +7.1 | 2e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.9 | 1e-04 | 1/9 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 10/34 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.007 | 3/46 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.015 | 2/23 (A-172, LoVo) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.054 | 4/29 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.087 | 4/46 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.087 | 3/37 (NCI-H2347, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0829×, HEC-1-A 0.0871×); [[Decitabine (drug)]] 0.5 µM in 1 line (A-172 0.0872×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.652×** | -4.7 | 0.001 | 8/44 (H4, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.704×** | -3.9 | 0.031 | 10/45 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.041 | 9/42 (HS-578T, HEC-1-A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -3.6 | 0.048 | 12/43 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.753× | -3.1 | 0.13 | 8/44 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.754× | -3.1 | 0.13 | 9/41 (A-427, SW 900, …) | inconsistent across doses |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.736× | -3.1 | 0.13 | 4/40 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.13 | 7/43 (hTERT-HPNE, RKO, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.821× | -3.1 | 0.13 | 7/42 (SHP-77, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.92 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0872× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 4.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0829× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 3.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0871× (z -8.9) |
| [[A-427 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC23A3]] | +0.64 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TOMM20L-DT]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PSMG3-AS1]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MYH11]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[FAM184B]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[QRICH2]] | +0.58 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[MYL6B-AS1]] | +0.58 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SPAG5-AS1]] | +0.58 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[HAVCR2]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.61 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[SDHAF3]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CBR1]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TEKTIP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (17.1, 22.3); signed map (30.0, 3.9). **Vector** length 37.0, 3.21% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +4.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.2 | -3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tektin bundle interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,539,171-3,544,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC100128569; previously C19orf71 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NCJ1](https://www.uniprot.org/uniprotkb/A6NCJ1) (Tektin bundle-interacting protein 1):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. Located at the center of the tektin bundle where may function to recruit tektins or stabilize the bundle.

**Summary**, from NCBI Gene [100128569](https://www.ncbi.nlm.nih.gov/gene/100128569):

> Predicted to be involved in flagellated sperm motility. Predicted to be located in axonemal microtubule. Predicted to be active in axonemal A tubule inner sheath and sperm flagellum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34496) · Entrez [100128569](https://www.ncbi.nlm.nih.gov/gene/100128569) · UniProt [A6NCJ1](https://www.uniprot.org/uniprotkb/A6NCJ1) · Ensembl [ENSG00000183397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183397)

## Data

Gene col 11398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11398); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11398]; `tensor/DDL_lfc|DDL_z.npy` [11398]; `embed/gene_vectors.npy` [11398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11398 or target_col == 11398). Every well: [[TEKTIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEKTIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
