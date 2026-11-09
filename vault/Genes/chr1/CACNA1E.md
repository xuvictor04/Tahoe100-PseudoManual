---
symbol: "CACNA1E"
type: "gene"
col: 12555
ensembl_id: "ENSG00000198216"
name: "calcium voltage-gated channel subunit alpha1 E"
location: "1q25.3"
module: 75
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CACNA1E

*calcium voltage-gated channel subunit alpha1 E* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.92× (z +24.5, q 0e+00, up in 19 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0486×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.139×); [[Peretinoin (drug)]] 0.5 µM in 1 line (COLO 205 0.0374×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLB1]] (+0.80, fdr 7e-06), [[LINC01811]] (+0.72, fdr 7e-06), [[MTUS2]] (+0.69, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIWIL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.92×** | +24.5 | 0e+00 | 19/24 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.77×** | +24.3 | 0e+00 | 19/22 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.25×** | +17.2 | 0e+00 | 31/38 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **6.99×** | +16.3 | 0e+00 | 21/27 (A-172, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.28×** | +12.2 | 4e-32 | 16/26 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +11.9 | 1e-30 | 0/2 | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.48×** | +11.6 | 2e-29 | 1/3 (A498) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.86×** | +11.3 | 7e-28 | 1/8 (PANC-1) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.26×** | +9.9 | 2e-21 | 20/27 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.25×** | +9.6 | 3e-20 | 12/40 (A498, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.06×** | +9.4 | 3e-19 | 19/34 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.20×** | +9.4 | 3e-19 | 14/30 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +6.8 | 6e-10 | 17/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.1 | 4e-08 | 8/25 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.4 | 2e-06 | 5/15 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0486×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.139×); [[Peretinoin (drug)]] 0.5 µM in 1 line (COLO 205 0.0374×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.0916×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.69 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.4× (z +13.3) | — |
| [[A498 (line)]] | wt | 2.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.3) |
| [[PANC-1 (line)]] | alt | 0.848 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +10.2) | — |
| [[A-427 (line)]] | wt | 1.53 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.2× (z +8.6) | — |
| [[C32 (line)]] | wt | 1.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.7× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 7.01 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0374× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 0.962 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 0.857 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +8.5) | — |
| [[LoVo (line)]] | wt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.5× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 1.70 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 19.9× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +11.5) | — |
| [[SW480 (line)]] | alt | 5.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0486× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.894 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.722 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.747 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.564 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.730 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.631 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLB1]] | +0.80 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.69 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.69 | +0.65 / +0.78 | both halves | 7e-06 | pathway: Neuronal System |
| [[RBFOX3]] | +0.69 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[DKK2]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LINC03042]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.67 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[DNAH2]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[GRM8]] | +0.65 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIWIL1]] | B | PIWIL1 activity raises CACNA1E's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 1.82× lower at baseline in the lines without PIWIL1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[TOP2A]] | B | TOP2A activity lowers CACNA1E's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HTR2C]] | B | HTR2C activity raises CACNA1E's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without HTR2C | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[IGFL4]] | B | IGFL4 activity raises CACNA1E's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without IGFL4 | 0.053 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[LINC01819]] | B | LINC01819 activity raises CACNA1E's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.41× lower at baseline in the lines without LINC01819 | 0.060 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[GFRA1]] | B | GFRA1 activity raises CACNA1E's level | lines that do not express GFRA1 (33) vs lines expressing it (17) | 1.05× lower at baseline in the lines without GFRA1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NLGN4Y, MAPK4, GREM2 |
| [[HUNK]] | B | HUNK activity raises CACNA1E's level | lines that do not express HUNK (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without HUNK | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, 32.3); signed map (31.3, 18.2). **Vector** length 58.2, 9.83% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +24.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +24.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +16.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:181,317,690-181,813,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cav2.3, BII, CACH6; previously CACNL1A6 |
| Gene groups (HGNC) | EF-hand domain containing; Calcium voltage-gated channel alpha1 subunits |
| Reactome | 5 pathways, smallest: Presynaptic depolarization and calcium channel opening; Regulation of insulin secretion; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15878](https://www.uniprot.org/uniprotkb/Q15878) (Voltage-dependent R-type calcium channel subunit alpha-1E):

> Voltage-sensitive calcium channels (VSCC) mediate the entry of calcium ions into excitable cells. They are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, gene expression, cell motility, cell division and cell death. The isoform alpha-1E gives rise to R-type calcium currents. R-type calcium channels belong to the 'high-voltage activated' (HVA) group and are blocked by nickel. They are however insensitive to …

**Summary**, from NCBI Gene [777](https://www.ncbi.nlm.nih.gov/gene/777):

> Voltage-dependent calcium channels are multisubunit complexes consisting of alpha-1, alpha-2, beta, and delta subunits in a 1:1:1:1 ratio. These channels mediate the entry of calcium ions into excitable cells, and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, gene expression, cell motility, cell division and cell death. This gene encodes the alpha-1E subunit of the R-type calcium channels, which belong to the …

**Accessions** — [HGNC:1392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1392) · Entrez [777](https://www.ncbi.nlm.nih.gov/gene/777) · UniProt [Q15878](https://www.uniprot.org/uniprotkb/Q15878) · Ensembl [ENSG00000198216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198216)

## Data

Gene col 12555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12555); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12555]; `tensor/DDL_lfc|DDL_z.npy` [12555]; `embed/gene_vectors.npy` [12555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12555 or target_col == 12555). Every well: [[CACNA1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
