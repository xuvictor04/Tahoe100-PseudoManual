---
symbol: "NSMCE1-DT"
type: "gene"
col: 14447
ensembl_id: "ENSG00000245888"
name: "NSMCE1 divergent transcript"
location: "16p12.1"
module: 23
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NSMCE1-DT

*NSMCE1 divergent transcript* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +14.5, q 8e-45, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.594× (z -5.0, q 3e-04, down in 12 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rosiglitazone (drug)]] 5 µM in 1 line (HEC-1-A 0.0757×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0734×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXA1L-DT]] (+0.82, fdr 7e-06), [[PIGP]] (+0.78, fdr 9e-06), [[TMEM202-AS1]] (+0.77, fdr 7e-06); moves opposite to [[APMAP]] (-0.65, fdr 6e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +14.5 | 8e-45 | 24/30 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +10.8 | 8e-25 | 21/29 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.23×** | +10.8 | 8e-25 | 5/13 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +10.0 | 3e-21 | 1/1 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +9.5 | 3e-19 | 20/43 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +8.9 | 5e-17 | 15/28 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.4 | 1e-11 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.2 | 3e-11 | 19/39 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.1 | 1e-10 | 12/44 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.06×** | +6.9 | 2e-10 | 20/43 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.91×** | +6.2 | 3e-08 | 17/41 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.4 | 3e-06 | 2/10 (A498, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.2 | 7e-06 | 9/24 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 6e-05 | 14/42 (LoVo, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.4 | 4e-04 | 9/44 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 2/29 (NCI-H2030, A-172) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.004 | 6/44 (A-172, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.004 | 5/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.029 | 5/35 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14447.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rosiglitazone (drug)]] 5 µM in 1 line (HEC-1-A 0.0757×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0734×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -5.0 | 3e-04 | 12/42 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.708× | -3.3 | 0.20 | 11/41 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.790× | -3.2 | 0.20 | 5/44 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Furosemide (drug)]] 5 µM |  | 0.791× | -3.2 | 0.20 | 3/44 (NCI-H23, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0757× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0734× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.673 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXA1L-DT]] | +0.82 | +0.82 / +0.68 | both halves | 7e-06 | same gene group |
| [[PIGP]] | +0.78 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[TMEM202-AS1]] | +0.77 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.77 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.77 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[USP38-DT]] | +0.76 | +0.78 / +0.61 | both halves | 7e-06 | same gene group |
| [[SEPTIN7-DT]] | +0.76 | +0.81 / +0.49 | both halves | 1e-05 | same gene group |
| [[LINC00240]] | +0.75 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[DDX59-AS1]] | +0.75 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.75 | +0.83 / +0.41 | both halves | 4e-05 |  |
| [[ATE1OSP]] | +0.75 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[EPM2A-DT]] | +0.74 | +0.82 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APMAP]] | -0.65 | -0.59 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NSMCE1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KATNAL2]] | B | KATNAL2 activity raises NSMCE1-DT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without KATNAL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises NSMCE1-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.0, 20.5); signed map (30.4, -7.2). **Vector** length 53.9, 7.47% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | NSMCE1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p12.1 — chr16:27,268,205-27,290,492 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51368) · Entrez [400512](https://www.ncbi.nlm.nih.gov/gene/400512) · Ensembl [ENSG00000245888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245888)

## Data

Gene col 14447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14447); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14447]; `tensor/DDL_lfc|DDL_z.npy` [14447]; `embed/gene_vectors.npy` [14447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14447 or target_col == 14447). Every well: [[NSMCE1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMCE1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
