---
symbol: "EAF1-AS1"
type: "gene"
col: 14636
ensembl_id: "ENSG00000249786"
name: "EAF1 antisense RNA 1"
location: "3p25.1"
module: 21
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EAF1-AS1

*EAF1 antisense RNA 1* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +9.5, q 8e-19, up in 24 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (NCI-H460 0.0722×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB14]] (+0.84, fdr 7e-06), [[SPATC1]] (+0.84, fdr 7e-06), [[HSPA2-AS1]] (+0.80, fdr 7e-06); moves opposite to [[ICMT]] (-0.62, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +9.5 | 8e-19 | 24/34 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +9.2 | 1e-17 | 7/11 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +8.9 | 1e-16 | 3/3 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 4e-09 | 20/33 (NCI-H2347, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +5.6 | 3e-06 | 15/42 (HS-578T, RPMI-7951, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.0 | 6e-05 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +4.9 | 6e-05 | 3/12 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.69×** | +4.5 | 3e-04 | 8/27 (NCI-H2030, NCI-H460, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 3e-04 | 7/30 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 3e-04 | 12/34 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.5 | 4e-04 | 5/33 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.4 | 4e-04 | 3/15 (Hs 766T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.003 | 8/29 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.009 | 4/43 (CFPAC-1, C-33 A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.009 | 7/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.019 | 4/45 (SW1417, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.039 | 2/43 (C-33 A, C32) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.063 | 5/43 (SNU-423, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.064 | 5/39 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.080 | 5/38 (J82, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14636.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (NCI-H460 0.0722×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.834× | -5.5 | 2e-05 | 27/48 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.692× | -3.0 | 0.70 | 7/43 (PANC-1, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.26 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0722× (z -9.2) |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB14]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.80 | +0.78 / +0.72 | both halves | 7e-06 | same gene group |
| [[PKD2L2]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[C1orf56]] | +0.77 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.76 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.75 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 | same gene group |
| [[VPS39-DT]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.74 | +0.64 / +0.74 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICMT]] | -0.62 | -0.56 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 26.7); signed map (32.1, 6.0). **Vector** length 34.0, 3.04% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EAF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.1 — chr3:15,436,171-15,449,994 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42328) · Entrez [100873956](https://www.ncbi.nlm.nih.gov/gene/100873956) · Ensembl [ENSG00000249786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249786)

## Data

Gene col 14636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14636); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14636]; `tensor/DDL_lfc|DDL_z.npy` [14636]; `embed/gene_vectors.npy` [14636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14636 or target_col == 14636). Every well: [[EAF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EAF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
