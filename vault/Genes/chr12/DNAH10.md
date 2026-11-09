---
symbol: "DNAH10"
type: "gene"
col: 12439
ensembl_id: "ENSG00000197653"
name: "dynein axonemal heavy chain 10"
location: "12q24.31"
module: 53
arm: "+"
pooled_cpm: 2.47
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# DNAH10

*dynein axonemal heavy chain 10* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.25× (z +28.5, q 0e+00, up in 34 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD1L1]] (+0.84, fdr 7e-06), [[LINC02646]] (+0.84, fdr 7e-06), [[LINC01618]] (+0.82, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IGSF11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.25×** | +28.5 | 0e+00 | 34/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.53×** | +21.7 | 0e+00 | 30/34 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.92×** | +18.1 | 0e+00 | 40/43 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.50×** | +14.1 | 3e-43 | 0/1 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +13.8 | 3e-41 | 0/1 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.21×** | +13.6 | 3e-40 | 26/33 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +13.4 | 4e-39 | 10/11 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.68×** | +13.2 | 4e-38 | 38/45 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.46×** | +12.1 | 4e-32 | 16/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +10.8 | 1e-25 | 26/37 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +8.9 | 2e-17 | 27/44 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +8.6 | 6e-16 | 7/14 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.0 | 5e-14 | 15/44 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +7.2 | 2e-11 | 22/45 (LS 180, BT-474, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.95×** | +6.3 | 1e-08 | 19/43 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +5.6 | 1e-06 | 11/39 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.008 | 7/44 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.031 | 5/23 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.80×** | +3.1 | 0.049 | 2/38 (LoVo, SK-MEL-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 5 µM |  | 0.683× | -3.7 | 0.10 | 9/44 (C32, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.69 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 2.01 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 32.0× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 7.53× (z +8.7) | — |
| [[SW480 (line)]] | alt | 1.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +9.8) | — |
| [[A498 (line)]] | wt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.7) | — |
| [[A549 (line)]] | wt | 1.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 4.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +10.1) | — |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD1L1]] | +0.84 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.84 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.81 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.80 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[NEB]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.79 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[L3MBTL2-AS1]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.78 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.78 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.78 | +0.70 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF11]] | B | IGSF11 activity raises DNAH10's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without IGSF11 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNAH10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WFDC10B]] | B | WFDC10B activity lowers DNAH10's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.34× higher at baseline in the lines without WFDC10B | 0.071 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[SLC13A3]] | B | SLC13A3 activity raises DNAH10's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without SLC13A3 | 0.087 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -9.6); signed map (22.3, 9.3). **Vector** length 54.2, 6.97% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +18.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +28.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +21.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,762,188-123,935,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43808 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVF4](https://www.uniprot.org/uniprotkb/Q8IVF4) (Dynein axonemal heavy chain 10):

> Force generating protein of respiratory cilia. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP. Involved in sperm motility; implicated in sperm flagellar assembly. Probable inner arm dynein heavy chain.

**Summary**, from NCBI Gene [196385](https://www.ncbi.nlm.nih.gov/gene/196385):

> Dyneins are microtubule-associated motor protein complexes composed of several heavy, light, and intermediate chains. The axonemal dyneins, found in cilia and flagella, are components of the outer and inner dynein arms attached to the peripheral microtubule doublets. DNAH10 is an inner arm dynein heavy chain (Maiti et al., 2000 [PubMed 11175280]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2941) · Entrez [196385](https://www.ncbi.nlm.nih.gov/gene/196385) · UniProt [Q8IVF4](https://www.uniprot.org/uniprotkb/Q8IVF4) · Ensembl [ENSG00000197653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197653)

## Data

Gene col 12439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12439); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12439]; `tensor/DDL_lfc|DDL_z.npy` [12439]; `embed/gene_vectors.npy` [12439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12439 or target_col == 12439). Every well: [[DNAH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
