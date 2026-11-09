---
symbol: "MAMDC2"
type: "gene"
col: 9061
ensembl_id: "ENSG00000165072"
name: "MAM domain containing 2"
location: "9q21.12"
module: 9
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MAMDC2

*MAM domain containing 2* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +14.3, q 2e-43, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +12.7, q 3e-34, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Canagliflozin (drug)]] 5 µM: 0.678× (z -4.2, q 0.012, down in 4 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.144×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SNU-423 0.0625×; ⚠ cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 0.137×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HTR1F]] (+0.53, fdr 1e-05), [[SLC13A4]] (+0.52, fdr 3e-04), [[DYNC1I1]] (+0.52, fdr 3e-05); moves opposite to [[NAMPTP1]] (-0.45, fdr 9e-05), [[SNAP29]] (-0.43, fdr 5e-04), [[SPTSSA]] (-0.41, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +14.3 | 2e-43 | 5/8 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +12.7 | 3e-34 | 18/31 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +12.6 | 7e-34 | 13/14 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +10.5 | 8e-24 | 3/8 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.8 | 2e-04 | 10/37 (SK-MEL-2, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.4 | 0.001 | 5/24 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +4.4 | 0.001 | 9/42 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.3 | 0.001 | 2/11 (J82, SW1417) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.2 | 0.001 | 2/8 (NCI-H2347, HOP62) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.003 | 6/43 (J82, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.004 | 8/29 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.62×** | +3.9 | 0.004 | 1/11 (Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.38×** | +3.7 | 0.009 | 4/17 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.009 | 6/24 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.011 | 8/45 (SW480, J82, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.015 | 1/15 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.059 | 3/35 (SK-MEL-2, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9061.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.144×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SNU-423 0.0625×; ⚠ cell-cycle shift, explains ~18% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 0.137×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (drug)]] 5 µM |  | **0.678×** | -4.2 | 0.012 | 4/30 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.821× | -3.2 | 0.42 | 8/45 (Hs 766T, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 6.93 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0625× (z -10.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTR1F]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.52 | +0.26 / +0.63 | both halves | 3e-04 |  |
| [[DYNC1I1]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ECSCR]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[FGF1]] | +0.52 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SLC14A2]] | +0.51 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[DOCK2]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CMAHP]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ANK1]] | +0.50 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[CDH6]] | +0.49 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[RERGL]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[CCDC190]] | +0.47 | +0.53 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAMPTP1]] | -0.45 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[SNAP29]] | -0.43 | -0.37 / -0.24 | both halves | 5e-04 |  |
| [[SPTSSA]] | -0.41 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[GRINA]] | -0.40 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[WASHC4]] | -0.39 | -0.37 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | MAMDC2's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | MAMDC2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.472 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.209). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.0, 18.9); signed map (33.9, 29.8). **Vector** length 40.4, 4.15% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MAM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:70,043,848-70,226,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21981 |
| Matched by | ensembl_id |

UniProt [Q7Z304](https://www.uniprot.org/uniprotkb/Q7Z304) carries no function annotation.

**Summary**, from NCBI Gene [256691](https://www.ncbi.nlm.nih.gov/gene/256691):

> Predicted to enable glycosaminoglycan binding activity. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23673) · Entrez [256691](https://www.ncbi.nlm.nih.gov/gene/256691) · UniProt [Q7Z304](https://www.uniprot.org/uniprotkb/Q7Z304) · Ensembl [ENSG00000165072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165072)

## Data

Gene col 9061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9061); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9061]; `tensor/DDL_lfc|DDL_z.npy` [9061]; `embed/gene_vectors.npy` [9061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9061 or target_col == 9061). Every well: [[MAMDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAMDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
