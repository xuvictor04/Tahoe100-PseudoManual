---
symbol: "SAT2"
type: "gene"
col: 6531
ensembl_id: "ENSG00000141504"
name: "spermidine/spermine N1-acetyltransferase family member 2"
location: "17p13.1"
module: 59
arm: "+"
pooled_cpm: 13.42
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# SAT2

*spermidine/spermine N1-acetyltransferase family member 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.14× (z +5.8, q 3e-06, up in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +3.9, q 0.011, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 6.06×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.188×, RPMI-7951 0.161×; ⚠ cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.110×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.77, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[KRT10]] (+0.76, fdr 7e-06, ⚠ KRT10 in the vector space only through flagged drug-doses), [[LAMTOR4]] (+0.76, fdr 7e-06), [[ATP5MC2]] (+0.74, fdr 7e-06), [[SNHG7]] (+0.74, fdr 7e-06); moves opposite to [[PRKDC]] (-0.74, fdr 7e-06), [[MACROH2A1]] (-0.74, fdr 7e-06), [[XRCC5]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 6.06×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.8 | 3e-06 | 35/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +4.4 | 0.003 | 24/45 (HEC-1-A, RKO, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.009 | 25/42 (SNU-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.011 | 28/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.66×** | +3.9 | 0.011 | 23/42 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.052 | 17/47 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.98× | +3.1 | 0.12 | 16/45 (SNU-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.98× | +3.1 | 0.12 | 20/44 (A498, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.49× | +3.1 | 0.14 | 16/45 (HEC-1-A, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.188×, RPMI-7951 0.161×; ⚠ cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.110×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.748× | -3.1 | 0.53 | 20/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.745× | -3.1 | 0.53 | 23/47 (CFPAC-1, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.06× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -10.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.77 | +0.69 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.76 | +0.69 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR4]] | +0.76 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.74 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.74 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | +0.73 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[SNHG8]] | +0.72 | +0.57 / +0.78 | both halves | 8e-06 |  |
| [[SIRT2]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.71 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.70 | +0.48 / +0.80 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG12]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[TOM1]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.69 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[FLCN]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.74 | -0.78 / -0.74 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.74 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.72 | -0.73 / -0.71 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.71 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[NUP155]] | -0.69 | -0.76 / -0.64 | both halves | 7e-06 |  |
| [[PSME3]] | -0.69 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[DARS2]] | -0.69 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[TRIP13]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[IPO5]] | -0.68 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[NUDT5]] | -0.67 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.66 | -0.60 / -0.73 | both halves | 7e-06 |  |
| [[NUP188]] | -0.66 | -0.51 / -0.73 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity raises SAT2's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.45× lower at baseline in the lines without EPB41L2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-36.4, -28.9); signed map (-13.8, -1.2). **Vector** length 89.7, 25.6% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Amino acids regulate mTORC1* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.7 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.3 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | spermidine/spermine N1-acetyltransferase family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,626,234-7,627,876 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSAT2 |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F10](https://www.uniprot.org/uniprotkb/Q96F10) (Thialysine N-epsilon-acetyltransferase):

> Catalyzes the N-acetylation of the amino acid thialysine (S-(2-aminoethyl)-L-cysteine), a L-lysine analog with the 4-methylene group substituted with a sulfur. May also catalyze acetylation of polyamines, such as norspermidine, spermidine or spermine. However, ability to acetylate polyamines is weak, suggesting that it does not act as a diamine acetyltransferase in vivo.

**Summary**, from NCBI Gene [112483](https://www.ncbi.nlm.nih.gov/gene/112483):

> Enables diamine N-acetyltransferase activity and identical protein binding activity. Involved in polyamine metabolic process. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23160) · Entrez [112483](https://www.ncbi.nlm.nih.gov/gene/112483) · UniProt [Q96F10](https://www.uniprot.org/uniprotkb/Q96F10) · Ensembl [ENSG00000141504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141504)

## Data

Gene col 6531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6531); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6531]; `tensor/DDL_lfc|DDL_z.npy` [6531]; `embed/gene_vectors.npy` [6531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6531 or target_col == 6531). Every well: [[SAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
