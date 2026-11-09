---
symbol: "COL26A1"
type: "gene"
col: 8402
ensembl_id: "ENSG00000160963"
name: "collagen type XXVI alpha 1 chain"
location: "7q22.1"
module: 191
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# COL26A1

*collagen type XXVI alpha 1 chain* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.4× (z +35.3, q 0e+00, up in 33 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH3]] (+0.81, fdr 7e-06), [[LINC00624]] (+0.78, fdr 7e-06), [[HULC]] (+0.77, fdr 7e-06).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AFF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.4×** | +35.3 | 0e+00 | 33/34 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **12.3×** | +35.2 | 0e+00 | 29/33 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **34.7×** | +35.2 | 0e+00 | 44/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **24.9×** | +31.4 | 0e+00 | 41/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **6.46×** | +26.2 | 0e+00 | 42/44 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **9.31×** | +22.1 | 0e+00 | 39/41 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.57×** | +17.0 | 0e+00 | 32/38 (NCI-H460, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.48×** | +16.9 | 0e+00 | 21/31 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.81×** | +14.5 | 1e-45 | 20/44 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.30×** | +13.9 | 3e-42 | 32/40 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.14×** | +13.5 | 4e-40 | 3/4 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.79×** | +13.2 | 4e-38 | 28/34 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.55×** | +12.6 | 2e-34 | 31/44 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.9 | 3e-26 | 6/17 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.64×** | +9.6 | 2e-20 | 24/41 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.67×** | +8.0 | 5e-14 | 18/37 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +6.0 | 7e-08 | 14/35 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.803× | -3.1 | 0.60 | 10/43 (RPMI-7951, CHP-212, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.728× | -3.1 | 0.60 | 12/41 (NCI-H2347, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.70 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 141× (z +18.9) | — |
| [[HEC-1-A (line)]] | alt | 7.86 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +16.2) | — |
| [[KATO III (line)]] | alt | 7.66 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 69.6× (z +16.4) | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 6.33 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 31.7× (z +15.5) | — |
| [[A498 (line)]] | wt | 1.32 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 117× (z +12.4) | — |
| [[A549 (line)]] | wt | 2.96 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 86.7× (z +10.2) | — |
| [[C32 (line)]] | wt | 3.60 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 195× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 5.24 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 194× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 16.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.57× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 3.33 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 223× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 5.92 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 50.8× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 4.43 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.2× (z +10.6) | — |
| [[A-172 (line)]] | wt | 1.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 1.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.9× (z +13.4) | — |
| [[LoVo (line)]] | wt | 1.21 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 48.0× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.15 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 18.3× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 3.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.3× (z +17.9) | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.6× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 4.43 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 159× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 1.27 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 130× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 5.03 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 48.2× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 2.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 59.2× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 7.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +8.6) | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH3]] | +0.81 | +0.88 / +0.81 | both halves | 7e-06 |  |
| [[LINC00624]] | +0.78 | +0.68 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[HULC]] | +0.77 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[LINC00243]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.73 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.73 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[CCDC144NL-1]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[CEACAM22P-1]] | +0.70 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.69 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.67 | +0.58 / +0.77 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SCHLAP1]] | +0.67 | +0.72 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF2]] | B | AFF2 activity raises COL26A1's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without AFF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers COL26A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.905). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, 33.8); signed map (26.8, 16.8). **Vector** length 61.4, 9.69% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +26.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +35.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +5.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | +2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXVI alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,362,875-101,559,024 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Emu2, EMI6; previously EMID2 |
| Gene groups (HGNC) | Collagens; EMI domain containing |
| Reactome | 6 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

UniProt [Q96A83](https://www.uniprot.org/uniprotkb/Q96A83) carries no function annotation.

**Summary**, from NCBI Gene [136227](https://www.ncbi.nlm.nih.gov/gene/136227):

> This gene encodes a protein containing an emilin domain and two collagen stretches. This gene may be associated with aspirin-intolerant asthma. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:18038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18038) · Entrez [136227](https://www.ncbi.nlm.nih.gov/gene/136227) · UniProt [Q96A83](https://www.uniprot.org/uniprotkb/Q96A83) · Ensembl [ENSG00000160963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160963)

## Data

Gene col 8402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8402); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8402]; `tensor/DDL_lfc|DDL_z.npy` [8402]; `embed/gene_vectors.npy` [8402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8402 or target_col == 8402). Every well: [[COL26A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL26A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
