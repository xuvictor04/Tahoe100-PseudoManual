---
symbol: "AJUBA-DT"
type: "gene"
col: 15103
ensembl_id: "ENSG00000258457"
name: "AJUBA divergent transcript"
location: "14q11.2"
module: 10
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 3
n_dd_up_clean: 32
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# AJUBA-DT

*AJUBA divergent transcript* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.09× (z +19.3, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.529× (z -5.1, q 2e-04, down in 13 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHODL]] (+0.69, fdr 7e-06), [[KIF6]] (+0.66, fdr 7e-06), [[APPBP2-DT]] (+0.65, fdr 1e-05); moves opposite to [[DAP3]] (-0.56, fdr 9e-05), [[ZCCHC17]] (-0.55, fdr 1e-04), [[ORC3]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.09×** | +19.3 | 0e+00 | 26/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.29×** | +17.3 | 0e+00 | 28/30 (CFPAC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.82×** | +12.2 | 5e-32 | 3/3 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.8 | 1e-20 | 1/1 (BT-474) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +9.8 | 1e-20 | 32/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.96×** | +9.1 | 7e-18 | 19/28 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +8.5 | 1e-15 | 30/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +8.5 | 2e-15 | 30/43 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.50×** | +7.7 | 9e-13 | 23/45 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +7.6 | 2e-12 | 23/41 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.33×** | +7.1 | 7e-11 | 11/13 (HEC-1-A, A498, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +6.3 | 1e-08 | 12/25 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.2 | 3e-08 | 13/44 (A498, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +6.1 | 4e-08 | 13/44 (NCI-H2347, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.94×** | +5.5 | 1e-06 | 12/27 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.2 | 6e-06 | 8/30 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +5.2 | 6e-06 | 16/35 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +5.1 | 1e-05 | 12/35 (PANC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.529×** | -5.1 | 2e-04 | 13/32 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.715×** | -4.0 | 0.017 | 13/43 (A498, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.633×** | -3.9 | 0.022 | 9/37 (LS 180, C-33 A, …) | two highest doses | low cells (technical?) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.695× | -3.1 | 0.30 | 5/40 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 2.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 1.67 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +9.9) | [[Naproxen (drug)]] 5 µM 0.0654× (z -8.6) |
| [[A-427 (line)]] | wt | 4.92 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0818× (z -8.5) |
| [[A498 (line)]] | wt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +10.0) | — |
| [[A-172 (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHODL]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[KIF6]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[APPBP2-DT]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 | same gene group |
| [[CES3]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.64 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[ACAD9-DT]] | +0.64 | +0.74 / +0.53 | both halves | 1e-05 | same gene group |
| [[ANKRD31]] | +0.64 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[LINC00240]] | +0.63 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ARL14EP-DT]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 | same gene group |
| [[GUCY2C-AS1]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[BANK1]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TFAP2A-AS1]] | +0.62 | +0.73 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP3]] | -0.56 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[ZCCHC17]] | -0.55 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[ORC3]] | -0.55 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[GPR89B]] | -0.54 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[GPR89A]] | -0.54 | -0.60 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AJUBA-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises AJUBA-DT's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without SYT9-AS1 | 0.016 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.9, 25.3); signed map (36.9, -5.7). **Vector** length 56.3, 8.48% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +19.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | AJUBA divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:22,982,698-22,999,078 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55449) · Entrez [107984660](https://www.ncbi.nlm.nih.gov/gene/107984660) · Ensembl [ENSG00000258457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258457)

## Data

Gene col 15103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15103); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15103]; `tensor/DDL_lfc|DDL_z.npy` [15103]; `embed/gene_vectors.npy` [15103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15103 or target_col == 15103). Every well: [[AJUBA-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AJUBA-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
