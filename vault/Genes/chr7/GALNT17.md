---
symbol: "GALNT17"
type: "gene"
col: 11653
ensembl_id: "ENSG00000185274"
name: "polypeptide N-acetylgalactosaminyltransferase 17"
location: "7q11.22"
module: 140
arm: "+"
pooled_cpm: 7.47
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# GALNT17

*polypeptide N-acetylgalactosaminyltransferase 17* — 7q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +18.5, q 0e+00, up in 31 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0327×, A-427 0.0819×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.186×; ⚠ cell-cycle shift, explains ~9% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.176×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.255×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (A549 0.0589×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C8orf34]] (+0.75, fdr 7e-06), [[LINC02755]] (+0.75, fdr 7e-06), [[CSMD1]] (+0.72, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +18.5 | 0e+00 | 31/37 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.76×** | +16.6 | 0e+00 | 26/37 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +15.9 | 0e+00 | 4/8 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.82×** | +15.6 | 0e+00 | 17/23 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +12.0 | 6e-31 | 5/10 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +9.8 | 7e-21 | 26/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +6.3 | 2e-08 | 16/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.6 | 1e-06 | 13/37 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.8 | 1e-04 | 2/16 (KATO III, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 2e-04 | 15/41 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 7/47 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 9/42 (C32, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.8 | 0.007 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.5 | 0.022 | 1/26 (Hs 766T) | top dose only | cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.048 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.068 | 11/46 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11653.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0327×, A-427 0.0819×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.186×; ⚠ cell-cycle shift, explains ~9% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.176×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.255×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (A549 0.0589×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -4.0 | 0.040 | 14/47 (RPMI-7951, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 69.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0819× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 13.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.35× (z +12.0) | — |
| [[SW480 (line)]] | alt | 2.42 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.6× (z +12.9) | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0589× (z -9.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0327× (z -19.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 2.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 2.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 2.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +8.5) | — |
| [[LoVo (line)]] | wt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.26× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 440 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -12.2) |
| [[PANC-1 (line)]] | alt | 1.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +12.5) | — |
| [[A-172 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf34]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[CSMD1]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[AGBL1]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SLC27A6]] | +0.71 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[PPP1R9A-AS1]] | +0.70 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[USH2A]] | +0.70 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.69 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[GALNTL6]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 | same gene group; pathway: O-linked glycosylation |
| [[CNTNAP5]] | +0.68 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[SCHLAP1]] | +0.68 | +0.59 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GALNT17's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.8, 28.3); signed map (33.1, 12.1). **Vector** length 58.8, 8.20% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -4.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.22 — chr7:71,132,144-71,713,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNTL3, GalNAc-T5L, GalNAc-T19, GalNAc-T17, ppGalNAc-T17; previously WBSCR17 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IS24](https://www.uniprot.org/uniprotkb/Q6IS24) (Polypeptide N-acetylgalactosaminyltransferase 17):

> May catalyze the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor.

**Summary**, from NCBI Gene [64409](https://www.ncbi.nlm.nih.gov/gene/64409):

> This gene encodes an N-acetylgalactosaminyltransferase. This gene is located centromeric to the common deleted region in Williams-Beuren syndrome (WBS), a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. This protein may play a role in membrane trafficking. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:16347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16347) · Entrez [64409](https://www.ncbi.nlm.nih.gov/gene/64409) · UniProt [Q6IS24](https://www.uniprot.org/uniprotkb/Q6IS24) · Ensembl [ENSG00000185274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185274)

## Data

Gene col 11653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11653); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11653]; `tensor/DDL_lfc|DDL_z.npy` [11653]; `embed/gene_vectors.npy` [11653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11653 or target_col == 11653). Every well: [[GALNT17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
