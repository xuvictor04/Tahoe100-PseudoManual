---
symbol: "ABCC11"
type: "gene"
col: 4261
ensembl_id: "ENSG00000121270"
name: "ATP binding cassette subfamily C member 11"
location: "16q12.1"
module: 21
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ABCC11

*ATP binding cassette subfamily C member 11* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.02× (z +22.3, q 0e+00, up in 18 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.70, fdr 1e-05), [[SLC27A6]] (+0.70, fdr 1e-05), [[SLC26A5]] (+0.70, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.02×** | +22.3 | 0e+00 | 18/23 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.91×** | +16.0 | 0e+00 | 5/5 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.87×** | +15.7 | 0e+00 | 9/9 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.31×** | +14.0 | 4e-42 | 6/6 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.04×** | +12.3 | 1e-32 | 18/29 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +6.4 | 2e-08 | 6/9 (SW1417, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +6.3 | 2e-08 | 7/27 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +6.3 | 2e-08 | 8/27 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +5.4 | 4e-06 | 4/19 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.54×** | +5.0 | 3e-05 | 1/2 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.22×** | +4.6 | 2e-04 | 4/7 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.5 | 3e-04 | 5/17 (BT-474, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.4 | 4e-04 | 11/39 (SW1417, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +4.2 | 0.001 | 7/35 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.001 | 12/38 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +4.0 | 0.002 | 6/24 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.002 | 2/39 (SNU-423, BT-474) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.70×** | +4.0 | 0.002 | 2/18 (CFPAC-1, SW1417) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.02×** | +3.8 | 0.004 | 4/34 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.011 | 9/42 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.012 | 2/39 (HEC-1-A, LS 180) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.025 | 8/33 (KATO III, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.667× | -3.1 | 0.97 | 6/27 (COLO 205, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 0.836 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 0.823 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +10.1) | — |
| [[SW480 (line)]] | alt | 1.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.8) | — |
| [[A-172 (line)]] | wt | 0.779 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.664 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.804 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.713 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.638 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.716 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.825 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.777 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.991 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SLC27A6]] | +0.70 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.69 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.68 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[A2ML1-AS1]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.67 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SNAP25-AS1]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[HSPE1-MOB4]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LANCL1-AS1]] | +0.65 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ADAP2]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[HSPA2-AS1]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCC11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 30.9); signed map (36.5, 6.6). **Vector** length 36.9, 4.39% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +22.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:48,165,773-48,247,568 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP8 |
| Gene groups (HGNC) | ATP binding cassette subfamily C |
| Reactome | 2 pathways, smallest: ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J66](https://www.uniprot.org/uniprotkb/Q96J66) (ATP-binding cassette sub-family C member 11):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes physiological compounds and xenobiotics from cells. Plays a role in physiological processes involving bile acids, conjugated steroids and cyclic nucleotides, including cAMP and cGMP. Mediates the ATP-dependent efflux of a range of physiological lipophilic anions, including the glutathione S-conjugates leukotriene C4 and dinitrophenyl S-glutathione, steroid sulfates, such as dehydroepiandrosterone 3-sulfate …

**Summary**, from NCBI Gene [85320](https://www.ncbi.nlm.nih.gov/gene/85320):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This ABC full transporter is a member of the MRP subfamily which is involved in multi-drug resistance. The product of this gene participates in physiological processes involving bile acids, conjugated …

**Accessions** — [HGNC:14639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14639) · Entrez [85320](https://www.ncbi.nlm.nih.gov/gene/85320) · UniProt [Q96J66](https://www.uniprot.org/uniprotkb/Q96J66) · Ensembl [ENSG00000121270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121270)

## Data

Gene col 4261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4261); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4261]; `tensor/DDL_lfc|DDL_z.npy` [4261]; `embed/gene_vectors.npy` [4261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4261 or target_col == 4261). Every well: [[ABCC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
