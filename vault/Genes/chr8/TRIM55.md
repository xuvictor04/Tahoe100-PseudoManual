---
symbol: "TRIM55"
type: "gene"
col: 7199
ensembl_id: "ENSG00000147573"
name: "tripartite motif containing 55"
location: "8q13.1"
module: 66
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 10
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TRIM55

*tripartite motif containing 55* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +12.7, q 4e-34, up in 1 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.228×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0740×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMPD4]] (+0.63, fdr 1e-05), [[PIEZO2]] (+0.58, fdr 3e-05), [[VCAN]] (+0.57, fdr 5e-05); moves opposite to [[VKORC1L1]] (-0.51, fdr 5e-05), [[PUS7]] (-0.50, fdr 1e-04), [[CCT6P3-1]] (-0.50, fdr 6e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CDH12]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +12.7 | 4e-34 | 1/6 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.99×** | +11.2 | 1e-26 | 4/5 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.00×** | +10.8 | 8e-25 | 4/4 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.14×** | +8.5 | 3e-15 | 2/5 (SNU-423, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +7.3 | 3e-11 | 3/6 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.7 | 1e-06 | 4/6 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.19×** | +5.5 | 4e-06 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +4.8 | 1e-04 | 2/7 (LOX-IMVI, A-427) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.8 | 1e-04 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +4.8 | 1e-04 | 2/6 (MIA PaCa-2, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.46×** | +4.5 | 3e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +4.3 | 7e-04 | 3/7 (LOX-IMVI, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +4.0 | 0.003 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.17×** | +3.9 | 0.005 | 1/5 (RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.014 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.93×** | +3.3 | 0.037 | 0/7 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.040 | 0/7 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.042 | 1/8 (LOX-IMVI) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.69×** | +3.1 | 0.049 | 2/6 (LOX-IMVI, A-427) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.049 | 2/7 (RPMI-7951, LOX-IMVI) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.053 | 0/5 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7199.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.228×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0740×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.714× | -3.3 | 0.52 | 0/7 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 69.0 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0740× (z -8.9) |
| [[A-172 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.400 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMPD4]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[VCAN]] | +0.57 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CALD1]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[NOCT]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[LIMA1]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MOXD1]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MYLK]] | +0.54 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[COL7A1]] | +0.53 | +0.25 / +0.60 | both halves | 4e-04 |  |
| [[NUAK2]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CCDC148]] | +0.53 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[TEX41]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.51 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[PUS7]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CCT6P3-1]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[FOXK2]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ZNF749]] | -0.49 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[NTAQ1]] | -0.46 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[PAM16]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[CAMKK2]] | -0.45 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[DCUN1D2]] | -0.45 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[C8orf76]] | -0.45 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[RABEPK]] | -0.45 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH12]] | C | TRIM55 activity raises CDH12's level | lines that do not express TRIM55 (40) vs lines expressing it (10) | 4.35× lower at baseline in the lines without TRIM55 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01425, SIM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 18.3); signed map (39.6, 30.5). **Vector** length 17.1, 3.70% of its response variance represented; |z| ≥ 3 in 188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +2.8 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.4 | +0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.3 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | +1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.5 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 55 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,126,896-66,175,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MURF-2; previously RNF29 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYV6](https://www.uniprot.org/uniprotkb/Q9BYV6) (Tripartite motif-containing protein 55):

> E3 ubiquitin ligase that plays an important role in regulating cardiac development and contractility, muscle growth, metabolism, and fiber-type differentiation. Acts as a critical factor that regulates cardiomyocyte size during development in concert with TRIM63 by regulating E2F1-mediated gene expression (By similarity). Plays a role in apoptosis induction in cardiomyocytes by promoting ubiquitination of the DUSP1 phosphatase. Promotes non-canonical NF-kappa-B signaling and B-cell-mediated …

**Summary**, from NCBI Gene [84675](https://www.ncbi.nlm.nih.gov/gene/84675):

> The protein encoded by this gene contains a RING zinc finger, a motif known to be involved in protein-protein interactions. This protein associates transiently with microtubules, myosin, and titin during muscle sarcomere assembly. It may act as a transient adaptor and plays a regulatory role in the assembly of sarcomeres. Four alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14215) · Entrez [84675](https://www.ncbi.nlm.nih.gov/gene/84675) · UniProt [Q9BYV6](https://www.uniprot.org/uniprotkb/Q9BYV6) · Ensembl [ENSG00000147573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147573)

## Data

Gene col 7199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7199); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7199]; `tensor/DDL_lfc|DDL_z.npy` [7199]; `embed/gene_vectors.npy` [7199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7199 or target_col == 7199). Every well: [[TRIM55 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM55.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
