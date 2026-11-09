---
symbol: "KCNH1"
type: "gene"
col: 6751
ensembl_id: "ENSG00000143473"
name: "potassium voltage-gated channel subfamily H member 1"
location: "1q32.2"
module: 61
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# KCNH1

*potassium voltage-gated channel subfamily H member 1* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.27× (z +19.8, q 0e+00, up in 23 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.129×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD1]] (+0.71, fdr 7e-06), [[LINC02511]] (+0.69, fdr 1e-05), [[GRIA4]] (+0.68, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FSTL5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNBD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.27×** | +19.8 | 0e+00 | 23/27 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.36×** | +14.2 | 3e-43 | 7/11 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.49×** | +13.9 | 1e-41 | 3/3 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.45×** | +12.2 | 4e-32 | 20/44 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +11.9 | 2e-30 | 26/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +11.4 | 5e-28 | 11/30 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.59×** | +11.4 | 5e-28 | 2/5 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +10.8 | 3e-25 | 27/42 (NCI-H460, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.42×** | +8.5 | 1e-15 | 21/38 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.32×** | +8.1 | 3e-14 | 22/44 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +7.7 | 7e-13 | 20/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +7.5 | 3e-12 | 24/45 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +7.3 | 2e-11 | 16/34 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +6.6 | 1e-09 | 20/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.94×** | +6.2 | 3e-08 | 10/29 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.89×** | +6.1 | 3e-08 | 15/42 (C-33 A, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.74×** | +5.3 | 3e-06 | 15/34 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.3 | 3e-06 | 8/29 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6751.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.129×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.729× | -3.1 | 0.99 | 5/35 (RPMI-7951, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -12.2) |
| [[C-33 A (line)]] | alt | 5.27 | 1 | 0 | [[Selinexor (drug)]] 5 µM 23.3× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 4.04 | 1 | 0 | [[Selinexor (drug)]] 5 µM 9.30× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 1.14 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 20.5× (z +8.9) | — |
| [[A-172 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.971 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.857 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.69 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 | pathway: Neuronal System |
| [[GPM6A]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | pathway: Neuronal System |
| [[FAT3]] | +0.66 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.65 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[FMN2]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ERC2]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[XIRP2]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL5]] | B | FSTL5 activity raises KCNH1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without FSTL5 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[DISC1FP1]] | B | DISC1FP1 activity raises KCNH1's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 1.70× lower at baseline in the lines without DISC1FP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574 |
| [[TOP2A]] | B | TOP2A activity lowers KCNH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01885]] | B | LINC01885 activity raises KCNH1's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without LINC01885 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383 |
| [[LHFPL5]] | C | LHFPL5's natural level weakens KCNH1's drug response | LHFPL5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.33; direction clear | 0.049 | ⚠ tissue can mimic it; precision caveat |
| [[CNTNAP5]] | C | CNTNAP5's natural level weakens KCNH1's drug response | CNTNAP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.49; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNBD1]] | C | KCNH1's natural level weakens CNBD1's drug response | KCNH1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.41; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 30.5); signed map (33.3, 20.1). **Vector** length 51.0, 6.89% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +19.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily H member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:210,676,823-211,134,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv10.1, eag, h-eag, eag1, hEAG, K(V)10.1 |
| Gene groups (HGNC) | Potassium voltage-gated channels; PAS domain containing |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O95259](https://www.uniprot.org/uniprotkb/O95259) (Voltage-gated delayed rectifier potassium channel KCNH1):

> Pore-forming (alpha) subunit of a voltage-gated delayed rectifier potassium channel that mediates outward-rectifying potassium currents which, on depolarization, reaches a steady-state level and do not inactivate. The activation kinetics depend on the prepulse potential and external divalent cation concentration. With negative prepulses, the current activation is delayed and slowed down several fold, whereas more positive prepulses speed up activation. The time course of activation is biphasic …

**Summary**, from NCBI Gene [3756](https://www.ncbi.nlm.nih.gov/gene/3756):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily H. This member is a pore-forming (alpha) subunit of a voltage-gated …

**Accessions** — [HGNC:6250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6250) · Entrez [3756](https://www.ncbi.nlm.nih.gov/gene/3756) · UniProt [O95259](https://www.uniprot.org/uniprotkb/O95259) · Ensembl [ENSG00000143473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143473)

## Data

Gene col 6751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6751); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6751]; `tensor/DDL_lfc|DDL_z.npy` [6751]; `embed/gene_vectors.npy` [6751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6751 or target_col == 6751). Every well: [[KCNH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
