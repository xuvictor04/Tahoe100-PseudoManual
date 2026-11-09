---
symbol: "DPM3"
type: "gene"
col: 10995
ensembl_id: "ENSG00000179085"
name: "dolichyl-phosphate mannosyltransferase subunit 3, regulatory"
location: "1q22"
module: 24
arm: "+"
pooled_cpm: 7.64
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DPM3

*dolichyl-phosphate mannosyltransferase subunit 3, regulatory* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +6.4, q 9e-08, up in 24 of 27 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -5.1, q 2e-04, down in 27 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.220×, NCI-H460 0.253×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H23 0.0447×, RPMI-7951 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM52-AS1]] (+0.77, fdr 7e-06), [[MIF]] (+0.76, fdr 7e-06), [[LAMTOR2]] (+0.76, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.70, fdr 7e-06), [[CCT5]] (-0.65, fdr 7e-06), [[ABCF2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCSK1N]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +6.4 | 9e-08 | 24/27 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.32×** | +5.2 | 5e-05 | 27/37 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.24×** | +5.0 | 1e-04 | 29/41 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.08×** | +4.4 | 0.002 | 12/14 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.6 | 0.038 | 15/33 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +3.3 | 0.083 | 14/23 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10995.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.220×, NCI-H460 0.253×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H23 0.0447×, RPMI-7951 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -5.1 | 2e-04 | 27/42 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -4.5 | 0.002 | 26/41 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.553× | -3.4 | 0.11 | 17/46 (NCI-H1792, J82, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.598× | -3.1 | 0.25 | 18/46 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.583× | -3.1 | 0.25 | 9/46 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 7.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 9.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0671× (z -8.9) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM52-AS1]] | +0.77 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[MIF]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[LAMTOR2]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | STRING 453 |
| [[NDUFA3]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[LAMTOR4]] | +0.75 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.75 | +0.64 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CNNM2]] | +0.74 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.73 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[LSM2]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.72 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[NME3]] | +0.71 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.71 | +0.49 / +0.79 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[CCT5]] | -0.65 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.64 | -0.45 / -0.73 | both halves | 3e-05 |  |
| [[PDAP1]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[STIP1]] | -0.63 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.61 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PSMD12]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SLC25A24]] | -0.61 | -0.49 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1N]] | B | PCSK1N activity lowers DPM3's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.13× higher at baseline in the lines without PCSK1N | 0.019 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[MELTF]] | B | MELTF activity lowers DPM3's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without MELTF | 0.090 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.6, -21.2); signed map (-30.5, 8.4). **Vector** length 61.9, 13.1% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -4.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.1 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dolichyl-phosphate mannosyltransferase subunit 3, regulatory |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,139,891-155,140,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34275, MGC125904, MGC125905 |
| Gene groups (HGNC) | Dolichyl-phosphate mannosyltransferase subunits |
| Reactome | 15 pathways, smallest: Defective DPM1 causes DPM1-CDG; Defective DPM2 causes DPM2-CDG; Defective DPM3 causes DPM3-CDG |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2X0](https://www.uniprot.org/uniprotkb/Q9P2X0) (Dolichol-phosphate mannosyltransferase subunit 3):

> Stabilizer subunit of the dolichol-phosphate mannose (DPM) synthase complex; tethers catalytic subunit DPM1 to the endoplasmic reticulum.

**Summary**, from NCBI Gene [54344](https://www.ncbi.nlm.nih.gov/gene/54344):

> Dolichol-phosphate mannose (Dol-P-Man) serves as a donor of mannosyl residues on the lumenal side of the endoplasmic reticulum (ER). Lack of Dol-P-Man results in defective surface expression of GPI-anchored proteins. Dol-P-Man is synthesized from GDP-mannose and dolichol-phosphate on the cytosolic side of the ER by the enzyme dolichyl-phosphate mannosyltransferase. The protein encoded by this gene is a subunit of dolichyl-phosphate mannosyltransferase and acts as a stabilizer subunit of the …

**Accessions** — [HGNC:3007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3007) · Entrez [54344](https://www.ncbi.nlm.nih.gov/gene/54344) · UniProt [Q9P2X0](https://www.uniprot.org/uniprotkb/Q9P2X0) · Ensembl [ENSG00000179085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179085)

## Data

Gene col 10995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10995); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10995]; `tensor/DDL_lfc|DDL_z.npy` [10995]; `embed/gene_vectors.npy` [10995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10995 or target_col == 10995). Every well: [[DPM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
