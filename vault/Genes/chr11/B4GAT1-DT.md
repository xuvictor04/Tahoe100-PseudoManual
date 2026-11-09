---
symbol: "B4GAT1-DT"
type: "gene"
col: 14940
ensembl_id: "ENSG00000255468"
name: "B4GAT1 divergent transcript"
location: "11q13.2"
module: 10
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# B4GAT1-DT

*B4GAT1 divergent transcript* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.95× (z +8.7, q 1e-15, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.50× (z +3.4, q 0.092, up in 8 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.398× (z -7.3, q 2e-10, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.513× (z -5.6, q 5e-06, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSPOP]] (+0.55, fdr 1e-05), [[ITGB2]] (+0.55, fdr 4e-04), [[ADAMTS13]] (+0.53, fdr 4e-05); moves opposite to [[BLOC1S5-TXNDC5]] (-0.52, fdr 5e-05), [[MRPL2]] (-0.51, fdr 9e-05), [[BLOC1S5]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RDM1P5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +8.7 | 1e-15 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +6.7 | 6e-09 | 6/12 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +4.9 | 2e-04 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.092 | 8/38 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.49× | +3.2 | 0.16 | 1/44 (SW48) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.30× | +3.1 | 0.17 | 5/43 (SHP-77, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.398×** | -7.3 | 2e-10 | 27/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.459×** | -6.3 | 1e-07 | 20/40 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.513×** | -5.6 | 5e-06 | 18/40 (SW1417, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.526×** | -5.4 | 1e-05 | 17/39 (HOP62, BT-474, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.530×** | -5.3 | 1e-05 | 15/30 (PANC-1, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.669×** | -4.7 | 2e-04 | 18/34 (PANC-1, J82, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.590×** | -4.4 | 9e-04 | 14/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.608×** | -4.2 | 0.002 | 11/47 (BT-474, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -4.0 | 0.004 | 13/44 (NCI-H2030, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.620×** | -3.8 | 0.009 | 12/36 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.639×** | -3.7 | 0.010 | 15/39 (BT-474, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.649×** | -3.6 | 0.015 | 15/44 (A-427, A-172, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.038 | 9/45 (Panc 03.27, SW 900, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.666×** | -3.2 | 0.056 | 12/20 (MIA PaCa-2, SW1417, …) | all doses, flat |  |
| [[Hesperidin (drug)]] 0.5 µM |  | **0.684×** | -3.2 | 0.059 | 9/39 (COLO 205, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0659× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 1.71 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0669× (z -9.0) |
| [[A-172 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.841 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSPOP]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ITGB2]] | +0.55 | +0.53 / +0.26 | both halves | 4e-04 |  |
| [[ADAMTS13]] | +0.53 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[DHRS4L2]] | +0.53 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[DHX15]] | +0.53 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[TKFC]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ID2-AS1]] | +0.52 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[VAPA]] | +0.51 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[CYP4A22-AS1]] | +0.51 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[STK31]] | +0.51 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ARGLU1]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[DHX9]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLOC1S5-TXNDC5]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MRPL2]] | -0.51 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[BLOC1S5]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.48 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[NKAP]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TXNL4B]] | -0.45 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[GAN]] | -0.45 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R21]] | -0.45 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[YIPF5]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[GOLGA5]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[COA8]] | -0.44 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ATG12]] | -0.44 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises B4GAT1-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without RDM1P5 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises B4GAT1-DT's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.19× lower at baseline in the lines without LINC02026 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.355). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.6, 24.7); signed map (32.4, -29.2). **Vector** length 37.8, 3.73% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +0.8 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.7 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +1.3 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -5.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | B4GAT1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.2 — chr11:66,347,950-66,364,804 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56070) · Entrez [102724064](https://www.ncbi.nlm.nih.gov/gene/102724064) · Ensembl [ENSG00000255468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255468)

## Data

Gene col 14940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14940); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14940]; `tensor/DDL_lfc|DDL_z.npy` [14940]; `embed/gene_vectors.npy` [14940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14940 or target_col == 14940). Every well: [[B4GAT1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GAT1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
