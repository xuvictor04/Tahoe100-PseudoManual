---
symbol: "IQCN"
type: "gene"
col: 5075
ensembl_id: "ENSG00000130518"
name: "IQ motif containing N"
location: "19p13.11"
module: 93
arm: "+"
pooled_cpm: 6.12
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# IQCN

*IQ motif containing N* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.49× (z +17.4, q 0e+00, up in 38 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (SHP-77 0.0607×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.0553×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Lopinavir (drug)]] 0.05 µM in 1 line (A498 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATF3]] (+0.75, fdr 7e-06), [[FGF18]] (+0.74, fdr 7e-06), [[TRIM72]] (+0.74, fdr 7e-06); moves opposite to [[PARGP1]] (-0.58, fdr 2e-05), [[PGS1]] (-0.57, fdr 7e-06), [[RNF4]] (-0.57, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SEMA4A]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Radotinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.49×** | +17.4 | 0e+00 | 38/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.70×** | +7.5 | 1e-11 | 25/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.63×** | +5.4 | 2e-05 | 27/40 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.35×** | +4.5 | 8e-04 | 21/41 (NCI-H1792, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +4.1 | 0.004 | 22/42 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +3.7 | 0.022 | 16/40 (SW1417, A-172, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.87×** | +3.3 | 0.069 | 11/42 (A-172, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.079 | 18/39 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (SHP-77 0.0607×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.0553×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Lopinavir (drug)]] 0.05 µM in 1 line (A498 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 0.520× | -3.6 | 0.12 | 16/41 (KATO III, LoVo, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.543× | -3.5 | 0.12 | 13/41 (HOP62, J82, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.545× | -3.2 | 0.23 | 15/40 (COLO 205, H4, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.584× | -3.1 | 0.27 | 9/41 (Panc 03.27, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.08 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +12.1) | [[Lopinavir (drug)]] 0.05 µM 0.0552× (z -8.6) |
| [[LoVo (line)]] | wt | 7.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.0553× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 8.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +11.1) | — |
| [[C32 (line)]] | wt | 7.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.7× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 3.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 4.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 2.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 6.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 3.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +14.6) | — |
| [[PANC-1 (line)]] | alt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 7.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0607× (z -9.1) |
| [[SW1417 (line)]] | alt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +8.9) | — |
| [[SW480 (line)]] | alt | 5.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +13.5) | — |
| [[A-427 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF3]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[FGF18]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[LINC02901]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[LDHC]] | +0.72 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[PRKCG]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.70 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[USP50]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[TEX14]] | +0.68 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARGP1]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PGS1]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[RNF4]] | -0.57 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[SNRNP40]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[VPS33B]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[STARD3]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.55 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[CDK5RAP1]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.54 | -0.61 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA4A]] | B | SEMA4A activity raises IQCN's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without SEMA4A | 0.050 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IQCN's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Radotinib (drug)]] 5 µM | C | IQCN activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express IQCN (3) vs lines expressing it (43) | the lines without IQCN: 0.79× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 45); across organs; also absent: ENSG00000257894, CDC42EP1, PDE4C; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | IQCN activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express IQCN (3) vs lines expressing it (43) | the lines without IQCN: 0.72× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 45); across organs; also absent: ENSG00000257894, CDC42EP1, PDE4C; maybe low, not absent |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM | C | IQCN activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express IQCN (3) vs lines expressing it (43) | the lines without IQCN: 0.76× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 45); across organs; also absent: ENSG00000257894, CDC42EP1, PDE4C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, -16.6); signed map (16.3, 11.7). **Vector** length 99.3, 25.1% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.5 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.6 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | -2.4 | -2.1 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,257,098-18,274,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1683 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0B3](https://www.uniprot.org/uniprotkb/Q9H0B3) (IQ domain-containing protein N):

> Essential for spermiogenesis and fertilization. May be required for manchette assembly in elongating spermatids (By similarity).

**Summary**, from NCBI Gene [80726](https://www.ncbi.nlm.nih.gov/gene/80726):

> Involved in spermatid development. Located in mitochondrion. Implicated in spermatogenic failure 78. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29350) · Entrez [80726](https://www.ncbi.nlm.nih.gov/gene/80726) · UniProt [Q9H0B3](https://www.uniprot.org/uniprotkb/Q9H0B3) · Ensembl [ENSG00000130518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130518)

## Data

Gene col 5075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5075); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5075]; `tensor/DDL_lfc|DDL_z.npy` [5075]; `embed/gene_vectors.npy` [5075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5075 or target_col == 5075). Every well: [[IQCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
