---
symbol: "PKNOX2"
type: "gene"
col: 9131
ensembl_id: "ENSG00000165495"
name: "PBX/knotted 1 homeobox 2"
location: "11q24.2"
module: 61
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PKNOX2

*PBX/knotted 1 homeobox 2* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.68× (z +21.2, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Naproxen (drug)]] 5 µM: 0.664× (z -3.9, q 0.067, down in 5 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0583×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.119×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (AN3 CA 0.139×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP2]] (+0.71, fdr 7e-06), [[SORCS1]] (+0.68, fdr 7e-06), [[SYN3]] (+0.68, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PDZRN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.68×** | +21.2 | 0e+00 | 24/28 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.45×** | +20.5 | 0e+00 | 19/24 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **7.81×** | +19.9 | 0e+00 | 38/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.82×** | +16.4 | 0e+00 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **5.38×** | +16.3 | 0e+00 | 31/40 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.34×** | +16.2 | 0e+00 | 33/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +12.2 | 3e-32 | 3/9 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.49×** | +12.1 | 6e-32 | 29/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +11.4 | 2e-28 | 1/4 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +11.3 | 9e-28 | 23/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +10.1 | 4e-22 | 13/27 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +9.6 | 3e-20 | 16/27 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.13×** | +5.8 | 3e-07 | 13/28 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +5.7 | 5e-07 | 6/18 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.6 | 9e-07 | 2/8 (PANC-1, BT-474) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.5 | 1e-06 | 9/32 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.3 | 3e-06 | 2/40 (PANC-1, HEC-1-A) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.2 | 9e-04 | 4/27 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.002 | 6/30 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0583×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.119×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (AN3 CA 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Naproxen (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.067 | 5/19 (C32, RPMI-7951, …) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.669× | -3.3 | 0.24 | 1/44 (HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 86.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0583× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.139× (z -8.5) |
| [[PANC-1 (line)]] | alt | 0.924 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 1.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +9.3) | — |
| [[KATO III (line)]] | alt | 0.807 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.7× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +11.4) | — |
| [[A-172 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.702 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.794 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.646 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.642 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.806 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.641 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.777 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.657 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP2]] | +0.71 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.68 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[SYN3]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LDB2]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KCNN3]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[DACH2]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.66 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.64 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ST8SIA1]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[HULC]] | +0.63 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[SYN1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZRN3]] | B | PDZRN3 activity raises PKNOX2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without PDZRN3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[TOP2A]] | B | TOP2A activity lowers PKNOX2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAN1C1]] | B | MAN1C1 activity raises PKNOX2's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without MAN1C1 | 0.078 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[LDB2]] | B | LDB2 activity raises PKNOX2's level | lines that do not express LDB2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without LDB2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000256915, SLC2A14, ENSG00000253496; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 32.1); signed map (31.7, 19.3). **Vector** length 43.4, 5.58% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +10.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | PBX/knotted 1 homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,164,687-125,433,389 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

UniProt [Q96KN3](https://www.uniprot.org/uniprotkb/Q96KN3) carries no function annotation.

**Summary**, from NCBI Gene [63876](https://www.ncbi.nlm.nih.gov/gene/63876):

> Homeodomain proteins are sequence-specific transcription factors that share a highly conserved DNA-binding domain and play fundamental roles in cell proliferation, differentiation, and death. PKNOX2 belongs to the TALE (3-amino acid loop extension) class of homeodomain proteins characterized by a 3-amino acid extension between alpha helices 1 and 2 within the homeodomain (Imoto et al., 2001 [PubMed 11549286]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:16714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16714) · Entrez [63876](https://www.ncbi.nlm.nih.gov/gene/63876) · UniProt [Q96KN3](https://www.uniprot.org/uniprotkb/Q96KN3) · Ensembl [ENSG00000165495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165495)

## Data

Gene col 9131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9131); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9131]; `tensor/DDL_lfc|DDL_z.npy` [9131]; `embed/gene_vectors.npy` [9131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9131 or target_col == 9131). Every well: [[PKNOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKNOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
