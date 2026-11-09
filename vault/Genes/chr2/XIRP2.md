---
symbol: "XIRP2"
type: "gene"
col: 8631
ensembl_id: "ENSG00000163092"
name: "xin actin binding repeat containing 2"
location: "2q24.3"
module: 90
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# XIRP2

*xin actin binding repeat containing 2* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.16× (z +17.6, q 0e+00, up in 16 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AN3 CA 0.0590×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0780×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.0880×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.77, fdr 7e-06), [[GRIA4]] (+0.76, fdr 7e-06), [[CNBD1]] (+0.76, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ASCL1]] → it (grade B ⚠); 4 go from it, the strongest it → [[BMAL2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.16×** | +17.6 | 0e+00 | 16/21 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +8.8 | 3e-16 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.91×** | +8.1 | 9e-14 | 19/32 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +7.8 | 1e-12 | 1/6 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +5.8 | 7e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.3 | 1e-05 | 9/23 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +5.2 | 2e-05 | 6/26 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.0 | 4e-05 | 12/36 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +4.9 | 5e-05 | 2/7 (SNU-1, SNU-423) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.82×** | +4.1 | 0.002 | 1/3 (SNU-1) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.71×** | +4.1 | 0.002 | 1/8 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.019 | 1/12 (NCI-H460) | top dose only | cell-cycle shift (explains ~11% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.5 | 0.022 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.031 | 1/24 (NCI-H460) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.036 | 3/32 (SNU-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.098 | 4/21 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AN3 CA 0.0590×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0780×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.0880×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0590× (z -9.8) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0780× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.765 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.656 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.715 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.719 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.743 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.876 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.853 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.684 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.986 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.804 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.686 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.916 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.715 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.795 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.697 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.77 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.76 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 | STRING 479 |
| [[GLRA3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LRRC4C]] | +0.73 | +0.57 / +0.76 | both halves | 9e-06 |  |
| [[CNTNAP5]] | +0.73 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[MYT1L]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.72 | +0.54 / +0.79 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.71 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[SCHLAP1]] | +0.71 | +0.47 / +0.80 | both halves | 2e-05 |  |
| [[SGCZ]] | +0.70 | +0.47 / +0.79 | both halves | 2e-05 |  |
| [[SORCS1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | B | ASCL1 activity raises XIRP2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.33× lower at baseline in the lines without ASCL1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[SRRM4]] | B | SRRM4 activity raises XIRP2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.51× lower at baseline in the lines without SRRM4 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[SOX11]] | B | SOX11 activity raises XIRP2's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.31× lower at baseline in the lines without SOX11 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |
| [[CALCA]] | B | CALCA activity raises XIRP2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.20× lower at baseline in the lines without CALCA | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[TOP2A]] | B | TOP2A activity lowers XIRP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMAL2-AS1]] | C | XIRP2 activity raises BMAL2-AS1's level | lines that do not express XIRP2 (3) vs lines expressing it (47) | 1.31× lower at baseline in the lines without XIRP2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PDE11A, ENSG00000214803, ENSG00000228566; maybe low, not absent; its own permutation p |
| [[STARD13-AS]] | C | XIRP2 activity raises STARD13-AS's level | lines that do not express XIRP2 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without XIRP2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PDE11A, ENSG00000214803, ENSG00000228566; maybe low, not absent; its own permutation p |
| cells under [[AT7519 (drug)]] 5 µM | C | XIRP2's natural level lowers the cells' numbers under AT7519 5 µM (makes them more sensitive) | XIRP2's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.361 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | XIRP2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | XIRP2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.511 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, 30.0); signed map (33.5, 15.7). **Vector** length 34.7, 4.31% of its response variance represented; |z| ≥ 3 in 733 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | xin actin binding repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:166,888,480-167,259,753 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CMYA3 |
| Gene groups (HGNC) | LIM domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [A4UGR9](https://www.uniprot.org/uniprotkb/A4UGR9) (Xin actin-binding repeat-containing protein 2):

> Protects actin filaments from depolymerization. Required for correct morphology of cell membranes and maturation of intercalated disks of cardiomyocytes via facilitating localization of XIRP1 and CDH2 to the termini of aligned mature cardiomyocytes (By similarity). Thereby required for correct postnatal heart development and growth regulation that is crucial for overall heart morphology and diastolic function (By similarity). Required for normal electrical conduction in the heart including …

**Summary**, from NCBI Gene [129446](https://www.ncbi.nlm.nih.gov/gene/129446):

> Enables actin filament binding activity. Predicted to be involved in actin filament organization and regulation of actin filament organization. Predicted to act upstream of or within cardiac muscle tissue morphogenesis; cell-cell junction organization; and ventricular septum development. Located in focal adhesion and stress fiber. Implicated in depressive disorder. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14303) · Entrez [129446](https://www.ncbi.nlm.nih.gov/gene/129446) · UniProt [A4UGR9](https://www.uniprot.org/uniprotkb/A4UGR9) · Ensembl [ENSG00000163092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163092)

## Data

Gene col 8631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8631); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8631]; `tensor/DDL_lfc|DDL_z.npy` [8631]; `embed/gene_vectors.npy` [8631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8631 or target_col == 8631). Every well: [[XIRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XIRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
