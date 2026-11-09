---
symbol: "SLC27A6"
type: "gene"
col: 3461
ensembl_id: "ENSG00000113396"
name: "solute carrier family 27 member 6"
location: "5q23.3"
module: 140
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SLC27A6

*solute carrier family 27 member 6* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.64× (z +25.4, q 0e+00, up in 25 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.124×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.81, fdr 7e-06), [[MEIOC]] (+0.81, fdr 7e-06), [[HPSE2]] (+0.81, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.64×** | +25.4 | 0e+00 | 25/25 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.3×** | +19.4 | 0e+00 | 3/3 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.60×** | +18.9 | 0e+00 | 11/12 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.56×** | +13.2 | 7e-38 | 3/4 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +11.3 | 2e-27 | 21/28 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.04×** | +9.3 | 2e-18 | 25/39 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +6.9 | 3e-10 | 17/42 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +5.8 | 4e-07 | 16/34 (A-172, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +5.5 | 2e-06 | 8/21 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.2 | 1e-05 | 6/17 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +5.2 | 1e-05 | 10/25 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.1 | 2e-05 | 6/21 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +5.1 | 2e-05 | 11/37 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +4.6 | 2e-04 | 3/5 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.5 | 2e-04 | 11/29 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +3.8 | 0.005 | 1/19 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.006 | 7/32 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.019 | 9/42 (HOP62, A-172, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.058 | 3/21 (A549, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.0 | 0.063 | 7/32 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.067 | 2/41 (HOP62, SW 900) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.124×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.73 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +14.3) | — |
| [[A-172 (line)]] | wt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +12.8) | — |
| [[A-427 (line)]] | wt | 9.00 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -9.5) |
| [[A549 (line)]] | wt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +9.2) | — |
| [[J82 (line)]] | alt | 9.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +8.7) | — |
| [[LoVo (line)]] | wt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.22× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +12.4) | — |
| [[SW480 (line)]] | alt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.64× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.81 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.81 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HPSE2]] | +0.81 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[USH2A]] | +0.81 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.80 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.79 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[HRG-AS1]] | +0.78 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.78 | +0.56 / +0.80 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.78 | +0.57 / +0.83 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.78 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.78 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC27A6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01807]] | B | LINC01807 activity raises SLC27A6's level | lines that do not express LINC01807 (11) vs lines expressing it (39) | 1.22× lower at baseline in the lines without LINC01807 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000253496, SLC2A14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.6, 28.7); signed map (32.6, 12.7). **Vector** length 47.3, 6.27% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +19.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:128,538,013-129,033,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FATP6, VLCS-H1, FACVL2, ACSVL2 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Reactome | 4 pathways, smallest: Transport of fatty acids; Transport of vitamins, nucleosides, and related molecules; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2P4](https://www.uniprot.org/uniprotkb/Q9Y2P4) (Long-chain fatty acid transport protein 6):

> Mediates the import of long-chain fatty acids (LCFA) into the cell by facilitating their transport at the plasma membrane. Also functions as an acyl-CoA ligase catalyzing the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates (By similarity). Plays a pivotal role in regulating available LCFA substrates from exogenous sources in tissues undergoing high levels of beta-oxidation such as the heart.

**Summary**, from NCBI Gene [28965](https://www.ncbi.nlm.nih.gov/gene/28965):

> This gene encodes a member of the fatty acid transport protein family (FATP). FATPs are involved in the uptake of long-chain fatty acids and have unique expression patterns. Alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11000) · Entrez [28965](https://www.ncbi.nlm.nih.gov/gene/28965) · UniProt [Q9Y2P4](https://www.uniprot.org/uniprotkb/Q9Y2P4) · Ensembl [ENSG00000113396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113396)

## Data

Gene col 3461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3461); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3461]; `tensor/DDL_lfc|DDL_z.npy` [3461]; `embed/gene_vectors.npy` [3461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3461 or target_col == 3461). Every well: [[SLC27A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
