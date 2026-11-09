---
symbol: "CCDC39"
type: "gene"
col: 16074
ensembl_id: "ENSG00000284862"
name: "coiled-coil domain 39 molecular ruler complex subunit"
location: "3q26.33"
module: 21
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CCDC39

*coiled-coil domain 39 molecular ruler complex subunit* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.66× (z +12.3, q 5e-32, up in 31 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Darinaparsin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0539×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H460 0.126×); [[Saquinavir (drug)]] 0.5 µM in 1 line (NCI-H460 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB14-AS1]] (+0.78, fdr 1e-05), [[MAL2-AS1]] (+0.74, fdr 7e-06), [[RN7SL2]] (+0.73, fdr 7e-06); moves opposite to [[ALG10]] (-0.54, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[C2CD5-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.66×** | +12.3 | 5e-32 | 31/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +10.3 | 1e-22 | 32/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.3 | 1e-22 | 15/16 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +10.0 | 3e-21 | 27/37 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.8 | 1e-16 | 5/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +8.1 | 6e-14 | 27/44 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +6.9 | 3e-10 | 18/37 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +5.7 | 7e-07 | 2/6 (CFPAC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.2 | 0.002 | 10/30 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.0 | 0.003 | 6/17 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.011 | 4/17 (SHP-77, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.020 | 6/42 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 6/30 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.036 | 8/44 (A-427, NCI-H23, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.040 | 7/36 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.044 | 5/38 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.56×** | +3.0 | 0.082 | 1/38 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16074.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Darinaparsin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0539×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H460 0.126×); [[Saquinavir (drug)]] 0.5 µM in 1 line (NCI-H460 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.790× | -3.2 | 0.53 | 6/45 (NCI-H1573, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -3.1 | 0.53 | 7/48 (HCT15, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.12 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 2.76 | 0 | 2 | — | [[Cepharanthine (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[HOP62 (line)]] | alt | 2.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.0× (z +16.6) | — |
| [[Hs 766T (line)]] | wt | 2.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 3.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.4× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.0539× (z -9.2) |
| [[SNU-423 (line)]] | alt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +8.9) | — |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB14-AS1]] | +0.78 | +0.54 / +0.83 | both halves | 1e-05 |  |
| [[MAL2-AS1]] | +0.74 | +0.60 / +0.78 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.73 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[USH2A]] | +0.72 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.72 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.71 | +0.53 / +0.84 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.71 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.70 | +0.54 / +0.84 | both halves | 1e-05 |  |
| [[AKAP13-AS1]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.69 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.68 | +0.55 / +0.77 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TICAM2-AS1]] | +0.67 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.67 | +0.56 / +0.84 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD5-AS1]] | C | CCDC39's natural level weakens C2CD5-AS1's drug response | CCDC39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.06; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PTPRT]] | C | CCDC39's natural level weakens PTPRT's drug response | CCDC39's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.01; direction clear | 0.041 | ⚠ tissue can mimic it; precision caveat |
| [[LHFPL5]] | C | CCDC39's natural level weakens LHFPL5's drug response | CCDC39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.06; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 29.3); signed map (34.7, 6.4). **Vector** length 39.9, 4.13% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain 39 molecular ruler complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:180,602,858-180,684,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434A128, CILD14, FAP59, CFAP59 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFE4](https://www.uniprot.org/uniprotkb/Q9UFE4) (Coiled-coil domain-containing protein 39):

> Required for assembly of dynein regulatory complex (DRC) and inner dynein arm (IDA) complexes, which are responsible for ciliary beat regulation, thereby playing a central role in motility in cilia and flagella. Probably acts together with CCDC40 to form a molecular ruler that determines the 96 nanometer (nm) repeat length and arrangements of components in cilia and flagella (By similarity). Not required for outer dynein arm complexes assembly.

**Summary**, from NCBI Gene [339829](https://www.ncbi.nlm.nih.gov/gene/339829):

> The protein encoded by this gene is involved in the motility of cilia and flagella. The encoded protein is essential for the assembly of dynein regulatory and inner dynein arm complexes, which regulate ciliary beat. Defects in this gene are a cause of primary ciliary dyskinesia type 14 (CILD14). [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:25244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25244) · Entrez [339829](https://www.ncbi.nlm.nih.gov/gene/339829) · UniProt [Q9UFE4](https://www.uniprot.org/uniprotkb/Q9UFE4) · Ensembl [ENSG00000284862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284862)

## Data

Gene col 16074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16074); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16074]; `tensor/DDL_lfc|DDL_z.npy` [16074]; `embed/gene_vectors.npy` [16074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16074 or target_col == 16074). Every well: [[CCDC39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
