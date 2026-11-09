---
symbol: "RN7SL1"
type: "gene"
col: 15869
ensembl_id: "ENSG00000276168"
name: "RNA component of signal recognition particle 7SL1"
location: "14q21.3"
module: 21
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RN7SL1

*RNA component of signal recognition particle 7SL1* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.87× (z +11.1, q 6e-26, up in 20 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +5.6, q 2e-06, up in 22 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfatinib (drug)]] 0.05 µM in 1 line (LoVo 0.0723×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.91, fdr 7e-06), [[TICAM2-AS1]] (+0.87, fdr 7e-06), [[FAM217A]] (+0.86, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.87×** | +11.1 | 6e-26 | 20/21 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +10.3 | 3e-22 | 4/5 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +9.1 | 2e-17 | 5/7 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +6.7 | 2e-09 | 19/34 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.15×** | +6.3 | 3e-08 | 13/22 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 22/37 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.72×** | +4.3 | 0.001 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.44×** | +4.2 | 0.002 | 10/36 (LOX-IMVI, Hs 766T, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.010 | 13/35 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.026 | 3/21 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.028 | 5/42 (HS-578T, A-427, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +3.4 | 0.028 | 2/42 (A498, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.064 | 9/32 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.065 | 6/44 (RKO, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.069 | 9/43 (LoVo, NCI-H2030, …) | two highest doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfatinib (drug)]] 0.05 µM in 1 line (LoVo 0.0723×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.28 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0723× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 3.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.91 | +0.85 / +0.89 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.87 | +0.78 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FAM217A]] | +0.86 | +0.70 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[ZRANB2-AS1]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.84 | +0.71 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[LRRC37A16P]] | +0.82 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.81 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.81 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.81 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.81 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.80 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RN7SL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KIAA2012]] | C | KIAA2012 activity raises RN7SL1's level | lines that do not express KIAA2012 (3) vs lines expressing it (47) | 1.20× lower at baseline in the lines without KIAA2012 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OPN3, SMAD7, TESK2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 28.5); signed map (34.3, 5.5). **Vector** length 39.3, 3.85% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +9.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA component of signal recognition particle 7SL1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q21.3 — chr14:49,586,580-49,586,878 (+) |
| Ensembl biotype | misc_RNA |
| Also known as | 7SL, 7L1a, RNSRP1; previously RN7SL |
| Gene groups (HGNC) | Signal recognition particle; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [6029](https://www.ncbi.nlm.nih.gov/gene/6029):

> The signal recognition particle (SRP) is a cytoplasmic ribonucleoprotein complex that mediates cotranslational insertion of secretory proteins into the lumen of the endoplasmic reticulum. The SRP consists of 6 polypeptides (e.g., SRP19; MIM 182175) and a 7SL RNA molecule, such as RN7SL1, that is partially homologous to Alu DNA (Ullu and Weiner, 1984 [PubMed 6084597]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:10038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10038) · Entrez [6029](https://www.ncbi.nlm.nih.gov/gene/6029) · Ensembl [ENSG00000276168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276168)

## Data

Gene col 15869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15869); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15869]; `tensor/DDL_lfc|DDL_z.npy` [15869]; `embed/gene_vectors.npy` [15869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15869 or target_col == 15869). Every well: [[RN7SL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RN7SL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
