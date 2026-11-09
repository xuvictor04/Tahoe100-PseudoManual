---
symbol: "FANCF"
type: "gene"
col: 11376
ensembl_id: "ENSG00000183161"
name: "FA complementation group F"
location: "11p14.3"
module: 16
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# FANCF

*FA complementation group F* — 11p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.81× (z +5.3, q 4e-05, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.76× (z +5.3, q 4e-05, up in 17 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.253× (z -12.7, q 3e-34, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCD2]] (+0.71, fdr 7e-06), [[KLHL9]] (+0.70, fdr 1e-05), [[HDDC3]] (+0.69, fdr 7e-06); moves opposite to [[TPTEP2-CSNK1E]] (-0.58, fdr 1e-05), [[NFATC2IP]] (-0.54, fdr 2e-05), [[PDE6D]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.3 | 4e-05 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +5.3 | 4e-05 | 17/43 (A498, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.2 | 4e-05 | 19/44 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.7 | 3e-04 | 4/47 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.7 | 3e-04 | 9/45 (A-172, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.1 | 0.004 | 6/22 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.015 | 8/38 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.41× | +3.2 | 0.10 | 5/45 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.39× | +3.1 | 0.13 | 7/46 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.14 | 4/46 (SW480, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.253×** | -12.7 | 3e-34 | 43/46 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.299×** | -11.2 | 2e-26 | 35/45 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.342×** | -9.9 | 5e-21 | 27/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.348×** | -9.8 | 2e-20 | 34/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.651×** | -5.6 | 3e-06 | 23/33 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.556×** | -5.4 | 5e-06 | 19/42 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.616×** | -4.5 | 6e-04 | 16/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.003 | 17/46 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -3.9 | 0.005 | 13/42 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.030 | 14/32 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.63 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -18.1) |
| [[A-172 (line)]] | wt | 3.40 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0751× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 3.91 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0880× (z -11.1) |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0370× (z -12.6) |
| [[COLO 205 (line)]] | alt | 7.49 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0360× (z -11.2) |
| [[HT-29 (line)]] | alt | 7.45 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0683× (z -11.1) |
| [[SW480 (line)]] | alt | 5.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.112× (z -11.7) |
| [[A549 (line)]] | wt | 4.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -8.7) |
| [[H4 (line)]] | wt | 7.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0394× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0835× (z -8.8) |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0277× (z -10.4) |
| [[KATO III (line)]] | alt | 4.67 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0670× (z -10.0) |
| [[LS 180 (line)]] | wt | 6.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0687× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 1 | — | [[Erythromycin (drug)]] 5 µM 0.0623× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 4.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 5.86 | 0 | 1 | — | [[Tolcapone (drug)]] 0.05 µM 0.0719× (z -8.7) |
| [[SW1417 (line)]] | alt | 7.86 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0725× (z -11.8) |
| [[A-427 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD2]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[HDDC3]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[KAT14]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[CDPF1]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ADO]] | +0.68 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[MSANTD4]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZNF22]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[THNSL1]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.64 | +0.69 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.58 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[NFATC2IP]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PDE6D]] | -0.54 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MBOAT7]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises FANCF's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.9, 14.4); signed map (-3.2, -29.7). **Vector** length 55.4, 7.64% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -12.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -9.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.3 — chr11:22,622,533-22,625,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAF |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPI8](https://www.uniprot.org/uniprotkb/Q9NPI8) (Fanconi anemia group F protein):

> DNA repair protein that may operate in a postreplication repair or a cell cycle checkpoint function. May be implicated in interstrand DNA cross-link repair and in the maintenance of normal chromosome stability (By similarity).

**Summary**, from NCBI Gene [2188](https://www.ncbi.nlm.nih.gov/gene/2188):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3587) · Entrez [2188](https://www.ncbi.nlm.nih.gov/gene/2188) · UniProt [Q9NPI8](https://www.uniprot.org/uniprotkb/Q9NPI8) · Ensembl [ENSG00000183161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183161)

## Data

Gene col 11376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11376); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11376]; `tensor/DDL_lfc|DDL_z.npy` [11376]; `embed/gene_vectors.npy` [11376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11376 or target_col == 11376). Every well: [[FANCF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
