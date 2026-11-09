---
symbol: "TMEM236"
type: "gene"
col: 7289
ensembl_id: "ENSG00000148483"
name: "transmembrane protein 236"
location: "10p12.33"
module: 39
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TMEM236

*transmembrane protein 236* — 10p12.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.62× (z +9.3, q 1e-17, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.647× (z -4.4, q 0.005, down in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 0.0689×, HepG2/C3A 0.0836×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.0550×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.0868×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (AsPC-1 0.0669×); [[Megestrol (drug)]] 0.5 µM in 1 line (HCT15 0.0636×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A14]] (+0.84, fdr 7e-06), [[ANKDD1B]] (+0.81, fdr 7e-06), [[CDKL4]] (+0.80, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IMPA1P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.62×** | +9.3 | 1e-17 | 35/40 (A-172, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +9.0 | 5e-17 | 29/37 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +7.9 | 6e-13 | 22/36 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +7.1 | 2e-10 | 9/16 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +6.5 | 9e-09 | 19/33 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +6.1 | 9e-08 | 20/35 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.11×** | +5.4 | 6e-06 | 23/45 (LoVo, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +5.3 | 7e-06 | 4/11 (LOX-IMVI, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +4.7 | 1e-04 | 15/44 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.99×** | +4.5 | 4e-04 | 18/40 (A-427, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +4.2 | 0.002 | 16/40 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.003 | 13/36 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.004 | 12/44 (NCI-H460, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.011 | 17/41 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.60×** | +3.4 | 0.027 | 15/43 (LoVo, LS 180, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.041 | 7/42 (A498, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.095 | 10/40 (J82, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7289.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LS 180 0.0689×, HepG2/C3A 0.0836×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.0550×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.0868×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (AsPC-1 0.0669×); [[Megestrol (drug)]] 0.5 µM in 1 line (HCT15 0.0636×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.647×** | -4.4 | 0.005 | 20/41 (AsPC-1, KATO III, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.537×** | -4.1 | 0.014 | 16/40 (RPMI-7951, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.725× | -3.3 | 0.19 | 6/44 (NCI-H23, LS 180, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.438× | -3.1 | 0.27 | 11/36 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 3 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0550× (z -10.2) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0689× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Megestrol (drug)]] 0.5 µM 0.0636× (z -9.4) |
| [[LoVo (line)]] | wt | 6.75 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +13.6) | [[Belinostat (drug)]] 0.5 µM 0.0918× (z -9.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0836× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[J82 (line)]] | alt | 8.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A14]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ANKDD1B]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.80 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.80 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.77 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.77 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[OIT3]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[RAPSN]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPA1P1]] | B | IMPA1P1 activity raises TMEM236's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without IMPA1P1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[LINC01291]] | B | LINC01291 activity raises TMEM236's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without LINC01291 | 0.073 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[SMCO2]] | B | SMCO2 activity raises TMEM236's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without SMCO2 | 0.081 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, -14.0); signed map (17.2, 7.4). **Vector** length 89.9, 17.9% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +1.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.2 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.3 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -3.0 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 236 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.33 — chr10:17,752,201-17,800,868 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA16O1.2, bA162I21.2; previously FAM23B, FAM23A |
| Matched by | ensembl_id |

UniProt [Q5W0B7](https://www.uniprot.org/uniprotkb/Q5W0B7) carries no function annotation.

**Summary**, from NCBI Gene [653567](https://www.ncbi.nlm.nih.gov/gene/653567):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23473) · Entrez [653567](https://www.ncbi.nlm.nih.gov/gene/653567) · UniProt [Q5W0B7](https://www.uniprot.org/uniprotkb/Q5W0B7) · Ensembl [ENSG00000148483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148483)

## Data

Gene col 7289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7289); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7289]; `tensor/DDL_lfc|DDL_z.npy` [7289]; `embed/gene_vectors.npy` [7289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7289 or target_col == 7289). Every well: [[TMEM236 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM236.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
