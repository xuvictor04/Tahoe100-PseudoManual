---
symbol: "CENPBD2P"
type: "gene"
col: 13134
ensembl_id: "ENSG00000213753"
name: "CENPB DNA-binding domains containing 2, pseudogene"
location: "19q13.43"
module: 38
arm: "+"
pooled_cpm: 19.07
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CENPBD2P

*CENPB DNA-binding domains containing 2, pseudogene* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +11.5, q 5e-28, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0933×); [[AZD2858 (drug)]] 0.5 µM in 1 line (NCI-H23 0.0636×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0683×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCN]] (+0.62, fdr 2e-05), [[TMEM269]] (+0.57, fdr 3e-05), [[UFC1]] (+0.56, fdr 7e-06); moves opposite to [[CASP2]] (-0.54, fdr 2e-05), [[MOCS1]] (-0.49, fdr 3e-05), [[CHST10]] (-0.49, fdr 7e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRKCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +11.5 | 5e-28 | 42/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +10.8 | 8e-25 | 34/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +9.6 | 1e-19 | 30/36 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +9.2 | 5e-18 | 36/42 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.8 | 8e-10 | 21/30 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.8 | 8e-10 | 34/42 (SNU-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.04×** | +4.9 | 7e-05 | 26/45 (HOP62, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.34×** | +3.9 | 0.007 | 16/44 (H4, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.069 | 10/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.072 | 11/46 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +3.0 | 0.13 | 10/48 (HCT15, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13134.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0933×); [[AZD2858 (drug)]] 0.5 µM in 1 line (NCI-H23 0.0636×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0683×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.832× | -3.4 | 0.37 | 18/48 (A-172, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.8) | — |
| [[A549 (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.9) | — |
| [[LoVo (line)]] | wt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +18.7) | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.5) | [[AZD2858 (drug)]] 0.5 µM 0.0636× (z -10.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0683× (z -9.4) |
| [[C32 (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.52× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0933× (z -10.9) |
| [[SW480 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.7) | — |
| [[A-172 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCN]] | +0.62 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[TMEM269]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[UFC1]] | +0.56 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[OSCP1]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[DHDH]] | +0.56 | +0.60 / +0.49 | both halves | 2e-05 |  |
| [[STX5-DT]] | +0.56 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ROPN1L]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[GPR137]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BUD31]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC01291]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PTPN6]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ATF3]] | +0.53 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP2]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MOCS1]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CHST10]] | -0.49 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[TMEM177]] | -0.49 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[EEF1E1]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[MCOLN2]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[ZNF232]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[FANCL]] | -0.46 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[SNRPD1]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[FHOD3]] | -0.46 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[AGPS]] | -0.46 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCG]] | B | PRKCG activity raises CENPBD2P's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without PRKCG | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[ROPN1L]] | C | ROPN1L activity raises CENPBD2P's level | lines that do not express ROPN1L (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without ROPN1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NBEAP2, FAM229B, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, -24.4); signed map (11.2, 15.8). **Vector** length 77.6, 15.1% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Pyridoxine (drug)]] 0.05 µM |  | +1.4 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | CENPB DNA-binding domains containing 2, pseudogene |
| Locus type | pseudogene |
| Location | 19q13.43 — chr19:58,598,967-58,599,435 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously CENPBD1P1 |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family; Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28421) · Entrez [65996](https://www.ncbi.nlm.nih.gov/gene/65996) · Ensembl [ENSG00000213753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213753)

## Data

Gene col 13134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13134); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13134]; `tensor/DDL_lfc|DDL_z.npy` [13134]; `embed/gene_vectors.npy` [13134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13134 or target_col == 13134). Every well: [[CENPBD2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPBD2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
