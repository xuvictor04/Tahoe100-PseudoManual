---
symbol: "CLDN10"
type: "gene"
col: 5617
ensembl_id: "ENSG00000134873"
name: "claudin 10"
location: "13q32.1"
module: 140
arm: "+"
pooled_cpm: 2.89
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# CLDN10

*claudin 10* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.47× (z +13.7, q 4e-40, up in 15 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW 900 0.0895×, SHP-77 0.229×; ⚠ cell-cycle shift, explains ~15% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.129×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.176×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (SW 900 0.148×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.277×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW 900 0.185×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN10-AS1]] (+0.64, fdr 7e-06, ⚠ same locus), [[SCN1A-AS1]] (+0.63, fdr 5e-05), [[AQP4-AS1]] (+0.62, fdr 1e-05), [[LINC00922]] (+0.62, fdr 3e-05); moves opposite to [[POGK]] (-0.48, fdr 3e-05), [[CNDP2]] (-0.47, fdr 3e-05), [[LARS1]] (-0.46, fdr 4e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLDN10-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.47×** | +13.7 | 4e-40 | 15/20 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +10.3 | 2e-22 | 0/7 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +9.7 | 7e-20 | 1/5 (NCI-H1792) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +8.9 | 1e-16 | 0/6 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.88×** | +4.9 | 1e-04 | 9/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.7 | 2e-04 | 1/7 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.001 | 4/22 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.003 | 9/35 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +4.0 | 0.004 | 1/7 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.004 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.007 | 0/13 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.7 | 0.010 | 0/6 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.58×** | +3.4 | 0.033 | 0/33 | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.3 | 0.041 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.2 | 0.044 | 1/11 (NCI-H460) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW 900 0.0895×, SHP-77 0.229×; ⚠ cell-cycle shift, explains ~15% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.129×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.176×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (SW 900 0.148×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.277×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW 900 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.641× | -3.5 | 0.15 | 9/38 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.620× | -3.5 | 0.15 | 3/42 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.2 | 0.22 | 12/43 (AsPC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 35.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0895× (z -17.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -9.3) |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0805× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 0.857 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.881 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.818 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.798 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.813 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.837 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.917 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN10-AS1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SCN1A-AS1]] | +0.63 | +0.39 / +0.74 | both halves | 5e-05 |  |
| [[AQP4-AS1]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[LINC00922]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[PECAM1]] | +0.60 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[EVI2B]] | +0.60 | +0.38 / +0.67 | both halves | 6e-05 |  |
| [[SEMA6D]] | +0.59 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[PTPRT]] | +0.59 | +0.40 / +0.71 | both halves | 5e-05 |  |
| [[A2ML1-AS1]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GABRG3]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[DCTN6-DT]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PMEL]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[TEX11]] | +0.56 | +0.34 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CNDP2]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LARS1]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN10-AS1]] | B | CLDN10-AS1 activity raises CLDN10's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without CLDN10-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[TMEM163]] | B | TMEM163 activity raises CLDN10's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without TMEM163 | 0.084 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.8, 29.8); signed map (32.6, 10.5). **Vector** length 40.9, 5.74% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | claudin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:95,433,604-95,579,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OSP-L, CPETRL3 |
| Gene groups (HGNC) | Claudins |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P78369](https://www.uniprot.org/uniprotkb/P78369) (Claudin-10):

> Forms paracellular channels: polymerizes in tight junction strands with cation- and anion-selective channels through the strands, conveying epithelial permeability in a process known as paracellular tight junction permeability.; [Isoform 1]: Forms cation-selective paracellular channels. In sweat glands and in the thick ascending limb (TAL) of Henle's loop in kidney, it controls paracellular sodium permeability which is essential for proper sweat production and renal function.; [Isoform 2]: …

**Summary**, from NCBI Gene [9071](https://www.ncbi.nlm.nih.gov/gene/9071):

> This gene encodes a member of the claudin family. Claudins are integral membrane proteins and components of tight junction strands. Tight junction strands serve as a physical barrier to prevent solutes and water from passing freely through the paracellular space between epithelial or endothelial cell sheets, and also play critical roles in maintaining cell polarity and signal transductions. The expression level of this gene is associated with recurrence of primary hepatocellular carcinoma. Six …

**Accessions** — [HGNC:2033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2033) · Entrez [9071](https://www.ncbi.nlm.nih.gov/gene/9071) · UniProt [P78369](https://www.uniprot.org/uniprotkb/P78369) · Ensembl [ENSG00000134873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134873)

## Data

Gene col 5617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5617); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5617]; `tensor/DDL_lfc|DDL_z.npy` [5617]; `embed/gene_vectors.npy` [5617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5617 or target_col == 5617). Every well: [[CLDN10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
