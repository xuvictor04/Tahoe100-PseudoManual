---
symbol: "SELENOK"
type: "gene"
col: 3505
ensembl_id: "ENSG00000113811"
name: "selenoprotein K"
location: "3p21.1"
module: 4
arm: "-"
pooled_cpm: 60.42
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SELENOK

*selenoprotein K* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +7.7, q 6e-12, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC186]] (+0.76, fdr 7e-06), [[TMEM258]] (+0.74, fdr 7e-06), [[IFT20]] (+0.73, fdr 7e-06); moves opposite to [[ATIC]] (-0.76, fdr 7e-06), [[VMA21]] (-0.73, fdr 7e-06), [[CAD]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +7.7 | 6e-12 | 47/48 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.21×** | +5.1 | 8e-05 | 36/41 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.52×** | +4.8 | 3e-04 | 45/49 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.7 | 4e-04 | 45/47 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +4.2 | 0.002 | 40/48 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.76×** | +3.8 | 0.012 | 36/48 (NCI-H2030, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.012 | 35/48 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.81×** | +3.7 | 0.014 | 28/45 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.73×** | +3.7 | 0.014 | 35/48 (SNU-1, LoVo, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +3.6 | 0.017 | 34/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.65×** | +3.4 | 0.036 | 34/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.036 | 35/48 (C32, SNU-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.63×** | +3.3 | 0.040 | 30/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.65×** | +3.3 | 0.046 | 31/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +3.1 | 0.078 | 31/50 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 31.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 48.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 49.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 55.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 43.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.6) | — |
| [[SW48 (line)]] | wt | 57.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +8.7) | — |
| [[A-172 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 135 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC186]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[IFT20]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RNF181]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.72 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[STX5]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SELENOM]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | same gene group; STRING 878 |
| [[TMEM106A]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TMF1]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TULP3]] | +0.68 | +0.52 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.76 | -0.61 / -0.78 | both halves | 7e-06 |  |
| [[VMA21]] | -0.73 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[CAD]] | -0.72 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[PFAS]] | -0.72 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.70 | -0.57 / -0.74 | both halves | 9e-06 |  |
| [[PRPF19]] | -0.70 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.69 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[DHX15]] | -0.68 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.67 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[C1QBP]] | -0.67 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[WDR77]] | -0.66 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[DHX9]] | -0.66 | -0.49 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises SELENOK's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without ARHGDIB | 0.013 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[DNAJB9]] | C | DNAJB9's natural level weakens SELENOK's drug response | DNAJB9's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.43; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.5, -34.6); signed map (-47.9, 14.6). **Vector** length 83.4, 33.4% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.9 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -3.9 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -3.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -3.4 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,884,417-53,891,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SELK |
| Gene groups (HGNC) | Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6D0](https://www.uniprot.org/uniprotkb/Q9Y6D0) (Selenoprotein K):

> Required for Ca(2+) flux in immune cells and plays a role in T-cell proliferation and in T-cell and neutrophil migration (By similarity). Involved in endoplasmic reticulum-associated degradation (ERAD) of soluble glycosylated proteins. Required for palmitoylation and cell surface expression of CD36 and involved in macrophage uptake of low-density lipoprotein and in foam cell formation (By similarity). Together with ZDHHC6, required for palmitoylation of ITPR1 in immune cells, leading to …

**Summary**, from NCBI Gene [58515](https://www.ncbi.nlm.nih.gov/gene/58515):

> The protein encoded by this gene belongs to the selenoprotein K family. It is a transmembrane protein that is localized in the endoplasmic reticulum (ER), and is involved in ER-associated degradation (ERAD) of misfolded, glycosylated proteins. It also has a role in the protection of cells from ER stress-induced apoptosis. Knockout studies in mice show the importance of this gene in promoting Ca(2+) flux in immune cells and mounting effective immune response. This protein is a selenoprotein, …

**Accessions** — [HGNC:30394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30394) · Entrez [58515](https://www.ncbi.nlm.nih.gov/gene/58515) · UniProt [Q9Y6D0](https://www.uniprot.org/uniprotkb/Q9Y6D0) · Ensembl [ENSG00000113811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113811)

## Data

Gene col 3505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3505); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3505]; `tensor/DDL_lfc|DDL_z.npy` [3505]; `embed/gene_vectors.npy` [3505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3505 or target_col == 3505). Every well: [[SELENOK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
