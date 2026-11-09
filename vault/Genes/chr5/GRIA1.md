---
symbol: "GRIA1"
type: "gene"
col: 7900
ensembl_id: "ENSG00000155511"
name: "glutamate ionotropic receptor AMPA type subunit 1"
location: "5q33.2"
module: 9
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 33
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GRIA1

*glutamate ionotropic receptor AMPA type subunit 1* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.21× (z +14.9, q 0e+00, up in 11 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.156×); [[Panobinostat (drug)]] 0.5 µM in 1 line (Hs 766T 0.0834×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0957×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Hs 766T 0.137×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOCK3]] (+0.70, fdr 7e-06), [[UNC80]] (+0.68, fdr 7e-06), [[TACR3-AS1]] (+0.67, fdr 7e-06); moves opposite to [[WDR5]] (-0.51, fdr 2e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SIM1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC8A1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.21×** | +14.9 | 0e+00 | 11/13 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.67×** | +11.7 | 2e-29 | 11/14 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +9.0 | 6e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +8.9 | 7e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.05×** | +7.1 | 1e-10 | 8/19 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +7.1 | 1e-10 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +6.2 | 5e-08 | 11/20 (SW480, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +5.5 | 3e-06 | 3/13 (A-172, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +5.2 | 1e-05 | 7/13 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +5.1 | 2e-05 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +4.2 | 0.001 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.1 | 0.002 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.38×** | +3.9 | 0.004 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +3.8 | 0.006 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.8 | 0.006 | 0/6 | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.156×); [[Panobinostat (drug)]] 0.5 µM in 1 line (Hs 766T 0.0834×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0957×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (Hs 766T 0.137×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 87.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -12.1) |
| [[A-172 (line)]] | wt | 1.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.1× (z +11.3) | — |
| [[A-427 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.762 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.916 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.684 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.761 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.787 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.777 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.784 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCK3]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[UNC80]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[TACR3-AS1]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 | pathway: Neuronal System; STRING 427 |
| [[PECAM1]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ABCA13]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.66 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[VCAN-AS1]] | +0.65 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[KCNIP1]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ANK1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[CNTNAP5]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIM1]] | B | SIM1 activity raises GRIA1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.08× lower at baseline in the lines without SIM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[DOK5]] | B | DOK5 activity raises GRIA1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.71× lower at baseline in the lines without DOK5 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5 |
| [[KRT5]] | C | KRT5 activity raises GRIA1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.55× lower at baseline in the lines without KRT5 | 0.007 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A1-AS1]] | B | GRIA1 activity raises SLC8A1-AS1's level | lines that do not express GRIA1 (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without GRIA1 | 0.056 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |
| [[LINC01592]] | B | GRIA1 activity raises LINC01592's level | lines that do not express GRIA1 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without GRIA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |
| [[LINC01151]] | B | GRIA1 activity raises LINC01151's level | lines that do not express GRIA1 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without GRIA1 | 0.091 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |
| cells under [[Pemigatinib (drug)]] 5 µM | B | GRIA1 activity lowers the cells' numbers under Pemigatinib 5 µM (makes them more sensitive) | lines that do not express GRIA1 (17) vs lines expressing it (31) | the lines without GRIA1: 1.17× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.371). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.7, 30.3); signed map (30.9, 15.8). **Vector** length 28.8, 4.96% of its response variance represented; |z| ≥ 3 in 517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +1.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.3 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor AMPA type subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:153,489,615-153,813,869 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluA1, GLURA; previously GLUR1 |
| Gene groups (HGNC) | Glutamate ionotropic receptor AMPA type subunits |
| Reactome | 20 pathways, smallest: Activation of AMPA receptors; Trafficking of GluR2-containing AMPA receptors; Synaptic adhesion-like molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P42261](https://www.uniprot.org/uniprotkb/P42261) (Glutamate receptor 1):

> Ionotropic glutamate receptor that functions as a ligand-gated cation channel, gated by L-glutamate and glutamatergic agonists such as alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA), quisqualic acid, and kainic acid. L-glutamate acts as an excitatory neurotransmitter at many synapses in the central nervous system. Binding of the excitatory neurotransmitter L-glutamate induces a conformation change, leading to the opening of the cation channel, and thereby converts the chemical …

**Summary**, from NCBI Gene [2890](https://www.ncbi.nlm.nih.gov/gene/2890):

> Glutamate receptors are the predominant excitatory neurotransmitter receptors in the mammalian brain and are activated in a variety of normal neurophysiologic processes. These receptors are heteromeric protein complexes with multiple subunits, each possessing transmembrane regions, and all arranged to form a ligand-gated ion channel. The classification of glutamate receptors is based on their activation by different pharmacologic agonists. This gene belongs to a family of …

**Accessions** — [HGNC:4571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4571) · Entrez [2890](https://www.ncbi.nlm.nih.gov/gene/2890) · UniProt [P42261](https://www.uniprot.org/uniprotkb/P42261) · Ensembl [ENSG00000155511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155511)

## Data

Gene col 7900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7900); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7900]; `tensor/DDL_lfc|DDL_z.npy` [7900]; `embed/gene_vectors.npy` [7900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7900 or target_col == 7900). Every well: [[GRIA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
