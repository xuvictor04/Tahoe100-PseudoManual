---
symbol: "ISYNA1"
type: "gene"
col: 2638
ensembl_id: "ENSG00000105655"
name: "inositol-3-phosphate synthase 1"
location: "19p13.11"
module: 138
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# ISYNA1

*inositol-3-phosphate synthase 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +7.3, q 2e-10, up in 13 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.713× (z -4.1, q 0.027, down in 13 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (J82 0.0636×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0684×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.302×; ⚠ cell-cycle shift, explains ~31% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (A549 0.0889×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGRN]] (+0.62, fdr 1e-05), [[CRTC2]] (+0.59, fdr 2e-05), [[NFKB2]] (+0.59, fdr 1e-05); moves opposite to [[CWC27]] (-0.44, fdr 2e-04), [[NVL]] (-0.44, fdr 2e-04), [[SNX4]] (-0.43, fdr 3e-04).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.3 | 2e-10 | 13/36 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.0 | 9e-10 | 3/6 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.4 | 2e-08 | 10/22 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +5.3 | 2e-05 | 3/10 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.2 | 0.003 | 4/21 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.6 | 0.025 | 1/10 (NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.5 | 0.040 | 2/10 (NCI-H23, PANC-1) | top dose only | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.33×** | +3.4 | 0.044 | 8/36 (SW48, COLO 205, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.044 | 8/41 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.055 | 8/32 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.3 | 0.057 | 0/42 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.064 | 7/36 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.064 | 4/41 (Hs 766T, A549, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.1 | 0.068 | 8/30 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2638.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (J82 0.0636×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0684×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.302×; ⚠ cell-cycle shift, explains ~31% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (A549 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -4.1 | 0.027 | 13/41 (AsPC-1, SK-MEL-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -3.6 | 0.086 | 14/38 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 5 µM |  | 0.604× | -3.2 | 0.27 | 6/27 (C-33 A, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.835× | -3.1 | 0.27 | 6/41 (RPMI-7951, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.00 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0889× (z -8.6) |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 8.41 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0684× (z -8.9) |
| [[J82 (line)]] | alt | 4.28 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0636× (z -10.7) |
| [[A-172 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGRN]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.59 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[NFKB2]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SLC9A3-AS1]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TRIM28]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[MICALL2]] | +0.54 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[KHNYN]] | +0.53 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GET4]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[RNF44]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[BAG6]] | +0.53 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[FBRS]] | +0.52 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[RGL2]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC27]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[NVL]] | -0.44 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[SNX4]] | -0.43 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[DHX57]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[RTN4IP1]] | -0.42 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[ERCC8]] | -0.42 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[MRPS35]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[PCGF6]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CDC123]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ERGIC2]] | -0.42 | -0.31 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ISYNA1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ISYNA1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, -23.4); signed map (0.7, 5.1). **Vector** length 39.2, 4.15% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.2 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.1 | +2.9 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.1 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | inositol-3-phosphate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,434,388-18,438,167 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ino1, INOS, IPS |
| Reactome | 2 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPH2](https://www.uniprot.org/uniprotkb/Q9NPH2) (Inositol-3-phosphate synthase 1):

> Key enzyme in myo-inositol biosynthesis pathway that catalyzes the conversion of glucose 6-phosphate to 1-myo-inositol 1-phosphate in a NAD-dependent manner. Rate-limiting enzyme in the synthesis of all inositol-containing compounds.

**Summary**, from NCBI Gene [51477](https://www.ncbi.nlm.nih.gov/gene/51477):

> This gene encodes an inositol-3-phosphate synthase enzyme. The encoded protein plays a critical role in the myo-inositol biosynthesis pathway by catalyzing the rate-limiting conversion of glucose 6-phosphate to myoinositol 1-phosphate. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the short arm of chromosome 4. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:29821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29821) · Entrez [51477](https://www.ncbi.nlm.nih.gov/gene/51477) · UniProt [Q9NPH2](https://www.uniprot.org/uniprotkb/Q9NPH2) · Ensembl [ENSG00000105655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105655)

## Data

Gene col 2638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2638); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2638]; `tensor/DDL_lfc|DDL_z.npy` [2638]; `embed/gene_vectors.npy` [2638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2638 or target_col == 2638). Every well: [[ISYNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISYNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
