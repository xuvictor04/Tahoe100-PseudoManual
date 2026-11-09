---
symbol: "NSUN5"
type: "gene"
col: 5048
ensembl_id: "ENSG00000130305"
name: "NOP2/Sun RNA methyltransferase 5"
location: "7q11.23"
module: 12
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NSUN5

*NOP2/Sun RNA methyltransferase 5* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.13× (z +7.7, q 7e-12, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -8.7, q 2e-15, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDRG1]] (+0.81, fdr 7e-06), [[MRPL58]] (+0.76, fdr 7e-06), [[KBTBD6]] (+0.75, fdr 7e-06); moves opposite to [[TMBIM6]] (-0.64, fdr 7e-06), [[FAM81A]] (-0.62, fdr 1e-05), [[PDIA3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[VCPKMT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.7 | 7e-12 | 34/39 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +7.4 | 3e-11 | 37/43 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +7.0 | 5e-10 | 29/35 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.81×** | +5.9 | 7e-07 | 31/42 (KATO III, LoVo, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.74×** | +5.7 | 2e-06 | 20/37 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.45×** | +5.3 | 1e-05 | 19/42 (KATO III, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.0 | 6e-05 | 13/45 (SW1417, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.7 | 1e-04 | 23/44 (PANC-1, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.002 | 21/44 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.003 | 19/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.021 | 12/44 (BT-474, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.38×** | +3.3 | 0.042 | 12/44 (NCI-H1792, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.080 | 11/44 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -8.7 | 2e-15 | 33/40 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -5.1 | 9e-05 | 21/44 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -3.9 | 0.020 | 16/44 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.20 | 12/45 (NCI-H2347, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.742× | -3.1 | 0.22 | 14/43 (HepG2/C3A, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.735× | -3.0 | 0.22 | 17/41 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.7) |
| [[A549 (line)]] | wt | 8.39 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.138× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.9) |
| [[SNU-423 (line)]] | alt | 5.68 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0586× (z -10.4) |
| [[SW48 (line)]] | wt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -9.0) |
| [[A-172 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDRG1]] | +0.81 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.76 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[SURF2]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[NT5C]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PUS3]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 | STRING 473 |
| [[TMEM70]] | +0.72 | +0.61 / +0.82 | both halves | 7e-06 |  |
| [[PHAX]] | +0.70 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[RP9]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.68 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM6]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[FAM81A]] | -0.62 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PDIA3]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[STT3B]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[GNAS]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[YBX1]] | -0.60 | -0.26 / -0.65 | both halves | 4e-04 | STRING 473 |
| [[TM9SF3]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[TMED4]] | -0.58 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[DDOST]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CRTAP]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[GANAB]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VCPKMT]] | C | NSUN5 activity raises VCPKMT's level | lines that do not express NSUN5 (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without NSUN5 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: PDCD6P1, PTPN3, FOXRED2; maybe low, not absent |
| [[FAHD2B]] | C | NSUN5 activity raises FAHD2B's level | lines that do not express NSUN5 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without NSUN5 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: PDCD6P1, PTPN3, FOXRED2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.5, -3.5); signed map (-3.0, -19.6). **Vector** length 73.2, 17.1% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,302,516-73,308,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOL1R, p120(NOL1), FLJ10267, NSUN5A, Ynl022cL; previously WBSCR20, WBSCR20A |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P11](https://www.uniprot.org/uniprotkb/Q96P11) (28S rRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that specifically methylates the C(5) position of cytosine 3782 (m5C3782) in 28S rRNA. m5C3782 promotes protein translation without affecting ribosome biogenesis and fidelity. Required for corpus callosum and cerebral cortex development (By similarity).

**Summary**, from NCBI Gene [55695](https://www.ncbi.nlm.nih.gov/gene/55695):

> This gene encodes a member of an evolutionarily conserved family of proteins that may function as methyltransferases. This gene is located in a larger region of chromosome 7 that is deleted in Williams-Beuren syndrome, a multisystem developmental disorder. There are two pseudogenes for this gene located in the same region of chromosome 7. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:16385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16385) · Entrez [55695](https://www.ncbi.nlm.nih.gov/gene/55695) · UniProt [Q96P11](https://www.uniprot.org/uniprotkb/Q96P11) · Ensembl [ENSG00000130305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130305)

## Data

Gene col 5048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5048); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5048]; `tensor/DDL_lfc|DDL_z.npy` [5048]; `embed/gene_vectors.npy` [5048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5048 or target_col == 5048). Every well: [[NSUN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
