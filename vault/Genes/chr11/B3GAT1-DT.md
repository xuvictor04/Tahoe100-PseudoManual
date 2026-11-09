---
symbol: "B3GAT1-DT"
type: "gene"
col: 14946
ensembl_id: "ENSG00000255545"
name: "B3GAT1 divergent transcript"
location: "11q25"
module: 27
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# B3GAT1-DT

*B3GAT1 divergent transcript* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.10× (z +11.9, q 1e-29, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.48× (z +10.4, q 9e-23, up in 2 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.425× (z -5.1, q 2e-04, down in 3 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNE3]] (+0.82, fdr 7e-06), [[LINC02058]] (+0.81, fdr 7e-06), [[CHDH]] (+0.79, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RIMBP2]] → it (grade C ⚠); 2 go from it, the strongest it → [[ERICH2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.10×** | +11.9 | 1e-29 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +10.4 | 9e-23 | 2/8 (HEC-1-A, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.86×** | +8.3 | 1e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +7.8 | 8e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.46×** | +5.3 | 1e-05 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.6 | 4e-04 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.96×** | +4.6 | 4e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.002 | 2/13 (HOP62, C-33 A) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.2 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.0 | 0.004 | 1/4 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.012 | 3/9 (COLO 205, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.88×** | +3.6 | 0.017 | 1/8 (SW480) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.73×** | +3.2 | 0.056 | 5/11 (SW480, COLO 205, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.76×** | +3.2 | 0.056 | 0/6 | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.057 | 1/5 (A-172) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.03×** | +3.0 | 0.096 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.096 | 4/13 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.425×** | -5.1 | 2e-04 | 3/13 (SW 1271, HOP62, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.461×** | -4.4 | 0.003 | 7/14 (HOP62, SW480, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.511×** | -3.6 | 0.068 | 2/13 (HEC-1-A, SW 1271) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.581× | -3.2 | 0.18 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.7 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0503× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.2) |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0312× (z -16.8) |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0541× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -10.4) |
| [[SW1417 (line)]] | alt | 6.83 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0734× (z -9.0) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNE3]] | +0.82 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02058]] | +0.81 | +0.68 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CHDH]] | +0.79 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.77 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.75 | +0.77 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[FGD3]] | +0.75 | +0.81 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PKHD1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[A1CF]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01622]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SMOC2]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[VWA2]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMBP2]] | C | RIMBP2 activity raises B3GAT1-DT's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without RIMBP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[C9orf152]] | C | C9orf152 activity raises B3GAT1-DT's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without C9orf152 | 0.066 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises B3GAT1-DT's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.26× lower at baseline in the lines without PROM1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERICH2-DT]] | B | B3GAT1-DT activity raises ERICH2-DT's level | lines that do not express B3GAT1-DT (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without B3GAT1-DT | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000213981, HEPHL1, ENSG00000287069 |
| [[ITGA9-AS1]] | B | B3GAT1-DT activity raises ITGA9-AS1's level | lines that do not express B3GAT1-DT (33) vs lines expressing it (17) | 1.59× lower at baseline in the lines without B3GAT1-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000213981, HEPHL1, ENSG00000287069 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 44.9); signed map (61.9, 15.1). **Vector** length 44.3, 14.7% of its response variance represented; |z| ≥ 3 in 392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +10.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -5.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | B3GAT1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q25 — chr11:134,412,284-134,505,665 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC283177, AP004608.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27449) · Entrez [283177](https://www.ncbi.nlm.nih.gov/gene/283177) · Ensembl [ENSG00000255545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255545)

## Data

Gene col 14946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14946); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14946]; `tensor/DDL_lfc|DDL_z.npy` [14946]; `embed/gene_vectors.npy` [14946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14946 or target_col == 14946). Every well: [[B3GAT1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GAT1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
